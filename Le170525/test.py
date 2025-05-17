import numpy
import random
choices=["Ajouter","Modifier","Supprimer","Quitter"]
for i,choice in enumerate (choices,1):
    print(f"{i}.{choice}")
#c'est fonction pour demende a le telisateur de demmende un choice et apre donne le message l'inscreption
def Choice():
    print("Choice votre option!")

    choices=["Football","Basketball","Tennis","Natation"]

    for i,choice in enumerate (choices,1):
        nb = int(input("Votre option:"))
        i=nb
        print(f"{i}.{choice}")
        if nb==1 :
            print(f"Bravo,dans le club Football")
            break
        elif nb == 2 :
            print(f"Bravo,dans le club Basketball")
            break
        elif nb==3:
            print(f"Bravo,dans le club Tennis")
            break
        else:
            print(f"Bravo,dans le club Natation")
            break
Choice()


