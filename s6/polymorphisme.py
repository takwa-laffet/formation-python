class Animal:
    def parler(self):
        print ("un animal fait un bruit")
class Chien(Animal):
    def parler(self):
        print("wouf wouf")
class Chat(Animal):
    def parler(self):
        print("mewo mewo")
#methode 1
""" animaux = [Chien(),Chat(),Animal()]
for a in animaux:
    a.parler() """

#methode 2
def fparler(p):
    p.parler()
chat = Chat()
chien= Chien()
animaux =Animal()
fparler(chat)
fparler(chien)
fparler(animaux)