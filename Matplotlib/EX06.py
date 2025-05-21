import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import random



ages=[22, 25, 30, 35, 40, 22, 27, 29, 30, 31, 35, 38, 40, 45, 50, 22]
#plt.hist(ages,width=0.3)
plt.hist(ages, bins=6, color='green', edgecolor='black')
plt.title("Diagramme Histogramme")
plt.xlabel("Axe x")
plt.ylabel("Axe y")
plt.grid()
plt.tight_layout()
plt.show()