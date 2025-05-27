import pandas as pd
import matplotlib.pyplot as plt
from numpy.ma.core import append



df=pd.read_csv(r"C:\Users\Yunes\PycharmProjects\TestDeCours\PYTHON\pandas\DATA.csv")

print(f"Affiche les premier element dans le fichier Data.csv {df.head()}")
print(f"Afficher les columns :")
print(df.columns)
print(f"utilise pour affechier les nombres des columns et les lines shape:{df.shape}")
print(f"decripe:{df.describe()}")
print(f"{df}")

list=[]

for i in range(len(df)):
    list.append(i)
print(list)

#plt.plot(list,df['TotalInfected'],'-r',mec='r',mfc='k',label='Infected')
plt.pie(df['TotalInfected'], list, autopct='%1.1f%%')
plt.title("Diagramme des Infections")
plt.xlabel("Axe x")
plt.ylabel("Axe y")
#plt.legend()
#plt.grid(True)
plt.tight_layout()
plt.show()

