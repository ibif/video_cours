"""
scenes/Physique_EnergiePotentielleElectrostatique_08.py — Chapitre « Énergie
potentielle électrostatique » (1ereC, Physique), scène 08.

Conservation de l'énergie mécanique pour une particule chargée :
Em=Ec+Ep=½mv²+qV, conservation car force électrostatique conservative
(poids souvent négligeable). Théorème Ec(A)+qV_A=Ec(B)+qV_B, reformulation
du théorème de l'énergie cinétique ΔEc=W(F⃗)=q(V_A-V_B)=qU_AB.
Source : 1ereC/Physique.pdf, pages 66-75.
"""

import textwrap

from manim import DOWN, LEFT, RIGHT, UP, YELLOW, FadeIn, FadeOut, MathTex, Text, VGroup, Write

from shapes.base_scene import NotionScene
from shapes.boxes import essentiel_box, scene_title, theorem_box, warning_box


def _wrap(text: str, width: int = 56) -> str:
    return "\n".join(textwrap.fill(line, width=width) for line in text.split("\n"))


class ConservationEnergieMecanique(NotionScene):
    def construct(self):
        titre = scene_title("Conservation de l'énergie mécanique")
        titre.scale(0.5)
        titre.to_edge(UP)

        # --- Énoncé : énergie mécanique d'une particule chargée -----------------------
        enonce = Text(
            _wrap(
                "Une particule de charge q et de masse m se déplace dans "
                "un champ électrostatique, du point A au point B. Que "
                "devient son énergie mécanique ?",
                width=54,
            ),
            font_size=23,
        )
        enonce.next_to(titre, DOWN, buff=0.7)

        with self.voiceover(
            text=(
                "Considérons une particule de charge q et de masse m, se "
                "déplaçant dans un champ électrostatique, du point A "
                "jusqu'au point B. Que devient son énergie mécanique au "
                "cours de ce trajet ?"
            )
        ) as tracker:
            self.play(Write(enonce))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(enonce))

        # --- Raisonnement : théorème de l'énergie cinétique reformulé -----------------
        tec = MathTex(
            r"\Delta E_c = E_c(B) - E_c(A) = W_{A \to B}(\vec{F}) = q\,(V_A - V_B) = qU_{AB}",
            font_size=25,
        )
        tec.next_to(titre, DOWN, buff=0.8)

        with self.voiceover(
            text=(
                "Reprenons le théorème de l'énergie cinétique. La "
                "variation d'énergie cinétique entre A et B est égale au "
                "travail de la force électrostatique — en négligeant, "
                "comme souvent, le poids de la particule devant la force "
                "électrique. Ce travail vaut q fois V A moins V B, "
                "c'est-à-dire q fois U A B."
            )
        ) as tracker:
            self.play(Write(tec))
            self.wait(tracker.get_remaining_duration())

        self.play(tec.animate.scale(0.75).to_edge(UP + RIGHT).shift(DOWN * 0.9))

        regroupement1 = MathTex(r"E_c(B) - E_c(A) = qV_A - qV_B", font_size=27)
        regroupement2 = MathTex(
            r"E_c(B) + qV_B = E_c(A) + qV_A",
            font_size=30,
            color=YELLOW,
        )
        regroupement = VGroup(regroupement1, regroupement2).arrange(DOWN, buff=0.45)
        regroupement.next_to(titre, DOWN, buff=0.9).to_edge(LEFT, buff=0.7)

        with self.voiceover(
            text=(
                "En développant q fois V A moins V B, puis en regroupant "
                "les termes en A d'un côté et les termes en B de l'autre — "
                "exactement comme nous l'avions fait pour le poids — on "
                "obtient une relation remarquable : l'énergie cinétique en "
                "B, plus q V B, est égale à l'énergie cinétique en A, plus "
                "q V A."
            )
        ) as tracker:
            self.play(Write(regroupement1))
            self.play(Write(regroupement2))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(tec))
        self.play(regroupement.animate.move_to(UP * 1.0))

        # --- Interprétation : énergie mécanique ------------------------------------------
        interpretation = theorem_box(
            VGroup(
                Text("Énergie mécanique de la particule chargée :", font_size=22),
                MathTex(r"E_m = E_c + E_p = \dfrac{1}{2}mv^2 + qV", font_size=30),
                Text("se conserve : Em(A) = Em(B).", font_size=21),
            ).arrange(DOWN, buff=0.25),
            box_width=9.6,
        )
        interpretation.next_to(regroupement, DOWN, buff=0.7)

        with self.voiceover(
            text=(
                "Cette quantité conservée, Ec plus q V, n'est autre que "
                "l'énergie mécanique de la particule : la somme de son "
                "énergie cinétique, un demi m v carré, et de son énergie "
                "potentielle électrostatique, q V. Comme la force "
                "électrostatique est conservative, et le poids négligé ou "
                "lui-même conservatif, l'énergie mécanique de la particule "
                "se conserve tout au long du trajet."
            )
        ) as tracker:
            self.play(FadeIn(interpretation))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(regroupement), FadeOut(interpretation))

        # --- Mise en garde : poids négligeable, à justifier -----------------------------
        remarque = warning_box(
            Text(
                _wrap(
                    "Le poids est en général négligeable devant la force "
                    "électrostatique pour une particule chargée légère "
                    "(électron, ion) — mais cela doit toujours être "
                    "justifié par un calcul, jamais simplement affirmé.",
                    width=52,
                ),
                font_size=22,
            ),
            box_width=11.0,
        )
        remarque.next_to(titre, DOWN, buff=0.7)

        with self.voiceover(
            text=(
                "Une remarque importante : le poids est en général "
                "négligeable devant la force électrostatique, pour une "
                "particule chargée légère comme un électron ou un ion. "
                "Mais attention, cette approximation doit toujours être "
                "justifiée par un calcul comparant les deux forces, et "
                "jamais simplement affirmée sans vérification."
            )
        ) as tracker:
            self.play(FadeIn(remarque))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(remarque))

        # --- À retenir --------------------------------------------------------------------
        retenir = essentiel_box(
            VGroup(
                Text(
                    "Em = Ec + Ep = ½mv² + qV se conserve (force "
                    "électrostatique conservative, poids souvent négligé).",
                    font_size=20,
                ),
                MathTex(r"E_c(A) + qV_A = E_c(B) + qV_B", font_size=26),
                Text("Reformulation : ΔEc = qU_AB.", font_size=20),
            ).arrange(DOWN, buff=0.25),
            box_width=10.6,
        )
        retenir.next_to(titre, DOWN, buff=0.6)

        with self.voiceover(
            text=(
                "À retenir : l'énergie mécanique d'une particule chargée, "
                "somme de son énergie cinétique et de son énergie "
                "potentielle électrostatique q V, se conserve dans un "
                "champ électrostatique. On peut l'écrire Ec de A plus q V "
                "A égale Ec de B plus q V B, ce qui reformule simplement le "
                "théorème de l'énergie cinétique : delta Ec égale q U A B."
            )
        ) as tracker:
            self.play(FadeIn(retenir))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(titre), FadeOut(retenir))
