"""
scenes/Physique_AmplificateurOperationnel_05.py — Chapitre « L'amplificateur
opérationnel » (1ereC, Physique), scène 05.

§ 5. Le montage suiveur : sortie reliée directement à E- (réaction
négative totale), entrée Ue sur E+. Démonstration : ε = 0 → V+ = V-,
V+ = Ue, V- = Us → Us = Ue. Gain Av = 1. Intérêt : adaptation
d'impédance (i+ = 0, ne prélève aucun courant à la source), application
voltmètre électronique.
Source : 1ereC/Physique.pdf, pages 99-107 (§ 5).
"""

import textwrap

from manim import (
    DOWN,
    LEFT,
    ORANGE,
    RIGHT,
    UP,
    WHITE,
    YELLOW,
    FadeIn,
    FadeOut,
    Line,
    MathTex,
    Polygon,
    Text,
    VGroup,
    Write,
)

from shapes.base_scene import NotionScene
from shapes.boxes import essentiel_box, example_box, property_box, scene_title, theorem_box, warning_box


def _wrap(text: str, width: int = 56) -> str:
    return "\n".join(textwrap.fill(line, width=width) for line in text.split("\n"))


def _ao_symbole(width=2.4, height=1.6):
    haut = UP * height / 2 + LEFT * width / 2
    bas = DOWN * height / 2 + LEFT * width / 2
    pointe = RIGHT * width / 2
    triangle = Polygon(haut, bas, pointe, color=WHITE, stroke_width=3)
    plus = Text("+", font_size=22, color=WHITE).move_to(haut + RIGHT * 0.35 + DOWN * 0.05)
    moins = Text("−", font_size=22, color=WHITE).move_to(bas + RIGHT * 0.35 + UP * 0.05)
    return VGroup(triangle, plus, moins), haut, bas, pointe


def _schema_suiveur():
    """Montage suiveur : Ue directement sur E+, sortie S reliée par un
    fil de réaction directement à E− (rebouclage total, gain 1)."""
    symbole, haut, bas, pointe = _ao_symbole()

    fil_e_plus = Line(haut + LEFT * 0.9, haut, stroke_width=3, color=WHITE)
    fil_s = Line(pointe, pointe + RIGHT * 0.9, stroke_width=3, color=WHITE)
    label_ue = Text("Ue", font_size=20, color=YELLOW).next_to(fil_e_plus, LEFT, buff=0.1)
    label_us = Text("Us", font_size=20, color=ORANGE).next_to(fil_s, RIGHT, buff=0.1)

    # Fil de réaction : de la sortie, redescend, revient vers E- (bas)
    coin_haut = pointe + RIGHT * 0.9 + DOWN * 0.0
    reaction_bas = bas + LEFT * 1.6
    reaction = VGroup(
        Line(coin_haut, coin_haut + DOWN * 1.5, stroke_width=2.5, color=YELLOW),
        Line(coin_haut + DOWN * 1.5, reaction_bas + DOWN * 1.5, stroke_width=2.5, color=YELLOW),
        Line(reaction_bas + DOWN * 1.5, bas, stroke_width=2.5, color=YELLOW),
    )

    return VGroup(symbole, fil_e_plus, fil_s, label_ue, label_us, reaction)


class MontageSuiveur(NotionScene):
    def construct(self):
        titre = scene_title("Le montage suiveur")
        titre.scale(0.45)
        titre.to_edge(UP)

        # --- Énoncé -------------------------------------------------------
        mise_en_situation = Text(
            _wrap(
                "Un montage à AO qui ne modifie pas la tension mais qui "
                "protège la source qui la fournit : à quoi cela peut-il "
                "bien servir ?",
                width=58,
            ),
            font_size=22,
        )
        mise_en_situation.next_to(titre, DOWN, buff=0.35)

        with self.voiceover(
            text=(
                "Un montage à AO qui ne modifie pas la valeur de la "
                "tension mais qui protège la source qui la fournit : à "
                "quoi cela peut-il bien servir ? C'est le montage suiveur."
            )
        ) as tracker:
            self.play(Write(titre))
            self.play(FadeIn(mise_en_situation))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(mise_en_situation))

        # --- Raisonnement : schéma + démonstration ---------------------------
        schema = _schema_suiveur()
        schema.scale(1.0)
        schema.next_to(titre, DOWN, buff=0.6).shift(LEFT * 2.7)

        demonstration = theorem_box(
            VGroup(
                Text("Sortie reliée à E− → réaction négative totale.", font_size=19),
                MathTex(r"\varepsilon = 0 \Rightarrow V_+ = V_-", font_size=25),
                MathTex(r"V_+ = U_e \quad ; \quad V_- = U_s", font_size=25),
                MathTex(r"\Rightarrow \ U_s = U_e", font_size=28, color=YELLOW),
            ).arrange(DOWN, buff=0.18),
            box_width=8.6,
        )
        demonstration.next_to(schema, RIGHT, buff=0.4)

        with self.voiceover(
            text=(
                "La sortie est reliée directement à l'entrée E moins : il "
                "y a donc une réaction négative totale, et l'AO "
                "fonctionne en régime linéaire, avec epsilon égal à zéro, "
                "donc V plus égale V moins. Or V plus vaut Ue, puisque Ue "
                "est appliquée sur E plus, et V moins vaut Us, puisque la "
                "sortie est reliée directement à E moins. On en déduit "
                "immédiatement que Us égale Ue."
            )
        ) as tracker:
            self.play(FadeIn(schema))
            self.play(FadeIn(demonstration))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(schema), FadeOut(demonstration))

        # --- Exemple : intérêt / application ----------------------------------
        exemple = example_box(
            VGroup(
                Text("Gain Av = Us / Ue = 1 (tension recopiée à l'identique).", font_size=19),
                Text("Intérêt : i+ = 0, le suiveur ne prélève AUCUN courant", font_size=19),
                Text("à la source Ue → adaptation d'impédance.", font_size=19),
                Text("Application : voltmètre électronique (mesure sans", font_size=19),
                Text("perturber le circuit mesuré).", font_size=19),
            ).arrange(DOWN, aligned_edge=LEFT, buff=0.16),
            box_width=11.2,
        )
        exemple.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Le gain Av du suiveur vaut donc 1 : la tension est "
                "recopiée à l'identique. Son intérêt n'est pas "
                "d'amplifier, mais d'adapter l'impédance : puisque i plus "
                "est nul, le suiveur ne prélève aucun courant à la source "
                "Ue, contrairement à un appareil de mesure classique. "
                "C'est le principe du voltmètre électronique, qui mesure "
                "une tension sans perturber le circuit mesuré."
            )
        ) as tracker:
            self.play(FadeIn(exemple))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(exemple))

        # --- À retenir --------------------------------------------------------
        retenir = essentiel_box(
            VGroup(
                Text("À retenir", font_size=24, weight="BOLD"),
                MathTex(r"U_s = U_e \quad ; \quad A_v = 1", font_size=28),
                Text("Intérêt : adaptation d'impédance (i+ = 0).", font_size=20),
            ).arrange(DOWN, buff=0.22),
            box_width=11.2,
        )
        retenir.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Retenons l'essentiel. Us égale Ue, le gain vaut 1. "
                "L'intérêt du montage suiveur est l'adaptation "
                "d'impédance, grâce au courant d'entrée nul."
            )
        ) as tracker:
            self.play(FadeIn(retenir))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(retenir))

        # --- Pièges à éviter --------------------------------------------------
        pieges = warning_box(
            VGroup(
                Text("• Le suiveur n'est PAS un simple fil : c'est bien un", font_size=19),
                Text("   AO en régime linéaire, avec ε = 0, qui impose", font_size=19),
                Text("   Us = Ue tout en isolant la source de la charge.", font_size=19),
                Text("• Ne pas confondre gain Av = 1 avec « aucun intérêt » :", font_size=19),
                Text("   son rôle est l'adaptation d'impédance, pas l'ampli.", font_size=19),
            ).arrange(DOWN, aligned_edge=LEFT, buff=0.15),
            box_width=12.0,
        )
        pieges.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Deux pièges à éviter. Le suiveur n'est pas un simple fil "
                ": c'est bien un AO en régime linéaire, avec epsilon égal "
                "à zéro, qui impose Us égale Ue tout en isolant la source "
                "de la charge. Et ne confondez pas un gain de 1 avec "
                "l'absence d'intérêt : son rôle est l'adaptation "
                "d'impédance, pas l'amplification."
            )
        ) as tracker:
            self.play(FadeIn(pieges))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(pieges), FadeOut(titre))
