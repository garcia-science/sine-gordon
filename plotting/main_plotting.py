from plotting.axes_soliton_2D import axes_construction_two_d
import input.variables as var
import plotting.plot_variables as varpi
from plotting.loading_data import load_data
# from plotting.plot_center import plot_center
from plotting.plot_soliton_2D import plot_soliton2d
from plotting.soliton_video import video_soliton
# from plotting.plot_colormap_2d import colormap_2d
import time


def main_plot():
    x_axes_center, x_axes, X, Y = axes_construction_two_d(varpi.time_step, var.dx * var.D, var.D)
    center, phi_t_list = load_data(varpi.time_step, var.output + var.dir_name + '\\center.txt',
                                   var.output + var.dir_name)
    # plot_center(x_axes_center, center, varpi.output_plot)
    # plot_soliton2d(phi_t_list, x_axes, varpi.output_plot, varpi.time_step)
    video_soliton(phi_t_list, x_axes, varpi.output_plot, varpi.time_step)
    # colormap_2d()


if __name__ == "__main__":
    start = time.process_time()
    print("start")
    main_plot()
    elapsed_time = time.process_time() - start
    print(str(elapsed_time) + " seconds")
    print("Done")
