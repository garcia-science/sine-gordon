import numpy as np
import matplotlib.pyplot as plt
import matplotlib

matplotlib.rcParams['text.usetex'] = True  # To use latex (Needs to have miktex or another tex processor)


matplotlib.rcParams.update({'font.size': 12})  # Size of font of plot


def plot_soliton2d(phi_t_list, x_axes, path_plot, t_n):
    """
    :param t_n: time step (varpi.time step)
    :param path_plot: directory to save the images
    :param phi_t_list: all t_i.txt in a list
    :type x_axes: x axis to plot soliton
    """
    data1 = np.array(phi_t_list)  # convert a list to an array
    fig1 = plt.figure()
    # plt.axes(xlim=(0, 100), ylim=(0, 8))
    image, = plt.plot(x_axes, data1[0], linewidth=2, label=r'$f(x)=2(B^{2}-1)$tanh$(Bx)$sech$(Bx)$, \\ $B=0.8$, $\gamma=0.1$')
    plt.xlabel(r'$x$', fontsize=17)
    plt.ylabel(r'$\dot{\phi}(x,100)$', fontsize=17)
    plt.xticks(fontsize=16)
    plt.yticks(fontsize=16)
    plt.legend(shadow=True, loc='upper left')
    fig1.savefig(path_plot + "\\phi_set\\psi_step_0.png", dpi=96)
    # Save as video

    for k in range(1, t_n - 1):
        image.set_data(x_axes, data1[k])
        plt.text(70, 0.5, r'$t = %s$' % (k/100),
                 {'color': 'black', 'fontsize': 14, 'ha': 'center', 'va': 'center',
                  'bbox': dict(boxstyle="round", fc="white", ec="black", pad=0.2)})
        plt.draw()
        fig1.savefig(path_plot + "\\phi_set\\phi_step_{0}.png".format(k), dpi=96)
    return
