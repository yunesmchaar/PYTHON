import matplotlib.pyplot as plt

x=[0,1,2,3,4]
y = [0,1,4,9,16]

#creation du graphique
plt.plot(x,y)

#Ajout de titres et labels

plt.title("Graphique de y=x^2")
plt.xlabel("x")
plt.ylabel("y")

#affichage
plt.show()