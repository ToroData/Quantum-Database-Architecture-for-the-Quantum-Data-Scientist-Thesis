# Quantum Database Architecture for the Quantum Data Scientist: A Theoretical Treatise on Lindblad Operators, EIT in Multi-Level Atomic Ensembles, and High-Fidelity Data Encoding

This repository hosts all the projects developed within the framework of the Bachelor thesis, refer to [![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.14810946.svg)](https://doi.org/10.5281/zenodo.14810946).

Quantum memories are indispensable for driving secure quantum communication networks, as well as for solving challenges in large-scale data storage and processing. This thesis is based on quantum mechanics and quantum optics—particularly on Electromagnetically Induced Transparency (EIT) and the DLCZ protocol—, and addresses critical issues of Big Data management, ethical information handling, and data security in data science. However, providing high-fidelity storage, mitigating noisy channels, and designing efficient quantum algorithms for secure and ethical data handling remains an open challenge. This thesis presents an architecture for quantum databases that combines the physics of multi-level atomic ensembles with state-of-the-art quantum algorithms. The objective is to attain secure and ethical Big Data handling by means of quantum memory systems. A review is carried out through Lindblad operators and light-matter interactions, establishing a quantum database architecture capable of responding to the requirements of data science. Both in the Lambda scheme within an EIT-based quantum memory and the DLCZ protocol, the system achieves high-fidelity photon-atom coherence and secure storage. At the algorithmic level, the proposal leverages Hilbert subspaces as logical partitions  —similar to sharding in classical databases—, enabling scalable data encoding and manipulation through unitary operations. These operations allow for the efficient and parallel retrieval of information, while maintaining coherence in noisy environments. The simulation results confirm the theoretical framework described and demonstrate the system's ability to establish an ethical treatment of Big Data while strengthening information security. This thesis thus novelly proposes the integration of quantum systems in data science, addressing privacy, ethics, and security issues at scale, offering a framework with practical applications of secure data governance.

## Table of Contents

1. [Quantum Database Simulation (qDB)](#1-quantum-database-simulation-qdb)
2. [Visualization and Decomposition of Quantum Gates](#2-visualization-and-decomposition-of-quantum-gates)
3. [Electromagnetically Induced Transparency (EIT) Semiclassical Visualization](#3-electromagnetically-induced-transparency-eit-semiclassical-visualization)
4. [EIT Simulation and Visualization](#4-eit-simulation-and-visualization)
5. [Uncertainty Principle Graph](#5-uncertainty-principle-graph)

---

## 1. Quantum Database Simulation (qDB)

This project implements a Quantum Database (qDB) that analyzes salary equality between departments in a company. The qDB uses the Hilbert space $\mathcal{H}$ and, for the case presented, the Grover's Search Algorithm to simulate the qDB and optimize the query and data analysis process.

The salary is encoded in quantum states that allow the parallelization of searches. The Grover algorithm is used to identify the department that meets the equality condition. The Quantum Fourier Transform (QFT) is used as support for performing the sums.

A potential way of using a qDB applied to a real-world problem such as salary equality analysis is demonstrated.

- Link to Project: [Quantum Database Simulation (qDB)](./Quantum%20Database%20Simulation/docs/README.md)

---

## 2. Visualization and Decomposition of Quantum Gates

This directory contains the code that generates Figures A.7 and A.8 in the body of the BsC thesis. The scripts generate visualizations of the density matrices and the Bloch sphere representation for both a pure state and a mixed state.

1. Bloch Sphere:

<div style="display: flex; flex-wrap: wrap; justify-content: space-between;"> <div style="width: 48%;"> <p><b>Pure state (`Bloch_pure_state.png`):</b></p> <img src="./Qiskit%20Graph/docs/img/Bloch_pure_state.png" alt="Bloch Pure State" style="width: 50%;"> </div> <div style="width: 48%;"> <p><b>Mixed state (`Bloch_mixed_state.png`):</b></p> <img src="./Qiskit%20Graph/docs/img/Bloch_mixed_state.png" alt="Bloch Mixed State" style="width: 50%;"> </div> </div>

2. Density matrix:

<div style="display: flex; flex-wrap: wrap; justify-content: space-between;"> <div style="width: 48%;"> <p><b>Pure state (`Density_pure_state.png`):</b></p> <img src="./Qiskit%20Graph/docs/img/Density_pure_state.png" alt="Density Pure State" style="width: 75%;"> </div> <div style="width: 48%;"> <p><b>Mixed state (`Density_mixed_state.png`):</b></p> <img src="./Qiskit%20Graph/docs/img/Density_mixed_state.png" alt="Density Mixed State" style="width: 75%;"> </div> </div>

3. Decomposition of the Toffoli Gate:

<div style="text-align: center;"> <p><b>`toffoli_decomposed_bw.png`:</b></p> <img src="./Qiskit%20Graph/docs/img/toffoli_decomposed_bw.png" alt="Toffoli Decomposed" style="width: 50%;"> </div>

- Link to Project: [Visualization and Decomposition of Quantum Gates](./Qiskit%20Graph/docs/README.md)

---

## 3. Electromagnetically Induced Transparency (EIT) Semiclassical Visualization

This script generates a visualization of EIT using a semiclassical approximation. It includes:

- Representation of the wave function.
- Velocity groups and photons.
- Representation of the Hamiltonian and Rabi frequencies.

<video controls width="100%">
  <source src="EITSetup.mp4" type="video/mp4">
  Your browser does not support the video tag.
</video>

- Link to Project: [EIT Semiclassical Visualization](./Manim/docs/README.md)

---

## 4. EIT Simulation and Visualization

This project hosts a numerical simulation of Electromagnetically Induced Transparency (EIT) based on the Lindblad equation as well as the final visualization of the real and imaginary part of the first-order electrical susceptibility.

- Main Features:
  - Simulation of EIT in a three-level Lambda scheme.
  - Visualization of susceptibility for control ON/OFF states.

<p style="text-align: center;">
  <img src="Real_and_Imaginary_Parts_of_First_Order_Electrical_Susceptibility.png" alt="Real and Imaginary Parts of First Order Electrical Susceptibility" style="width: 50%;">
</p>
<p style="text-align: center;">
  <img src="Imaginary_Part_of_First_Order_Susceptibility_Control_ON.png" alt="Imaginary Part of Susceptibility" style="width: 50%;">
</p>

- Link to Project: [Electromagnetically Induced Transparency (EIT): Simulation and Visualization](./Electromagnetically%20Induced%20Transparency%20Simulation/docs/README.md)

---

## 5. Uncertainty Principle Graph

This project visualizes the Uncertainty Principle in quantum mechanics using a 2D contour plot. The graph illustrates the relation between position uncertainty \( \Delta x \) and momentum uncertainty \( \Delta p \), and the minimum bound defined by \( \frac{\hbar}{2} \).

<p style="text-align: center;">
  <img src="./Uncertainty%20Principle/docs/Uncertainty_principle.png" alt="Uncertainty Principle Graph" style="width: 75%;">
</p>

- Link to Project: [Uncertainty Principle Graph](./Uncertainty%20Principle/docs/README.md)

---

## Licence

This project is licensed under the same terms as the BSc thesis it is derived from. Please refer to the thesis documentation for specific licensing details and any applicable restrictions.

## Contact

For questions or suggestions related specifically to this thesis, please contact:

- Name: Ricard Santiago Raigada García
- Email: <rraigadag@uoc.edu>
