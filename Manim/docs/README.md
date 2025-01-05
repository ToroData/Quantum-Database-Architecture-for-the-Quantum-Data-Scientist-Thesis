# Electromagnetically Induced Transparency (EIT) Semiclassical Visualization

## Table of Contents

- [Description](#description)
- [Project Structure](#project-structure)
- [Installation](#installation)
- [Usage](#usage)
- [Licence](#licence)
- [Contact](#contact)

## Description

This script generates a visualization of EIT using a semiclassical approximation. It includes:

- Representation of the wave function.
- Velocity groups and photons.
- Representation of the Hamiltonian and Rabi frequencies.

<video controls width="100%">
  <source src="EITSetup.mp4" type="video/mp4">
  Your browser does not support the video tag.
</video>

## Project Structure

```bash
.
├── eit_visualization.py     # Main script to render the EIT visualization
└── custom_template.tex      # Custom LaTeX template for math rendering
```

## Installation

### Requisitos previos

1. Manim Community v0.18.1
2. Python 3.9.21
3. Additional dependencies:
   - `libcairo2-dev`
   - `ffmpeg`
   - LaTeX (`texlive` and related packages)

### Instrucciones

Run the following commands to install the required dependencies:

```bash
sudo apt update
sudo apt install libcairo2-dev ffmpeg \
    texlive texlive-latex-extra texlive-fonts-extra \
    texlive-latex-recommended texlive-science tipa \
    libpango1.0-dev
pip install manim
pip install IPython --upgrade
```

## Usage

### Ejecutar el script

Render the animation by running:

```bash
manim -pql eit_visualization.py EITSetup
```

- Optionally:
  - `-p -r 3840,2160`: Custom resolution (4K).

## Licence

This project is licensed under the same terms as the BSc thesis it is derived from. Please refer to the thesis documentation for specific licensing details and any applicable restrictions.

## Contact

For questions or suggestions related specifically to this thesis, please contact:

- Name: Ricard Santiago Raigada García
- Email: <rraigadag@uoc.edu>
