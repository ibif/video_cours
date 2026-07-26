"""
scenes/Chimie_PetroleGazNaturels_05.py — Chapitre 5 « Pétrole et gaz
naturels » (1ereC, Chimie), scène 05.

§ 5. Le craquage : définition (rupture de grosses molécules sous chaleur
400-800°C + catalyseur), équation générale alcane lourd → alcane léger +
alcène, exemple résolu 1 (C₁₂H₂₆ → C₈H₁₈ + C₄H₈, vérification du bilan
en C et en H), intérêts (rendement en essence, matières premières pour
la pétrochimie). Source : 1ereC/Chimie.pdf, chapitre 5, page 49.
"""

import textwrap

from manim import (
    DOWN,
    LEFT,
    RIGHT,
    UP,
    WHITE,
    YELLOW,
    GREEN,
    FadeIn,
    FadeOut,
    MathTex,
    Text,
    VGroup,
    Write,
    config,
)

from shapes.base_scene import NotionScene
from shapes.boxes import corrige_box, definition_box, exercise_box, property_box, scene_title


def _wrap(text: str, width: int = 56) -> str:
    return "\n".join(textwrap.fill(line, width=width) for line in text.split("\n"))


def _fit(mobject, top_y):
    bas_visible = -config.frame_height / 2 + 0.25
    hauteur_dispo = top_y - bas_visible
    if mobject.height > hauteur_dispo:
        mobject.scale(hauteur_dispo / mobject.height, about_point=mobject.get_top())
    return mobject


def _bullets(items, font_size=22, color=WHITE, width=52):
    lines = VGroup(
        *[Text(f"• {_wrap(it, width=width)}", font_size=font_size, color=color) for it in items]
    )
    lines.arrange(DOWN, aligned_edge=LEFT, buff=0.22)
    return lines


class LeCraquage(NotionScene):
    def construct(self):
        titre = scene_title("5. Le craquage des hydrocarbures")
        titre.scale(0.6)
        titre.to_edge(UP)

        # --- Énoncé : définition du craquage -------------------------------------
        definition = definition_box(
            Text(
                _wrap(
                    "Le craquage est une réaction chimique qui casse de "
                    "grosses molécules d'alcanes en molécules plus "
                    "petites, sous l'effet de la chaleur (400 à 800°C), "
                    "en présence ou non d'un catalyseur.",
                    width=48,
                ),
                font_size=23,
            ),
        )
        definition.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Le craquage est une réaction chimique qui casse de "
                "grosses molécules d'alcanes en molécules plus petites, "
                "sous l'effet de la chaleur, entre quatre cents et huit "
                "cents degrés Celsius, en présence ou non d'un "
                "catalyseur. Contrairement à la distillation, cette fois "
                "il s'agit bien d'une transformation chimique."
            )
        ) as tracker:
            self.play(Write(titre))
            self.play(FadeIn(definition))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(definition))

        # --- Raisonnement : équation générale du craquage ------------------------
        entete_eq = Text("Équation générale du craquage", font_size=24, color=YELLOW, weight="BOLD")
        entete_eq.next_to(titre, DOWN, buff=0.4)

        equation_generale = property_box(
            MathTex(
                r"C_nH_{2n+2} \;\rightarrow\; C_pH_{2p+2} \;+\; C_qH_{2q}",
                font_size=30,
                color="#1A1A1A",
            ),
        )
        equation_generale.next_to(entete_eq, DOWN, buff=0.45)

        condition = MathTex(r"\text{avec } n = p + q", font_size=26, color=WHITE)
        condition.next_to(equation_generale, DOWN, buff=0.35)

        groupe_eq = VGroup(entete_eq, equation_generale, condition)

        with self.voiceover(
            text=(
                "L'équation générale du craquage s'écrit ainsi : un "
                "alcane lourd, C indice n H indice deux n plus deux, "
                "se transforme en un alcane plus léger, C indice p H "
                "indice deux p plus deux, et un alcène, C indice q H "
                "indice deux q, avec n égal à p plus q : le nombre total "
                "d'atomes de carbone se conserve."
            )
        ) as tracker:
            self.play(FadeIn(entete_eq))
            self.play(Write(equation_generale))
            self.play(Write(condition))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(groupe_eq))

        # --- Exemple traité : C12H26 → C8H18 + C4H8 ------------------------------
        enonce = exercise_box(
            Text(
                _wrap(
                    "Le dodécane C₁₂H₂₆ est craqué en octane C₈H₁₈ et un "
                    "alcène. Écrire et vérifier cette équation.",
                    width=46,
                ),
                font_size=22,
            ),
            box_width=10.5,
        )
        enonce.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Traitons un exemple : le dodécane, C douze H vingt-six, "
                "est craqué en octane, C huit H dix-huit, et un alcène. "
                "Écrivons et vérifions cette équation."
            )
        ) as tracker:
            self.play(FadeIn(enonce))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(enonce))

        equation_ex = MathTex(
            r"C_{12}H_{26} \;\rightarrow\; C_8H_{18} \;+\; C_4H_8",
            font_size=32,
            color=WHITE,
        )
        equation_ex.next_to(titre, DOWN, buff=0.6)

        with self.voiceover(
            text=(
                "Puisque n égale douze et p égale huit, q vaut quatre : "
                "l'alcène formé est donc C-4-H-8. L'équation s'écrit : "
                "C douze H vingt-six donne C huit H dix-huit plus C "
                "quatre H huit."
            )
        ) as tracker:
            self.play(Write(equation_ex))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(equation_ex))

        verification = corrige_box(
            VGroup(
                Text("Bilan en carbone : 12 = 8 + 4 ✓", font_size=24),
                Text("Bilan en hydrogène : 26 = 18 + 8 ✓", font_size=24),
            ).arrange(DOWN, aligned_edge=LEFT, buff=0.3),
            box_width=8.5,
        )
        verification.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Vérifions les bilans. En carbone : douze est bien égal "
                "à huit plus quatre. En hydrogène : vingt-six est bien "
                "égal à dix-huit plus huit. L'équation est équilibrée."
            )
        ) as tracker:
            self.play(FadeIn(verification))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(verification))

        # --- À retenir : intérêts du craquage ------------------------------------
        interets = property_box(
            _bullets(
                [
                    "Augmenter le rendement en essence, la fraction la plus demandée",
                    "Fournir les alcènes, matières premières de la pétrochimie (plastiques, etc.)",
                ],
                font_size=21,
                width=46,
            ),
            box_width=10.5,
        )
        interets.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Le craquage présente deux intérêts majeurs : il permet "
                "d'augmenter le rendement en essence, la fraction la plus "
                "demandée par les automobilistes ; et il fournit des "
                "alcènes, matières premières indispensables à la "
                "pétrochimie, pour fabriquer par exemple des matières "
                "plastiques."
            )
        ) as tracker:
            self.play(FadeIn(interets))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(interets), FadeOut(titre))
