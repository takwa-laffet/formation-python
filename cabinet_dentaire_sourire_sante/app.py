from functools import wraps

from flask import Flask, flash, redirect, render_template, request, session, url_for
from werkzeug.security import check_password_hash, generate_password_hash

from config import Config
from db import get_connection


app = Flask(__name__)
app.config.from_object(Config)


VALID_ROLES = {"admin", "secretaire", "dentiste"}
VALID_APPOINTMENT_STATUSES = {"Confirme", "Annule", "Realise"}


def login_required(view_func):
    @wraps(view_func)
    def wrapped(*args, **kwargs):
        if "user_id" not in session:
            flash("Veuillez vous connecter.", "warning")
            return redirect(url_for("login"))
        return view_func(*args, **kwargs)

    return wrapped


def roles_required(*allowed_roles):
    def decorator(view_func):
        @wraps(view_func)
        def wrapped(*args, **kwargs):
            role = session.get("role")
            if role not in allowed_roles:
                flash("Acces non autorise pour votre role.", "danger")
                return redirect(url_for("index"))
            return view_func(*args, **kwargs)

        return wrapped

    return decorator


def get_current_dentist_id():
    user_id = session.get("user_id")
    if not user_id:
        return None

    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT id FROM dentists WHERE user_id = %s", (user_id,))
    dentist = cursor.fetchone()
    cursor.close()
    conn.close()
    return dentist["id"] if dentist else None


@app.route("/")
def home():
    if "user_id" in session:
        return redirect(url_for("index"))
    return redirect(url_for("login"))


@app.route("/signup", methods=["GET", "POST"])
def signup():
    if request.method == "POST":
        full_name = request.form.get("full_name", "").strip()
        email = request.form.get("email", "").strip().lower()
        password = request.form.get("password", "")
        role = request.form.get("role", "").strip().lower()

        if not full_name or not email or not password or role not in VALID_ROLES:
            flash("Tous les champs sont obligatoires et le role doit etre valide.", "danger")
            return render_template("signup.html")

        conn = get_connection()
        cursor = conn.cursor(dictionary=True)

        cursor.execute("SELECT id FROM users WHERE email = %s", (email,))
        existing_user = cursor.fetchone()
        if existing_user:
            cursor.close()
            conn.close()
            flash("Cet email est deja utilise.", "warning")
            return render_template("signup.html")

        password_hash = generate_password_hash(password)
        cursor.execute(
            """
            INSERT INTO users (full_name, email, password_hash, role)
            VALUES (%s, %s, %s, %s)
            """,
            (full_name, email, password_hash, role),
        )
        user_id = cursor.lastrowid

        if role == "dentiste":
            cursor.execute(
                """
                INSERT INTO dentists (full_name, speciality, email, phone, user_id)
                VALUES (%s, %s, %s, %s, %s)
                """,
                (full_name, "Generaliste", email, "", user_id),
            )

        conn.commit()
        cursor.close()
        conn.close()

        flash("Compte cree avec succes. Connectez-vous.", "success")
        return redirect(url_for("login"))

    return render_template("signup.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form.get("email", "").strip().lower()
        password = request.form.get("password", "")

        conn = get_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM users WHERE email = %s", (email,))
        user = cursor.fetchone()
        cursor.close()
        conn.close()

        if not user or not check_password_hash(user["password_hash"], password):
            flash("Email ou mot de passe invalide.", "danger")
            return render_template("login.html")

        session["user_id"] = user["id"]
        session["full_name"] = user["full_name"]
        session["role"] = user["role"]

        flash("Connexion reussie.", "success")
        return redirect(url_for("index"))

    return render_template("login.html")


@app.route("/logout")
@login_required
def logout():
    session.clear()
    flash("Vous etes deconnecte.", "info")
    return redirect(url_for("login"))


@app.route("/index")
@login_required
def index():
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)

    cursor.execute("SELECT COUNT(*) AS total FROM patients")
    total_patients = cursor.fetchone()["total"]

    cursor.execute("SELECT COUNT(*) AS total FROM dentists")
    total_dentists = cursor.fetchone()["total"]

    cursor.execute("SELECT COUNT(*) AS total FROM appointments")
    total_appointments = cursor.fetchone()["total"]

    cursor.close()
    conn.close()

    return render_template(
        "index.html",
        total_patients=total_patients,
        total_dentists=total_dentists,
        total_appointments=total_appointments,
    )


@app.route("/patients")
@login_required
@roles_required("admin", "secretaire", "dentiste")
def patients():
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM patients ORDER BY id DESC")
    data = cursor.fetchall()
    cursor.close()
    conn.close()
    return render_template("patients.html", patients=data)


@app.route("/patients/add", methods=["GET", "POST"])
@login_required
@roles_required("admin", "secretaire")
def add_patient():
    if request.method == "POST":
        full_name = request.form.get("full_name", "").strip()
        birth_date = request.form.get("birth_date", "").strip()
        phone = request.form.get("phone", "").strip()
        email = request.form.get("email", "").strip().lower()

        if not full_name or not birth_date:
            flash("Le nom et la date de naissance sont obligatoires.", "danger")
            return render_template("add_patient.html")

        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(
            """
            INSERT INTO patients (full_name, birth_date, phone, email)
            VALUES (%s, %s, %s, %s)
            """,
            (full_name, birth_date, phone, email),
        )
        conn.commit()
        cursor.close()
        conn.close()

        flash("Patient ajoute avec succes.", "success")
        return redirect(url_for("patients"))

    return render_template("add_patient.html")


@app.route("/patients/edit/<int:patient_id>", methods=["GET", "POST"])
@login_required
@roles_required("admin", "secretaire")
def edit_patient(patient_id):
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)

    if request.method == "POST":
        full_name = request.form.get("full_name", "").strip()
        birth_date = request.form.get("birth_date", "").strip()
        phone = request.form.get("phone", "").strip()
        email = request.form.get("email", "").strip().lower()

        if not full_name or not birth_date:
            cursor.close()
            conn.close()
            flash("Le nom et la date de naissance sont obligatoires.", "danger")
            return redirect(url_for("edit_patient", patient_id=patient_id))

        cursor.execute(
            """
            UPDATE patients
            SET full_name = %s, birth_date = %s, phone = %s, email = %s
            WHERE id = %s
            """,
            (full_name, birth_date, phone, email, patient_id),
        )
        conn.commit()
        cursor.close()
        conn.close()

        flash("Patient mis a jour avec succes.", "success")
        return redirect(url_for("patients"))

    cursor.execute("SELECT * FROM patients WHERE id = %s", (patient_id,))
    patient = cursor.fetchone()
    cursor.close()
    conn.close()

    if not patient:
        flash("Patient introuvable.", "warning")
        return redirect(url_for("patients"))

    return render_template("edit_patient.html", patient=patient)


@app.route("/patients/delete/<int:patient_id>", methods=["POST"])
@login_required
@roles_required("admin", "secretaire")
def delete_patient(patient_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM patients WHERE id = %s", (patient_id,))
    conn.commit()
    cursor.close()
    conn.close()

    flash("Patient supprime.", "info")
    return redirect(url_for("patients"))


@app.route("/dentists")
@login_required
@roles_required("admin", "secretaire", "dentiste")
def dentists():
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM dentists ORDER BY id DESC")
    data = cursor.fetchall()
    cursor.close()
    conn.close()
    return render_template("dentists.html", dentists=data)


@app.route("/dentists/add", methods=["GET", "POST"])
@login_required
@roles_required("admin")
def add_dentist():
    if request.method == "POST":
        full_name = request.form.get("full_name", "").strip()
        speciality = request.form.get("speciality", "").strip()
        email = request.form.get("email", "").strip().lower()
        phone = request.form.get("phone", "").strip()

        if not full_name or not email:
            flash("Le nom et l'email sont obligatoires.", "danger")
            return render_template("add_dentist.html")

        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(
            """
            INSERT INTO dentists (full_name, speciality, email, phone)
            VALUES (%s, %s, %s, %s)
            """,
            (full_name, speciality, email, phone),
        )
        conn.commit()
        cursor.close()
        conn.close()

        flash("Dentiste ajoute avec succes.", "success")
        return redirect(url_for("dentists"))

    return render_template("add_dentist.html")


@app.route("/dentists/edit/<int:dentist_id>", methods=["GET", "POST"])
@login_required
@roles_required("admin")
def edit_dentist(dentist_id):
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)

    if request.method == "POST":
        full_name = request.form.get("full_name", "").strip()
        speciality = request.form.get("speciality", "").strip()
        email = request.form.get("email", "").strip().lower()
        phone = request.form.get("phone", "").strip()

        if not full_name or not email:
            cursor.close()
            conn.close()
            flash("Le nom et l'email sont obligatoires.", "danger")
            return redirect(url_for("edit_dentist", dentist_id=dentist_id))

        cursor.execute(
            """
            UPDATE dentists
            SET full_name = %s, speciality = %s, email = %s, phone = %s
            WHERE id = %s
            """,
            (full_name, speciality, email, phone, dentist_id),
        )
        conn.commit()
        cursor.close()
        conn.close()

        flash("Dentiste mis a jour avec succes.", "success")
        return redirect(url_for("dentists"))

    cursor.execute("SELECT * FROM dentists WHERE id = %s", (dentist_id,))
    dentist = cursor.fetchone()
    cursor.close()
    conn.close()

    if not dentist:
        flash("Dentiste introuvable.", "warning")
        return redirect(url_for("dentists"))

    return render_template("edit_dentist.html", dentist=dentist)


@app.route("/dentists/delete/<int:dentist_id>", methods=["POST"])
@login_required
@roles_required("admin")
def delete_dentist(dentist_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM dentists WHERE id = %s", (dentist_id,))
    conn.commit()
    cursor.close()
    conn.close()

    flash("Dentiste supprime.", "info")
    return redirect(url_for("dentists"))


@app.route("/appointments")
@login_required
@roles_required("admin", "secretaire", "dentiste")
def appointments():
    date_filter = request.args.get("date", "").strip()

    conn = get_connection()
    cursor = conn.cursor(dictionary=True)

    base_query = """
        SELECT
            a.id,
            p.full_name AS patient_name,
            d.full_name AS dentist_name,
            a.appointment_datetime,
            a.status,
            a.patient_id,
            a.dentist_id
        FROM appointments a
        JOIN patients p ON p.id = a.patient_id
        JOIN dentists d ON d.id = a.dentist_id
    """
    conditions = []
    params = []

    if session.get("role") == "dentiste":
        current_dentist_id = get_current_dentist_id()
        if current_dentist_id:
            conditions.append("a.dentist_id = %s")
            params.append(current_dentist_id)
        else:
            # Dentiste sans profil associe: ne rien afficher.
            conditions.append("1 = 0")

    if date_filter:
        conditions.append("DATE(a.appointment_datetime) = %s")
        params.append(date_filter)

    if conditions:
        base_query += " WHERE " + " AND ".join(conditions)

    base_query += " ORDER BY a.appointment_datetime ASC"

    cursor.execute(base_query, tuple(params))
    data = cursor.fetchall()
    cursor.close()
    conn.close()

    return render_template("appointments.html", appointments=data, date_filter=date_filter)


@app.route("/appointments/add", methods=["GET", "POST"])
@login_required
@roles_required("admin", "secretaire")
def add_appointment():
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)

    cursor.execute("SELECT id, full_name FROM patients ORDER BY full_name")
    patients_data = cursor.fetchall()
    cursor.execute("SELECT id, full_name FROM dentists ORDER BY full_name")
    dentists_data = cursor.fetchall()

    if request.method == "POST":
        patient_id = request.form.get("patient_id", "").strip()
        dentist_id = request.form.get("dentist_id", "").strip()
        appointment_datetime = request.form.get("appointment_datetime", "").strip()
        status = request.form.get("status", "Confirme").strip()

        if (
            not patient_id
            or not dentist_id
            or not appointment_datetime
            or status not in VALID_APPOINTMENT_STATUSES
        ):
            cursor.close()
            conn.close()
            flash("Tous les champs sont obligatoires et le statut doit etre valide.", "danger")
            return render_template(
                "add_appointment.html",
                patients=patients_data,
                dentists=dentists_data,
                status_choices=sorted(VALID_APPOINTMENT_STATUSES),
            )

        cursor = conn.cursor()
        cursor.execute(
            """
            INSERT INTO appointments (patient_id, dentist_id, appointment_datetime, status)
            VALUES (%s, %s, %s, %s)
            """,
            (patient_id, dentist_id, appointment_datetime, status),
        )
        conn.commit()
        cursor.close()
        conn.close()

        flash("Rendez-vous ajoute avec succes.", "success")
        return redirect(url_for("appointments"))

    cursor.close()
    conn.close()
    return render_template(
        "add_appointment.html",
        patients=patients_data,
        dentists=dentists_data,
        status_choices=sorted(VALID_APPOINTMENT_STATUSES),
    )


@app.route("/appointments/edit/<int:appointment_id>", methods=["GET", "POST"])
@login_required
@roles_required("admin", "secretaire", "dentiste")
def edit_appointment(appointment_id):
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)

    cursor.execute("SELECT id, full_name FROM patients ORDER BY full_name")
    patients_data = cursor.fetchall()
    cursor.execute("SELECT id, full_name FROM dentists ORDER BY full_name")
    dentists_data = cursor.fetchall()

    cursor.execute("SELECT * FROM appointments WHERE id = %s", (appointment_id,))
    appointment = cursor.fetchone()

    if not appointment:
        cursor.close()
        conn.close()
        flash("Rendez-vous introuvable.", "warning")
        return redirect(url_for("appointments"))

    if request.method == "POST":
        patient_id = request.form.get("patient_id", "").strip()
        dentist_id = request.form.get("dentist_id", "").strip()
        appointment_datetime = request.form.get("appointment_datetime", "").strip()
        status = request.form.get("status", "").strip()

        if (
            not patient_id
            or not dentist_id
            or not appointment_datetime
            or status not in VALID_APPOINTMENT_STATUSES
        ):
            cursor.close()
            conn.close()
            flash("Tous les champs sont obligatoires et le statut doit etre valide.", "danger")
            return redirect(url_for("edit_appointment", appointment_id=appointment_id))

        # Un dentiste ne peut modifier que ses propres rendez-vous.
        if session.get("role") == "dentiste":
            current_dentist_id = get_current_dentist_id()
            if not current_dentist_id or appointment["dentist_id"] != current_dentist_id:
                cursor.close()
                conn.close()
                flash("Vous ne pouvez modifier que vos propres rendez-vous.", "danger")
                return redirect(url_for("appointments"))

        cursor = conn.cursor()
        cursor.execute(
            """
            UPDATE appointments
            SET patient_id = %s,
                dentist_id = %s,
                appointment_datetime = %s,
                status = %s
            WHERE id = %s
            """,
            (patient_id, dentist_id, appointment_datetime, status, appointment_id),
        )
        conn.commit()
        cursor.close()
        conn.close()

        flash("Rendez-vous mis a jour avec succes.", "success")
        return redirect(url_for("appointments"))

    cursor.close()
    conn.close()

    return render_template(
        "edit_appointment.html",
        appointment=appointment,
        patients=patients_data,
        dentists=dentists_data,
        status_choices=sorted(VALID_APPOINTMENT_STATUSES),
    )


@app.route("/appointments/delete/<int:appointment_id>", methods=["POST"])
@login_required
@roles_required("admin", "secretaire")
def delete_appointment(appointment_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM appointments WHERE id = %s", (appointment_id,))
    conn.commit()
    cursor.close()
    conn.close()

    flash("Rendez-vous supprime.", "info")
    return redirect(url_for("appointments"))


if __name__ == "__main__":
    app.run(debug=True)
