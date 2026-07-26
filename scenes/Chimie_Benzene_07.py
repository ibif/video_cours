"""
scenes/Chimie_Benzene_07.py — Chapitre 4 (1ereC, Chimie), scène 07.

§ Substitution électrophile — halogénation : definition_box réaction de
substitution électrophile (un H remplacé, noyau aromatique conservé),
bromation (C6H6 + Br2 → C6H5Br + HBr, catalyseur FeBr3 formé in situ via
limaille de fer), chloration analogue avec FeCl3, definition_box
catalyseur, schéma de la bromation.
Source : 1ereC/Chimie.pdf, chapitre 4, pages 40-41.
"""

import textwrap

import numpy as np

from manim import (
    DOWN,
    LEFT,
    RIGHT,
    UP,
    ORIGIN,
    PI,
    WHITE,
    YELLOW,
    RED,
    GREEN,
    FadeIn,
    FadeOut,
    Arrow,
    Circle,
    Dot,
    Line,
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


def _hex_vertices(center, radius=0.9, start_angle=PI / 2):
    pts = []
    for i in range(6):
        angle = start_angle + i * (PI / 3)
        pts.append(center + radius * np.array([np.cos(angle), np.sin(angle), 0.0]))
    return pts


def _cycle_benzenique(center, radius=0.9, color=WHITE):
    """Hybride de résonance simplifié : hexagone + cercle inscrit."""
    vertices = _hex_vertices(center, radius)
    edges = VGroup(*[Line(vertices[i], vertices[(i + 1) % 6], color=color, stroke_width=3) for i in range(6)])
    dots = VGroup(*[Dot(v, radius=0.045, color=color) for v in vertices])
    cercle = Circle(radius=radius * 0.55, color=color, stroke_width=2.5).move_to(center)
    return VGroup(edges, dots, cercle), vertices


class SubstitutionElectrophileHalogenation(NotionScene):
    def construct(self):
        titre = scene_title("7. Substitution électrophile : halogénation")
        titre.scale(0.45)
        titre.to_edge(UP)

        # --- Énoncé : definition_box réaction de substitution électrophile ------
        definition = definition_box(
            Text(
                _wrap(
                    "Une réaction de substitution électrophile sur le "
                    "benzène consiste à remplacer un atome d'hydrogène du "
                    "cycle par un autre groupe d'atomes, sans détruire le "
                    "noyau aromatique.",
                    width=48,
                ),
                font_size=25,
            ),
        )
        definition.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Une réaction de substitution électrophile sur le "
                "benzène consiste à remplacer un atome d'hydrogène du "
                "cycle par un autre groupe d'atomes, sans détruire le "
                "noyau aromatique, qui reste intact avec son nuage "
                "électronique délocalisé."
            )
        ) as tracker:
            self.play(Write(titre))
            self.play(FadeIn(definition))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(definition))

        # --- Animation du raisonnement : schéma de la bromation -------------------
        entete = Text("La bromation du benzène", font_size=25, color=YELLOW, weight="BOLD")
        entete.next_to(titre, DOWN, buff=0.4)

        benzene, _ = _cycle_benzenique(LEFT * 4.3)
        label_benzene = Text("benzène", font_size=18, color=WHITE).next_to(benzene, DOWN, buff=0.25)

        br2 = MathTex(r"+\ Br_2", font_size=30, color=RED).next_to(benzene, RIGHT, buff=0.5)
        catalyseur = Text("FeBr3 (catalyseur)", font_size=16, color=YELLOW)

        fleche = Arrow(LEFT * 0.6, RIGHT * 0.6, color=WHITE, buff=0)
        fleche.next_to(br2, RIGHT, buff=0.35)
        catalyseur.next_to(fleche, UP, buff=0.15)

        produit, sommets = _cycle_benzenique(RIGHT * 3.6)
        br_label = MathTex("Br", font_size=26, color=RED)
        br_label.next_to(sommets[0], UP, buff=0.15)
        liaison_br = Line(sommets[0], sommets[0] + UP * 0.35, color=RED, stroke_width=3)
        produit_complet = VGroup(produit, liaison_br, br_label)
        label_produit = Text("bromobenzène", font_size=18, color=WHITE).next_to(produit_complet, DOWN, buff=0.25)

        plus_hbr = MathTex(r"+\ HBr", font_size=28, color=WHITE)
        plus_hbr.next_to(produit_complet, RIGHT, buff=0.5)

        schema = VGroup(
            benzene, label_benzene, br2, fleche, catalyseur,
            produit_complet, label_produit, plus_hbr,
        )
        schema.move_to(ORIGIN)
        schema.next_to(entete, DOWN, buff=0.55)
        _fit(schema, entete.get_bottom()[1] - 0.5)

        groupe_schema = VGroup(entete, schema)

        with self.voiceover(
            text=(
                "Prenons l'exemple de la bromation. Le benzène réagit "
                "avec le dibrome, en présence de tribromure de fer comme "
                "catalyseur, formé in situ à partir de limaille de fer "
                "ajoutée au milieu réactionnel. Un atome d'hydrogène du "
                "cycle est remplacé par un atome de brome : on obtient du "
                "bromobenzène, avec dégagement de bromure d'hydrogène "
                "gazeux."
            )
        ) as tracker:
            self.play(FadeIn(entete))
            self.play(FadeIn(benzene), FadeIn(label_benzene))
            self.play(FadeIn(br2))
            self.play(FadeIn(fleche), FadeIn(catalyseur))
            self.play(FadeIn(produit_complet), FadeIn(label_produit))
            self.play(FadeIn(plus_hbr))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(groupe_schema))

        # --- Exemple traité : les équations bilans -------------------------------
        entete2 = Text("Bromation et chloration : deux équations analogues", font_size=21, color=YELLOW, weight="BOLD")
        entete2.next_to(titre, DOWN, buff=0.4)

        eq_brome = MathTex(
            r"C_6H_6 + Br_2 \xrightarrow{FeBr_3} C_6H_5Br + HBr",
            font_size=30,
            color=WHITE,
        )
        eq_chlore = MathTex(
            r"C_6H_6 + Cl_2 \xrightarrow{FeCl_3} C_6H_5Cl + HCl",
            font_size=30,
            color=GREEN,
        )
        equations = VGroup(eq_brome, eq_chlore).arrange(DOWN, buff=0.5)
        equations.next_to(entete2, DOWN, buff=0.5)
        groupe_eq = VGroup(entete2, equations)

        with self.voiceover(
            text=(
                "La chloration se déroule de façon tout à fait analogue : "
                "le benzène réagit avec le dichlore, en présence de "
                "trichlorure de fer comme catalyseur, pour donner du "
                "chlorobenzène et du chlorure d'hydrogène. Dans les deux "
                "cas, un halogène remplace un hydrogène, et le noyau "
                "aromatique est conservé."
            )
        ) as tracker:
            self.play(FadeIn(entete2))
            self.play(Write(eq_brome))
            self.play(Write(eq_chlore))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(groupe_eq))

        # --- À retenir : definition_box catalyseur --------------------------------
        definition2 = definition_box(
            Text(
                _wrap(
                    "Un catalyseur est une espèce chimique qui accélère "
                    "une réaction sans être consommée : elle se retrouve "
                    "intacte à la fin de la réaction et n'apparaît donc "
                    "pas dans l'équation bilan.",
                    width=48,
                ),
                font_size=24,
            ),
        )
        definition2.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Retenons enfin ce qu'est un catalyseur : une espèce "
                "chimique qui accélère une réaction sans être consommée. "
                "Elle se retrouve intacte à la fin de la réaction, et "
                "n'apparaît donc pas dans l'équation bilan — c'est "
                "pourquoi le tribromure de fer ou le trichlorure de fer "
                "ne figurent qu'au-dessus de la flèche de réaction, "
                "jamais parmi les réactifs ou les produits."
            )
        ) as tracker:
            self.play(FadeIn(definition2))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(definition2), FadeOut(titre))
