from pathlib import Path
import input.variables as var
import os
import platform

pth = os.path.abspath(os.getcwd())
PATH = str(Path(pth).parents[0])

time_step = int((var.number_iterations + 1) / var.number_steps_print_file)

# VARIABLES FOR OUTPUTS
if platform.system() == "Darwin":
    output_plot = PATH + "/output_plotting/"
else:
    output_plot = PATH + "\\output_plotting\\"

