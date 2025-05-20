import pandas as pd

data = pd.read_csv(r'C:\Users\Yunes\PycharmProjects\TestDeCours\PYTHON\cours\archive (1)\athlete_events.csv')

def conso(x):
    if x < 18:
        return 'Mineur'
    elif (x >= 18) & (x < 40):
        return 'Adulte'
    else:
        return 'Vieux'

data['Age'] = data['Age'].map(conso)
print(data.loc[20:60, 'Age'])
