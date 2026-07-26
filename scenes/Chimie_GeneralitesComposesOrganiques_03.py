"""
scenes/Chimie_GeneralitesComposesOrganiques_03.py — Chapitre 1 (1ereC, Chimie), scène 03.

§ 2, 2.1 Analyse élémentaire qualitative : définition, et mise en évidence
du carbone et de l'hydrogène par combustion complète (schéma du dispositif
en 3 étapes : combustion → sulfate de cuivre anhydre qui bleuit (H2O) →
eau de chaux qui se trouble (CO2)), équations chimiques.
Source : 1ereC/Chimie.pdf, pages 5-6.
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
    GRAY,
    ORANGE,
    FadeIn,
    FadeOut,
    Arrow,
    Rectangle,
    MathTex,
    Text,
    VGroup,
    Write,
    config,
)

from shapes.base_scene import NotionScene
from shapes.boxes import definition_box, example_box, scene_title


def _wrap(text: str, width: int = 56) -> str:
    return "\n".join(textwrap.fill(line, width=width) for line in text.split("\n"))


def _fit(mobject, top_y):
    bas_visible = -config.frame_height / 2 + 0.25
    hauteur_dispo = top_y - bas_visible
    if mobject.height > hauteur_dispo:
        mobject.scale(hauteur_dispo / mobject.height, about_point=mobject.get_top())
    return mobject


def _flacon(label_text: str, contenu_color, label_color=WHITE):
    """Un petit flacon schématique (rectangle) surmonté d'une étiquette."""
    corps = Rectangle(width=1.6, height=1.1, color=WHITE, stroke_width=3, fill_color=contenu_color, fill_opacity=0.5)
    etiquette = Text(_wrap(label_text, width=16), font_size=16, color=label_color)
    etiquette.next_to(corps, DOWN, buff=0.15)
    return VGroup(corps, etiquette)


class MiseEnEvidenceCarboneHydrogene(NotionScene):
    def construct(self):
        titre = scene_title("2. Analyse élémentaire qualitative")
        titre.scale(0.6)
        titre.to_edge(UP)

        # --- Énoncé : définition de l'analyse élémentaire qualitative ---------
        definition = definition_box(
            Text(
                _wrap(
                    "L'analyse élémentaire qualitative d'un composé "
                    "organique a pour but d'identifier la nature des "
                    "éléments qui le constituent.",
                    width=48,
                ),
                font_size=26,
            ),
        )
        definition.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "L'analyse élémentaire qualitative d'un composé organique "
                "a pour but d'identifier la nature des éléments qui le "
                "constituent. Voyons d'abord comment mettre en évidence le "
                "carbone et l'hydrogène."
            )
        ) as tracker:
            self.play(Write(titre))
            self.play(FadeIn(definition))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(definition))

        # --- Animation du raisonnement : dispositif en 3 étapes ----------------
        entete = Text("Dispositif d'analyse élémentaire qualitative", font_size=23, color=YELLOW, weight="BOLD")
        entete.next_to(titre, DOWN, buff=0.35)

        # Étape 1 : combustion de l'échantillon
        flamme = ORANGE
        etape1_corps = Rectangle(width=1.6, height=1.1, color=WHITE, stroke_width=3)
        etape1_texte = Text("échantillon\n+ O₂, chauffage", font_size=15, color=WHITE)
        etape1_texte.move_to(etape1_corps.get_center())
        etape1 = VGroup(etape1_corps, etape1_texte)
        label1 = Text("1. Combustion", font_size=17, color=flamme)
        bloc1 = VGroup(etape1, label1).arrange(DOWN, buff=0.18)

        fleche1 = Arrow(LEFT * 0.4, RIGHT * 0.4, color=WHITE, buff=0)

        # Étape 2 : sulfate de cuivre anhydre (blanc -> bleu)
        bloc2 = _flacon("sulfate de cuivre\nanhydre : blanc → bleu", BLUE)
        label2 = Text("2. Détection de H₂O", font_size=17, color=BLUE)
        bloc2_full = VGroup(bloc2, label2).arrange(DOWN, buff=0.18)

        fleche2 = Arrow(LEFT * 0.4, RIGHT * 0.4, color=WHITE, buff=0)

        # Étape 3 : eau de chaux (se trouble)
        bloc3 = _flacon("eau de chaux :\nse trouble", GRAY)
        label3 = Text("3. Détection de CO₂", font_size=17, color=GRAY)
        bloc3_full = VGroup(bloc3, label3).arrange(DOWN, buff=0.18)

        schema = VGroup(bloc1, fleche1, bloc2_full, fleche2, bloc3_full).arrange(RIGHT, buff=0.35, aligned_edge=UP)
        schema.next_to(entete, DOWN, buff=0.45)
        _fit(schema, entete.get_bottom()[1] - 0.4)

        groupe_schema = VGroup(entete, schema)

        with self.voiceover(
            text=(
                "On réalise la combustion d'un échantillon du composé "
                "organique dans le dioxygène de l'air. Les gaz produits "
                "traversent ensuite, successivement, deux réactifs : "
                "d'abord du sulfate de cuivre anhydre, blanc, qui bleuit — "
                "il s'est formé de l'eau ; puis de l'eau de chaux, "
                "c'est-à-dire une solution d'hydroxyde de calcium, qui se "
                "trouble — il s'est formé du dioxyde de carbone."
            )
        ) as tracker:
            self.play(FadeIn(entete))
            self.play(FadeIn(bloc1))
            self.play(FadeIn(fleche1), FadeIn(bloc2_full))
            self.play(FadeIn(fleche2), FadeIn(bloc3_full))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(groupe_schema))

        # --- Exemple traité : les équations chimiques mises en jeu -------------
        entete_eq = Text("Les réactions mises en jeu", font_size=25, color=YELLOW, weight="BOLD")
        entete_eq.next_to(titre, DOWN, buff=0.4)

        eq1 = MathTex(
            r"CuSO_4 \; (blanc) + 5H_2O \rightarrow CuSO_4, 5H_2O \; (bleu)",
            font_size=32,
            color=BLUE,
        )
        eq2 = MathTex(
            r"CO_2 + Ca(OH)_2 \rightarrow CaCO_3 + H_2O",
            font_size=32,
            color=GRAY,
        )
        equations = VGroup(eq1, eq2).arrange(DOWN, buff=0.5)
        equations.next_to(entete_eq, DOWN, buff=0.5)

        groupe_eq = VGroup(entete_eq, equations)

        with self.voiceover(
            text=(
                "Les réactions mises en jeu s'écrivent ainsi. D'abord, le "
                "sulfate de cuivre blanc capte cinq molécules d'eau et "
                "devient du sulfate de cuivre pentahydraté, bleu. Ensuite, "
                "le dioxyde de carbone réagit avec l'hydroxyde de calcium "
                "de l'eau de chaux pour former un précipité de carbonate "
                "de calcium, responsable du trouble, et de l'eau."
            )
        ) as tracker:
            self.play(FadeIn(entete_eq))
            self.play(Write(eq1))
            self.play(Write(eq2))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(groupe_eq))

        # --- À retenir : conclusion + pyrolyse ----------------------------------
        conclusion = example_box(
            Text(
                _wrap(
                    "Si la combustion d'un composé produit de l'eau et du "
                    "dioxyde de carbone, alors ce composé contient les "
                    "éléments hydrogène et carbone. Tout composé organique "
                    "contient l'élément carbone ; on peut aussi le mettre "
                    "en évidence par pyrolyse (chauffage sans air) : il "
                    "apparaît un dépôt noir de carbone.",
                    width=48,
                ),
                font_size=24,
            ),
        )
        conclusion.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Retenons la conclusion : si la combustion d'un composé "
                "produit de l'eau et du dioxyde de carbone, alors ce "
                "composé contient les éléments hydrogène et carbone. Tout "
                "composé organique contient l'élément carbone ; on peut "
                "aussi le mettre en évidence par pyrolyse, c'est-à-dire un "
                "chauffage sans air : il apparaît alors un dépôt noir de "
                "carbone."
            )
        ) as tracker:
            self.play(FadeIn(conclusion))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(conclusion), FadeOut(titre))
