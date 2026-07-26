"""
scenes/Maths_AnglesOrientesTrigonometrie_08.py — Chapitre « Angles orientés
et trigonométrie » (1ereC, Maths), scène 08.

§ Formules d'addition : cos(a±b), sin(a±b) avec démonstration (produit
scalaire de deux vecteurs du cercle calculé de deux façons), corollaire sur
la tangente de a+b / a-b. Exemple résolu 5 : cos(π/12) et sin(π/12) via
π/12 = π/3 - π/4.
Source : 1ereC/Maths.pdf, chapitre 2, pages 14-27.
"""

import textwrap

import numpy as np
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
from shapes.boxes import example_box, theorem_box, scene_title


def _wrap(text: str, width: int = 56) -> str:
    return "\n".join(textwrap.fill(line, width=width) for line in text.split("\n"))


class FormulesAddition(NotionScene):
    def construct(self):
        titre = scene_title("Les formules d'addition")
        titre.scale(0.65)
        titre.to_edge(UP)

        # --- Énoncé : théorème --------------------------------------------
        theoreme = theorem_box(
            VGroup(
                Text("Formules d'addition", font_size=24, weight="BOLD"),
                MathTex(r"\cos(a-b) = \cos a \cos b + \sin a \sin b", font_size=24),
                MathTex(r"\cos(a+b) = \cos a \cos b - \sin a \sin b", font_size=24),
                MathTex(r"\sin(a+b) = \sin a \cos b + \cos a \sin b", font_size=24),
                MathTex(r"\sin(a-b) = \sin a \cos b - \cos a \sin b", font_size=24),
            ).arrange(DOWN, buff=0.22),
            box_width=8.6,
        )
        theoreme.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Voici quatre formules essentielles, à connaître par cœur, "
                "appelées formules d'addition. Cosinus de a moins b égale "
                "cosinus a cosinus b plus sinus a sinus b. Cosinus de a "
                "plus b égale cosinus a cosinus b moins sinus a sinus b. "
                "Sinus de a plus b égale sinus a cosinus b plus cosinus a "
                "sinus b. Et sinus de a moins b égale sinus a cosinus b "
                "moins cosinus a sinus b."
            )
        ) as tracker:
            self.play(Write(titre))
            self.play(FadeIn(theoreme))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(theoreme))

        # --- Raisonnement : démonstration par produit scalaire ---------------
        radius = 1.4
        cercle = Circle(radius=radius, color=WHITE, stroke_width=2)
        axe_x = Line(LEFT * radius * 1.3, RIGHT * radius * 1.3, color=GRAY_B, stroke_width=1)
        axe_y = Line(DOWN * radius * 1.3, UP * radius * 1.3, color=GRAY_B, stroke_width=1)
        O = Dot(ORIGIN, color=WHITE, radius=0.04)
        pA = Dot(np.array([radius * 0.8, radius * 0.6, 0]), color=YELLOW, radius=0.05)
        pB = Dot(np.array([radius * 0.35, radius * -0.94, 0]), color=GREEN, radius=0.05)
        lblA = MathTex("M(a)", font_size=18, color=YELLOW).next_to(pA, UP, buff=0.06)
        lblB = MathTex("M(b)", font_size=18, color=GREEN).next_to(pB, DOWN, buff=0.06)
        vecA = Line(ORIGIN, pA.get_center(), color=YELLOW, stroke_width=2)
        vecB = Line(ORIGIN, pB.get_center(), color=GREEN, stroke_width=2)
        figure = VGroup(axe_x, axe_y, cercle, O, pA, pB, lblA, lblB, vecA, vecB)
        figure.to_edge(LEFT, buff=0.6).shift(DOWN * 0.2)

        demo = VGroup(
            Text("Démonstration (cas a - b)", font_size=21, color=YELLOW, weight="BOLD"),
            Text(
                "Soient M(a) et M(b) les points images de a et b : OM(a)⃗ et OM(b)⃗ sont unitaires.",
                font_size=17,
            ),
            MathTex(
                r"\text{1) coordonnées : } \overrightarrow{OM(a)} \cdot \overrightarrow{OM(b)} = \cos a \cos b + \sin a \sin b",
                font_size=18,
            ),
            MathTex(
                r"\text{2) angle : } \overrightarrow{OM(a)} \cdot \overrightarrow{OM(b)} = \|\overrightarrow{OM(a)}\| \, \|\overrightarrow{OM(b)}\| \cos(a-b) = \cos(a-b)",
                font_size=18,
            ),
            MathTex(r"\text{d'où : } \cos(a-b) = \cos a \cos b + \sin a \sin b", font_size=19),
        ).arrange(DOWN, buff=0.22, aligned_edge=LEFT)
        demo.to_edge(RIGHT, buff=0.3).shift(DOWN * 0.1)

        with self.voiceover(
            text=(
                "Démontrons la formule de cosinus de a moins b, à l'aide "
                "du produit scalaire. Soient M de a et M de b les points "
                "images de a et de b sur le cercle trigonométrique : les "
                "vecteurs O M de a et O M de b sont unitaires. On calcule "
                "leur produit scalaire de deux façons. D'abord avec les "
                "coordonnées : cosinus a, sinus a, pour le premier "
                "vecteur, cosinus b, sinus b pour le second, ce qui donne "
                "cosinus a cosinus b plus sinus a sinus b. Ensuite avec la "
                "formule du produit scalaire faisant intervenir l'angle : "
                "comme les deux vecteurs sont unitaires, leur produit "
                "scalaire vaut simplement le cosinus de l'angle orienté "
                "entre eux, c'est-à-dire cosinus de a moins b. En "
                "identifiant les deux résultats, on obtient exactement la "
                "formule annoncée. Les trois autres formules d'addition "
                "s'en déduisent, en remplaçant b par moins b, ou en "
                "utilisant sinus x égale cosinus de pi sur deux moins x."
            )
        ) as tracker:
            self.play(FadeIn(figure))
            self.play(FadeIn(demo))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(figure), FadeOut(demo))

        # --- Corollaire : tangente de a+b, a-b ---------------------------------
        corollaire = theorem_box(
            VGroup(
                Text("Corollaire : tangente d'une somme/différence", font_size=22, weight="BOLD"),
                MathTex(
                    r"\tan(a+b) = \dfrac{\tan a + \tan b}{1 - \tan a \tan b}",
                    font_size=25,
                ),
                MathTex(
                    r"\tan(a-b) = \dfrac{\tan a - \tan b}{1 + \tan a \tan b}",
                    font_size=25,
                ),
            ).arrange(DOWN, buff=0.28),
            box_width=8.5,
        )
        corollaire.next_to(titre, DOWN, buff=0.55)

        with self.voiceover(
            text=(
                "On en déduit, en divisant sinus par cosinus, deux "
                "formules pour la tangente d'une somme et d'une "
                "différence : tangente de a plus b égale tangente a plus "
                "tangente b, le tout divisé par un moins tangente a "
                "tangente b ; et tangente de a moins b égale tangente a "
                "moins tangente b, divisé par un plus tangente a tangente "
                "b."
            )
        ) as tracker:
            self.play(FadeIn(corollaire))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(corollaire))

        # --- Exemple résolu 5 -----------------------------------------------------
        exemple = example_box(
            VGroup(
                Text("Calculer cos(π/12) et sin(π/12), sachant que π/12 = π/3 - π/4.", font_size=20),
                MathTex(
                    r"\cos\!\left(\dfrac{\pi}{12}\right) = \cos\!\left(\dfrac{\pi}{3}-\dfrac{\pi}{4}\right)"
                    r" = \dfrac{1}{2}\cdot\dfrac{\sqrt{2}}{2} + \dfrac{\sqrt{3}}{2}\cdot\dfrac{\sqrt{2}}{2}"
                    r" = \dfrac{\sqrt{6}+\sqrt{2}}{4}",
                    font_size=20,
                ),
                MathTex(
                    r"\sin\!\left(\dfrac{\pi}{12}\right) = \sin\!\left(\dfrac{\pi}{3}-\dfrac{\pi}{4}\right)"
                    r" = \dfrac{\sqrt{3}}{2}\cdot\dfrac{\sqrt{2}}{2} - \dfrac{1}{2}\cdot\dfrac{\sqrt{2}}{2}"
                    r" = \dfrac{\sqrt{6}-\sqrt{2}}{4}",
                    font_size=20,
                ),
                MathTex(
                    r"\text{Vérification : } \cos^2\!\left(\tfrac{\pi}{12}\right) + \sin^2\!\left(\tfrac{\pi}{12}\right)"
                    r" = \dfrac{8+2\sqrt{12}}{16} + \dfrac{8-2\sqrt{12}}{16} = 1 \; \checkmark",
                    font_size=19,
                ),
            ).arrange(DOWN, buff=0.28),
            box_width=11.3,
        )
        exemple.next_to(titre, DOWN, buff=0.55)

        with self.voiceover(
            text=(
                "Exemple résolu. Calculons cosinus et sinus de pi douzième, "
                "sachant que pi douzième s'écrit pi tiers moins pi quart. "
                "En appliquant la formule d'addition pour le cosinus, on "
                "obtient un demi fois racine de deux sur deux, plus racine "
                "de trois sur deux fois racine de deux sur deux, soit "
                "racine de six plus racine de deux, le tout sur quatre. De "
                "même pour le sinus, on obtient racine de six moins racine "
                "de deux, sur quatre. On vérifie enfin que la somme des "
                "carrés de ces deux valeurs vaut bien un, ce qui confirme "
                "le calcul."
            )
        ) as tracker:
            self.play(FadeIn(exemple))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(exemple), FadeOut(titre))
