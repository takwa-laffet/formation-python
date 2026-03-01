from config import Config
from utils import JsonManager
from services import CourseService


class EnrollmentService:
    """Service pour la gestion des inscriptions"""
    
    @staticmethod
    def get_all_enrollments():
        """Retourne toutes les inscriptions"""
        return JsonManager.read(Config.ENROLLMENTS_FILE)
    
    @staticmethod
    def get_enrollments_by_course(course_id):
        """Retourne toutes les inscriptions à un cours"""
        enrollments = EnrollmentService.get_all_enrollments()
        return [e for e in enrollments if e.get('course_id') == course_id]
    
    @staticmethod
    def get_enrollments_by_student(student_id):
        """Retourne toutes les inscriptions d'un étudiant"""
        enrollments = EnrollmentService.get_all_enrollments()
        return [e for e in enrollments if e.get('student_id') == student_id]
    
    @staticmethod
    def is_student_enrolled(student_id, course_id):
        """Vérifie si un étudiant est déjà inscrit à un cours"""
        enrollments = EnrollmentService.get_all_enrollments()
        
        for enrollment in enrollments:
            if (enrollment.get('student_id') == student_id and 
                enrollment.get('course_id') == course_id):
                return True
        
        return False
    
    @staticmethod
    def get_available_places(course_id):
        """Retourne le nombre de places disponibles pour un cours"""
        course = CourseService.get_course_by_id(course_id)
        
        if not course:
            return 0
        
        enrollments = EnrollmentService.get_enrollments_by_course(course_id)
        enrolled_count = len(enrollments)
        
        return course.capacite_max - enrolled_count
    
    @staticmethod
    def enroll_student(student_id, course_id):
        """
        Inscrit un étudiant à un cours
        Retourne: (success: bool, message: str)
        """
        # Vérifier si le cours existe
        course = CourseService.get_course_by_id(course_id)
        if not course:
            return False, "Cours introuvable"
        
        # Vérifier si l'étudiant est déjà inscrit
        if EnrollmentService.is_student_enrolled(student_id, course_id):
            return False, "Étudiant déjà inscrit à ce cours"
        
        # Vérifier les places disponibles
        available = EnrollmentService.get_available_places(course_id)
        if available <= 0:
            return False, "Plus de places disponibles"
        
        # Créer l'inscription
        enrollment_data = {
            'student_id': student_id,
            'course_id': course_id
        }
        
        JsonManager.append(Config.ENROLLMENTS_FILE, enrollment_data)
        return True, "Inscription réussie"
    
    @staticmethod
    def unenroll_student(student_id, course_id):
        """Désinscrit un étudiant d'un cours"""
        enrollments = JsonManager.read(Config.ENROLLMENTS_FILE)
        
        enrollments = [e for e in enrollments 
                      if not (e.get('student_id') == student_id and 
                             e.get('course_id') == course_id)]
        
        JsonManager.write(Config.ENROLLMENTS_FILE, enrollments)
    
    @staticmethod
    def get_student_count_for_course(course_id):
        """Retourne le nombre d'étudiants inscrits à un cours"""
        enrollments = EnrollmentService.get_enrollments_by_course(course_id)
        return len(enrollments)
