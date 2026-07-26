"""
scenes/Maths_GeometrieAnalytiquePlan_06.py — Chapitre 14 « Géométrie
analytique du plan » (1ereC, Maths), scène 06.

§ Équation réduite y=mx+p (pente m=-a/b, ordonnée à l'origine p=-c/b), cas
b=0 (droite verticale x=k). Lecture géométrique de la pente
m=(yB-yA)/(xB-xA). Représentation paramétrique {x=xA+αt, y=yA+βt}, avec
démonstration, passage paramétrique↔cartésienne. Exemple résolu complet :
droite par A(2;-1), u(-3;2).
Source : 1ereC/Maths.pdf, chapitre 14, pages 169-170.
"""

import textwrap

from manim import DOWN, LEFT, RIGHT, UP, WHITE, YELLOW, Axes, Create, Dot, FadeIn, FadeOut, MathTex, Text, VGroup, Write

from shapes.base_scene import NotionScene
from shapes.boxes import definition_box, example_box, scene_title, theorem_box, warning_box


def _wrap(text: str, width: int = 56) -> str:
    return "\n".join(textwrap.fill(line, width=width) for line in text.split("\n"))


class EquationReduiteParametrique(NotionScene):
    def construct(self):
        titre = scene_title("Équation réduite et représentation paramétrique")
        titre.scale(0.42)
        titre.to_edge(UP)

        # --- Énoncé : équation réduite ---------------------------------------------
        def_reduite = definition_box(
            VGroup(
                Text("Équation réduite d'une droite", font_size=24, weight="BOLD"),
                MathTex(
                    r"(D): ax+by+c=0,\ b\neq0 \ \Rightarrow\ y = \underbrace{-\dfrac{a}{b}}_{m}x "
                    r"\underbrace{-\dfrac{c}{b}}_{p}",
                    font_size=27,
                ),
                Text("m : pente (coefficient directeur)   p : ordonnée à l'origine", font_size=21),
            ).arrange(DOWN, buff=0.25),
            box_width=11.0,
        )
        def_reduite.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Quand b est non nul, on peut isoler y dans l'équation a x "
                "plus b y plus c égale zéro, et obtenir la forme réduite y "
                "égale m x plus p, où m, appelé pente ou coefficient "
                "directeur, vaut moins a sur b, et p, l'ordonnée à "
                "l'origine, vaut moins c sur b."
            )
        ) as tracker:
            self.play(Write(titre))
            self.play(FadeIn(def_reduite))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(def_reduite))

        cas_vertical = warning_box(
            VGroup(
                Text("Cas particulier : b = 0", font_size=22, weight="BOLD"),
                MathTex(r"ax+c=0 \ (a\neq0) \iff x = -\dfrac{c}{a} = k \quad \text{(droite VERTICALE)}", font_size=25),
            ).arrange(DOWN, buff=0.25),
            box_width=10.5,
        )
        cas_vertical.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Attention au cas où b est nul : l'équation devient a x "
                "plus c égale zéro, donc x égale une constante k. C'est une "
                "droite verticale, parallèle à l'axe des ordonnées, qui n'a "
                "PAS d'équation réduite de la forme y égale m x plus p."
            )
        ) as tracker:
            self.play(FadeIn(cas_vertical))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(cas_vertical))

        lecture_pente = theorem_box(
            MathTex(
                r"A(x_A;y_A),\ B(x_B;y_B) \in (D),\ x_A\neq x_B \ \Rightarrow\ "
                r"m = \dfrac{y_B-y_A}{x_B-x_A}",
                font_size=27,
            ),
        )
        lecture_pente.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "La pente a une lecture géométrique très concrète : si A et "
                "B sont deux points distincts de la droite avec des "
                "abscisses différentes, la pente m est égale à y-B moins "
                "y-A, sur x-B moins x-A — c'est le rapport entre la "
                "variation verticale et la variation horizontale, "
                "l'accroissement de y pour un accroissement de x."
            )
        ) as tracker:
            self.play(FadeIn(lecture_pente))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(lecture_pente))

        # --- Représentation paramétrique -------------------------------------------
        param = theorem_box(
            VGroup(
                Text("Représentation paramétrique de (D)", font_size=23, weight="BOLD"),
                MathTex(
                    r"A(x_A;y_A),\ \vec{u}(\alpha;\beta) \ \Rightarrow\ "
                    r"(D): \begin{cases} x = x_A + \alpha t \\ y = y_A + \beta t \end{cases}, \ t\in\mathbb{R}",
                    font_size=27,
                ),
            ).arrange(DOWN, buff=0.25),
            box_width=9.5,
        )
        param.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Une droite se décrit aussi par une représentation "
                "paramétrique : x égale x-A plus alpha t, et y égale y-A "
                "plus bêta t, où t parcourt tous les réels. Chaque valeur "
                "de t donne un point de la droite, et chaque point de la "
                "droite correspond à une unique valeur de t."
            )
        ) as tracker:
            self.play(FadeIn(param))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(param))

        demo_param = VGroup(
            MathTex(
                r"M(x;y)\in(D) \iff \overrightarrow{AM} \text{ colinéaire à } \vec{u}"
                r"\iff \exists t\in\mathbb{R}\ /\ \overrightarrow{AM} = t\,\vec{u}",
                font_size=24,
            ),
            MathTex(
                r"\overrightarrow{AM} = t\,\vec{u} \iff (x-x_A\,;\,y-y_A) = (t\alpha\,;\,t\beta)"
                r"\iff \begin{cases} x=x_A+\alpha t \\ y=y_A+\beta t \end{cases}",
                font_size=23,
            ),
        ).arrange(DOWN, buff=0.35)
        demo_param.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "La démonstration découle directement de la définition du "
                "vecteur directeur : M appartient à (D) si et seulement si "
                "le vecteur A-M est colinéaire à u, c'est-à-dire s'il "
                "existe un réel t tel que A-M égale t fois u. En identifiant "
                "les coordonnées, on retrouve exactement le système "
                "paramétrique."
            )
        ) as tracker:
            self.play(Write(demo_param))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(demo_param))

        # --- Exemple traité complet ------------------------------------------------
        axes = Axes(
            x_range=[-3, 3, 1], y_range=[-3, 3, 1], x_length=4.4, y_length=4.4,
            axis_config={"include_tip": True, "color": WHITE, "font_size": 16},
        )
        axes.move_to(LEFT * 3.3 + DOWN * 0.2)
        pa = VGroup(Dot(axes.c2p(2, -1), color="#DE7C1F"), MathTex("A", font_size=24).next_to(axes.c2p(2, -1), DOWN, buff=0.1))
        droite_ex = axes.plot(lambda x: (-2 * x + 1) / 3, x_range=[-3, 3], color=YELLOW)
        figure = VGroup(axes, droite_ex, pa)

        calcul = example_box(
            MathTex(
                r"A(2;-1),\ \vec{u}(-3;2)"
                r"\\[5pt]"
                r"\text{Cart.: } 2(x-2) - (-3)(y+1) = 0 \Rightarrow 2x+3y-1=0"
                r"\\[4pt]"
                r"\text{Réduite: } y = -\dfrac{2}{3}x + \dfrac{1}{3}"
                r"\\[4pt]"
                r"\text{Param.: } \begin{cases} x = 2-3t \\ y = -1+2t \end{cases}",
                font_size=21,
            ),
            box_width=6.6,
        )
        calcul.move_to(RIGHT * 3.2 + DOWN * 0.2)

        with self.voiceover(
            text=(
                "Exemple complet : la droite passant par A de coordonnées 2 "
                "et moins 1, de vecteur directeur u de coordonnées moins 3 "
                "et 2. Avec la formule bêta x moins x-A, moins alpha y "
                "moins y-A, on obtient 2, x moins 2, moins moins 3, y plus "
                "1, égale zéro, soit 2x plus 3y moins 1 égale zéro. La "
                "forme réduite est y égale moins deux tiers x plus un "
                "tiers. Et la représentation paramétrique est x égale 2 "
                "moins 3t, y égale moins 1 plus 2t."
            )
        ) as tracker:
            self.play(Create(figure))
            self.play(FadeIn(calcul))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(figure), FadeOut(calcul))

        # --- À retenir --------------------------------------------------------
        retenir = definition_box(
            VGroup(
                MathTex(r"y = mx+p \quad (b\neq0) \qquad x=k \quad (b=0)", font_size=25),
                MathTex(r"\begin{cases} x = x_A+\alpha t \\ y = y_A+\beta t \end{cases}, \ t\in\mathbb{R}", font_size=25),
            ).arrange(DOWN, buff=0.3),
        )
        retenir.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "À retenir : une droite non verticale a une équation "
                "réduite y égale m x plus p ; une droite verticale a "
                "l'équation x égale k. Et toute droite, verticale ou non, "
                "admet une représentation paramétrique construite à partir "
                "d'un point et d'un vecteur directeur."
            )
        ) as tracker:
            self.play(FadeIn(retenir))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(retenir))

        # --- Piège à éviter -----------------------------------------------------
        piege = warning_box(
            Text(
                _wrap(
                    "Une droite verticale (x=k) n'a PAS d'équation réduite "
                    "y=mx+p — sa pente serait « infinie ». Ne cherchez "
                    "jamais m et p pour une droite verticale : passez "
                    "directement par l'équation cartésienne ou paramétrique.",
                    width=48,
                ),
                font_size=22,
            ),
        )
        piege.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Piège classique à éviter : une droite verticale, d'équation "
                "x égale k, n'a pas d'équation réduite y égale m x plus p. "
                "Sa pente serait infinie, ce qui n'a pas de sens. Face à une "
                "droite verticale, passez directement par l'équation "
                "cartésienne ou la représentation paramétrique."
            )
        ) as tracker:
            self.play(FadeIn(piege))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(piege), FadeOut(titre))
