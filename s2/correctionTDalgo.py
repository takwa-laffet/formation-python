# 1. Table de multiplication
n = int(input("Donnez un nombre: "))
for i in range(1, 11):
    print(n, "x", i, "=", n * i)

# 2. 10 premiers nombres naturels en ordre décroissant
for i in range(10, 0, -1):
    print(i, end=" ")
#methode 2 
# Initialiser le compteur à 10 (le plus grand nombre)
i = 10

# Tant que i est supérieur ou égal à 1
while i >= 1:
    print(i, end=" ")
    i -= 1  # diminuer i de 1 à chaque tour


# 3. 20 premiers nombres premiers
count = 0
num = 2
while count < 20:
    is_prime = True
    for j in range(2, num):
        if num % j == 0:
            is_prime = False
            break
    if is_prime:
        print(num, end=" ")
        count += 1
    num += 1

# 4. Factorielle
n = int(input("n = "))
fact = 1
for i in range(1, n + 1):
    fact *= i
print("Factorielle =", fact)

# 5.Fibonacci
a, b = 0, 1
for i in range(10):
    print(a, end=" ")
    a, b = b, a + b

# 6. Vérifier palindrome (chaîne)
s = input("Donnez une chaîne: ")
inverse = ""
for c in s:          # on parcourt chaque caractère
    inverse = c + inverse   # on ajoute devant au lieu d'ajouter derrière
if s == inverse:
    print("Palindrome")
else:
    print("Pas palindrome")

# 7. Compter mots dans une phrase
phrase = input("Phrase: ")
count = 1
for c in phrase:
    if c == " ":
        count += 1
print("Nombre de mots:", count)

# 8. Mot inverse
s = input("Donnez un mot: ")
inverse = ""
for c in s:        
    inverse = c + inverse  
print(inverse)
# 9. Compter lettre donnée
phrase = input("Phrase: ")
lettre = input("Lettre: ")
cpt = 0
for ch in phrase:
    if ch == lettre:
        cpt += 1
print("Apparaît", cpt, "fois")

# 10. Supprimer espaces
ch = input("Chaîne: ")
nouveau = ""
for c in ch:
    if c != " ":
        nouveau += c
print(nouveau)

# 11. Chaque mot sur une ligne
phrase = input("Phrase: ")
mot = ""
for c in phrase:
    if c != " ":
        mot += c
    else:
        print(mot)
        mot = ""
print(mot)

# 12. Somme diagonales matrice n*n
n = int(input("Taille: "))
mat = []
for i in range(n):
    ligne = []
    for j in range(n):
        ligne.append(int(input(f"Entrez mat[{i}][{j}]: ")))
    mat.append(ligne)
    
s = 0
for i in range(n):
    s += mat[i][i] + mat[i][n-1-i]
print("Somme diagonales =", s)

# 13. Couples (i, j) entre 1 et 5
for i in range(1, 6):
    for j in range(1, 6):
        print("(", i, ",", j, ")", end=" ")

# 14. Table de multiplication tableau
for i in range(1, 11):
    for j in range(1, 11):
        print(i*j, end="\t")
    print()

# 15. Triangle de Pascal
n = int(input("Nombre de lignes: "))
for i in range(n):
    val = 1
    for j in range(i+1):
        print(val, end=" ")
        val = val * (i - j) // (j + 1)
    print()

# 16. PPCM
a = int(input("a = "))
b = int(input("b = "))
ppcm = a if a > b else b
while True:
    if ppcm % a == 0 and ppcm % b == 0:
        break
    ppcm += 1
print("PPCM =", ppcm)

# 17. PGCD
a = int(input("a = "))
b = int(input("b = "))
pgcd = 1
for i in range(1, min(a, b)+1):
    if a % i == 0 and b % i == 0:
        pgcd = i
print("PGCD =", pgcd)

# 18. Nombre parfait
n = int(input("n = "))
s = 0
for i in range(1, n):
    if n % i == 0:
        s += i
if s == n:
    print("Nombre parfait")
else:
    print("Pas parfait")

# 19. Nombre Armstrong
n = int(input("n = "))
s = 0
m = n
d = 0
tmp = m
while tmp > 0:
    d += 1
    tmp //= 10
tmp = m
while tmp > 0:
    r = tmp % 10
    p = 1
    for i in range(d):
        p *= r
    s += p
    tmp //= 10
if s == n:
    print("Armstrong")
else:
    print("Pas Armstrong")

# 20. Suite de Collatz
n = int(input("n = "))
while n != 1:
    print(n, end=" ")
    if n % 2 == 0:
        n //= 2
    else:
        n = 3*n + 1
print(1)

# 21. Nombres premiers jusqu’à 1000
for num in range(2, 1001):
    is_prime = True
    for j in range(2, num):
        if num % j == 0:
            is_prime = False
            break
    if is_prime:
        print(num, end=" ")

# 22. Puissance a^b avec boucle
a = int(input("a = "))
b = int(input("b = "))
res = 1
for i in range(b):
    res *= a
print("a^b =", res)

# 23. Moyenne série de nombres (-1 pour arrêter)
s = 0
c = 0
while True:
    n = int(input("Donnez un nombre (-1 fin): "))
    if n == -1:
        break
    s += n
    c += 1
print("Moyenne =", s/c)

# 24. Pyramide numérique
for i in range(1, 10):
    print(str(i) * i)

# 25. Premier nombre >1000 divisible par 17,19,23
n = 1001
while True:
    if n % 17 == 0 and n % 19 == 0 and n % 23 == 0:
        print(n)
        break
    n += 1

# 26. Triangle d’étoiles
n = int(input("Hauteur: "))
for i in range(1, n+1):
    print("*" * i)

# 27. Suite de Collatz (bis)
n = int(input("n = "))
while n != 1:
    print(n, end=" ")
    if n % 2 == 0:
        n //= 2
    else:
        n = 3*n + 1
print(1)

# 28. Pyramide nombres (même que 24)
for i in range(1, 10):
    print(str(i) * i)

# 29. Couples (i,j) 1 à 5 (même que 13)
for i in range(1, 6):
    for j in range(1, 6):
        print("(", i, ",", j, ")", end=" ")

# 30. Nombres premiers ≤ n
n = int(input("n = "))
for num in range(2, n+1):
    prime = True
    for j in range(2, num):
        if num % j == 0:
            prime = False
            break
    if prime:
        print(num, end=" ")

# 31. Nombre palindrome
n = int(input("n = "))
m = n
inv = 0
while m > 0:
    r = m % 10
    inv = inv*10 + r
    m //= 10
if inv == n:
    print("Palindrome")
else:
    print("Pas palindrome")

# 32. Somme chiffres pairs
n = int(input("n = "))
s = 0
while n > 0:
    d = n % 10
    if d % 2 == 0:
        s += d
    n //= 10
print("Somme chiffres pairs =", s)

# 33. Nombres divisibles par 7 mais pas 5
c = 0
for i in range(1, 1001):
    if i % 7 == 0 and i % 5 != 0:
        c += 1
print(c)

# 34. Générer mot de passe aléatoire
import random
chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
n = int(input("Longueur: "))
pwd = ""
for i in range(n):
    pwd += chars[random.randint(0, len(chars)-1)]
print("Mot de passe:", pwd)

# 35. Position première voyelle
mot = input("Mot: ")
pos = -1
voyelles = "aeiouyAEIOUY"
for i in range(len(mot)):
    if mot[i] in voyelles:
        pos = i
        break
print("Position =", pos)

# 36. 20 Fibonacci et vérifier pairs
a, b = 0, 1
for i in range(20):
    print(a, "(pair)" if a % 2 == 0 else "(impair)")
    a, b = b, a + b

# 37. FizzBuzz
for i in range(1, 101):
    if i % 15 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)
