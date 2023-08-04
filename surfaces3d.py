import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d

# Elliptic Paraboloid
plt.figure()
ax = plt.axes(projection='3d')
x = np.linspace(-1, 1, 30)
y = np.linspace(-1, 1, 30)
X, Y = np.meshgrid(x, y)
Z = X**2 + Y**2
ax.contour3D(X, Y, Z, 50)
ax.set_title('Elliptic Paraboloid')

# Ellipsoid
plt.figure()
ax = plt.axes(projection='3d')
x = np.linspace(-1, 1, 30)
y = np.linspace(-1, 1, 30)
X, Y = np.meshgrid(x, y)
Z = np.sqrt(1 - (X**2) - (Y**2))
ax.plot_surface(X, Y, Z, cmap='viridis')
ax.set_title('Ellipsoid')

# Cone
plt.figure()
ax = plt.axes(projection='3d')
theta = np.linspace(0, 2*np.pi, 30)
z = np.linspace(-1, 1, 30)
Z, THETA = np.meshgrid(z, theta)
R = 1 - Z
X = R * np.cos(THETA)
Y = R * np.sin(THETA)
ax.plot_surface(X, Y, Z, cmap='viridis')
ax.set_title('Cone')

# Square Pyramid
plt.figure()
ax = plt.axes(projection='3d')
x = np.linspace(-1, 1, 30)
y = np.linspace(-1, 1, 30)
X, Y = np.meshgrid(x, y)
Z = np.zeros_like(X)
Z[(X >= 0) & (Y >= 0) & (X + Y <= 1)] = 1
ax.plot_surface(X, Y, Z, cmap='viridis')
ax.set_title('Square Pyramid')

# Parallelepiped
plt.figure()
ax = plt.axes(projection='3d')
x = np.linspace(-1, 1, 30)
y = np.linspace(-1, 1, 30)
X, Y = np.meshgrid(x, y)
Z = np.ones_like(X)
Z[(X >= -0.5) & (X <= 0.5) & (Y >= -0.5) & (Y <= 0.5)] = 0
ax.plot_surface(X, Y, Z, cmap='viridis')
ax.set_title('Parallelepiped')

plt.show()
