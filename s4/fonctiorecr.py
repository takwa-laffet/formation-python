n=int(input("donner n\n"))
"""def somme(n):
  s=0
  for i in n:
    s= s+int(i)
  print(s)
somme(n) """
# fonction recursive pour trouver la somme des chiffres d'un nombre
""" def somme(n):
    if n<10:
        return n
    else:
        return n%10 + somme(n//10)
print(somme(n))
 """
#somme(12)
#1+somme(2)
#1+2
#factorielle normale
""" 
n = int(input("n = "))
fact = 1
for i in range(1, n + 1):
    fact *= i
print("Factorielle =", fact) """

#factorielle recursive
def factorielle(n):
    if n ==0:
        return 1
    else:
        return n*factorielle(n-1)
print(factorielle(n))
#sys.setrecursionlimit(1000) cette linge modifie la limite
#  !!!!!! atention la limite de memoire