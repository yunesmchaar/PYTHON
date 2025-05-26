import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv(r"C:\Users\Yunes\PycharmProjects\TestDeCours\PYTHON\Matplotlib\cars.csv")

print(f"le resultat en resume {df.shape}")
print(f"les columns dans un ficheir est {df.columns}")