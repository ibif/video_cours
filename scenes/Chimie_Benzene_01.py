"""
scenes/Chimie_Benzene_01.py — Chapitre 4 (1ereC, Chimie), scène 01.

§ Introduction : situation d'apprentissage (visite de la SIR à Abidjan),
historique (Faraday, 1825), formule brute C6H6, masse molaire M = 78 g/mol,
definition_box « hydrocarbure aromatique ».
Source : 1ereC/Chimie.pdf, chapitre 4, pages 35-36.
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
from shapes.boxes import definition_box, scene_title


def _wrap(text: str, width: int = 56) -> str:
    return "\n".join(textwrap.fill(line, width=width) for line in text.split("\n"))


def _fit(mobject, top_y):
    bas_visible = -config.frame_height / 2 + 0.25
    hauteur_dispo = top_y - bas_visible
    if mobject.height > hauteur_dispo:
        mobject.scale(hauteur_dispo / mobject.height, about_point=mobject.get_top())
    return mobject


class IntroductionFormuleBruteBenzene(NotionScene):
    def construct(self):
        titre = scene_title("1. Introduction et formule brute du benzène")
        titre.scale(0.5)
        titre.to_edge(UP)

        # --- Énoncé : situation d'apprentissage -------------------------------
        situation = Text(
            _wrap(
                "Lors d'une visite de la Société Ivoirienne de Raffinage "
                "(SIR) à Abidjan, des élèves apprennent que le pétrole "
                "brut contient un hydrocarbure très particulier : le "
                "benzène, utilisé comme matière première dans de "
                "nombreuses synthèses industrielles.",
                width=54,
            ),
            font_size=25,
            color=WHITE,
        )
        situation.next_to(titre, DOWN, buff=0.5)
        _fit(situation, titre.get_bottom()[1] - 0.4)

        with self.voiceover(
            text=(
                "Lors d'une visite de la Société Ivoirienne de Raffinage, "
                "la SIR, à Abidjan, des élèves apprennent que le pétrole "
                "brut contient un hydrocarbure très particulier : le "
                "benzène, utilisé comme matière première dans de "
                "nombreuses synthèses industrielles. Mais que sait-on "
                "vraiment de cette molécule ?"
            )
        ) as tracker:
            self.play(Write(titre))
            self.play(FadeIn(situation))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(situation))

        # --- Animation du raisonnement : un peu d'histoire ---------------------
        entete = Text("1825 — la découverte de Faraday", font_size=26, color=YELLOW, weight="BOLD")
        entete.next_to(titre, DOWN, buff=0.45)

        histoire = Text(
            _wrap(
                "En 1825, le physicien et chimiste britannique Michael "
                "Faraday isole pour la première fois le benzène à partir "
                "d'un résidu huileux obtenu lors de la fabrication de gaz "
                "d'éclairage. Il en détermine la composition : un "
                "hydrocarbure très riche en carbone.",
                width=52,
            ),
            font_size=24,
            color=WHITE,
        )
        histoire.next_to(entete, DOWN, buff=0.4)
        groupe_histoire = VGroup(entete, histoire)
        _fit(groupe_histoire, titre.get_bottom()[1] - 0.4)

        with self.voiceover(
            text=(
                "C'est en dix-huit cent vingt-cinq que le physicien et "
                "chimiste britannique Michael Faraday isole pour la "
                "première fois le benzène, à partir d'un résidu huileux "
                "obtenu lors de la fabrication du gaz d'éclairage. Il en "
                "détermine la composition : un hydrocarbure étonnamment "
                "riche en carbone."
            )
        ) as tracker:
            self.play(FadeIn(entete))
            self.play(FadeIn(histoire))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(groupe_histoire))

        # --- Exemple traité : formule brute et masse molaire --------------------
        entete2 = Text("Formule brute et masse molaire", font_size=26, color=YELLOW, weight="BOLD")
        entete2.next_to(titre, DOWN, buff=0.4)

        formule = MathTex(r"C_6H_6", font_size=64, color=WHITE)
        masse = MathTex(r"M(C_6H_6) = 6 \times 12 + 6 \times 1 = 78\ g.mol^{-1}", font_size=34, color=WHITE)
        bloc = VGroup(formule, masse).arrange(DOWN, buff=0.5)
        bloc.next_to(entete2, DOWN, buff=0.5)

        groupe_formule = VGroup(entete2, bloc)

        with self.voiceover(
            text=(
                "Après analyse élémentaire, la formule brute du benzène "
                "est établie : C six H six. Sa masse molaire vaut six fois "
                "douze, plus six fois un, soit soixante-dix-huit grammes "
                "par mole."
            )
        ) as tracker:
            self.play(FadeIn(entete2))
            self.play(Write(formule))
            self.play(Write(masse))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(groupe_formule))

        # --- À retenir : definition_box « hydrocarbure aromatique » ------------
        definition = definition_box(
            Text(
                _wrap(
                    "Le benzène C6H6 est le représentant le plus simple "
                    "des hydrocarbures aromatiques : une famille de "
                    "composés organiques cycliques possédant des "
                    "propriétés chimiques particulières, très différentes "
                    "de celles des alcanes, alcènes ou alcynes.",
                    width=48,
                ),
                font_size=25,
            ),
        )
        definition.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Retenons donc ceci : le benzène, de formule C six H six, "
                "est le représentant le plus simple des hydrocarbures "
                "aromatiques, une famille de composés organiques "
                "cycliques aux propriétés chimiques bien particulières, "
                "très différentes de celles des alcanes, des alcènes ou "
                "des alcynes déjà étudiés. C'est cette originalité que "
                "nous allons explorer dans ce chapitre."
            )
        ) as tracker:
            self.play(FadeIn(definition))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(definition), FadeOut(titre))
