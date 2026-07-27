"""
scenes/Physique_EnergiePotentielle_01.py — Chapitre 4 « Énergie potentielle »
(1ereC, Physique), scène 01.

Notion d'énergie potentielle : situations d'accroche (barrage de Buyo,
pierre soulevée, ressort comprimé d'un pistolet à bouchon), définition
générale, remarques (référence arbitraire, deux énergies potentielles au
programme).
Source : 1ereC/Physique.pdf, chapitre 4, pages 34-42.
"""

import textwrap

from manim import (
    BLUE_E,
    DOWN,
    GREY_BROWN,
    LEFT,
    ORANGE,
    RIGHT,
    UP,
    WHITE,
    YELLOW,
    Circle,
    FadeIn,
    FadeOut,
    Line,
    Rectangle,
    Text,
    VGroup,
    Write,
)

from shapes.base_scene import NotionScene
from shapes.boxes import definition_box, essentiel_box, scene_title, warning_box


def _wrap(text: str, width: int = 56) -> str:
    return "\n".join(textwrap.fill(line, width=width) for line in text.split("\n"))


def _barrage():
    """Schéma simplifié d'un barrage : mur + retenue d'eau en amont."""
    mur = Rectangle(width=1.0, height=2.2, color=GREY_BROWN, fill_color=GREY_BROWN, fill_opacity=1.0)
    eau = Rectangle(width=2.0, height=1.6, color=BLUE_E, fill_color=BLUE_E, fill_opacity=1.0)
    eau.next_to(mur, LEFT, buff=0).align_to(mur, DOWN)
    sol = Line(LEFT * 1.6, RIGHT * 0.6, color=WHITE)
    sol.next_to(VGroup(mur, eau), DOWN, buff=0)
    return VGroup(eau, mur, sol)


def _pierre():
    """Une pierre (disque) tenue en hauteur, au-dessus du sol."""
    sol = Line(LEFT * 1.0, RIGHT * 1.0, color=WHITE)
    pierre = Circle(radius=0.25, color=GREY_BROWN, fill_color=GREY_BROWN, fill_opacity=1.0)
    pierre.move_to(sol.get_center() + UP * 1.6)
    return VGroup(sol, pierre)


def _ressort_comprime():
    """Ressort comprimé (zigzag court) contre un bouchon, dans un tube."""
    tube = Rectangle(width=2.2, height=0.6, color=WHITE)
    points = [tube.get_left() + RIGHT * 0.1]
    n = 6
    for i in range(1, n):
        x = 0.1 + i * (0.7 / n)
        y = 0.15 if i % 2 else -0.15
        points.append(tube.get_left() + RIGHT * x + UP * y)
    points.append(tube.get_left() + RIGHT * 0.8)
    ressort = VGroup(*[Line(points[i], points[i + 1], color=ORANGE) for i in range(len(points) - 1)])
    bouchon = Rectangle(width=0.25, height=0.5, color=YELLOW, fill_color=YELLOW, fill_opacity=1.0)
    bouchon.move_to(tube.get_left() + RIGHT * 0.9)
    return VGroup(tube, ressort, bouchon)


class NotionEnergiePotentielle(NotionScene):
    def construct(self):
        titre = scene_title("Notion d'énergie potentielle")
        titre.scale(0.55)
        titre.to_edge(UP)

        # --- Énoncé : trois situations d'accroche ------------------------------
        barrage = _barrage().scale(0.9)
        pierre = _pierre().scale(0.9)
        ressort = _ressort_comprime().scale(0.9)

        legende_barrage = Text("Barrage de Buyo", font_size=20)
        legende_pierre = Text("Pierre soulevée", font_size=20)
        legende_ressort = Text("Ressort comprimé", font_size=20)

        groupe1 = VGroup(barrage, legende_barrage.next_to(barrage, DOWN, buff=0.25))
        groupe2 = VGroup(pierre, legende_pierre.next_to(pierre, DOWN, buff=0.25))
        groupe3 = VGroup(ressort, legende_ressort.next_to(ressort, DOWN, buff=0.25))

        situations = VGroup(groupe1, groupe2, groupe3).arrange(RIGHT, buff=1.1)
        situations.next_to(titre, DOWN, buff=0.8)

        with self.voiceover(
            text=(
                "Observons trois situations bien concrètes. L'eau retenue "
                "en amont du barrage de Buyo, une pierre que l'on tient en "
                "l'air, et le ressort comprimé d'un pistolet à bouchon. "
                "Dans chacun de ces cas, rien ne bouge pour l'instant, et "
                "pourtant, chaque système est prêt à libérer de l'énergie : "
                "l'eau peut faire tourner une turbine, la pierre peut "
                "tomber, le ressort peut détendre brutalement le bouchon."
            )
        ) as tracker:
            self.play(FadeIn(groupe1))
            self.play(FadeIn(groupe2))
            self.play(FadeIn(groupe3))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(situations))

        # --- Raisonnement : point commun ---------------------------------------
        question = Text(
            _wrap(
                "Point commun : dans les trois cas, une énergie est "
                "« en réserve », liée à la position ou à la configuration "
                "du système, prête à se transformer.",
                width=52,
            ),
            font_size=26,
        )
        question.next_to(titre, DOWN, buff=0.7)

        with self.voiceover(
            text=(
                "Le point commun entre ces trois situations, c'est qu'une "
                "certaine quantité d'énergie est déjà présente dans le "
                "système, mise en réserve du fait de sa position — l'eau en "
                "hauteur, la pierre en l'air — ou de sa configuration — le "
                "ressort comprimé. Cette énergie ne demande qu'à se "
                "transformer en une autre forme d'énergie, en général de "
                "l'énergie cinétique. C'est précisément cette énergie mise "
                "en réserve que l'on appelle énergie potentielle."
            )
        ) as tracker:
            self.play(Write(question))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(question))

        # --- Définition ----------------------------------------------------------
        definition = definition_box(
            Text(
                _wrap(
                    "L'énergie potentielle est l'énergie que possède un "
                    "système du fait de sa position ou de sa configuration. "
                    "Elle est susceptible de se transformer en d'autres "
                    "formes d'énergie (le plus souvent en énergie "
                    "cinétique).",
                    width=54,
                ),
                font_size=24,
            ),
            box_width=11.2,
        )
        definition.next_to(titre, DOWN, buff=0.6)

        with self.voiceover(
            text=(
                "Retenons la définition générale : l'énergie potentielle "
                "est l'énergie que possède un système du fait de sa "
                "position, ou de sa configuration. Elle est susceptible de "
                "se transformer en d'autres formes d'énergie, le plus "
                "souvent en énergie cinétique."
            )
        ) as tracker:
            self.play(FadeIn(definition))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(definition))

        # --- Remarques -------------------------------------------------------
        remarque = warning_box(
            Text(
                _wrap(
                    "L'énergie potentielle est définie à une constante "
                    "près : on choisit une référence arbitraire où Ep=0. "
                    "Seules ses variations ont un sens physique. Au "
                    "programme : deux énergies potentielles, celle de "
                    "pesanteur et celle élastique.",
                    width=54,
                ),
                font_size=23,
            ),
            box_width=11.4,
        )
        remarque.next_to(titre, DOWN, buff=0.6)

        with self.voiceover(
            text=(
                "Deux remarques importantes. D'abord, l'énergie "
                "potentielle est définie à une constante près : on choisit "
                "toujours une référence arbitraire pour laquelle l'énergie "
                "potentielle vaut zéro. Seules les variations d'énergie "
                "potentielle ont un sens physique réel. Ensuite, au "
                "programme de cette année, nous étudierons deux énergies "
                "potentielles : l'énergie potentielle de pesanteur, et "
                "l'énergie potentielle élastique."
            )
        ) as tracker:
            self.play(FadeIn(remarque))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(remarque))

        # --- À retenir -----------------------------------------------------------
        retenir = essentiel_box(
            Text(
                _wrap(
                    "Énergie potentielle : énergie « en réserve » liée à la "
                    "position ou à la configuration d'un système, "
                    "convertible en une autre forme d'énergie. Définie à "
                    "une constante près : seule sa variation compte.",
                    width=56,
                ),
                font_size=23,
            )
        )
        retenir.next_to(titre, DOWN, buff=0.6)

        with self.voiceover(
            text=(
                "À retenir : l'énergie potentielle est une énergie en "
                "réserve, liée à la position ou à la configuration d'un "
                "système, et convertible en une autre forme d'énergie. "
                "Elle est définie à une constante près : c'est sa variation "
                "qui compte physiquement. Dans la scène suivante, nous "
                "allons mettre en évidence la première de ces deux énergies "
                "potentielles : l'énergie potentielle de pesanteur."
            )
        ) as tracker:
            self.play(FadeIn(retenir))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(titre), FadeOut(retenir))
