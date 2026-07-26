"""
scenes/Chimie_GeneralitesComposesOrganiques_05.py — Chapitre 1 (1ereC, Chimie), scène 05.

§ 3, 3.1, 3.2 Analyse élémentaire quantitative : définition, principe
(combustion complète, piégeage et pesée séparée de H2O et CO2), formules
des pourcentages massiques de C et H, et Exemple résolu 1 (calcul complet).
Source : 1ereC/Chimie.pdf, pages 6-7.
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
from shapes.boxes import definition_box, example_box, property_box, scene_title


def _wrap(text: str, width: int = 56) -> str:
    return "\n".join(textwrap.fill(line, width=width) for line in text.split("\n"))


def _fit(mobject, top_y):
    bas_visible = -config.frame_height / 2 + 0.25
    hauteur_dispo = top_y - bas_visible
    if mobject.height > hauteur_dispo:
        mobject.scale(hauteur_dispo / mobject.height, about_point=mobject.get_top())
    return mobject


class AnalyseQuantitativePourcentages(NotionScene):
    def construct(self):
        titre = scene_title("3. Analyse élémentaire quantitative")
        titre.scale(0.6)
        titre.to_edge(UP)

        # --- Énoncé : définition ------------------------------------------------
        definition = definition_box(
            Text(
                _wrap(
                    "L'analyse élémentaire quantitative a pour but de "
                    "déterminer les proportions (pourcentages massiques) "
                    "des différents éléments présents dans un composé "
                    "organique, afin d'en déduire sa formule brute.",
                    width=48,
                ),
                font_size=25,
            ),
        )
        definition.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "L'analyse élémentaire quantitative a pour but de "
                "déterminer les proportions, c'est-à-dire les pourcentages "
                "massiques, des différents éléments présents dans un "
                "composé organique, afin d'en déduire sa formule brute."
            )
        ) as tracker:
            self.play(Write(titre))
            self.play(FadeIn(definition))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(definition))

        # --- Animation du raisonnement : principe (schéma pesée séparée) -------
        entete = Text("Principe : combustion, piégeage, pesée séparée", font_size=22, color=YELLOW, weight="BOLD")
        entete.next_to(titre, DOWN, buff=0.4)

        four = Rectangle(width=1.6, height=1.1, color=WHITE, stroke_width=3)
        four_texte = Text("masse m\nconnue", font_size=15, color=WHITE)
        four_texte.move_to(four.get_center())
        bloc_four = VGroup(four, four_texte)

        fleche1 = Arrow(LEFT * 0.4, RIGHT * 0.4, color=WHITE, buff=0)

        piege_h2o = Rectangle(width=1.6, height=1.1, color=BLUE, stroke_width=3, fill_color=BLUE, fill_opacity=0.4)
        piege_h2o_texte = Text("desséchant\n(H₂O piégée,\npesée)", font_size=13, color=WHITE)
        piege_h2o_texte.move_to(piege_h2o.get_center())
        bloc_h2o = VGroup(piege_h2o, piege_h2o_texte)

        fleche2 = Arrow(LEFT * 0.4, RIGHT * 0.4, color=WHITE, buff=0)

        piege_co2 = Rectangle(width=1.6, height=1.1, color=GRAY, stroke_width=3, fill_color=GRAY, fill_opacity=0.4)
        piege_co2_texte = Text("potasse KOH\n(CO₂ piégé,\npesé)", font_size=13, color=WHITE)
        piege_co2_texte.move_to(piege_co2.get_center())
        bloc_co2 = VGroup(piege_co2, piege_co2_texte)

        schema = VGroup(bloc_four, fleche1, bloc_h2o, fleche2, bloc_co2).arrange(RIGHT, buff=0.35, aligned_edge=UP)
        schema.next_to(entete, DOWN, buff=0.45)
        _fit(schema, entete.get_bottom()[1] - 0.4)

        groupe_schema = VGroup(entete, schema)

        with self.voiceover(
            text=(
                "Le principe est le suivant. On réalise la combustion "
                "complète d'une masse m connue du composé. Tout le carbone "
                "est transformé en dioxyde de carbone, et tout l'hydrogène "
                "en eau. On piège et on pèse séparément l'eau, absorbée "
                "par un desséchant comme la pierre ponce sulfurique, puis "
                "le dioxyde de carbone, absorbé par la potasse."
            )
        ) as tracker:
            self.play(FadeIn(entete))
            self.play(FadeIn(bloc_four))
            self.play(FadeIn(fleche1), FadeIn(bloc_h2o))
            self.play(FadeIn(fleche2), FadeIn(bloc_co2))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(groupe_schema))

        # --- Exemple traité : formules des pourcentages puis calcul complet ----
        propriete = property_box(
            VGroup(
                MathTex(
                    r"\%C = \dfrac{12 \times m(CO_2)}{44 \times m} \times 100",
                    font_size=30,
                ),
                MathTex(
                    r"\%H = \dfrac{2 \times m(H_2O)}{18 \times m} \times 100",
                    font_size=30,
                ),
            ).arrange(DOWN, buff=0.4),
        )
        propriete.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Une mole de dioxyde de carbone, quarante-quatre grammes, "
                "contient une mole de carbone, douze grammes. Une mole "
                "d'eau, dix-huit grammes, contient deux moles "
                "d'hydrogène, deux grammes : n'oublions surtout pas ce "
                "facteur deux. On en déduit les pourcentages massiques de "
                "carbone et d'hydrogène par ces deux formules."
            )
        ) as tracker:
            self.play(FadeIn(propriete))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(propriete))

        exemple = example_box(
            VGroup(
                Text(
                    _wrap(
                        "La combustion complète de m = 0,24 g d'un composé "
                        "organique A fournit 0,528 g de CO₂ et 0,216 g de "
                        "H₂O.",
                        width=48,
                    ),
                    font_size=22,
                ),
                MathTex(
                    r"m(C) = \dfrac{12}{44} \times 0{,}528 = 0{,}144\,g "
                    r"\Rightarrow \%C = \dfrac{0{,}144}{0{,}24}\times 100 = 60\%",
                    font_size=24,
                ),
                MathTex(
                    r"m(H) = \dfrac{2}{18} \times 0{,}216 = 0{,}024\,g "
                    r"\Rightarrow \%H = \dfrac{0{,}024}{0{,}24}\times 100 = 10\%",
                    font_size=24,
                ),
            ).arrange(DOWN, buff=0.35, aligned_edge=LEFT),
            box_width=12.0,
        )
        exemple.next_to(titre, DOWN, buff=0.4)
        _fit(exemple, titre.get_bottom()[1] - 0.4)

        with self.voiceover(
            text=(
                "Exemple résolu. La combustion complète de zéro virgule "
                "vingt-quatre gramme d'un composé organique A fournit zéro "
                "virgule cinq cent vingt-huit gramme de dioxyde de carbone "
                "et zéro virgule deux cent seize gramme d'eau. La masse de "
                "carbone vaut donc zéro virgule cent quarante-quatre "
                "gramme, soit soixante pour cent de la masse initiale. La "
                "masse d'hydrogène vaut zéro virgule zéro vingt-quatre "
                "gramme, soit dix pour cent. Le composé A contient donc soixante "
                "pour cent de carbone et dix pour cent d'hydrogène en "
                "masse."
            )
        ) as tracker:
            self.play(FadeIn(exemple))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(exemple), FadeOut(titre))
