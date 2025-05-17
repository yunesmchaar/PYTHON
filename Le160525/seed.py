import random

random.seed(42)
print(random.randint(1, 100))  # ex : 82

# Sauvegarde de l'état
etat = random.getstate()

print(random.randint(1, 100))  # ex : 15
print(random.randint(1, 100))  # ex : 4

# Restauration de l'état
random.setstate(etat)
print(random.randint(1, 100))  # ex : 15 (identique au premier appel après sauvegarde)
