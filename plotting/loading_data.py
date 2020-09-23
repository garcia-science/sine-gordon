import numpy as np
import input.variables as var


def load_data(t_n, path_dirname) -> tuple:
    """
    :param path_dirname: directory of t_i.txt. Remember that it is necessary to change B and x_00 to obtain the current
    directory
    :type t_n: varpi.time_step. Impress file step
    """
    # t_n = 50
    phi_t_list = []
    center = np.loadtxt(path_dirname + "\\center.txt")
    # one_h_row_phi = []  # if you need one row of the matrix, use this
    for p in range(0, t_n):
        inner_phi = np.loadtxt(path_dirname + "\\t_" + str(p) + ".txt")
        # one_h_row_phi.append(inner_phi[100])
        phi_t_list.append(inner_phi)
        # phi_100_vectors = np.array(one_h_row_phi)
    return center, phi_t_list  # phi_100_vectors

# print(load_data(varpi.time_step, var.output + var.dir_name + '\\center.txt', var.output + var.dir_name))
