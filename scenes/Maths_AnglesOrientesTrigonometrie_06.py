"""
scenes/Maths_AnglesOrientesTrigonometrie_06.py — Chapitre « Angles orientés
et trigonométrie » (1ereC, Maths), scène 06.

§ Tangente d'un nombre réel : définition tan x = sin x/cos x, propriétés
(périodicité π, 1+tan²x=1/cos²x), lecture géométrique sur la droite (T),
tableau des valeurs remarquables (0, π/6, π/4, π/3, π/2, π), astuce de
mémorisation.
Source : 1ereC/Maths.pdf, chapitre 2, pages 14-27.
"""

import textwrap

from manim import (
    DOWN,
    LEFT,
    ORIGIN,
    RIGHT,
    UP,
    WHITE,
    YELLOW,
    GREEN,
    GRAY_B,
    Circle,
    Dot,
    FadeIn,
    FadeOut,
    Line,
    MathTex,
    Text,
    VGroup,
    Write,
)

from shapes.base_scene import NotionScene
from shapes.boxes import definition_box, method_box, property_box, scene_title


def _wrap(text: str, width: int = 56) -> str:
    return "\n".join(textwrap.fill(line, width=width) for line in text.split("\n"))


def _cercle_axes(radius=1.4):
    axe_x = Line(LEFT * radius * 1.3, RIGHT * radius * 1.3, color=GRAY_B, stroke_width=1)
    axe_y = Line(DOWN * radius * 1.3, UP * radius * 1.3, color=GRAY_B, stroke_width=1)
    cercle = Circle(radius=radius, color=WHITE, stroke_width=2)
    O = Dot(ORIGIN, color=WHITE, radius=0.04)
    I = Dot(RIGHT * radius, color=YELLOW, radius=0.05)
    J = Dot(UP * radius, color=YELLOW, radius=0.05)
    label_O = MathTex("O", font_size=22, color=WHITE).next_to(O, DOWN + LEFT, buff=0.08)
    label_I = MathTex("I", font_size=22, color=YELLOW).next_to(I, DOWN, buff=0.08)
    label_J = MathTex("J", font_size=22, color=YELLOW).next_to(J, UP, buff=0.08)
    return VGroup(axe_x, axe_y, cercle, O, I, J, label_O, label_I, label_J)


class TangenteValeursRemarquables(NotionScene):
    def construct(self):
        titre = scene_title("Tangente et valeurs remarquables")
        titre.scale(0.58)
        titre.to_edge(UP)

        # --- Énoncé : définition -------------------------------------------
        definition = definition_box(
            VGroup(
                Text("Tangente de x", font_size=25, weight="BOLD"),
                MathTex(
                    r"\tan x = \dfrac{\sin x}{\cos x}, \quad \text{définie pour } x \neq \dfrac{\pi}{2} + k\pi,\ k \in \mathbb{Z}",
                    font_size=25,
                ),
            ).arrange(DOWN, buff=0.25),
            box_width=10.5,
        )
        definition.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "On définit la tangente d'un réel x, notée tan x, comme le "
                "quotient du sinus de x par le cosinus de x. Ce quotient "
                "n'existe que si le cosinus de x n'est pas nul : la "
                "tangente est donc définie pour tout réel x différent de "
                "pi sur deux plus k pi, k entier relatif."
            )
        ) as tracker:
            self.play(Write(titre))
            self.play(FadeIn(definition))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(definition))

        # --- Raisonnement : propriétés + lecture géométrique -----------------
        proprietes = property_box(
            VGroup(
                Text("Propriétés", font_size=23, weight="BOLD"),
                MathTex(r"\tan(x + \pi) = \tan x \quad \text{(périodicité } \pi \text{)}", font_size=23),
                MathTex(r"1 + \tan^2 x = \dfrac{1}{\cos^2 x}", font_size=23),
            ).arrange(DOWN, buff=0.25),
            box_width=6.6,
        )
        proprietes.to_edge(LEFT, buff=0.5).shift(DOWN * 0.3)

        fig = _cercle_axes(radius=1.4)
        tangente_T = Line(fig[5].get_center() + DOWN * 0.1, fig[5].get_center() + UP * 1.6, color="#DE7C1F", stroke_width=2)
        label_T = MathTex("(T)", font_size=20, color="#DE7C1F").next_to(tangente_T, UP, buff=0.05)
        angle_pt = fig[5].point_at_angle(0.9)
        point_m = Dot(angle_pt, color=GREEN, radius=0.05)
        droite_om = Line(fig[5].get_center(), angle_pt + (angle_pt - fig[5].get_center()) * 0.55, color=GREEN, stroke_width=1.5)
        point_tan = Dot(fig[5].get_center() + UP * 1.05, color="#DE7C1F", radius=0.05)
        label_tan_pt = MathTex(r"\tan x", font_size=18, color="#DE7C1F").next_to(point_tan, RIGHT, buff=0.06)
        figure = VGroup(fig, tangente_T, label_T, point_m, droite_om, point_tan, label_tan_pt)
        figure.next_to(proprietes, RIGHT, buff=0.5)

        with self.voiceover(
            text=(
                "La tangente vérifie deux propriétés utiles. D'abord, elle "
                "est périodique de période pi, et non deux pi comme "
                "cosinus et sinus : tan de x plus pi égale tan x. Ensuite, "
                "on a la relation un plus tangente carrée de x égale un "
                "sur cosinus carré de x. Géométriquement, tan x se lit "
                "directement sur la droite (T), tangente au cercle "
                "trigonométrique en I : c'est l'ordonnée du point "
                "d'intersection de la droite (O M de x) avec cette droite "
                "(T)."
            )
        ) as tracker:
            self.play(FadeIn(proprietes))
            self.play(FadeIn(figure))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(proprietes), FadeOut(figure))

        # --- Tableau des valeurs remarquables ----------------------------------
        angles = [r"0", r"\dfrac{\pi}{6}", r"\dfrac{\pi}{4}", r"\dfrac{\pi}{3}", r"\dfrac{\pi}{2}", r"\pi"]
        cosinus = [r"1", r"\dfrac{\sqrt{3}}{2}", r"\dfrac{\sqrt{2}}{2}", r"\dfrac{1}{2}", r"0", r"-1"]
        sinus = [r"0", r"\dfrac{1}{2}", r"\dfrac{\sqrt{2}}{2}", r"\dfrac{\sqrt{3}}{2}", r"1", r"0"]
        tangentes = [r"0", r"\dfrac{\sqrt{3}}{3}", r"1", r"\sqrt{3}", r"\text{n.d.}", r"0"]

        def _col(items, header, color=WHITE):
            head = Text(header, font_size=20, color=YELLOW, weight="BOLD")
            cells = [MathTex(it, font_size=20, color=color) for it in items]
            col = VGroup(head, *cells).arrange(DOWN, buff=0.28)
            return col

        col_x = _col(angles, "x")
        col_cos = _col(cosinus, "cos x")
        col_sin = _col(sinus, "sin x")
        col_tan = _col(tangentes, "tan x")
        tableau = VGroup(col_x, col_cos, col_sin, col_tan).arrange(RIGHT, buff=0.6)
        ligne_sep = Line(tableau.get_left() + LEFT * 0.1, tableau.get_right() + RIGHT * 0.1, color=GRAY_B, stroke_width=1)
        ligne_sep.next_to(col_x[0], DOWN, buff=0.12).align_to(tableau, LEFT).stretch_to_fit_width(tableau.width + 0.2)
        tableau_complet = VGroup(tableau, ligne_sep)
        tableau_complet.next_to(titre, DOWN, buff=0.55)

        with self.voiceover(
            text=(
                "Voici le tableau des valeurs remarquables à connaître par "
                "cœur : pour x égale zéro, pi sur six, pi sur quatre, pi "
                "sur trois et pi sur deux, ainsi que pi, on lit le cosinus, "
                "le sinus, et la tangente lorsqu'elle est définie. Notons "
                "que la tangente n'est pas définie en pi sur deux, "
                "puisque le cosinus s'y annule."
            )
        ) as tracker:
            self.play(FadeIn(tableau_complet))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(tableau_complet))

        # --- Méthode : astuce de mémorisation -----------------------------------
        astuce = method_box(
            VGroup(
                Text("Astuce de mémorisation", font_size=23, weight="BOLD"),
                MathTex(
                    r"\sin: \sqrt{\dfrac{0}{2}},\ \sqrt{\dfrac{1}{2\cdot2}},\ \sqrt{\dfrac{2}{2\cdot2}},\ \sqrt{\dfrac{3}{2\cdot2}},\ \sqrt{\dfrac{4}{2\cdot2}}",
                    font_size=22,
                ),
                Text(
                    _wrap(
                        "En écrivant sin(0), sin(π/6), sin(π/4), sin(π/3), "
                        "sin(π/2) sous la forme √(0)/2, √(1)/2, √(2)/2, "
                        "√(3)/2, √(4)/2, on retrouve 0, 1/2, √2/2, √3/2, 1 "
                        ": une suite CROISSANTE. Le cosinus suit l'ordre "
                        "inverse (DÉcroissant), car cos x = sin(π/2 − x).",
                        width=48,
                    ),
                    font_size=19,
                ),
            ).arrange(DOWN, buff=0.25),
            box_width=10,
        )
        astuce.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Une astuce facilite la mémorisation de ce tableau. En "
                "écrivant les cinq sinus sous la forme racine carrée de "
                "zéro sur deux, racine carrée de un sur deux, racine "
                "carrée de deux sur deux, racine carrée de trois sur deux, "
                "racine carrée de quatre sur deux, on retrouve bien zéro, "
                "un demi, racine de deux sur deux, racine de trois sur "
                "deux, et un : une suite croissante, avec le numérateur "
                "sous la racine qui augmente de un à chaque étape. Le "
                "cosinus suit exactement l'ordre inverse, décroissant, "
                "puisque le cosinus de x est le sinus de pi sur deux "
                "moins x."
            )
        ) as tracker:
            self.play(FadeIn(astuce))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(astuce), FadeOut(titre))
