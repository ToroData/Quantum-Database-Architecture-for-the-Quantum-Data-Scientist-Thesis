"""
This module generates graphs to visualize the real and imaginary parts of
the first-order electrical susceptibility

Author: Ricard Santiago Raigada García
Date: 06/12/2024
Version: 0.0.1
"""
from typing import List, Dict, Optional
import matplotlib.pyplot as plt
from plots.plot_config import configure_plot_styles
from plots.plot_annotations import get_annotations


def configure_ax(ax: plt.Axes,
                 xlabel: str,
                 ylabel: str,
                 title: str,
                 titlepad: Optional[int] = None
                 ) -> None:
    """
    Configures the settings for a plot.

    Args:
        ax (matplotlib.axes.Axes): The axes to configure
        xlabel (str): Label for the x-axis
        ylabel (str): Label for the y-axis
        title (str): Title of the plot
        titlepad (int, optional): Padding for the title. Defaults to plt.rcParams['axes.titlepad']
    """
    if titlepad is None:
        titlepad = plt.rcParams.get('axes.titlepad', 35)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    ax.set_title(title, pad=titlepad)
    ax.grid(axis='y', linewidth=0.7, alpha=0.6)
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['bottom'].set_linewidth(1.5)
    ax.spines['left'].set_linewidth(False)


def add_annotations(ax: plt.Axes,
                    annotations: List[Dict[str, any]]
                    ) -> None:
    """
    Adds annotations to the plot.

    Args:
        ax (matplotlib.axes.Axes): The axes to annotate.
        annotations (list of dict): A list of annotations:
            'text': Annotation text
            'xy': Coordinates to point to
            'xytext': Coordinates for the text
            'color': Color of the annotation
    """
    for ann in annotations:
        ax.annotate(
            ann['text'],
            xy=ann['xy'],
            xytext=ann['xytext'],
            color=ann['color'],
            arrowprops={"arrowstyle": '->', "color": ann['color']})


def generate_plot(
    delta_p: List[float],
    gamma: float,
    Re_chi1_on: List[float],
    Im_chi1_on: List[float],
    Re_chi1_off: List[float],
    Im_chi1_off: List[float],
) -> None:
    """
    Generates a full plot with active and inactive control laser states.

    Args:
        delta_p (np.array): Detuning of a single photon
        gamma (float): Decay rate
        Re_chi1_on, Im_chi1_on: Real and imaginary parts of susceptibility (control ON)
        Re_chi1_off, Im_chi1_off: Real and imaginary parts of susceptibility (control OFF)
    """
    configure_plot_styles()
    annotations = get_annotations()
    fig, ax = plt.subplots(figsize=(12, 10))

    ax.plot(
        delta_p / gamma,
        Re_chi1_on,
        label='Re[$\\chi^{(1)}$] (Control ON)',
        color='#1f77b4',
        linestyle='-')
    ax.plot(
        delta_p / gamma,
        Im_chi1_on,
        label='Im[$\\chi^{(1)}$] (Control ON)',
        color='#ff7f0e',
        linestyle='-')
    ax.plot(
        delta_p / gamma,
        Re_chi1_off,
        label='Re[$\\chi^{(1)}$] (Control OFF)',
        color='#646464',
        linestyle='--')
    ax.plot(
        delta_p / gamma,
        Im_chi1_off,
        label='Im[$\\chi^{(1)}$] (Control OFF)',
        color='#878787',
        linestyle='--')

    configure_ax(
        ax,
        'Detuning $\\Delta_p/\\gamma$',
        'Susceptibility $\\chi^{(1)}$',
        'Real and Imaginary Parts of First Order Electrical Susceptibility')

    add_annotations(ax, annotations)

    ax.legend(
        loc='upper right',
        bbox_to_anchor=(0.56, 1.10),
        ncol=2,
        frameon=False,
        title_fontsize=14
    )
    plt.show()


def generate_imaginary_active_plot(
    delta_p: List[float],
    gamma: float,
    Im_chi1_on: List[float]
) -> None:
    """
    Generates the plot for the imaginary part of susceptibility with the control laser ON.

    Args:
        delta_p (np.array): Detuning of a single photon
        gamma (float): Decay rate
        Im_chi1_on (list): Imaginary part of susceptibility (control ON)
    """
    configure_plot_styles()
    fig, ax = plt.subplots(figsize=(10, 6))

    ax.plot(
        delta_p / gamma,
        Im_chi1_on,
        label='Im[$\\chi^{(1)}$] (Control ON)',
        color='#ff7f0e',
        linestyle='-')
    configure_ax(
        ax,
        'Detuning $\\Delta_p/\\gamma$',
        'Imaginary Susceptibility $\\chi^{(1)}$',
        'Imaginary Part of First Order Susceptibility (Control ON)',
        titlepad=35)
    ax.legend(
        loc='upper right',
        bbox_to_anchor=(0.3, 1.10),
        ncol=2,
        frameon=False,
        title_fontsize=14
    )
    plt.show()
