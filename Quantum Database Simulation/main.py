"""
Main file to run the entire project, and simulate a Quantum Database

Author: Ricard Santiago Raigada García
Date: 06/12/2024
Version: 0.0.1
"""
import argparse
from src.classical_data import generate_normalized_inputs
from src.quantum_circuit import create_quantum_circuit, simulate_circuit
from qiskit.visualization import plot_histogram
from plots.plot_generator import generate_histogram_plot
import matplotlib.pyplot as plt


def main(equal_department=4, save=True):
    """
    Function to generate salary data by department and execute a
    classical and quantum circuit to find the department with equal pay

    Args:
        equal_department (int, optional): Forces a department to be equal
        to check the same solution in classical and in quantum. Defaults to 4
        save (bool, optional): Save the plot as an image. Defaults to True
    """
    normalized_inputs, equal_departments = generate_normalized_inputs(
        equal_department=equal_department
    )

    qc = create_quantum_circuit(normalized_inputs)
    counts = simulate_circuit(qc)
    print("Simulation results:", counts)

    generate_histogram_plot(counts, save=save)
    plt.show()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Quantum database simulation.")
    parser.add_argument(
        "--equal_department",
        type=int,
        default=4,
        help="Department for which equal pay is forced, thus validating the same result "
        "both by the classical and the quantum method (default value: 4)"
    )
    parser.add_argument(
        "--save",
        dest="save",
        action="store_true",
        help="Save the plot as an image. Enabled by default"
    )
    parser.add_argument(
        "--no-save",
        dest="save",
        action="store_false",
        help="Do not save the plot as an image"
    )
    parser.set_defaults(save=True)
    args = parser.parse_args()
    main(
        args.equal_department,
        save=args.save
        )
