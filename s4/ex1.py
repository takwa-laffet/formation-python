from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def parler(self):
        pass

class Chien(Animal):
    def parler(self):
        print("wouf wouf ")

class Chat(Animal):
    def parler(self):
        print("mewo mewo")

animaux = [Chien(), Chat()]
for a in animaux:
    a.parler()
