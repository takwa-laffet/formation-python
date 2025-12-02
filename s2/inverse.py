# Liste initiale
liste_origine = [1, 2, 3, 4, 5]

# Liste vide pour stocker l'inverse
liste_inverse = []

# Parcourir la liste d'origine de la fin vers le début
index = len(liste_origine) - 1
while index >= 0:
    liste_inverse.append(liste_origine[index])
    index -= 1

# Afficher le résultat
print("Liste originale :", liste_origine)
print("Liste inversée :", liste_inverse)
