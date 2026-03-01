from flask import Flask, render_template, request, redirect, url_for
from config import Config
from services import UserService, CourseService, EnrollmentService

app = Flask(__name__)
app.config.from_object(Config)


# Route principale - Accueil
@app.route('/')
def index():
    """Page d'accueil avec statistiques"""
    user_count = len(UserService.get_all_users())
    course_count = len(CourseService.get_all_courses())
    enrollment_count = len(EnrollmentService.get_all_enrollments())
    
    return render_template('index.html', 
                           user_count=user_count, 
                           course_count=course_count,
                           enrollment_count=enrollment_count)


# Routes pour la gestion des utilisateurs
@app.route('/users')
def users():
    """Liste des utilisateurs"""
    all_users = UserService.get_all_users()
    return render_template('users.html', users=all_users)


@app.route('/users/add', methods=['POST'])
def add_user():
    """Ajouter un utilisateur"""
    nom = request.form.get('nom')
    email = request.form.get('email')
    role = request.form.get('role')
    
    UserService.add_user(nom, email, role)
    return redirect(url_for('users'))


@app.route('/users/edit/<int:user_id>')
def edit_user(user_id):
    """Modifier un utilisateur"""
    user = UserService.get_user_by_id(user_id)
    all_users = UserService.get_all_users()
    return render_template('users.html', users=all_users, edit_user=user)


@app.route('/users/update/<int:user_id>', methods=['POST'])
def update_user(user_id):
    """Mettre à jour un utilisateur"""
    nom = request.form.get('nom')
    email = request.form.get('email')
    role = request.form.get('role')
    
    UserService.update_user(user_id, nom, email, role)
    return redirect(url_for('users'))


@app.route('/users/delete/<int:user_id>')
def delete_user(user_id):
    """Supprimer un utilisateur"""
    UserService.delete_user(user_id)
    return redirect(url_for('users'))


# Routes pour la gestion des cours
@app.route('/courses')
def courses():
    """Liste des cours"""
    all_courses = CourseService.get_all_courses()
    teachers = UserService.get_teachers()
    
    # Compter les inscriptions par cours
    enrollment_counts = {}
    for course in all_courses:
        enrollment_counts[course.id] = EnrollmentService.get_student_count_for_course(course.id)
    
    return render_template('courses.html', 
                           courses=all_courses, 
                           teachers=teachers,
                           enrollment_counts=enrollment_counts)


@app.route('/courses/add', methods=['POST'])
def add_course():
    """Ajouter un cours"""
    titre = request.form.get('titre')
    teacher_id = int(request.form.get('teacher_id'))
    capacite_max = int(request.form.get('capacite_max'))
    
    CourseService.add_course(titre, teacher_id, capacite_max)
    return redirect(url_for('courses'))


@app.route('/courses/edit/<int:course_id>')
def edit_course(course_id):
    """Modifier un cours"""
    course = CourseService.get_course_by_id(course_id)
    all_courses = CourseService.get_all_courses()
    teachers = UserService.get_teachers()
    
    enrollment_counts = {}
    for c in all_courses:
        enrollment_counts[c.id] = EnrollmentService.get_student_count_for_course(c.id)
    
    return render_template('courses.html', 
                           courses=all_courses, 
                           teachers=teachers,
                           edit_course=course,
                           enrollment_counts=enrollment_counts)


@app.route('/courses/update/<int:course_id>', methods=['POST'])
def update_course(course_id):
    """Mettre à jour un cours"""
    titre = request.form.get('titre')
    teacher_id = int(request.form.get('teacher_id'))
    capacite_max = int(request.form.get('capacite_max'))
    
    CourseService.update_course(course_id, titre, teacher_id, capacite_max)
    return redirect(url_for('courses'))


@app.route('/courses/delete/<int:course_id>')
def delete_course(course_id):
    """Supprimer un cours"""
    CourseService.delete_course(course_id)
    return redirect(url_for('courses'))


# Routes pour la gestion des inscriptions
@app.route('/enrollments')
def enrollments():
    """Liste des inscriptions"""
    all_enrollments = EnrollmentService.get_all_enrollments()
    students = UserService.get_students()
    courses = CourseService.get_all_courses()
    
    # Compter les inscriptions par cours
    enrollment_counts = {}
    for course in courses:
        enrollment_counts[course.id] = EnrollmentService.get_student_count_for_course(course.id)
    
    return render_template('enroll.html', 
                           enrollments=all_enrollments,
                           students=students,
                           courses=courses,
                           enrollment_counts=enrollment_counts)


@app.route('/enrollments/add', methods=['POST'])
def add_enrollment():
    """Ajouter une inscription"""
    student_id = int(request.form.get('student_id'))
    course_id = int(request.form.get('course_id'))
    
    success, message = EnrollmentService.enroll_student(student_id, course_id)
    
    all_enrollments = EnrollmentService.get_all_enrollments()
    students = UserService.get_students()
    courses = CourseService.get_all_courses()
    
    enrollment_counts = {}
    for course in courses:
        enrollment_counts[course.id] = EnrollmentService.get_student_count_for_course(course.id)
    
    return render_template('enroll.html', 
                           enrollments=all_enrollments,
                           students=students,
                           courses=courses,
                           enrollment_counts=enrollment_counts,
                           message=message)


@app.route('/enrollments/delete/<int:student_id>/<int:course_id>')
def delete_enrollment(student_id, course_id):
    """Supprimer une inscription"""
    EnrollmentService.unenroll_student(student_id, course_id)
    return redirect(url_for('enrollments'))


if __name__ == '__main__':
    app.run(debug=True)
