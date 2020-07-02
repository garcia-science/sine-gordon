import numpy as np
import input.variables as var


def initial(u: np.ndarray) -> np.ndarray:
    """
    Define initial conditions
    :type u: float
    :param u: field
    :return:
    """
    yy = -7.
    for i in range(0, var.D):
        xx = -7.
        for j in range(0, var.D):
            # tmp = 3. - np.sqrt(xx * xx + yy * yy)
            tmp = np.exp(xx)
            u[i][j][0] = 4. * (np.arctan(tmp))
            # u[i][j][0] = 4. * (np.atan(tmp))
            xx = xx + var.dx
        yy = yy + var.dy
    return u
