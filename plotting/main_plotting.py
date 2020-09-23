from plotting.axes_soliton_2D import axes_construction_two_d
import input.variables as var
import plotting.plot_variables as varpi
# from plotting.calculate_position_center import calculate_position_center
from plotting.loading_data import load_data
from plotting.plot_center import plot_center
# from plotting.plot_soliton_2D import plot_soliton2d
from plotting.soliton_video import video_soliton
# from src.fx_force import force_x
# from src.f_force import force
# from plotting.force_plot import force_plot
# from plotting.plot_force_3d import plt_force_3d
# from plotting.force_fx_fy_1 import fy1_force
# from plotting.plot_colormap_2d import colormap_2d
import time


def main_plot():

    x_axes_center, x_axes, X, Y, i, j = axes_construction_two_d(var.dt, varpi.time_step, var.dx * var.D, var.D)
    center, phi_t_list = load_data(varpi.time_step, var.output + var.dir_name)
    # calculate_position_center(phi_100_vectors, var.output + var.dir_name)
    plot_center(x_axes_center, var.output + var.dir_name, varpi.output_plot)
    # plot_soliton2d(phi_t_list, x_axes, varpi.output_plot, varpi.time_step)
    video_soliton(phi_t_list, x_axes, varpi.output_plot, varpi.time_step)
    # x_force_axis, force_1d = force_x(var.dx, var.D, var.B)
    # force_plot(x_force_axis, force_2d, varpi.output_plot)
    # force_2d = fy1_force()
    # plt_force_3d(i, j, force_1d)
    # colormap_2d()


if __name__ == "__main__":
    start = time.process_time()
    print("start")
    main_plot()
    elapsed_time = time.process_time() - start
    print(str(elapsed_time) + " seconds")
    print("Done")
