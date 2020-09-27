import input.variables as var
import sys
import numpy as np
import os
import csv


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


def calculate_position_center(list_values: list, path: str) -> None:
    """
    Calculate the position of the center using derivatives calculation
    :param list_values: list of values for the position 100
    :param path: path of the output file
    :param f: external force
    :return:
    """
    x0 = None
    for index in range(len(list_values) - 1):
        f1 = list_values[index] - np.pi
        f2 = list_values[index + 1] - np.pi
        if (f1 * f2) < 0:
            x0 = ((f2 * index * var.dx) - (f1 * (index + 1) * var.dx)) / (f2 - f1)
            # print(x0)
    f = open(path + "/" + "center.txt", 'a')
    f.write(str(x0) + '\n')
    f.close()


def print_file(dir_name: str, psi_time_list: list) -> None:
    """
    Print output to directory and print the position of the center
    :param dir_name:
    :param path: path of the output
    :param psi_time_list: list of the values of psi
    :param f: external force
    :return:
    """

    create_directory(dir_name)
    j = 0
    for item in psi_time_list:
        f = open(dir_name + "/" + "t_" + str(j) + ".txt", 'w')
       # calculate_position_center(item, dir_name)
       # for ele in item:
        csvwriter = csv.writer(f)
        csvwriter.writerows(item)
        f.close()
        j += 1
    return None
