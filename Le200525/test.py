import matplotlib.pyplot as plt
xpoint=[1,4,6,8,10]
ypoint=[1,6,7,8,10]

plt.plot(xpoint,ypoint,'o-r',mec='r',mfc='k')

plt.title("Mon test pyplot")
plt.xlabel("Axe x")
plt.ylabel("Axe y")
plt.show()