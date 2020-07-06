import numpy as np
import master.input.variables as var


def initial(u: np.ndarray) -> np.ndarray:
    """
    Define initial conditions
    :type u: float
    :param u: field
    :return:
    """
    yy = -50.
    for i in range(0, var.D):
        xx = -50.
        for j in range(0, var.D):
            tmp = np.exp(xx)
            u[i][j][0] = 4. * (np.arctan(tmp))
            xx = xx + var.dx
        yy = yy + var.dy
    return u
