import matplotlib.patches as patches
import matplotlib.pyplot as plt

def plot_RK_solution(us, ts, hs, mu, xlims=(-1.5, 1.2), ylims=(-1.5, 1.5)):
    plt.subplot(2,1,1)
    plt.title(f'Dormand-Prince, {us.shape[0] - 1} Zeit-Schritte')
    plt.axis([*xlims, *ylims])
    plt.plot(us[:,0], us[:,2])
    delta = mu / (mu + 1.0) # gemeinsamer Schwerpunkt
    plt.plot(-delta,        0.0, 'o', markersize=5, color='deepskyblue')  # Erde
    plt.plot((1.0 - delta), 0.0, 'o', markersize=2, color='gold')         # Mond

    plt.subplot(2,1,2)
    plt.title('Zeit vs. Schrittweite')
    plt.plot(ts, hs)
    plt.xlim(ts[0], ts[-1])


def init_animation(ax, mu, u0, v0, ts, hs):
    ax[0].axis([ -1.5, 1.2, -1.5, 1.5])
    delta = mu / (mu + 1.0) # gemeinsamer Schwerpunkt
    ax[0].plot(
        -delta,
        0.0,
        'o',
        markersize=10,
        color='deepskyblue',
    )
    ax[0].plot(
        (1.0 - delta),
        0.0,
        'o',
        markersize=4,
        color='gold',
    )

    ax[0].add_patch(
        plt.Circle(
            u0,
            0.02,
            color='maroon',
        )
    )
    ax[0].add_patch(
        patches.FancyArrow(
            *u0,
            *v0,
            color='maroon',
            head_width=0.03,
        )
    )
    ax[1].set_title('Zeit vs. Schrittweite')
    ax[1].plot(ts, hs)
    ax[1].plot(
            ts[0],
            hs[0],
            color='maroon',
            marker='o',
    )
    plt.xlim(ts[0], ts[-1])

def draw_frame(frame, ax, steps_per_frame, u, v, ts, hs):
    current_step  = frame * steps_per_frame
    previous_step = min(
        -1,
        (frame - 1) * steps_per_frame,
    )
    ax[0].plot(
        u[previous_step + 1:current_step + 1, 0],
        u[previous_step + 1:current_step + 1, 1],
        color='steelblue',
    )
    ax[0].patches[0].set_center(u[current_step,:])
    ax[0].patches[1].set_data(
        x =u[current_step,0],
        y =u[current_step,1],
        dx=v[current_step,0],
        dy=v[current_step,1],
    )
    ax[1].get_children()[1].set_xdata(ts[current_step])
    ax[1].get_children()[1].set_ydata(hs[current_step])
