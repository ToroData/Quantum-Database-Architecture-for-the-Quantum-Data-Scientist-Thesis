"""
Module to run the Quantum Database simulation using Qiskit's QASM simulator

Author: Ricard Santiago Raigada García
Date: 06/12/2024
Version: 0.0.1
"""
from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister, Aer, execute
from typing import List, Any
from numpy import pi

def make_quantum_database_gate(
    address: QuantumRegister,
    data: QuantumRegister,
    inputs: List[List[int]]
    ) -> Any:
    """
    Creates a quantum database gate that maps input data based on address

    Args:
        address (QuantumRegister): quantum register for address qubits
        data (QuantumRegister): quantum register for data qubits
        inputs (List[List[int]]): list of input values to store in quantum database

    Returns:
        Any: returns a quantum gate representing the quantum database
    """
    qc = QuantumCircuit(address, data)
    for indx in range(len(inputs)):
        binary_indx = bin(4 + indx)[-2:]
        qc.x(address[0]) if binary_indx[0] == '0' else None
        qc.x(address[1]) if binary_indx[1] == '0' else None

        for j, value in enumerate(inputs[indx]):
            binary_value = bin(4 + value)[-2:]
            qc.ccx(address[0], address[1], data[2 * j]
                   ) if binary_value[0] == '1' else None
            qc.ccx(address[0], address[1], data[2 * j + 1]
                   ) if binary_value[1] == '1' else None

        [qc.x(address[i]) for i in range(2) if binary_indx[i] == '0']
    return qc.to_gate(label="QuantumDatabase")


def QFT_gate(n: int) -> Any:
    """
    Creates a Quantum Fourier Transform (QFT) gate

    Args:
        n (int): number of qubits

    Returns:
        Any: quantum gate representing the QFT
    """
    qc = QuantumCircuit(n)
    for i in range(n - 1, -1, -1):
        qc.h(i)
        for j in range(i - 1, -1, -1):
            qc.cp(pi / (2 ** (i - j)), j, i)
    for i in range(n // 2):
        qc.swap(i, n - i - 1)
    return qc.to_gate(label=f"QFT({n})")


def data_processor_gate(
    data: QuantumRegister,
    output: QuantumRegister
    ) -> Any:
    """
    Creates a gate for processing quantum data using QFT and additional logic

    Args:
        data (QuantumRegister): quantum register for input data
        output (QuantumRegister): quantum register for result qubits

    Returns:
        Any: a quantum gate representing the data processor
    """
    qc = QuantumCircuit(data, output)
    qc.append(QFT_gate(len(output)), output)
    for q in range(len(data)):
        add_qubit(qc, data, output, q)
        add_qubit(qc, data, output, q) if q % 2 == 0 else None
    qc.append(QFT_gate(len(output)).inverse(), output)
    return qc.to_gate(label="DataProcessor")


def add_qubit(
    qc: QuantumCircuit,
    data: QuantumRegister,
    output: QuantumRegister,
    q: int,
    sign: int = 1
    ) -> None:
    """
    Adds the contribution of a single qubit to the quantum data processor

    Args:
        qc (QuantumCircuit): quantum circuit to which the qubit's contribution is added
        data (QuantumRegister): quantum register for input data qubits
        output (QuantumRegister): quantum register for result qubits
        q (int): index of the qubit in the data register
        sign (int, optional): the sign of the contribution (+1,-1). Defaults to 1.
    """
    sign = -sign if q >= len(data) // 2 else sign
    for indx, qb in enumerate(output):
        qc.cp(sign * pi / (2 ** (3 - indx)), data[q], qb)


def data_validator_gate(output: QuantumRegister) -> Any:
    """
    Create a data validator or oracle gate

    Args:
        output (QuantumRegister): quantum register for result qubits

    Returns:
        Any: quantum gate representing the data validator
    """
    qc = QuantumCircuit(output)
    qc.x(output)
    qc.h(output[-1])
    qc.mct(output[:-1], output[-1])
    qc.h(output[-1])
    qc.x(output)
    return qc.to_gate(label="DataValidator")


def create_quantum_circuit(inputs: List[List[int]]) -> QuantumCircuit:
    """
    Constructs the main quantum circuit for querying and validating the database

    Args:
        inputs (List[List[int]]): The normalized inputs for the database

    Returns:
        QuantumCircuit: The complete quantum circuit
    """
    address = QuantumRegister(2, name="query")
    data = QuantumRegister(12, name="database")
    output = QuantumRegister(4, name="results")
    classical = ClassicalRegister(2, name="c")
    qc = QuantumCircuit(address, data, output, classical)

    qc.h(address)

    qc.append(make_quantum_database_gate(address, data, inputs), address[:] + data[:])
    qc.append(data_processor_gate(data, output), data[:] + output[:])
    qc.append(data_validator_gate(output), output[:])

    processor_inverse_gate = data_processor_gate(data, output).inverse()
    processor_inverse_gate.name = "DataProcessor Inverse"
    qc.append(processor_inverse_gate, data[:] + output[:])

    database_inverse_gate = make_quantum_database_gate(address, data, inputs).inverse()
    database_inverse_gate.name = "QuantumDatabase Inverse"
    qc.append(database_inverse_gate, address[:] + data[:])

    # Grover's diffusion operator
    qc.h(address)
    qc.x(address)
    qc.cz(address[0], address[1])
    qc.x(address)
    qc.h(address)

    qc.measure(address, classical)
    qc = qc.reverse_bits()
    return qc



def simulate_circuit(qc: QuantumCircuit) -> dict:
    """
    Simulates the quantum circuit using the QASM simulator

    Args:
        qc (QuantumCircuit): the quantum circuit to simulate

    Returns:
        dict: a dictionary of measurement results with counts
    """
    backend = Aer.get_backend('qasm_simulator')
    job = execute(qc, backend, shots=1000)
    result = job.result()
    return result.get_counts()
