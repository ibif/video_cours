"""
scenes/Maths_LimitesContinuite_06.py — Chapitre 5 « Limites et continuité »
(1ereC, Maths), scène 06.

Méthode 2 : multiplier par l'expression conjuguée pour lever une F.I.
contenant une racine carrée. Exemples résolus 5 et 6.
Source : 1ereC/Maths.pdf, chapitre 5, pages 52-65.
"""

from manim import DOWN, UP, FadeIn, FadeOut, MathTex, Text, VGroup, Write, YELLOW

from shapes.base_scene import NotionScene
from shapes.boxes import essentiel_box, example_box, method_box, scene_title


class MethodeExpressionConjuguee(NotionScene):
    def construct(self):
        titre = scene_title("Méthode 2 — l'expression conjuguée")
        titre.scale(0.55)
        titre.to_edge(UP)
        self.play(Write(titre))

        # --- Énoncé de la méthode -------------------------------------------
        methode = method_box(
            MathTex(
                r"""
                \begin{array}{l}
                \text{Face à une F.I. contenant } \sqrt{u}-\sqrt{v}\ \text{(ou } \sqrt{u}-a\text{), on multiplie}\\
                \text{par l'expression conjuguée } \sqrt{u}+\sqrt{v}\ \text{(ou } \sqrt{u}+a\text{) :}\\[4pt]
                (\sqrt{u}-\sqrt{v})(\sqrt{u}+\sqrt{v}) = u - v
                \end{array}
                """,
                font_size=25,
            ),
            box_width=11.0,
        )
        methode.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Deuxième méthode : quand une forme indéterminée contient "
                "une différence de racines carrées, on multiplie et on "
                "divise par l'expression conjuguée. Le produit racine de u "
                "moins racine de v, par racine de u plus racine de v, "
                "vaut u moins v : la racine carrée disparaît, ce qui permet "
                "souvent de factoriser et de lever l'indétermination."
            )
        ) as tracker:
            self.play(FadeIn(methode))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(methode))

        # --- Exemple 5 : √(x²+3) - x en +∞ ---------------------------------------
        ex5_titre = Text("Exemple 5 — lim (√(x²+3) - x) en +∞ :", font_size=23, color=YELLOW, weight="BOLD")
        ex5_titre.next_to(titre, DOWN, buff=0.35)
        ex5_calc = MathTex(
            r"""
            \begin{array}{l}
            \sqrt{x^2+3}-x = \dfrac{(\sqrt{x^2+3}-x)(\sqrt{x^2+3}+x)}{\sqrt{x^2+3}+x}
            = \dfrac{(x^2+3)-x^2}{\sqrt{x^2+3}+x} = \dfrac{3}{\sqrt{x^2+3}+x}\\[6pt]
            \lim_{x\to+\infty}\big(\sqrt{x^2+3}+x\big) = +\infty
            \ \Longrightarrow\ \lim_{x\to+\infty}\big(\sqrt{x^2+3}-x\big) = 0
            \end{array}
            """,
            font_size=23,
        )
        ex5_calc.next_to(ex5_titre, DOWN, buff=0.35)

        with self.voiceover(
            text=(
                "Exemple : la limite de racine de x carré plus trois, moins "
                "x, en plus l'infini, est une forme plus l'infini moins "
                "l'infini. On multiplie par l'expression conjuguée : après "
                "simplification, il reste trois, sur racine de x carré plus "
                "trois, plus x. Le dénominateur tend vers plus l'infini, "
                "donc le quotient, et la limite cherchée, tendent vers "
                "zéro."
            )
        ) as tracker:
            self.play(FadeIn(ex5_titre))
            self.play(Write(ex5_calc))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(ex5_titre), FadeOut(ex5_calc))

        # --- Exemple 6 : (√x - 2)/(x - 4) en 4 -----------------------------------
        ex6_titre = Text("Exemple 6 — lim (√x - 2)/(x - 4) en x0 = 4 :", font_size=22, color=YELLOW, weight="BOLD")
        ex6_titre.next_to(titre, DOWN, buff=0.35)
        ex6_calc = MathTex(
            r"""
            \begin{array}{l}
            \text{F.I. } 0/0 \text{ en } x=4\\
            \dfrac{\sqrt{x}-2}{x-4} = \dfrac{(\sqrt{x}-2)(\sqrt{x}+2)}{(x-4)(\sqrt{x}+2)}
            = \dfrac{x-4}{(x-4)(\sqrt{x}+2)} = \dfrac{1}{\sqrt{x}+2} \quad (x\neq 4)\\[6pt]
            \Longrightarrow\ \lim_{x\to 4} \dfrac{\sqrt{x}-2}{x-4} = \dfrac{1}{4}
            \end{array}
            """,
            font_size=23,
        )
        ex6_calc.next_to(ex6_titre, DOWN, buff=0.35)
        ex6_box = example_box(ex6_calc, box_width=10.5)
        ex6_box.next_to(ex6_titre, DOWN, buff=0.3)

        with self.voiceover(
            text=(
                "Autre exemple : racine de x moins deux, sur x moins "
                "quatre, en x égale quatre, donne encore une forme zéro sur "
                "zéro. On multiplie par la conjuguée racine de x plus deux "
                ": le numérateur devient x moins quatre, qui se simplifie "
                "avec le dénominateur. Il reste un sur racine de x plus "
                "deux, dont la limite en quatre vaut un quart."
            )
        ) as tracker:
            self.play(FadeIn(ex6_titre))
            self.play(FadeIn(ex6_box))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(ex6_titre), FadeOut(ex6_box))

        # --- À retenir -----------------------------------------------------------
        retenir = essentiel_box(
            Text(
                "Racine carrée dans une F.I. : multiplier numérateur ET dénominateur "
                "par l'expression conjuguée, puis simplifier.",
                font_size=24,
            ),
            box_width=11.5,
        )
        retenir.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "À retenir : dès qu'une forme indéterminée contient une "
                "racine carrée, le réflexe est de multiplier numérateur et "
                "dénominateur par l'expression conjuguée, ce qui fait "
                "disparaître la racine et permet de simplifier."
            )
        ) as tracker:
            self.play(FadeIn(retenir))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(retenir), FadeOut(titre))
