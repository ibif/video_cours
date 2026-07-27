"""
scenes/Maths_Denombrement_10.py — Chapitre 6 « Dénombrement » (1ereC, Maths),
scène 10.

§ La formule du binôme de Newton : observation (a+b)² et (a+b)³ avec les
coefficients du triangle de Pascal, théorème avec démonstration (choix de
a ou b dans chaque facteur). Exemple résolu 7 (développer (a+b)⁴ et
(2x-1)³). Conséquences remarquables : 2ⁿ=Σ(n p) et 0=Σ(-1)ᵖ(n p).
Source : 1ereC/Maths.pdf, chapitre 6, pages 76-77.
"""

import textwrap

from manim import DOWN, UP, FadeIn, FadeOut, MathTex, Text, VGroup, Write, YELLOW

from shapes.base_scene import NotionScene
from shapes.boxes import example_box, property_box, scene_title, theorem_box


def _wrap(text: str, width: int = 54) -> str:
    return "\n".join(textwrap.fill(line, width=width) for line in text.split("\n"))


class BinomeDeNewton(NotionScene):
    def construct(self):
        titre = scene_title("Dénombrement — Formule du binôme de Newton")
        titre.scale(0.5)
        titre.to_edge(UP)

        # --- Énoncé : observation ---------------------------------------------------
        obs1 = MathTex(r"(a+b)^2 = 1\,a^2 + 2\,ab + 1\,b^2", font_size=26)
        obs2 = MathTex(r"(a+b)^3 = 1\,a^3 + 3\,a^2b + 3\,ab^2 + 1\,b^3", font_size=26)
        obs3 = Text(
            _wrap(
                "Coefficients 1, 2, 1 puis 1, 3, 3, 1 : ce sont exactement "
                "les lignes n=2 et n=3 du triangle de Pascal !",
                width=50,
            ),
            font_size=22,
            color=YELLOW,
        )
        observation = VGroup(obs1, obs2, obs3).arrange(DOWN, buff=0.35)
        observation.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Observons les développements déjà connus de a plus b au "
                "carré, et de a plus b au cube. a plus b au carré donne "
                "un a-carré, deux ab, un b-carré. a plus b au cube donne "
                "un a-cube, trois a-carré-b, trois a-b-carré, un b-cube. "
                "Les coefficients, 1, 2, 1 puis 1, 3, 3, 1, ne sont autres "
                "que les lignes n égale 2 et n égale 3 du triangle de "
                "Pascal ! Ce n'est pas un hasard : c'est ce que révèle la "
                "formule du binôme de Newton."
            )
        ) as tracker:
            self.play(Write(titre))
            self.play(Write(obs1))
            self.play(Write(obs2))
            self.play(FadeIn(obs3))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(observation))

        # --- Raisonnement : théorème + démonstration --------------------------------
        theo = theorem_box(
            VGroup(
                Text("Formule du binôme de Newton", font_size=23, weight="BOLD"),
                MathTex(
                    r"(a+b)^n = \sum_{p=0}^{n} \binom{n}{p}\, a^{n-p}\, b^{p}",
                    font_size=28,
                ),
            ).arrange(DOWN, buff=0.25),
        )
        theo.next_to(titre, DOWN, buff=0.45)

        with self.voiceover(
            text=(
                "Voici la formule générale : a plus b, à la puissance n, "
                "est égal à la somme, pour p allant de 0 à n, de n "
                "choisir p, fois a puissance n moins p, fois b puissance "
                "p."
            )
        ) as tracker:
            self.play(FadeIn(theo))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(theo))

        demo1 = MathTex(
            r"(a+b)^n = \underbrace{(a+b)(a+b)\cdots(a+b)}_{n \text{ facteurs}}",
            font_size=23,
        )
        demo2 = Text(
            _wrap(
                "En développant, chaque terme du résultat naît d'un choix "
                "— a OU b — effectué dans CHACUN des n facteurs.",
                width=50,
            ),
            font_size=21,
        )
        demo3 = MathTex(
            r"\text{Le terme } a^{n-p}b^{p} \text{ apparaît autant de fois qu'il y a de façons}",
            font_size=21,
        )
        demo4 = MathTex(
            r"\text{de choisir les } p \text{ facteurs où l'on prend } b \text{ parmi les } n \text{ facteurs} \ \to\ \binom{n}{p} \text{ fois}",
            font_size=20,
        )
        demo = VGroup(demo1, demo2, demo3, demo4).arrange(DOWN, buff=0.32)
        demo.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Démontrons cette formule par dénombrement. a plus b "
                "puissance n est le produit de n facteurs, chacun égal à "
                "a plus b. En développant ce produit, chaque terme du "
                "résultat naît d'un choix, a ou b, effectué dans chacun "
                "des n facteurs. Le terme a puissance n moins p, b "
                "puissance p, apparaît donc autant de fois qu'il y a de "
                "façons de choisir, parmi les n facteurs, lesquels p "
                "facteurs fourniront un b : c'est exactement n choisir p "
                "façons. D'où le coefficient dans la formule."
            )
        ) as tracker:
            self.play(Write(demo1))
            self.play(FadeIn(demo2))
            self.play(Write(demo3))
            self.play(Write(demo4))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(demo))

        # --- Exemple traité : développements -----------------------------------------
        enonce_dev = Text(
            "Exemple résolu 7 : développer (a+b)⁴ puis (2x−1)³.",
            font_size=23,
        )
        enonce_dev.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Mettons la formule en pratique sur deux développements : "
                "a plus b, exposant 4, puis 2x moins 1, exposant 3."
            )
        ) as tracker:
            self.play(FadeIn(enonce_dev))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(enonce_dev))

        dev1 = MathTex(
            r"(a+b)^4 = a^4 + 4a^3b + 6a^2b^2 + 4ab^3 + b^4",
            font_size=24,
        )
        dev1.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Pour a plus b, exposant 4, on lit directement la ligne n "
                "égale 4 du triangle de Pascal : 1, 4, 6, 4, 1. On "
                "obtient : a-quatre, plus 4 a-cube-b, plus 6 a-carré-"
                "b-carré, plus 4 a-b-cube, plus b-quatre."
            )
        ) as tracker:
            self.play(Write(dev1))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(dev1))

        dev2_1 = MathTex(
            r"(2x-1)^3 = (2x)^3 + 3(2x)^2(-1) + 3(2x)(-1)^2 + (-1)^3",
            font_size=22,
        )
        dev2_2 = MathTex(
            r"= 8x^3 - 12x^2 + 6x - 1",
            font_size=27,
            color=YELLOW,
        )
        dev2 = VGroup(dev2_1, dev2_2).arrange(DOWN, buff=0.35)
        dev2.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Pour 2x moins 1, exposant 3, on pose a égale 2x et b "
                "égale moins 1, et on applique la ligne n égale 3, 1, 3, "
                "3, 1. Après simplification des puissances, on obtient 8 "
                "x-cube, moins 12 x-carré, plus 6x, moins 1. Remarquez "
                "l'alternance des signes, due au signe négatif de b."
            )
        ) as tracker:
            self.play(Write(dev2_1))
            self.play(Write(dev2_2))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(dev2))

        # --- À retenir : conséquences remarquables --------------------------------
        conseq = property_box(
            VGroup(
                Text("Conséquences remarquables (a=b=1 et a=1,b=−1)", font_size=21, weight="BOLD"),
                MathTex(r"2^{n} = \sum_{p=0}^{n} \binom{n}{p} \quad (\text{d'où } \mathrm{Card}(\mathcal{P}(E))=2^n)", font_size=23),
                MathTex(r"0 = \sum_{p=0}^{n} (-1)^{p}\binom{n}{p}", font_size=25),
            ).arrange(DOWN, buff=0.28),
        )
        conseq.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "La formule du binôme livre deux conséquences remarquables. "
                "En posant a égale b égale 1, on obtient : 2 puissance n "
                "est égal à la somme de tous les n choisir p, pour p "
                "allant de 0 à n. C'est exactement ce résultat qui "
                "justifie, comme promis au début du chapitre, que le "
                "cardinal de l'ensemble des parties de E vaut 2 puissance "
                "n : chaque partie de E correspond à un choix de p "
                "éléments, pour un certain p. Et en posant a égale 1, b "
                "égale moins 1, on obtient : 0 est égal à la somme "
                "alternée des n choisir p, avec des signes plus et moins "
                "qui se succèdent."
            )
        ) as tracker:
            self.play(FadeIn(conseq))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(conseq), FadeOut(titre))
