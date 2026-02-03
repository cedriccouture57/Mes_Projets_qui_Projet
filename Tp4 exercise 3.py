from dataclasses import dataclass
import random
@dataclass
class Item:
    nom: str
    qte: int


class SacADos:
    def __init__(self):
        self.liste_item = []

    def ajouter_item(self, item_a_ajouter: Item):
        if len(self.liste_item) == 0:
            # vide, donc ajouter sans vérification
            self.liste_item.append(item_a_ajouter)
        else:
            for item in self.liste_item:
                if item.nom == item_a_ajouter.nom:
                    item.qte += item_a_ajouter.qte
                else :
                    self.liste_item.append(item_a_ajouter)


sad = SacADos()
sad.ajouter_item(Item("or", 5))
sad.ajouter_item(Item("or", 10))
sad.ajouter_item(Item("argent", 10))

print(sad.liste_item)
