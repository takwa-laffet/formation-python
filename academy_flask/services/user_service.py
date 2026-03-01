from config import Config
from models import User, Student, Teacher, Admin
from utils import JsonManager


class UserService:
    """Service pour la gestion des utilisateurs"""
    
    @staticmethod
    def get_all_users():
        """Retourne tous les utilisateurs"""
        users_data = JsonManager.read(Config.USERS_FILE)
        users = []
        
        for user_data in users_data:
            role = user_data.get('role')
            if role == Config.ROLE_STUDENT:
                users.append(Student.from_dict(user_data))
            elif role == Config.ROLE_TEACHER:
                users.append(Teacher.from_dict(user_data))
            elif role == Config.ROLE_ADMIN:
                users.append(Admin.from_dict(user_data))
            else:
                users.append(User.from_dict(user_data))
        
        return users
    
    @staticmethod
    def get_user_by_id(user_id):
        """Retourne un utilisateur par son ID"""
        user_data = JsonManager.find_by_id(Config.USERS_FILE, user_id)
        
        if not user_data:
            return None
        
        role = user_data.get('role')
        if role == Config.ROLE_STUDENT:
            return Student.from_dict(user_data)
        elif role == Config.ROLE_TEACHER:
            return Teacher.from_dict(user_data)
        elif role == Config.ROLE_ADMIN:
            return Admin.from_dict(user_data)
        
        return User.from_dict(user_data)
    
    @staticmethod
    def get_next_id():
        """Génère le prochain ID utilisateur"""
        users = JsonManager.read(Config.USERS_FILE)
        if not users:
            return 1
        
        max_id = max(int(user.get('id', 0)) for user in users)
        return max_id + 1
    
    @staticmethod
    def add_user(nom, email, role):
        """Ajoute un nouvel utilisateur"""
        user_id = UserService.get_next_id()
        
        user_data = {
            'id': user_id,
            'nom': nom,
            'email': email,
            'role': role
        }
        
        JsonManager.append(Config.USERS_FILE, user_data)
        return user_id
    
    @staticmethod
    def update_user(user_id, nom, email, role):
        """Met à jour un utilisateur existant"""
        user_data = {
            'id': user_id,
            'nom': nom,
            'email': email,
            'role': role
        }
        
        JsonManager.update(Config.USERS_FILE, user_id, user_data)
    
    @staticmethod
    def delete_user(user_id):
        """Supprime un utilisateur"""
        JsonManager.delete(Config.USERS_FILE, user_id)
    
    @staticmethod
    def get_teachers():
        """Retourne tous les enseignants"""
        all_users = UserService.get_all_users()
        return [user for user in all_users if user.role == Config.ROLE_TEACHER]
    
    @staticmethod
    def get_students():
        """Retourne tous les étudiants"""
        all_users = UserService.get_all_users()
        return [user for user in all_users if user.role == Config.ROLE_STUDENT]
