""" import csv
with open("etudiants.csv","r") as f:
    lecteur = csv.DictReader(f)
    for ligne in lecteur:
        print(ligne)
         """
import csv
with open("etudiants.csv","w",newline="") as f:
    champs=["nom","age","note"]
    lecteur = csv.DictWriter(f,fieldnames=champs)
    lecteur.writeheader()
    lecteur.writerow({"nom":"takwa","age":"12","note":"12"})
    lecteur.writerow({"nom":"youssef","age":"12","note":"12"})
