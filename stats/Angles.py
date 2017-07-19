from core.colorama import init, Fore
import numpy as np
import matplotlib.pyplot as plt

init()

def plotAngles(match):
    X, Y = np.mgrid[0:4, 0:3]
    T = np.arctan2(Y - 3 / 2., X - 4 / 2.)
    R = 10 + np.sqrt((Y - 3 / 2.0) ** 2 + (X - 4 / 2.0) ** 2)
    U, V = R * np.cos(T), R * np.sin(T)

    plt.axes([0.025, 0.025, 0.95, 0.95])
    plt.quiver(X, Y, U, V, R, alpha=.5)
    plt.quiver(X, Y, U, V, edgecolor='k', facecolor='None', linewidth=0.5)

    plt.xlim(-1, 4)
    plt.xticks(())
    plt.ylim(-1, 3)
    plt.yticks(())

    plt.show()