import json

# Dictionnaire global pour stocker les étudiants
fichier_JSON = "etudiants.json"
etudiants = {}  # dictionnaire global

# Fonction pour charger le JSON
def charger_JSON():
    global etudiants
    try:
        with open(fichier_JSON, 'r', encoding='utf-8') as file:
            etudiants = json.load(file)
            print("Données chargées avec succès !")
    except FileNotFoundError:
        print(f"⚠️ Le fichier '{fichier_JSON}' n'existe pas. Un nouveau fichier sera créé.")
        etudiants = {}
    except json.JSONDecodeError:
        print(f"⚠️ Le fichier '{fichier_JSON}' contient un format JSON invalide.")
        etudiants = {}

# Fonction pour sauvegarder le JSON
def sauvegarde_JSON():
    global etudiants
    with open(fichier_JSON, 'w', encoding='utf-8') as file:
        json.dump(etudiants, file, indent=4, ensure_ascii=False)
        print("Données sauvegardées avec succès !")

# Fonction pour ajouter un étudiant
def ajout_etudiant():
    global etudiants
    matricule = input("Donner la matricule de l'étudiant: ")
    nom = input("Donner le nom de l'étudiant: ")
    prenom = input("Donner le prénom de l'étudiant: ")
    note = input("Donner la note de l'étudiant: ")

    if matricule in etudiants:
        print("Cet étudiant existe déjà !")
    else:
        etudiants[matricule] = {
            'Nom': nom,
            'Prenom': prenom,
            'Note': note
        }
        print("Étudiant ajouté avec succès.")
        sauvegarde_JSON()

# Fonction pour afficher tous les étudiants
def affich_etudiants():
    global etudiants
    if etudiants:
        print("\n--- Liste des étudiants ---")
        for matricule, infos in etudiants.items():
                    print(f"Matricule: {matricule} | Nom: {infos['Nom']} | Prénom: {infos['Prenom']} | Note: {infos['Note']}")
    else:
        print("Aucun étudiant n'a encore été ajouté.")

# Menu principal
def Menu():
    print("\n===== MENU PRINCIPAL =====")
    print("1: Ajouter un étudiant")
    print("2: Modifier un étudiant")
    print("3: Supprimer un étudiant")
    print("4: Afficher tous les étudiants")
    print("5: Quitter")

# Charger les données au démarrage
charger_JSON()

# Boucle principale
while True:
    Menu()
    try:
        x = int(input("Donnez votre choix: "))
    except ValueError:
        print("Veuillez entrer un nombre valide (1-5).")
        continue

    if x == 1:
        ajout_etudiant()
    elif x == 2:
        print("Fonction modification à implémenter...")
    elif x == 3:
        print("Fonction affichage à implémenter...")

    elif x == 4:
        print("Fonction affichage à implémenter...")
    elif x == 5:
        print("Au revoir !")
        break
    else:
        print("Choix invalide, veuillez choisir entre 1 et 5.")
