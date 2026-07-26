"""
scenes/Chimie_AlcenesAlcynes_01.py — Chapitre 3 (1ereC, Chimie), scène 01.

Introduction aux hydrocarbures insaturés et à la molécule d'éthylène :
formule brute C2H4, formule semi-développée CH2=CH2, structure plane,
carbone trigonal (angles ≈120°), rigidité de la double liaison (rotation
impossible), longueur de la liaison C=C (134 pm) comparée à la liaison C-C
des alcanes (154 pm). Source : 1ereC/Chimie.pdf, chapitre 3, pages 25-26.
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
from shapes.boxes import definition_box, property_box, scene_title, warning_box


def _wrap(text: str, width: int = 56) -> str:
    return "\n".join(textwrap.fill(line, width=width) for line in text.split("\n"))


def _fit(mobject, top_y):
    bas_visible = -config.frame_height / 2 + 0.25
    hauteur_dispo = top_y - bas_visible
    if mobject.height > hauteur_dispo:
        mobject.scale(hauteur_dispo / mobject.height, about_point=mobject.get_top())
    return mobject


def _ethylene_schema():
    """Schéma plan de la molécule d'éthylène : 2 C trigonaux (120°) reliés
    par une double liaison, chacun portant 2 H."""
    c_gauche = np.array([-0.55, 0, 0])
    c_droite = np.array([0.55, 0, 0])

    angle = np.pi / 3  # 60° au-dessus/dessous de l'horizontale -> 120° entre liaisons C-H
    longueur = 0.85
    h1_gauche = c_gauche + longueur * np.array([-np.cos(angle), np.sin(angle), 0])
    h2_gauche = c_gauche + longueur * np.array([-np.cos(angle), -np.sin(angle), 0])
    h1_droite = c_droite + longueur * np.array([np.cos(angle), np.sin(angle), 0])
    h2_droite = c_droite + longueur * np.array([np.cos(angle), -np.sin(angle), 0])

    # double liaison C=C : deux traits parallèles
    double_liaison = VGroup(
        Line(c_gauche + UP * 0.05, c_droite + UP * 0.05, color=WHITE, stroke_width=4),
        Line(c_gauche + DOWN * 0.05, c_droite + DOWN * 0.05, color=WHITE, stroke_width=4),
    )

    liaisons_ch = VGroup(
        Line(c_gauche, h1_gauche, color=WHITE, stroke_width=3),
        Line(c_gauche, h2_gauche, color=WHITE, stroke_width=3),
        Line(c_droite, h1_droite, color=WHITE, stroke_width=3),
        Line(c_droite, h2_droite, color=WHITE, stroke_width=3),
    )

    atomes_c = VGroup(
        Dot(c_gauche, radius=0.09, color=BLUE),
        Dot(c_droite, radius=0.09, color=BLUE),
    )
    atomes_h = VGroup(
        *[Dot(p, radius=0.07, color=GREY) for p in (h1_gauche, h2_gauche, h1_droite, h2_droite)]
    )
    labels = VGroup(
        MathTex("C", font_size=26, color=WHITE).next_to(c_gauche, DOWN * 0.001, buff=0.0).shift(UP * 0.02),
        MathTex("C", font_size=26, color=WHITE).move_to(c_droite),
        MathTex("H", font_size=22, color=WHITE).move_to(h1_gauche),
        MathTex("H", font_size=22, color=WHITE).move_to(h2_gauche),
        MathTex("H", font_size=22, color=WHITE).move_to(h1_droite),
        MathTex("H", font_size=22, color=WHITE).move_to(h2_droite),
    )

    angle_label = Text("≈120°", font_size=18, color=YELLOW)
    angle_label.next_to(c_gauche, LEFT, buff=0.55)

    return VGroup(double_liaison, liaisons_ch, atomes_c, atomes_h, labels, angle_label)


class IntroductionEthylene(NotionScene):
    def construct(self):
        titre = scene_title("1. La molécule d'éthylène : premier alcène")
        titre.scale(0.5)
        titre.to_edge(UP)

        # --- Énoncé : hydrocarbures insaturés, formule de l'éthylène -----------
        intro = Text(
            _wrap(
                "Les alcanes ne contiennent que des liaisons simples entre "
                "carbones : on les dit saturés. Certains hydrocarbures "
                "possèdent une liaison double ou triple entre deux "
                "carbones : ce sont des hydrocarbures insaturés. Le plus "
                "simple des alcènes est l'éthylène.",
                width=56,
            ),
            font_size=24,
            color=WHITE,
        )
        intro.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Les alcanes ne contiennent que des liaisons simples entre "
                "atomes de carbone : on dit qu'ils sont saturés. Mais "
                "certains hydrocarbures possèdent une liaison double ou "
                "une liaison triple entre deux carbones : ce sont des "
                "hydrocarbures insaturés. Le plus simple des alcènes, "
                "premiers représentants de cette famille, est l'éthylène."
            )
        ) as tracker:
            self.play(Write(titre))
            self.play(FadeIn(intro))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(intro))

        # --- Animation du raisonnement : formules + schéma plan -----------------
        entete = Text("Formule brute et semi-développée", font_size=24, color=YELLOW, weight="BOLD")
        entete.next_to(titre, DOWN, buff=0.4)

        formules = VGroup(
            MathTex(r"\text{Formule brute : } C_2H_4", font_size=30, color=WHITE),
            MathTex(r"\text{Formule semi-développée : } CH_2 = CH_2", font_size=30, color=WHITE),
        ).arrange(DOWN, buff=0.35)
        formules.next_to(entete, DOWN, buff=0.4)

        schema = _ethylene_schema()
        schema.next_to(formules, DOWN, buff=0.5)
        _fit(schema, formules.get_bottom()[1] - 0.4)

        groupe1 = VGroup(entete, formules, schema)

        with self.voiceover(
            text=(
                "L'éthylène a pour formule brute C deux H quatre, et pour "
                "formule semi-développée C H deux, double liaison, C H "
                "deux. La molécule est plane : les deux atomes de carbone "
                "et les quatre atomes d'hydrogène se trouvent dans un même "
                "plan. Chaque carbone, dit trigonal, forme des angles "
                "d'environ cent vingt degrés avec ses trois voisins."
            )
        ) as tracker:
            self.play(FadeIn(entete))
            self.play(FadeIn(formules))
            self.play(FadeIn(schema))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(groupe1))

        # --- Exemple traité : longueur de la liaison C=C vs C-C -----------------
        exemple = property_box(
            VGroup(
                MathTex(r"\text{Liaison } C=C \text{ (éthylène) : } 134\ pm", font_size=26),
                MathTex(r"\text{Liaison } C-C \text{ (alcane, ex. éthane) : } 154\ pm", font_size=26),
                MathTex(r"\text{La double liaison est donc plus courte.}", font_size=24),
            ).arrange(DOWN, buff=0.3, aligned_edge=LEFT),
            box_width=11.0,
        )
        exemple.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Comparons les longueurs de liaison : la liaison double "
                "carbone-carbone de l'éthylène mesure environ cent trente "
                "quatre picomètres, contre cent cinquante quatre "
                "picomètres pour la liaison simple carbone-carbone d'un "
                "alcane comme l'éthane. La double liaison est donc plus "
                "courte, et surtout plus riche en électrons."
            )
        ) as tracker:
            self.play(FadeIn(exemple))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(exemple))

        # --- À retenir : rigidité de la double liaison ---------------------------
        retenir = property_box(
            Text(
                _wrap(
                    "Contrairement à la liaison simple C-C qui autorise la "
                    "libre rotation, la double liaison C=C est rigide : "
                    "aucune rotation n'est possible autour d'elle. C'est "
                    "cette rigidité qui rendra possible la stéréoisomérie "
                    "Z/E, étudiée plus loin.",
                    width=48,
                ),
                font_size=25,
            ),
        )
        retenir.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Retenons l'essentiel : contrairement à la liaison simple "
                "carbone-carbone, qui autorise la libre rotation des deux "
                "fragments l'un par rapport à l'autre, la double liaison "
                "carbone-carbone est rigide. Aucune rotation n'est "
                "possible autour d'elle. C'est précisément cette rigidité "
                "qui rendra possible la stéréoisomérie Z et E, que nous "
                "étudierons plus loin dans ce chapitre."
            )
        ) as tracker:
            self.play(FadeIn(retenir))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(retenir))

        # --- Pièges à éviter -----------------------------------------------------
        piege = warning_box(
            Text(
                _wrap(
                    "Ne pas confondre : dans un alcane, les groupes "
                    "peuvent tourner librement autour d'une liaison C-C. "
                    "Dans un alcène, cette rotation est bloquée au niveau "
                    "de la double liaison C=C — la molécule y est plane et "
                    "figée.",
                    width=48,
                ),
                font_size=25,
            ),
        )
        piege.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Attention à un piège fréquent : dans un alcane, les "
                "groupes peuvent tourner librement autour de n'importe "
                "quelle liaison simple carbone-carbone. Dans un alcène, "
                "cette rotation est bloquée au niveau de la double "
                "liaison : la molécule y est plane et figée, ce qui aura "
                "des conséquences importantes sur son isomérie."
            )
        ) as tracker:
            self.play(FadeIn(piege))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(piege), FadeOut(titre))
