class Course:
    """Classe représentant un cours"""
    
    def __init__(self, course_id, titre, teacher_id, capacite_max=30):
        self.id = course_id
        self.titre = titre
        self.teacher_id = teacher_id
        self.capacite_max = capacite_max
    
    def to_dict(self):
        """Convertit le cours en dictionnaire"""
        return {
            'id': self.id,
            'titre': self.titre,
            'teacher_id': self.teacher_id,
            'capacite_max': self.capacite_max
        }
    
    @staticmethod
    def from_dict(data):
        """Crée un cours depuis un dictionnaire"""
        return Course(
            course_id=data.get('id'),
            titre=data.get('titre'),
            teacher_id=data.get('teacher_id'),
            capacite_max=data.get('capacite_max', 30)
        )
    
    def __repr__(self):
        return f"<Course {self.titre} (Teacher: {self.teacher_id})>"
