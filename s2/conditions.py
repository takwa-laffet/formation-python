""" a=int(input("donner a\n"))
b=int(input("danner b\n"))
 """
""" 
if a>b:
  s=a+b
  if a>0:
    print("a est plus grand que b et plus grand que 0")
  elif a<0:
    print("a est plus grand que b et plus petit que 0")
  print("a est plus grand que b")
elif a<b:
    print("a est plus petit que b")
    if a>0:
      print("a est plus petit que b et plus grand que 0")  
else:
  print("a est egale a b")

 """
""" a=int(input("donner a\n"))
b=int(input("danner b\n"))

if(a>b):
    somme=a+b
    print("a est plus grand que b")
    if(a>0):
      print("a est plus grand que b et plus grand que 0")
      print("la somme",somme)
    elif(a<0):
       print("a est plus grand que b et plus petit que 0")
       print("la somme",somme)
elif(a==b):
   print("a est egale a b")
else:
    print("b est plus grand que a")
 """

#i=1

""" for i in range(10):
  print(i) 
 """
""" fruits=["apple","banana","cherry","banana"]
for x in fruits:
   if fruits.count(x)==2:
       print(x,"est present 2 fois")       
    
   else:
       print(x)
  """""" 
color=["rouge","vert","bleu"]
legume=["tomate","carotte","pomme de terre"]
for x in color:
    for y in legume:
        print(x,y)
        continue """
#boucle while afficher chaque couleur avec chaque legume
color=["rouge","vert","bleu"]
legume=["tomate","carotte","pomme de terre"]

element=0
while element < len(color) and element<len(legume):
    print(color[element],legume[element])
    element+=1


""" 
s=0
while s <= len(color):
    print(s)
    s+=1 """

