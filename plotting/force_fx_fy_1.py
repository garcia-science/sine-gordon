import input.variables as var
import numpy as np


def fy1_force():
    """
    Define force for the solitons
    :return:

    """
    fy1_list = []
    for m in range(1, var.D - 1):
        for n in range(1, var.D - 1):
            f = 2 * (var.B * var.B - 1) * np.tanh(var.B * var.dx * (m - ((var.D - 1) / 2))) / np.cosh(
                var.B * var.dx * (m - ((var.D - 1) / 2)))
            fy1_list.append(f)
    force_2d = np.array(fy1_list)
    return force_2d
