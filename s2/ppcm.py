# Définir deux nombres entiers
a = 12  # Exemple de premier nombre
b = 18  # Exemple de deuxième nombre

# Assurez-vous que les nombres sont positifs
if a <= 0 or b <= 0:
    print("Les nombres doivent être strictement positifs.")
else:
    # Trouver le PPCM par une méthode itérative
    ppcm = a if a > b else b  # Commencez par le plus grand des deux nombres

    # Boucle jusqu'à trouver le PPCM
    while True:
        if ppcm % a == 0 and ppcm % b == 0:
            break  # Si le PPCM est trouvé, sortez de la boucle
        ppcm += 1  # Incrémentez pour tester le prochain multiple

    # Afficher le résultat
    print("Le PPCM de", a, "et", b, "est :", ppcm)
