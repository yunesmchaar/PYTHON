import numpy as np
import matplotlib.pyplot as plt  # You need to import matplotlib

def f(x,y):
    return x**2+y**2
x=np.linspace(-1000,1000,100)
y=np.linspace(-10,0,50)
x,y=np.meshgrid(x,y)

z=f(x,y)

fig=plt.figure()
ax=fig.add_subplot(111,projection='3d')
ax.plot_surface(x,y,z,cmap='plasma')
plt.show()