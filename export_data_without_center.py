import input.variables as var
import sys
import os
import numpy as np


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


def create_directory(dir_name: str) -> None:
    """
    Create directory for output
    :param dir_name: Directory of output
    :return:
    """
    try:
        os.mkdir(dir_name)
        print("Directory ", dir_name, " Created ")
    except FileExistsError:
        print("Directory ", dir_name, " already exists")


def print_file(dir_name: str, psi_time_list: list) -> None:
    """
    Print output to directory and print the position of the center
    :param dir_name:
    :param psi_time_list: list of the values of psi
    :return:
    """

    create_directory(dir_name)
    j = 0
    for item in psi_time_list:
        np.savetxt(dir_name + "/" + "t_" + str(j) + ".txt", item, fmt='%4.6f', delimiter='\t')
        j = j + 1
    return None
