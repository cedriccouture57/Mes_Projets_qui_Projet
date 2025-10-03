#combat de monstre hehe
#Par Cédric couture
import random
win = 0
loss = 0

niveau_vie = 20
play_game = True

while play_game:
    if win % 3 == 0 and not win == 0:
        force_adversaire =random.randint(4,5)
        print(f"Vous avez trouver un adversaire special vous avez  {niveau_vie} hp et le  Boss a {force_adversaire} hp que voulez vous faire ? \n")
    else:
        force_adversaire = random.randint(1,2)
        print(f" Vous avez {win} victoire")
        print(f"Vous avez {niveau_vie} hp et le monstre a {force_adversaire} hp que voulez vous faire ? \n")

    lancer_de = random.randint(1,6)
    ####afficher info monstre et info joueur

    choix_jeux = int(input("1- Combattre cet adversaire \n2- Contourner cet adversaire et aller ouvrir une autre porte "
                           "\n3- Afficher les règles du jeu \n4- Quitter la partie \n Quel est votre choix ?:"))

    if niveau_vie <= 0:
        exit()
    if choix_jeux == 1:
        print(f"\n Vous attaquer l'adversaire infligeant {lancer_de} dégats ")
        if lancer_de > force_adversaire:
            niveau_vie += lancer_de
            win += 1
            print(f" Brazoo vous avez gagnez le combat vous avez maintenant {niveau_vie} hp")
        elif lancer_de <= force_adversaire:
            niveau_vie -= lancer_de
            print(f"Malheureusement l'attaque n'était pas assez puissant le monstre ta battu tu as maintenant {niveau_vie} hp \n")
            loss += 1

    elif choix_jeux == 2:
        niveau_vie -= 1
        pass
    elif choix_jeux == 3:
      print(f"\nLe combat se fait avec un lancer de dé (simulé par un nombre aléatoire entre 1 et 6)\n"
            f"Le niveau de vie de l’usager diminue dans le cas d’une défaite ou augmente lorsqu’il y a victoire.\n"
            f"Et ce, en fonction du niveau de difficulté de l’adversaire.Exemple :\n"
            f"niveau_de_vie de l’usager = 20  et  force_adversaire = 4\n"
            f"Si le dé du joueur donne 4 ou moins, il y a défaite : le niveau d96e vie tombe alors à 16 (20 - 4).\n"
            f"Si le dé du joueur donne 5 ou plus, il y a victoire : le niveau de vie monte alors 992à 24 (20 + 4).\n")

    elif choix_jeux == 4:
        play_game = False

