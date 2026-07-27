"""
scenes/Maths_AnglesOrientesTrigonometrie_02.py — Chapitre « Angles orientés
et trigonométrie » (1ereC, Maths), scène 02.

§ Point image d'un nombre réel : construction par enroulement de la droite
tangente au cercle trigonométrique, définition du point image M(x),
propriété (deux réels ont même point image ssi ils diffèrent d'un multiple
de 2π), lecture de cos x, sin x, tan x sur la figure.
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
    ORANGE,
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
from shapes.boxes import definition_box, property_box, scene_title


def _wrap(text: str, width: int = 56) -> str:
    return "\n".join(textwrap.fill(line, width=width) for line in text.split("\n"))


def _cercle_axes(radius=1.5):
    axe_x = Line(LEFT * radius * 1.3, RIGHT * radius * 1.3, color=GRAY_B, stroke_width=1)
    axe_y = Line(DOWN * radius * 1.3, UP * radius * 1.3, color=GRAY_B, stroke_width=1)
    cercle = Circle(radius=radius, color=WHITE, stroke_width=2)
    O = Dot(ORIGIN, color=WHITE, radius=0.04)
    I = Dot(RIGHT * radius, color=YELLOW, radius=0.05)
    J = Dot(UP * radius, color=YELLOW, radius=0.05)
    label_O = MathTex("O", font_size=24, color=WHITE).next_to(O, DOWN + LEFT, buff=0.08)
    label_I = MathTex("I", font_size=24, color=YELLOW).next_to(I, DOWN, buff=0.08)
    label_J = MathTex("J", font_size=24, color=YELLOW).next_to(J, UP, buff=0.08)
    return VGroup(axe_x, axe_y, cercle, O, I, J, label_O, label_I, label_J)


class PointImageNombreReel(NotionScene):
    def construct(self):
        titre = scene_title("Le point image d'un nombre réel")
        titre.scale(0.6)
        titre.to_edge(UP)

        with self.voiceover(
            text=(
                "Dans la scène précédente, on a défini le radian comme "
                "unité de mesure des angles. On va maintenant associer, à "
                "chaque nombre réel, un point précis du cercle "
                "trigonométrique : son point image."
            )
        ) as tracker:
            self.play(Write(titre))
            self.wait(tracker.get_remaining_duration())

        # --- Raisonnement : construction par enroulement --------------------
        fig = _cercle_axes(radius=1.5)
        fig.shift(LEFT * 3.0)

        tangente = Line(
            fig[5].get_center() + DOWN * 1.7,
            fig[5].get_center() + UP * 1.7,
            color=ORANGE,
            stroke_width=2,
        )
        graduations = VGroup(
            *[
                Line(
                    fig[5].get_center() + UP * k * 0.35 + LEFT * 0.05,
                    fig[5].get_center() + UP * k * 0.35 + RIGHT * 0.05,
                    color=ORANGE,
                    stroke_width=1.5,
                )
                for k in range(-4, 5)
            ]
        )
        label_tangente = MathTex("(T)", font_size=22, color=ORANGE).next_to(tangente, UP, buff=0.1)

        point_x = Dot(fig[5].get_center() + [1.5 * 0.55, 1.5 * 0.835, 0], color=GREEN, radius=0.06)
        label_point_x = MathTex("M(x)", font_size=24, color=GREEN).next_to(point_x, UP + RIGHT, buff=0.08)
        fleche_enroul = MathTex(r"x", font_size=22, color=ORANGE).next_to(tangente, RIGHT, buff=0.15).shift(UP * 0.9)

        schema = VGroup(fig, tangente, graduations, label_tangente, point_x, label_point_x, fleche_enroul)

        explication = definition_box(
            VGroup(
                Text("Point image M(x)", font_size=24, weight="BOLD"),
                Text(
                    _wrap(
                        "On enroule sur le cercle trigonométrique, à partir "
                        "de I, un fil de longueur |x| gradué comme la "
                        "droite (T) tangente au cercle en I : dans le sens "
                        "direct si x > 0, dans le sens indirect si x < 0. "
                        "Le point d'arrivée M(x) est le point image de x.",
                        width=38,
                    ),
                    font_size=19,
                ),
            ).arrange(DOWN, buff=0.25),
            box_width=6.4,
        )
        explication.to_edge(RIGHT, buff=0.4).shift(DOWN * 0.2)

        with self.voiceover(
            text=(
                "On imagine la droite (T), tangente au cercle "
                "trigonométrique au point I, graduée comme un axe gradué "
                "ordinaire. Pour un réel x, on enroule sur le cercle, à "
                "partir de I, un fil de longueur valeur absolue de x pris "
                "sur cette droite : dans le sens direct si x est positif, "
                "dans le sens indirect si x est négatif. Le point où "
                "s'arrête le fil est appelé le point image de x, noté "
                "M de x."
            )
        ) as tracker:
            self.play(FadeIn(schema))
            self.wait(0.3)
            self.play(FadeIn(explication))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(schema), FadeOut(explication))

        # --- Propriété : même point image ssi congrus 2 pi -------------------
        propriete = property_box(
            VGroup(
                Text(
                    _wrap(
                        "Deux réels x et y ont le même point image sur le "
                        "cercle trigonométrique si, et seulement si, ils "
                        "diffèrent d'un multiple entier de 2π :",
                        width=50,
                    ),
                    font_size=22,
                ),
                MathTex(r"M(x) = M(y) \iff \exists\, k \in \mathbb{Z},\ x = y + k \times 2\pi", font_size=27),
            ).arrange(DOWN, buff=0.3),
            box_width=9.5,
        )
        propriete.next_to(titre, DOWN, buff=0.55)

        with self.voiceover(
            text=(
                "Comme le périmètre du cercle trigonométrique vaut deux "
                "pi, faire un tour complet de plus ou de moins ramène "
                "exactement au même point. On obtient donc la propriété "
                "suivante : deux réels x et y ont le même point image si, "
                "et seulement si, ils diffèrent d'un multiple entier de "
                "deux pi, c'est-à-dire s'il existe un entier relatif k tel "
                "que x égale y plus k fois deux pi."
            )
        ) as tracker:
            self.play(FadeIn(propriete))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(propriete))

        # --- Exemple traité : lecture de cos x, sin x, tan x sur la figure ---
        fig2 = _cercle_axes(radius=1.7)
        point_m = Dot(fig2[5].get_center() + [1.7 * 0.62, 1.7 * 0.78, 0], color=GREEN, radius=0.06)
        label_m = MathTex("M(x)", font_size=22, color=GREEN).next_to(point_m, UP, buff=0.08)
        proj_cos = Line(point_m.get_center(), [point_m.get_center()[0], 0, 0], color=YELLOW, stroke_width=2)
        proj_sin = Line(point_m.get_center(), [0, point_m.get_center()[1], 0], color=ORANGE, stroke_width=2)
        label_cos = MathTex(r"\cos x", font_size=20, color=YELLOW).next_to(proj_cos, DOWN, buff=0.08)
        label_sin = MathTex(r"\sin x", font_size=20, color=ORANGE).next_to(proj_sin, LEFT, buff=0.08)
        tangente2 = Line(
            fig2[5].get_center() + DOWN * 0.2,
            fig2[5].get_center() + UP * 1.6,
            color="#DE7C1F",
            stroke_width=1.5,
        )
        droite_om = Line(ORIGIN + LEFT * 3.0, point_m.get_center() + (point_m.get_center() - ORIGIN) * 0.4, color=GREEN, stroke_width=1)
        point_tan = Dot(fig2[5].get_center() + UP * 1.05, color="#DE7C1F", radius=0.05)
        label_tan = MathTex(r"\tan x", font_size=20, color="#DE7C1F").next_to(point_tan, RIGHT, buff=0.08)

        figure_complete = VGroup(
            fig2, point_m, label_m, proj_cos, proj_sin, label_cos, label_sin,
            tangente2, droite_om, point_tan, label_tan,
        )
        figure_complete.move_to(ORIGIN).shift(DOWN * 0.3)

        with self.voiceover(
            text=(
                "Sur cette figure, le point M de x permet de lire "
                "directement trois nombres essentiels de ce chapitre : son "
                "abscisse est le cosinus de x, son ordonnée est le sinus "
                "de x, et l'ordonnée du point où la droite O-M coupe la "
                "tangente (T) est la tangente de x. Ces trois nombres "
                "seront définis précisément dans les scènes suivantes."
            )
        ) as tracker:
            self.play(FadeIn(figure_complete))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(figure_complete), FadeOut(titre))
