"""
This module computes the calculation of the real and imaginary parts of
the first-order electrical susceptibility

Author: Ricard Santiago Raigada García
Date: 06/12/2024
Version: 0.0.1
"""
from typing import Tuple, List
import numpy as np
from qutip import steadystate, basis


def calculate_susceptibility(
    delta_p: np.ndarray,
    gamma: float,
    gamma_sg: float,
    Omega_p: float,
    Omega_c_on: float,
    Omega_c_off: float
) -> Tuple[List[float], List[float], List[float], List[float]]:
    """
    Computes the real and imaginary part of the first-order susceptibility

    Args:
        delta_p (numpy.ndarray): Single-photon detunings
        gamma (float): Decay rate of the excited state
        gamma_sg (float): Decay rate of the metastable state
        Omega_p (float): Rabi frequency of the probe field
        Omega_c_on (float): Rabi frequency of the control laser (ON state)
        Omega_c_off (float): Rabi frequency of the control laser (OFF state)

    Returns:
        Tuple[List[float], List[float], List[float], List[float]]:
            Re_chi1_on: Real part of susceptibility (Control ON).
            Im_chi1_on: Imaginary part of susceptibility (Control ON).
            Re_chi1_off: Real part of susceptibility (Control OFF).
            Im_chi1_off: Imaginary part of susceptibility (Control OFF).
    """
    Re_chi1_on, Im_chi1_on = [], []
    Re_chi1_off, Im_chi1_off = [], []

    # States of the Lambda system
    g = basis(3, 0)
    e = basis(3, 1)
    s = basis(3, 2)

    proj_g = g * g.dag()
    proj_e = e * e.dag()
    proj_s = s * s.dag()
    sigma_ge = g * e.dag()
    sigma_eg = e * g.dag()
    sigma_se = s * e.dag()
    sigma_es = e * s.dag()
    sigma_gs = g * s.dag()
    sigma_sg = s * g.dag()

    # Spontaneous decay
    c_ops = [
        np.sqrt(gamma) * sigma_ge,
        np.sqrt(gamma_sg) * sigma_gs
    ]

    # Iterate over detunings for control ON
    for dp in delta_p:
        H_on = (
            -dp * proj_e
            + (dp - 0.0) * proj_s  # Two-photon resonance
            + Omega_p * (sigma_eg + sigma_ge)
            + Omega_c_on * (sigma_es + sigma_se)
        )
        # Steady state
        rho_ss_on = steadystate(H_on, c_ops)
        rho_ge_on = rho_ss_on.matrix_element(g.dag(), e)
        Re_chi1_on.append(np.real(rho_ge_on))
        Im_chi1_on.append(np.imag(rho_ge_on))

    # Detunings for control OFF
    for dp in delta_p:
        H_off = (
            -dp * proj_e
            + (dp - 0.0) * proj_s
            + Omega_p * (sigma_eg + sigma_ge)
        )
        rho_ss_off = steadystate(H_off, c_ops)
        rho_ge_off = rho_ss_off.matrix_element(g.dag(), e)
        Re_chi1_off.append(np.real(rho_ge_off))
        Im_chi1_off.append(np.imag(rho_ge_off))
    return Re_chi1_on, Im_chi1_on, Re_chi1_off, Im_chi1_off
