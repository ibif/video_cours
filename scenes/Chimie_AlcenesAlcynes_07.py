"""
scenes/Chimie_AlcenesAlcynes_07.py — Chapitre 3 (1ereC, Chimie), scène 07.

Nomenclature des alcynes : suffixe -yne (même méthode que pour les alcènes,
en remplaçant -ène par -yne), tableau d'exemples (éthyne, prop-1-yne,
but-1-yne, but-2-yne, 4-méthylpent-2-yne), et mise en garde : pas de
stéréoisomérie Z/E pour les alcynes (molécule linéaire).
Source : 1ereC/Chimie.pdf, chapitre 3, page 30.
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
from shapes.boxes import method_box, scene_title, warning_box


def _wrap(text: str, width: int = 56) -> str:
    return "\n".join(textwrap.fill(line, width=width) for line in text.split("\n"))


def _fit(mobject, top_y):
    bas_visible = -config.frame_height / 2 + 0.25
    hauteur_dispo = top_y - bas_visible
    if mobject.height > hauteur_dispo:
        mobject.scale(hauteur_dispo / mobject.height, about_point=mobject.get_top())
    return mobject


class NomenclatureAlcynes(NotionScene):
    def construct(self):
        titre = scene_title("7. Nomenclature des alcynes")
        titre.scale(0.55)
        titre.to_edge(UP)

        # --- Énoncé : même méthode, suffixe différent -----------------------------
        intro = Text(
            _wrap(
                "La méthode de nomenclature des alcynes reprend "
                "exactement celle des alcènes : seul le suffixe change, "
                "-yne au lieu de -ène, pour signaler la triple liaison.",
                width=54,
            ),
            font_size=24,
            color=WHITE,
        )
        intro.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "La méthode de nomenclature des alcynes reprend "
                "exactement celle des alcènes : la chaîne principale doit "
                "contenir la triple liaison, la numérotation lui donne la "
                "priorité, et les ramifications se placent par ordre "
                "alphabétique. Seul le suffixe change : yne au lieu de "
                "ène, pour signaler la triple liaison."
            )
        ) as tracker:
            self.play(Write(titre))
            self.play(FadeIn(intro))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(intro))

        # --- Animation du raisonnement : rappel méthode + suffixe -----------------
        methode = method_box(
            VGroup(
                Text("1. Chaîne principale contenant la triple liaison.", font_size=22),
                Text("2. Suffixe -yne, indice de position le plus petit.", font_size=22),
                Text("3. Numérotation donnant priorité à la triple liaison.", font_size=22),
                Text("4. Ramifications par ordre alphabétique.", font_size=22),
            ).arrange(DOWN, buff=0.25, aligned_edge=LEFT),
            box_width=11.0,
        )
        methode.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "On retrouve donc les quatre mêmes étapes : repérer la "
                "chaîne principale contenant la triple liaison, choisir "
                "le suffixe yne avec l'indice de position le plus petit "
                "possible, numéroter en donnant la priorité à la triple "
                "liaison, puis placer les ramifications par ordre "
                "alphabétique."
            )
        ) as tracker:
            self.play(FadeIn(methode))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(methode))

        # --- Exemple traité : tableau des alcynes usuels --------------------------
        entete = Text("Alcynes à connaître", font_size=24, color=YELLOW, weight="BOLD")
        entete.next_to(titre, DOWN, buff=0.35)

        tableau = VGroup(
            MathTex(r"HC \equiv CH \; : \; \text{éthyne (acétylène)}", font_size=24),
            MathTex(r"HC \equiv C-CH_3 \; : \; \text{prop-1-yne}", font_size=24),
            MathTex(r"HC \equiv C-CH_2-CH_3 \; : \; \text{but-1-yne}", font_size=24),
            MathTex(r"CH_3-C \equiv C-CH_3 \; : \; \text{but-2-yne}", font_size=24),
            MathTex(r"CH_3-C \equiv C-CH(CH_3)-CH_3 \; : \; \text{4-méthylpent-2-yne}", font_size=22),
        ).arrange(DOWN, buff=0.28, aligned_edge=LEFT)
        tableau.next_to(entete, DOWN, buff=0.4)
        _fit(tableau, entete.get_bottom()[1] - 0.4)

        groupe = VGroup(entete, tableau)

        with self.voiceover(
            text=(
                "Voici les principaux alcynes à connaître : H C triple "
                "liaison C H, c'est l'éthyne, plus connu sous le nom "
                "d'acétylène. H C triple liaison C, C H trois, le "
                "prop-un-yne. H C triple liaison C, C H deux, C H trois, "
                "le but-un-yne. C H trois, triple liaison, C H trois, le "
                "but-deux-yne. Et enfin une molécule ramifiée : le "
                "quatre-méthylpent-deux-yne."
            )
        ) as tracker:
            self.play(FadeIn(entete))
            self.play(FadeIn(tableau))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(groupe))

        # --- À retenir --------------------------------------------------------------
        retenir = Text(
            _wrap(
                "Comme pour les alcènes, le suffixe -yne s'accompagne "
                "toujours de l'indice de position de la triple liaison, "
                "sauf lorsqu'un seul emplacement est possible (éthyne, "
                "propyne).",
                width=52,
            ),
            font_size=24,
            color=WHITE,
        )
        retenir.next_to(titre, DOWN, buff=0.4)
        _fit(retenir, titre.get_bottom()[1] - 0.4)

        with self.voiceover(
            text=(
                "Retenons l'essentiel : comme pour les alcènes, le "
                "suffixe yne s'accompagne toujours de l'indice de "
                "position de la triple liaison, sauf lorsqu'un seul "
                "emplacement est géométriquement possible, comme dans "
                "l'éthyne ou le propyne."
            )
        ) as tracker:
            self.play(FadeIn(retenir))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(retenir))

        # --- Pièges à éviter : pas de Z/E pour les alcynes -------------------------
        piege = warning_box(
            Text(
                _wrap(
                    "Un alcyne ne présente JAMAIS de stéréoisomérie Z/E : "
                    "sa molécule est linéaire (carbone digonal, 180°), il "
                    "n'y a donc pas de « côtés » de part et d'autre de la "
                    "triple liaison. Cette notion est réservée aux "
                    "alcènes.",
                    width=48,
                ),
                font_size=23,
            ),
        )
        piege.next_to(titre, DOWN, buff=0.4)
        _fit(piege, titre.get_bottom()[1] - 0.4)

        with self.voiceover(
            text=(
                "Attention à un piège très fréquent : un alcyne ne "
                "présente jamais de stéréoisomérie Z sur E. Sa molécule "
                "est linéaire, avec un carbone digonal à cent "
                "quatre-vingts degrés : il n'y a donc pas de côtés "
                "distincts de part et d'autre de la triple liaison. Cette "
                "notion de stéréoisomérie Z sur E reste réservée aux "
                "alcènes."
            )
        ) as tracker:
            self.play(FadeIn(piege))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(piege), FadeOut(titre))
