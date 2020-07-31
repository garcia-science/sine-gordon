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
    plt.plot(x_axes_center, center, linewidth=2, label=r'$f=0.1$, $\gamma=0.1$')
    # plt.plot(x_axes_center, center_neg, linewidth=2, label=r'$f=-0.1$, $\gamma=0.1$')
    plt.xlabel(r'$Time$', fontsize=17)
    plt.ylabel(r'$\dot{\psi}(\delta)$', fontsize=17)
    plt.xticks(fontsize=16)
    plt.yticks(fontsize=16)
    plt.legend(shadow=True, fontsize='x-large')
    fig1.savefig(path_plot+'center_movement.png')
    plt.show()
