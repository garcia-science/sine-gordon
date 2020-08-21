import matplotlib.pyplot as plt
import matplotlib

matplotlib.rcParams['text.usetex'] = True  # To use latex (Needs to have miktex or another tex processor)


def plot_center(x_axes_center, center, path_plot):
    """
    :param path_plot: directory to save the images
    :param center:
    :type x_axes_center: x axis to plot center
    """
    fig1 = plt.figure(1)
    plt.plot(x_axes_center, center, linewidth=2, label=r'$B=0.8$ $\gamma=0.1$')
    # plt.plot(x_axes_center, center_neg, linewidth=2, label=r'$f=-0.1$, $\gamma=0.1$')
    plt.xlabel(r'$Time$', fontsize=17)
    plt.ylabel(r'$\dot{\psi}(\delta)$', fontsize=17)
    plt.text(0.13, 45.00000000007, r'$f(x)=2(B^{2}-1)$tanh$(Bx)$sech$(Bx)$',
             {'color': 'black', 'fontsize': 12, 'ha': 'center', 'va': 'center',
              'bbox': dict(boxstyle="round", fc="white", ec="black", pad=0.2)})
    plt.xticks(fontsize=16)
    plt.yticks(fontsize=16)
    plt.legend(shadow=True)
    fig1.savefig(path_plot + 'cntr_mov_f_non_cte_B_0.8xy0_45.png')
    plt.show()
