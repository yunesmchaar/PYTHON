import numpy as np
def testShap():
    print(f"Hello Shape")
    print(f"C'est quoi Shape de Numpy?")
    print(f"Shape : -trouve la forme d'un tableau")
    print(f"-Donne cette information sous forme de tuple,c'est-a-dire une liste entre parentheses qu'on ne peut pas changer")
    print(f"Exemple de test :")
    #list=np.array([12,15,18,20,10])
    #print(f"les information sous forme de tuple :{list.shape}")
    list=np.array([[12,15,16],[18,17,1],[19,14,13]])
    print(f"les information sous forme de tuple : {list.shape}")

