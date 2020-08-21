import input.variables as var
import numpy as np


def force(a, b, c) -> tuple:  # float:
    """
    Define force for the solitons
    :param a: var.dx
    :param b: var.D
    :param c: var.B
    :return:
    """
    fx_list = []
    x_force_axis = np.linspace(-a*(b-1)/2, a*(b-1)/2, num=b-1)
    for m in range(0, b - 1):
        f = 2 * (c * c - 1) * np.tanh(c * a * (m - ((b - 1) / 2)))/np.cosh(c * a * (m - ((b - 1) / 2)))
        fx_list.append(f)
    force_1d = np.array(fx_list)
    return x_force_axis, force_1d
