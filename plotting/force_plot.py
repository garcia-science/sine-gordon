import matplotlib.pyplot as plt
import matplotlib

matplotlib.rcParams['text.usetex'] = True  # To use latex (Needs to have miktex or another tex processor)

# matplotlib.rcParams.update({'font.size': 15})  # Size of font of plot


def force_plot(x_force_axis, force_1d, path_plot):
    fig1 = plt.figure()
    plt.plot(x_force_axis, force_1d, linewidth=2, label=r'$f(x)=2(B^{2}-1)\mathrm{tanh}(Bx)\mathrm{sech}(Bx)e^{-\frac{y^2}{\sigma^2}}$, $B=0.8$, $\sigma=15$')
    plt.xlabel(r'$x$', fontsize=18)
    plt.ylabel(r'$f(x)$', fontsize=18)
    plt.xticks(fontsize=16)
    plt.yticks(fontsize=16)
    plt.legend(shadow=True, loc='lower left')
    fig1.savefig(path_plot + "force.png", dpi=96)
    return
