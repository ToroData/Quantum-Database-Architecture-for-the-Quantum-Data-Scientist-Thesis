"""
Main script to calculate and plot the fist-order electrical suceptiility

Author: Ricard Santiago Raigada García
Date: 06/12/2024
Version: 0.0.1
"""
import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from src.calculations import calculate_susceptibility
from src.config import gamma, gamma_sg, delta_p, Omega_p, Omega_c_on, Omega_c_off
from plots.plot_generator import generate_plot, generate_imaginary_active_plot


def main() -> None:
    """
    Streamlit app for visualizing first-order electrical susceptibility with thesis content.
    """

    st.set_page_config(page_title="First Order Electrical Susceptibility Visualization", page_icon="🔬", layout="wide")
    st.markdown("<style> .block-container { max-width: 1200px; } </style>", unsafe_allow_html=True)

    st.title("Visualization of First Order Electrical Susceptibility")

    st.markdown(r"""This web is a follow-up work to a degree thesis. The purpose is to interactively show how the modification of different system parameters affects the transparency window generated in the context of Electromagnetically Induced Transparency (EIT). The reader is encouraged to explore changes in the system configuration to understand how it affects the transparency window.

Also, you can find the entire thesis and the citation method at 

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.14810946.svg)](https://doi.org/10.5281/zenodo.14810946). 

To cite the code, please use the following reference:  

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.14811156.svg)](https://doi.org/10.5281/zenodo.14811156).""")
    st.markdown(
        "<p style='font-size:0.85em; font-style:italic; color:gray;'>"
        "This project is licensed under the same terms as the BSc thesis it is derived from. "
        "Please refer to the thesis documentation for specific licensing details and any applicable restrictions."
        "</p>",
        unsafe_allow_html=True
    )
    st.markdown(r"""
    ## **1. Introduction**
    
Up to now, a three-level system in $\Lambda$ configuration with interaction with a probe and control field has been described. The couplings of the Rabi frequencies with the ground, metastable and excited states have been described. Solving the equations of the previous section to find analytically a unique solution is an intractable problem.

The description of the system is a complex problem that addresses a set of coupled partial differential equations (PDEs), known in the literature as Maxwell-Bloch equations and used in nonlinear optics (Saksida, 2005), (also see. S. Malinovsky & R. Berman, 2011, pp. 120–135) The equations describing the behaviour of bosonic quasiparticles include the propagation of the electromagnetic field and the time evolution of the coherences of the atomic populations. The variables of the equations are interdependent and highly coupled both in time and space, which makes the PDEs nonlinear. The dependence comes from multiple parameters such as the Rabi frequencies, the detuning and the decay rate. The resulting PDEs, assuming they could be solved analytically, would not have a closed solution space. On the other hand, the Hamiltonian of the system, when including decoherence, makes it non-Hermitian, so it is not orthogonal.
    """)


    st.markdown(r"""
    ## **2. Numerical Solution Approach**
    
For this reason, it is more appropriate to propose a numerical simulation based on the Lindblad equation""") 
    st.latex(r"""
    \frac{d p}{d t} = \frac{-i}{\hbar}[H_{int},\, \rho] + \sum_{i,j}\Gamma_{ij}\left (\sigma_{ij}\rho \sigma_{ji}^\dagger -\frac{1}{2}  \left\{ \sigma_{ji}^\dagger \sigma_{ij}, \rho \right\} \right ),
    """)
    st.markdown("""that describes the time evolution of the density matrix $\rho$ of the system. In the simulation, the first order electrical susceptibility $\chi^{(1)}$ obtained from the coherence $\rho_{ge}$ has been calculated. The probe field introduces a perturbation and $\rho_{ge}$ shows the response to it. The real part of $\chi^{(1)}$ represents the dispersion, while the imaginary part represents the absorption.

In the visualizations, the steady states are calculated for values of $\Delta_p$ and $\rho_{ge}$ is represented to graph the evolution of the system, both when the control is off; therefore, it is in an absorptive state, and when the control is on, and therefore, the medium is transparent in resonance. The parameters chosen in the tests arise indicatively from experiments previously presented, as Steck, 2001. It has been guaranteed that the parameters chosen in this thesis offer a viable configuration based on all the characteristics and requirements presented in the previous sections. Requirements like $\Delta_p\approx 0$ such that $\Omega_p \ll \Omega_c$. For this purpose, the cost function has been defined:
    """)

    st.latex(r"""
    \text{cost}(\Omega_p,\Omega_c,\Delta)
    =
    \langle e|\rho_{ss}(\Omega_p,\Omega_c,\Delta)|e\rangle
    \;+\;
    P(\Delta).
    """)

    st.markdown(r"""
    Function that minimizes the population in the excited state $\ket{e}$— $\langle e|\rho_{ss}|e\rangle$. And applies a penalty $P(\Delta)$ if $\Delta_{\text{min}}\leq\Delta\leq\Delta_{\text{max}}$ or if $\Delta$ exceeds $1000$—because there are no longer dynamic effects of interest. The simulation uses the `steadystate` function in QuTIP, the L-BFGS-B. The original paper was published in 1997, and titled as _Algorithm 778: L-BFGS-B: Fortran Subroutines for Large-Scale Bound-Constrained Optimization_. The _main purpose of algorithm L-BFGS-B is to minimize a nonlinear function of n variables_ (Zhu & Byrd, 1997,
p. 1). This method has been used to find the steady state of the Lindblad equation and for parameter optimization. This method is a restricted quasi-Newton optimization algorithm, available at `scipy.optimize.minimize`. Although the function is executed in Python, the calculation optimization is done in Fortran. This method is suitable because it allows the use of bound constraints, and is suitable for complex functions or those with many parameters. The calculation is based on using finite differences of the gradient from an approximation to the Hessian matrix.
    """)

    st.markdown(r"""
    ## **3. Results and Visualizations**
    
    The graph _Real and Imaginary Parts of First Order Electrical Susceptibility_, shows the real and imaginary parts of $\chi^{(1)}$ both with the control on and with the control off. It can be seen that when the control is on, the desired transparency window is created where the atomic medium becomes transparent. It can be seen in the orange curve around $0$ on the $x$-axis. To better appreciate the results, a second graph is provided showing only the transparency window, refer to the Figure _Imaginary Part of Susceptibility with Control ON_.
    """)


    st.sidebar.header("System parameters")
    gamma_val = st.sidebar.slider(r"$\gamma$ Excited state decay rate", 0.1, 2.0, gamma, step=0.1)
    gamma_sg_val = st.sidebar.slider(r"$\gamma_{sg}$ Metastable state decay rate", 0.0001, 0.01, gamma_sg, step=0.0001)
    Omega_p_val = st.sidebar.slider(r"$\Omega_P$ Rabi frequency of the probe field", 0.01, 0.5, Omega_p, step=0.01)
    Omega_c_on_val = st.sidebar.slider(r"$\Omega_{C,\,ON}$ Rabi frequency of control laser - ON", 0.0, 2.0, Omega_c_on, step=0.1)
    Omega_c_off_val = st.sidebar.slider(r"$\Omega_{C,\,OFF}$ Rabi frequency of control laser - OFF", 0.0, 1.0, Omega_c_off, step=0.1)

    delta_p_val = np.linspace(-3 * gamma_val, 3 * gamma_val, 1000)
    Re_chi1_on, Im_chi1_on, Re_chi1_off, Im_chi1_off = calculate_susceptibility(
        delta_p_val, gamma_val, gamma_sg_val, Omega_p_val, Omega_c_on_val, Omega_c_off_val
    )


    st.subheader("Real and Imaginary Parts of First Order Electrical Susceptibility")
    fig1 = generate_plot(delta_p_val, gamma_val, Re_chi1_on, Im_chi1_on, Re_chi1_off, Im_chi1_off)
    st.pyplot(fig1)

    st.subheader("Imaginary Part of Susceptibility with Control ON")
    fig2 = generate_imaginary_active_plot(delta_p_val, gamma_val, Im_chi1_on)
    st.pyplot(fig2)

    
    st.markdown("""
### References

- Malinovsky, V. S., & Berman, P. R. (2011). *Principles of Laser Spectroscopy and Quantum Optics.* Princeton University Press. [https://doi.org/10.1515/9781400837045-007](https://doi.org/10.1515/9781400837045-007)

- Saksida, P. (2005). *Maxwell-Bloch equations, C. Neumann system, and Kaluza-Klein theory* (tech. rep.).

- Steck, D. A. (2001). *Rubidium 87 D Line Data* (tech. rep.). [http://steck.us/alkalidata](http://steck.us/alkalidata)

- Zhu, C., & Byrd, R. H. (1997). *Algorithm 778: L-BFGS-B: Fortran Subroutines for Large-Scale Bound-Constrained Optimization.* (Tech. Rep.).  
""")

if __name__ == "__main__":
    main()
