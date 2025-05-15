import numpy as np
import matplotlib.pyplot as plt  # You need to import matplotlib

def f(x):
    return (x + 5) ** 2

x = np.linspace(-10, 0, 50)
y = f(x)

plt.plot(x, y)
plt.xlabel('x')  # Adding labels is good practice
plt.ylabel('f(x)')
plt.title('Plot of f(x) = (x + 5)²')
plt.grid(True)   # Adding grid makes it easier to read
plt.show()       # This displays the plot