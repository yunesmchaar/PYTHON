import numpy as np
arr = np.array([1,2,3,4,5])
print("arr")

print(f"{type(arr)}")
print(np.__version__)

arr= np.array(42)
print(f"Nombre de Dimension :{arr.ndim}")
print(f"Tableau de zero arrays:{arr}")

arr=np.array([1,2,3])
print(f"Nombre de Dimension :{arr.ndim}")
print(f"Tableau de 1-D dimension arrays:{arr}")

arr=np.array([[1,2,3],[1,5,8]])
print(f"Nombre de Dimension :{arr.ndim}")
print(f"Tableau de 2-D dimension arrays:{arr}")

arr=np.array([[[1,2,3],[1,8,1],[1,9,3]],[[1,2,3],[3,6,9],[1,7,8]]])
print(f"Nombre de Dimension :{arr.ndim}")
print(f"Tableau de 2-D dimension arrays:{arr}")

arr=np.array([[12,16,18],[16,19,10]],ndmin=3)
print(f"Tableau de 3-D dimension autre methode de creation :{arr}")