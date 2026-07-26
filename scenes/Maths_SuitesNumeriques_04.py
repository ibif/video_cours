"""
scenes/Maths_SuitesNumeriques_04.py — Chapitre 15 « Suites numériques »
(1ereC, Maths), scène 04.

Sens de variation d'une suite : définitions et les trois méthodes (signe de
un+1 - un, quotient un+1/un si termes strictement positifs, étude de la
fonction associée si un = f(n)). Exemples résolus 3 et 4.
Source : 1ereC/Maths.pdf, chapitre 15, pages 176-188.
"""

import textwrap

from manim import DOWN, UP, FadeIn, FadeOut, MathTex, Text, VGroup, Write, YELLOW

from shapes.base_scene import NotionScene
from shapes.boxes import definition_box, essentiel_box, example_box, scene_title, theorem_box, warning_box


def _wrap(text: str, width: int = 58) -> str:
    return "\n".join(textwrap.fill(line, width=width) for line in text.split("\n"))


class SensVariationSuite(NotionScene):
    def construct(self):
        titre = scene_title("Sens de variation d'une suite — trois méthodes")
        titre.scale(0.46)
        titre.to_edge(UP)
        self.play(Write(titre))

        # --- Énoncé : définitions -------------------------------------------------
        definitions = definition_box(
            VGroup(
                Text("(un) est croissante si, pour tout n : un+1 ≥ un", font_size=21),
                Text("(un) est décroissante si, pour tout n : un+1 ≤ un", font_size=21),
                Text("(un) est constante si, pour tout n : un+1 = un", font_size=21),
                Text("(un) est monotone si elle est croissante ou décroissante", font_size=21),
            ).arrange(DOWN, buff=0.2),
            box_width=10.8,
        )
        definitions.next_to(titre, DOWN, buff=0.35)

        with self.voiceover(
            text=(
                "Définitions : une suite u indice n est croissante si, "
                "pour tout entier n, u indice n plus un est supérieur ou "
                "égal à u indice n. Elle est décroissante dans le cas "
                "inverse, et constante si deux termes consécutifs "
                "quelconques sont toujours égaux. On dit qu'elle est "
                "monotone si elle est croissante, ou si elle est "
                "décroissante, sur tout son ensemble de définition."
            )
        ) as tracker:
            self.play(FadeIn(definitions))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(definitions))

        # --- Théorème : trois méthodes ---------------------------------------------
        methodes = theorem_box(
            VGroup(
                Text("Trois méthodes pour étudier le sens de variation :", font_size=22, weight="BOLD"),
                MathTex(r"1)\ \text{signe de } u_{n+1}-u_n", font_size=26),
                MathTex(r"2)\ \text{quotient } \dfrac{u_{n+1}}{u_n} \text{ comparé à } 1 \ (u_n>0)", font_size=26),
                MathTex(r"3)\ \text{sens de variation de } f, \text{ si } u_n=f(n)", font_size=26),
            ).arrange(DOWN, buff=0.25),
            box_width=11.0,
        )
        methodes.next_to(titre, DOWN, buff=0.35)

        with self.voiceover(
            text=(
                "Trois méthodes permettent d'étudier le sens de variation "
                "d'une suite. Première méthode : étudier le signe de la "
                "différence u indice n plus un moins u indice n. Deuxième "
                "méthode, utilisable seulement si tous les termes sont "
                "strictement positifs : comparer le quotient u indice n "
                "plus un sur u indice n à un. Troisième méthode, si u "
                "indice n égale f de n : étudier directement le sens de "
                "variation de la fonction f associée."
            )
        ) as tracker:
            self.play(FadeIn(methodes))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(methodes))

        # --- Exemple résolu 3 : méthode différence -----------------------------
        ex3_titre = Text(
            "Exemple 3 (différence) — un = n² - 6n + 2 :",
            font_size=23,
            color=YELLOW,
            weight="BOLD",
        )
        ex3_titre.next_to(titre, DOWN, buff=0.35)
        ex3_calc = example_box(
            MathTex(
                r"""
                u_{n+1}-u_n = (n+1)^2-6(n+1)+2-(n^2-6n+2) = 2n-5
                """,
                font_size=24,
            ),
            box_width=10.8,
        )
        ex3_calc.next_to(ex3_titre, DOWN, buff=0.3)
        ex3_concl = MathTex(
            r"2n-5\geq 0 \Longleftrightarrow n\geq 3 \ \Longrightarrow\ (u_n) \text{ décroît puis croît à partir de } n=3",
            font_size=21,
        )
        ex3_concl.next_to(ex3_calc, DOWN, buff=0.25)

        with self.voiceover(
            text=(
                "Exemple : u indice n égale n carré moins six n plus deux. "
                "On calcule la différence u indice n plus un moins u "
                "indice n, qui se simplifie en deux n moins cinq. Cette "
                "différence est positive ou nulle dès que n est supérieur "
                "ou égal à trois : la suite décroît d'abord, puis croît à "
                "partir du rang trois. Elle n'est donc pas monotone sur "
                "tout ℕ."
            )
        ) as tracker:
            self.play(FadeIn(ex3_titre))
            self.play(FadeIn(ex3_calc))
            self.play(FadeIn(ex3_concl))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(ex3_titre), FadeOut(ex3_calc), FadeOut(ex3_concl))

        # --- Exemple résolu 4 : méthode quotient -------------------------------
        ex4_titre = Text(
            "Exemple 4 (quotient) — un = 2ⁿ / n, pour n ≥ 1 :",
            font_size=23,
            color=YELLOW,
            weight="BOLD",
        )
        ex4_titre.next_to(titre, DOWN, buff=0.35)
        ex4_calc = example_box(
            MathTex(
                r"""
                \dfrac{u_{n+1}}{u_n} = \dfrac{2^{n+1}/(n+1)}{2^n/n}
                = \dfrac{2n}{n+1}
                """,
                font_size=25,
            ),
            box_width=9.6,
        )
        ex4_calc.next_to(ex4_titre, DOWN, buff=0.3)
        ex4_concl = MathTex(
            r"\dfrac{2n}{n+1}\geq 1 \Longleftrightarrow 2n\geq n+1 \Longleftrightarrow n\geq 1 \ \Longrightarrow\ (u_n) \text{ croissante}",
            font_size=21,
        )
        ex4_concl.next_to(ex4_calc, DOWN, buff=0.25)

        with self.voiceover(
            text=(
                "Autre exemple : u indice n égale deux puissance n, sur n, "
                "pour n supérieur ou égal à un — tous les termes sont "
                "strictement positifs, on peut donc utiliser le quotient. "
                "Le rapport u indice n plus un sur u indice n se simplifie "
                "en deux n sur n plus un, qui est toujours supérieur ou "
                "égal à un pour n supérieur ou égal à un. La suite est "
                "donc croissante."
            )
        ) as tracker:
            self.play(FadeIn(ex4_titre))
            self.play(FadeIn(ex4_calc))
            self.play(FadeIn(ex4_concl))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(ex4_titre), FadeOut(ex4_calc), FadeOut(ex4_concl))

        # --- À retenir -----------------------------------------------------------
        retenir = essentiel_box(
            Text(
                _wrap(
                    "Trois méthodes pour le sens de variation : signe de "
                    "un+1 - un (toujours valable), comparaison du quotient "
                    "un+1/un à 1 (si tous les termes sont strictement "
                    "positifs), ou variation de f si un = f(n).",
                    width=58,
                ),
                font_size=22,
            ),
            box_width=11.3,
        )
        retenir.next_to(titre, DOWN, buff=0.35)

        with self.voiceover(
            text=(
                "À retenir : la méthode de la différence fonctionne "
                "toujours. La méthode du quotient exige que tous les "
                "termes soient strictement positifs. Et lorsque u indice n "
                "s'écrit f de n, étudier f suffit, à condition que f soit "
                "monotone sur l'intervalle considéré."
            )
        ) as tracker:
            self.play(FadeIn(retenir))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(retenir))

        # --- Piège à éviter ----------------------------------------------------
        piege = warning_box(
            Text(
                _wrap(
                    "La méthode du quotient n'est valable que si TOUS les "
                    "termes de la suite sont strictement positifs : sinon, "
                    "diviser change le sens des inégalités de façon "
                    "incontrôlée, et la conclusion peut être fausse.",
                    width=56,
                ),
                font_size=22,
            ),
            box_width=11.2,
        )
        piege.next_to(titre, DOWN, buff=0.35)

        with self.voiceover(
            text=(
                "Piège à éviter : la méthode du quotient n'est valable que "
                "si tous les termes de la suite sont strictement positifs. "
                "Si un seul terme est négatif ou nul, diviser par ce terme "
                "peut inverser le sens de l'inégalité sans qu'on s'en "
                "aperçoive, et fausser complètement la conclusion."
            )
        ) as tracker:
            self.play(FadeIn(piege))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(piege), FadeOut(titre))
