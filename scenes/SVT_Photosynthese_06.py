"""
scenes/SVT_Photosynthese_06.py — Chapitre 10 (1ereC, SVT), scène 06.

§ 10.3.1-10.3.2 La phase photochimique (phase claire) : conditions et lieu
(lumière indispensable, membranes des thylakoïdes) + la photolyse de l'eau
(définition, équation MathTex 2H2O --lumière--> 4H+ + 4e- + O2, preuve par
isotopes marqués).
Source : 1ereC/SVT.pdf, pages 108-109.
"""

import textwrap

from manim import (
    DOWN,
    LEFT,
    RIGHT,
    UP,
    WHITE,
    YELLOW,
    Arrow,
    FadeIn,
    FadeOut,
    MathTex,
    Rectangle,
    Text,
    VGroup,
    Write,
)

from shapes.base_scene import NotionScene
from shapes.boxes import definition_box, example_box, scene_title, warning_box


def _wrap(text: str, width: int = 56) -> str:
    return "\n".join(textwrap.fill(line, width=width) for line in text.split("\n"))


def _bullets(items, font_size=22, color=WHITE, width=52):
    lines = VGroup(
        *[Text(f"• {_wrap(it, width=width)}", font_size=font_size, color=color) for it in items]
    )
    lines.arrange(DOWN, aligned_edge=LEFT, buff=0.22)
    return lines


def _schema_photolyse():
    """Schéma simplifié : une molécule d'eau frappée par la lumière se
    scinde en protons, électrons et dioxygène."""
    thylakoide = Rectangle(width=3.4, height=0.5, fill_color="#1F7A3D", fill_opacity=0.85, stroke_color="#0F5A22", stroke_width=1.5)
    label_thyl = Text("membrane du thylakoïde", font_size=12, color="#3FCB63")
    label_thyl.next_to(thylakoide, DOWN, buff=0.15)

    eau = Text("2 H2O", font_size=20, color="#5AA9E6")
    eau.next_to(thylakoide, UP, buff=0.9).shift(LEFT * 1.6)

    fleche_lum = Arrow(UP * 0.8, DOWN * 0.05, color=YELLOW, buff=0).scale(0.8)
    fleche_lum.next_to(eau, UP, buff=0.1)
    label_lum = Text("lumière", font_size=13, color=YELLOW).next_to(fleche_lum, UP, buff=0.05)

    fleche_vers = Arrow(LEFT * 0.6, RIGHT * 0.6, color=WHITE, buff=0)
    fleche_vers.next_to(eau, RIGHT, buff=0.3)

    produits = VGroup(
        Text("4 H+", font_size=18, color="#E67E22"),
        Text("4 e-", font_size=18, color="#F1C40F"),
        Text("O2", font_size=18, color="#3FCB63"),
    ).arrange(DOWN, buff=0.15)
    produits.next_to(fleche_vers, RIGHT, buff=0.3)

    return VGroup(thylakoide, label_thyl, eau, fleche_lum, label_lum, fleche_vers, produits)


class PhaseClaireEtPhotolyse(NotionScene):
    def construct(self):
        titre = scene_title("10.3.1-10.3.2 — Phase claire et photolyse de l'eau")
        titre.scale(0.46)
        titre.to_edge(UP)

        # --- Énoncé : conditions et lieu de la phase photochimique -----------
        conditions = definition_box(
            _bullets(
                [
                    "Nécessite obligatoirement la lumière.",
                    "Se déroule dans les membranes des thylakoïdes "
                    "(grana).",
                    "Met en jeu la chlorophylle, l'eau et des accepteurs "
                    "d'électrons.",
                ],
                font_size=20,
                width=48,
            ),
            box_width=11.0,
        )
        conditions.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Étudions maintenant en détail la première phase de la "
                "photosynthèse, la phase photochimique, aussi appelée "
                "phase claire. Elle nécessite obligatoirement la "
                "lumière ; elle se déroule dans les membranes des "
                "thylakoïdes, regroupées en grana ; et elle met en jeu "
                "la chlorophylle, l'eau, et des accepteurs d'électrons."
            )
        ) as tracker:
            self.play(Write(titre))
            self.play(FadeIn(conditions))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(conditions))

        # --- Animation du raisonnement : la photolyse de l'eau ----------------
        def_photolyse = definition_box(
            Text(
                _wrap(
                    "La photolyse de l'eau est la rupture des molécules "
                    "d'eau sous l'action de l'énergie lumineuse captée "
                    "par la chlorophylle. Elle libère du dioxygène O2, "
                    "des protons H+ et des électrons e-.",
                    width=54,
                ),
                font_size=21,
            ),
            box_width=12.0,
        )
        def_photolyse.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "L'énergie lumineuse absorbée par la chlorophylle excite "
                "des électrons ; cette énergie sert à casser, on dit "
                "lyser, les molécules d'eau : c'est la photolyse de "
                "l'eau. Définition : la photolyse de l'eau est la "
                "rupture des molécules d'eau sous l'action de l'énergie "
                "lumineuse captée par la chlorophylle. Elle libère du "
                "dioxygène, des protons H plus et des électrons."
            )
        ) as tracker:
            self.play(FadeIn(def_photolyse))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(def_photolyse))

        # --- Exemple traité : équation de la photolyse + schéma --------------
        equation = MathTex(
            r"2\,H_2O \xrightarrow{\;\text{lumière}\;} 4\,H^+ + 4\,e^- + O_2",
            font_size=30,
            color=WHITE,
        )
        equation.next_to(titre, DOWN, buff=0.5)

        schema = _schema_photolyse()
        schema.scale(0.95)
        schema.next_to(equation, DOWN, buff=0.6)

        with self.voiceover(
            text=(
                "L'équation de la photolyse s'écrit ainsi : deux "
                "molécules d'eau, avec la lumière, donnent quatre "
                "protons, quatre électrons et une molécule de "
                "dioxygène. Ce dioxygène formé est rejeté dans "
                "l'atmosphère : c'est exactement le gaz que l'on "
                "recueille au cours de l'expérience de la plante "
                "aquatique, que nous verrons bientôt. Cette équation "
                "démontre que l'O2 dégagé provient bien de l'eau, et non "
                "du CO2 : les expériences aux isotopes stables, avec de "
                "l'eau marquée à l'oxygène dix-huit, le confirment "
                "formellement."
            )
        ) as tracker:
            self.play(Write(equation))
            self.play(FadeIn(schema))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(equation), FadeOut(schema))

        # --- À retenir : la preuve par isotopes marqués ------------------------
        preuve = example_box(
            Text(
                _wrap(
                    "Preuve expérimentale : en faisant photosynthétiser "
                    "une plante avec de l'eau enrichie en oxygène 18 "
                    "(isotope marqué), on retrouve l'oxygène 18 dans le "
                    "O2 dégagé, jamais dans le glucose. À l'inverse, avec "
                    "du CO2 marqué, l'oxygène 18 se retrouve dans le "
                    "glucose, jamais dans le O2 dégagé.",
                    width=54,
                ),
                font_size=20,
            ),
            box_width=12.0,
        )
        preuve.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Détaillons cette preuve expérimentale. En faisant "
                "photosynthétiser une plante avec de l'eau enrichie en "
                "oxygène dix-huit, un isotope marqué, on retrouve cet "
                "oxygène dix-huit dans le dioxygène dégagé, jamais dans "
                "le glucose. À l'inverse, avec du dioxyde de carbone "
                "marqué à l'oxygène dix-huit, on retrouve l'isotope dans "
                "le glucose, jamais dans le dioxygène dégagé. La preuve "
                "est donc double et sans appel."
            )
        ) as tracker:
            self.play(FadeIn(preuve))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(preuve))

        # --- Piège à éviter : la photolyse n'est qu'une étape -------------------
        piege = warning_box(
            Text(
                _wrap(
                    "Piège à éviter : la photolyse de l'eau n'est qu'une "
                    "étape de la phase claire, pas toute la "
                    "photosynthèse. Les électrons et les protons "
                    "libérés ne s'accumulent pas librement : ils servent "
                    "immédiatement à fabriquer l'ATP et le NADPH,H+ "
                    "(scène suivante).",
                    width=54,
                ),
                font_size=20,
            ),
            box_width=12.0,
        )
        piege.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Attention : la photolyse de l'eau n'est qu'une étape de "
                "la phase claire, pas toute la photosynthèse à elle "
                "seule. Les électrons et les protons qu'elle libère ne "
                "s'accumulent pas librement dans le thylakoïde : ils "
                "servent immédiatement à fabriquer l'ATP et le "
                "NADPH,H plus, ce que nous verrons dans la scène "
                "suivante."
            )
        ) as tracker:
            self.play(FadeIn(piege))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(titre), FadeOut(piege))
