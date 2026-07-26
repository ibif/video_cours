"""
scenes/Maths_SuitesNumeriques_05.py — Chapitre 15 « Suites numériques »
(1ereC, Maths), scène 05.

Suites majorées, minorées, bornées. Remarque sur l'infinité de majorants et
la méthode pour montrer qu'une suite n'est pas majorée. Exemple résolu 5
complet : un = 5 - 3/(n+1), bornée avec 2 ≤ un < 5.
Source : 1ereC/Maths.pdf, chapitre 15, pages 176-188.
"""

import textwrap

from manim import DOWN, UP, FadeIn, FadeOut, MathTex, Text, VGroup, Write, YELLOW

from shapes.base_scene import NotionScene
from shapes.boxes import definition_box, essentiel_box, example_box, scene_title, warning_box


def _wrap(text: str, width: int = 58) -> str:
    return "\n".join(textwrap.fill(line, width=width) for line in text.split("\n"))


class SuitesMajoreesMinoreesBornees(NotionScene):
    def construct(self):
        titre = scene_title("Suites majorées, minorées, bornées")
        titre.scale(0.5)
        titre.to_edge(UP)
        self.play(Write(titre))

        # --- Énoncé : définitions -------------------------------------------------
        definitions = definition_box(
            VGroup(
                MathTex(
                    r"(u_n) \text{ majorée par } M: \ \forall n,\ u_n\leq M",
                    font_size=27,
                ),
                MathTex(
                    r"(u_n) \text{ minorée par } m: \ \forall n,\ u_n\geq m",
                    font_size=27,
                ),
                Text(
                    "(un) est bornée si elle est à la fois majorée et minorée.",
                    font_size=22,
                ),
            ).arrange(DOWN, buff=0.25),
            box_width=10.8,
        )
        definitions.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Définitions : une suite u indice n est majorée par un réel "
                "M si, pour tout entier n, u indice n est inférieur ou "
                "égal à M — M est alors appelé un majorant. Elle est "
                "minorée par m si tous ses termes sont supérieurs ou égaux "
                "à m. Et elle est dite bornée si elle est à la fois "
                "majorée et minorée."
            )
        ) as tracker:
            self.play(FadeIn(definitions))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(definitions))

        # --- Remarque : infinité de majorants / non majorée ------------------------
        remarque = warning_box(
            Text(
                _wrap(
                    "Un majorant n'est jamais unique : si M majore (un), "
                    "tout réel plus grand que M majore aussi (un). Pour "
                    "montrer qu'une suite N'EST PAS majorée, on montre que "
                    "ses termes finissent par dépasser tout nombre donné, "
                    "aussi grand soit-il.",
                    width=56,
                ),
                font_size=22,
            ),
            box_width=11.3,
        )
        remarque.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Remarque importante : un majorant n'est jamais unique. Si "
                "M majore la suite, alors n'importe quel réel plus grand "
                "que M la majore aussi : il existe une infinité de "
                "majorants possibles. À l'inverse, pour montrer qu'une "
                "suite n'est pas majorée, on montre que ses termes finissent "
                "toujours par dépasser n'importe quel nombre donné, aussi "
                "grand soit-il."
            )
        ) as tracker:
            self.play(FadeIn(remarque))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(remarque))

        # --- Exemple résolu 5 -----------------------------------------------------
        ex5_titre = Text(
            "Exemple 5 — un = 5 - 3/(n+1) :",
            font_size=25,
            color=YELLOW,
            weight="BOLD",
        )
        ex5_titre.next_to(titre, DOWN, buff=0.4)
        ex5_calc = example_box(
            VGroup(
                MathTex(
                    r"\text{Pour tout } n\geq 0: \quad 0 < \dfrac{3}{n+1}\leq 3",
                    font_size=25,
                ),
                MathTex(
                    r"\Longrightarrow\ 2 \leq 5-\dfrac{3}{n+1} < 5,\quad \text{soit } 2\leq u_n<5",
                    font_size=25,
                ),
                Text(
                    "un est bornée : minorée par 2 et majorée par 5.",
                    font_size=22,
                    weight="BOLD",
                ),
            ).arrange(DOWN, buff=0.3),
            box_width=10.8,
        )
        ex5_calc.next_to(ex5_titre, DOWN, buff=0.3)

        with self.voiceover(
            text=(
                "Exemple : u indice n égale cinq moins trois sur n plus un. "
                "Pour tout n supérieur ou égal à zéro, la fraction trois "
                "sur n plus un est strictement comprise entre zéro et "
                "trois, bornes incluses pour la valeur trois au rang zéro. "
                "En soustrayant à cinq, on obtient que u indice n est "
                "toujours compris entre deux, inclus, et cinq, exclu. La "
                "suite est donc bornée : minorée par deux, majorée par "
                "cinq."
            )
        ) as tracker:
            self.play(FadeIn(ex5_titre))
            self.play(FadeIn(ex5_calc))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(ex5_titre), FadeOut(ex5_calc))

        # --- À retenir -----------------------------------------------------------
        retenir = essentiel_box(
            Text(
                _wrap(
                    "Majorée : tous les termes ≤ M. Minorée : tous les "
                    "termes ≥ m. Bornée : majorée ET minorée. Un majorant "
                    "(ou un minorant) n'est jamais unique.",
                    width=56,
                ),
                font_size=22,
            ),
            box_width=11.0,
        )
        retenir.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "À retenir : une suite majorée reste toujours en dessous "
                "d'un certain seuil, une suite minorée reste toujours "
                "au-dessus d'un certain seuil, et une suite bornée vérifie "
                "les deux à la fois. Un majorant, comme un minorant, n'est "
                "jamais unique."
            )
        ) as tracker:
            self.play(FadeIn(retenir))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(retenir))

        # --- Piège à éviter ----------------------------------------------------
        piege = warning_box(
            Text(
                _wrap(
                    "Piège : « majorée » ne veut pas dire « converge vers "
                    "son majorant ». Une suite peut être majorée sans être "
                    "monotone, ni même converger. Bornée + monotone est ce "
                    "qui garantit la convergence (théorème admis, hors "
                    "programme ici).",
                    width=56,
                ),
                font_size=21,
            ),
            box_width=11.3,
        )
        piege.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Attention au piège : être majorée ne signifie pas "
                "converger vers son majorant, ni même converger du tout. "
                "Une suite peut très bien être bornée sans être monotone. "
                "Ce sont les deux propriétés réunies, bornée et monotone, "
                "qui garantissent la convergence de la suite."
            )
        ) as tracker:
            self.play(FadeIn(piege))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(piege), FadeOut(titre))
