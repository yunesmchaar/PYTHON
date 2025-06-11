#Exercice 1 : Écrire une fonction qui prend une liste de nombres et retourne la moyenne.
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
def moyenne():
    listnom=[]
    listmoy=[]
    nb=int(input("Donner le nombre des etudiants:"))
    for i in range(nb):
         nom=input("Donner le nom d'un etudiant:")
         listnom.append(nom)
         nbr=int(input("Donner les nombres des matieres:"))
         som=0
         for j in range(nbr):
             note=float(input("Donner note:"))
             som=som+note
         my=som/nbr
         listmoy.append(my)
    print(listnom)
    print("-----------------------------------------------------------------------------")
    print(listmoy)
    df=pd.DataFrame({
         "Nom:":listnom,
         "note:":listmoy
        })
    df.to_csv("note_etudiant.csv",index=False,encoding='utf-8-sig')
    print(f"les resultats et enregetre dans le fichier note_etudiant.csv")
    return df
donne=moyenne()
plt.plot(donne["Nom"],donne["note"])
plt.title("statistique des notes des etudiants")
plt.xlabel("Axe x")
plt.ylabel("Axe y")
plt.show()


