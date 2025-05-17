from numpy import random
import numpy as np

x=np.array( [10,18,15])
print(f"de dimension:{x.ndim}")
print(f"le Tab:{x}")

x=np.array( [[10,18,15],[10,14,18]])
print(f"de dimension:{x.ndim}")
print(f"le Tab:{x}")

x=np.array( [[[10,18,15],[10,14,18]],[[1,2,3],[1,5,4]]])
print(f"de dimension:{x.ndim}")
print(f"le Tab:{x}")

x=np.array( [10,18,15],ndmin=2)
print(f"de dimension:{x.ndim}")
print(f"le Tab:{x}")

y=random.randint(1,19,)
print(f"de dimension:{y.ndim}")
print(f"le Tab:{y}")




