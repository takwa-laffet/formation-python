# Import necessary Flask and security tools
from functools import wraps
from flask import Flask, flash, redirect, render_template, request, session, url_for
from werkzeug.security import check_password_hash, generate_password_hash

# Import app configuration and database connection
from config import Config
from db import get_connection

# Create Flask app and load configuration
app = Flask(__name__)
app.config.from_object(Config)

# Define valid user roles in the system
VALID_ROLES = {"admin", "secretaire", "dentiste"}

# Define valid appointment statuses
VALID_APPOINTMENT_STATUSES = {"Confirme", "Annule", "Realise"}

# =============================================================================
# DECORATORS: Functions that protect routes by checking permissions
# =============================================================================

# Decorator: Ensure user is logged in before accessing a route
def login_required(view_func):
    """Check if user_id is in session. If not, redirect to login page."""
    @wraps(view_func)
    def wrapped(*args, **kwargs):
        if "user_id" not in session:
            flash("Veuillez vous connecter.", "warning")
            return redirect(url_for("login"))
        return view_func(*args, **kwargs)
    return wrapped


# Decorator: Check if user has required role to access a route
def roles_required(*allowed_roles):
    """Check if user's role matches one of the allowed_roles."""
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

# =============================================================================
# HELPER FUNCTION: Get current dentist
# =============================================================================

def get_current_dentist_id():
    """
    Get the dentist ID for the logged-in user.
    Returns the dentist ID if user is a dentist, None otherwise.
    """
    user_id = session.get("user_id")
    if not user_id:
        return None

    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    # Query the dentists table to find the dentist associated with this user
    cursor.execute("SELECT id FROM dentists WHERE user_id = %s", (user_id,))
    dentist = cursor.fetchone()
    cursor.close()
    conn.close()
    return dentist["id"] if dentist else None


# =============================================================================
# AUTHENTICATION ROUTES: Login, Signup, Logout
# =============================================================================

# Route: Home page - redirect logged in users to index, others to login
@app.route("/")
def home():
    """If user is logged in, go to dashboard. Otherwise go to login page."""
    if "user_id" in session:
        return redirect(url_for("index"))
    return redirect(url_for("login"))


# Route: User registration / Signup
@app.route("/signup", methods=["GET", "POST"])
def signup():
    """
    Handle user registration:
    - GET: Show signup form
    - POST: Create new user account
    """
    if request.method == "POST":
        # Get form data and clean it (strip whitespace)
        full_name = request.form.get("full_name", "").strip()
        email = request.form.get("email", "").strip().lower()
        password = request.form.get("password", "")
        role = request.form.get("role", "").strip().lower()

        # Validate all required fields are provided
        if not full_name or not email or not password or role not in VALID_ROLES:
            flash("Tous les champs sont obligatoires et le role doit etre valide.", "danger")
            return render_template("signup.html")

        conn = get_connection()
        cursor = conn.cursor(dictionary=True)

        # Check if email already exists (prevent duplicate accounts)
        cursor.execute("SELECT id FROM users WHERE email = %s", (email,))
        existing_user = cursor.fetchone()
        if existing_user:
            cursor.close()
            conn.close()
            flash("Cet email est deja utilise.", "warning")
            return render_template("signup.html")

        # Hash password for security (never store plain passwords)
        password_hash = generate_password_hash(password)
        
        # Insert new user into the database
        cursor.execute(
            """
            INSERT INTO users (full_name, email, password_hash, role)
            VALUES (%s, %s, %s, %s)
            """,
            (full_name, email, password_hash, role),
        )
        user_id = cursor.lastrowid  # Get the newly created user's ID

        # If user is a dentist, also create their dentist profile
        if role == "dentiste":
            cursor.execute(
                """
                INSERT INTO dentists (full_name, speciality, email, phone, user_id)
                VALUES (%s, %s, %s, %s, %s)
                """,
                (full_name, "Generaliste", email, "", user_id),
            )

        conn.commit()  # Save all changes to database
        cursor.close()
        conn.close()

        flash("Compte cree avec succes. Connectez-vous.", "success")
        return redirect(url_for("login"))

    # If GET request, just show the signup form
    return render_template("signup.html")


# Route: User login
@app.route("/login", methods=["GET", "POST"])
def login():
    """
    Handle user login:
    - GET: Show login form
    - POST: Authenticate user and create session
    """
    if request.method == "POST":
        # Get login credentials from form
        email = request.form.get("email", "").strip().lower()
        password = request.form.get("password", "")

        conn = get_connection()
        cursor = conn.cursor(dictionary=True)
        
        # Find user by email in database
        cursor.execute("SELECT * FROM users WHERE email = %s", (email,))
        user = cursor.fetchone()
        cursor.close()
        conn.close()

        # Check if user exists AND password is correct
        if not user or not check_password_hash(user["password_hash"], password):
            flash("Email ou mot de passe invalide.", "danger")
            return render_template("login.html")

        # Create session for the logged-in user
        session["user_id"] = user["id"]
        session["full_name"] = user["full_name"]
        session["role"] = user["role"]

        flash("Connexion reussie.", "success")
        return redirect(url_for("index"))

    # If GET request, just show the login form
    return render_template("login.html")


# Route: User logout
@app.route("/logout")
@login_required  # Only logged-in users can logout
def logout():
    """Clear session data and redirect to login page."""
    session.clear()
    flash("Vous etes deconnecte.", "info")
    return redirect(url_for("login"))


# =============================================================================
# DASHBOARD ROUTE: Shows statistics
# =============================================================================

@app.route("/index")
@login_required  # User must be logged in
def index():
    """
    Dashboard page showing:
    - Total number of patients
    - Total number of dentists
    - Total number of appointments
    """
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)

    # Count total patients
    cursor.execute("SELECT COUNT(*) AS total FROM patients")
    total_patients = cursor.fetchone()["total"]

    # Count total dentists
    cursor.execute("SELECT COUNT(*) AS total FROM dentists")
    total_dentists = cursor.fetchone()["total"]

    # Count total appointments
    cursor.execute("SELECT COUNT(*) AS total FROM appointments")
    total_appointments = cursor.fetchone()["total"]

    cursor.close()
    conn.close()

    # Pass statistics to the template
    return render_template(
        "index.html",
        total_patients=total_patients,
        total_dentists=total_dentists,
        total_appointments=total_appointments,
    )


# =============================================================================
# PATIENT MANAGEMENT ROUTES
# =============================================================================

# Route: List all patients
@app.route("/patients")
@login_required
@roles_required("admin", "secretaire", "dentiste")
def patients():
    """Display all patients in a table."""
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    
    # Get all patients from database, sorted by newest first
    cursor.execute("SELECT * FROM patients ORDER BY id DESC")
    data = cursor.fetchall()
    cursor.close()
    conn.close()
    
    return render_template("patients.html", patients=data)


# Route: Add a new patient
@app.route("/patients/add", methods=["GET", "POST"])
@login_required
@roles_required("admin", "secretaire")  # Only admin and secretaire can add patients
def add_patient():
    """
    Add a new patient:
    - GET: Show add patient form
    - POST: Save new patient to database
    """
    if request.method == "POST":
        # Get form data
        full_name = request.form.get("full_name", "").strip()
        birth_date = request.form.get("birth_date", "").strip()
        phone = request.form.get("phone", "").strip()
        email = request.form.get("email", "").strip().lower()

        # Validate required fields
        if not full_name or not birth_date:
            flash("Le nom et la date de naissance sont obligatoires.", "danger")
            return render_template("add_patient.html")

        # Insert new patient into database
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

    # If GET request, show the form
    return render_template("add_patient.html")


# Route: Edit existing patient
@app.route("/patients/edit/<int:patient_id>", methods=["GET", "POST"])
@login_required
@roles_required("admin", "secretaire")
def edit_patient(patient_id):
    """
    Edit patient information:
    - GET: Show edit form with current patient data
    - POST: Update patient in database
    """
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)

    if request.method == "POST":
        # Get updated form data
        full_name = request.form.get("full_name", "").strip()
        birth_date = request.form.get("birth_date", "").strip()
        phone = request.form.get("phone", "").strip()
        email = request.form.get("email", "").strip().lower()

        # Validate required fields
        if not full_name or not birth_date:
            cursor.close()
            conn.close()
            flash("Le nom et la date de naissance sont obligatoires.", "danger")
            return redirect(url_for("edit_patient", patient_id=patient_id))

        # Update patient in database
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

    # Get the patient's current data to show in the form
    cursor.execute("SELECT * FROM patients WHERE id = %s", (patient_id,))
    patient = cursor.fetchone()
    cursor.close()
    conn.close()

    if not patient:
        flash("Patient introuvable.", "warning")
        return redirect(url_for("patients"))

    return render_template("edit_patient.html", patient=patient)


# Route: Delete a patient
@app.route("/patients/delete/<int:patient_id>", methods=["POST"])
@login_required
@roles_required("admin", "secretaire")
def delete_patient(patient_id):
    """Delete a patient from the database."""
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM patients WHERE id = %s", (patient_id,))
    conn.commit()
    cursor.close()
    conn.close()

    flash("Patient supprime.", "info")
    return redirect(url_for("patients"))


# =============================================================================
# DENTIST MANAGEMENT ROUTES
# =============================================================================

# Route: List all dentists
@app.route("/dentists")
@login_required
@roles_required("admin", "secretaire", "dentiste")
def dentists():
    """Display all dentists in a table."""
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM dentists ORDER BY id DESC")
    data = cursor.fetchall()
    cursor.close()
    conn.close()
    return render_template("dentists.html", dentists=data)


# Route: Add a new dentist
@app.route("/dentists/add", methods=["GET", "POST"])
@login_required
@roles_required("admin")  # Only admin can add dentists
def add_dentist():
    """
    Add a new dentist:
    - GET: Show add dentist form
    - POST: Save new dentist to database
    """
    if request.method == "POST":
        # Get form data
        full_name = request.form.get("full_name", "").strip()
        speciality = request.form.get("speciality", "").strip()
        email = request.form.get("email", "").strip().lower()
        phone = request.form.get("phone", "").strip()

        # Validate required fields
        if not full_name or not email:
            flash("Le nom et l'email sont obligatoires.", "danger")
            return render_template("add_dentist.html")

        # Insert new dentist into database
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

    # If GET request, show the form
    return render_template("add_dentist.html")


# Route: Edit existing dentist
@app.route("/dentists/edit/<int:dentist_id>", methods=["GET", "POST"])
@login_required
@roles_required("admin")
def edit_dentist(dentist_id):
    """
    Edit dentist information:
    - GET: Show edit form with current dentist data
    - POST: Update dentist in database
    """
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)

    if request.method == "POST":
        # Get updated form data
        full_name = request.form.get("full_name", "").strip()
        speciality = request.form.get("speciality", "").strip()
        email = request.form.get("email", "").strip().lower()
        phone = request.form.get("phone", "").strip()

        # Validate required fields
        if not full_name or not email:
            cursor.close()
            conn.close()
            flash("Le nom et l'email sont obligatoires.", "danger")
            return redirect(url_for("edit_dentist", dentist_id=dentist_id))

        # Update dentist in database
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

    # Get the dentist's current data to show in the form
    cursor.execute("SELECT * FROM dentists WHERE id = %s", (dentist_id,))
    dentist = cursor.fetchone()
    cursor.close()
    conn.close()

    if not dentist:
        flash("Dentiste introuvable.", "warning")
        return redirect(url_for("dentists"))

    return render_template("edit_dentist.html", dentist=dentist)


# Route: Delete a dentist
@app.route("/dentists/delete/<int:dentist_id>", methods=["POST"])
@login_required
@roles_required("admin")
def delete_dentist(dentist_id):
    """Delete a dentist from the database."""
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM dentists WHERE id = %s", (dentist_id,))
    conn.commit()
    cursor.close()
    conn.close()

    flash("Dentiste supprime.", "info")
    return redirect(url_for("dentists"))


# =============================================================================
# APPOINTMENT MANAGEMENT ROUTES
# =============================================================================

# Route: List all appointments (with optional date filter)
@app.route("/appointments")
@login_required
@roles_required("admin", "secretaire", "dentiste")
def appointments():
    """
    Display all appointments:
    - Admin/Secretaire see all appointments
    - Dentist only sees their own appointments
    - Can filter by date using URL parameter
    """
    # Get the date filter from URL if provided (e.g., /appointments?date=2024-01-15)
    date_filter = request.args.get("date", "").strip()

    conn = get_connection()
    cursor = conn.cursor(dictionary=True)

    # Build the SQL query to fetch appointments with patient and dentist names
    base_query = """
        SELECT
            a.id,
            p.full_name AS patient_name,
            d.full_name AS dentist_name,
            a.appointment_datetime,
            a.status,
            a.medical_description,
            a.patient_id,
            a.dentist_id
        FROM appointments a
        JOIN patients p ON p.id = a.patient_id
        JOIN dentists d ON d.id = a.dentist_id
    """
    conditions = []  # Store WHERE clause conditions
    params = []      # Store query parameters (safe from SQL injection)

    # If user is a dentist, only show their own appointments
    if session.get("role") == "dentiste":
        current_dentist_id = get_current_dentist_id()
        if current_dentist_id:
            conditions.append("a.dentist_id = %s")
            params.append(current_dentist_id)
        else:
            # Dentist without a profile - show nothing
            conditions.append("1 = 0")

    # If date filter is provided, add it to WHERE clause
    if date_filter:
        conditions.append("DATE(a.appointment_datetime) = %s")
        params.append(date_filter)

    # Add WHERE clause if there are conditions
    if conditions:
        base_query += " WHERE " + " AND ".join(conditions)

    # Sort by appointment date (earliest first)
    base_query += " ORDER BY a.appointment_datetime ASC"

    cursor.execute(base_query, tuple(params))
    data = cursor.fetchall()
    cursor.close()
    conn.close()

    return render_template("appointments.html", appointments=data, date_filter=date_filter)


# Route: Add a new appointment
@app.route("/appointments/add", methods=["GET", "POST"])
@login_required
@roles_required("admin", "secretaire")  # Only admin and secretaire can add appointments
def add_appointment():
    """
    Add a new appointment:
    - GET: Show form with patient and dentist lists
    - POST: Save new appointment with medical description
    """
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)

    # Get list of all patients for dropdown
    cursor.execute("SELECT id, full_name FROM patients ORDER BY full_name")
    patients_data = cursor.fetchall()
    
    # Get list of all dentists for dropdown
    cursor.execute("SELECT id, full_name FROM dentists ORDER BY full_name")
    dentists_data = cursor.fetchall()

    if request.method == "POST":
        # Get form data
        patient_id = request.form.get("patient_id", "").strip()
        dentist_id = request.form.get("dentist_id", "").strip()
        appointment_datetime = request.form.get("appointment_datetime", "").strip()
        status = request.form.get("status", "Confirme").strip()
        medical_description = request.form.get("medical_description", "").strip()

        # Validate required fields
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

        # Insert new appointment into database
        cursor = conn.cursor()
        cursor.execute(
            """
            INSERT INTO appointments (patient_id, dentist_id, appointment_datetime, status, medical_description)
            VALUES (%s, %s, %s, %s, %s)
            """,
            (patient_id, dentist_id, appointment_datetime, status, medical_description),
        )
        conn.commit()
        cursor.close()
        conn.close()

        flash("Rendez-vous ajoute avec succes.", "success")
        return redirect(url_for("appointments"))

    # If GET request, show the form
    cursor.close()
    conn.close()
    return render_template(
        "add_appointment.html",
        patients=patients_data,
        dentists=dentists_data,
        status_choices=sorted(VALID_APPOINTMENT_STATUSES),
    )


# Route: Edit existing appointment
@app.route("/appointments/edit/<int:appointment_id>", methods=["GET", "POST"])
@login_required
@roles_required("admin", "secretaire", "dentiste")
def edit_appointment(appointment_id):
    """
    Edit appointment information:
    - GET: Show edit form with current appointment data
    - POST: Update appointment in database
    - Dentists can only edit their own appointments
    """
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)

    # Get list of all patients for dropdown
    cursor.execute("SELECT id, full_name FROM patients ORDER BY full_name")
    patients_data = cursor.fetchall()
    
    # Get list of all dentists for dropdown
    cursor.execute("SELECT id, full_name FROM dentists ORDER BY full_name")
    dentists_data = cursor.fetchall()

    # Get the appointment data
    cursor.execute("SELECT * FROM appointments WHERE id = %s", (appointment_id,))
    appointment = cursor.fetchone()

    # Check if appointment exists
    if not appointment:
        cursor.close()
        conn.close()
        flash("Rendez-vous introuvable.", "warning")
        return redirect(url_for("appointments"))

    if request.method == "POST":
        # Get updated form data
        patient_id = request.form.get("patient_id", "").strip()
        dentist_id = request.form.get("dentist_id", "").strip()
        appointment_datetime = request.form.get("appointment_datetime", "").strip()
        status = request.form.get("status", "").strip()
        medical_description = request.form.get("medical_description", "").strip()

        # Validate required fields
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

        # Check if dentist is only editing their own appointment
        if session.get("role") == "dentiste":
            current_dentist_id = get_current_dentist_id()
            if not current_dentist_id or appointment["dentist_id"] != current_dentist_id:
                cursor.close()
                conn.close()
                flash("Vous ne pouvez modifier que vos propres rendez-vous.", "danger")
                return redirect(url_for("appointments"))

        # Update appointment in database
        cursor = conn.cursor()
        cursor.execute(
            """
            UPDATE appointments
            SET patient_id = %s,
                dentist_id = %s,
                appointment_datetime = %s,
                status = %s,
                medical_description = %s
            WHERE id = %s
            """,
            (patient_id, dentist_id, appointment_datetime, status, medical_description, appointment_id),
        )
        conn.commit()
        cursor.close()
        conn.close()

        flash("Rendez-vous mis a jour avec succes.", "success")
        return redirect(url_for("appointments"))

    # If GET request, show the form with current data
    cursor.close()
    conn.close()

    return render_template(
        "edit_appointment.html",
        appointment=appointment,
        patients=patients_data,
        dentists=dentists_data,
        status_choices=sorted(VALID_APPOINTMENT_STATUSES),
    )


# Route: Delete an appointment
@app.route("/appointments/delete/<int:appointment_id>", methods=["POST"])
@login_required
@roles_required("admin", "secretaire")
def delete_appointment(appointment_id):
    """Delete an appointment from the database."""
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM appointments WHERE id = %s", (appointment_id,))
    conn.commit()
    cursor.close()
    conn.close()

    flash("Rendez-vous supprime.", "info")
    return redirect(url_for("appointments"))


# =============================================================================
# APPLICATION ENTRY POINT
# =============================================================================

if __name__ == "__main__":
    # Run Flask development server with debug mode enabled
    # Debug mode: auto-reloads code on changes, shows detailed error pages
    app.run(debug=True)
