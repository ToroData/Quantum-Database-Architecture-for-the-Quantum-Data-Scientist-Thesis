"""
Script to decompose a Toffoli (CCNOT) gate into basic quantum gates

Author: Ricard Santiago Raigada García
Date: 11/12/2024
Version: 1.1.1
"""
from qiskit import QuantumCircuit
import qiskit.quantum_info as qi
from qiskit.visualization import circuit_drawer


qc = QuantumCircuit(3)
qc.ccx(0, 1, 2)  # Toffoli Gate (CCNOT)
decomposed_qc = qc.decompose()

if __name__ == "__main__":
    circuit = circuit_drawer(
        decomposed_qc,
        output='mpl',
        style="bw"
        )
    circuit.savefig(
        "toffoli_decomposed_bw.png",
        format="png",
        dpi=300
        )
