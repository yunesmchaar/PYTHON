import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

noms={
    'nom':["Alice","Bob","Claire"],
    'Age':[25,30,28],
    'ville':["Paris","Lyon","Marseille"]
}
mynoms=pd.DataFrame(noms)
#print(mynoms)

#print(mynoms.columns)
#print(mynoms['nom'])

#age_claire=mynoms[mynoms['nom']=='Claire']['Age'].values[0]
#print(age_claire)

#filtr= mynoms[mynoms['Age']>26]
#print(filtr)

print(mynoms['Age'].describe())