import input.variables as var
import numpy as np


def force_x(a, D, B_square) -> float:
    """
    Define force for the solitons
    :param a: var.dx
    :param b: var.D
    :param c: var.B
    :return:
    """
    # x_force_axis = np.linspace(-a*(b-1)/2, a*(b-1)/2, num=b-1)
    f = np.zeros((D, D), float)
    #f = var.f
    for m in range(0, D - 1):
        for n in range(0, D - 1):
            f[m][n] = 2 * (B_square - 1) * np.tanh(np.sqrt(B_square) * a * (n - ((D - 1) / 2))) / np.cosh(
                np.sqrt(B_square) * a * (n -
                                         ((D - 1) /
                                          2)))
    return f
