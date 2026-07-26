"""
scenes/Chimie_GeneralitesComposesOrganiques_02.py — Chapitre 1 (1ereC, Chimie), scène 02.

§ 1.3 La covalence (valence) des éléments C, H, O, N, et la caténation du
carbone : pourquoi il existe tant de composés organiques (chaînes de
longueur illimitée, linéaires, ramifiées ou cycliques).
Source : 1ereC/Chimie.pdf, page 5.
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
    FadeIn,
    FadeOut,
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


class CovalenceEtCatenation(NotionScene):
    def construct(self):
        titre = scene_title("1.3 — La covalence et la caténation du carbone")
        titre.scale(0.55)
        titre.to_edge(UP)

        # --- Énoncé : une chimie de covalence -----------------------------
        intro = Text(
            _wrap(
                "Les composés organiques sont des assemblages d'atomes "
                "liés par des liaisons covalentes : la chimie organique "
                "est essentiellement une chimie de covalence.",
                width=54,
            ),
            font_size=25,
            color=WHITE,
        )
        intro.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Les composés organiques sont des assemblages d'atomes "
                "liés par des liaisons covalentes : la chimie organique "
                "est essentiellement une chimie de covalence."
            )
        ) as tracker:
            self.play(Write(titre))
            self.play(FadeIn(intro))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(intro))

        # --- Animation du raisonnement : définition + tableau des covalences ---
        definition = definition_box(
            Text(
                _wrap(
                    "La covalence (ou valence) d'un atome est le nombre de "
                    "liaisons de covalence qu'il peut former avec d'autres "
                    "atomes.",
                    width=48,
                ),
                font_size=26,
            ),
        )
        definition.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "La covalence, ou valence, d'un atome est le nombre de "
                "liaisons de covalence qu'il peut former avec d'autres "
                "atomes."
            )
        ) as tracker:
            self.play(FadeIn(definition))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(definition))

        entete_tab = Text("Covalences à retenir en chimie organique", font_size=25, color=YELLOW, weight="BOLD")
        entete_tab.next_to(titre, DOWN, buff=0.4)

        lignes = VGroup(
            MathTex(r"C : 4", font_size=32, color=WHITE),
            MathTex(r"H : 1", font_size=32, color=WHITE),
            MathTex(r"O : 2", font_size=32, color=WHITE),
            MathTex(r"N : 3", font_size=32, color=WHITE),
        ).arrange(RIGHT, buff=0.9)
        lignes.next_to(entete_tab, DOWN, buff=0.5)

        groupe_tab = VGroup(entete_tab, lignes)

        with self.voiceover(
            text=(
                "Dans les molécules organiques, on retiendra quatre "
                "valeurs : le carbone forme quatre liaisons, l'hydrogène "
                "une seule liaison, l'oxygène deux liaisons, et l'azote "
                "trois liaisons."
            )
        ) as tracker:
            self.play(FadeIn(entete_tab))
            self.play(FadeIn(lignes))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(groupe_tab))

        # --- Exemple traité : la caténation, chaînes de carbone ----------------
        entete_cat = Text("La caténation : le carbone s'enchaîne avec lui-même", font_size=23, color=YELLOW, weight="BOLD")
        entete_cat.scale(0.95)
        entete_cat.next_to(titre, DOWN, buff=0.4)

        # petit schéma : 3 types de chaînes en pointillés simples (C-C-C-C)
        def make_chain(n=4):
            atomes = VGroup(*[MathTex("C", font_size=30, color=BLUE) for _ in range(n)])
            atomes.arrange(RIGHT, buff=0.6)
            liaisons = VGroup(
                *[
                    Line(atomes[i].get_right(), atomes[i + 1].get_left(), color=WHITE, stroke_width=3)
                    for i in range(n - 1)
                ]
            )
            return VGroup(liaisons, atomes)

        chaine_lin = make_chain(5)
        label_lin = Text("linéaire", font_size=18, color=WHITE)
        bloc_lin = VGroup(chaine_lin, label_lin).arrange(DOWN, buff=0.2)

        # ramifiée : chaîne principale + une branche
        principale = VGroup(*[MathTex("C", font_size=30, color=BLUE) for _ in range(4)])
        principale.arrange(RIGHT, buff=0.6)
        branche = MathTex("C", font_size=30, color=BLUE)
        branche.next_to(principale[1], UP, buff=0.5)
        liaisons_r = VGroup(
            *[
                Line(principale[i].get_right(), principale[i + 1].get_left(), color=WHITE, stroke_width=3)
                for i in range(3)
            ],
            Line(principale[1].get_top(), branche.get_bottom(), color=WHITE, stroke_width=3),
        )
        chaine_ram = VGroup(liaisons_r, principale, branche)
        label_ram = Text("ramifiée", font_size=18, color=WHITE)
        bloc_ram = VGroup(chaine_ram, label_ram).arrange(DOWN, buff=0.35)

        # cyclique : hexagone de C
        import numpy as np

        n_cycle = 6
        rayon = 0.6
        sommets = [
            np.array([rayon * np.cos(2 * np.pi * k / n_cycle), rayon * np.sin(2 * np.pi * k / n_cycle), 0])
            for k in range(n_cycle)
        ]
        atomes_cycle = VGroup(*[MathTex("C", font_size=26, color=BLUE).move_to(p) for p in sommets])
        liaisons_cycle = VGroup(
            *[
                Line(sommets[k], sommets[(k + 1) % n_cycle], color=WHITE, stroke_width=3)
                for k in range(n_cycle)
            ]
        )
        chaine_cyc = VGroup(liaisons_cycle, atomes_cycle)
        label_cyc = Text("cyclique", font_size=18, color=WHITE)
        bloc_cyc = VGroup(chaine_cyc, label_cyc).arrange(DOWN, buff=0.35)

        schema_chaines = VGroup(bloc_lin, bloc_ram, bloc_cyc).arrange(RIGHT, buff=1.0, aligned_edge=DOWN)
        schema_chaines.next_to(entete_cat, DOWN, buff=0.5)
        _fit(schema_chaines, entete_cat.get_bottom()[1] - 0.4)

        groupe_cat = VGroup(entete_cat, schema_chaines)

        with self.voiceover(
            text=(
                "Le carbone, tétravalent, possède une propriété "
                "remarquable : il peut s'enchaîner avec lui-même par des "
                "liaisons simples, doubles ou triples, et former des "
                "chaînes de longueur presque illimitée, linéaires, "
                "ramifiées ou cycliques. C'est ce qu'on appelle la "
                "caténation."
            )
        ) as tracker:
            self.play(FadeIn(entete_cat))
            self.play(FadeIn(schema_chaines))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(groupe_cat))

        # --- À retenir : pourquoi tant de composés organiques -----------------
        propriete = property_box(
            Text(
                _wrap(
                    "Grâce à la caténation du carbone, on connaît "
                    "aujourd'hui plusieurs millions de composés "
                    "organiques, contre seulement quelques milliers de "
                    "composés minéraux.",
                    width=48,
                ),
                font_size=25,
            ),
        )
        propriete.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Cette caténation explique que l'on connaisse aujourd'hui "
                "plusieurs millions de composés organiques, contre "
                "seulement quelques milliers de composés minéraux."
            )
        ) as tracker:
            self.play(FadeIn(propriete))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(propriete), FadeOut(titre))
