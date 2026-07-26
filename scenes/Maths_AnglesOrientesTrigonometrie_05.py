"""
scenes/Maths_AnglesOrientesTrigonometrie_05.py — Chapitre « Angles orientés
et trigonométrie » (1ereC, Maths), scène 05.

§ Cosinus et sinus d'un nombre réel : définition (abscisse/ordonnée du
point image), propriétés fondamentales (cos²x+sin²x=1, bornes, périodicité
2π) avec démonstration.
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


class CosinusSinusNombreReel(NotionScene):
    def construct(self):
        titre = scene_title("Cosinus et sinus d'un nombre réel")
        titre.scale(0.6)
        titre.to_edge(UP)

        # --- Énoncé : définition -------------------------------------------
        fig = _cercle_axes(radius=1.6)
        fig.to_edge(LEFT, buff=0.6).shift(DOWN * 0.2)
        point_m = Dot(fig[5].get_center() + [1.6 * 0.62, 1.6 * 0.78, 0], color="#DE7C1F", radius=0.06)
        label_m = MathTex("M(x)", font_size=22, color="#DE7C1F").next_to(point_m, UP, buff=0.08)
        proj_cos = Line(point_m.get_center(), [point_m.get_center()[0], fig[5].get_center()[1], 0], color=YELLOW, stroke_width=2)
        proj_sin = Line(point_m.get_center(), [fig[5].get_center()[0], point_m.get_center()[1], 0], color=GREEN, stroke_width=2)
        label_cos = MathTex(r"\cos x", font_size=20, color=YELLOW).next_to(proj_cos, DOWN, buff=0.08)
        label_sin = MathTex(r"\sin x", font_size=20, color=GREEN).next_to(proj_sin, LEFT, buff=0.08)
        figure = VGroup(fig, point_m, label_m, proj_cos, proj_sin, label_cos, label_sin)

        definition = definition_box(
            VGroup(
                Text("Cosinus et sinus de x", font_size=24, weight="BOLD"),
                Text(
                    _wrap(
                        "Soit M(x) le point image du réel x sur le cercle "
                        "trigonométrique, dans un repère (O ; I, J). "
                        "L'abscisse de M(x) est le cosinus de x, notée "
                        "cos x. L'ordonnée de M(x) est le sinus de x, "
                        "notée sin x.",
                        width=40,
                    ),
                    font_size=20,
                ),
            ).arrange(DOWN, buff=0.25),
            box_width=6.6,
        )
        definition.to_edge(RIGHT, buff=0.4).shift(DOWN * 0.2)

        with self.voiceover(
            text=(
                "Le plan étant muni du repère orthonormé O, I, J, on peut "
                "maintenant définir précisément le cosinus et le sinus "
                "d'un nombre réel x. Soit M de x le point image de x sur "
                "le cercle trigonométrique. Par définition, l'abscisse de "
                "M de x est le cosinus de x, noté cos x, et l'ordonnée de "
                "M de x est le sinus de x, noté sin x."
            )
        ) as tracker:
            self.play(Write(titre))
            self.play(FadeIn(figure))
            self.play(FadeIn(definition))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(figure), FadeOut(definition))

        # --- Raisonnement : propriétés fondamentales avec démonstration -----
        proprietes = property_box(
            VGroup(
                Text("Propriétés fondamentales", font_size=24, weight="BOLD"),
                MathTex(r"\cos^2 x + \sin^2 x = 1", font_size=27),
                MathTex(r"-1 \leqslant \cos x \leqslant 1 \quad\text{et}\quad -1 \leqslant \sin x \leqslant 1", font_size=25),
                MathTex(r"\cos(x + 2\pi) = \cos x \quad\text{et}\quad \sin(x + 2\pi) = \sin x", font_size=25),
            ).arrange(DOWN, buff=0.28),
            box_width=10,
        )
        proprietes.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Ces définitions entraînent trois propriétés fondamentales. "
                "D'abord, cosinus carré de x plus sinus carré de x vaut "
                "toujours un. Ensuite, le cosinus et le sinus sont "
                "toujours compris entre moins un et un. Enfin, cosinus et "
                "sinus sont périodiques, de période deux pi : ajouter deux "
                "pi à x ne change ni son cosinus, ni son sinus."
            )
        ) as tracker:
            self.play(FadeIn(proprietes))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(proprietes))

        # --- Démonstration -----------------------------------------------------
        demo = VGroup(
            Text("Démonstration", font_size=24, color=YELLOW, weight="BOLD"),
            Text(
                _wrap(
                    "M(x) appartient au cercle trigonométrique, de rayon 1 "
                    "et de centre O : on a donc OM(x) = 1, c'est-à-dire "
                    "OM(x)² = 1.",
                    width=54,
                ),
                font_size=20,
            ),
            MathTex(
                r"OM(x)^2 = (\cos x - 0)^2 + (\sin x - 0)^2 = \cos^2 x + \sin^2 x",
                font_size=24,
            ),
            MathTex(r"\text{donc} \quad \cos^2 x + \sin^2 x = 1", font_size=24),
            Text(
                _wrap(
                    "Comme un carré est positif, cos²x ⩽ 1 et sin²x ⩽ 1, "
                    "d'où -1 ⩽ cos x ⩽ 1 et -1 ⩽ sin x ⩽ 1. Enfin, M(x) et "
                    "M(x+2π) sont le même point du cercle (propriété de la "
                    "scène 2), donc ils ont même abscisse et même "
                    "ordonnée : cos et sin sont 2π-périodiques.",
                    width=54,
                ),
                font_size=20,
            ),
        ).arrange(DOWN, buff=0.3, aligned_edge=LEFT)
        demo.next_to(titre, DOWN, buff=0.55)

        with self.voiceover(
            text=(
                "Démontrons ces propriétés. Le point M de x appartient au "
                "cercle trigonométrique, de rayon un et de centre O : la "
                "distance O M de x vaut donc un, et son carré vaut aussi "
                "un. Or, par la formule de la distance dans un repère "
                "orthonormé, O M de x au carré est égal à cosinus carré "
                "de x plus sinus carré de x, puisque O a pour coordonnées "
                "zéro, zéro et M de x a pour coordonnées cosinus de x, "
                "sinus de x. On obtient donc bien cosinus carré de x plus "
                "sinus carré de x égale un. Comme un carré est toujours "
                "positif ou nul, chacun des deux carrés est inférieur ou "
                "égal à un, ce qui donne l'encadrement de cos x et de "
                "sin x entre moins un et un. Enfin, on a vu que M de x et "
                "M de x plus deux pi désignent exactement le même point du "
                "cercle : ils ont donc la même abscisse et la même "
                "ordonnée, ce qui prouve la périodicité de cosinus et de "
                "sinus, de période deux pi."
            )
        ) as tracker:
            self.play(FadeIn(demo))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(demo))

        # --- À retenir / piège --------------------------------------------------
        piege = property_box(
            Text(
                _wrap(
                    "À retenir : cos x et sin x sont définis pour TOUT réel "
                    "x (le point image existe toujours), contrairement à "
                    "la tangente qui sera définie sous condition à la "
                    "scène suivante.",
                    width=50,
                ),
                font_size=22,
            ),
            box_width=9.5,
        )
        piege.next_to(titre, DOWN, buff=0.6)

        with self.voiceover(
            text=(
                "Point important à retenir avant de poursuivre : le "
                "cosinus et le sinus sont définis pour tout réel x, sans "
                "aucune exception, car le point image existe toujours. Ce "
                "ne sera plus le cas pour la tangente, que nous allons "
                "définir dans la scène suivante, et qui nécessite une "
                "condition sur x."
            )
        ) as tracker:
            self.play(FadeIn(piege))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(piege), FadeOut(titre))
