"""
scenes/Chimie_PetroleGazNaturels_06.py — Chapitre 5 « Pétrole et gaz
naturels » (1ereC, Chimie), scène 06.

§ 6. Le reformage et l'indice d'octane : définition du reformage
(isomérisation / cyclisation / aromatisation sans changer le nombre de
carbones), exemple heptane → 2,2,3-triméthylbutane, définition de
l'indice d'octane (échelle heptane = 0, isooctane = 100), propriété
(plus ramifié / cyclique / aromatique = indice élevé), exemple résolu 2
(super sans plomb 95, phénomène de cliquetis).
Source : 1ereC/Chimie.pdf, chapitre 5, page 49-50.
"""

import textwrap

from manim import (
    DOWN,
    LEFT,
    RIGHT,
    UP,
    WHITE,
    YELLOW,
    GREEN,
    FadeIn,
    FadeOut,
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


class ReformageEtIndiceOctane(NotionScene):
    def construct(self):
        titre = scene_title("6. Le reformage et l'indice d'octane")
        titre.scale(0.58)
        titre.to_edge(UP)

        # --- Énoncé : définition du reformage ------------------------------------
        definition = definition_box(
            Text(
                _wrap(
                    "Le reformage transforme la structure d'un alcane "
                    "(isomérisation, cyclisation, aromatisation) SANS "
                    "changer son nombre d'atomes de carbone, afin "
                    "d'améliorer la qualité de l'essence.",
                    width=48,
                ),
                font_size=23,
            ),
        )
        definition.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Le reformage est une autre transformation chimique du "
                "raffinage. Il modifie la structure d'un alcane, par "
                "isomérisation, cyclisation ou aromatisation, sans "
                "changer son nombre d'atomes de carbone, dans le but "
                "d'améliorer la qualité de l'essence."
            )
        ) as tracker:
            self.play(Write(titre))
            self.play(FadeIn(definition))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(definition))

        # --- Raisonnement : exemple heptane → 2,2,3-triméthylbutane -------------
        entete_reformage = Text("Exemple : isomérisation de l'heptane", font_size=23, color=YELLOW, weight="BOLD")
        entete_reformage.next_to(titre, DOWN, buff=0.4)

        equation_reformage = MathTex(
            r"\text{heptane} \;(n\text{-}C_7H_{16}) \;\xrightarrow{\text{reformage}}\; 2,2,3\text{-triméthylbutane}",
            font_size=26,
            color=WHITE,
        )
        equation_reformage.next_to(entete_reformage, DOWN, buff=0.4)

        note_reformage = Text("même formule brute C₇H₁₆, structure différente", font_size=18, color=GREEN)
        note_reformage.next_to(equation_reformage, DOWN, buff=0.35)

        groupe_reformage = VGroup(entete_reformage, equation_reformage, note_reformage)
        _fit(groupe_reformage, titre.get_bottom()[1] - 0.4)

        with self.voiceover(
            text=(
                "Prenons un exemple : l'heptane linéaire, de formule C "
                "sept H seize, peut être reformé en deux-virgule-deux-"
                "virgule-trois-triméthylbutane. La formule brute reste "
                "identique, C sept H seize, mais la structure de la "
                "molécule change complètement : elle devient bien plus "
                "ramifiée."
            )
        ) as tracker:
            self.play(FadeIn(entete_reformage))
            self.play(Write(equation_reformage))
            self.play(FadeIn(note_reformage))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(groupe_reformage))

        # --- Exemple traité : définition de l'indice d'octane -------------------
        indice_octane = definition_box(
            Text(
                _wrap(
                    "L'indice d'octane mesure la résistance d'une essence "
                    "au cliquetis. Échelle de référence : n-heptane = 0, "
                    "isooctane (2,2,4-triméthylpentane) = 100.",
                    width=48,
                ),
                font_size=23,
            ),
        )
        indice_octane.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "On définit alors l'indice d'octane : il mesure la "
                "résistance d'une essence au cliquetis, ce phénomène "
                "d'auto-inflammation prématurée dans le moteur. L'échelle "
                "de référence prend le n-heptane, très peu résistant, "
                "comme indice zéro, et l'isooctane, très résistant, comme "
                "indice cent."
            )
        ) as tracker:
            self.play(FadeIn(indice_octane))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(indice_octane))

        propriete = property_box(
            Text(
                _wrap(
                    "Plus une molécule est ramifiée, cyclique ou "
                    "aromatique, plus son indice d'octane est élevé : le "
                    "reformage améliore donc l'indice d'octane de "
                    "l'essence.",
                    width=48,
                ),
                font_size=23,
            ),
        )
        propriete.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Retenons la propriété clé : plus une molécule "
                "d'hydrocarbure est ramifiée, cyclique ou aromatique, "
                "plus son indice d'octane est élevé. C'est exactement "
                "pour cela que le reformage, qui rend les molécules plus "
                "ramifiées ou cycliques, améliore l'indice d'octane de "
                "l'essence."
            )
        ) as tracker:
            self.play(FadeIn(propriete))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(propriete))

        # --- À retenir : exemple résolu, le super sans plomb 95 -----------------
        exemple = example_box(
            Text(
                _wrap(
                    "Le « super sans plomb 95 » vendu à la pompe a un "
                    "indice d'octane de 95 : un mélange équivalant, pour "
                    "la résistance au cliquetis, à un carburant contenant "
                    "95% d'isooctane et 5% de n-heptane.",
                    width=48,
                ),
                font_size=22,
            ),
            box_width=11.0,
        )
        exemple.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Un exemple concret : le super sans plomb quatre-vingt-"
                "quinze, vendu à la pompe, porte un indice d'octane de "
                "quatre-vingt-quinze. Cela signifie qu'il se comporte, "
                "vis-à-vis du cliquetis, comme un mélange équivalent à "
                "quatre-vingt-quinze pour cent d'isooctane et cinq pour "
                "cent de n-heptane. Plus l'indice est élevé, mieux le "
                "moteur est protégé du cliquetis."
            )
        ) as tracker:
            self.play(FadeIn(exemple))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(exemple), FadeOut(titre))
