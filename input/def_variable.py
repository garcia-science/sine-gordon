import input.variables as var

import numpy as np


def define_variables() -> tuple:
    """
    Define variables to use
     dt = dx / np.sqrt(2.)
    """
    u = np.zeros((var.D, var.D, 3), float)
    f = np.zeros((var.D, var.D), float)
    psi = np.zeros((var.D, var.D), float)
    psi_time_list = []

    return u, f, psi, psi_time_list
