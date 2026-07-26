"""
scenes/Chimie_EsterificationHydrolyse_04.py — Chapitre 8 « Estérification et
hydrolyse d'un ester » (1ereC, Chimie), scène 04.

§ Caractéristiques de l'estérification (2/2) : limitée par l'hydrolyse.
Constat expérimental (≈2/3 mol d'ester pour un mélange équimolaire),
mécanisme (hydrolyse inverse dès apparition d'ester+eau), definition_box
équilibre d'estérification-hydrolyse (équilibre dynamique, 4 espèces
coexistent).
Source : 1ereC/Chimie.pdf, chapitre 8, pages 77-78.
"""

import textwrap

from manim import (
    DOWN,
    UP,
    WHITE,
    YELLOW,
    GREEN,
    RED,
    FadeIn,
    FadeOut,
    MathTex,
    Text,
    VGroup,
    Write,
    config,
)

from shapes.base_scene import NotionScene
from shapes.boxes import definition_box, scene_title


def _wrap(text: str, width: int = 56) -> str:
    return "\n".join(textwrap.fill(line, width=width) for line in text.split("\n"))


def _fit(mobject, top_y):
    bas_visible = -config.frame_height / 2 + 0.25
    hauteur_dispo = top_y - bas_visible
    if mobject.height > hauteur_dispo:
        mobject.scale(hauteur_dispo / mobject.height, about_point=mobject.get_top())
    return mobject


class CaracteristiquesLimiteeHydrolyse(NotionScene):
    def construct(self):
        titre = scene_title("4. Caractéristiques (2/2) : une réaction LIMITÉE")
        titre.scale(0.48)
        titre.to_edge(UP)

        # --- Énoncé -----------------------------------------------------------
        enonce = Text(
            _wrap(
                "Si l'on attend suffisamment longtemps, ou que l'on "
                "chauffe à reflux, l'estérification finit-elle par "
                "transformer TOUT l'acide et TOUT l'alcool en ester ? "
                "L'expérience répond par la négative.",
                width=54,
            ),
            font_size=24,
            color=WHITE,
        )
        enonce.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Si l'on attend suffisamment longtemps, ou que l'on "
                "chauffe à reflux, l'estérification finit-elle par "
                "transformer tout l'acide et tout l'alcool en ester ? "
                "L'expérience répond par la négative."
            )
        ) as tracker:
            self.play(Write(titre))
            self.play(FadeIn(enonce))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(enonce))

        # --- Raisonnement : constat expérimental -----------------------------------
        entete = Text("Constat expérimental", font_size=26, color=YELLOW, weight="BOLD")
        entete.next_to(titre, DOWN, buff=0.4)

        constat = Text(
            _wrap(
                "Pour un mélange équimolaire d'un acide carboxylique et "
                "d'un alcool primaire (même quantité de matière n de "
                "chacun), on ne récupère à l'équilibre qu'environ "
                "2/3 de mol d'ester : il reste toujours de "
                "l'acide et de l'alcool n'ayant pas réagi.",
                width=48,
            ),
            font_size=23,
            color=WHITE,
        )
        constat.next_to(entete, DOWN, buff=0.4)
        groupe = VGroup(entete, constat)
        _fit(groupe, titre.get_bottom()[1] - 0.4)

        with self.voiceover(
            text=(
                "Le constat expérimental est net : pour un mélange "
                "équimolaire d'un acide carboxylique et d'un alcool "
                "primaire, c'est-à-dire la même quantité de matière n de "
                "chacun, on ne récupère à l'équilibre qu'environ deux "
                "tiers de mole d'ester. Il reste toujours de l'acide et "
                "de l'alcool n'ayant pas réagi, quel que soit le temps "
                "d'attente."
            )
        ) as tracker:
            self.play(FadeIn(entete))
            self.play(FadeIn(constat))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(groupe))

        # --- Exemple traité : le mécanisme (hydrolyse inverse) ----------------------
        entete2 = Text("Pourquoi ? Le mécanisme en jeu", font_size=24, color=YELLOW, weight="BOLD")
        entete2.next_to(titre, DOWN, buff=0.35)

        directe = MathTex(
            r"acide + alcool \xrightarrow{\text{estérification}} ester + eau",
            font_size=26,
            color=GREEN,
        )
        inverse = MathTex(
            r"ester + eau \xrightarrow{\text{hydrolyse}} acide + alcool",
            font_size=26,
            color=RED,
        )
        explication = Text(
            _wrap(
                "Dès que de l'ester et de l'eau apparaissent, la réaction "
                "inverse — l'hydrolyse — démarre elle aussi et consomme "
                "une partie de l'ester formé. Les deux réactions "
                "finissent par se compenser exactement.",
                width=48,
            ),
            font_size=21,
            color=WHITE,
        )
        bloc2 = VGroup(directe, inverse, explication).arrange(DOWN, buff=0.35)
        bloc2.next_to(entete2, DOWN, buff=0.35)
        groupe2 = VGroup(entete2, bloc2)
        _fit(groupe2, titre.get_bottom()[1] - 0.35)

        with self.voiceover(
            text=(
                "Ce résultat s'explique par un mécanisme simple. Dès que "
                "de l'ester et de l'eau apparaissent dans le milieu, ces "
                "deux espèces peuvent elles-mêmes réagir en sens inverse "
                "— c'est l'hydrolyse — pour régénérer de l'acide et de "
                "l'alcool. À mesure que la réaction directe avance, la "
                "réaction inverse, l'hydrolyse, s'intensifie, jusqu'à ce "
                "que les deux vitesses deviennent égales : le système "
                "n'évolue alors plus, macroscopiquement."
            )
        ) as tracker:
            self.play(FadeIn(entete2))
            self.play(Write(directe))
            self.play(Write(inverse))
            self.play(FadeIn(explication))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(groupe2))

        # --- À retenir : definition_box équilibre ------------------------------------
        definition = definition_box(
            VGroup(
                Text(
                    _wrap(
                        "L'estérification est une réaction LIMITÉE : elle "
                        "s'arrête à un ÉQUILIBRE dynamique entre "
                        "estérification et hydrolyse, où les 4 espèces — "
                        "acide, alcool, ester, eau — coexistent en "
                        "proportions constantes.",
                        width=48,
                    ),
                    font_size=23,
                ),
                MathTex(
                    r"acide + alcool \;\rightleftharpoons\; ester + eau",
                    font_size=28,
                ),
            ).arrange(DOWN, buff=0.35),
        )
        definition.next_to(titre, DOWN, buff=0.4)
        _fit(definition, titre.get_bottom()[1] - 0.4)

        with self.voiceover(
            text=(
                "Retenons donc cette troisième caractéristique : "
                "l'estérification est une réaction limitée. Elle "
                "s'arrête à un équilibre dynamique entre estérification "
                "et hydrolyse, où les quatre espèces — acide, alcool, "
                "ester et eau — coexistent en proportions constantes, "
                "d'où la double flèche de l'équation générale."
            )
        ) as tracker:
            self.play(FadeIn(definition))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(definition), FadeOut(titre))
