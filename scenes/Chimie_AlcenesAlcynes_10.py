"""
scenes/Chimie_AlcenesAlcynes_10.py — Chapitre 3 (1ereC, Chimie), scène 10.

La règle de Markovnikov et l'hydratation des alcènes : théorème de
Markovnikov (le H se fixe sur le carbone le plus hydrogéné), exemple résolu
de l'addition de HCl sur le propène (2-chloropropane majoritaire),
hydratation catalysée par H2SO4 (propan-2-ol majoritaire), application
industrielle à la fabrication de l'éthanol. Source : 1ereC/Chimie.pdf,
chapitre 3, page 32.
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
    RED,
    FadeIn,
    FadeOut,
    MathTex,
    Text,
    VGroup,
    Write,
    config,
)

from shapes.base_scene import NotionScene
from shapes.boxes import example_box, scene_title, theorem_box


def _wrap(text: str, width: int = 56) -> str:
    return "\n".join(textwrap.fill(line, width=width) for line in text.split("\n"))


def _fit(mobject, top_y):
    bas_visible = -config.frame_height / 2 + 0.25
    hauteur_dispo = top_y - bas_visible
    if mobject.height > hauteur_dispo:
        mobject.scale(hauteur_dispo / mobject.height, about_point=mobject.get_top())
    return mobject


class MarkovnikovHydratation(NotionScene):
    def construct(self):
        titre = scene_title("10. La règle de Markovnikov et l'hydratation")
        titre.scale(0.5)
        titre.to_edge(UP)

        # --- Énoncé : un alcène dissymétrique pose une question -------------------
        intro = Text(
            _wrap(
                "Lorsqu'on additionne HCl ou H2O sur un alcène "
                "dissymétrique, comme le propène, les deux carbones de "
                "la double liaison ne portent pas le même nombre "
                "d'hydrogènes : où se fixe alors l'hydrogène ?",
                width=54,
            ),
            font_size=23,
            color=WHITE,
        )
        intro.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Lorsqu'on additionne une molécule dissymétrique comme "
                "H C l ou l'eau sur un alcène lui-même dissymétrique, "
                "comme le propène, les deux atomes de carbone de la "
                "double liaison ne portent pas le même nombre "
                "d'hydrogènes. Une question se pose alors : où l'hydrogène "
                "vient-il se fixer ?"
            )
        ) as tracker:
            self.play(Write(titre))
            self.play(FadeIn(intro))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(intro))

        # --- Animation du raisonnement : théorème de Markovnikov -----------------
        theoreme = theorem_box(
            Text(
                _wrap(
                    "Règle de Markovnikov : lors de l'addition d'une "
                    "molécule HX (ou H2O) sur un alcène dissymétrique, "
                    "l'atome d'hydrogène H se fixe préférentiellement sur "
                    "le carbone de la double liaison qui porte déjà le "
                    "plus grand nombre d'atomes d'hydrogène.",
                    width=48,
                ),
                font_size=24,
            ),
        )
        theoreme.next_to(titre, DOWN, buff=0.4)
        _fit(theoreme, titre.get_bottom()[1] - 0.4)

        with self.voiceover(
            text=(
                "La règle de Markovnikov répond à cette question : lors "
                "de l'addition d'une molécule H X, ou d'eau, sur un "
                "alcène dissymétrique, l'atome d'hydrogène se fixe "
                "préférentiellement sur le carbone de la double liaison "
                "qui porte déjà le plus grand nombre d'atomes "
                "d'hydrogène. On résume parfois cela par la formule : "
                "les riches s'enrichissent."
            )
        ) as tracker:
            self.play(FadeIn(theoreme))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(theoreme))

        # --- Exemple traité : HCl sur le propène -----------------------------------
        entete = Text("Exemple résolu : HCl sur le propène", font_size=23, color=YELLOW, weight="BOLD")
        entete.next_to(titre, DOWN, buff=0.35)

        propene = MathTex(r"CH_2=CH-CH_3 + HCl \longrightarrow \; ?", font_size=28)
        propene.next_to(entete, DOWN, buff=0.4)

        produits = VGroup(
            VGroup(
                MathTex(r"CH_3-CHCl-CH_3", font_size=28, color=GREEN),
                Text("2-chloropropane — MAJORITAIRE", font_size=18, color=GREEN),
            ).arrange(DOWN, buff=0.15),
            VGroup(
                MathTex(r"CH_2Cl-CH_2-CH_3", font_size=28, color=RED),
                Text("1-chloropropane — minoritaire", font_size=18, color=RED),
            ).arrange(DOWN, buff=0.15),
        ).arrange(RIGHT, buff=1.0)
        produits.next_to(propene, DOWN, buff=0.5)

        groupe = VGroup(entete, propene, produits)
        _fit(groupe, titre.get_bottom()[1] - 0.35)

        with self.voiceover(
            text=(
                "Appliquons la règle au propène : C H deux, double "
                "liaison C H, C H trois, additionné à H C l. Le carbone "
                "un porte deux hydrogènes, le carbone deux n'en porte "
                "qu'un seul. D'après Markovnikov, l'hydrogène de H C l se "
                "fixe sur le carbone un, le plus riche en hydrogènes, et "
                "le chlore se fixe donc sur le carbone deux. Le produit "
                "majoritaire est le deux-chloropropane ; le "
                "un-chloropropane reste minoritaire."
            )
        ) as tracker:
            self.play(FadeIn(entete))
            self.play(FadeIn(propene))
            self.play(FadeIn(produits))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(groupe))

        # --- À retenir : hydratation et application industrielle ------------------
        exemple = example_box(
            VGroup(
                Text("Hydratation du propène (catalyseur H₂SO₄) :", font_size=21, weight="BOLD"),
                MathTex(
                    r"CH_2=CH-CH_3 + H_2O \xrightarrow{H_2SO_4} CH_3-CH(OH)-CH_3",
                    font_size=25,
                ),
                Text("propan-2-ol, majoritaire (Markovnikov)", font_size=19, color=YELLOW),
                Text("Application industrielle : hydratation de l'éthylène → éthanol.", font_size=19),
            ).arrange(DOWN, buff=0.3),
            box_width=11.5,
        )
        exemple.next_to(titre, DOWN, buff=0.35)
        _fit(exemple, titre.get_bottom()[1] - 0.35)

        with self.voiceover(
            text=(
                "La règle de Markovnikov s'applique de la même façon à "
                "l'hydratation. En présence d'acide sulfurique comme "
                "catalyseur, le propène additionne de l'eau pour donner "
                "majoritairement le propan-deux-ol, l'hydrogène de l'eau "
                "se fixant sur le carbone le plus hydrogéné. Cette "
                "réaction est utilisée industriellement : l'hydratation "
                "de l'éthylène permet ainsi de fabriquer de l'éthanol à "
                "grande échelle."
            )
        ) as tracker:
            self.play(FadeIn(exemple))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(exemple))

        # --- Pièges à éviter -------------------------------------------------------
        piege = Text(
            _wrap(
                "Piège fréquent : inverser la règle et fixer le H sur le "
                "carbone le MOINS hydrogéné. Retenez l'image « les "
                "riches s'enrichissent » : H va toujours vers le carbone "
                "qui a déjà le plus d'hydrogènes.",
                width=52,
            ),
            font_size=22,
            color=WHITE,
        )
        piege.next_to(titre, DOWN, buff=0.4)
        _fit(piege, titre.get_bottom()[1] - 0.4)

        with self.voiceover(
            text=(
                "Attention à un piège très fréquent : inverser la règle "
                "et fixer l'hydrogène sur le carbone le moins hydrogéné. "
                "Retenez l'image mnémotechnique : les riches "
                "s'enrichissent. L'hydrogène va toujours vers le carbone "
                "qui possède déjà le plus grand nombre d'hydrogènes."
            )
        ) as tracker:
            self.play(FadeIn(piege))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(piege), FadeOut(titre))
