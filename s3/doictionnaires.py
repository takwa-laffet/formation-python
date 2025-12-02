""" etudaints = {
  "etudaint1":  {
  "nom":"sara",
  "age":21,
  "filiere": "cybersecurite"},

  "etudaint2" : {
      "nom":"ali",
      "age":22,
      "filiere":"genie logiciel"
  }
} """

etudaints ={
    "nom" : "sara",
    "age":33,
    "filiere":"mathematiques"
}
#ajouter un cle valeur
#etudaints["email"]="sara@gmail.com"  
#print(etudaints)
#ajouter valuer ou modifier
#etudaints["age"]="40"
#print(etudaints)
#supprimer un element
#filiere = etudaints.pop("filiere")
#print(etudaints)
#print(filiere)
#methode 2
#etudaints.popitem()
#print(etudaints)
#vider le dictionnaire
#etudaints.clear()
#print(etudaints)
#print(type(etudaints))
#afficher tous les cle du dictionnaire
#print(etudaints.keys())

#afficher tous les valeurs du dictionnaire
#etudaints.values()
#print(etudaints.values())
#print(etudaints)
#afficher tous les items du dictionnaire
#print(etudaints.items())
#print(etudaints)
""" print(etudaint["nom"])
print(etudaint["age"])
print(etudaint["filiere"]) """

###############################################################################################

# 1) Création du dictionnaire avec 3 livres
books = {
    "livre1": {"titre": "Le Petit Prince", "auteur": "Antoine de Saint-Exupéry", "annee": 1943},
    "livre2": {"titre": "L'Étranger",       "auteur": "Albert Camus","annee": 1942},
    "livre3": {"titre": "Les Misérables",   "auteur": "Victor Hugo","annee": 1862},
}
# 2) modification 2 eme livre annee
#books["livre2"]["annee"]=2020
#print(books)
# 3) Ajouter une clé 'pages' pour chaque livre
#books["livre1"]["pages"] = 46
#books["livre2"]["pages"] = 200
#books["livre3"]["pages"] = 400
#print(books)
#print(books)
# 4) afficher tous les livres
print("tous les livres:")
for keys,values in books.items():
    print(keys,values)
# 5) afficher titre et auteur et anee de chaque livre
print("afficher titre et auteur  de chaque livre:")
for keys,values in books.items():
    print("le livre :",keys,",","le titre:",values["titre"],",","l'auteur:",values["auteur"])