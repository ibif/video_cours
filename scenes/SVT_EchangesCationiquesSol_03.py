"""
scenes/SVT_EchangesCationiquesSol_03.py — Chapitre 9 (1ereC, SVT), scène 03.

Le complexe argilo-humique (CAH) : définition (association argile +
humus), rôle de réservoir d'éléments nutritifs, schéma du CAH chargé
négativement retenant les cations de la solution du sol, et définition de
la solution du sol. Source : 1ereC/SVT.pdf, pages 97-98.
"""

import math
import textwrap

from manim import (
    DOWN,
    LEFT,
    ORANGE,
    RED,
    RIGHT,
    UP,
    WHITE,
    YELLOW,
    Arrow,
    Circle,
    FadeIn,
    FadeOut,
    Text,
    VGroup,
    Write,
)

from shapes.base_scene import NotionScene
from shapes.boxes import definition_box, property_box, scene_title


def _wrap(text: str, width: int = 56) -> str:
    return "\n".join(textwrap.fill(line, width=width) for line in text.split("\n"))


def _bullets(items, font_size=24, color=WHITE, width=54):
    lines = VGroup(
        *[Text(f"• {_wrap(it, width=width)}", font_size=font_size, color=color) for it in items]
    )
    lines.arrange(DOWN, aligned_edge=LEFT, buff=0.22)
    return lines


def _point_on_circle(center, radius, angle_deg):
    angle_rad = math.radians(angle_deg)
    return center + radius * (math.cos(angle_rad) * RIGHT + math.sin(angle_rad) * UP)


class ComplexeArgiloHumique(NotionScene):
    def construct(self):
        titre = scene_title("9.2 — Le complexe argilo-humique (CAH)")
        titre.scale(0.66)
        titre.to_edge(UP)

        # --- Énoncé : argiles et humus ne restent pas séparés --------------
        intro = Text(
            _wrap(
                "Dans le sol, les argiles (minérales) et l'humus "
                "(organique) ne restent pas séparés : ils s'associent "
                "étroitement pour former un ensemble stable, le complexe "
                "argilo-humique.",
                width=56,
            ),
            font_size=25,
            color=WHITE,
        )
        intro.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Dans le sol, les argiles, d'origine minérale, et "
                "l'humus, d'origine organique, ne restent pas séparés : "
                "ils s'associent étroitement pour former un ensemble "
                "stable, appelé le complexe argilo-humique, ou CAH."
            )
        ) as tracker:
            self.play(Write(titre))
            self.play(FadeIn(intro))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(intro))

        # --- Raisonnement : définition + schéma du CAH ---------------------
        def_cah = definition_box(
            Text(
                _wrap(
                    "Le complexe argilo-humique (CAH) est l'ensemble "
                    "formé par l'association intime des argiles et de "
                    "l'humus dans le sol. Il porte des charges négatives "
                    "à sa surface, capables d'attirer et de retenir les "
                    "cations de la solution du sol.",
                    width=54,
                ),
                font_size=22,
            ),
            box_width=11.8,
        )
        def_cah.next_to(titre, DOWN, buff=0.45)

        with self.voiceover(
            text=(
                "Le complexe argilo-humique est donc l'ensemble formé par "
                "l'association intime des argiles et de l'humus dans le "
                "sol. Comme les deux constituants portent des charges "
                "négatives à leur surface, le complexe tout entier attire "
                "et retient les cations de la solution du sol."
            )
        ) as tracker:
            self.play(FadeIn(def_cah))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(def_cah))

        # Schéma : micelle du CAH chargée négativement, cations attirés
        micelle = Circle(radius=1.0, color=ORANGE, fill_color=ORANGE, fill_opacity=0.3, stroke_width=3)
        micelle_label = Text("CAH", font_size=20, color=WHITE, weight="BOLD").move_to(micelle.get_center())

        charge_angles = [30, 90, 150, 210, 270, 330]
        charges = VGroup()
        for angle in charge_angles:
            point = _point_on_circle(micelle.get_center(), 1.0, angle)
            charge = Text("-", font_size=26, color=RED, weight="BOLD")
            charge.move_to(point)
            charges.add(charge)

        cation_data = [
            ("Ca2+", 30, 2.3),
            ("K+", 90, 2.3),
            ("Mg2+", 150, 2.3),
            ("H+", 210, 2.3),
            ("NH4+", 270, 2.3),
            ("Na+", 330, 2.3),
        ]
        cations = VGroup()
        fleches = VGroup()
        for label, angle, dist in cation_data:
            pos_ext = _point_on_circle(micelle.get_center(), dist, angle)
            pos_bord = _point_on_circle(micelle.get_center(), 1.05, angle)
            txt = Text(label, font_size=18, color=YELLOW).move_to(pos_ext)
            fleche = Arrow(pos_ext, pos_bord, buff=0.12, color=YELLOW, stroke_width=2.5, max_tip_length_to_length_ratio=0.25)
            cations.add(txt)
            fleches.add(fleche)

        schema = VGroup(micelle, micelle_label, charges, cations, fleches)
        schema.scale(0.95)
        schema.next_to(titre, DOWN, buff=0.6)

        with self.voiceover(
            text=(
                "Voici une représentation du complexe argilo-humique. Sa "
                "surface, criblée de charges négatives, attire les "
                "cations qui circulent dans la solution du sol : calcium, "
                "potassium, magnésium, hydrogène, ammonium, sodium. Ces "
                "cations viennent se fixer autour du complexe, retenus "
                "par l'attraction électrique entre charges opposées."
            )
        ) as tracker:
            self.play(FadeIn(micelle), FadeIn(micelle_label), FadeIn(charges))
            self.play(FadeIn(cations), FadeIn(fleches))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(schema))

        # --- À retenir : rôle de réservoir -----------------------------------
        role = property_box(
            Text(
                _wrap(
                    "Le complexe argilo-humique joue un rôle de "
                    "réservoir d'éléments nutritifs : il retient les "
                    "cations (Ca2+, Mg2+, K+, Na+, H+, NH4+) et les met à "
                    "la disposition des racines des plantes.",
                    width=54,
                ),
                font_size=22,
            ),
            box_width=11.8,
        )
        role.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Retenons le rôle essentiel du complexe argilo-humique : "
                "c'est un réservoir d'éléments nutritifs. Il retient les "
                "cations, calcium, magnésium, potassium, sodium, "
                "hydrogène, ammonium, et les met à la disposition des "
                "racines des plantes, au fur et à mesure de leurs "
                "besoins."
            )
        ) as tracker:
            self.play(FadeIn(role))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(role))

        # --- Définition de la solution du sol --------------------------------
        def_solution = definition_box(
            Text(
                _wrap(
                    "La solution du sol est l'eau du sol contenant des "
                    "ions dissous. C'est à partir d'elle que les racines "
                    "des plantes prélèvent leurs éléments nutritifs.",
                    width=54,
                ),
                font_size=23,
            ),
            box_width=11.5,
        )
        def_solution.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Enfin, précisons ce qu'est la solution du sol : c'est "
                "l'eau du sol contenant des ions dissous. C'est à partir "
                "de cette solution, et uniquement à partir d'elle, que "
                "les racines des plantes prélèvent leurs éléments "
                "nutritifs. Le complexe argilo-humique et la solution du "
                "sol fonctionnent donc comme deux compartiments "
                "communicants."
            )
        ) as tracker:
            self.play(FadeIn(def_solution))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(titre), FadeOut(def_solution))
