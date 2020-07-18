# Import the necessary libraries
import input.variables as var
import numpy as np
import matplotlib.pyplot as plt
import matplotlib

matplotlib.rcParams['text.usetex'] = True
matplotlib.rcParams.update({'font.size': 15})

# Load Data center
center = np.loadtxt('center.txt')
# center_neg = np.loadtxt('center_neg.txt')

# Load data soliton
phi_t_list = []  # This list will contain all data from t_1.txt
inner_phi = np.zeros((var.D, var.D))  # Initializing the matrix
# first_row_phi = [] # If we need one row only of every matrix, use this
for p in range(0, len(center - 1)):
    inner_phi = np.loadtxt('t_' + str(p) + '.txt')
    phi_t_list.append(inner_phi)
    # first_row_phi.append((inner_phi[1]))

# Load Data center
center = np.loadtxt('center.txt')
# center_neg = np.loadtxt('center_neg.txt')

# Constructing the axes soliton 2D
# x_axes = pd.DataFrame(x_axe)
x_axes = np.linspace(0, var.dx * var.D, num=201, axis=-1)
X = x_axes
Y = X
X, Y = np.meshgrid(X, Y)
"""
# Plot Center

# Create x_axis
x_axes_center = np.linspace(0, len(center)-1)

# Figure 1
fig1 = plt.figure(1)
plt.plot(x_axes_center, center, linewidth=2, label='$Force$ $f=0.1$')
plt.plot(x_axes_center, center_neg, linewidth=2, label='$Force$ $f=-0.1$')
plt.xlabel(r'$Time$', fontsize=17)
plt.ylabel(r'$\dot{\psi}(x)$', fontsize=17)
plt.xticks(fontsize=16)
plt.yticks(fontsize=16)
plt.legend(shadow=True, fontsize='x-large')
plt.show()
"""

# Figure 2: Plot soliton 2D
data1 = np.array(phi_t_list)
fig2 = plt.figure()
ax = fig2.subplots()  # fig2.gca()
image, = ax.plot(x_axes, data1[0], label="$f=-0.1$")
ax.set_xlabel(r'$x$', fontsize=17)
ax.set_ylabel(r'$\phi(x,100)$', fontsize=17)
ax.legend()
# ax.set_x(fontsize=16)
# ax.set_yticks(fontsize=16)
plt.draw()
fig2.savefig("psi_step_0.png", dpi=96)
# Save it
for k in range(1, len(center - 1)):
    image.set_data(x_axes, data1[k])
    plt.draw()
    # filename = 'psi_step' + str(k) + '.png'
    fig2.savefig("phi_step_{0}.png".format(k))

"""
# Colormap2D Plot

# c sequence
col_intense = data2
c = col_intense
# Plot colormap 2D

fig2 = plt.figure(2)
plt.scatter(X, Y, s=400, c=c, marker='s', cmap='gist_rainbow', linewidths=1.5)
plt.xlabel(r'$x$', fontsize=17)
plt.ylabel(r'$y$', fontsize=17)
c_bar = plt.colorbar()
c_bar.set_label(r'$\phi(x,1)$', fontsize=17)
plt.show() """
