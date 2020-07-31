import numpy as np


def load_data(t_n, path_center, path_dirname) -> tuple:
    """
    :param path_dirname: directory of t_i.txt
    :param path_center: directory of center.txt
    :type t_n: varpi.time_step. Impress file step
    """
    phi_t_list = []
    center = np.loadtxt(path_center)
    # first_row_phi = [] if you need one row of the matrix, use this
    for p in range(0, t_n):
        inner_phi = np.loadtxt(path_dirname + "\\t_" + str(p) + ".txt")
        phi_t_list.append(inner_phi)
        # first_row_phi.append((inner_phi[1]))
    return center, phi_t_list


# print(load_data(varpi.time_step, var.output + var.dir_name + '\\center.txt', var.output + var.dir_name))
