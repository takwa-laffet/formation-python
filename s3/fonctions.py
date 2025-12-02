""" def saluer():
    print("salut")

for i in range(3):
    saluer()
 """#pourquoi utliser des fonctions?
#1) pour éviter de repéter meme code plusieurs fois
#2)pour pouvoir corriger ou modifier  plus simple 
#3) pour reutliser le code dans différents programmes 
#4)pour rendre le code plus organisé et plus facile a lire 

#les fonctions les parametres
""" def saluer(nom,pernom,age):
    print("salut",nom ," ",pernom)
    print("vous avez",age,"ans") """
"""
h=input("donnez mois votre nom : ")
p=input("donnez mois votre prenom : ")
a=int(input("donner mois votre age : "))
nom="sara"
saluer("sara",p,23)
 """
""" def calculer_moyenne(n1,n2,coff,nometudiant,matieres):
    m=(n1+n2)/coff
    return m,coff, n1,n2,print("la moyenne de",nometudiant,"dans la matiere",matieres,"est",m)
calculer_moyenne(20,30,2,"sara","math")

saluer("sara","ali",calculer_moyenne(20,30,2,"sara","math")) """
""" 
note1=int(input("donnez la note 1 : "))
note2=int(input("donnez la note 2 : "))
coff=int(input("donnez le coefficient : "))
nom=input("donnez le nom de l etudiant : ")
matiere=input("donnez la matiere : ")
calculer_moyenne(note1,note2,coff,nom,matiere) """

#les fonctions les parametres par defaut
""" def dire_bonjour(nom="sara"):
    print("bonjour",nom)
pernom=input("donnez votre nom : ")
dire_bonjour(pernom)
#dire_bonjour("nourhen")
#dire_bonjour()
 """
a,b=int(input("donnez deux nombres :"))