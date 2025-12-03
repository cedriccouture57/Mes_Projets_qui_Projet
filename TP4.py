# code
#Cédric couture

# Binouche

from math import pi
import random
from dataclasses import dataclass

class StringFoo:
    def __init__(self):
        self.message = ""

    def set_string(self):
        self.message = input("message: ")

    def print_string(self):
        print(f"{self.message.upper()}")


stringfoo = StringFoo()
stringfoo.set_string()
stringfoo.print_string()


class Rectangle:
    def __init__(self):
        self.largeur = None
        self.longueur = None

    def calcul_aire(self):
        self.largeur = input("Largeur: ")
        self.longueur = input("Longeur: ")

    def afficher_infos(self):
        print(float(self.largeur) * float(self.longueur))


rectangle = Rectangle()
rectangle.calcul_aire()
rectangle.afficher_infos()


class Cercle:
    def __init__(self):
        self.rayon = None

    def calcul_aire(self):
        self.rayon = input("Rayon: ")
        return float(self.rayon) * float(self.rayon) * pi

    def calcul_circonference(self):
        return float(self.rayon) * pi * 2


cercle = Cercle()
print(f"Aire: {cercle.calcul_aire()}")
print(f"Circonférence: {cercle.calcul_circonference()}")


@dataclass
class DonneesDnD:
    force: int = random.randint(1,20)
    dex:  int = random.randint(1,20)
    con:  int = random.randint(1,20)
    intelligence:  int = random.randint(1,20)
    wis:  int = random.randint(1,20)
    cha:  int = random.randint(1,20)

class Hero:
    def __init__(self, nom):
        self.nb_vie = random.randint(1, 10) + random.randint(1, 10)
        self.force_atk = random.randint(1, 6)
        self.force_def = random.randint(1, 6)
        self.nom = nom
        self.stats = DonneesDnD()

    def atk(self):
        return random.randint(1,6) + self.force_atk

    def deff(self, dmg_recu):
        if dmg_recu <= self.force_def :
            print("Youppi tu n'as pas pris de dégats")
        else:
            self.nb_vie -= dmg_recu - self.force_def

    def est_vivant(self):
        return self.nb_vie > 0


h = Hero("Cédric")

dommage = h.atk()
h.nb_vie = 11

if h.est_vivant():
   print("Youhou!")
else:
    print("RIP!")



stats = DonneesDnD()

