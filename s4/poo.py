class Voiture:
    def __init__(self, marque, couleur):
        self.marque = marque
        self.couleur = couleur

    def introduction(self):
        print("Je suis une voiture", self.marque, "de couleur", self.couleur)


v1 = Voiture("BMW", "rouge")
v2 = Voiture("Mercedes", "noir")

v1.introduction()
v2.introduction()

print(v1.marque)
print(v1.couleur)
print(type(v1.couleur))
