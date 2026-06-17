import matplotlib.patches as patches
import matplotlib.pyplot as plt

def plot_RK_solution(u, mu, xlims=(-1.5, 1.5), ylims=(-0.8, 0.8)):
    plt.title(f'Runge-Kutta, {u.shape[0] - 1} Zeit-Schritte')
    plt.axis([*xlims, *ylims])
    plt.plot(u[:,0], u[:,2])
    # Erde und Mond
    delta = mu / (mu + 1.0) # gemeinsamer Schwerpunkt
    plt.plot(-delta,        0.0, 'o', markersize=5, color='deepskyblue')
    plt.plot((1.0 - delta), 0.0, 'o', markersize=2, color='gold')


def init_animation(mu, u0, v0, a0):
    ax = plt.gca()
    ax.axis([ -1.3, 1.3, -0.8, 0.8])
    ax.set_aspect('equal')


    delta = mu / (mu + 1.0) # gemeinsamer Schwerpunkt
    ax.plot(
        -delta,
        0.0,
        'o',
        markersize=10,
        color='deepskyblue',
    )
    ax.plot(
        (1.0 - delta),
        0.0,
        'o',
        markersize=4,
        color='gold',
    )

    ax.add_patch(
        plt.Circle(
            u0,
            0.02,
            color='maroon',
        )
    )
    ax.add_patch(
        patches.FancyArrow(
            *u0,
            *v0,
            color='maroon',
            head_width=0.03,
        )
    )
    ax.add_patch(
        patches.FancyArrow(
            *u0,
            *a0,
            color='forestgreen',
            head_width=0.03,
        )
    )

def draw_frame(frame, steps_per_frame, u, v, a):
    current_step  = frame * steps_per_frame
    previous_step = min(
        -1,
        (frame - 1) * steps_per_frame,
    )
    ax = plt.gca()
    ax.plot(
        u[previous_step + 1:current_step + 1, 0],
        u[previous_step + 1:current_step + 1, 1],
        color='steelblue',
    )
    ax.patches[0].set_center(u[current_step,:])
    ax.patches[1].set_data(
        x =u[current_step,0],
        y =u[current_step,1],
        dx=v[current_step,0],
        dy=v[current_step,1],
    )
    ax.patches[2].set_data(
        x =u[current_step,0],
        y =u[current_step,1],
        dx=a[current_step,0],
        dy=a[current_step,1],
    )
