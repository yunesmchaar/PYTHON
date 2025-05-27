from tkinter.font import names
from unittest.mock import inplace
#importation de pandas
import pandas as pd
#importation de numpy
import numpy as np
#lecture de fichier de donne apartier de URL
df=pd.read_csv(r"C:\Users\Yunes\PycharmProjects\TestDeCours\PYTHON\Le270525\CarPrice_Assignement.csv")
#convertir le fichier en forme de tableau
tab=np.array(df)
print(f"Affichage de 5 premier element {df.head()}")
print(f" columns {df.columns}")
print(f"{df.shape}")
#lire les  5 derniere elements de la liste
for i in range(len(tab)):
    if i>200:
        print(f"Affichage de derniere element de la liste {tab[i]}")

# 5- Afficher les informations sur le dataframe
print(df.info())

# 6- Valeurs distinctes des variables qualitatives
for col in df.select_dtypes(include=['object']).columns:
    print(f"{col}: {df[col].unique()}")


#creer outre columns
cars={
    'car_ID':[],
    'CarName':[],
    'doornumber':[],
    'carbody':[],
    'carlength':[],
    'carwidth':[],
    'carheight':[],
    'cylindernumber':[],
    'price':[]
}
mycars=pd.DataFrame(cars)
print(f"{mycars.head()}")
#transformer un fichier reel
mycars.to_csv('cars.csv',index=True)
#supprimer de column carbody
mycars.drop(['carbody'],axis=1,inplace=True)
print(mycars.head())
#mycars.add[3]('x',axis=1,inplace=True)
mycars['doornumber']=['4']


# Nommer x la variable carbody de DF
x = cars['carbody']

# Catégories de 'doornumber'
print(mycars['doornumber'].unique())

# Nombre de voitures par catégorie
print(mycars['doornumber'].value_counts())

# Supprimer les lignes avec valeurs manquantes
DF_clean = mycars.dropna()

# Compter les répétitions pour 'price'
print(mycars['price'].value_counts())