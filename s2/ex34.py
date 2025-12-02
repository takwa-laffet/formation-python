""" import time

# caractères utilisables
lettres_min = "abcdefghijklmnopqrstuvwxyz"
lettres_maj = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
chiffres = "0123456789"
specials = "!@#$%^&*()-_=+[]{};:,.<>/?"
caracteres = lettres_min + lettres_maj + chiffres + specials

longueur = 12
mot_de_passe = ""

# une simple "pseudo-random" basée sur le temps
seed = int(time.time() * 1000)  # millisecondes actuelles

for i in range(longueur):
    # calcul simple pour pseudo-aléatoire
    seed = (seed * 9301 + 49297) % 233280
    print(seed)
    index = seed % len(caracteres)
    print(caracteres)
    print(index)
    mot_de_passe += caracteres[index]

print("Mot de passe généré :", mot_de_passe)
 """
# 2 eme solution avec ranom
# caractères utilisables

import random

lettres_min = "abcdefghijklmnopqrstuvwxyz"
lettres_maj = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
chiffres = "0123456789"
specials = "!@#$%^&*()-_=+[]{};:,.<>/?"
caracteres = lettres_min + lettres_maj + chiffres + specials

longueur = 12
mot_de_passe = ""
print(len(caracteres))

for i in range(longueur):
    
    index = random.randint(0, len(caracteres) - 1)
    print(index)
    mot_de_passe = mot_de_passe+caracteres[index]

print("Mot de passe généré :", mot_de_passe)