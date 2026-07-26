"""
scenes/Chimie_ComposesOxygenes_04.py — Chapitre 6 « Quelques composés
oxygénés » (1ereC, Chimie), scène 04.

§ Propriétés chimiques des alcools : combustion (équation générale +
exemple éthanol), réaction avec le sodium, obtention de l'éthanol
(fermentation, hydratation de l'éthylène) + les phénols (mention simple).
Source : 1ereC/Chimie.pdf, chapitre 6, pages 58-59.
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
from shapes.boxes import definition_box, property_box, scene_title, warning_box


def _wrap(text: str, width: int = 56) -> str:
    return "\n".join(textwrap.fill(line, width=width) for line in text.split("\n"))


def _fit(mobject, top_y):
    bas_visible = -config.frame_height / 2 + 0.25
    hauteur_dispo = top_y - bas_visible
    if mobject.height > hauteur_dispo:
        mobject.scale(hauteur_dispo / mobject.height, about_point=mobject.get_top())
    return mobject


class ProprietesChimiquesAlcoolsEtPhenols(NotionScene):
    def construct(self):
        titre = scene_title("Propriétés chimiques des alcools — les phénols")
        titre.scale(0.55)
        titre.to_edge(UP)

        # --- Énoncé : la combustion ------------------------------------------------
        entete_comb = Text("La combustion des alcools", font_size=25, color=YELLOW, weight="BOLD")
        entete_comb.next_to(titre, DOWN, buff=0.4)

        eq_gen = MathTex(
            r"C_nH_{2n+2}O + \dfrac{3n}{2}O_2 \rightarrow nCO_2 + (n+1)H_2O",
            font_size=28,
            color=WHITE,
        )
        eq_gen.next_to(entete_comb, DOWN, buff=0.45)

        eq_ethanol = MathTex(
            r"C_2H_6O + 3\,O_2 \rightarrow 2\,CO_2 + 3\,H_2O",
            font_size=28,
            color=WHITE,
        )
        eq_ethanol.next_to(eq_gen, DOWN, buff=0.4)

        groupe_comb = VGroup(entete_comb, eq_gen, eq_ethanol)

        with self.voiceover(
            text=(
                "Comme tout composé organique, un alcool brûle en présence "
                "de dioxygène. La combustion complète d'un alcool C indice "
                "n, H indice deux n plus deux, O suit l'équation générale : "
                "il réagit avec trois n sur deux moles de dioxygène pour "
                "donner n moles de dioxyde de carbone et n plus un moles "
                "d'eau. Pour l'éthanol, C-2 H-6 O, cela donne : l'éthanol "
                "plus trois O-2 donne deux C-O-2 plus trois H-2-O."
            )
        ) as tracker:
            self.play(Write(titre))
            self.play(FadeIn(entete_comb))
            self.play(Write(eq_gen))
            self.play(Write(eq_ethanol))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(groupe_comb))

        # --- Raisonnement : réaction avec le sodium --------------------------------
        entete_na = Text("Réaction avec le sodium", font_size=25, color=YELLOW, weight="BOLD")
        entete_na.next_to(titre, DOWN, buff=0.4)

        eq_na = MathTex(
            r"2\,R\text{-}OH + 2\,Na \rightarrow 2\,R\text{-}O^-Na^+ + H_2",
            font_size=28,
            color=WHITE,
        )
        eq_na.next_to(entete_na, DOWN, buff=0.45)

        commentaire_na = Text(
            _wrap(
                "Le sodium déplace l'hydrogène du groupe -OH : on observe "
                "un dégagement gazeux de dihydrogène (effervescence).",
                width=48,
            ),
            font_size=22,
        )
        commentaire_na.next_to(eq_na, DOWN, buff=0.4)

        groupe_na = VGroup(entete_na, eq_na, commentaire_na)

        with self.voiceover(
            text=(
                "Deuxième propriété : la réaction avec le sodium métallique. "
                "Deux R-O-H plus deux sodium donnent deux R-O moins, "
                "sodium plus, plus H-2. Le sodium déplace l'hydrogène "
                "porté par l'oxygène du groupe hydroxyle : on observe un "
                "dégagement gazeux de dihydrogène, une effervescence, qui "
                "permet de mettre en évidence la présence d'un alcool."
            )
        ) as tracker:
            self.play(FadeIn(entete_na))
            self.play(Write(eq_na))
            self.play(FadeIn(commentaire_na))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(groupe_na))

        # --- Exemple traité : obtention de l'éthanol -------------------------------
        obtention = property_box(
            VGroup(
                Text("Deux voies d'obtention de l'éthanol :", font_size=22, weight="BOLD"),
                Text("• fermentation de jus sucrés (levures) : sources du vin de palme, du koutoukou ;", font_size=20),
                Text("• hydratation catalytique de l'éthylène (voie industrielle) :", font_size=20),
                MathTex(r"CH_2=CH_2 + H_2O \rightarrow CH_3-CH_2-OH", font_size=24, color="#1A1A1A"),
            ).arrange(DOWN, buff=0.28, aligned_edge=LEFT),
            box_width=12.0,
        )
        obtention.next_to(titre, DOWN, buff=0.4)
        _fit(obtention, titre.get_bottom()[1] - 0.4)

        with self.voiceover(
            text=(
                "L'éthanol s'obtient par deux voies principales. La "
                "première, biologique, est la fermentation de jus sucrés "
                "par des levures : c'est à l'origine du vin de palme et du "
                "koutoukou. La seconde, industrielle, est l'hydratation "
                "catalytique de l'éthylène : l'éthylène plus l'eau donnent "
                "l'éthanol."
            )
        ) as tracker:
            self.play(FadeIn(obtention))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(obtention))

        # --- À retenir : les phénols (mention simple) -------------------------------
        def_phenol = definition_box(
            Text(
                _wrap(
                    "Un phénol est un composé dont le groupe -OH est fixé "
                    "directement sur un carbone du noyau benzénique. Ce "
                    "n'est PAS un alcool : ce n'est pas un carbone "
                    "tétragonal. Un phénol possède un caractère acide "
                    "faible.",
                    width=48,
                ),
                font_size=23,
            ),
        )
        def_phenol.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Terminons par une mention simple des phénols. Un phénol "
                "est un composé dont le groupe hydroxyle est fixé "
                "directement sur un carbone du noyau benzénique. Ce n'est "
                "donc pas un alcool, puisque ce carbone n'est pas "
                "tétragonal, mais aromatique. Un phénol possède un "
                "caractère acide faible, plus marqué que celui d'un "
                "alcool."
            )
        ) as tracker:
            self.play(FadeIn(def_phenol))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(def_phenol))

        # --- Piège à éviter : phénol ≠ alcool ---------------------------------------
        piege = warning_box(
            Text(
                _wrap(
                    "Ne classez jamais un phénol parmi les alcools, même si "
                    "les deux portent un groupe -OH : le carbone qui le "
                    "porte n'a pas la même nature (aromatique pour le "
                    "phénol, tétragonal pour l'alcool), et leurs propriétés "
                    "chimiques diffèrent nettement.",
                    width=48,
                ),
                font_size=22,
            ),
        )
        piege.next_to(titre, DOWN, buff=0.4)
        _fit(piege, titre.get_bottom()[1] - 0.4)

        with self.voiceover(
            text=(
                "Attention : ne classez jamais un phénol parmi les alcools, "
                "même si tous deux portent un groupe hydroxyle. Le carbone "
                "qui le porte n'a pas la même nature — aromatique pour le "
                "phénol, tétragonal pour l'alcool — et leurs propriétés "
                "chimiques diffèrent nettement, à commencer par leur "
                "acidité."
            )
        ) as tracker:
            self.play(FadeIn(piege))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(piege), FadeOut(titre))
