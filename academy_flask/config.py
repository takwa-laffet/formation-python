import os

# Configuration de l'application Flask
class Config:
    """Configuration de l'application Academy"""
    SECRET_KEY = 'academy-secret-key-2024'
    
    # Chemins des fichiers JSON
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    DATA_DIR = os.path.join(BASE_DIR, 'data')
    
    USERS_FILE = os.path.join(DATA_DIR, 'users.json')
    COURSES_FILE = os.path.join(DATA_DIR, 'courses.json')
    ENROLLMENTS_FILE = os.path.join(DATA_DIR, 'enrollments.json')
    
    # Roles utilisateurs
    ROLE_STUDENT = 'student'
    ROLE_TEACHER = 'teacher'
    ROLE_ADMIN = 'admin'
