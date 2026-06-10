import math
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.backend_bases

def setup_plotting(title, figsize=(15,8)):
    plt.figure(figsize=figsize)
    plt.suptitle(title)
    fig11 = plt.subplot(2, 3, 1)
    plt.title("explizites Euler-Verfahren (Lösung)")
    fig12 = plt.subplot(2, 3, 2)
    plt.title("modifiziertes Euler-Verfahren (Lösung)")
    fig13 = plt.subplot(2, 3, 3)
    plt.title("Heun-Verfahren (Lösung)")
    fig21 = plt.subplot(2, 3, 4)
    plt.title("explizites Euler-Verfahren (Fehler)")
    fig22 = plt.subplot(2, 3, 5)
    plt.title("modifiziertes Euler-Verfahren (Fehler)")
    fig23 = plt.subplot(2, 3, 6)
    plt.title("Heun-Verfahren (Fehler)")
    return (fig11, fig12, fig13, fig21, fig22, fig23)

def add_to_plot(fig, ts, ys_1, errors_1, ys_2, errors_2, ys_3, errors_3, symbol='o'):
    fig11, fig12, fig13, fig21, fig22, fig23 = fig
    plt.sca(fig11)
    plt.plot(ts, ys_1, color="red", marker=symbol)
    plt.sca(fig12)
    plt.plot(ts, ys_2, color="green", marker=symbol)
    plt.sca(fig13)
    plt.plot(ts, ys_3, color="blue", marker=symbol)
    plt.sca(fig21)
    plt.semilogy(ts, errors_1, color="red", marker=symbol)
    plt.sca(fig22)
    plt.semilogy(ts, errors_2, color="green", marker=symbol)
    plt.sca(fig23)
    plt.semilogy(ts, errors_3, color="blue", marker=symbol)


def draw_frame(frame, n_steps, t0, x_max, R, u, a, b, c):
    plt.clf()
    ax = plt.gca()
    
    current_x = frame * x_max / n_steps
    
    #  Reifen
    ax.add_patch(plt.Circle((current_x, 0), R,        color='black'))
    ax.add_patch(plt.Circle((current_x, 0), R - 0.25, color='lightgray'))

    #  Speichen
    for i in range(5):
        plt.plot(
            [current_x, current_x + (R - 0.125) * np.cos(i * 0.4 * math.pi + t0 - current_x)], 
            [0.0,                   (R - 0.125) * np.sin(i * 0.4 * math.pi + t0 - current_x)],
            linewidth=15,
            solid_capstyle='butt',
            color='black',
        )

    #  Nabe
    ax.plot([current_x], [0.0], marker='o', color='#eeeeee', markersize=12)
    ax.plot([0.0, current_x], [0.0, 0.0], linewidth=3, color='#eeeeee')

    #  Boden
    ax.fill([-1.3, 1.3 + 4.0 * math.pi, 1.3 + 4.0 * math.pi, -1.3],[-2 * R, -2 * R, -R, -R], color='brown')
    ax.text(0.0, -1.5 * R, 'Zykloide', fontsize=15, horizontalalignment='center', verticalalignment='center', color='#ff8888')

    #  Punkte auf dem Reifen
    ax.plot(a[0,frame], a[1,frame], marker='o', color='lightgreen', markersize=12)
    ax.plot(b[0,frame], b[1,frame], marker='o', color='#8888ff',    markersize=12)
    ax.plot(c[0,frame], c[1,frame], marker='o', color='#ff8888',    markersize=12)
    ax.plot(u[0,frame], u[1,frame], marker='o', color='cyan',       markersize=8 )

    #  Bewegung der Punkte auf dem Reifen
    ax.plot(a[0,:frame + 1], a[1,:frame + 1], linewidth=5, color='lightgreen')
    ax.plot(b[0,:frame + 1], b[1,:frame + 1], linewidth=5, color='#8888ff')
    ax.plot(c[0,:frame + 1], c[1,:frame + 1], linewidth=5, color='#ff8888')
    ax.plot(u[0,:frame + 1], u[1,:frame + 1], linewidth=3, color='cyan')

    ax.set_aspect('equal')
    plt.xlim(-1.3, 1.3 + 4.0 * math.pi)
    plt.ylim(-2 * R, 2 * R)
    plt.axis('off')
    return 