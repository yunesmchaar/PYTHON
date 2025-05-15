
import numpy as np

def testZeros_like():
    list = np.array([[12, 15, 16], [18, 17, 1], [19, 14, 13]])
    print(f"****************le constructeur Zeros_like()********************")
    print(f"cree un nouveau tableau rempli de zeros ,qui a la meme forme et le meme type de donnees que le tableau a.")
    print(f"Tyntaxe: np.zeros_like(a,dtype=None)")
    print(f"a:tableau de reference")
    print(f"dtype(optionnel):type des donnees a utiliser.")
    print(f"Tableau Original:")
    print(f"{list}")
    print(f"Tableau zeros_like(a,dtype=None):")
    print(f"{np.zeros_like(list,dtype=None)}")
