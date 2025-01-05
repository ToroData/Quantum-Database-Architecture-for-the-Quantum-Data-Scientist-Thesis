"""
Main script to calculate and plot the fist-order electrical suceptiility

Author: Ricard Santiago Raigada García
Date: 06/12/2024
Version: 0.0.1
"""
from src.calculations import calculate_susceptibility
from src.config import gamma, gamma_sg, delta_p, Omega_p, Omega_c_on, Omega_c_off
from plots.plot_generator import generate_plot, generate_imaginary_active_plot


def main() -> None:
    """
    Main function to calculate susceptibilities and generate plots.
    """
    Re_chi1_on, Im_chi1_on, Re_chi1_off, Im_chi1_off = calculate_susceptibility(
        delta_p, gamma, gamma_sg, Omega_p, Omega_c_on, Omega_c_off)
    generate_plot(
        delta_p,
        gamma,
        Re_chi1_on,
        Im_chi1_on,
        Re_chi1_off,
        Im_chi1_off)
    generate_imaginary_active_plot(delta_p, gamma, Im_chi1_on)


if __name__ == "__main__":
    main()
