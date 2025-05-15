
import numpy as np
def Rechape():
    Tab=[]
    for i in range(12):
        nb=int(input("Entres l'elements:"))
        Tab.append(nb)
    print(f"Le Tableau Original:{Tab}")
    array=np.array(Tab)
    Reshap=array.reshape((3,4))
    print(f"Tableau Reshape:{Reshap}")

Rechape()