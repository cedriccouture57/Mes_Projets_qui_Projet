import random


def calcul_stats():
    de = [random.randint(1,6), random.randint(1,6), random.randint(1,6), random.randint(1,6)]
    de.sort(reverse=True)

    return de[0] + de[1] + de[2]


class Npc:
    def __init__(self):
        self.force = calcul_stats()
        self.agilite = calcul_stats()
        self.constitution = calcul_stats()
        self.intelligence = calcul_stats()
        self.sagesse = calcul_stats()
        self.charisme = calcul_stats()
        self.armure = random.randint(1,12)
        self.nom = ""
        self.race = ""
        self.espece = ""
        self.pv = random.randint(1,20)
        self.profession = ""

    def afficher_stats(self):
        print(f"Force = {self.force} agillite = {self.agilite} constitution = {self.constitution} intelligence = {self.intelligence} sagesse = {self.sagesse} charisme = {self.charisme}")


n = Npc()
n.afficher_stats()


class Kobold(Npc):
    def __init__(self, nom):
        super().__init__()
        self.race = "Kobold"
        self.nom = nom

    def afficher_stats(self):
        print(f"Nom = {self.nom}")
        super().afficher_stats()



# faire hero et cible la meme chose que kobold pouette binouche touppi et binou

k = Kobold("Binouche")
k.afficher_stats()

