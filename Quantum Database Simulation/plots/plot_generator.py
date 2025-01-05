"""
This module generates plots for visualizing quantum circuit simulation results

Author: Ricard Santiago Raigada García
Date: 06/12/2024
Version: 0.0.1
"""
from typing import Dict
import matplotlib.pyplot as plt
import datetime
from plots.plot_config import configure_plot_styles


def configure_ax(
    ax: plt.Axes,
    xlabel: str,
    ylabel: str,
    title: str,
    titlepad: int = 35) -> None:
    """
    Configures the settings for a plot

    Args:
        ax (matplotlib.axes.Axes): the axes to configure
        xlabel (str): label for the x-axis
        ylabel (str): label for the y-axis
        title (str): title of the plot
        titlepad (int, optional): padding for the title. Defaults to 35
    """
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    ax.set_title(title, pad=titlepad)
    ax.grid(axis='y', linewidth=0.7, alpha=0.6)
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)


def generate_histogram_plot(
    counts: Dict[str, int],
    title: str = "Quantum Circuit Simulation Results",
    save: bool = True
    ) -> None:
    """
    Generates a histogram plot for the simulation results.

    Args:
        counts (dict): the simulation results as a dictionary {state: frequency}
        title (str, optional): default title "Quantum Circuit Simulation Results"
        save (bool, optional): whether to save the plot as a file. Defaults to True
    """
    configure_plot_styles()
    states = list(counts.keys())
    frequencies = list(counts.values())

    fig, ax = plt.subplots(figsize=(10, 6))
    ax.bar(states, frequencies, color='#1f77b4', alpha=0.7)

    configure_ax(
        ax,
        xlabel="Quantum States",
        ylabel="Frequency",
        title=title
    )

    ax.set_xticks(range(len(states)))
    ax.set_xticklabels(states, rotation=45, ha='right')

    plt.tight_layout()
    if save:
        timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"histogram_{timestamp}.png"
        plt.savefig(f"plots/{filename}", dpi=600)
        print(f"Plot saved as {filename}")
    plt.show()
