from src.export_data import print_file, verify_step_print
from input.initial_cond import initial
from input.def_variable import define_variables
# from src.f_force import force
from src.fx_force import force
from src.first_iteration import first_it
from src.borders_2nd_iteration import second_it
from src.twodsol_v1 import solution
import input.variables as var
import time


def main():
    verify_step_print()
    u, f, psi, psi_time_list = define_variables()
    u = initial(u)
    f = force(var.dx, var.D, var.B)
    # f = force(f)
    first_it(u, f)
    second_it(u)
    psi_time_list = solution(var.number_iterations, u, f, psi, psi_time_list)
    print_file(var.output + var.dir_name, psi_time_list)


if __name__ == "__main__":
    start = time.process_time()
    print("start")
    main()
    elapsed_time = time.process_time() - start
    print(str(elapsed_time) + " seconds")
    print("Done")
