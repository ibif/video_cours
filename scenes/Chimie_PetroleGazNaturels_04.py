"""
scenes/Chimie_PetroleGazNaturels_04.py — Chapitre 5 « Pétrole et gaz
naturels » (1ereC, Chimie), scène 04.

§ 4. Les principales fractions et leurs usages : tableau des 6 fractions
issues de la distillation (gaz de raffinerie/GPL C₁-C₄, essences
C₅-C₁₀, kérosène C₁₀-C₁₄, gasoil C₁₄-C₂₀, fiouls lourds C₂₀-C₃₅, bitume
>C₃₅) avec intervalles d'ébullition et usages, et piège : la
distillation est une séparation physique, pas une réaction chimique.
Source : 1ereC/Chimie.pdf, chapitre 5, page 48.
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
    Table,
    Text,
    VGroup,
    Write,
    config,
)

from shapes.base_scene import NotionScene
from shapes.boxes import scene_title, warning_box


def _wrap(text: str, width: int = 56) -> str:
    return "\n".join(textwrap.fill(line, width=width) for line in text.split("\n"))


def _fit(mobject, top_y):
    bas_visible = -config.frame_height / 2 + 0.25
    hauteur_dispo = top_y - bas_visible
    if mobject.height > hauteur_dispo:
        mobject.scale(hauteur_dispo / mobject.height, about_point=mobject.get_top())
    return mobject


class LesPrincipalesFractionsEtLeursUsages(NotionScene):
    def construct(self):
        titre = scene_title("4. Les principales fractions et leurs usages")
        titre.scale(0.55)
        titre.to_edge(UP)

        # --- Énoncé : la colonne livre 6 grandes fractions ----------------------
        intro = Text(
            _wrap(
                "La distillation fractionnée du pétrole brut livre six "
                "grandes fractions, classées de la plus légère, en haut "
                "de la colonne, à la plus lourde, en bas.",
                width=54,
            ),
            font_size=25,
            color=WHITE,
        )
        intro.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "La distillation fractionnée du pétrole brut livre six "
                "grandes fractions, classées de la plus légère, en haut "
                "de la colonne, à la plus lourde, tout en bas."
            )
        ) as tracker:
            self.play(Write(titre))
            self.play(FadeIn(intro))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(intro))

        # --- Raisonnement + exemple : tableau des 6 fractions -------------------
        rows = [
            ["Gaz de raffinerie / GPL", "C₁-C₄", "< 20°C", "Carburant GPL, chauffage"],
            ["Essences", "C₅-C₁₀", "20-180°C", "Carburant automobile"],
            ["Kérosène", "C₁₀-C₁₄", "180-250°C", "Carburant aviation"],
            ["Gasoil", "C₁₄-C₂₀", "250-350°C", "Carburant diesel, chauffage"],
            ["Fiouls lourds", "C₂₀-C₃₅", "350-450°C", "Centrales, navires"],
            ["Bitume", "> C₃₅", "> 450°C (résidu)", "Revêtement routier"],
        ]
        col_labels = ["Fraction", "Nb. de C", "Intervalle Téb", "Usage principal"]
        table = Table(
            rows,
            col_labels=[Text(c, font_size=16, weight="BOLD") for c in col_labels],
            element_to_mobject=Text,
            element_to_mobject_config={"font_size": 15},
            line_config={"color": WHITE, "stroke_width": 1},
            include_outer_lines=True,
            v_buff=0.22,
            h_buff=0.3,
        )
        table.get_entries().set_color(WHITE)
        table.get_col_labels().set_color(YELLOW)
        for line in table.get_horizontal_lines():
            line.set_color(WHITE)
        for line in table.get_vertical_lines():
            line.set_color(WHITE)
        table.next_to(titre, DOWN, buff=0.45)
        _fit(table, titre.get_bottom()[1] - 0.3)

        with self.voiceover(
            text=(
                "En tête de colonne, les gaz de raffinerie et le G-P-L, de "
                "un à quatre atomes de carbone, bouillant sous vingt "
                "degrés : carburant GPL et chauffage. Puis les essences, "
                "de cinq à dix carbones, entre vingt et cent quatre-vingts "
                "degrés : carburant automobile. Le kérosène, de dix à "
                "quatorze carbones, entre cent quatre-vingts et deux cent "
                "cinquante degrés : carburant pour l'aviation. Le gasoil, "
                "de quatorze à vingt carbones, entre deux cent cinquante "
                "et trois cent cinquante degrés : carburant diesel et "
                "chauffage. Les fiouls lourds, de vingt à trente-cinq "
                "carbones, jusqu'à quatre cent cinquante degrés : "
                "centrales thermiques et navires. Et tout en bas, résidu "
                "non vaporisé, le bitume, au-delà de trente-cinq "
                "carbones : revêtement routier."
            )
        ) as tracker:
            self.play(FadeIn(table))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(table))

        # --- Piège à éviter : distillation = séparation physique ----------------
        piege = warning_box(
            Text(
                _wrap(
                    "La distillation fractionnée est une séparation "
                    "PHYSIQUE : elle trie les molécules déjà présentes "
                    "dans le brut selon leur température d'ébullition. Ce "
                    "n'est PAS une réaction chimique, aucune nouvelle "
                    "molécule n'est créée.",
                    width=48,
                ),
                font_size=23,
            ),
        )
        piege.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Attention à ne pas confondre : la distillation "
                "fractionnée est une séparation physique. Elle trie les "
                "molécules déjà présentes dans le pétrole brut selon leur "
                "température d'ébullition. Ce n'est en aucun cas une "
                "réaction chimique : aucune nouvelle molécule n'est créée "
                "à cette étape."
            )
        ) as tracker:
            self.play(FadeIn(piege))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(piege), FadeOut(titre))
