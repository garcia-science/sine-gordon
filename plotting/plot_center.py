import matplotlib.pyplot as plt
import matplotlib
import numpy as np
import input.variables as var

matplotlib.rcParams['text.usetex'] = True  # To use latex (Needs to have miktex or another tex processor)


def plot_center(x_axes_center, path_dirname, path_plot):
    """
    :param path_dirname: var.dir_name
    :param path_plot: directory to save the images
    :type x_axes_center: x axis to plot center
    """
    center = np.loadtxt(path_dirname + '\\center.txt')
    fig1 = plt.figure(1)
    plt.plot(x_axes_center, center, linewidth=2, label=r'$B=1.1$ $\gamma=0.01$')
    # plt.plot(x_axes_center, center_neg, linewidth=2, label=r'$f=-0.1$, $\gamma=0.1$', \sigma=15)
    plt.xlabel(r'$Time$', fontsize=17)
    plt.ylabel(r'$\dot{\psi}(\delta)$', fontsize=17)
    plt.text(0.15, 44.9840, r'$f(x)=2(B^{2}-1)$tanh$(Bx)$sech$(Bx)e^{y^2/\sigma^2}$',
             {'color': 'black', 'fontsize': 12, 'ha': 'center', 'va': 'center',
              'bbox': dict(boxstyle="round", fc="white", ec="black", pad=0.2)})
    plt.xticks(fontsize=16)
    plt.yticks(fontsize=16)
    plt.legend(shadow=True)
    fig1.savefig(path_plot + 'cnt_mov_f_non_cte_B_' + str(var.B) + '_x00_' + str(var.x_00) + '.png')
    plt.show()
