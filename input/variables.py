import os
import platform
from pathlib import Path

pth = os.path.abspath(os.getcwd())
PATH = str(Path(pth).parents[0])

D = 201
dx = 0.5
dy = dx
dt = 0.01
x_0 = dx*100
y_0 = dy*100
x_00 = 2
y_00 = 4
Gamma = 0.02
B_square = 1.1
sigma = 15
Disp = 1 / (2 + (Gamma * dt))
Dism = (2 - (Gamma * dt))
dts = (dt / dx) * (dt / dx)
number_iterations = 999
number_steps_print_file = 50
#f = -0.09

# VARIABLES FOR OUTPUTS
if platform.system() == "Darwin":
    output = PATH + "/output/"
else:
    output = PATH + "\\output\\"

dir_name = "rev_dx_" + str(dx) + "_dt_" + str(round(dt, 2)) + "_D_" + str(D) + "_B_square_" + str(
    float(round(B_square, 2))) + "_x_0_" + str(float(round(x_00, 2))) + "_f_var"
