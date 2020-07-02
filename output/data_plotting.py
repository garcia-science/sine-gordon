# Import the necessary libraries
# import seaborn as sns
import input.variables as var
import numpy as np
# import pandas as pd
import matplotlib.pyplot as plt
import matplotlib

matplotlib.rcParams['text.usetex'] = True

# Load data
phi_t_list = []
inner_phi = np.zeros((var.D, var.D))
first_row_phi = []
for p in range(1, var.number_iterations + 1):
    inner_phi = np.loadtxt('t_' + str(p) + '.txt')
    phi_t_list.append(inner_phi)
    first_row_phi.append((inner_phi[1]))



# Constructing the axes
# x_axes = pd.DataFrame(x_axe)
x_axes = np.linspace(0, var.dx * var.D, num=201, axis=-1)
X = x_axes
Y = X
X, Y = np.meshgrid(X, Y)


"""
# figure
fig1 = plt.figure(1)

# Plot
# for k in range(1, var.number_iterations):
plt.plot(x_axes, data_2[1, :])
plt.xlabel(r'$x$', fontsize=17)
plt.ylabel(r'$\phi(x,1)$', fontsize=17)

# Colormap2D plot

# c sequence
col_intense = data2
c = col_intense
#Plot

fig2 = plt.figure(2)
plt.scatter(X, Y, s=400, c=c, marker='s', cmap='gist_rainbow', linewidths=1.5)
plt.xlabel(r'$x$', fontsize=17)
plt.ylabel(r'$y$', fontsize=17)
c_bar = plt.colorbar()
c_bar.set_label(r'$\phi(x,1)$', fontsize=17)
plt.show() """
