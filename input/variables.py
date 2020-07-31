import os
import platform
from pathlib import Path

pth = os.path.abspath(os.getcwd())
PATH = str(Path(pth).parents[0])

D = 201
dx = 0.5
dy = dx
dt = 0.01
Gamma = 0.1
B = 0.3
sigma = 15
Disp = 1 / (2 + (Gamma * dt))
Dism = (2 - (Gamma * dt))
dts = (dt / dx) * (dt / dx)
number_iterations = 999
number_steps_print_file = 20
f = 0.1

# VARIABLES FOR OUTPUTS
if platform.system() == "Darwin":
    output = PATH + "/output/"
else:
    output = PATH + "\\output\\"

dir_name = "test_dx_" + str(dx) + "_dt_" + str(round(dt, 2)) + "_D_" + str(D) + "_F_" + str(
    float(round(f, 2)))
