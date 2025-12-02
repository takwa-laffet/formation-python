#gestion d'err
#valeurError 

#x=int("abc")
""" x=int("abc")
print(x) """
# Traceback (most recent call last):
#  File "C:\Users\takwa\python\s2\gestionerr.py", line 3, in <module>
#    x=int("abc")
#      ^^^^^^^^^^
#ValueError: invalid literal for int() with base 10: 'abc' 
""" try:
    x=int("abc")
except ValueError:
    print("erreur!")
 """

try:
    open("takwa.txt")
except :
    print("fichier introuvable")
finally:
    print("fichier ouvert")