from itertools import product

import numpy as np

import input.variables as var

"""
def define_variables() -> tuple:
    
    Define variables to use
    :return:
    
    # dt = dx / np.sqrt(2.)

    u = np.zeros((var.D, var.D, 3), float)
    psi = np.zeros((var.D, var.D), float)
    psi_time_list = []

    return u, psi, psi_time_list
    """

# def initial(u: np.ndarray) -> np.ndarray:

"""
    Define initial conditions
    :param u:
    :return:
    """


# yy = -7.
# for i in range(0, var.D):
#  xx = -7.
#  for j in range(0, var.D):
# tmp = 3. - np.sqrt(xx * xx + yy * yy)
#    tmp = np.exp(xx)
#   u[i][j][0] = 4. * (np.arctan(tmp))
# # u[i][j][0] = 4. * (math.atan(tmp))
#  xx = xx + var.dx
#   yy = yy + var.dy

#   return u


def solution(nint, u, f, psi, psi_time_list) -> list:
    """
    Integrate solution
    :param f: force
    :param nint:
    :param u: field that functional dependence is (x,y,t)
    :param psi:
    :param psi_time_list:
    :return:
    """

    # for m, l in product(range(1, var.D - 1), range(1, var.D - 1)):
    # u[m][l][1] = 0.5 * (dts * a2 - dt * dt * np.sin(tmp))
    # f = 0
    # a2 = u[m - 1][l][0] + u[m][l + 1][0] + u[m][l - 1][0]
    # tmp = .25 * a2
    # u[m][l][1] = .5 * (var.dts * a2 - var.dt * var.dt * np.sin(tmp)) + 0.5 * var.dt * var.dt * f + (
    # 1 - 2 * var.dts) * u[m][l][0]

    # for mm in range(1, var.D - 1):  # Borders in second iteration
    # u[mm][0][1] = u[mm][1][1]
    # u[mm][var.D - 1][1] = u[mm][var.D - 2][1]
    # u[0][mm][1] = u[1][mm][1]
    # u[var.D - 1][mm][1] = u[var.D - 2][mm][1]

    # u[0][0][1] = u[1][0][1]  # Still undefined terms
    # u[var.D - 1][0][1] = u[var.D - 2][0][1]
    # u[0][var.D - 1][1] = u[1][var.D - 1][1]
    # u[var.D - 1][var.D - 1][1] = u[var.D - 2][var.D - 1][1]
    # tmp = 0.

    for k in range(0, nint + 1):  # Following iterations
        print(k, "out of", nint)
        for m, l in product(range(1, var.D - 1), range(1, var.D - 1)):
            a1 = u[m + 1][l][1] + u[m - 1][l][1] + u[m][l + 1][1] + u[m][l - 1][1]
            tmp = .25 * a1
            u[m][l][2] = -u[m][l][
                0] * var.Disp * var.Dism + 2 * var.Disp * var.dts * a1 - 2 * var.Disp * var.dt * var.dt * np.sin(
                tmp) + 2 * var.Disp * var.dt * var.dt * f + 4 * (1 - 2 * var.dts) * var.Disp * u[m][l][1]

            # u[m][l][2] = -u[m][l][0] + dts * a1 - dt * dt * np.sin(tmp)
            u[m][0][2] = u[m][1][2]
            u[m][var.D - 1][2] = u[m][var.D - 2][2]

        for mm in range(1, var.D - 1):  # Condiciones de borde
            u[mm][0][2] = u[mm][1][2]
            u[mm][var.D - 1][2] = u[mm][var.D - 2][2]
            u[0][mm][2] = u[1][mm][2]
            u[var.D - 1][mm][2] = u[var.D - 2][mm][2]

        u[0][0][2] = u[1][0][2]
        u[var.D - 1][0][2] = u[var.D - 2][0][2]
        u[0][var.D - 1][2] = u[1][var.D - 1][2]
        u[var.D - 1][var.D - 1][2] = u[var.D - 2][var.D - 1][2]

        for l, m in product(range(0, var.D), range(0, var.D)):
            # New iterations nowold
            u[l][m][0] = u[l][m][1]
            u[l][m][1] = u[l][m][2]

        for j, i in product(range(0, var.D, 1), range(0, var.D, 1)):
            # Export data for print to file
            psi[i][j] = u[i][j][2]
        psi_time_list.append(psi)  # NO VA DENTRO DEL FOR j,i
        # print(len(psi_time_list))
    return psi_time_list
