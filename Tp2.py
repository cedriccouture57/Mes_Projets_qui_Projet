'''

Code pour un jeu de devinette de chiffre de 1:1000
-Cédric Couture

'''
print("Essayez de deviner le chiffre que j'ai choisi hihihi")
import random
devinette = random.randint(1, 1000)
binouche = int(input('Réponse :'))
while binouche != devinette :

    if binouche <= devinette :
        print("Bah non c'est plus grand hehehe ")

    else :
        print("Bah non c'est plus petit hehehe ")

    binouche = int(input('Réponse :'))

if binouche == devinette:
    print(f'Brazooooo! Le numéro étais bien {devinette}')
