import numpy as np


def axes_construction_two_d(t_n, x, a) -> tuple:
    """
    :param a: var.D
    :param x: var.dx*var.D
    :type t_n: impress file step varpi.time_step
    """
    x_axes_center = np.linspace(0, t_n - 1)
    x_axes = np.linspace(0, x, num=a, axis=-1)
    X = x_axes
    Y = X
    X, Y = np.meshgrid(X, Y)
    return x_axes_center, x_axes, X, Y


