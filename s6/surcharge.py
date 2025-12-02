class Employe:
    def salaire(self):
        print("le salaire de l'employe est de ",50+4000)
class Manager(Employe):
    def salaire(self):
        print("le salaire de l'employe est de ",50+5000)
            
e=Employe()
m=Manager()
e.salaire()
m.salaire()