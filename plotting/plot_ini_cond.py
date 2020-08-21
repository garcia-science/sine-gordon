import input.variables as var
import numpy as np
from input.initial_cond import initial
from itertools import product
import matplotlib.pyplot as plt
import matplotlib

matplotlib.rcParams['text.usetex'] = True

u = np.zeros((var.D, var.D, 3), float)
initial(u)
x_axes = np.linspace(0, var.dx * var.D, num=201, axis=-1)
X = x_axes
Y = X
X, Y = np.meshgrid(X, Y)

# Plot t=0
""""
fig1 = plt.figure(1)
plt.plot(x_axes, u[1])
plt.xlabel(r'$x$', fontsize=17)
plt.ylabel(r'$\phi(x,t=0)$', fontsize=17)
"""
# Colormap2D plot
# c sequence

psi_0 = np.zeros((var.D, var.D), float)
for j, i in product(range(0, var.D, 1), range(0, var.D, 1)):
    # Export data for print to file
    psi_0[i][j] = u[i][j][0]

col_sequence = psi_0
c = col_sequence


fig2 = plt.figure(2)
plt.scatter(X, Y, s=400, c=c, marker='s', cmap='gist_rainbow', linewidths=1.5)
plt.xlabel(r'$x$', fontsize=17)
plt.ylabel(r'$y$', fontsize=17)
c_bar = plt.colorbar()
c_bar.set_label(r'$\psi(x,y,t=0)$', fontsize=17)
