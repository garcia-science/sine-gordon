from itertools import product

import numpy as np

import input.variables as var


def first_it(u, f):

    for m, l in product(range(1, var.D - 1), range(1, var.D - 1)):
        # u[m][l][1] = 0.5 * (dts * a2 - dt * dt * np.sin(tmp))
        a2 = u[m - 1][l][0] + u[m + 1][l][0] + u[m][l + 1][0] + u[m][l - 1][0]
        tmp = .25 * a2
        u[m][l][1] = (var.dts * a2 - var.dt * var.dt * np.sin(tmp)) + var.dt * var.dt * f + 2*(
                1 - 2 * var.dts) * u[m][l][0]
    return u
