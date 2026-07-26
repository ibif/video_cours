"""
scenes/Chimie_GeneralitesComposesOrganiques_09.py — Chapitre 1 (1ereC, Chimie), scène 09.

§ 5 Les chaînes carbonées : définition + les 3 types (linéaire, ramifiée,
cyclique) avec exemples (pentane/propène, 2-méthylbutane, cyclohexane) et
schéma en formule topologique. Source : 1ereC/Chimie.pdf, page 9.
"""

import textwrap

import numpy as np

from manim import (
    DOWN,
    LEFT,
    RIGHT,
    UP,
    WHITE,
    YELLOW,
    BLUE,
    FadeIn,
    FadeOut,
    Line,
    MathTex,
    Text,
    VGroup,
    Write,
    config,
)

from shapes.base_scene import NotionScene
from shapes.boxes import definition_box, example_box, scene_title


def _wrap(text: str, width: int = 56) -> str:
    return "\n".join(textwrap.fill(line, width=width) for line in text.split("\n"))


def _fit(mobject, top_y):
    bas_visible = -config.frame_height / 2 + 0.25
    hauteur_dispo = top_y - bas_visible
    if mobject.height > hauteur_dispo:
        mobject.scale(hauteur_dispo / mobject.height, about_point=mobject.get_top())
    return mobject


def _zigzag(n_sommets, dy=0.35):
    """Ligne brisée topologique de n_sommets atomes de carbone."""
    points = []
    for k in range(n_sommets):
        y = dy if k % 2 == 0 else -dy
        points.append(np.array([k * 0.55, y, 0]))
    segments = VGroup(*[Line(points[i], points[i + 1], color=WHITE, stroke_width=4) for i in range(n_sommets - 1)])
    return segments, points


def _pentane_topo():
    segments, _ = _zigzag(5)
    return segments


def _ramifiee_topo():
    # chaîne principale de 4 sommets + une ramification sur le 2e sommet
    segments, points = _zigzag(4)
    branche = Line(points[1], points[1] + np.array([0.28, 0.6, 0]), color=WHITE, stroke_width=4)
    return VGroup(segments, branche)


def _cyclohexane_topo():
    n = 6
    rayon = 0.55
    sommets = [
        np.array([rayon * np.cos(2 * np.pi * k / n + np.pi / 6), rayon * np.sin(2 * np.pi * k / n + np.pi / 6), 0])
        for k in range(n)
    ]
    return VGroup(*[Line(sommets[k], sommets[(k + 1) % n], color=WHITE, stroke_width=4) for k in range(n)])


class ChainesCarbonees(NotionScene):
    def construct(self):
        titre = scene_title("5. Les chaînes carbonées")
        titre.scale(0.6)
        titre.to_edge(UP)

        # --- Énoncé : définition -------------------------------------------------
        definition = definition_box(
            Text(
                _wrap(
                    "On appelle chaîne carbonée l'enchaînement des atomes "
                    "de carbone dans une molécule organique.",
                    width=48,
                ),
                font_size=26,
            ),
        )
        definition.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "On appelle chaîne carbonée l'enchaînement des atomes de "
                "carbone dans une molécule organique. On distingue trois "
                "types de chaînes carbonées."
            )
        ) as tracker:
            self.play(Write(titre))
            self.play(FadeIn(definition))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(definition))

        # --- Animation du raisonnement : les 3 types, en topologique -----------
        entete = Text("Les trois types de chaînes carbonées", font_size=24, color=YELLOW, weight="BOLD")
        entete.next_to(titre, DOWN, buff=0.4)

        lin = _pentane_topo()
        label_lin = Text("linéaire\n(pentane)", font_size=17, color=WHITE)
        bloc_lin = VGroup(lin, label_lin).arrange(DOWN, buff=0.3)

        ram = _ramifiee_topo()
        label_ram = Text("ramifiée\n(2-méthylbutane)", font_size=17, color=WHITE)
        bloc_ram = VGroup(ram, label_ram).arrange(DOWN, buff=0.3)

        cyc = _cyclohexane_topo()
        label_cyc = Text("cyclique\n(cyclohexane)", font_size=17, color=WHITE)
        bloc_cyc = VGroup(cyc, label_cyc).arrange(DOWN, buff=0.3)

        schema = VGroup(bloc_lin, bloc_ram, bloc_cyc).arrange(RIGHT, buff=1.1, aligned_edge=DOWN)
        schema.next_to(entete, DOWN, buff=0.5)
        _fit(schema, entete.get_bottom()[1] - 0.4)

        groupe_schema = VGroup(entete, schema)

        with self.voiceover(
            text=(
                "Dans une chaîne linéaire, les atomes de carbone sont "
                "enchaînés les uns à la suite des autres, sans "
                "embranchement, comme dans le pentane. Dans une chaîne "
                "ramifiée, la chaîne principale porte une ou plusieurs "
                "ramifications, comme dans le deux-méthylbutane. Dans une "
                "chaîne cyclique, les atomes de carbone forment un cycle, "
                "un anneau, comme dans le cyclohexane."
            )
        ) as tracker:
            self.play(FadeIn(entete))
            self.play(FadeIn(bloc_lin))
            self.play(FadeIn(bloc_ram))
            self.play(FadeIn(bloc_cyc))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(groupe_schema))

        # --- Exemple traité : formules semi-développées + saturée/insaturée ----
        exemple = example_box(
            VGroup(
                MathTex(r"\text{pentane : } CH_3-CH_2-CH_2-CH_2-CH_3", font_size=24),
                MathTex(r"\text{propène (insaturé) : } CH_2=CH-CH_3", font_size=24),
                MathTex(r"\text{2-méthylbutane : } CH_3-CH(CH_3)-CH_2-CH_3", font_size=24),
                MathTex(r"\text{cyclohexane : } C_6H_{12}", font_size=24),
            ).arrange(DOWN, buff=0.32, aligned_edge=LEFT),
            box_width=11.0,
        )
        exemple.next_to(titre, DOWN, buff=0.4)
        _fit(exemple, titre.get_bottom()[1] - 0.4)

        with self.voiceover(
            text=(
                "Une chaîne linéaire peut être saturée, avec uniquement "
                "des liaisons simples, comme le pentane, ou insaturée, "
                "avec une liaison double ou triple, comme le propène. Le "
                "deux-méthylbutane illustre la chaîne ramifiée, avec son "
                "groupe méthyle en position deux. Et le cyclohexane, de "
                "formule brute C six H douze, illustre la chaîne "
                "cyclique."
            )
        ) as tracker:
            self.play(FadeIn(exemple))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(exemple), FadeOut(titre))
