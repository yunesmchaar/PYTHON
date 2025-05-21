import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import random

heures = list(range(6, 19))
temperatures = [12, 14, 15, 17, 20, 22, 23, 22, 21, 20, 18, 16, 14]
plt.figure(figsize=(10, 5))
plt.plot(heures,temperatures, marker='o', linestyle='-', color='blue', label='Température (°C)')
plt.title("Évolution de la température")
plt.xlabel("Axe X")
plt.ylabel("Axe Y")
plt.xticks(heures)
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()