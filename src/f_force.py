from itertools import product

import numpy as np

import input.variables as var


def force(f):
    f = 0.
    """
    for m, n in product(range(1, var.D - 1), range(1, var.D - 1)):
        
        
            f = 2 * (var.B * var.B - 1) * np.tanh(var.B * var.dx * (m - ((var.D - 1) / 2))) * np.exp(
            -(var.dx * (n - ((var.D - 1) / 2))) * (var.dx *
                                                   (n -
                                                    ((var.D
                                                      - 1) / 2))) / var.sigma * var.sigma) / np.cosh(
            var.B * var.dx * (m - ((var.D - 1) / 2)))
            """
    return f
