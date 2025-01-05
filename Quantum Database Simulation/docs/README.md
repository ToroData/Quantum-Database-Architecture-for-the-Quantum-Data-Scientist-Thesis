# Quantum Database Simulation (qDB)

## Table of Contents

- [Description](#description)
- [Project Structure](#project-structure)
- [Installation](#installation)
- [Setup](#setup)
- [Usage](#usage)
- [Workflow](#workflow)
- [Licence](#licence)
- [Contact](#contact)

## Description

This project implements a Quantum Database (qDB) that analyzes salary equality between departments in a company. The qDB uses the Hilbert space $\mathcal{H}$ and, for the case presented, the Grover's Search Algorithm to simulate the qDB and optimize the query and data analysis process.

The salary is encoded in quantum states that allow the parallelization of searches. The Grover algorithm is used to identify the department that meets the equality condition. The Quantum Fourier Transform (QFT) is used as support for performing the sums.

A potential way of using a qDB applied to a real-world problem such as salary equality analysis is demonstrated.

## Project Structure

```bash
.
├── main.py               # Main script to run the entire project
├── src/
│   ├── classical_data.py   # Generates classical salary data for quantum encoding
│   ├── quantum_circuit.py  # Constructs the quantum database circuit and simulates it
├── plots/
│   ├── plot_config.py      # Configures global plot styles
│   ├── plot_generator.py   # Generates histograms for quantum results
├── environment.yml       # Conda environment file with all dependencies
└── README.md             # Documentation of the project
```

## Installation

Requirements:

- Python 3.9
- Qiskit
- Matplotlib
- Scikit-learn
- Conda (optional, but recommended)

## Setup

1. Create and activate the Conda environment:

```bash
conda env create -f environment.yml
conda activate quantumDatabase
```

## Usage

Run the main script to generate and analyze salary equality across departments:

```bash
python main.py --equal_department 3 --save
```

Options:
`--equal_department`: Specify the department with enforced salary equality (default: 4).
`--save`: Save the plot of results as an image (default: enabled).
`--no-save`: Disable saving the plot.

## Workflow

1. The `classical_data.py` module generates a dataset of salaries distributed by gender and salary. Equality is forced on one of them to compare the correct result in the quantum version. Then the dataset is scaled for the quantum simulation since it uses the QFT.

2. The database simulation is built in the quantum software layer. To do this, the following is created:

- Query register for department indices.
- Database register for salary data.
- Grover's algorithm identifies the department with salary equality.

3. Finally, a histogram is generated showing the probability of determining the department with salary equality.

## Licence

This project is licensed under the same terms as the BSc thesis it is derived from. Please refer to the thesis documentation for specific licensing details and any applicable restrictions.

## Contact

For questions or suggestions related specifically to this thesis, please contact:

- Name: Ricard Santiago Raigada García
- Email: <rraigadag@uoc.edu>
