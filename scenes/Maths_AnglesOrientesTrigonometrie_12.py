"""
scenes/Maths_AnglesOrientesTrigonometrie_12.py — Chapitre « Angles orientés
et trigonométrie » (1ereC, Maths), scène 12.

§ Équations trigonométriques de base : cos x = a, sin x = a, tan x = a
(théorèmes + figure des solutions sur le cercle, cas particuliers).
Exemples résolus 8 (cos2x=-1/2), 9 (sin(2x+π/3)=1/2), 10 (tan3x=-1).
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
from shapes.boxes import example_box, theorem_box, scene_title


def _wrap(text: str, width: int = 56) -> str:
    return "\n".join(textwrap.fill(line, width=width) for line in text.split("\n"))


def _cercle_axes(radius=1.2):
    axe_x = Line(LEFT * radius * 1.3, RIGHT * radius * 1.3, color=GRAY_B, stroke_width=1)
    axe_y = Line(DOWN * radius * 1.3, UP * radius * 1.3, color=GRAY_B, stroke_width=1)
    cercle = Circle(radius=radius, color=WHITE, stroke_width=2)
    O = Dot(ORIGIN, color=WHITE, radius=0.03)
    return VGroup(axe_x, axe_y, cercle, O)


class EquationsTrigonometriquesBase(NotionScene):
    def construct(self):
        titre = scene_title("Équations trigonométriques de base")
        titre.scale(0.58)
        titre.to_edge(UP)

        with self.voiceover(
            text=(
                "Nous savons maintenant calculer cosinus, sinus et "
                "tangente. Étudions le problème inverse : résoudre une "
                "équation où l'inconnue est dans l'angle. Il existe trois "
                "équations de référence : cosinus x égale a, sinus x "
                "égale a, et tangente x égale a."
            )
        ) as tracker:
            self.play(Write(titre))
            self.wait(tracker.get_remaining_duration())

        # --- cos x = a ------------------------------------------------------------
        fig_cos = _cercle_axes(radius=1.15)
        pM1 = Dot(fig_cos[2].point_at_angle(0.9), color=YELLOW, radius=0.05)
        pM2 = Dot(fig_cos[2].point_at_angle(-0.9), color=YELLOW, radius=0.05)
        droite_v = Line(
            [fig_cos[2].point_at_angle(0.9)[0], -1.4, 0],
            [fig_cos[2].point_at_angle(0.9)[0], 1.4, 0],
            color=ORANGE,
            stroke_width=1.5,
        )
        fig_cos_full = VGroup(fig_cos, droite_v, pM1, pM2)

        theo_cos = theorem_box(
            VGroup(
                Text("Équation cos x = a", font_size=22, weight="BOLD"),
                Text("Si |a| > 1 : aucune solution.", font_size=19),
                Text("Si |a| ⩽ 1, avec a = cos φ :", font_size=19),
                MathTex(r"\cos x = \cos \varphi \iff x = \varphi + k2\pi \ \text{ou}\ x = -\varphi + k2\pi,\ k\in\mathbb{Z}", font_size=19),
            ).arrange(DOWN, buff=0.22),
            box_width=6.6,
        )
        theo_cos.to_edge(LEFT, buff=0.4).shift(DOWN * 0.2)
        fig_cos_full.next_to(theo_cos, RIGHT, buff=0.5)

        with self.voiceover(
            text=(
                "Premier cas : cosinus x égale a. Si la valeur absolue de "
                "a dépasse un, aucune solution, puisque le cosinus reste "
                "toujours entre moins un et un. Sinon, en écrivant a "
                "égale cosinus phi, les solutions sont x égale phi plus k "
                "deux pi, ou x égale moins phi plus k deux pi, k entier "
                "relatif : géométriquement, ce sont les deux points du "
                "cercle symétriques par rapport à l'axe (OI)."
            )
        ) as tracker:
            self.play(FadeIn(theo_cos))
            self.play(FadeIn(fig_cos_full))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(theo_cos), FadeOut(fig_cos_full))

        # --- sin x = a --------------------------------------------------------------
        fig_sin = _cercle_axes(radius=1.15)
        pN1 = Dot(fig_sin[2].point_at_angle(0.7), color=GREEN, radius=0.05)
        pN2 = Dot(fig_sin[2].point_at_angle(3.14159 - 0.7), color=GREEN, radius=0.05)
        droite_h = Line(
            [-1.4, fig_sin[2].point_at_angle(0.7)[1], 0],
            [1.4, fig_sin[2].point_at_angle(0.7)[1], 0],
            color=ORANGE,
            stroke_width=1.5,
        )
        fig_sin_full = VGroup(fig_sin, droite_h, pN1, pN2)

        theo_sin = theorem_box(
            VGroup(
                Text("Équation sin x = a", font_size=22, weight="BOLD"),
                Text("Si |a| > 1 : aucune solution.", font_size=19),
                Text("Si |a| ⩽ 1, avec a = sin φ :", font_size=19),
                MathTex(r"\sin x = \sin \varphi \iff x = \varphi + k2\pi \ \text{ou}\ x = \pi - \varphi + k2\pi,\ k\in\mathbb{Z}", font_size=18),
            ).arrange(DOWN, buff=0.22),
            box_width=6.6,
        )
        theo_sin.to_edge(LEFT, buff=0.4).shift(DOWN * 0.2)
        fig_sin_full.next_to(theo_sin, RIGHT, buff=0.5)

        with self.voiceover(
            text=(
                "Deuxième cas : sinus x égale a. Même condition "
                "d'existence, valeur absolue de a inférieure ou égale à "
                "un. En écrivant a égale sinus phi, les solutions sont x "
                "égale phi plus k deux pi, ou x égale pi moins phi plus k "
                "deux pi. Géométriquement, ce sont cette fois les deux "
                "points du cercle symétriques par rapport à l'axe (OJ)."
            )
        ) as tracker:
            self.play(FadeIn(theo_sin))
            self.play(FadeIn(fig_sin_full))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(theo_sin), FadeOut(fig_sin_full))

        # --- tan x = a ---------------------------------------------------------------
        theo_tan = theorem_box(
            VGroup(
                Text("Équation tan x = a", font_size=22, weight="BOLD"),
                Text("Toujours au moins une solution (a quelconque), avec a = tan φ :", font_size=19),
                MathTex(r"\tan x = \tan \varphi \iff x = \varphi + k\pi,\ k \in \mathbb{Z}", font_size=24),
            ).arrange(DOWN, buff=0.25),
            box_width=9.5,
        )
        theo_tan.next_to(titre, DOWN, buff=0.55)

        with self.voiceover(
            text=(
                "Troisième cas : tangente x égale a. Ici, a peut être "
                "n'importe quel réel, la tangente prenant toutes les "
                "valeurs réelles. En écrivant a égale tangente phi, "
                "l'ensemble des solutions est x égale phi plus k pi, k "
                "entier relatif : une seule famille de solutions, "
                "espacées de pi et non de deux pi, car la tangente est "
                "pi-périodique."
            )
        ) as tracker:
            self.play(FadeIn(theo_tan))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(theo_tan))

        # --- Cas particuliers ------------------------------------------------------
        cas_part = theorem_box(
            VGroup(
                Text("Cas particuliers utiles", font_size=21, weight="BOLD"),
                MathTex(r"\cos x = 1 \iff x = k2\pi \qquad \cos x = -1 \iff x = \pi + k2\pi", font_size=18),
                MathTex(r"\cos x = 0 \iff x = \tfrac{\pi}{2} + k\pi \qquad \sin x = 0 \iff x = k\pi", font_size=18),
                MathTex(r"\sin x = 1 \iff x = \tfrac{\pi}{2} + k2\pi \qquad \sin x = -1 \iff x = -\tfrac{\pi}{2} + k2\pi", font_size=18),
            ).arrange(DOWN, buff=0.22),
            box_width=10.5,
        )
        cas_part.next_to(titre, DOWN, buff=0.55)

        with self.voiceover(
            text=(
                "Quelques cas particuliers reviennent très souvent, à "
                "connaître directement : cosinus x égale un équivaut à x "
                "égale k deux pi ; cosinus x égale moins un équivaut à x "
                "égale pi plus k deux pi ; cosinus x égale zéro équivaut à "
                "x égale pi sur deux plus k pi ; sinus x égale zéro "
                "équivaut à x égale k pi ; sinus x égale un équivaut à x "
                "égale pi sur deux plus k deux pi ; et sinus x égale moins "
                "un équivaut à x égale moins pi sur deux plus k deux pi."
            )
        ) as tracker:
            self.play(FadeIn(cas_part))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(cas_part))

        # --- Exemples résolus 8, 9, 10 -----------------------------------------------
        ex8 = example_box(
            VGroup(
                Text("Résoudre cos 2x = -1/2 dans ℝ.", font_size=20),
                MathTex(
                    r"\cos 2x = -\dfrac{1}{2} = \cos\!\left(\dfrac{2\pi}{3}\right)"
                    r" \iff 2x = \dfrac{2\pi}{3} + k2\pi \ \text{ou} \ 2x = -\dfrac{2\pi}{3} + k2\pi",
                    font_size=18,
                ),
                MathTex(
                    r"\iff x = \dfrac{\pi}{3} + k\pi \ \text{ou} \ x = -\dfrac{\pi}{3} + k\pi,\ k \in \mathbb{Z}",
                    font_size=20,
                ),
            ).arrange(DOWN, buff=0.25),
            box_width=10.8,
        )
        ex8.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Exemple résolu huit. Résolvons cosinus de deux x égale "
                "moins un demi. On reconnaît moins un demi comme cosinus "
                "de deux pi tiers. On obtient deux x égale deux pi tiers "
                "plus k deux pi, ou deux x égale moins deux pi tiers plus "
                "k deux pi. En divisant tout par deux, attention, on "
                "divise aussi la période : x égale pi tiers plus k pi, ou "
                "x égale moins pi tiers plus k pi, k entier relatif."
            )
        ) as tracker:
            self.play(FadeIn(ex8))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(ex8))

        ex9 = example_box(
            VGroup(
                Text("Résoudre sin(2x + π/3) = 1/2 dans ℝ.", font_size=20),
                MathTex(
                    r"\sin\!\left(2x+\dfrac{\pi}{3}\right) = \dfrac{1}{2} = \sin\!\left(\dfrac{\pi}{6}\right)",
                    font_size=20,
                ),
                MathTex(
                    r"\iff 2x+\dfrac{\pi}{3} = \dfrac{\pi}{6} + k2\pi \ \text{ou} \ 2x+\dfrac{\pi}{3} = \pi - \dfrac{\pi}{6} + k2\pi",
                    font_size=18,
                ),
                MathTex(
                    r"\iff x = -\dfrac{\pi}{12} + k\pi \ \text{ou} \ x = \dfrac{\pi}{4} + k\pi,\ k \in \mathbb{Z}",
                    font_size=20,
                ),
            ).arrange(DOWN, buff=0.22),
            box_width=10.8,
        )
        ex9.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Exemple résolu neuf. Résolvons sinus de deux x plus pi "
                "tiers égale un demi. On reconnaît un demi comme sinus de "
                "pi sixième. On obtient deux x plus pi tiers égale pi "
                "sixième plus k deux pi, ou deux x plus pi tiers égale pi "
                "moins pi sixième, c'est-à-dire cinq pi sixièmes, plus k "
                "deux pi. En isolant x puis en divisant par deux, on "
                "obtient x égale moins pi douzième plus k pi, ou x égale "
                "pi quart plus k pi, k entier relatif."
            )
        ) as tracker:
            self.play(FadeIn(ex9))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(ex9))

        ex10 = example_box(
            VGroup(
                Text("Résoudre tan 3x = -1 dans ℝ.", font_size=21),
                MathTex(
                    r"\tan 3x = -1 = \tan\!\left(-\dfrac{\pi}{4}\right)"
                    r" \iff 3x = -\dfrac{\pi}{4} + k\pi",
                    font_size=21,
                ),
                MathTex(r"\iff x = -\dfrac{\pi}{12} + \dfrac{k\pi}{3},\ k \in \mathbb{Z}", font_size=22),
            ).arrange(DOWN, buff=0.28),
            box_width=9.5,
        )
        ex10.next_to(titre, DOWN, buff=0.55)

        with self.voiceover(
            text=(
                "Exemple résolu dix. Résolvons tangente de trois x égale "
                "moins un. On reconnaît moins un comme tangente de moins "
                "pi quart. On obtient trois x égale moins pi quart plus k "
                "pi, une seule famille puisqu'il s'agit d'une tangente. En "
                "divisant par trois, x égale moins pi douzième plus k pi "
                "tiers, k entier relatif."
            )
        ) as tracker:
            self.play(FadeIn(ex10))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(ex10), FadeOut(titre))
