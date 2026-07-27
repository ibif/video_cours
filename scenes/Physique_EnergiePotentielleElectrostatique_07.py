"""
scenes/Physique_EnergiePotentielleElectrostatique_07.py — Chapitre « Énergie
potentielle électrostatique » (1ereC, Physique), scène 07.

L'électronvolt : définition (énergie acquise par une charge élémentaire e
accélérée sous 1 V), 1 eV=1,6×10⁻¹⁹ J, multiples (keV, MeV, GeV), conversion
J↔eV, utilité pour les énergies de particules.
Source : 1ereC/Physique.pdf, pages 66-75.
"""

import textwrap

from manim import DOWN, LEFT, RIGHT, UP, YELLOW, FadeIn, FadeOut, MathTex, Text, VGroup, Write

from shapes.base_scene import NotionScene
from shapes.boxes import definition_box, essentiel_box, example_box, property_box, scene_title


def _wrap(text: str, width: int = 56) -> str:
    return "\n".join(textwrap.fill(line, width=width) for line in text.split("\n"))


class Electronvolt(NotionScene):
    def construct(self):
        titre = scene_title("Une unité d'énergie adaptée : l'électronvolt")
        titre.scale(0.48)
        titre.to_edge(UP)

        # --- Énoncé : le joule est trop grand pour les particules ---------------------
        constat = Text(
            _wrap(
                "Les énergies mises en jeu à l'échelle d'une particule "
                "chargée (électron, ion, proton) sont extrêmement petites "
                "en joules. Il existe une unité mieux adaptée : "
                "l'électronvolt.",
                width=54,
            ),
            font_size=23,
        )
        constat.next_to(titre, DOWN, buff=0.7)

        with self.voiceover(
            text=(
                "À l'échelle d'une particule chargée — un électron, un "
                "ion, un proton — les énergies mises en jeu, exprimées en "
                "joules, sont extrêmement petites, avec des puissances de "
                "10 très négatives peu commodes à manier. Il existe une "
                "unité d'énergie bien mieux adaptée à cette échelle : "
                "l'électronvolt."
            )
        ) as tracker:
            self.play(Write(constat))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(constat))

        # --- Définition -------------------------------------------------------------------
        definition = definition_box(
            VGroup(
                Text(
                    "L'électronvolt (eV) est l'énergie acquise par une",
                    font_size=22,
                ),
                Text(
                    "charge élémentaire e accélérée sous une tension de 1 V :",
                    font_size=22,
                ),
                MathTex(r"1\ \text{eV} = e \times 1\ \text{V} = 1{,}6\times10^{-19}\ \text{J}", font_size=28),
            ).arrange(DOWN, buff=0.25),
            box_width=10.8,
        )
        definition.next_to(titre, DOWN, buff=0.6)

        with self.voiceover(
            text=(
                "Par définition, l'électronvolt, noté e V, est l'énergie "
                "acquise par une charge élémentaire e, accélérée sous une "
                "tension de 1 volt. Numériquement, 1 électronvolt vaut e "
                "fois 1 volt, soit 1 virgule 6 fois 10 puissance moins 19 "
                "joule — c'est-à-dire exactement la valeur, en coulombs, de "
                "la charge élémentaire."
            )
        ) as tracker:
            self.play(FadeIn(definition))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(definition))

        # --- Raisonnement : multiples ---------------------------------------------------
        multiples = property_box(
            VGroup(
                MathTex(r"1\ \text{keV} = 10^{3}\ \text{eV}", font_size=27),
                MathTex(r"1\ \text{MeV} = 10^{6}\ \text{eV}", font_size=27),
                MathTex(r"1\ \text{GeV} = 10^{9}\ \text{eV}", font_size=27),
            ).arrange(DOWN, buff=0.3),
            box_width=7.4,
        )
        multiples.next_to(titre, DOWN, buff=0.6)

        with self.voiceover(
            text=(
                "Comme pour toute unité, on utilise des multiples : le "
                "kiloélectronvolt, keV, vaut mille électronvolts ; le "
                "mégaélectronvolt, MeV, vaut un million d'électronvolts ; "
                "et le gigaélectronvolt, GeV, vaut un milliard "
                "d'électronvolts. Ces multiples sont très utilisés en "
                "physique des particules."
            )
        ) as tracker:
            self.play(FadeIn(multiples))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(multiples))

        # --- Exemple traité : conversions --------------------------------------------------
        enonce = Text(
            _wrap(
                "Convertir 3,2×10⁻¹⁷ J en électronvolts, puis 2 MeV en "
                "joules.",
                width=52,
            ),
            font_size=23,
        )
        enonce.next_to(titre, DOWN, buff=0.7)

        with self.voiceover(
            text=(
                "Entraînons-nous à convertir. Convertissons d'abord 3 "
                "virgule 2 fois 10 puissance moins 17 joule en "
                "électronvolts, puis 2 mégaélectronvolts en joules."
            )
        ) as tracker:
            self.play(Write(enonce))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(enonce))

        calcul = example_box(
            VGroup(
                MathTex(
                    r"\dfrac{3{,}2\times10^{-17}}{1{,}6\times10^{-19}} = 200\ \text{eV}",
                    font_size=26,
                ),
                MathTex(
                    r"2\ \text{MeV} = 2\times10^{6} \times 1{,}6\times10^{-19} = 3{,}2\times10^{-13}\ \text{J}",
                    font_size=24,
                ),
            ).arrange(DOWN, buff=0.35),
            box_width=10.6,
        )
        calcul.next_to(titre, DOWN, buff=0.6)

        with self.voiceover(
            text=(
                "Pour convertir des joules en électronvolts, on divise par "
                "1 virgule 6 fois 10 puissance moins 19 : ici, on obtient "
                "200 électronvolts. Inversement, pour convertir des "
                "électronvolts en joules, on multiplie par cette même "
                "valeur : 2 mégaélectronvolts, soit 2 fois 10 puissance 6 "
                "électronvolts, valent 3 virgule 2 fois 10 puissance moins "
                "13 joule."
            )
        ) as tracker:
            self.play(FadeIn(calcul))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(calcul))

        # --- À retenir --------------------------------------------------------------------
        retenir = essentiel_box(
            Text(
                _wrap(
                    "1 eV=1,6×10⁻¹⁹ J (énergie d'une charge élémentaire "
                    "accélérée sous 1 V). Multiples : keV, MeV, GeV. "
                    "Conversion : diviser par 1,6×10⁻¹⁹ pour passer de J à "
                    "eV, multiplier pour l'inverse.",
                    width=56,
                ),
                font_size=21,
            )
        )
        retenir.next_to(titre, DOWN, buff=0.6)

        with self.voiceover(
            text=(
                "À retenir : 1 électronvolt vaut 1 virgule 6 fois 10 "
                "puissance moins 19 joule — c'est l'énergie d'une charge "
                "élémentaire accélérée sous 1 volt. On utilise couramment "
                "ses multiples, keV, MeV, GeV. Pour convertir des joules en "
                "électronvolts, on divise par 1 virgule 6 fois 10 "
                "puissance moins 19 ; pour l'inverse, on multiplie."
            )
        ) as tracker:
            self.play(FadeIn(retenir))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(titre), FadeOut(retenir))
