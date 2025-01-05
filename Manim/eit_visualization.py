"""
Script to generate a visual representation of the EIT with a semiclassical approximation

Author: Ricard Santiago Raigada García
Date: 28/10/2024
Version: 1.0.0
"""
from manim import *


class EITSetup(Scene):
    def construct(self):
        title = Text(
            "Electromagnetically Induced Transparency (EIT)",
            font_size=36)
        self.play(Write(title))
        self.wait(2)
        self.play(FadeOut(title))

        # Wavefunction formula
        custom_template = TexTemplate.from_file("custom_template.tex")
        wavefunction_formula = MathTex(
            r"\tilde{\Psi} = c_1(t)e^{-i \omega_{L,1}t} \ket{g} + "
            r"c_2(t)e^{-i \omega_{L,2}t} \ket{s} + c_3(t)\ket{e}",
            tex_template=custom_template
        )
        wavefunction_formula.scale(0.8).to_corner(UP + LEFT)
        self.play(Write(wavefunction_formula))

        # Velocity Group ($V_g$)
        velocity_group_label = Tex(r"Velocity Group ($V_g$)", font_size=24)
        velocity_group = Circle(
            radius=1,
            color=YELLOW,
            fill_opacity=0.3).shift(
            LEFT * 3 + DOWN * 2)
        velocity_group_label.next_to(velocity_group, DOWN)
        photons = VGroup(*[
            Dot(point=[x, y, 0], color=GOLD)
            for x, y in [
                (-0.3, 0), (0.3, 0), (0, 0.4), (0, -0.4),
                (-0.7, 0.3), (0.7, 0.3), (0.3, -0.7), (-0.3, -0.7),
                (-0.4, 0.6), (0.4, 0.6), (-0.6, -0.4), (0.6, -0.4)
            ]
        ])
        photons.move_to(velocity_group.get_center())

        # Rb Vapor Cell
        rubidium_cell = Rectangle(
            height=1.5,
            width=3,
            color=BLUE,
            fill_opacity=1).shift(
            UP * 1.5)
        rubidium_label = Text(
            "Rubidium Vapor Cell",
            font_size=24).next_to(
            rubidium_cell,
            UP)

        # Probe/ Control laser
        control_laser = Arrow(
            start=RIGHT * 4 + DOWN * 1.5,
            end=rubidium_cell.get_right(),
            color=GREY,
            buff=0.1)
        probe_laser = Arrow(
            start=LEFT * 4 + DOWN * 1.5,
            end=rubidium_cell.get_left(),
            color=GREY,
            buff=0.11)
        control_label = Tex(
            r"Control Laser $\Omega_c$: $| s \rangle$",
            font_size=24).next_to(
            control_laser,
            RIGHT)
        probe_label = Tex(
            r"Probe Laser $\Omega_p$: $| g \rangle$",
            font_size=24).next_to(
            probe_laser,
            LEFT)

        # Scene
        self.play(
            Create(velocity_group),
            Write(velocity_group_label),
            FadeIn(photons))
        self.play(Create(rubidium_cell), Write(rubidium_label))
        self.play(GrowArrow(control_laser), Write(control_label))
        self.play(GrowArrow(probe_laser), Write(probe_label))
        self.play(FadeOut(wavefunction_formula))

        # Hamiltonian Formula
        hamiltonian_formula = MathTex(
            r"\tilde{H} = \frac{\hbar}{2}\begin{pmatrix} 0 & \Omega_g & \Omega_s \\ \Omega_g & 2 \Delta_g & 0 \\ \Omega_s & 0 & 2 \Delta_s \end{pmatrix}")
        hamiltonian_formula.scale(0.8)
        hamiltonian_formula.to_corner(UP + LEFT)
        self.play(Write(hamiltonian_formula))

        # Translation
        moving_velocity_group = velocity_group.copy().move_to(rubidium_cell.get_center())
        moving_photons = photons.copy().move_to(rubidium_cell.get_center())
        self.play(
            control_laser.animate.set_color(YELLOW),
            rubidium_cell.animate.set_fill(opacity=0.3)
        )
        self.play(
            ReplacementTransform(photons, moving_photons),
            ReplacementTransform(velocity_group, moving_velocity_group),
            FadeOut(velocity_group_label),
            probe_laser.animate.set_color(YELLOW),
            run_time=2)
        self.play(FadeOut(hamiltonian_formula))

        # Rabi frequencies
        rabi_formula = MathTex(
            r"\Omega_i = \frac{- \langle g_i | d_i \cdot E_i | e \rangle}{\hbar}")
        rabi_formula.scale(0.8).next_to(rubidium_cell, DOWN * 1.5)
        self.play(Write(rabi_formula))
        self.wait(2)

        self.play(
            control_laser.animate.set_color(GREY),
            rubidium_cell.animate.set_fill(opacity=1),
            FadeOut(moving_photons),
            FadeOut(moving_velocity_group)
        )
        self.wait(3)

        self.play(
            control_laser.animate.set_color(YELLOW),
            rubidium_cell.animate.set_fill(opacity=0.3),
            probe_laser.animate.set_color(YELLOW),
            FadeIn(moving_photons),
            FadeIn(moving_velocity_group)
        )
        self.play(
            moving_photons.animate.move_to(
                LEFT * 3 + DOWN * 2
            ),
            moving_velocity_group.animate.move_to(
                LEFT * 3 + DOWN * 2
            )
        )
        self.play(
            control_laser.animate.set_color(GREY),
            rubidium_cell.animate.set_fill(opacity=1),
            probe_laser.animate.set_color(GREY),
        )
        self.wait(2)
