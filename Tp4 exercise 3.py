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
            item_trouve = False
            for item in self.liste_item:
                if item.nom == item_a_ajouter.nom:
                    item.qte += item_a_ajouter.qte
                    item_trouve = True

            if not item_trouve:
                self.liste_item.append(item_a_ajouter)

    def retirer_item(self, item_a_enlever: Item):
        if len(self.liste_item) == 0:
            return

        for item in self.liste_item:
            if item.nom == item_a_enlever.nom:
                item_restant = item.qte - item_a_enlever.qte
                if item_restant < 0:
                    print("Ohalala tu est pauvre mon homme tu en a pas assez pour en retirer")
                    break
                elif item_restant > 0:
                    item.qte = item_restant
                else:
                    self.liste_item.remove(Item(item.nom, item.qte))


sad = SacADos()
sad.ajouter_item(Item("or", 5))
sad.ajouter_item(Item("or", 10))
sad.ajouter_item(Item("argent", 10))
sad.ajouter_item(Item("argent", 10))
sad.retirer_item(Item("argent", 20))
print(sad.liste_item)
