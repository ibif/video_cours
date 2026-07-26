"""
scenes/Maths_SuitesNumeriques_01.py — Chapitre 15 « Suites numériques »
(1ereC, Maths), scène 01.

Définition d'une suite numérique, notations, vocabulaire des termes
consécutifs. Piège : u(n+1) ne veut pas dire u(n)+1 ; une suite n'est pas
une courbe continue mais un nuage de points isolés.
Source : 1ereC/Maths.pdf, chapitre 15, pages 176-188.
"""

import textwrap

from manim import (
    DOWN,
    LEFT,
    RIGHT,
    UP,
    WHITE,
    YELLOW,
    Axes,
    Dot,
    FadeIn,
    FadeOut,
    MathTex,
    Text,
    VGroup,
    Write,
)

from shapes.base_scene import NotionScene
from shapes.boxes import definition_box, essentiel_box, scene_title, warning_box


def _wrap(text: str, width: int = 58) -> str:
    return "\n".join(textwrap.fill(line, width=width) for line in text.split("\n"))


class DefinitionSuiteNumerique(NotionScene):
    def construct(self):
        titre = scene_title("Suites numériques — définition et notations")
        titre.scale(0.48)
        titre.to_edge(UP)
        self.play(Write(titre))

        # --- Énoncé : définition ------------------------------------------------
        definition = definition_box(
            VGroup(
                Text(
                    _wrap(
                        "Une suite numérique est une fonction définie sur "
                        "ℕ (ou une partie de ℕ) et à valeurs dans ℝ.",
                        width=52,
                    ),
                    font_size=24,
                ),
                MathTex(
                    r"u : n \longmapsto u(n), \text{ noté } u_n",
                    font_size=30,
                ),
            ).arrange(DOWN, buff=0.3),
            box_width=10.5,
        )
        definition.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Une suite numérique est une fonction définie sur l'ensemble "
                "des entiers naturels ℕ, ou sur une partie de ℕ, et à "
                "valeurs dans ℝ. À chaque entier n, elle associe un réel, "
                "que l'on note u indice n, plutôt que u de n comme pour une "
                "fonction ordinaire."
            )
        ) as tracker:
            self.play(FadeIn(definition))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(definition))

        # --- Vocabulaire : termes consécutifs ------------------------------------
        vocabulaire = definition_box(
            VGroup(
                Text(
                    "u0 est le premier terme (terme initial).",
                    font_size=23,
                ),
                Text(
                    "un est le terme général, de rang (ou d'indice) n.",
                    font_size=23,
                ),
                MathTex(
                    r"u_{n-1}, \ u_n, \ u_{n+1} \ \text{ sont trois termes consécutifs.}",
                    font_size=27,
                ),
            ).arrange(DOWN, buff=0.25),
            box_width=10.8,
        )
        vocabulaire.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Vocabulaire : u zéro est le premier terme de la suite, "
                "aussi appelé terme initial. u indice n est le terme "
                "général, de rang n. Et u indice n moins un, u indice n, u "
                "indice n plus un désignent trois termes consécutifs : "
                "chacun suit immédiatement le précédent dans la suite."
            )
        ) as tracker:
            self.play(FadeIn(vocabulaire))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(vocabulaire))

        # --- Animation du raisonnement : nuage de points isolés -------------------
        axes = Axes(
            x_range=[-0.5, 6, 1],
            y_range=[-0.5, 4, 1],
            x_length=6.5,
            y_length=3.8,
            axis_config={"color": WHITE, "font_size": 16},
        )
        axes.move_to(DOWN * 0.3)
        points = VGroup(
            *[
                Dot(axes.c2p(n, 0.5 + 0.35 * n + 0.05 * n * n), color=YELLOW, radius=0.07)
                for n in range(6)
            ]
        )
        label = Text("Une suite : des points isolés, jamais reliés", font_size=20)
        label.next_to(axes, DOWN, buff=0.25)
        figure = VGroup(axes, points, label)

        with self.voiceover(
            text=(
                "Contrairement à une fonction de la variable réelle, une "
                "suite ne se représente pas par une courbe continue : on "
                "obtient un nuage de points isolés, un point par entier n, "
                "et rien entre deux points consécutifs — puisque la suite "
                "n'est tout simplement pas définie pour les valeurs non "
                "entières."
            )
        ) as tracker:
            self.play(FadeIn(figure))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(figure))

        # --- À retenir -------------------------------------------------------------
        retenir = essentiel_box(
            Text(
                _wrap(
                    "Une suite (un) est une fonction de ℕ dans ℝ. u0, u1, "
                    "u2... sont ses termes. un désigne le terme général, de "
                    "rang n. Représentation graphique : un nuage de points "
                    "isolés (n ; un), jamais une courbe continue.",
                    width=58,
                ),
                font_size=22,
            ),
            box_width=11.3,
        )
        retenir.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "À retenir : une suite, notée u indice n ou entre "
                "parenthèses u indice n, est une fonction de ℕ dans ℝ. Ses "
                "images successives u zéro, u un, u deux, et ainsi de "
                "suite, sont ses termes. Sa représentation graphique est "
                "toujours un nuage de points isolés, jamais une courbe "
                "continue."
            )
        ) as tracker:
            self.play(FadeIn(retenir))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(retenir))

        # --- Piège à éviter ----------------------------------------------------
        piege = warning_box(
            Text(
                _wrap(
                    "u(n+1) ne signifie pas « un + 1 » ! u(n+1) est le "
                    "terme de rang n+1, tandis que un+1 est le terme de "
                    "rang n auquel on ajoute 1. Ces deux quantités sont en "
                    "général totalement différentes.",
                    width=56,
                ),
                font_size=22,
            ),
            box_width=11.2,
        )
        piege.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Piège classique à éviter absolument : le terme u, dont "
                "l'indice est n plus un, ne signifie pas le terme u "
                "d'indice n, auquel on ajouterait un. Dans le premier cas, "
                "l'addition porte sur le rang, avant de calculer le terme ; "
                "dans le second, elle porte sur la valeur du terme, après "
                "coup. Ces deux quantités sont, en général, complètement "
                "différentes."
            )
        ) as tracker:
            self.play(FadeIn(piege))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(piege), FadeOut(titre))
