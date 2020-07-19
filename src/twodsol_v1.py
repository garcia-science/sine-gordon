import numpy as np
import input.variables as var


def solution(nint: int, u: np.array, f: np.array, psi: np.array, psi_time_list: list) -> list:
    """
    Integrate solution
    :param f: force
    :param nint: number of iterations
    :param u: field that functional dependence is (x,y,t)
    :param psi:  field at new iterations
    :param psi_time_list: list of psi for different time
    :return: psi_time_list: list of psi for different time
    """

    # for m in range(1, var.D - 1):
    # for l in range(1, var.D - 1):
    # a2 = u[m + 1][l][0] + u[m - 1][l][0] + u[m][l + 1][0] + u[m][l - 1][0]
    # tmp = .25 * a2
    # u1 = .5 * ((var.dts * a2) - (var.dt * var.dt * np.sin(tmp)))
    # u2 = (1 - (2 * var.dts)) * u[m][l][0]
    # uf = f * var.dt * var.dt
    # u[m][l][1] = u1 + u2 + uf

    for mm in range(1, var.D - 1):  # Borders in second iteration
        u[mm][0][1] = u[mm][1][1]
        u[mm][var.D - 1][1] = u[mm][var.D - 2][1]
        u[0][mm][1] = u[1][mm][1]
        u[var.D - 1][mm][1] = u[var.D - 2][mm][1]
    u[0][0][1] = u[1][0][1]  # Still undefined terms
    u[var.D - 1][0][1] = u[var.D - 2][0][1]
    u[0][var.D - 1][1] = u[1][var.D - 1][1]
    u[var.D - 1][var.D - 1][1] = u[var.D - 2][var.D - 1][1]

    for k in range(0, nint + 1):  # Following iterations
        if (k % 20) == 0: print(k, "out of ", nint)
        for m in range(1, var.D - 1):
            for l in range(1, var.D - 1):
                a1 = u[m + 1][l][1] + u[m - 1][l][1] + u[m][l + 1][1] + u[m][l - 1][1]
                tmp = .25 * a1
                u3 = -1 * u[m][l][0] * var.Disp * var.Dism
                u4 = 2 * var.Disp * (var.dts * a1) - 2 * (var.dt * var.dt * np.sin(tmp)) * var.Disp
                u5 = 4 * (1 - (2 * var.dts)) * u[m][l][1] * var.Disp
                uf = 2 * f * var.dt * var.dt * var.Disp
                u[m][l][2] = u3 + u4 + u5 + uf
                u[m][0][2] = u[m][1][2]
                u[m][var.D - 1][2] = u[m][var.D - 2][2]

        for mm in range(1, var.D - 1):
            u[mm][0][2] = u[mm][1][2]
            u[mm][var.D - 1][2] = u[mm][var.D - 2][2]
            u[0][mm][2] = u[1][mm][2]
            u[var.D - 1][mm][2] = u[var.D - 2][mm][2]
        u[0][0][2] = u[1][0][2]
        u[var.D - 1][0][2] = u[var.D - 2][0][2]
        u[0][var.D - 1][2] = u[1][var.D - 1][2]
        u[var.D - 1][var.D - 1][2] = u[var.D - 2][var.D - 1][2]

        for l in range(0, var.D):  # New iterations now old. Rule of definition of derivative
            for m in range(0, var.D):
                u[l][m][0] = u[l][m][1]
                u[l][m][1] = u[l][m][2]

        for i in range(0, var.D, 1):
            for j in range(0, var.D, 1):
                psi[i][j] = u[i][j][2]

# EXPORT ROW NUMBER 100 TO VERIFY DISPLACEMENTS WITH FORCE

        lista_profile = []
        if (k % 20) == 0:
            for j in range(var.D):
                # print(psi[100][j])
                lista_profile.append(psi[100][j])
            psi_time_list.append(lista_profile)

    return psi_time_list
