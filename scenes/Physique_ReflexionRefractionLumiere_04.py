"""
scenes/Physique_ReflexionRefractionLumiere_04.py — Chapitre « Réflexion et
réfraction de la lumière blanche » (1ereC, Physique), scène 04.

§ Réfraction : dispositif (demi-cylindre eau/verre), observations (rayon
brisé, se rapproche de la normale en entrant dans un milieu plus
réfringent), définition de la réfraction et du dioptre, vocabulaire (rayon
incident/réfracté, i1/i2), définition de l'indice de réfraction absolu
n = c/v (sans unité, ≥1), tableau des indices usuels.
Source : 1ereC/Physique.pdf, pages 117-129.
"""

import textwrap

import numpy as np

from manim import (
    DOWN,
    LEFT,
    ORIGIN,
    RIGHT,
    UP,
    WHITE,
    YELLOW,
    BLUE,
    GREY,
    Create,
    DashedLine,
    Dot,
    FadeIn,
    FadeOut,
    Line,
    MathTex,
    Rectangle,
    Text,
    VGroup,
    Write,
)

from shapes.base_scene import NotionScene
from shapes.boxes import definition_box, essentiel_box, property_box, scene_title, warning_box


def _wrap(text: str, width: int = 56) -> str:
    return "\n".join(textwrap.fill(line, width=width) for line in text.split("\n"))


def _refraction_schema(i1_deg: float, i2_deg: float, center: np.ndarray = ORIGIN, t: float = 2.0, surf_half: float = 2.6):
    """
    Schéma de réfraction : dioptre horizontal (milieu 1 au-dessus, milieu 2
    en dessous, plus réfringent), rayon incident SI et rayon réfracté IT
    (se rapprochant de la normale si le milieu 2 est plus réfringent).
    """
    i1 = np.radians(i1_deg)
    i2 = np.radians(i2_deg)
    I = center

    milieu1 = Rectangle(width=2 * surf_half, height=1.8, fill_color=BLUE, fill_opacity=0.06, stroke_width=0)
    milieu1.move_to(I + UP * 0.9)
    milieu2 = Rectangle(width=2 * surf_half, height=1.8, fill_color=BLUE, fill_opacity=0.18, stroke_width=0)
    milieu2.move_to(I + DOWN * 0.9)

    dioptre = Line(I + LEFT * surf_half, I + RIGHT * surf_half, color=GREY, stroke_width=4)
    normale = DashedLine(I + DOWN * 1.6, I + UP * 1.9, color=WHITE, stroke_width=2)

    S = I + t * np.array([-np.sin(i1), np.cos(i1), 0])
    T = I + t * np.array([np.sin(i2), -np.cos(i2), 0])

    rayon_incident = Line(S, I, color=YELLOW, stroke_width=4)
    rayon_refracte = Line(I, T, color=YELLOW, stroke_width=4)
    point_I = Dot(I, color=WHITE, radius=0.06)

    groupe = VGroup(milieu1, milieu2, dioptre, normale, rayon_incident, rayon_refracte, point_I)
    return groupe, S, I, T


class RefractionExperienceDioptreIndice(NotionScene):
    def construct(self):
        titre = scene_title("Réfraction : expérience, dioptre, indice de réfraction")
        titre.scale(0.4)
        titre.to_edge(UP)

        # --- Énoncé : dispositif expérimental ----------------------------------
        mise_en_situation = Text(
            _wrap(
                "Sur un banc d'optique, un demi-cylindre d'eau (ou de "
                "verre) repose sur un disque gradué. On envoie un rayon "
                "laser depuis l'air vers ce milieu transparent. Que "
                "devient le rayon en traversant la surface de séparation ?",
                width=50,
            ),
            font_size=20,
        )
        mise_en_situation.next_to(titre, DOWN, buff=0.35)

        schema0, S0, I0, T0 = _refraction_schema(45, 32, center=DOWN * 0.7)
        schema0.next_to(mise_en_situation, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Sur un banc d'optique, un demi-cylindre d'eau, ou de "
                "verre, repose sur un disque gradué. On envoie un rayon "
                "laser depuis l'air vers ce milieu transparent. Que "
                "devient le rayon en traversant la surface de séparation "
                "entre les deux milieux ?"
            )
        ) as tracker:
            self.play(Write(titre))
            self.play(FadeIn(mise_en_situation))
            self.play(Create(schema0))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(mise_en_situation), FadeOut(schema0))

        # --- Raisonnement : observations et vocabulaire --------------------------
        schema, S, I, T = _refraction_schema(45, 32, center=LEFT * 2.8 + DOWN * 0.2)
        label_S = Text("S", font_size=20).next_to(S, UP, buff=0.1)
        label_I = Text("I", font_size=20).next_to(I, LEFT, buff=0.15)
        label_T = Text("T", font_size=20).next_to(T, DOWN, buff=0.1)
        label_i1 = MathTex("i_1", font_size=22, color=BLUE).move_to(I + UP * 0.7 + LEFT * 0.5)
        label_i2 = MathTex("i_2", font_size=22, color=BLUE).move_to(I + DOWN * 0.6 + RIGHT * 0.35)
        label_milieu1 = Text("milieu 1 (air)", font_size=16).move_to(I + UP * 1.55 + RIGHT * 1.1)
        label_milieu2 = Text("milieu 2 (eau, plus réfringent)", font_size=15).move_to(I + DOWN * 1.55 + RIGHT * 0.0)
        schema_legende = VGroup(schema, label_S, label_I, label_T, label_i1, label_i2, label_milieu1, label_milieu2)
        schema_legende.move_to(LEFT * 3.0 + DOWN * 0.1)

        vocabulaire = VGroup(
            Text("SI : rayon incident", font_size=19),
            Text("IT : rayon réfracté", font_size=19),
            Text("i1 : angle d'incidence", font_size=19),
            Text("i2 : angle de réfraction", font_size=19),
            Text("Dioptre : surface séparant deux milieux", font_size=19),
            Text("transparents différents.", font_size=19),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.2)
        vocabulaire.next_to(schema_legende, RIGHT, buff=0.7)

        with self.voiceover(
            text=(
                "On observe que le rayon lumineux est brisé exactement au "
                "point d'incidence : sa direction change brusquement en "
                "passant d'un milieu à l'autre. Plus précisément, en "
                "entrant dans un milieu plus réfringent, c'est-à-dire un "
                "milieu où la lumière se propage moins vite, comme l'eau "
                "par rapport à l'air, le rayon se rapproche de la "
                "normale. Ce phénomène s'appelle la réfraction. La surface "
                "de séparation entre les deux milieux transparents "
                "s'appelle un dioptre. Le rayon incident SI arrive avec un "
                "angle i1, le rayon réfracté IT repart avec un angle i2, "
                "plus petit, tous deux mesurés depuis la normale."
            )
        ) as tracker:
            self.play(Create(schema_legende))
            self.play(Write(vocabulaire))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(schema_legende), FadeOut(vocabulaire))

        # --- Définition : réfraction, dioptre ----------------------------------------
        definition1 = definition_box(
            VGroup(
                Text("Réfraction et dioptre", font_size=22, weight="BOLD"),
                Text("La réfraction est le changement de direction d'un rayon", font_size=20),
                Text("lumineux en traversant la surface de séparation (dioptre)", font_size=20),
                Text("entre deux milieux transparents différents.", font_size=20),
            ).arrange(DOWN, buff=0.2),
            box_width=11.8,
        )
        definition1.next_to(titre, DOWN, buff=0.35)

        with self.voiceover(
            text=(
                "Retenons la définition : la réfraction est le changement "
                "de direction d'un rayon lumineux en traversant la "
                "surface de séparation entre deux milieux transparents "
                "différents. Cette surface de séparation s'appelle un "
                "dioptre."
            )
        ) as tracker:
            self.play(FadeIn(definition1))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(definition1))

        # --- Définition : indice de réfraction absolu --------------------------------
        definition2 = definition_box(
            VGroup(
                Text("Indice de réfraction absolu", font_size=22, weight="BOLD"),
                MathTex(r"n = \dfrac{c}{v}", font_size=30, color=YELLOW),
                Text("c : célérité de la lumière dans le vide (3×10⁸ m/s)", font_size=19),
                Text("v : célérité de la lumière dans le milieu considéré", font_size=19),
                Text("n est sans unité, et toujours n ≥ 1.", font_size=19),
            ).arrange(DOWN, buff=0.2),
            box_width=11.6,
        )
        definition2.next_to(titre, DOWN, buff=0.35)

        with self.voiceover(
            text=(
                "Pour quantifier à quel point un milieu est réfringent, on "
                "définit son indice de réfraction absolu n, égal au "
                "rapport c sur v : c, la célérité de la lumière dans le "
                "vide, environ trois cent mille kilomètres par seconde, "
                "divisée par v, la célérité de la lumière dans ce milieu, "
                "toujours plus lente. L'indice n est un nombre sans unité, "
                "et il vaut toujours au moins un, puisque rien ne va plus "
                "vite que la lumière dans le vide."
            )
        ) as tracker:
            self.play(FadeIn(definition2))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(definition2))

        # --- Tableau des indices usuels ------------------------------------------------
        indices = VGroup(
            MathTex(r"\text{vide : } n = 1", font_size=24),
            MathTex(r"\text{air : } n \approx 1", font_size=24),
            MathTex(r"\text{glace : } n = 1{,}31", font_size=24),
            MathTex(r"\text{eau : } n = 1{,}33", font_size=24),
            MathTex(r"\text{verre : } n = 1{,}50 \ \text{à} \ 1{,}52", font_size=24),
            MathTex(r"\text{diamant : } n = 2{,}42", font_size=24),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.22)
        table_box = property_box(indices, box_width=8.0)
        table_box.next_to(titre, DOWN, buff=0.35)

        with self.voiceover(
            text=(
                "Voici les indices de quelques milieux usuels. Le vide a "
                "un indice exactement égal à un, l'air un indice très "
                "proche de un. La glace a un indice de un virgule "
                "trente-et-un, l'eau un virgule trente-trois. Le verre est "
                "plus réfringent, entre un virgule cinquante et un virgule "
                "cinquante-deux selon sa composition. Et le diamant "
                "possède un indice remarquablement élevé, deux virgule "
                "quarante-deux, ce qui explique en partie son éclat "
                "particulier, comme on le verra plus loin dans ce "
                "chapitre."
            )
        ) as tracker:
            self.play(FadeIn(table_box))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(table_box))

        # --- À retenir --------------------------------------------------------------
        retenir = essentiel_box(
            VGroup(
                Text("À retenir", font_size=24, weight="BOLD"),
                Text("Réfraction : déviation du rayon au passage d'un dioptre.", font_size=20),
                MathTex(r"n = \dfrac{c}{v} \ , \quad n \geq 1, \ \text{sans unité}", font_size=26),
                Text("Milieu plus réfringent = indice plus grand = lumière", font_size=20),
                Text("plus lente ; le rayon s'en rapproche de la normale.", font_size=20),
            ).arrange(DOWN, buff=0.2),
            box_width=12.0,
        )
        retenir.next_to(titre, DOWN, buff=0.35)

        with self.voiceover(
            text=(
                "Retenons l'essentiel : la réfraction est la déviation "
                "d'un rayon lumineux au passage d'un dioptre. L'indice de "
                "réfraction n vaut c sur v, il est sans unité et toujours "
                "supérieur ou égal à un. Plus un milieu est réfringent, "
                "plus son indice est grand, plus la lumière y est lente, "
                "et plus le rayon s'en rapproche de la normale en y "
                "entrant."
            )
        ) as tracker:
            self.play(FadeIn(retenir))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(retenir))

        # --- Piège à éviter ------------------------------------------------------------
        piege = warning_box(
            VGroup(
                Text("• Ne pas confondre \"plus réfringent\" et \"plus dense\" :", font_size=20),
                Text("   le lien existe souvent mais l'indice se définit par la", font_size=20),
                Text("   vitesse de la lumière (n=c/v), pas par la densité.", font_size=20),
                Text("• Un rayon en incidence normale (i1=0) n'est jamais", font_size=20),
                Text("   dévié, même en changeant de milieu (i2 = 0 aussi).", font_size=20),
            ).arrange(DOWN, aligned_edge=LEFT, buff=0.16),
            box_width=12.2,
        )
        piege.next_to(titre, DOWN, buff=0.35)

        with self.voiceover(
            text=(
                "Piège à éviter : ne confondez pas «plus réfringent» et "
                "«plus dense». Le lien existe souvent, mais l'indice de "
                "réfraction se définit rigoureusement par la vitesse de la "
                "lumière dans le milieu, pas par sa densité. Autre point "
                "important : un rayon en incidence normale, avec i1 égal "
                "zéro, n'est jamais dévié, même en changeant de milieu, "
                "car i2 vaut alors zéro aussi."
            )
        ) as tracker:
            self.play(FadeIn(piege))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(piege), FadeOut(titre))
