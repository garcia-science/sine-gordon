import input.variables as var
import numpy as np


def force_x(a, b, c) -> np.ndarray:  # float:
    """
    Define force for the solitons
    :param a: var.dx
    :param b: var.D
    :param c: var.B
    :return:
    """
    # x_force_axis = np.linspace(-a*(b-1)/2, a*(b-1)/2, num=b-1)
    f = np.zeros((var.D, var.D), float)
    for m in range(0, b - 1):
        for n in range(0, b - 1):
            f[m][n] = 2 * (c * c - 1) * np.tanh(c * a * (m - ((b - 1) / 2))) / np.cosh(c * a * (m - ((b - 1) / 2)))
    return f
