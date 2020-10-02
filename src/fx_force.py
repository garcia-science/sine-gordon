import input.variables as var
import numpy as np


def force(dx, D, B_square) -> float:
    """
    Define force for the solitons
    :param a: var.dx
    :param b: var.D
    :param c: var.B
    :return:
    """
    f = np.zeros((D, D), float)
    print(f.shape)
    # f = var.f
    for m in range(0, D):
        for n in range(0, D):
            first_term = 2 * (B_square - 1)
            inner_term = np.sqrt(B_square) * dx * (n - (D - 1) / 2)
            sec_term = np.tanh(inner_term)
            f[m][n] = first_term * sec_term
            #f[m][n] = var.f
    return f
