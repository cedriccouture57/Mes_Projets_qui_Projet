'''

Code pour un jeu de devinette de chiffre de 1:1000
-Cédric Couture

'''

import random
devinette = random.randint(1, 1000)
binouche = int(input('Réponse :'))
while binouche != devinette :

    if binouche == devinette :
        print(f'Brazooooo! Le Numéro étais bien {devinette}')

    elif binouche <= devinette :
        print("Bah non c'est plus grand hehehe ")

    else :
        print("Bah non c'est plus petit hehehe ")

    binouche = int(input('Réponse :'))