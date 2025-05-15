import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Define the function
def f(X, Y):
    return X*2 * Y*2

# Create X and Y ranges
x = np.linspace(-1000, 1000, 100)
y = np.linspace(-10, 0, 50)
X, Y = np.meshgrid(x, y)

# Compute Z values
Z = f(X, Y)

# Create the 3D plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(X, Y, Z, cmap='plasma')

# Show the plot
plt.show()