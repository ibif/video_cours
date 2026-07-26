"""
scenes/Maths_AnglesOrientesTrigonometrie_03.py — Chapitre « Angles orientés
et trigonométrie » (1ereC, Maths), scène 03.

§ Angle orienté de deux vecteurs : rappel, mesures d'un angle orienté
(α + k2π), mesure principale (dans ]-π;π]), exemple résolu (mesure
principale de -119π/6).
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
    Arc,
    FadeIn,
    FadeOut,
    MathTex,
    Text,
    VGroup,
    Vector,
    Write,
)

from shapes.base_scene import NotionScene
from shapes.boxes import definition_box, example_box, scene_title


def _wrap(text: str, width: int = 56) -> str:
    return "\n".join(textwrap.fill(line, width=width) for line in text.split("\n"))


class AngleOrienteMesures(NotionScene):
    def construct(self):
        titre = scene_title("Angle orienté de deux vecteurs : mesures")
        titre.scale(0.55)
        titre.to_edge(UP)

        # --- Énoncé : rappel angle orienté -----------------------------------
        vecteur_u = Vector(RIGHT * 1.8, color=YELLOW)
        vecteur_v = Vector([1.8 * 0.5, 1.8 * 0.866, 0], color=GREEN)
        label_u = MathTex(r"\vec{u}", font_size=26, color=YELLOW).next_to(vecteur_u, DOWN, buff=0.1)
        label_v = MathTex(r"\vec{v}", font_size=26, color=GREEN).next_to(vecteur_v, UP + LEFT, buff=0.05)
        arc_angle = Arc(radius=0.7, start_angle=0, angle=1.047, color=WHITE, stroke_width=2)
        label_angle = MathTex(r"(\vec{u}, \vec{v})", font_size=22, color=WHITE).move_to(
            [0.9 * 0.94, 0.9 * 0.34, 0]
        )
        figure = VGroup(vecteur_u, vecteur_v, label_u, label_v, arc_angle, label_angle)
        figure.move_to(ORIGIN).shift(LEFT * 3.5 + DOWN * 0.3)

        rappel = Text(
            _wrap(
                "Le plan étant orienté, à tout couple de vecteurs non nuls "
                "(u⃗, v⃗) on associe un angle orienté, noté (u⃗, v⃗), qui "
                "tient compte du sens dans lequel on tourne de u⃗ vers v⃗.",
                width=42,
            ),
            font_size=22,
            color=WHITE,
        )
        rappel.to_edge(RIGHT, buff=0.4)

        with self.voiceover(
            text=(
                "Le plan étant orienté par le sens direct défini "
                "précédemment, on associe à tout couple de vecteurs non "
                "nuls u vecteur, v vecteur, un angle orienté, noté "
                "parenthèse u vecteur, v vecteur fermée parenthèse, qui "
                "tient compte du sens dans lequel on tourne pour amener "
                "u vecteur sur v vecteur."
            )
        ) as tracker:
            self.play(Write(titre))
            self.play(FadeIn(figure))
            self.play(FadeIn(rappel))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(figure), FadeOut(rappel))

        # --- Raisonnement : mesures d'un angle orienté -----------------------
        def_mesures = definition_box(
            VGroup(
                Text("Mesures d'un angle orienté", font_size=25, weight="BOLD"),
                Text(
                    _wrap(
                        "Si α est une mesure en radians de l'angle orienté "
                        "(u⃗, v⃗), alors tous les réels de la forme α+k×2π, "
                        "k∈ℤ, sont aussi des mesures de ce même angle "
                        "orienté : l'angle a une infinité de mesures, "
                        "toutes congrues entre elles modulo 2π.",
                        width=48,
                    ),
                    font_size=21,
                ),
                MathTex(r"(\vec{u}, \vec{v}) = \alpha + k \times 2\pi,\quad k \in \mathbb{Z}", font_size=26),
            ).arrange(DOWN, buff=0.25),
            box_width=10.5,
        )
        def_mesures.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Un angle orienté n'a pas une seule mesure, mais une "
                "infinité. Si alpha est une mesure en radians de l'angle "
                "orienté u vecteur, v vecteur, alors tous les réels de la "
                "forme alpha plus k fois deux pi, avec k entier relatif, "
                "sont aussi des mesures de ce même angle orienté : ajouter "
                "ou retirer un tour complet ne change pas la position "
                "finale."
            )
        ) as tracker:
            self.play(FadeIn(def_mesures))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(def_mesures))

        # --- La mesure principale ---------------------------------------------
        def_principale = definition_box(
            VGroup(
                Text("Mesure principale", font_size=25, weight="BOLD"),
                Text(
                    _wrap(
                        "Parmi toutes les mesures d'un angle orienté "
                        "(u⃗, v⃗), une seule appartient à l'intervalle "
                        "]-π ; π]. C'est la mesure principale de l'angle "
                        "orienté (u⃗, v⃗).",
                        width=48,
                    ),
                    font_size=21,
                ),
            ).arrange(DOWN, buff=0.25),
            box_width=10,
        )
        def_principale.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Parmi toutes ces mesures, une seule appartient à "
                "l'intervalle ouvert à gauche en moins pi, fermé à droite "
                "en pi, c'est-à-dire l'intervalle ]-π ; π]. On l'appelle "
                "la mesure principale de l'angle orienté."
            )
        ) as tracker:
            self.play(FadeIn(def_principale))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(def_principale))

        # --- Exemple résolu 2 --------------------------------------------------
        exemple = example_box(
            VGroup(
                Text(
                    "Déterminer la mesure principale de l'angle de mesure -119π/6.",
                    font_size=21,
                ),
                MathTex(
                    r"-\dfrac{119\pi}{6} = -\dfrac{119\pi}{6} + 10 \times 2\pi = -\dfrac{119\pi}{6} + \dfrac{120\pi}{6} = \dfrac{\pi}{6}",
                    font_size=23,
                ),
                Text(
                    "Comme π/6 appartient à ]-π ; π], la mesure principale est π/6.",
                    font_size=21,
                ),
            ).arrange(DOWN, buff=0.3),
            box_width=11,
        )
        exemple.next_to(titre, DOWN, buff=0.55)

        with self.voiceover(
            text=(
                "Exemple résolu. Déterminons la mesure principale de "
                "l'angle de mesure moins cent dix-neuf pi sixièmes. On "
                "cherche l'entier k tel que moins cent dix-neuf pi "
                "sixièmes plus k fois deux pi tombe dans l'intervalle "
                "]-π ; π]. En ajoutant dix fois deux pi, soit cent vingt "
                "pi sixièmes, on obtient moins cent dix-neuf pi sixièmes "
                "plus cent vingt pi sixièmes, c'est-à-dire pi sixième. "
                "Comme pi sixième appartient bien à l'intervalle "
                "]-π ; π], la mesure principale cherchée est pi sixième."
            )
        ) as tracker:
            self.play(FadeIn(exemple))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(exemple), FadeOut(titre))
