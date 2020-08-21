import numpy as np
import input.variables as var

def axes_construction_two_d(t, t_n, x, a) -> tuple:
    """
    :param t: var.dt
    :param a: var.D
    :param x: var.dx*var.D
    :type t_n: impress file step varpi.time_step
    """
    x_axes_center = np.linspace(0, t * (t_n-1))
    x_axes = np.linspace(0, x, num=a, axis=-1)
    x_force_axes = np.arange(-var.dx*(a-1)/2, var.dx*(a-1)/2)
    X = x_axes
    Y = X
    X, Y = np.meshgrid(X, Y)
    i = x_force_axes
    j = i
    i, j = np.meshgrid(i, j)
    return x_axes_center, x_axes, X, Y, i, j


