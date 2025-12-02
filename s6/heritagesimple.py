class Personne:
    def __init__(self,nom,age):
        self.nom=nom
        self.age=age
    def salut(self):
        print(f"salut je suis {self.nom} et j'ai {self.age} ans")

#class fille 
class Etudiant(Personne):
    def __init__(self,nom,age,niveau):
       super().__init__(nom,age) # appeler le constructeur de la classe mére
       self.niveau=niveau
    def etudie(self):
        print(f"je suis {self.nom} et je suis en {self.niveau}")
 
Etudiant1=Etudiant("sara",23,"genie logiciel")
Etudiant1.etudie()
Etudiant1.salut()