import pandas as pd
df = pd.read_csv(r'C:\Users\Yunes\PycharmProjects\TestDeCours\PYTHON\cours\archive (1)\athlete_events.csv')

print("le Resultat est:")
df.shape
print(f"{df.to_string()}")