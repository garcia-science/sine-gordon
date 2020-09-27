import input.variables as var
import numpy as np

from input.initial_cond import initial
from itertools import product
import matplotlib.pyplot as plt
import matplotlib

matplotlib.rcParams['text.usetex'] = True

# u_0 = np.loadtxt(var.output + var.dir_name + "\\t_0.txt")
u = np.zeros((var.D, var.D, 1), float)
initial(u)
np.savetxt(var.output + "/" + 'u_0.txt', u[0], fmt='%1.4e')

x_axes = np.linspace(-var.x_0, var.x_0, num=201)
X = x_axes
Y = X
X, Y = np.meshgrid(X, Y)

# Plot t=0
fig1 = plt.figure(1)
plt.plot(x_axes, u[0])
plt.xlabel(r'$x$', fontsize=17)
plt.ylabel(r'$\phi(x,t=0)$', fontsize=17)

# Colormap2D plot
# c sequence
"""

col_sequence = psi_0
c = col_sequence


fig2 = plt.figure(2)
plt.scatter(X, Y, s=400, c=c, marker='s', cmap='gist_rainbow', linewidths=1.5)
plt.xlabel(r'$x$', fontsize=17)
plt.ylabel(r'$y$', fontsize=17)
c_bar = plt.colorbar()
c_bar.set_label(r'$\psi(x,y,t=0)$', fontsize=17)
"""
