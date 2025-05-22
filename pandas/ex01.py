import pandas as pd

df=pd.read_csv(r'C:\Users\Yunes\PycharmProjects\TestDeCours\PYTHON\lungcancer\cancer.csv')
#print(f"la taille :{df.shape}")
#print(f"data culemns:{df.columns}")
#print(f"Description : {df.describe(include='all')}")
#print(df.to_string())
#df['AGE'].value_counts()
#print(f"le nombre des AGS:{df['AGE'].value_counts()}")
print(f"Groupe by colonne :{df.groupby(['AGE'])}")
print(f"Groupe by colonne :{df.groupby(['AGE']).sum()}")
