import pandas as pd

# Tes datasets
mydataset = {
  'cars': ["BMW", "Volvo", "Ford"],
  'passings': [3, 7, 2]
}

mydata = {
    'noms': ["YOUNESS", "Youness", "salahden"],
    'note': ["18.50", "14.50", "16.25"]
}

myClass = {
    'Module': ["Math", "Programmation c", "programmation python", "Administration unix", "Administration windows"],
    'nombreProf': ["3", "2", "8", "10", "11"]
}

# Création des DataFrames
myvar = pd.DataFrame(mydataset)
mynote = pd.DataFrame(mydata)
myEtudiant = pd.DataFrame(myClass)

# Sauvegarde en fichiers CSV
myvar.to_csv('cars.csv', index=False)
mynote.to_csv('notes.csv', index=False)
myEtudiant.to_csv('modules.csv', index=False)

print("Fichiers CSV créés avec succès.")
