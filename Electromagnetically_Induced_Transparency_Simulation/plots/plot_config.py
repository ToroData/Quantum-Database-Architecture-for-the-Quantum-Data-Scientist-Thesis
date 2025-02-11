"""
This module offers global styles configuration

Author: Ricard Santiago Raigada García
Date: 06/12/2024
Version: 0.0.1
"""
import matplotlib.pyplot as plt


def configure_plot_styles() -> None:
    """
    Configures global styles for all plots
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
