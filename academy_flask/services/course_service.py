from config import Config
from models import Course
from utils import JsonManager


class CourseService:
    """Service pour la gestion des cours"""
    
    @staticmethod
    def get_all_courses():
        """Retourne tous les cours"""
        courses_data = JsonManager.read(Config.COURSES_FILE)
        return [Course.from_dict(course_data) for course_data in courses_data]
    
    @staticmethod
    def get_course_by_id(course_id):
        """Retourne un cours par son ID"""
        course_data = JsonManager.find_by_id(Config.COURSES_FILE, course_id)
        
        if not course_data:
            return None
        
        return Course.from_dict(course_data)
    
    @staticmethod
    def get_courses_by_teacher(teacher_id):
        """Retourne tous les cours d'un enseignant"""
        all_courses = CourseService.get_all_courses()
        return [course for course in all_courses if course.teacher_id == teacher_id]
    
    @staticmethod
    def get_next_id():
        """Génère le prochain ID de cours"""
        courses = JsonManager.read(Config.COURSES_FILE)
        if not courses:
            return 1
        
        max_id = max(int(course.get('id', 0)) for course in courses)
        return max_id + 1
    
    @staticmethod
    def add_course(titre, teacher_id, capacite_max=30):
        """Ajoute un nouveau cours"""
        course_id = CourseService.get_next_id()
        
        course_data = {
            'id': course_id,
            'titre': titre,
            'teacher_id': teacher_id,
            'capacite_max': capacite_max
        }
        
        JsonManager.append(Config.COURSES_FILE, course_data)
        return course_id
    
    @staticmethod
    def update_course(course_id, titre, teacher_id, capacite_max):
        """Met à jour un cours existant"""
        course_data = {
            'id': course_id,
            'titre': titre,
            'teacher_id': teacher_id,
            'capacite_max': capacite_max
        }
        
        JsonManager.update(Config.COURSES_FILE, course_id, course_data)
    
    @staticmethod
    def delete_course(course_id):
        """Supprime un cours"""
        JsonManager.delete(Config.COURSES_FILE, course_id)
