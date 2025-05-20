import numpy as np
import pandas as pd

# DataFrame 1
voiture = pd.DataFrame({
    'marque': np.array(['Serie 1', 'Focus', '308', 'Class A', 'Golf']),
    'couleur': np.array(['rouge', 'bleu', 'noir', 'gris', 'blanc'])
})

# DataFrame 2
voiture2 = pd.DataFrame({
    'annee': np.array([2020, 2019, 2019, 2021, 2018]),
    'marque': np.array(['Serie 1', 'Focus', '308', 'Class A', 'Golf'])
})

# Merge on 'marque'
voiture_f = pd.merge(voiture, voiture2, on='marque')
print(voiture_f)
