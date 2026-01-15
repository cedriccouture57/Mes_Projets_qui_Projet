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

class Hero(Npc):

    def __init__(self, nom):
        super().__init__()
        self.race = ("Humain")
        self.nom = nom
    def attaquer(self, cible):
        print(f"{self.nom} attaque {cible.nom}.")
        attaque = random.randint(1,20)
        if attaque == 20:
            cible.subir_dommage(random.randint(1, 8))
        elif attaque == 1:
            print("Pouah! Tu es misérable.")
        else:
            if attaque >= cible.armure:
                cible.subir_dommage(random.randint(1, 6))
            else:
                print("Holala ta rater pouette pouette")

class George(Npc):
    def __init__(self):
        super().__init__()
        self.race = "Humain"
        self.nom = "Ennemi"

    def subir_dommage(self, qte):
        print(f"Subit {qte} dommage(s)")


h = Hero("Cédric")
g = George()
g2 = George()
g2.nom = "Trump"

h.attaquer(g2)

h.attaquer(g)