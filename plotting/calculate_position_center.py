import input.variables as var
import numpy as np


def calculate_position_center(phi_100_vectors, path_dirname) -> None:
    """
    Calculate the position of the center using derivatives calculation
    :param phi_100_vectors: one hundred row of psi_t_list
    :param path_dirname: var.dir_name
    :return:
    """
    x0 = None
    list_values = phi_100_vectors
    print(len(list_values))
    for index in range(len(list_values) - 1):
        f1 = list_values[index] - np.pi
        f2 = list_values[index + 1] - np.pi
        print(len(f1))
        if (f1 * f2) < 0:
            x0 = ((f2 * index * var.dx) - (f1 * (index + 1) * var.dx)) / (f2 - f1)
            print(x0)
        f = open(path_dirname + "/" + "center.txt", 'w')
        f.write(str(x0) + '\n')
        f.close()
