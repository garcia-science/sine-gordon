from matplotlib import pyplot as plt
import matplotlib.animation as animation
import matplotlib
import input.variables as var

matplotlib.rcParams['text.usetex'] = True  # To use latex (Needs to have miktex or another tex processor)
matplotlib.rcParams.update({'font.size': 15})  # Size of font of plot


def video_soliton(phi_t_list, x_axes, path_plot, t_n):
    fig1 = plt.figure()
    ax = plt.axes(xlim=(-(var.D * var.dx-1), (var.D * var.dx-1)), ylim=(0, 8))
    ax.set_ylabel(r'$\dot{\phi}(x,100)$', fontsize=17)
    ax.set_xlabel(r'x', fontsize=17)
    line, = ax.plot([], [], lw=3, label=r'$f(x)=2(B^{2}-1)$tanh$(Bx)$sech$(Bx)e^{y^2/\sigma^2}$, \\ $B=1.1$, $\gamma=0.01$, $\sigma=15$')
    ax.legend(shadow=True, loc='upper left')

    def init():
        line.set_data([], [])
        return line,

    def animate(i):
        xx = x_axes
        yy = phi_t_list[i]
        line.set_data(xx, yy)
        plt.text(65, 0.5, r'$t = %s$' % (i/100),
                 {'color': 'black', 'fontsize': 14, 'ha': 'center', 'va': 'center',
                  'bbox': dict(boxstyle="round", fc="white", ec="black", pad=0.2)})
        return line,

    anim = animation.FuncAnimation(fig1, animate, init_func=init,
                                   frames=t_n, interval=20, blit=True)
    anim.save(path_plot + 'soliton_step_B_' + str(var.B) + '_x_00_' + str(var.x_00) + '_fx_non_cte.gif', writer='imagemagick', fps=2)
    plt.show()
