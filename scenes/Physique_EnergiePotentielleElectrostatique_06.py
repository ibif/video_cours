"""
scenes/Physique_EnergiePotentielleElectrostatique_06.py — Chapitre « Énergie
potentielle électrostatique » (1ereC, Physique), scène 06.

Énergie potentielle électrostatique : théorème ΔEp=-W_A→B(F⃗) (force
conservative), établissement de Ep=qV à partir de W=qU_AB=q(V_A-V_B),
définition Ep(M)=qV_M (+constante), attention au signe. Exemple résolu :
ion q=-2,5 µC en M (V_M=300 V) → Ep=-7,5×10⁻⁴ J ; déplacement vers N
(V_N=100 V) → W=-5×10⁻⁴ J résistant, ΔEp=+5×10⁻⁴ J.
Source : 1ereC/Physique.pdf, pages 66-75.
"""

import textwrap

from manim import DOWN, LEFT, RED, RIGHT, UP, YELLOW, FadeIn, FadeOut, MathTex, Text, VGroup, Write

from shapes.base_scene import NotionScene
from shapes.boxes import definition_box, essentiel_box, example_box, scene_title, theorem_box, warning_box


def _wrap(text: str, width: int = 56) -> str:
    return "\n".join(textwrap.fill(line, width=width) for line in text.split("\n"))


class EnergiePotentielleElectrostatique(NotionScene):
    def construct(self):
        titre = scene_title("Énergie potentielle électrostatique")
        titre.scale(0.5)
        titre.to_edge(UP)

        # --- Énoncé : rappel du théorème général --------------------------------------
        rappel = theorem_box(
            MathTex(
                r"\Delta E_p = E_p(B) - E_p(A) = -\,W_{A \to B}(\vec{F})",
                font_size=29,
            ),
            box_width=9.2,
        )
        rappel.next_to(titre, DOWN, buff=0.6)

        with self.voiceover(
            text=(
                "La force électrostatique étant conservative, on peut lui "
                "associer, exactement comme pour le poids, une énergie "
                "potentielle. Le théorème général s'écrit : delta Ep, "
                "égale Ep de B moins Ep de A, égale moins le travail de la "
                "force électrostatique de A vers B."
            )
        ) as tracker:
            self.play(FadeIn(rappel))
            self.wait(tracker.get_remaining_duration())

        self.play(rappel.animate.scale(0.7).to_corner(UP + RIGHT).shift(DOWN * 0.2))

        # --- Raisonnement : établissement de Ep=qV ----------------------------------------
        demo1 = MathTex(r"W_{A \to B}(\vec{F}) = qU_{AB} = q\,(V_A - V_B)", font_size=27)
        demo2 = MathTex(
            r"\Delta E_p = -\,W_{A \to B}(\vec{F}) = q\,(V_B - V_A) = qV_B - qV_A",
            font_size=27,
        )
        demo3 = MathTex(
            r"\text{Par identification : } E_p(M) = qV_M",
            font_size=29,
            color=YELLOW,
        )
        demo = VGroup(demo1, demo2, demo3).arrange(DOWN, buff=0.4, aligned_edge=LEFT)
        demo.next_to(titre, DOWN, buff=0.9).to_edge(LEFT, buff=0.6)

        with self.voiceover(
            text=(
                "Établissons l'expression de cette énergie potentielle. "
                "Nous savons que le travail de la force électrostatique de "
                "A vers B vaut q U A B, c'est-à-dire q fois V A moins V B. "
                "En reportant dans le théorème, delta Ep vaut donc q fois V "
                "B moins V A, c'est-à-dire q V B moins q V A. Par "
                "identification terme à terme, on obtient l'expression de "
                "l'énergie potentielle électrostatique en un point M : Ep "
                "de M égale q fois V M."
            )
        ) as tracker:
            self.play(Write(demo1))
            self.play(Write(demo2))
            self.play(Write(demo3))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(demo), FadeOut(rappel))

        # --- Définition -------------------------------------------------------------------
        definition = definition_box(
            VGroup(
                MathTex(r"E_p(M) = qV_M \; (+\text{constante})", font_size=30),
                Text(
                    "Référence : Ep=0 là où V=0 (même référence que V).",
                    font_size=21,
                ),
            ).arrange(DOWN, buff=0.3),
            box_width=9.6,
        )
        definition.next_to(titre, DOWN, buff=0.7)

        with self.voiceover(
            text=(
                "Retenons la définition : l'énergie potentielle "
                "électrostatique d'une charge q au point M vaut q fois V "
                "M, à une constante additive près. On choisit naturellement "
                "la même référence que pour le potentiel : Ep est nulle là "
                "où V est nul."
            )
        ) as tracker:
            self.play(FadeIn(definition))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(definition))

        # --- Attention au signe --------------------------------------------------------
        attention = warning_box(
            Text(
                _wrap(
                    "Attention au signe ! Ep=qV : si q est négative et V "
                    "positif, Ep est négative (et inversement). Le signe "
                    "de Ep dépend à la fois de celui de la charge et de "
                    "celui du potentiel.",
                    width=54,
                ),
                font_size=22,
            ),
            box_width=11.0,
        )
        attention.next_to(titre, DOWN, buff=0.7)

        with self.voiceover(
            text=(
                "Attention, un piège classique : puisque Ep vaut q fois V, "
                "si la charge q est négative et le potentiel V positif, "
                "alors l'énergie potentielle Ep est négative — et "
                "inversement si q est positive et V négatif. Le signe de "
                "Ep dépend donc à la fois du signe de la charge et de celui "
                "du potentiel, il faut être très vigilant."
            )
        ) as tracker:
            self.play(FadeIn(attention))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(attention))

        # --- Exemple résolu 4 -----------------------------------------------------------
        enonce = Text(
            _wrap(
                "Exemple : un ion de charge q=-2,5 µC est en M, où "
                "V_M=300 V. Calculer Ep(M), puis étudier son déplacement "
                "vers N, où V_N=100 V.",
                width=54,
            ),
            font_size=21,
        )
        enonce.next_to(titre, DOWN, buff=0.7)

        with self.voiceover(
            text=(
                "Exemple d'application. Un ion, de charge moins 2 virgule 5 "
                "microcoulombs, se trouve au point M, où le potentiel vaut "
                "300 volts. Calculons son énergie potentielle en M, puis "
                "étudions son déplacement vers le point N, où le potentiel "
                "vaut 100 volts."
            )
        ) as tracker:
            self.play(Write(enonce))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(enonce))

        calcul1 = example_box(
            MathTex(
                r"E_p(M) = qV_M = -2{,}5\times10^{-6} \times 300 = -7{,}5\times10^{-4}\ \text{J}",
                font_size=25,
            ),
            box_width=10.6,
        )
        calcul1.next_to(titre, DOWN, buff=0.7)

        with self.voiceover(
            text=(
                "L'énergie potentielle en M vaut q fois V M, soit moins 2 "
                "virgule 5 fois 10 puissance moins 6, fois 300, ce qui "
                "donne moins 7 virgule 5 fois 10 puissance moins 4 joule : "
                "une énergie potentielle négative, cohérente avec une "
                "charge négative en un point de potentiel positif."
            )
        ) as tracker:
            self.play(FadeIn(calcul1))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(calcul1))

        calcul2 = example_box(
            VGroup(
                MathTex(
                    r"W_{M \to N}(\vec{F}) = q\,(V_M - V_N) = -2{,}5\times10^{-6}\times 200",
                    font_size=23,
                ),
                MathTex(r"= -5\times10^{-4}\ \text{J} \; (\text{résistant})", font_size=25, color=RED),
                MathTex(
                    r"\Delta E_p = -\,W_{M \to N}(\vec{F}) = +5\times10^{-4}\ \text{J} > 0",
                    font_size=25,
                    color=YELLOW,
                ),
            ).arrange(DOWN, buff=0.28),
            box_width=11.2,
        )
        calcul2.next_to(titre, DOWN, buff=0.6)

        with self.voiceover(
            text=(
                "Le travail de la force électrostatique de M vers N vaut q "
                "fois V M moins V N, soit moins 2 virgule 5 fois 10 "
                "puissance moins 6 fois 200, c'est-à-dire moins 5 fois 10 "
                "puissance moins 4 joule : un travail résistant. La "
                "variation d'énergie potentielle vaut donc l'opposé, plus 5 "
                "fois 10 puissance moins 4 joule, positive : c'est bien "
                "cohérent, un travail résistant s'accompagne toujours d'un "
                "gain d'énergie potentielle."
            )
        ) as tracker:
            self.play(FadeIn(calcul2))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(calcul2))

        # --- À retenir ---------------------------------------------------------------------
        retenir = essentiel_box(
            Text(
                _wrap(
                    "Ep(M)=qV_M (+constante). ΔEp=-W_A→B(F⃗). Attention au "
                    "signe : Ep dépend à la fois du signe de q et de celui "
                    "de V — une charge négative dans un potentiel positif "
                    "a une énergie potentielle négative.",
                    width=56,
                ),
                font_size=21,
            )
        )
        retenir.next_to(titre, DOWN, buff=0.6)

        with self.voiceover(
            text=(
                "À retenir : l'énergie potentielle électrostatique en un "
                "point M vaut q fois V M, à une constante près, et sa "
                "variation entre A et B vaut l'opposé du travail de la "
                "force électrostatique de A vers B. Restez toujours "
                "vigilants sur le signe : il dépend conjointement de celui "
                "de la charge et de celui du potentiel."
            )
        ) as tracker:
            self.play(FadeIn(retenir))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(titre), FadeOut(retenir))
