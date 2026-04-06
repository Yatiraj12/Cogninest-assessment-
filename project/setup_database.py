import sqlite3
import random
from datetime import datetime, timedelta
from faker import Faker

DB_NAME = "clinic.db"
fake = Faker()


def create_connection():
    """Create SQLite connection."""
    return sqlite3.connect(DB_NAME)


def create_tables(conn):
    """Create all required tables."""
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS patients (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        first_name TEXT NOT NULL,
        last_name TEXT NOT NULL,
        email TEXT,
        phone TEXT,
        date_of_birth DATE,
        gender TEXT,
        city TEXT,
        registered_date DATE
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS doctors (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        specialization TEXT,
        department TEXT,
        phone TEXT
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS appointments (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        patient_id INTEGER,
        doctor_id INTEGER,
        appointment_date DATETIME,
        status TEXT,
        notes TEXT,
        FOREIGN KEY(patient_id) REFERENCES patients(id),
        FOREIGN KEY(doctor_id) REFERENCES doctors(id)
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS treatments (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        appointment_id INTEGER,
        treatment_name TEXT,
        cost REAL,
        duration_minutes INTEGER,
        FOREIGN KEY(appointment_id) REFERENCES appointments(id)
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS invoices (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        patient_id INTEGER,
        invoice_date DATE,
        total_amount REAL,
        paid_amount REAL,
        status TEXT,
        FOREIGN KEY(patient_id) REFERENCES patients(id)
    )
    """)

    conn.commit()


def random_date_within_last_year():
    """Generate random date within last 12 months."""
    today = datetime.today()
    days_ago = random.randint(0, 365)
    return (today - timedelta(days=days_ago)).strftime("%Y-%m-%d")


def insert_doctors(conn):
    """Insert 15 doctors."""
    cursor = conn.cursor()
    specializations = ["Dermatology", "Cardiology", "Orthopedics", "General", "Pediatrics"]
    departments = ["Skin", "Heart", "Bones", "General", "Children"]

    doctors = []
    for _ in range(15):
        name = fake.name()
        spec = random.choice(specializations)
        dept = departments[specializations.index(spec)]
        phone = fake.phone_number()
        doctors.append((name, spec, dept, phone))

    cursor.executemany("""
        INSERT INTO doctors (name, specialization, department, phone)
        VALUES (?, ?, ?, ?)
    """, doctors)

    conn.commit()
    return cursor.execute("SELECT id FROM doctors").fetchall()


def insert_patients(conn):
    """Insert 200 patients."""
    cursor = conn.cursor()
    cities = ["Mumbai", "Pune", "Delhi", "Bangalore", "Chennai", "Hyderabad", "Nagpur", "Nashik"]

    patients = []
    for _ in range(200):
        first_name = fake.first_name()
        last_name = fake.last_name()
        email = fake.email() if random.random() > 0.2 else None
        phone = fake.phone_number() if random.random() > 0.2 else None
        dob = fake.date_of_birth(minimum_age=1, maximum_age=90)
        gender = random.choice(["M", "F"])
        city = random.choice(cities)
        registered_date = random_date_within_last_year()

        patients.append((first_name, last_name, email, phone, dob, gender, city, registered_date))

    cursor.executemany("""
        INSERT INTO patients (first_name, last_name, email, phone, date_of_birth, gender, city, registered_date)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    """, patients)

    conn.commit()
    return cursor.execute("SELECT id FROM patients").fetchall()


def insert_appointments(conn, patient_ids, doctor_ids):
    """Insert 500 appointments."""
    cursor = conn.cursor()
    statuses = ["Scheduled", "Completed", "Cancelled", "No-Show"]

    appointments = []
    for _ in range(500):
        patient_id = random.choice(patient_ids)[0]
        doctor_id = random.choice(doctor_ids)[0]
        date = random_date_within_last_year()
        status = random.choice(statuses)
        notes = fake.sentence() if random.random() > 0.3 else None

        appointments.append((patient_id, doctor_id, date, status, notes))

    cursor.executemany("""
        INSERT INTO appointments (patient_id, doctor_id, appointment_date, status, notes)
        VALUES (?, ?, ?, ?, ?)
    """, appointments)

    conn.commit()
    return cursor.execute("SELECT id, status FROM appointments").fetchall()


def insert_treatments(conn, appointments):
    """Insert treatments for completed appointments."""
    cursor = conn.cursor()
    treatments = []

    for appointment_id, status in appointments:
        if status == "Completed" and len(treatments) < 350:
            treatment_name = random.choice(["X-Ray", "Blood Test", "MRI", "Consultation", "Surgery"])
            cost = random.randint(50, 5000)
            duration = random.randint(10, 120)
            treatments.append((appointment_id, treatment_name, cost, duration))

    cursor.executemany("""
        INSERT INTO treatments (appointment_id, treatment_name, cost, duration_minutes)
        VALUES (?, ?, ?, ?)
    """, treatments)

    conn.commit()


def insert_invoices(conn, patient_ids):
    """Insert 300 invoices."""
    cursor = conn.cursor()
    statuses = ["Paid", "Pending", "Overdue"]

    invoices = []
    for _ in range(300):
        patient_id = random.choice(patient_ids)[0]
        total = random.randint(100, 10000)
        paid = total if random.random() > 0.3 else random.randint(0, total)
        status = "Paid" if paid == total else random.choice(["Pending", "Overdue"])
        date = random_date_within_last_year()

        invoices.append((patient_id, date, total, paid, status))

    cursor.executemany("""
        INSERT INTO invoices (patient_id, invoice_date, total_amount, paid_amount, status)
        VALUES (?, ?, ?, ?, ?)
    """, invoices)

    conn.commit()


def main():
    conn = create_connection()
    create_tables(conn)

    doctor_ids = insert_doctors(conn)
    patient_ids = insert_patients(conn)
    appointments = insert_appointments(conn, patient_ids, doctor_ids)
    insert_treatments(conn, appointments)
    insert_invoices(conn, patient_ids)

    print("Database setup complete.")
    print("Inserted 15 doctors")
    print("Inserted 200 patients")
    print("Inserted 500 appointments")
    print("Inserted 350 treatments")
    print("Inserted 300 invoices")

    conn.close()


if __name__ == "__main__":
    main()