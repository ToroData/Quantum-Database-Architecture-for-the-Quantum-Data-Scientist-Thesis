# Uncertainty Principle Graph

## Table of Contents

- [Description](#description)
- [Project Structure](#project-structure)
- [Installation](#installation)
- [Usage](#usage)
- [Licence](#licence)
- [Contact](#contact)

## Description

This project visualizes the Uncertainty Principle in quantum mechanics using a 2D contour plot. The graph illustrates the relation between position uncertainty \( \Delta x \) and momentum uncertainty \( \Delta p \), and the minimum bound defined by \( \frac{\hbar}{2} \).

<p style="text-align: center;">
  <img src="./Uncertainty%20Principle/docs/Uncertainty_principle.png" alt="Uncertainty Principle Graph" style="width: 75%;">
</p>

## Project Structure

```bash
.
├── graph_uncertainty_principle.py  # Main script to generate the uncertainty graph
└── README.md                       # Documentation for the project
```

## Installation

### Requirements

- Python 3.9
- Matplotlib
- Numpy

### Setup

Install:

   ```bash
   pip install matplotlib numpy
   ```

## Usage

1. Run the script:

   ```bash
   python graph_uncertainty_principle.py
   ```

2. The plot will visualize the following:
   - Contour levels representing \( \Delta x \Delta p - \frac{\hbar}{2} \).
   - A colorbar indicating the magnitude of the uncertainty difference.

## Licence

This project is licensed under the same terms as the BSc thesis it is derived from. Please refer to the thesis documentation for specific licensing details and any applicable restrictions.

## Contact

For questions or suggestions related specifically to this thesis, please contact:

- Name: Ricard Santiago Raigada García
- Email: <rraigadag@uoc.edu>
