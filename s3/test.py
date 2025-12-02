def creer_etudiants():
    etudiants = {}  # Dictionnaire vide pour tous les étudiants
    n = int(input("Combien d'étudiants voulez-vous entrer ? "))
    for i in range(n):
        print(f"\nÉtudiant :")
        nom = input("Nom : ")
        prenom = input("Prénom : ")
        moyenne = float(input("Moyenne générale : "))
        # Ajouter chaque étudiant dans le dictionnaire avec clé unique
        etudiants[nom] = {
            'Prenom': prenom,
            'Moyenne_generale': moyenne
        }
    return etudiants


def meilleure_moyenne():
    etudiants = creer_etudiants()
    # Prendre le premier étudiant comme référence
    meilleur_nom = list(etudiants.keys())[0]
    meilleur = etudiants[meilleur_nom]

    for nom, info in etudiants.items():
        if info['Moyenne_generale'] > meilleur['Moyenne_generale']:
            meilleur = info
            meilleur_nom = nom

    print(f"\nL'étudiant {meilleur['Prenom']} {meilleur_nom} a la meilleure moyenne ({meilleur['Moyenne_generale']})")


# Exécution
meilleure_moyenne()
