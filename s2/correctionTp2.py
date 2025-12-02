# Ex 1: Créer une liste contenant vos 5 fruits préférés et l’afficher.
fruits = ["pomme", "banane", "fraise", "mangue", "kiwi"]
print(fruits)

# Ex 2: Ajouter un élément à une liste existante avec append().
fruits.append("orange")
print(fruits)

# Ex 3: Supprimer un élément d’une liste avec remove().
fruits.remove("kiwi")  # lève ValueError si absent
print(fruits)

# Ex 4: Afficher le premier et le dernier élément d’une liste.
print("Premier:", fruits[0])
print("Dernier:", fruits[-1])

# Ex 5: Compter combien de fois un élément apparaît dans une liste.
n = fruits.count("banane")
print("banane apparait", n, "fois")

# Ex 6: Trier une liste de nombres dans l’ordre croissant.
nums = [5, 2, 9, 1, 7]
nums.sort()
print(nums)

# Ex 7: Inverser une liste.
nums.reverse()
print(nums)

# Ex 8: Créer une liste de 10 nombres pairs avec range().
pairs = list(range(0, 20, 2))  # 0..18 -> 10 nombres pairs
print(pairs)

# Ex 9: Vérifier si un élément est présent dans une liste avec in.
print("pomme" in fruits)  # True/False

# Ex 10: Parcourir une liste et afficher chaque élément.
for f in fruits:
    print(f)
# Ex 11: Vérifier si un nombre est positif, négatif ou nul.
x = int(input("Nombre: "))
if x > 0:
    print("positif")
elif x < 0:
    print("négatif")
else:
    print("nul")

# Ex 12: Vérifier si un nombre est pair ou impair.
n = int(input("Entier: "))
print("pair" if n % 2 == 0 else "impair")

# Ex 13: Vérifier si une personne est mineure ou majeure selon son âge.
age = int(input("Age: "))
print("majeur" if age >= 18 else "mineur")

# Ex 14: Vérifier si une année est bissextile.
annee = int(input("Année: "))
if (annee % 4 == 0 and annee % 100 != 0) or (annee % 400 == 0):
    print("bissextile")
else:
    print("non bissextile")

# Ex 15: Vérifier si une lettre est une voyelle ou une consonne.
lettre = input("Lettre: ").lower()
if lettre in "aeiouyàâäéèêëîïôöùûü":
    print("voyelle")
else:
    print("consonne")

# Ex 16: Comparer deux nombres et afficher le plus grand.
a = float(input("a: ")); b = float(input("b: "))
if a > b:
    print("plus grand:", a)
elif b > a:
    print("plus grand:", b)
else:
    print("égaux")

# Ex 17: Vérifier si une chaîne contient le mot Python.
s = input("Texte: ")
print("contient 'Python'?" , "python" in s.lower())

# Ex 18: Vérifier si un étudiant est admis (note >= 10) ou recalé.
note = float(input("Note: "))
print("admis" if note >= 10 else "recalé")

# Ex 19: Vérifier si un triangle est équilatéral, isocèle ou scalène.
a = float(input("côté a: ")); b = float(input("b: ")); c = float(input("c: "))
if a == b == c:
    print("équilatéral")
elif a == b or b == c or a == c:
    print("isocèle")
else:
    print("scalène")

# Ex 20: Calculer la réduction selon l’âge (ex : -50% si <12 ans).
age = int(input("Age: "))
prix = float(input("Prix initial: "))
if age < 12:
    prix *= 0.5
print("Prix final:", prix)
# Ex 21: Afficher les nombres de 1 à 10 avec for.
for i in range(1, 11):
    print(i)

# Ex 22: Afficher les nombres pairs de 0 à 20.
for i in range(0, 21, 2):
    print(i)

# Ex 23: Calculer la somme des entiers de 1 à 100.
s = sum(range(1, 101))
print("somme 1..100 =", s)

# Ex 24: Afficher les tables de multiplication de 1 à 10.
for a in range(1, 11):
    for b in range(1, 11):
        print(f"{a}x{b}={a*b}")
    print("---")

# Ex 25: Compter le nombre de voyelles dans une chaîne donnée.
texte = input("Texte: ").lower()
voyelles = sum(1 for ch in texte if ch in "aeiouy")
print("voyelles:", voyelles)

# Ex 26: Afficher les éléments d’une liste avec une boucle for.
L = ["a","b","c"]
for item in L:
    print(item)

# Ex 27: Utiliser une boucle while pour compter jusqu’à 10.
i = 1
while i <= 10:
    print(i)
    i += 1

# Ex 28: Demander à l’utilisateur un mot de passe et répéter jusqu’à ce qu’il tape 1234.
while True:
    pwd = input("Mot de passe: ")
    if pwd == "1234":
        print("Accès accordé")
        break
    else:
        print("Essaye encore")

# Ex 29: Créer une boucle qui s’arrête quand un nombre supérieur à 50 est saisi.
while True:
    v = int(input("Nombre: "))
    if v > 50:
        print("arrêt, >50")
        break

# Ex 30: Calculer la factorielle d’un nombre avec une boucle.
n = int(input("n (>=0): "))
fact = 1
for i in range(2, n+1):
    fact *= i
print(f"{n}! =", fact)
# Ex 31: Utiliser range() pour afficher les nombres de 5 à 15.
for i in range(5, 16):
    print(i)

# Ex 32: Afficher les multiples de 3 entre 0 et 30.
for i in range(0, 31, 3):
    print(i)

# Ex 33: Utiliser continue pour ignorer le nombre 5 dans une boucle.
for i in range(1, 11):
    if i == 5:
        continue
    print(i)

# Ex 34: Utiliser break pour arrêter la boucle quand le nombre atteint 7.
for i in range(1, 20):
    if i == 7:
        break
    print(i)

# Ex 35: Afficher les 10 premiers nombres impairs.
count = 0
i = 1
while count < 10:
    print(i)
    i += 2
    count += 1

# Ex 36: Parcourir une liste et arrêter à la première occurrence de la valeur 0.
lst = [3,2,0,5,0]
for x in lst:
    if x == 0:
        print("trouvé 0, arrêt")
        break
    print(x)

# Ex 37: Afficher uniquement les nombres pairs entre 1 et 20 avec continue.
for i in range(1, 21):
    if i % 2 != 0:
        continue
    print(i)

# Ex 38: Utiliser range() pour créer une liste de carrés de 1 à 10.
carrés = [i*i for i in range(1, 11)]
print(carrés)

# Ex 39: Parcourir une chaîne et ignorer les espaces avec continue.
s = "bonjour tout le monde"
for ch in s:
    if ch == " ":
        continue
    print(ch, end="")
print()

# Ex 40: Simuler un compte à rebours de 10 à 0.
import time
for t in range(10, -1, -1):
    print(t)
    # time.sleep(1)  # décommentez pour pause réelle
