class Employe:
    def __init__(self,nom,age,domaine):
        self.nom=nom
        self.age=age
        self.domaine=domaine
    def travail(self):
        print(f"{self.nom} travaille dans le domaine de {self.domaine}")

class Sportif:
    def __init__(self,nom,age,sport):
        self.nom=nom
        self.age=age
        self.sport=sport
    def pratique_sport(self):
        print(f"{self.nom} pratique le sport de {self.sport}")
class EtudiantSportif(Employe,Sportif):
    def __init__(self,nom,age,domaine,sport,niveau):
        Employe.__init__(self,nom,age,domaine)
        Sportif.__init__(self,nom,age,sport)
        self.niveau=niveau
    def stage(self):
        print(f"{self.nom} travaille en stage dans le domaine de {self.domaine} et pratique le sport de {self.sport}")
        print(f"son niveau est {self.niveau}")

etudiant_sportif=EtudiantSportif("sara",23,"informatique","basket",3)
etudiant_sportif.stage()
etudiant_sportif.travail()
etudiant_sportif.pratique_sport()