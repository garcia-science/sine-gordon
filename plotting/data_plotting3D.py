# This import registers the 3D projection, but is otherwise unused.

from mpl_toolkits.mplot3d import Axes3D  # noqa: F401 unused import
from matplotlib.ticker import LinearLocator  # FormatStrFormatter
import matplotlib.pyplot as plt
import numpy as np
import input.variables as var
import matplotlib
matplotlib.rcParams['text.usetex'] = True


fig = plt.figure()
ax = fig.gca(projection='3d')

# Load the data
data3 = np.genfromtxt('t_2.txt', dtype=None)
phi_xy2 = data3[:, :]
X = np.arange(0, var.D * var.dx, var.dx)
Y = np.arange(0, var.D * var.dx, var.dx)
X, Y = np.meshgrid(X, Y)

# Plot the surface.
surf = ax.plot_surface(X, Y, data3[:, :], cmap='jet', linewidth=0.01, antialiased=True)

# Customize the axes.
ax.zaxis.set_major_locator(LinearLocator(6))
# ax.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))
ax.xaxis.set_major_locator(LinearLocator(6))
ax.yaxis.set_major_locator(LinearLocator(6))
ax.set_xlabel(r'$x$', fontsize=17)
ax.set_ylabel(r'$y$', fontsize=17)
ax.set_zlabel(r'$\phi(x,y)$', fontsize=17)
ax.zaxis.labelpad = 10
# Add a color bar which maps values to colors.
fig.colorbar(surf, shrink=0.5, aspect=5)

# We are going to do 10 plots, for 10 different angles
for angle in range(102, 118, 8):
    # Set the angle of the camera
    ax.view_init(30, angle)
    # Save it
    filename = 'phi_step' + str(angle) + '.png'
    plt.savefig(filename, dpi=96)
    plt.gca()

# plt.show()
