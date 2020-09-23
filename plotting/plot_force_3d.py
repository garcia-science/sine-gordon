"""
======================
3D surface Force
======================

Demonstrates plotting a 3D surface colored with the coolwarm color map.
The surface is made opaque by using antialiased=False.

Also demonstrates using the LinearLocator and custom formatting for the
z axis tick labels.
"""
# from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from matplotlib.ticker import LinearLocator, FormatStrFormatter
import numpy as np
import input.variables as var
import matplotlib as mpl
import matplotlib

matplotlib.rcParams['text.usetex'] = True  # To use latex (Needs to have miktex or another tex processor)

fig = plt.figure()
ax = fig.gca(projection='3d')
a = 0.1
b = 201
c = 0.8
sigma = 10
# Make data.
X = np.linspace(-a * (b - 1) / 2, a * (b - 1) / 2, num=b)
Y = np.linspace(-a * (b - 1) / 2, a * (b - 1) / 2, num=b)
X, Y = np.meshgrid(X, Y)
f = np.zeros((b, b), float)

for m in range(1, b - 1):
    for n in range(1, b - 1):
        f[m][n] = 2 * (c * c - 1) * np.tanh(c * a * (m - ((b - 1) / 2))) * np.exp(-(n - (b - 1) / 2)**2 / sigma**2) / np.cosh(
            c * a * (m - ((b - 1) / 2)))
np.savetxt(var.output + "/" + 'force.txt', f, fmt='%1.4e')

# Plot the surface.
surf = ax.plot_surface(X, Y, f)
ax.set_xlabel(r'$x$', fontsize=17)
ax.set_ylabel(r'$y$', fontsize=17)
ax.set_zlabel(r'$f(x,y)$', fontsize=17)
fake2Dline = mpl.lines.Line2D([0], [0], linestyle="none", c='b', marker='o')
ax.legend([fake2Dline], [r'$f(x)=2(B^{2}-1)\mathrm{tanh}(Bx)\mathrm{sech}(Bx)e^{-\frac{y^2}{\sigma^2}}$'], numpoints=1)

# Customize the z axis.
# ax.set_zlim(-1.01, 1.01)
ax.zaxis.set_major_locator(LinearLocator(10))
ax.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))

# Add a color bar which maps values to colors.

plt.show()
