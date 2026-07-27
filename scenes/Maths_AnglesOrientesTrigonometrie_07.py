"""
scenes/Maths_AnglesOrientesTrigonometrie_07.py — Chapitre « Angles orientés
et trigonométrie » (1ereC, Maths), scène 07.

§ Angles associés : -x, π-x, π+x, π/2-x, π/2+x — figure des points
symétriques du point image, tableau des propriétés (cosinus, sinus,
tangente), exemple résolu 4 (cos(2π/3), sin(5π/4), tan(7π/6)).
Source : 1ereC/Maths.pdf, chapitre 2, pages 14-27.
"""

import math
import textwrap

from manim import (
    DOWN,
    LEFT,
    ORIGIN,
    RIGHT,
    UP,
    WHITE,
    YELLOW,
    ORANGE,
    GREEN,
    RED,
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
from shapes.boxes import example_box, scene_title


def _wrap(text: str, width: int = 56) -> str:
    return "\n".join(textwrap.fill(line, width=width) for line in text.split("\n"))


def _cercle_axes(radius=1.5):
    axe_x = Line(LEFT * radius * 1.3, RIGHT * radius * 1.3, color=GRAY_B, stroke_width=1)
    axe_y = Line(DOWN * radius * 1.3, UP * radius * 1.3, color=GRAY_B, stroke_width=1)
    cercle = Circle(radius=radius, color=WHITE, stroke_width=2)
    O = Dot(ORIGIN, color=WHITE, radius=0.04)
    I = Dot(RIGHT * radius, color=YELLOW, radius=0.05)
    J = Dot(UP * radius, color=YELLOW, radius=0.05)
    label_O = MathTex("O", font_size=22, color=WHITE).next_to(O, DOWN + LEFT, buff=0.06)
    label_I = MathTex("I", font_size=22, color=YELLOW).next_to(I, DOWN, buff=0.06)
    label_J = MathTex("J", font_size=22, color=YELLOW).next_to(J, UP, buff=0.06)
    return VGroup(axe_x, axe_y, cercle, O, I, J, label_O, label_I, label_J)


class AnglesAssocies(NotionScene):
    def construct(self):
        titre = scene_title("Les angles associés")
        titre.scale(0.65)
        titre.to_edge(UP)

        with self.voiceover(
            text=(
                "On appelle angles associés à x les réels moins x, pi "
                "moins x, pi plus x, pi sur deux moins x, et pi sur deux "
                "plus x. Leurs points images sont liés à celui de x par "
                "des symétries simples, ce qui permet de retrouver leurs "
                "cosinus, sinus et tangente sans nouveau calcul."
            )
        ) as tracker:
            self.play(Write(titre))
            self.wait(tracker.get_remaining_duration())

        # --- Raisonnement : figure des points symétriques --------------------
        radius = 1.7
        fig = _cercle_axes(radius=radius)
        fig.to_edge(LEFT, buff=0.5).shift(DOWN * 0.2)
        center = fig[5].get_center()
        angle_x = 0.8  # x de référence

        def _pt(angle):
            return center + radius * math.cos(angle) * RIGHT + radius * math.sin(angle) * UP

        pM = Dot(_pt(angle_x), color=YELLOW, radius=0.06)
        pMoinsX = Dot(_pt(-angle_x), color=GREEN, radius=0.06)
        pPiMoinsX = Dot(_pt(3.14159 - angle_x), color=ORANGE, radius=0.06)
        pPiPlusX = Dot(_pt(3.14159 + angle_x), color=RED, radius=0.06)

        lblM = MathTex("M(x)", font_size=18, color=YELLOW).next_to(pM, UP + RIGHT, buff=0.05)
        lblMoinsX = MathTex("M(-x)", font_size=18, color=GREEN).next_to(pMoinsX, DOWN + RIGHT, buff=0.05)
        lblPiMoinsX = MathTex(r"M(\pi{-}x)", font_size=18, color=ORANGE).next_to(pPiMoinsX, UP + LEFT, buff=0.05)
        lblPiPlusX = MathTex(r"M(\pi{+}x)", font_size=18, color=RED).next_to(pPiPlusX, DOWN + LEFT, buff=0.05)

        figure = VGroup(fig, pM, pMoinsX, pPiMoinsX, pPiPlusX, lblM, lblMoinsX, lblPiMoinsX, lblPiPlusX)

        explication = Text(
            _wrap(
                "M(-x) est le symétrique de M(x) par rapport à l'axe "
                "(OI) ; M(π-x) est son symétrique par rapport à l'axe "
                "(OJ) ; M(π+x) est son symétrique par rapport à O. On "
                "obtient de même M(π/2-x) et M(π/2+x) par symétries par "
                "rapport à la bissectrice et à (OJ).",
                width=40,
            ),
            font_size=19,
        )
        explication.to_edge(RIGHT, buff=0.4)

        with self.voiceover(
            text=(
                "Sur le cercle trigonométrique, le point M de moins x est "
                "le symétrique de M de x par rapport à l'axe des "
                "cosinus, l'axe O I. Le point M de pi moins x est son "
                "symétrique par rapport à l'axe des sinus, l'axe O J. Le "
                "point M de pi plus x est son symétrique par rapport au "
                "centre O. On obtiendrait de la même façon M de pi sur "
                "deux moins x et M de pi sur deux plus x, par des "
                "symétries liées à la première bissectrice."
            )
        ) as tracker:
            self.play(FadeIn(figure))
            self.play(FadeIn(explication))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(figure), FadeOut(explication))

        # --- Tableau des propriétés ---------------------------------------------
        lignes = [
            (r"-x", r"\cos x", r"-\sin x", r"-\tan x"),
            (r"\pi - x", r"-\cos x", r"\sin x", r"-\tan x"),
            (r"\pi + x", r"-\cos x", r"-\sin x", r"\tan x"),
            (r"\dfrac{\pi}{2} - x", r"\sin x", r"\cos x", r"\dfrac{1}{\tan x}"),
            (r"\dfrac{\pi}{2} + x", r"-\sin x", r"\cos x", r"-\dfrac{1}{\tan x}"),
        ]
        entete = VGroup(
            MathTex("t", font_size=20, color=YELLOW),
            MathTex(r"\cos t", font_size=20, color=YELLOW),
            MathTex(r"\sin t", font_size=20, color=YELLOW),
            MathTex(r"\tan t", font_size=20, color=YELLOW),
        ).arrange(RIGHT, buff=0.8)

        table = VGroup(entete)
        for row in lignes:
            row_group = VGroup(*[MathTex(cell, font_size=19) for cell in row]).arrange(RIGHT, buff=0.75)
            table.add(row_group)
        table.arrange(DOWN, buff=0.3)
        # Aligner les colonnes verticalement sur celles de l'en-tête.
        for row in table[1:]:
            for i in range(4):
                row[i].move_to([table[0][i].get_center()[0], row[i].get_center()[1], 0])

        ligne_sep = Line(table.get_left() + LEFT * 0.15, table.get_right() + RIGHT * 0.15, color=GRAY_B, stroke_width=1)
        ligne_sep.next_to(entete, DOWN, buff=0.12)
        tableau_complet = VGroup(table, ligne_sep)
        tableau_complet.next_to(titre, DOWN, buff=0.5).scale(0.95)

        with self.voiceover(
            text=(
                "Voici le tableau récapitulatif à retenir. Pour moins x, "
                "le cosinus ne change pas mais le sinus et la tangente "
                "changent de signe. Pour pi moins x, le sinus ne change "
                "pas, le cosinus et la tangente changent de signe. Pour "
                "pi plus x, la tangente ne change pas, le cosinus et le "
                "sinus changent de signe. Pour pi sur deux moins x, "
                "cosinus et sinus s'échangent, et la tangente devient son "
                "inverse. Pour pi sur deux plus x, cosinus et sinus "
                "s'échangent aussi, mais avec un changement de signe sur "
                "le sinus, et la tangente devient l'opposé de son "
                "inverse."
            )
        ) as tracker:
            self.play(FadeIn(tableau_complet))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(tableau_complet))

        # --- Exemple résolu 4 -----------------------------------------------------
        exemple = example_box(
            VGroup(
                MathTex(
                    r"\cos\!\left(\dfrac{2\pi}{3}\right) = \cos\!\left(\pi - \dfrac{\pi}{3}\right) = -\cos\!\left(\dfrac{\pi}{3}\right) = -\dfrac{1}{2}",
                    font_size=23,
                ),
                MathTex(
                    r"\sin\!\left(\dfrac{5\pi}{4}\right) = \sin\!\left(\pi + \dfrac{\pi}{4}\right) = -\sin\!\left(\dfrac{\pi}{4}\right) = -\dfrac{\sqrt{2}}{2}",
                    font_size=23,
                ),
                MathTex(
                    r"\tan\!\left(\dfrac{7\pi}{6}\right) = \tan\!\left(\pi + \dfrac{\pi}{6}\right) = \tan\!\left(\dfrac{\pi}{6}\right) = \dfrac{\sqrt{3}}{3}",
                    font_size=23,
                ),
            ).arrange(DOWN, buff=0.32),
            box_width=11,
        )
        exemple.next_to(titre, DOWN, buff=0.55)

        with self.voiceover(
            text=(
                "Exemple résolu. Calculons trois valeurs à l'aide des "
                "angles associés. D'abord, cosinus de deux pi tiers "
                "s'écrit cosinus de pi moins pi tiers, donc l'opposé de "
                "cosinus de pi tiers, soit moins un demi. Ensuite, sinus "
                "de cinq pi quarts s'écrit sinus de pi plus pi quart, "
                "donc l'opposé de sinus de pi quart, soit moins racine de "
                "deux sur deux. Enfin, tangente de sept pi sixièmes "
                "s'écrit tangente de pi plus pi sixième : comme la "
                "tangente est pi-périodique, cela vaut simplement tangente "
                "de pi sixième, soit racine de trois sur trois."
            )
        ) as tracker:
            self.play(FadeIn(exemple))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(exemple), FadeOut(titre))
