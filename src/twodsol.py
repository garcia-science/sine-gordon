from mpl_toolkits.mplot3d import Axes3D
from itertools import product

import input.variables as var
import numpy as np
import matplotlib.pylab as plt
import os
import time

start = time.process_time()
print("start")


def define_variables():
    """
    Define variables to use
    :return:
    """
    # dt = dx / np.sqrt(2.)

    u = np.zeros((var.D, var.D, 3), float)
    psi = np.zeros((var.D, var.D), float)
    psi_time_list = []

    return u, psi, psi_time_list


def initial(u):
    """
    Define initial conditions
    :param u:
    :return:
    """
    yy = -7.
    for i in range(0, var.D):
        xx = -7.
        for j in range(0, var.D):
            # tmp = 3. - np.sqrt(xx * xx + yy * yy)
            tmp = np.exp(xx);
            u[i][j][0] = 4. * (np.arctan(tmp))
            # u[i][j][0] = 4. * (math.atan(tmp))
            xx = xx + var.dx
        yy = yy + var.dy

    return u


def solution(nint, u, psi_time_list):
    for m, l in product(range(1, var.D - 1), range(1, var.D - 1)):
        a2 = u[m + 1][l][0] + u[m - 1][l][0] + u[m][l + 1][0] + u[m][l - 1][0]
        tmp = .25 * a2
        #    u[m][l][1] = 0.5 * (dts * a2 - dt * dt * np.sin(tmp))
        F = 2 * (var.B * var.B - 1) * np.tanh(var.B * var.dx * (m - ((var.D - 1) / 2))) * np.exp(
            -(var.dx * (l - ((var.D - 1) / 2))) * (var.dx *
                                                   (l -
                                                    ((var.D
                                                      - 1) / 2))) / var.sigma * var.sigma) / np.cosh(
            var.B * var.dx * (m - ((var.D - 1) / 2)))
        u[m][l][1] = .5 * (var.dts * a2 - var.dt * var.dt * np.sin(tmp)) + 0.5 * var.dt * var.dt * F + (
                1 - 2 * var.dts) * u[m][l][0];

    for mm in range(1, var.D - 1):  # Bordersinseconditeration
        u[mm][0][1] = u[mm][1][1]
        u[mm][var.D - 1][1] = u[mm][var.D - 2][1]
        u[0][mm][1] = u[1][mm][1]
        u[var.D - 1][mm][1] = u[var.D - 2][mm][1]

    u[0][0][1] = u[1][0][1]  # Stillundefinedterms
    u[var.D - 1][0][1] = u[var.D - 2][0][1]
    u[0][var.D - 1][1] = u[1][var.D - 1][1]
    u[var.D - 1][var.D - 1][1] = u[var.D - 2][var.D - 1][1]
    tmp = 0.

    for k in range(0, nint + 1):  # Followingiterations
        print(k, "outof", nint)
        for m, l in product(range(1, var.D - 1), range(1, var.D - 1)):
            a1 = u[m + 1][l][1] + u[m - 1][l][1] + u[m][l + 1][1] + u[m][l - 1][1]
            tmp = .25 * a1
            F = 2 * (var.B * var.B - 1) * np.tanh(var.B * var.dx * (m - ((var.D - 1) / 2))) * np.exp(
                (-var.dx * (l - ((var.D - 1) / 2))) * (
                        var.dx * (l - ((var.D - 1) / 2))) / var.sigma * var.sigma) / np.cosh(
                var.B * var.dx * (m - ((var.D - 1) / 2)));
            u[m][l][2] = -u[m][l][
                0] * var.Disp * var.Dism + 2 * var.Disp * var.dts * a1 - 2 * var.Disp * var.dt * var.dt * np.sin(
                tmp) + 2 * var.Disp * var.dt * var.dt * F + 4 * (1 - 2 * var.dts) * var.Disp * u[m][l][1];

            # u[m][l][2] = -u[m][l][0] + dts * a1 - dt * dt * np.sin(tmp)
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

        for l, m in product(range(0, var.D), range(0, var.D)):
            # Newiterationsnowold
            u[l][m][0] = u[l][m][1]
            u[l][m][1] = u[l][m][2]
        for j, i in product(range(0, var.D, 5), range(0, var.D, 5)):
            # psi[i][j] = np.sin(u[i][j][2] / 2)
            psi[i][j] = u[i][j][2]
        psi_time_list.append(psi)

    return psi_time_list

    # if k == 1:
    #     for j in range(0, D, 5):
    #         for i in range(0, D, 5):
    #             # psi[i][j] = np.sin(u[i][j][2] / 2)
    #             psi[i][j] = u[i][j][2]
    #             f.write(str(psi[i][j]) + '\t')
    #         f.write("\n")
    #
    # if k == nint:
    #     for j in range(0, D, 5):
    #         for i in range(0, D, 5):
    #             # psi[i][j] = np.sin(u[i][j][2] / 2)
    #             psi[i][j] = u[i][j][2]
    #             g.write(str(psi[i][j]) + '\t')
    #         g.write("\n")


PATH = os.path.abspath(os.getcwd())
f = open(PATH + "/initial.txt", "w")
g = open(PATH + "/end.txt", "w")
u, psi, psi_time_list = define_variables()
u = initial(u)
psi_time_list = solution(var.number_iterations, u, psi_time_list)

#

# xx = np.arange(0, var.D, 5)
# yy = np.arange(0, var.D, 5)
# fig = plt.figure()
# ax = Axes3D(fig)
# X, Y = plt.meshgrid(xx, yy)
# solution(1)
# Z = funcz(psi)
# x.plot_wireframe(X, Y, Z, color="r")
# Numberoftimeiterations
# print(len(psi_time_list))
# Z = psi_time_list[1]
# fig = plt.figure()
# ax = Axes3D(fig)
# ax.plot_wireframe(X, Y, Z, color="g")
# ax.set_xlabel("X")
# ax.set_ylabel("Y")
# ax.set_zlabel("Z")
# plt.show()
print("Done")
print(psi_time_list[21])
f.close()
g.close()

elapsed_time = time.process_time() - start
print(str(elapsed_time) + " seconds")
