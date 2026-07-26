"""
scenes/Chimie_GeneralitesComposesOrganiques_08.py — Chapitre 1 (1ereC, Chimie), scène 08.

§ 4 Les différentes écritures d'une molécule organique : formule brute,
formule développée plane, formule semi-développée, formule topologique
(schéma de l'éthanol dans les 3 écritures + tableau récapitulatif).
Source : 1ereC/Chimie.pdf, pages 8-9.
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
    GRAY,
    FadeIn,
    FadeOut,
    Dot,
    Line,
    MathTex,
    Text,
    VGroup,
    Write,
    config,
)

from shapes.base_scene import NotionScene
from shapes.boxes import scene_title


def _wrap(text: str, width: int = 56) -> str:
    return "\n".join(textwrap.fill(line, width=width) for line in text.split("\n"))


def _fit(mobject, top_y):
    bas_visible = -config.frame_height / 2 + 0.25
    hauteur_dispo = top_y - bas_visible
    if mobject.height > hauteur_dispo:
        mobject.scale(hauteur_dispo / mobject.height, about_point=mobject.get_top())
    return mobject


def _ethanol_developpee():
    """Formule développée plane de l'éthanol : C2H6O, tous les atomes et
    toutes les liaisons représentés."""
    c1 = MathTex("C", font_size=28, color=WHITE).move_to(np.array([-0.6, 0, 0]))
    c2 = MathTex("C", font_size=28, color=WHITE).move_to(np.array([0.6, 0, 0]))
    o = MathTex("O", font_size=28, color=BLUE).move_to(np.array([1.6, 0, 0]))
    h_c1 = [
        MathTex("H", font_size=22, color=GRAY).move_to(np.array([-0.6, 0.7, 0])),
        MathTex("H", font_size=22, color=GRAY).move_to(np.array([-1.3, 0, 0])),
        MathTex("H", font_size=22, color=GRAY).move_to(np.array([-0.6, -0.7, 0])),
    ]
    h_c2 = [
        MathTex("H", font_size=22, color=GRAY).move_to(np.array([0.6, 0.7, 0])),
        MathTex("H", font_size=22, color=GRAY).move_to(np.array([0.6, -0.7, 0])),
    ]
    h_o = MathTex("H", font_size=22, color=GRAY).move_to(np.array([2.3, 0, 0]))

    atomes = VGroup(c1, c2, o, h_o, *h_c1, *h_c2)

    liaisons = VGroup(
        Line(c1.get_right(), c2.get_left(), color=WHITE, stroke_width=2.5),
        Line(c2.get_right(), o.get_left(), color=WHITE, stroke_width=2.5),
        Line(o.get_right(), h_o.get_left(), color=WHITE, stroke_width=2.5),
        *[Line(c1.get_center(), h.get_center(), color=WHITE, stroke_width=2, buff=0.18) for h in h_c1],
        *[Line(c2.get_center(), h.get_center(), color=WHITE, stroke_width=2, buff=0.18) for h in h_c2],
    )
    return VGroup(liaisons, atomes)


def _ethanol_topologique():
    """Formule topologique de l'éthanol : ligne brisée à 2 sommets + OH."""
    p1 = np.array([-0.8, -0.3, 0])
    p2 = np.array([0.0, 0.3, 0])
    p3 = np.array([0.8, -0.3, 0])
    trait = VGroup(
        Line(p1, p2, color=WHITE, stroke_width=4),
        Line(p2, p3, color=WHITE, stroke_width=4),
    )
    oh = MathTex("OH", font_size=28, color=BLUE)
    oh.next_to(p3, RIGHT, buff=0.1)
    return VGroup(trait, oh)


class EcrituresMoleculeOrganique(NotionScene):
    def construct(self):
        titre = scene_title("4. Les différentes écritures d'une molécule")
        titre.scale(0.58)
        titre.to_edge(UP)

        # --- Énoncé : pourquoi plusieurs écritures ? ----------------------------
        intro = Text(
            _wrap(
                "Connaissant la formule brute et la covalence de chaque "
                "élément (C=4, H=1, O=2, N=3), on peut représenter une "
                "molécule organique de plusieurs façons, selon le niveau "
                "de détail souhaité.",
                width=54,
            ),
            font_size=24,
            color=WHITE,
        )
        intro.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Connaissant la formule brute et la covalence de chaque "
                "élément — quatre pour le carbone, un pour l'hydrogène, "
                "deux pour l'oxygène, trois pour l'azote — on peut "
                "représenter une molécule organique de plusieurs façons, "
                "selon le niveau de détail souhaité. Prenons l'exemple de "
                "l'éthanol, de formule brute C deux H six O."
            )
        ) as tracker:
            self.play(Write(titre))
            self.play(FadeIn(intro))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(intro))

        # --- Animation du raisonnement : les 3 écritures de l'éthanol ----------
        entete = Text("L'éthanol C₂H₆O dans trois écritures", font_size=23, color=YELLOW, weight="BOLD")
        entete.next_to(titre, DOWN, buff=0.4)

        brute = MathTex("C_2H_6O", font_size=30, color=WHITE)
        label_brute = Text("brute", font_size=16, color=WHITE)
        bloc_brute = VGroup(brute, label_brute).arrange(DOWN, buff=0.2)

        developpee = _ethanol_developpee()
        label_dev = Text("développée", font_size=16, color=WHITE)
        bloc_dev = VGroup(developpee, label_dev).arrange(DOWN, buff=0.2)

        semi_dev = MathTex(r"CH_3-CH_2-OH", font_size=28, color=WHITE)
        label_semi = Text("semi-développée", font_size=16, color=WHITE)
        bloc_semi = VGroup(semi_dev, label_semi).arrange(DOWN, buff=0.2)

        topologique = _ethanol_topologique()
        label_topo = Text("topologique", font_size=16, color=WHITE)
        bloc_topo = VGroup(topologique, label_topo).arrange(DOWN, buff=0.2)

        schema = VGroup(bloc_brute, bloc_dev, bloc_semi, bloc_topo).arrange(RIGHT, buff=0.8, aligned_edge=DOWN)
        schema.next_to(entete, DOWN, buff=0.5)
        _fit(schema, entete.get_bottom()[1] - 0.4)

        groupe_schema = VGroup(entete, schema)

        with self.voiceover(
            text=(
                "La formule brute, C deux H six O, indique la nature et le "
                "nombre des atomes, mais pas leur enchaînement. La formule "
                "développée plane représente, elle, tous les atomes et "
                "toutes les liaisons : chaque carbone porte quatre "
                "liaisons, l'oxygène deux, chaque hydrogène une seule. La "
                "formule semi-développée regroupe, autour de chaque "
                "carbone, les hydrogènes qui lui sont liés : l'éthanol "
                "s'écrit alors CH3-CH2-OH. Enfin, la formule topologique, "
                "la plus rapide à tracer, représente la chaîne carbonée "
                "par une ligne brisée : chaque sommet et chaque extrémité "
                "est un atome de carbone, et les hydrogènes portés par le "
                "carbone ne sont plus écrits."
            )
        ) as tracker:
            self.play(FadeIn(entete))
            self.play(FadeIn(bloc_brute))
            self.play(FadeIn(bloc_dev))
            self.play(FadeIn(bloc_semi))
            self.play(FadeIn(bloc_topo))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(groupe_schema))

        # --- À retenir : tableau récapitulatif des 4 écritures ------------------
        entete_tab = Text("Ce que donne chaque écriture", font_size=24, color=YELLOW, weight="BOLD")
        entete_tab.next_to(titre, DOWN, buff=0.4)

        lignes = VGroup(
            Text("Brute : nature et nombre des atomes", font_size=20),
            Text("Développée : tous les atomes et toutes les liaisons", font_size=20),
            Text("Semi-développée : enchaînement des atomes lourds", font_size=20),
            Text("Topologique : squelette carboné seul", font_size=20),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.3)
        lignes.next_to(entete_tab, DOWN, buff=0.4)
        _fit(lignes, entete_tab.get_bottom()[1] - 0.4)

        groupe_tab = VGroup(entete_tab, lignes)

        with self.voiceover(
            text=(
                "Retenons ce que donne chaque écriture. La formule brute "
                "donne la nature et le nombre des atomes. La formule "
                "développée donne tous les atomes et toutes les liaisons. "
                "La formule semi-développée donne l'enchaînement des "
                "atomes lourds. Et la formule topologique donne le "
                "squelette carboné seul, la plus rapide des quatre à "
                "tracer."
            )
        ) as tracker:
            self.play(FadeIn(entete_tab))
            self.play(FadeIn(lignes))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(groupe_tab), FadeOut(titre))
