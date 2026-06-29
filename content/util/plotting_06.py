import matplotlib.patches as patches
import matplotlib.pyplot as plt

def plot_RK_solution(u, mu, verfahren, xlims=(-1.5, 1.5), ylims=(-0.8, 0.8)):
    plt.title(f'Extrapolation ({verfahren}), {u.shape[0] - 1} Zeit-Schritte')
    plt.axis([*xlims, *ylims])
    plt.plot(u[:,0], u[:,2])
    # Erde und Mond
    delta = mu / (mu + 1.0) # gemeinsamer Schwerpunkt
    plt.plot(-delta,        0.0, 'o', markersize=5, color='deepskyblue')
    plt.plot((1.0 - delta), 0.0, 'o', markersize=2, color='gold')
