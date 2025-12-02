import json
import os

FICHIER_JSON = "etudiants.json"

# -----------------------------
# Charger et sauvegarder les données
# -----------------------------
def charger_donnees():
    if os.path.exists(FICHIER_JSON):
        try:
            with open(FICHIER_JSON, "r", encoding="utf-8") as f:
                return json.load(f)
        except json.JSONDecodeError:
            print("⚠️ Fichier JSON corrompu, démarrage avec une base vide.")
    return {}

def sauvegarder_donnees():
    with open(FICHIER_JSON, "w", encoding="utf-8") as f:
        json.dump(etudiants, f, indent=4, ensure_ascii=False)

# -----------------------------
# Fonctions principales
# -----------------------------
def ajouter_etudiant():
    matricule = input("Entrez le matricule de l'étudiant : ")
    if matricule in etudiants:
        print("⚠️ Cet étudiant existe déjà.")
        return
    
    nom = input("Entrez le nom de l'étudiant : ")
    notes_str = input("Entrez les notes séparées par des espaces : ")
    
    try:
        notes = [float(n) for n in notes_str.split()]
        etudiants[matricule] = {"nom": nom, "notes": notes}
        sauvegarder_donnees()
        print(f"✅ Étudiant {nom} ajouté avec succès !")
    except ValueError:
        print("❌ Erreur : les notes doivent être des nombres.")

def modifier_etudiant():
    matricule = input("Entrez le matricule de l'étudiant à modifier : ")
    if matricule not in etudiants:
        print("❌ Étudiant introuvable.")
        return
    
    print(f"Étudiant actuel : {etudiants[matricule]}")
    nom = input("Nouveau nom (laisser vide pour ne pas changer) : ")
    notes_str = input("Nouvelles notes séparées par des espaces (laisser vide pour ne pas changer) : ")
    
    if nom:
        etudiants[matricule]["nom"] = nom
    if notes_str:
        try:
            notes = [float(n) for n in notes_str.split()]
            etudiants[matricule]["notes"] = notes
        except ValueError:
            print("⚠️ Erreur : les notes doivent être numériques.")
    
    sauvegarder_donnees()
    print("✅ Étudiant modifié avec succès.")

def supprimer_etudiant():
    matricule = input("Entrez le matricule à supprimer : ")
    if matricule in etudiants:
        del etudiants[matricule]
        sauvegarder_donnees()
        print("✅ Étudiant supprimé avec succès.")
    else:
        print("❌ Étudiant introuvable.")

def calculer_moyenne_etudiant(info):
    notes = info["notes"]
    if not notes:
        return None
    return sum(notes) / len(notes)

def afficher_etudiants(trier_par_moyenne=False):
    if not etudiants:
        print("📭 Aucun étudiant enregistré.")
        return

    # Tri par moyenne si demandé
    liste_etudiants = []
    for matricule, info in etudiants.items():
        moyenne = calculer_moyenne_etudiant(info)
        liste_etudiants.append((matricule, info["nom"], info["notes"], moyenne))

    if trier_par_moyenne:
        liste_etudiants.sort(key=lambda x: (x[3] if x[3] is not None else -1), reverse=True)

    print("\n📋 Liste des étudiants :")
    for matricule, nom, notes, moyenne in liste_etudiants:
        moy_affichage = f"{moyenne:.2f}" if moyenne is not None else "N/A"
        print(f"- {matricule} | Nom: {nom} | Notes: {notes} | Moyenne: {moy_affichage}")

def calculer_moyenne_individuelle():
    matricule = input("Entrez le matricule de l'étudiant : ")
    if matricule not in etudiants:
        print("❌ Étudiant introuvable.")
        return
    moyenne = calculer_moyenne_etudiant(etudiants[matricule])
    if moyenne is None:
        print("⚠️ Cet étudiant n’a pas de notes.")
    else:
        print(f"🧮 Moyenne de {etudiants[matricule]['nom']} : {moyenne:.2f}")

def calculer_moyenne_generale():
    total_notes = 0
    total_count = 0
    for info in etudiants.values():
        total_notes += sum(info["notes"])
        total_count += len(info["notes"])
    
    if total_count == 0:
        print("⚠️ Aucun étudiant n’a de notes pour calculer la moyenne générale.")
        return
    
    moyenne = total_notes / total_count
    print(f"🧮 Moyenne générale de la classe : {moyenne:.2f}")

def afficher_menu():
    print("\n===== MENU PRINCIPAL =====")
    print("1. Ajouter un étudiant")
    print("2. Modifier un étudiant")
    print("3. Supprimer un étudiant")
    print("4. Afficher tous les étudiants")
    print("5. Afficher tous les étudiants triés par moyenne")
    print("6. Calculer la moyenne d’un étudiant")
    print("7. Calculer la moyenne générale de la classe")
    print("8. Quitter")

# -----------------------------
# Programme principal
# -----------------------------
etudiants = charger_donnees()

while True:
    afficher_menu()
    choix = input("➡️ Votre choix : ")

    if choix == "1":
        ajouter_etudiant()
    elif choix == "2":
        modifier_etudiant()
    elif choix == "3":
        supprimer_etudiant()
    elif choix == "4":
        afficher_etudiants()
    elif choix == "5":
        afficher_etudiants(trier_par_moyenne=True)
    elif choix == "6":
        calculer_moyenne_individuelle()
    elif choix == "7":
        calculer_moyenne_generale()
    elif choix == "8":
        print("💾 Sauvegarde finale en cours...")
        sauvegarder_donnees()
        print("👋 Au revoir !")
        break
    else:
        print("❌ Choix invalide. Essayez encore.")
