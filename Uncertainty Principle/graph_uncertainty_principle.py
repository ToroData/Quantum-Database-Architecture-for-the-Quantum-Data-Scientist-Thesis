"""
This module generates a graph of the uncertainty principle.

Author: Ricard Santiago Raigada García
Date: 06/12/2024
Version: 0.0.1
"""
import matplotlib.pyplot as plt
import numpy as np


def set_plot_style() -> None:
    """
    Plot configuration style
    """
    plt.rcParams.update({
        'font.family': 'DejaVu Serif',
        'font.size': 12,
        'axes.titleweight': 'bold',
        'axes.titlesize': 18,
        'axes.titlepad': 60,
        'axes.labelsize': 12,
        'legend.fontsize': 12,
        'xtick.labelsize': 12,
        'ytick.labelsize': 12,
        'grid.color': '#CBCBCB',
        'grid.linewidth': 1.0,
        'axes.edgecolor': '#333333',
        'axes.linewidth': 1.2,
        'text.usetex': False
    })

def main() -> None:
    """
    Main function to generate uncertainty principle plot
    """
    # Params
    h = 6.62607015e-34
    hbar = h / (2 * np.pi)
    x = np.linspace(-10, 10, 400)
    p = np.linspace(-10, 10, 400)
    X, P = np.meshgrid(x, p)
    delta_x = np.abs(X)
    delta_p = np.abs(P)
    Z = delta_x * delta_p - hbar / 2
    set_plot_style()

    plt.figure(
        figsize=(8, 6)
        )
    contour = plt.contourf(
        X,
        P,
        Z,
        levels=50,
        cmap="inferno",
        alpha=0.8
        )
    cbar = plt.colorbar(contour)
    cbar.set_label(
        r'$\Delta x \Delta p - \frac{\hbar}{2}$',
        fontsize=14,
        style='italic'
        )

    plt.title(
        r'Uncertainty Principle: $\Delta x \Delta p \geq \frac{h}{4\pi}$',
        fontsize=18,
        style='italic'
        )
    plt.xlabel(
        r'Position uncertainty $\Delta x$',
        fontsize=16,
        style='italic'
        )
    plt.ylabel(
        r'Momentum uncertainty $\Delta p$',
        fontsize=16,
        style='italic'
        )
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    main()
