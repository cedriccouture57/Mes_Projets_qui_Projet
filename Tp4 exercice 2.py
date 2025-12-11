import random
pouette = int
class Npc:
    def __init__(self, force, agilite ,constitution, intelligence, sagesse, charisme):
        self.force = force
        self.agilite = agilite
        self.constitution = constitution
        self.intelligence = intelligence
        self.sagesse = sagesse
        self.charisme = charisme
        self.armure = random.randint(1,12)
        self.nom = "poteto"
        self.race = "acier inoxydable"
        self.espece = "porte"
        self.pv = random.randint(1,20)
        self.profession = "portier"

    def afficher_stats(self):
        print(f"Force = {self.force} agillite = {self.agilite} constitution = {self.constitution} intelligence = {self.intelligence} sagesse = {self.sagesse} charisme = {self.charisme}")




def binouche():
    de = [random.randint(1,6), random.randint(1,6), random.randint(1,6), random.randint(1,6)]
    de.sort(reverse=True)

    pouette = de[0] + de[1] + de[2]

binouche()
Npc.force = pouette
binouche()
Npc.agilite = pouette
binouche()
Npc.constitution = pouette
binouche()
Npc.intelligence = pouette
binouche()
Npc.sagesse = pouette
binouche()
Npc.charisme = pouette

