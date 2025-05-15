
import numpy as np

def testNdim():
    list = np.array([[12, 15, 16], [18, 17, 1], [19, 14, 13]])
    print(f"**************L'attribut ndim(nombre dimension)***********************")
    print(f"Donne le nombre de dimension contenues dans NdArray.")
    print(f"Tableau Original:")
    print(f"{list}")
    print(f"Tableau ndim:")
    print(f"{list.ndim}")