import numpy
import random

listeTab=['10','16','15','18','2']

random.shuffle(listeTab)
print(f"le Tableau generie aleatoirement :{listeTab}")

mon_tuple=(1,2,3)
print(f"mon tuple est:{mon_tuple}")
liste_temp=list(mon_tuple)
print(f"mon tuple convirt liste est {liste_temp}")
random.shuffle(liste_temp)
mon_tuple_melange=tuple(liste_temp)

print(f"{mon_tuple_melange}")

jeurs=('lundi','Mardi','mercredi')

mon_jeurs_list=list(jeurs)
random.shuffle(mon_jeurs_list)
mon_jeurs_tuple=tuple(mon_jeurs_list)

print(f"Mon tuple est:{mon_jeurs_tuple}")





