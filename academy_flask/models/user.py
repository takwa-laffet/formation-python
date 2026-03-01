from config import Config


class User:
    """Classe de base pour tous les utilisateurs"""
    
    def __init__(self, user_id, nom, email, role):
        self.id = user_id
        self.nom = nom
        self.email = email
        self.role = role
    
    def to_dict(self):
        """Convertit l'utilisateur en dictionnaire"""
        return {
            'id': self.id,
            'nom': self.nom,
            'email': self.email,
            'role': self.role
        }
    
    @staticmethod
    def from_dict(data):
        """Crée un utilisateur depuis un dictionnaire"""
        return User(
            user_id=data.get('id'),
            nom=data.get('nom'),
            email=data.get('email'),
            role=data.get('role')
        )
    
    def __repr__(self):
        return f"<User {self.nom} ({self.role})>"


class Student(User):
    """Classe Etudiant héritant de User"""
    
    def __init__(self, user_id, nom, email):
        super().__init__(user_id, nom, email, Config.ROLE_STUDENT)
    
    @staticmethod
    def from_dict(data):
        return Student(
            user_id=data.get('id'),
            nom=data.get('nom'),
            email=data.get('email')
        )


class Teacher(User):
    """Classe Enseignant héritant de User"""
    
    def __init__(self, user_id, nom, email):
        super().__init__(user_id, nom, email, Config.ROLE_TEACHER)
    
    @staticmethod
    def from_dict(data):
        return Teacher(
            user_id=data.get('id'),
            nom=data.get('nom'),
            email=data.get('email')
        )


class Admin(User):
    """Classe Administrateur héritant de User"""
    
    def __init__(self, user_id, nom, email):
        super().__init__(user_id, nom, email, Config.ROLE_ADMIN)
    
    @staticmethod
    def from_dict(data):
        return Admin(
            user_id=data.get('id'),
            nom=data.get('nom'),
            email=data.get('email')
        )
