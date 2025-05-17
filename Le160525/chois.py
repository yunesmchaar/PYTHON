import numpy
import random
#utilise la biliotheque numpy avec import random
#premiere exemple pour un liste simple
lis=[10,16,13,10]
result=random.choice(lis)
print(result)
result= numpy.random.choice(lis,size=2)
print(f"result={result}")

result=numpy.random.choice(lis,size=2,replace=False)
print(f"Result={result}")
proba=[0.1, 0.2, 0.6, 0.1]
result = numpy.random.choice(lis, size=4, p=proba,replace=False)  # ✅ Ce serait bon en fait si les longueurs matchent !
print(f"result:{result}")

result = random.choices(lis,weights=proba,k=2)
print(f"resultat:{result}")