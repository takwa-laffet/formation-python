from abc import ABC, abstractmethod
class Animal(ABC):
    @abstractmethod
    def parler(self):
        print("HI")
    def Zoom(self):
        print("Zoom")
class Chien(Animal):
    def parler(self):
        print("wouf wouf")
class Chat(Animal):
    def parler1(self):
        print("mewo mewo")
c=Chien()
c.parler()
chat=Chat()
chat.parler()
chat.Zoom()
