import input.variables as var


def second_it(u):
    for mm in range(1, var.D - 1):  # Borders in second iteration
        u[mm][0][1] = u[mm][1][1]
        u[mm][var.D - 1][1] = u[mm][var.D - 2][1]
        u[0][mm][1] = u[1][mm][1]
        u[var.D - 1][mm][1] = u[var.D - 2][mm][1]

    u[0][0][1] = u[1][0][1]  # Still undefined terms
    u[var.D - 1][0][1] = u[var.D - 2][0][1]
    u[0][var.D - 1][1] = u[1][var.D - 1][1]
    u[var.D - 1][var.D - 1][1] = u[var.D - 2][var.D - 1][1]
    tmp = 0.
    return u
