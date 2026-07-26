"""
scenes/Chimie_AlcenesAlcynes_08.py — Chapitre 3 (1ereC, Chimie), scène 08.

Combustion des alcènes et des alcynes : équations-bilans générales,
exemples de l'éthylène et de l'acétylène, chalumeau oxyacétylénique
(≈3000°C), applications soudure/découpe de métaux (garages et SIR
d'Abidjan/Dabou). Source : 1ereC/Chimie.pdf, chapitre 3, page 31.
"""

import textwrap

from manim import (
    DOWN,
    LEFT,
    RIGHT,
    UP,
    WHITE,
    YELLOW,
    ORANGE,
    RED,
    FadeIn,
    FadeOut,
    MathTex,
    Text,
    VGroup,
    Write,
    config,
)

from shapes.base_scene import NotionScene
from shapes.boxes import property_box, scene_title


def _wrap(text: str, width: int = 56) -> str:
    return "\n".join(textwrap.fill(line, width=width) for line in text.split("\n"))


def _fit(mobject, top_y):
    bas_visible = -config.frame_height / 2 + 0.25
    hauteur_dispo = top_y - bas_visible
    if mobject.height > hauteur_dispo:
        mobject.scale(hauteur_dispo / mobject.height, about_point=mobject.get_top())
    return mobject


class CombustionAlcenesAlcynes(NotionScene):
    def construct(self):
        titre = scene_title("8. Combustion des alcènes et des alcynes")
        titre.scale(0.5)
        titre.to_edge(UP)

        # --- Énoncé : la combustion, réaction commune à tous les hydrocarbures ---
        intro = Text(
            _wrap(
                "Comme tout hydrocarbure, un alcène ou un alcyne brûle "
                "dans le dioxygène. Cette combustion, complète en excès "
                "de dioxygène, produit du dioxyde de carbone et de l'eau.",
                width=54,
            ),
            font_size=24,
            color=WHITE,
        )
        intro.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Comme tout hydrocarbure, un alcène ou un alcyne brûle en "
                "présence de dioxygène. Lorsque le dioxygène est en "
                "excès, la combustion est complète et produit du dioxyde "
                "de carbone et de l'eau."
            )
        ) as tracker:
            self.play(Write(titre))
            self.play(FadeIn(intro))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(intro))

        # --- Animation du raisonnement : équations-bilans générales -------------
        propriete = property_box(
            VGroup(
                Text("Combustion complète d'un alcène :", font_size=22, weight="BOLD"),
                MathTex(
                    r"C_nH_{2n} + \dfrac{3n}{2}O_2 \longrightarrow nCO_2 + nH_2O",
                    font_size=28,
                ),
                Text("Combustion complète d'un alcyne :", font_size=22, weight="BOLD"),
                MathTex(
                    r"C_nH_{2n-2} + \dfrac{3n-1}{2}O_2 \longrightarrow nCO_2 + (n-1)H_2O",
                    font_size=28,
                ),
            ).arrange(DOWN, buff=0.35),
            box_width=11.5,
        )
        propriete.next_to(titre, DOWN, buff=0.35)
        _fit(propriete, titre.get_bottom()[1] - 0.35)

        with self.voiceover(
            text=(
                "L'équation-bilan générale de la combustion complète "
                "d'un alcène, C indice n H indice deux n, s'écrit avec le "
                "dioxygène pour donner n fois C O deux et n fois H deux "
                "O. Pour un alcyne, C indice n H indice deux n moins "
                "deux, l'équation est légèrement différente, puisqu'il y "
                "a deux hydrogènes de moins par molécule."
            )
        ) as tracker:
            self.play(FadeIn(propriete))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(propriete))

        # --- Exemple traité : éthylène et acétylène -------------------------------
        entete = Text("Deux exemples chiffrés", font_size=24, color=YELLOW, weight="BOLD")
        entete.next_to(titre, DOWN, buff=0.35)

        exemples = VGroup(
            MathTex(r"C_2H_4 + 3O_2 \longrightarrow 2CO_2 + 2H_2O", font_size=28),
            MathTex(r"2C_2H_2 + 5O_2 \longrightarrow 4CO_2 + 2H_2O", font_size=28),
        ).arrange(DOWN, buff=0.4)
        exemples.next_to(entete, DOWN, buff=0.45)

        groupe = VGroup(entete, exemples)

        with self.voiceover(
            text=(
                "Pour l'éthylène, l'équation ajustée est : C deux H "
                "quatre plus trois O deux donne deux C O deux plus deux "
                "H deux O. Pour l'acétylène, il faut ajuster avec des "
                "nombres entiers : deux C deux H deux plus cinq O deux "
                "donnent quatre C O deux plus deux H deux O."
            )
        ) as tracker:
            self.play(FadeIn(entete))
            self.play(FadeIn(exemples))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(groupe))

        # --- À retenir : le chalumeau oxyacétylénique ------------------------------
        entete2 = Text("Application : le chalumeau oxyacétylénique", font_size=22, color=YELLOW, weight="BOLD")
        entete2.next_to(titre, DOWN, buff=0.35)

        flamme = VGroup(
            Text("Combustion de C₂H₂ dans O₂ pur", font_size=22, color=WHITE),
            Text("→ flamme atteignant ≈ 3000°C", font_size=24, color=ORANGE, weight="BOLD"),
            Text(
                _wrap(
                    "Utilisé pour la soudure et la découpe des métaux "
                    "(garages, ateliers métallurgiques, SIR d'Abidjan et "
                    "de Dabou).",
                    width=44,
                ),
                font_size=20,
                color=WHITE,
            ),
        ).arrange(DOWN, buff=0.35)
        flamme.next_to(entete2, DOWN, buff=0.45)
        _fit(flamme, entete2.get_bottom()[1] - 0.45)

        groupe2 = VGroup(entete2, flamme)

        with self.voiceover(
            text=(
                "La combustion de l'acétylène dans du dioxygène pur, et "
                "non dans l'air, libère énormément d'énergie : la flamme "
                "obtenue atteint environ trois mille degrés Celsius. "
                "C'est le principe du chalumeau oxyacétylénique, utilisé "
                "pour souder et découper des métaux, notamment dans les "
                "garages automobiles et les ateliers métallurgiques, "
                "comme ceux de la SIR à Abidjan et à Dabou."
            )
        ) as tracker:
            self.play(FadeIn(entete2))
            self.play(FadeIn(flamme))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(groupe2))

        # --- Pièges à éviter -------------------------------------------------------
        piege = Text(
            _wrap(
                "Piège fréquent : oublier d'ajuster les nombres "
                "stœchiométriques devant O₂ (souvent non entiers, comme "
                "3n/2) — il faut alors multiplier toute l'équation par 2 "
                "pour obtenir des nombres entiers, comme dans l'exemple "
                "de l'acétylène.",
                width=52,
            ),
            font_size=22,
            color=WHITE,
        )
        piege.next_to(titre, DOWN, buff=0.4)
        _fit(piege, titre.get_bottom()[1] - 0.4)

        with self.voiceover(
            text=(
                "Attention à un piège classique lors de l'ajustement : "
                "le nombre stœchiométrique devant le dioxygène n'est pas "
                "toujours entier, comme trois n sur deux. Dans ce cas, il "
                "faut multiplier toute l'équation par deux pour obtenir "
                "des nombres entiers, exactement comme nous l'avons fait "
                "pour l'acétylène."
            )
        ) as tracker:
            self.play(FadeIn(piege))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(piege), FadeOut(titre))
