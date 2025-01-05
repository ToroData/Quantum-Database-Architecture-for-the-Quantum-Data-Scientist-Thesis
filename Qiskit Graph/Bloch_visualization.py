"""
Script to create a pure and mixed state and plot them on Bloch Sphere and matrix density

Author: Ricard Santiago Raigada García
Date: 11/12/2024
Version: 1.1.1
"""
from qiskit import QuantumCircuit
from qiskit.visualization import plot_bloch_multivector
from qiskit.quantum_info import Statevector, DensityMatrix
from matplotlib.figure import Figure
import matplotlib.pyplot as plt


def save_bloch_multivector(state: Statevector, filename: str) -> None:
    """Function to generate a bloch sphere and save it

    Args:
        state (Statevector): quantum state to plot
        filename (str): file name to save the plot
    """
    bloch_plot = plot_bloch_multivector(state.data)
    bloch_plot.savefig(
        filename,
        format="png",
        dpi=300
    )
    plt.close()


def save_density_matrix_plot(
        density_matrix: DensityMatrix,
        filename: str) -> None:
    """Function to generate a density matrix and save it

    Args:
        density_matrix (DensityMatrix): density matrix to plot
        filename (str): file name to save the plot
    """
    density_plot = density_matrix.draw('city')
    fig: Figure = density_plot.figure
    ax = fig.axes[0]
    ax.set_zlim(0, 1)
    plt.figure(fig.number)
    fig.savefig(
        filename,
        format="png",
        dpi=300
    )
    plt.close()


# Pure State
qc_pure = QuantumCircuit(1)
qc_pure.h(0)
pure_state = Statevector.from_instruction(qc_pure)
pure_density = DensityMatrix(pure_state)

# Mixed State
mixed_state = 0.6 * \
    DensityMatrix.from_label('0') + 0.4 * DensityMatrix.from_instruction(qc_pure)


if __name__ == "__main__":
    save_bloch_multivector(pure_state, "Bloch_pure_state.png")
    save_bloch_multivector(mixed_state, "Bloch_mixed_state.png")
    save_density_matrix_plot(pure_density, "Density_pure_state.png")
    save_density_matrix_plot(mixed_state, "Density_mixed_state.png")

