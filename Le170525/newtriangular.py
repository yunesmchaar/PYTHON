import random

min_heurs=2
max_heurs=10
temps_probable=5

temps_reel=random.triangular(min_heurs,max_heurs,temps_probable)

print(f"le temps estime pour la tache est {temps_reel:.2f} heurs")
