"""
scenes/Chimie_GeneralitesComposesOrganiques_10.py — Chapitre 1 (1ereC, Chimie), scène 10.

§ 6 L'isomérie : définition (C2H6O), isomérie de chaîne, de position, de
fonction, tableau récapitulatif, et Exemple résolu 3 (isomères de C3H6O2).
Source : 1ereC/Chimie.pdf, pages 9-10.
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
from shapes.boxes import definition_box, example_box, scene_title


def _wrap(text: str, width: int = 56) -> str:
    return "\n".join(textwrap.fill(line, width=width) for line in text.split("\n"))


def _fit(mobject, top_y):
    bas_visible = -config.frame_height / 2 + 0.25
    hauteur_dispo = top_y - bas_visible
    if mobject.height > hauteur_dispo:
        mobject.scale(hauteur_dispo / mobject.height, about_point=mobject.get_top())
    return mobject


class Isomerie(NotionScene):
    def construct(self):
        titre = scene_title("6. L'isomérie")
        titre.scale(0.6)
        titre.to_edge(UP)

        # --- Énoncé : le cas C2H6O, deux corps distincts ------------------------
        enonce = Text(
            _wrap(
                "Dès que l'atomicité d'une molécule devient importante, "
                "une même formule brute peut correspondre à plusieurs "
                "formules développées différentes. Ainsi, C₂H₆O "
                "correspond à deux corps bien distincts : l'éthanol "
                "(liquide, bout à 78 °C) et le méthoxyméthane (gaz à "
                "température ordinaire).",
                width=54,
            ),
            font_size=22,
            color=WHITE,
        )
        enonce.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Dès que l'atomicité d'une molécule devient importante, on "
                "peut écrire plusieurs formules développées différentes "
                "pour une même formule brute. Ainsi, la formule brute C "
                "deux H six O correspond à deux corps bien distincts : "
                "l'éthanol, un liquide qui bout à soixante-dix-huit "
                "degrés, et le méthoxyméthane, un gaz à température "
                "ordinaire."
            )
        ) as tracker:
            self.play(Write(titre))
            self.play(FadeIn(enonce))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(enonce))

        # --- Animation du raisonnement : définition + les 3 types --------------
        definition = definition_box(
            Text(
                _wrap(
                    "Des isomères sont des composés qui possèdent la même "
                    "formule brute mais des formules développées "
                    "différentes. Ils ont des propriétés physiques et "
                    "chimiques différentes.",
                    width=48,
                ),
                font_size=24,
            ),
        )
        definition.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Des isomères sont donc des composés qui possèdent la même "
                "formule brute mais des formules développées différentes. "
                "Ils ont des propriétés physiques et chimiques "
                "différentes : l'isomérie est un phénomène quasi général "
                "en chimie organique. En classe de première C, on "
                "distingue trois types d'isomérie."
            )
        ) as tracker:
            self.play(FadeIn(definition))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(definition))

        # --- Exemple traité : chaîne, position, fonction ------------------------
        entete = Text("Isomérie de chaîne, de position, de fonction", font_size=21, color=YELLOW, weight="BOLD")
        entete.next_to(titre, DOWN, buff=0.35)

        chaine = VGroup(
            Text("De chaîne (C₄H₁₀) :", font_size=19, color=YELLOW),
            MathTex(r"\text{butane : } CH_3-CH_2-CH_2-CH_3", font_size=20),
            MathTex(r"\text{2-méthylpropane : } CH_3-CH(CH_3)-CH_3", font_size=20),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.18)

        position = VGroup(
            Text("De position :", font_size=19, color=YELLOW),
            MathTex(r"\text{propan-1-ol : } CH_3-CH_2-CH_2-OH", font_size=20),
            MathTex(r"\text{propan-2-ol : } CH_3-CH(OH)-CH_3", font_size=20),
            MathTex(r"\text{but-1-ène : } CH_2=CH-CH_2-CH_3", font_size=20),
            MathTex(r"\text{but-2-ène : } CH_3-CH=CH-CH_3", font_size=20),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.18)

        fonction = VGroup(
            Text("De fonction :", font_size=19, color=YELLOW),
            MathTex(r"\text{éthanol : } CH_3-CH_2-OH \quad / \quad \text{méthoxyméthane : } CH_3-O-CH_3", font_size=18),
            MathTex(r"\text{propanal : } CH_3-CH_2-CHO \quad / \quad \text{propanone : } CH_3-CO-CH_3", font_size=18),
            MathTex(r"\text{acide éthanoïque : } CH_3-COOH \quad / \quad \text{méthanoate de méthyle : } H-COO-CH_3", font_size=17),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.18)

        bloc = VGroup(chaine, position, fonction).arrange(DOWN, aligned_edge=LEFT, buff=0.32)
        bloc.next_to(entete, DOWN, buff=0.35)
        groupe_types = VGroup(entete, bloc)
        _fit(groupe_types, titre.get_bottom()[1] - 0.4)

        with self.voiceover(
            text=(
                "Les isomères de chaîne ont la même formule brute mais des "
                "chaînes carbonées différentes : le butane a une chaîne "
                "linéaire, le deux-méthylpropane une chaîne ramifiée. Les "
                "isomères de position ont la même chaîne carbonée, mais le "
                "groupe caractéristique, ou la liaison multiple, n'occupe "
                "pas la même place : c'est le cas du propan-1-ol et du "
                "propan-2-ol, ou du but-1-ène et du but-2-ène. Enfin, les "
                "isomères de fonction ont des fonctions organiques "
                "différentes : l'éthanol, un alcool, et le "
                "méthoxyméthane, un éther-oxyde ; le propanal, un "
                "aldéhyde, et la propanone, une cétone ; l'acide "
                "éthanoïque, un acide carboxylique, et le méthanoate de "
                "méthyle, un ester."
            )
        ) as tracker:
            self.play(FadeIn(entete))
            self.play(FadeIn(chaine))
            self.play(FadeIn(position))
            self.play(FadeIn(fonction))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(groupe_types))

        # --- Exemple résolu 3 : isomères de C3H6O2 ------------------------------
        exemple = example_box(
            VGroup(
                Text(
                    _wrap(
                        "Isomères de formule brute C₃H₆O₂ (acides "
                        "carboxyliques et esters) :",
                        width=48,
                    ),
                    font_size=21,
                ),
                MathTex(r"\text{acide propanoïque : } CH_3-CH_2-COOH", font_size=22),
                MathTex(r"\text{méthanoate d'éthyle : } H-COO-CH_2-CH_3", font_size=22),
                MathTex(r"\text{éthanoate de méthyle : } CH_3-COO-CH_3", font_size=22),
            ).arrange(DOWN, buff=0.28, aligned_edge=LEFT),
            box_width=11.5,
        )
        exemple.next_to(titre, DOWN, buff=0.4)
        _fit(exemple, titre.get_bottom()[1] - 0.4)

        with self.voiceover(
            text=(
                "Exemple résolu : écrivons les formules semi-développées "
                "des isomères de formule brute C trois H six O deux, en "
                "nous limitant aux acides carboxyliques et aux esters. On "
                "trouve l'acide propanoïque, un acide carboxylique, puis "
                "deux esters : le méthanoate d'éthyle et l'éthanoate de "
                "méthyle. Ces trois composés sont des isomères de "
                "fonction."
            )
        ) as tracker:
            self.play(FadeIn(exemple))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(exemple), FadeOut(titre))
