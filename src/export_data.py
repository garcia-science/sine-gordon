import input.variables as var
import sys
import numpy as np
import os


def verify_step_print() -> None:
    """
    verify the number of iteration is divisor of number of printing
    :return:
    """
    if (var.number_iterations + 1) % var.number_steps_print_file != 0:
        print("Number iteration is not divisor between number of print")
        print("Exit of the run")
        sys.exit()
    else:
        pass


def create_directory(dirName: str) -> None:
    # Create target Directory
    try:
        os.mkdir(dirName)
        print("Directory ", dirName, " Created ")
    except FileExistsError:
        print("Directory ", dirName, " already exists")


def print_file(path: str, psi_time_list: list) -> None:
    """
    Print file
    :param path:
    :param psi_time_list:
    :return:
    """
    dirName = "dx_" + str(var.dx) + "_dt_" + str(var.dt) + "_D_" + str(var.D) + "_B_" + str(var.B)
    create_directory(path + dirName)
    j = 1
    for item in psi_time_list:
        if (j == 1) | (j % var.number_steps_print_file == 0):
            np.savetxt(path + dirName + "/" + "t_" + str(j) + ".txt", item, fmt='%4.6f', delimiter='\t')
        j = j + 1

    return None
