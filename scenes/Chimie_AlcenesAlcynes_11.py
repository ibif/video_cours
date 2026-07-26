"""
scenes/Chimie_AlcenesAlcynes_11.py — Chapitre 3 (1ereC, Chimie), scène 11.

Le test à l'eau de brome : test caractéristique de l'insaturation
(présence d'une double ou triple liaison C=C / C≡C), comparaison alcane
(reste rouge-orangé) / alcène ou alcyne (se décolore), équation de la
réaction. Source : 1ereC/Chimie.pdf, chapitre 3, page 32.
"""

import textwrap

from manim import (
    DOWN,
    LEFT,
    RIGHT,
    UP,
    WHITE,
    YELLOW,
    ORANGE,
    GREY,
    FadeIn,
    FadeOut,
    MathTex,
    RoundedRectangle,
    Text,
    VGroup,
    Write,
    config,
)

from shapes.base_scene import NotionScene
from shapes.boxes import property_box, scene_title


def _wrap(text: str, width: int = 56) -> str:
    return "\n".join(textwrap.fill(line, width=width) for line in text.split("\n"))


def _fit(mobject, top_y):
    bas_visible = -config.frame_height / 2 + 0.25
    hauteur_dispo = top_y - bas_visible
    if mobject.height > hauteur_dispo:
        mobject.scale(hauteur_dispo / mobject.height, about_point=mobject.get_top())
    return mobject


def _tube_essai(couleur, label):
    """Petit schéma de tube à essai : un rectangle-ellipse rempli d'une
    couleur, avec un label en dessous, pour illustrer le test à l'eau de
    brome (couleur qui persiste ou disparaît)."""
    tube = RoundedRectangle(
        width=0.7,
        height=1.6,
        corner_radius=0.25,
        fill_color=couleur,
        fill_opacity=0.85 if couleur != WHITE else 0.15,
        stroke_color=GREY,
        stroke_width=2,
    )
    texte = Text(label, font_size=17, color=WHITE)
    texte.next_to(tube, DOWN, buff=0.2)
    return VGroup(tube, texte)


class TestEauDeBrome(NotionScene):
    def construct(self):
        titre = scene_title("11. Le test à l'eau de brome")
        titre.scale(0.55)
        titre.to_edge(UP)

        # --- Énoncé : comment reconnaître une insaturation en pratique ----------
        intro = Text(
            _wrap(
                "Comment reconnaître expérimentalement la présence d'une "
                "double ou triple liaison dans un hydrocarbure, sans "
                "connaître sa formule ? Il existe un test simple : le "
                "test à l'eau de brome.",
                width=54,
            ),
            font_size=24,
            color=WHITE,
        )
        intro.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Comment reconnaître expérimentalement la présence d'une "
                "double ou d'une triple liaison dans un hydrocarbure, "
                "sans connaître sa formule à l'avance ? Il existe un "
                "test simple, très utilisé en laboratoire : le test à "
                "l'eau de brome."
            )
        ) as tracker:
            self.play(Write(titre))
            self.play(FadeIn(intro))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(intro))

        # --- Animation du raisonnement : principe du test ------------------------
        propriete = property_box(
            Text(
                _wrap(
                    "L'eau de brome, de couleur rouge-orangé, est un "
                    "réactif caractéristique de l'insaturation : elle se "
                    "décolore au contact d'un alcène ou d'un alcyne (le "
                    "dibrome s'additionne sur la double ou la triple "
                    "liaison).",
                    width=48,
                ),
                font_size=24,
            ),
        )
        propriete.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "L'eau de brome est une solution de dibrome dans l'eau, "
                "de couleur rouge-orangé. Elle constitue un réactif "
                "caractéristique de l'insaturation : au contact d'un "
                "alcène ou d'un alcyne, elle se décolore, car le dibrome "
                "s'additionne sur la double ou la triple liaison, "
                "exactement comme nous l'avons vu dans les réactions "
                "d'addition."
            )
        ) as tracker:
            self.play(FadeIn(propriete))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(propriete))

        # --- Exemple traité : comparaison alcane / alcène-alcyne ------------------
        entete = Text("Alcane vs alcène/alcyne face à l'eau de brome", font_size=21, color=YELLOW, weight="BOLD")
        entete.next_to(titre, DOWN, buff=0.35)

        tube_alcane = _tube_essai(ORANGE, "alcane\nreste rouge-orangé")
        tube_alcene = _tube_essai(WHITE, "alcène / alcyne\nse décolore")
        tubes = VGroup(tube_alcane, tube_alcene).arrange(RIGHT, buff=1.3)
        tubes.next_to(entete, DOWN, buff=0.5)

        groupe = VGroup(entete, tubes)

        with self.voiceover(
            text=(
                "En pratique, on verse quelques gouttes d'eau de brome "
                "dans deux tubes à essai : l'un contenant un alcane, "
                "l'autre un alcène ou un alcyne. Dans le tube contenant "
                "l'alcane, la couleur rouge-orangé persiste, car aucune "
                "addition n'est possible en l'absence de double ou "
                "triple liaison. Dans le tube contenant l'alcène ou "
                "l'alcyne, la coloration disparaît rapidement."
            )
        ) as tracker:
            self.play(FadeIn(entete))
            self.play(FadeIn(tube_alcane))
            self.play(FadeIn(tube_alcene))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(groupe))

        # --- À retenir : équation-type de la décoloration -------------------------
        equation = property_box(
            VGroup(
                MathTex(r"C_nH_{2n} + Br_2 \longrightarrow C_nH_{2n}Br_2", font_size=28),
                Text("(la coloration orangée du Br₂ disparaît)", font_size=20),
            ).arrange(DOWN, buff=0.3),
            box_width=10.5,
        )
        equation.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "L'équation-type de cette décoloration s'écrit : un "
                "alcène, C indice n H indice deux n, plus dibrome, donne "
                "le dérivé dibromé correspondant. La coloration orangée "
                "du dibrome disparaît car celui-ci est entièrement "
                "consommé par la réaction d'addition."
            )
        ) as tracker:
            self.play(FadeIn(equation))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(equation))

        # --- Pièges à éviter -------------------------------------------------------
        piege = Text(
            _wrap(
                "Piège fréquent : le test à l'eau de brome prouve la "
                "PRÉSENCE d'une insaturation, mais ne permet PAS de "
                "distinguer un alcène d'un alcyne — les deux décolorent "
                "l'eau de brome de la même façon. D'autres tests sont "
                "nécessaires pour les différencier.",
                width=52,
            ),
            font_size=21,
            color=WHITE,
        )
        piege.next_to(titre, DOWN, buff=0.4)
        _fit(piege, titre.get_bottom()[1] - 0.4)

        with self.voiceover(
            text=(
                "Attention à un piège très fréquent : le test à l'eau de "
                "brome prouve seulement la présence d'une insaturation, "
                "double ou triple liaison. Il ne permet en aucun cas de "
                "distinguer un alcène d'un alcyne, car les deux "
                "décolorent l'eau de brome de la même façon. D'autres "
                "analyses sont nécessaires pour les différencier avec "
                "certitude."
            )
        ) as tracker:
            self.play(FadeIn(piege))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(piege), FadeOut(titre))
