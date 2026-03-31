from flask import Flask, render_template, request, redirect, url_for
import mysql.connector

app = Flask(__name__)

# connecting to the database
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="salon_coiffure"
)

# creating a cursor object to execute SQL queries
cursor = conn.cursor()

def init_db():
    """Initialize the database with tables"""
    # Create database if not exists
    cursor.execute("CREATE DATABASE IF NOT EXISTS salon_coiffure")
    conn.commit()
    
    # Use the database
    cursor.execute("USE salon_coiffure")
    
    # Create reservations table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS reservations (
            id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(255),
            phone VARCHAR(50),
            date DATE,
            time_slot TIME
        )
    """)
    conn.commit()
    print("Table created successfully")

def is_slot_available(date, time_slot):
    """Check if the time slot is already reserved"""
    try:
        # Convert time string to TIME format for MySQL
        time_str = f"{time_slot}:00" if len(time_slot.split(':')) == 2 else time_slot
        cursor.execute(
            "SELECT * FROM reservations WHERE date = %s AND time_slot = %s",
            (date, time_str)
        )
        result = cursor.fetchone()
        return result is None
    except:
        return True

@app.route('/')
def index():
    """Display all reservations"""
    try:
        cursor.execute("SELECT * FROM reservations ORDER BY date, time_slot")
        reservations = cursor.fetchall()
        return render_template('index.html', reservations=reservations)
    except:
        return render_template('index.html', reservations=[])

@app.route('/form', methods=['GET', 'POST'])
def form():
    """Add a new reservation"""
    error = None
    success = None
    
    if request.method == 'POST':
        name = request.form.get('name')
        phone = request.form.get('phone')
        date = request.form.get('date')
        time_slot = request.form.get('time_slot')
        
        # Check if slot is available
        if not is_slot_available(date, time_slot):
            error = "Ce créneau est déjà réservé. Veuillez choisir un autre horaire."
        else:
            # Convert time string to TIME format for MySQL
            time_str = f"{time_slot}:00" if len(time_slot.split(':')) == 2 else time_slot
            
            # Save new reservation
            cursor.execute(
                "INSERT INTO reservations (name, phone, date, time_slot) VALUES (%s, %s, %s, %s)",
                (name, phone, date, time_str)
            )
            conn.commit()
            print("Reservation inserted successfully")
            success = "Réservation ajoutée avec succès!"
    
    return render_template('form.html', error=error, success=success)

@app.route('/delete/<int:reservation_id>')
def delete(reservation_id):
    """Delete a reservation"""
    cursor.execute("DELETE FROM reservations WHERE id = %s", (reservation_id,))
    conn.commit()
    print("Reservation deleted successfully")
    return redirect(url_for('index'))

@app.route('/check', methods=['GET', 'POST'])
def check():
    """Check if a slot is available"""
    available = None
    if request.method == 'POST':
        date = request.form.get('date')
        time_slot = request.form.get('time_slot')
        available = is_slot_available(date, time_slot)
    return render_template('check.html', available=available)

if __name__ == '__main__':
    init_db()
    app.run(debug=True)
