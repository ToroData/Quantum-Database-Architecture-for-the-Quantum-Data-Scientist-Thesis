"""
Config script with parameter configuration of the system

Author: Ricard Santiago Raigada García
Date: 06/12/2024
Version: 0.0.1
"""
from typing import Any
import numpy as np

# Parámetros del sistema
gamma: float = 1.0
gamma_sg: float = 1e-3 * gamma
delta_p: Any = np.linspace(-3 * gamma, 3 * gamma, 1000)
Omega_p: float = 0.1 * gamma
Omega_c_on: float = 1.0 * gamma
Omega_c_off: float = 0.0 * gamma
