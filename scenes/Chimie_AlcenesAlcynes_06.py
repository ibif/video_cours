"""
scenes/Chimie_AlcenesAlcynes_06.py — Chapitre 3 (1ereC, Chimie), scène 06.

Molécule d'acétylène et formule brute générale des alcynes : structure
linéaire H-C≡C-H, carbone digonal (angle 180°), longueur de la triple
liaison (120 pm), et formule générale CnH2n-2 (n≥2).
Source : 1ereC/Chimie.pdf, chapitre 3, page 30.
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
    GREY,
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
from shapes.boxes import definition_box, property_box, scene_title


def _wrap(text: str, width: int = 56) -> str:
    return "\n".join(textwrap.fill(line, width=width) for line in text.split("\n"))


def _fit(mobject, top_y):
    bas_visible = -config.frame_height / 2 + 0.25
    hauteur_dispo = top_y - bas_visible
    if mobject.height > hauteur_dispo:
        mobject.scale(hauteur_dispo / mobject.height, about_point=mobject.get_top())
    return mobject


def _schema_acetylene():
    """H-C≡C-H : structure parfaitement linéaire, carbone digonal (180°)."""
    h_gauche = np.array([-1.6, 0, 0])
    c_gauche = np.array([-0.5, 0, 0])
    c_droite = np.array([0.5, 0, 0])
    h_droite = np.array([1.6, 0, 0])

    triple = VGroup(
        Line(c_gauche + UP * 0.08, c_droite + UP * 0.08, color=WHITE, stroke_width=4),
        Line(c_gauche, c_droite, color=WHITE, stroke_width=4),
        Line(c_gauche + DOWN * 0.08, c_droite + DOWN * 0.08, color=WHITE, stroke_width=4),
    )
    liaisons_ch = VGroup(
        Line(h_gauche, c_gauche, color=WHITE, stroke_width=3),
        Line(c_droite, h_droite, color=WHITE, stroke_width=3),
    )
    atomes_c = VGroup(Dot(c_gauche, radius=0.09, color=BLUE), Dot(c_droite, radius=0.09, color=BLUE))
    atomes_h = VGroup(Dot(h_gauche, radius=0.07, color=GREY), Dot(h_droite, radius=0.07, color=GREY))
    labels = VGroup(
        MathTex("H", font_size=24, color=WHITE).next_to(h_gauche, UP, buff=0.15),
        MathTex("C", font_size=24, color=WHITE).next_to(c_gauche, UP, buff=0.15),
        MathTex("C", font_size=24, color=WHITE).next_to(c_droite, UP, buff=0.15),
        MathTex("H", font_size=24, color=WHITE).next_to(h_droite, UP, buff=0.15),
    )
    angle_label = Text("180° (linéaire)", font_size=18, color=YELLOW)
    angle_label.next_to(VGroup(triple, liaisons_ch), DOWN, buff=0.35)
    return VGroup(triple, liaisons_ch, atomes_c, atomes_h, labels, angle_label)


class MoleculeAcetylene(NotionScene):
    def construct(self):
        titre = scene_title("6. La molécule d'acétylène et les alcynes")
        titre.scale(0.55)
        titre.to_edge(UP)

        # --- Énoncé : une nouvelle famille, la triple liaison --------------------
        intro = Text(
            _wrap(
                "Au-delà de la double liaison, certains hydrocarbures "
                "possèdent une triple liaison C≡C entre deux carbones : "
                "ce sont les alcynes. Le plus simple d'entre eux est "
                "l'acétylène.",
                width=54,
            ),
            font_size=24,
            color=WHITE,
        )
        intro.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Au-delà de la double liaison, certains hydrocarbures "
                "possèdent une triple liaison entre deux atomes de "
                "carbone : ce sont les alcynes. Le plus simple d'entre "
                "eux est l'acétylène."
            )
        ) as tracker:
            self.play(Write(titre))
            self.play(FadeIn(intro))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(intro))

        # --- Animation du raisonnement : structure linéaire de l'acétylène ------
        entete = Text("Structure linéaire H-C≡C-H", font_size=24, color=YELLOW, weight="BOLD")
        entete.next_to(titre, DOWN, buff=0.4)

        formules = MathTex(r"\text{Formule brute : } C_2H_2", font_size=28, color=WHITE)
        formules.next_to(entete, DOWN, buff=0.4)

        schema = _schema_acetylene()
        schema.next_to(formules, DOWN, buff=0.5)
        _fit(schema, formules.get_bottom()[1] - 0.4)

        groupe1 = VGroup(entete, formules, schema)

        with self.voiceover(
            text=(
                "L'acétylène a pour formule brute C deux H deux. Sa "
                "molécule est parfaitement linéaire : les deux atomes de "
                "carbone sont dits digonaux, et forment un angle de cent "
                "quatre-vingts degrés avec leurs voisins. La triple "
                "liaison carbone-carbone mesure environ cent vingt "
                "picomètres, ce qui en fait la liaison la plus courte et "
                "la plus riche en électrons parmi les trois familles "
                "d'hydrocarbures."
            )
        ) as tracker:
            self.play(FadeIn(entete))
            self.play(FadeIn(formules))
            self.play(FadeIn(schema))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(groupe1))

        # --- Exemple traité : comparaison des longueurs de liaison --------------
        exemple = property_box(
            VGroup(
                MathTex(r"\text{Liaison } C-C \text{ (alcane) : } 154\ pm", font_size=26),
                MathTex(r"\text{Liaison } C=C \text{ (alcène) : } 134\ pm", font_size=26),
                MathTex(r"\text{Liaison } C \equiv C \text{ (alcyne) : } 120\ pm", font_size=26, color=YELLOW),
            ).arrange(DOWN, buff=0.3, aligned_edge=LEFT),
            box_width=11.0,
        )
        exemple.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "En comparant les trois familles, on observe une "
                "tendance nette : plus le nombre de liaisons entre les "
                "deux carbones augmente, plus la liaison est courte. La "
                "liaison simple mesure cent cinquante quatre picomètres, "
                "la double liaison cent trente quatre picomètres, et la "
                "triple liaison seulement cent vingt picomètres."
            )
        ) as tracker:
            self.play(FadeIn(exemple))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(exemple))

        # --- À retenir : formule brute générale des alcynes ----------------------
        definition = definition_box(
            VGroup(
                Text(
                    _wrap(
                        "Un alcyne est un hydrocarbure non cyclique dont la "
                        "molécule possède une seule triple liaison C≡C.",
                        width=46,
                    ),
                    font_size=24,
                ),
                MathTex(r"C_nH_{2n-2} \quad (n \geq 2)", font_size=34, color=YELLOW),
            ).arrange(DOWN, buff=0.35),
        )
        definition.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Retenons la définition générale : un alcyne est un "
                "hydrocarbure non cyclique dont la molécule possède une "
                "seule triple liaison carbone-carbone. Sa formule brute "
                "générale est C indice n, H indice deux n moins deux, "
                "avec n supérieur ou égal à 2."
            )
        ) as tracker:
            self.play(FadeIn(definition))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(definition))

        # --- Pièges à éviter -------------------------------------------------------
        piege = Text(
            _wrap(
                "Piège fréquent : ne pas confondre l'angle du carbone "
                "trigonal de l'alcène (≈120°, molécule plane) avec celui "
                "du carbone digonal de l'alcyne (180°, molécule "
                "linéaire) — deux géométries bien distinctes.",
                width=52,
            ),
            font_size=23,
            color=WHITE,
        )
        piege.next_to(titre, DOWN, buff=0.4)
        _fit(piege, titre.get_bottom()[1] - 0.4)

        with self.voiceover(
            text=(
                "Attention à un piège fréquent : ne confondez pas l'angle "
                "d'environ cent vingt degrés du carbone trigonal de "
                "l'alcène, qui donne une molécule plane, avec l'angle de "
                "cent quatre-vingts degrés du carbone digonal de "
                "l'alcyne, qui donne une molécule parfaitement linéaire. "
                "Ce sont deux géométries bien distinctes."
            )
        ) as tracker:
            self.play(FadeIn(piege))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(piege), FadeOut(titre))
