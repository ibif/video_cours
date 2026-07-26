"""
scenes/Chimie_PetroleGazNaturels_02.py — Chapitre 5 « Pétrole et gaz
naturels » (1ereC, Chimie), scène 02.

§ 2. Composition du pétrole brut et du gaz naturel : définition d'un
hydrocarbure, tableau des familles chimiques présentes dans le brut
(alcanes majoritaires, cycloalcanes, aromatiques, alcènes rares),
composition du gaz naturel (≈90% méthane + éthane/propane/butane), et
piège classique gaz naturel (méthane) vs GPL (butane/propane du
raffinage). Source : 1ereC/Chimie.pdf, chapitre 5, pages 46-47.
"""

import textwrap

from manim import (
    DOWN,
    LEFT,
    RIGHT,
    UP,
    WHITE,
    YELLOW,
    BLUE,
    GREEN,
    FadeIn,
    FadeOut,
    Rectangle,
    Table,
    Text,
    VGroup,
    Write,
    config,
)

from shapes.base_scene import NotionScene
from shapes.boxes import definition_box, scene_title, warning_box


def _wrap(text: str, width: int = 56) -> str:
    return "\n".join(textwrap.fill(line, width=width) for line in text.split("\n"))


def _fit(mobject, top_y):
    bas_visible = -config.frame_height / 2 + 0.25
    hauteur_dispo = top_y - bas_visible
    if mobject.height > hauteur_dispo:
        mobject.scale(hauteur_dispo / mobject.height, about_point=mobject.get_top())
    return mobject


def _barre(label, pourcentage, largeur_max=6.0, couleur=BLUE):
    barre = Rectangle(
        width=max(largeur_max * pourcentage / 100, 0.15),
        height=0.45,
        fill_color=couleur,
        fill_opacity=0.9,
        stroke_color=WHITE,
        stroke_width=1,
    )
    barre.align_to(barre, LEFT)
    texte = Text(f"{label} — {pourcentage}%", font_size=18, color=WHITE)
    ligne = VGroup(barre, texte).arrange(RIGHT, buff=0.3)
    return ligne


class CompositionDuPetroleBrutEtDuGazNaturel(NotionScene):
    def construct(self):
        titre = scene_title("2. Composition du pétrole brut et du gaz naturel")
        titre.scale(0.5)
        titre.to_edge(UP)

        # --- Énoncé : définition d'un hydrocarbure ------------------------------
        definition = definition_box(
            Text(
                _wrap(
                    "Un hydrocarbure est un composé organique dont la "
                    "molécule ne contient que des atomes de carbone C et "
                    "d'hydrogène H, de formule générale CₓHᵧ.",
                    width=48,
                ),
                font_size=25,
            ),
        )
        definition.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Un hydrocarbure est un composé organique dont la "
                "molécule ne contient que des atomes de carbone et "
                "d'hydrogène, de formule générale C indice x, H indice y. "
                "Le pétrole brut et le gaz naturel sont tous deux des "
                "mélanges complexes d'hydrocarbures. Voyons leur "
                "composition en détail."
            )
        ) as tracker:
            self.play(Write(titre))
            self.play(FadeIn(definition))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(definition))

        # --- Raisonnement : les familles du pétrole brut (tableau) -------------
        entete_tab = Text("Les familles chimiques du pétrole brut", font_size=24, color=YELLOW, weight="BOLD")
        entete_tab.next_to(titre, DOWN, buff=0.35)

        rows = [
            ["Alcanes", "linéaires/ramifiés", "majoritaire"],
            ["Cycloalcanes", "cycliques saturés", "importante"],
            ["Aromatiques", "cycles type benzène", "présente"],
            ["Alcènes", "insaturés (C=C)", "rare"],
        ]
        col_labels = ["Famille", "Description", "Proportion"]
        table = Table(
            rows,
            col_labels=[Text(c, font_size=18, weight="BOLD") for c in col_labels],
            element_to_mobject=Text,
            element_to_mobject_config={"font_size": 17},
            line_config={"color": WHITE, "stroke_width": 1},
            include_outer_lines=True,
            v_buff=0.25,
            h_buff=0.4,
        )
        table.get_entries().set_color(WHITE)
        table.get_col_labels().set_color(YELLOW)
        for line in table.get_horizontal_lines():
            line.set_color(WHITE)
        for line in table.get_vertical_lines():
            line.set_color(WHITE)
        table.next_to(entete_tab, DOWN, buff=0.4)
        _fit(table, entete_tab.get_bottom()[1] - 0.3)

        with self.voiceover(
            text=(
                "Le pétrole brut est un mélange de plusieurs familles "
                "d'hydrocarbures. Les alcanes, linéaires ou ramifiés, sont "
                "toujours majoritaires. Les cycloalcanes, des alcanes "
                "cycliques, forment une proportion importante. Les "
                "hydrocarbures aromatiques, à cycles de type benzène, sont "
                "également présents. Les alcènes, insaturés, restent en "
                "revanche très rares dans le brut."
            )
        ) as tracker:
            self.play(FadeIn(entete_tab))
            self.play(FadeIn(table))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(entete_tab), FadeOut(table))

        # --- Exemple traité : composition du gaz naturel ------------------------
        entete_gaz = Text("Composition typique du gaz naturel", font_size=24, color=YELLOW, weight="BOLD")
        entete_gaz.next_to(titre, DOWN, buff=0.4)

        barres = VGroup(
            _barre("Méthane CH₄", 90, couleur=GREEN),
            _barre("Éthane C₂H₆", 5, couleur=BLUE),
            _barre("Propane C₃H₈", 3, couleur=BLUE),
            _barre("Butane C₄H₁₀", 2, couleur=BLUE),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.3)
        barres.next_to(entete_gaz, DOWN, buff=0.45)

        groupe_gaz = VGroup(entete_gaz, barres)

        with self.voiceover(
            text=(
                "Le gaz naturel, lui, est composé à environ quatre-vingt-dix "
                "pour cent de méthane, C-H-4. Le reste se répartit entre "
                "l'éthane, le propane et le butane, présents en bien plus "
                "faibles proportions. C'est cette très forte dominance du "
                "méthane qui caractérise le gaz naturel."
            )
        ) as tracker:
            self.play(FadeIn(entete_gaz))
            self.play(FadeIn(barres))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(groupe_gaz))

        # --- Piège à éviter : gaz naturel (méthane) vs GPL (butane/propane) ----
        piege = warning_box(
            Text(
                _wrap(
                    "Ne confondez pas le gaz naturel (essentiellement du "
                    "méthane, extrait directement d'un gisement) avec le "
                    "GPL, gaz de pétrole liquéfié (butane et propane), qui "
                    "est lui obtenu lors du raffinage du pétrole.",
                    width=48,
                ),
                font_size=23,
            ),
        )
        piege.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Attention à un piège fréquent : ne confondez jamais le "
                "gaz naturel, essentiellement composé de méthane et "
                "extrait directement d'un gisement, avec le G-P-L, le gaz "
                "de pétrole liquéfié, composé de butane et de propane, qui "
                "est lui obtenu lors du raffinage du pétrole, et non "
                "extrait tel quel du sous-sol."
            )
        ) as tracker:
            self.play(FadeIn(piege))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(piege), FadeOut(titre))
