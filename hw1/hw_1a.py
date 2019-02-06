import numpy as np
import matplotlib.pyplot as plt


def g(E, e, M):
    return E - e*np.sin(E) - M

def dgdE(E, e):
    return 1 - e*np.cos(E)

def kepler_solver(M, e):
    E0 = M + 0.85*e*np.sign(np.sin(M)) # starting guess
    g0 = g(E0, e, M)
    dgdE0 = dgdE(E0, e)

    while np.abs(-g(E0, e, M)/dgdE(E0, e)) > 1E-14:
        E = E0 - g(E0, e, M)/dgdE(E0, e)
        E0 = E
    return E0

if __name__ == '__main__':
    plt.figure()
    plt.xlabel('M')
    plt.ylabel('E(M)')
    elist = np.arange(0.1, 1., 0.1)
    Mlist = np.linspace(0.001, 2*np.pi, 1000, endpoint=False)
    for e in elist:
        Elist = []
        for n, M in enumerate(Mlist):
            E = kepler_solver(M, e)
            Elist.append(E)
        plt.plot(Mlist, Elist, label=round(e, 1))
    plt.legend(title='eccentricity')
    plt.show()
