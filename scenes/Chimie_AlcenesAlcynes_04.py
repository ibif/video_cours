"""
scenes/Chimie_AlcenesAlcynes_04.py — Chapitre 3 (1ereC, Chimie), scène 04.

Isomérie de position des alcènes : définition, exemple but-1-ène / but-2-ène
(même formule brute commune C4H8, position de la double liaison différente).
Source : 1ereC/Chimie.pdf, chapitre 3, page 28.
"""

import textwrap

from manim import (
    DOWN,
    LEFT,
    RIGHT,
    UP,
    WHITE,
    YELLOW,
    FadeIn,
    FadeOut,
    MathTex,
    Text,
    VGroup,
    Write,
    config,
)

from shapes.base_scene import NotionScene
from shapes.boxes import definition_box, example_box, scene_title, warning_box


def _wrap(text: str, width: int = 56) -> str:
    return "\n".join(textwrap.fill(line, width=width) for line in text.split("\n"))


def _fit(mobject, top_y):
    bas_visible = -config.frame_height / 2 + 0.25
    hauteur_dispo = top_y - bas_visible
    if mobject.height > hauteur_dispo:
        mobject.scale(hauteur_dispo / mobject.height, about_point=mobject.get_top())
    return mobject


class IsomeriePositionAlcenes(NotionScene):
    def construct(self):
        titre = scene_title("4. Isomérie de position des alcènes")
        titre.scale(0.55)
        titre.to_edge(UP)

        # --- Énoncé : rappel de l'isomérie ---------------------------------------
        intro = Text(
            _wrap(
                "Pour une même formule brute, la position de la double "
                "liaison sur la chaîne carbonée peut varier : on parle "
                "d'isomérie de position.",
                width=52,
            ),
            font_size=25,
            color=WHITE,
        )
        intro.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Pour une même formule brute, la position de la double "
                "liaison sur la chaîne carbonée peut varier d'une "
                "molécule à l'autre : c'est ce qu'on appelle l'isomérie "
                "de position."
            )
        ) as tracker:
            self.play(Write(titre))
            self.play(FadeIn(intro))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(intro))

        # --- Animation du raisonnement : définition ------------------------------
        definition = definition_box(
            Text(
                _wrap(
                    "Deux alcènes sont isomères de position lorsqu'ils ont "
                    "la même formule brute, mais que la double liaison "
                    "C=C occupe une position différente sur la chaîne "
                    "carbonée.",
                    width=48,
                ),
                font_size=25,
            ),
        )
        definition.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Deux alcènes sont dits isomères de position lorsqu'ils "
                "ont la même formule brute, mais que la double liaison "
                "carbone-carbone occupe une position différente sur la "
                "chaîne carbonée."
            )
        ) as tracker:
            self.play(FadeIn(definition))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(definition))

        # --- Exemple traité : but-1-ène / but-2-ène ------------------------------
        exemple = example_box(
            VGroup(
                MathTex(r"\text{but-1-ène : } CH_2=CH-CH_2-CH_3", font_size=28),
                MathTex(r"\text{but-2-ène : } CH_3-CH=CH-CH_3", font_size=28),
                MathTex(r"\text{Formule brute commune : } C_4H_8", font_size=28, color=YELLOW),
            ).arrange(DOWN, buff=0.4),
            box_width=11.0,
        )
        exemple.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Prenons l'exemple classique : le but-un-ène, C H deux, "
                "double liaison C H, C H deux, C H trois, et le "
                "but-deux-ène, C H trois, C H, double liaison C H, C H "
                "trois. Ces deux molécules ont exactement la même formule "
                "brute, C quatre H huit, mais la double liaison est en "
                "position un dans la première, et en position deux dans "
                "la seconde. Ce sont donc des isomères de position."
            )
        ) as tracker:
            self.play(FadeIn(exemple))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(exemple))

        # --- À retenir -------------------------------------------------------------
        retenir = definition_box(
            Text(
                _wrap(
                    "Des propriétés physiques (température d'ébullition…) "
                    "et chimiques peuvent différer entre isomères de "
                    "position, bien qu'ils partagent la même formule "
                    "brute.",
                    width=48,
                ),
                font_size=25,
            ),
        )
        retenir.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Retenons l'essentiel : bien qu'ils partagent la même "
                "formule brute, deux isomères de position sont des "
                "molécules différentes, avec des propriétés physiques et "
                "chimiques qui peuvent différer, comme leur température "
                "d'ébullition."
            )
        ) as tracker:
            self.play(FadeIn(retenir))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(retenir))

        # --- Pièges à éviter -----------------------------------------------------
        piege = warning_box(
            Text(
                _wrap(
                    "Ne pas confondre isomérie de position (la double "
                    "liaison change de place sur la même chaîne) et "
                    "isomérie de chaîne (la chaîne carbonée elle-même "
                    "change de forme, linéaire ou ramifiée).",
                    width=48,
                ),
                font_size=24,
            ),
        )
        piege.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Attention à ne pas confondre l'isomérie de position, où "
                "seule la place de la double liaison change sur une même "
                "chaîne, avec l'isomérie de chaîne, où c'est la forme "
                "même de la chaîne carbonée qui change, linéaire ou "
                "ramifiée."
            )
        ) as tracker:
            self.play(FadeIn(piege))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(piege), FadeOut(titre))
