"""
scenes/Maths_LimitesContinuite_10.py — Chapitre 5 « Limites et continuité »
(1ereC, Maths), scène 10.

Continuité en un point (3 conditions), continuité à gauche/à droite.
Exemple résolu 14 (fonction par morceaux), contre-exemples (partie
entière, valeur imposée différente de la limite). Fonctions continues de
référence et opérations sur les fonctions continues (admises).
Source : 1ereC/Maths.pdf, chapitre 5, pages 52-65.
"""

import textwrap

from manim import DOWN, UP, FadeIn, FadeOut, MathTex, Text, VGroup, Write, YELLOW

from shapes.base_scene import NotionScene
from shapes.boxes import definition_box, example_box, property_box, scene_title


def _wrap(text: str, width: int = 58) -> str:
    return "\n".join(textwrap.fill(line, width=width) for line in text.split("\n"))


class ContinuiteEnUnPoint(NotionScene):
    def construct(self):
        titre = scene_title("Continuité en un point")
        titre.scale(0.6)
        titre.to_edge(UP)
        self.play(Write(titre))

        # --- Énoncé : définition de la continuité en x0 --------------------------
        def_continuite = definition_box(
            VGroup(
                Text("f est continue en x0 si les trois conditions suivantes sont réunies :", font_size=22),
                MathTex(
                    r"""
                    \begin{array}{l}
                    \text{1) } x_0 \in D_f \text{ (f est définie en } x_0\text{)}\\
                    \text{2) } \lim_{x\to x_0} f(x) \text{ existe et est finie}\\
                    \text{3) } \lim_{x\to x_0} f(x) = f(x_0)
                    \end{array}
                    """,
                    font_size=26,
                ),
            ).arrange(DOWN, buff=0.3),
            box_width=10.5,
        )
        def_continuite.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Une fonction f est continue en x zéro si trois conditions "
                "sont réunies : d'abord, f est définie en x zéro ; ensuite, "
                "f admet une limite finie en x zéro ; enfin, cette limite "
                "est exactement égale à f de x zéro. Intuitivement, la "
                "courbe ne présente ni saut, ni trou en x zéro."
            )
        ) as tracker:
            self.play(FadeIn(def_continuite))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(def_continuite))

        def_laterale = definition_box(
            MathTex(
                r"""
                \begin{array}{l}
                f \text{ continue à droite en } x_0 : \lim_{x\to x_0^{+}} f(x) = f(x_0)\\
                f \text{ continue à gauche en } x_0 : \lim_{x\to x_0^{-}} f(x) = f(x_0)
                \end{array}
                """,
                font_size=25,
            ),
            box_width=10.0,
        )
        def_laterale.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "On définit aussi la continuité à droite, quand la limite "
                "à droite existe et vaut f de x zéro, et la continuité à "
                "gauche, de la même façon avec la limite à gauche. f est "
                "continue en x zéro si et seulement si elle est continue à "
                "la fois à gauche et à droite en x zéro."
            )
        ) as tracker:
            self.play(FadeIn(def_laterale))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(def_laterale))

        # --- Exemple résolu 14 : fonction par morceaux ----------------------------
        ex14_titre = Text(
            "Exemple 14 — continuité en 1 de f définie par morceaux :",
            font_size=21,
            color=YELLOW,
            weight="BOLD",
        )
        ex14_titre.next_to(titre, DOWN, buff=0.35)
        ex14_def = MathTex(
            r"""
            f(x) = \left\{
            \begin{array}{ll}
            x^2 & \text{si } x \leq 1\\
            2x - 1 & \text{si } x > 1
            \end{array}
            \right.
            """,
            font_size=27,
        )
        ex14_def.next_to(ex14_titre, DOWN, buff=0.3)
        ex14_calc = MathTex(
            r"""
            \begin{array}{l}
            \lim_{x\to 1^{-}} f(x) = 1^2 = 1, \qquad f(1) = 1^2 = 1\\
            \lim_{x\to 1^{+}} f(x) = 2\times 1 - 1 = 1\\
            \Longrightarrow\ \lim_{x\to 1^{-}} f(x) = \lim_{x\to 1^{+}} f(x) = f(1) = 1
            \end{array}
            """,
            font_size=23,
        )
        ex14_calc.next_to(ex14_def, DOWN, buff=0.3)
        ex14_box = example_box(VGroup(ex14_def, ex14_calc).arrange(DOWN, buff=0.3), box_width=10.5)
        ex14_box.next_to(ex14_titre, DOWN, buff=0.25)

        with self.voiceover(
            text=(
                "Exemple : soit f de x égale x carré si x est inférieur ou "
                "égal à un, et deux x moins un si x est strictement "
                "supérieur à un. La limite à gauche en un vaut un, comme f "
                "de un ; la limite à droite en un vaut aussi un. Les trois "
                "valeurs coïncident : f est donc continue en un."
            )
        ) as tracker:
            self.play(FadeIn(ex14_titre))
            self.play(FadeIn(ex14_box))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(ex14_titre), FadeOut(ex14_box))

        # --- Contre-exemples --------------------------------------------------
        contre_titre = Text("Contre-exemples de discontinuité :", font_size=23, color=YELLOW, weight="BOLD")
        contre_titre.next_to(titre, DOWN, buff=0.35)
        contre = MathTex(
            r"""
            \begin{array}{l}
            \text{Partie entière } E : \lim_{x\to 1^{-}} E(x) = 0 \neq 1 = \lim_{x\to 1^{+}} E(x)\\
            \text{(saut en chaque entier, discontinue partout sauf sur } \mathbb{Z}^c\text{)}\\[6pt]
            g(x)=x^2 \text{ si } x\neq 1, \quad g(1)=5 :
            \quad \lim_{x\to 1} g(x) = 1 \neq 5 = g(1)
            \end{array}
            """,
            font_size=21,
        )
        contre.next_to(contre_titre, DOWN, buff=0.3)

        with self.voiceover(
            text=(
                "Deux contre-exemples classiques. La fonction partie "
                "entière fait un saut en chaque entier : la limite à "
                "gauche et la limite à droite en un diffèrent, donc elle "
                "est discontinue en chaque entier. Deuxième cas : une "
                "fonction qui vaut x carré partout sauf en un, où on lui "
                "impose la valeur cinq : la limite en un vaut un, mais la "
                "valeur de la fonction vaut cinq — la troisième condition "
                "échoue, donc la fonction est discontinue en un."
            )
        ) as tracker:
            self.play(FadeIn(contre_titre))
            self.play(Write(contre))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(contre_titre), FadeOut(contre))

        # --- Fonctions continues de référence + opérations (admises) -------------
        prop_ref = property_box(
            Text(
                _wrap(
                    "Les fonctions polynômes, x ↦ √x, sinus et cosinus sont "
                    "continues sur tout leur ensemble de définition.",
                    width=52,
                ),
                font_size=23,
            ),
            box_width=10.5,
        )
        prop_ref.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Propriété admise : les fonctions polynômes, la fonction "
                "racine carrée, ainsi que sinus et cosinus, sont continues "
                "en tout point de leur ensemble de définition."
            )
        ) as tracker:
            self.play(FadeIn(prop_ref))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(prop_ref))

        prop_ops = property_box(
            Text(
                _wrap(
                    "Si f et g sont continues en x0, alors f+g, f×g, "
                    "et f/g (si g(x0)≠0) le sont aussi.",
                    width=48,
                ),
                font_size=23,
            ),
            box_width=9.5,
        )
        prop_ops.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Autre propriété admise : si f et g sont continues en x "
                "zéro, alors leur somme, leur produit, et leur quotient — "
                "à condition que g de x zéro soit non nul — sont eux aussi "
                "continus en x zéro. En pratique, toute fonction usuelle "
                "construite par opérations à partir des fonctions de "
                "référence est continue sur son domaine de définition."
            )
        ) as tracker:
            self.play(FadeIn(prop_ops))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(prop_ops), FadeOut(titre))
