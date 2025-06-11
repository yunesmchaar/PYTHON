#Exercice 2 : Trier une liste de dictionnaires par une clé donnée (ex. : âge).

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


def Calcule_moy(liste):
    if not liste:
        return 0
    return sum(liste)/len(liste)
liste=[10,17,13,18]

result =Calcule_moy(liste)

print(f"la moyenne des notes est:{result}")

df=pd.DataFrame({
    "Note":[result]
    })

df.to_csv("result_note.csv",index=False,encoding='utf-8-sig')
print("\n le fichier et exist result_note.csv")
