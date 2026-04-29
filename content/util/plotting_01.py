import math
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.backend_bases

from  scipy  import  interpolate


def plot_polynomial(
    interpolation_function,
    a = 0,
    b = 10,
    n = 8,
    n_points = 1000,
):

    figure = plt.figure(figsize = (9.5, 9.0))
    random_spline = create_random_spline(a, b, n)

    interpolation_plot = draw_background(figure, random_spline, a, b, n_points)

    # we are using arrays as a substitute for pointers, which is probably not the
    # best way to do this
    nodes = [np.zeros(0), ]
    values = [np.zeros(0), ]
    
    figure.canvas.mpl_connect(
        'button_press_event', 
        lambda event : button_press(
            event,
            lambda point : add_point(
                figure,
                point,
                random_spline,
                nodes,
                values,
                interpolation_function,
                interpolation_plot,
            ),
        ),
    )
    plt.show()

def add_point(
    figure,
    point,
    random_spline,
    nodes, 
    values,
    interpolation_function,
    interpolation_plot,
):
    plt.figure(figure.number)    
    if not interpolation_plot.get_visible():
        interpolation_plot.set_visible(True)
    new_x = point[0]
    new_y = interpolate.splev(new_x, random_spline)
    
    # we only accept the point if it is new, to avoid division by 0
    if not any([(abs(new_x - node) < 1e-8) for node in nodes[0]]):
        
        plt.plot(new_x, new_y, 'bo')    
        
        nodes[0] = np.append(nodes[0], new_x)
        values[0] = np.append(values[0], new_y)

        xs, _ = interpolation_plot.get_data()
        ys = interpolation_function(values[0], nodes[0], xs)

        interpolation_plot.set_data(xs, ys)
    plt.draw()

def draw_background(figure, random_spline, a, b, n_points):
    plt.figure(figure.number)    
    plt.title('Stützstellen mit linker Maustaste platzieren')

    xs = np.linspace(a, b, n_points)
    ys = interpolate.splev(xs, random_spline)
    plt.plot (xs, ys, 'k-', linewidth = 2)  
    plt.axis([0, 10, np.min(ys) - 10.0, np.max(ys) + 10.0])
    interpolation_plot, = plt.plot(xs, np.zeros_like(ys), 'r-')
    interpolation_plot.set_visible(False)
    plt.draw()
    return interpolation_plot

def button_press(button_event, draw_function):
    if (button_event.button != 1):
        return
    if not(button_event.xdata and button_event.ydata):
        return
    draw_function(np.array([button_event.xdata, button_event.ydata]))

def create_random_spline(a, b, n):
    nodes  = (b - a) * np.random.rand(n)
    values = (b - a) * np.random.rand(n + 2)
    return interpolate.splrep(
        np.concatenate(([a], np.sort(nodes), [b])),
        values,
    )