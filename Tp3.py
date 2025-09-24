#combat de monstre hehe
#Par Cédric couture
import random
win = 0
loss = 0
lancer_de = random.randint(1,6)
niveau_vie = 20

choix_jeux = int(input("1- Combattre cet adversaire \n2- Contourner cet adversaire et aller ouvrir une autre porte "
                       "\n3- Afficher les règles du jeu \n4- Quitter la partie \n Quel est votre choix ?:"))

force_adversaire = random.randint(1,6)
#print(f'Vous tombez face à face avec un adversaire de difficulté :{force_adverasire}')
    while choix_jeux = "1" :
        if choix_jeux == "1":
            print("Vous décidez de combatre le monstre")
            print(f"Le monstre a {force_adversaire}")

    if lancer_de >= force_adversaire :
        print("vous avez gagner ce combat")
        win = +1
    elif lancer_de < force_adversaire :
        print("Oh non tu a perdu !")
        loss = +1
