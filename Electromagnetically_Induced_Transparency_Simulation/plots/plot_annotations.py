"""
This module provides annotations for plots

Author: Ricard Santiago Raigada García
Date: 06/12/2024
Version: 0.0.1
"""

def get_annotations() -> list:
    """
    Returns a list of annotations for the plot

    Returns:
        list: A list of dictionaries containing annotation
    """
    return [
        {
            'text': 'Re[$\\chi^{(1)}$] (Control OFF)',
            'xy': (2.129, 0.0477),
            'xytext': (2.529, 0.0577),
            'color': '#646464'
        },
        {
            'text': 'Im[$\\chi^{(1)}$] (Control OFF)',
            'xy': (0.461, 0.122),
            'xytext': (0.603, 0.1353),
            'color': '#878787'
        },
        {
            'text': 'Re[$\\chi^{(1)}$] (Control ON)',
            'xy': (2.143, 0.0332),
            'xytext': (2.535, 0.0160),
            'color': '#1f77b4'
        },
        {
            'text': 'Im[$\\chi^{(1)}$] (Control ON)',
            'xy': (0.400, 0.0047),
            'xytext': (0.603, -0.0340),
            'color': '#ff7f0e'
        }
    ]
