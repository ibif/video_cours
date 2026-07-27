"""
scenes/Physique_EnergiePotentielle_07.py — Chapitre 4 « Énergie potentielle »
(1ereC, Physique), scène 07.

Forces conservatives et énergie potentielle (approche qualitative) :
définition d'une force conservative (travail indépendant du chemin suivi,
nul sur un chemin fermé), exemples (poids et tension conservatives ;
frottements non conservatifs, dissipation en chaleur), théorème général
ΔEp = -W_{A→B}(F⃗), tableau récapitulatif, interprétation qualitative
(signe « moins » = échange d'énergie, équilibre stable = minimum de Ep,
instable = maximum de Ep).
Source : 1ereC/Physique.pdf, chapitre 4, pages 34-42.
"""

import textwrap

from manim import (
    DOWN,
    LEFT,
    ORANGE,
    RED,
    RIGHT,
    UP,
    WHITE,
    YELLOW,
    Axes,
    Dot,
    FadeIn,
    FadeOut,
    Line,
    MathTex,
    Text,
    VGroup,
    Write,
)

from shapes.base_scene import NotionScene
from shapes.boxes import definition_box, essentiel_box, scene_title, theorem_box, warning_box


def _wrap(text: str, width: int = 56) -> str:
    return "\n".join(textwrap.fill(line, width=width) for line in text.split("\n"))


class ForcesConservativesEp(NotionScene):
    def construct(self):
        titre = scene_title("Forces conservatives et énergie potentielle")
        titre.scale(0.5)
        titre.to_edge(UP)

        # --- Énoncé : définition ---------------------------------------------------------
        definition = definition_box(
            Text(
                _wrap(
                    "Une force est dite conservative si son travail entre "
                    "deux points ne dépend pas du chemin suivi. De façon "
                    "équivalente, son travail est nul sur tout chemin "
                    "fermé.",
                    width=54,
                ),
                font_size=23,
            ),
            box_width=11.0,
        )
        definition.next_to(titre, DOWN, buff=0.6)

        with self.voiceover(
            text=(
                "Introduisons la notion de force conservative. Une force "
                "est dite conservative si son travail entre deux points ne "
                "dépend pas du chemin suivi pour aller de l'un à l'autre. "
                "De manière équivalente, son travail est nul sur tout "
                "chemin fermé, c'est-à-dire un aller-retour au même point."
            )
        ) as tracker:
            self.play(FadeIn(definition))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(definition))

        # --- Raisonnement : exemples ------------------------------------------------------
        exemples = VGroup(
            Text("Forces conservatives : poids, tension d'un ressort.", font_size=23, color=YELLOW),
            Text(
                "Forces non conservatives : frottements (le travail dépend "
                "du chemin parcouru, l'énergie se dissipe en chaleur).",
                font_size=23,
                color=RED,
            ),
        ).arrange(DOWN, buff=0.4)
        exemples[1].set(width=min(exemples[1].width, 10.5))
        exemples.next_to(titre, DOWN, buff=0.8)

        with self.voiceover(
            text=(
                "Le poids et la tension d'un ressort sont des forces "
                "conservatives : nous l'avons vu, leur travail ne dépend "
                "que des positions de départ et d'arrivée. À l'inverse, "
                "les forces de frottement ne sont pas conservatives : leur "
                "travail dépend du chemin parcouru — plus le trajet est "
                "long, plus l'énergie dissipée en chaleur est importante."
            )
        ) as tracker:
            self.play(FadeIn(exemples))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(exemples))

        # --- Théorème général ---------------------------------------------------------------
        theoreme = theorem_box(
            VGroup(
                Text("À toute force conservative F⃗, on associe une énergie potentielle Ep telle que :", font_size=21),
                MathTex(r"\Delta E_p = E_p(B) - E_p(A) = -W_{A \to B}(\vec{F})", font_size=30),
            ).arrange(DOWN, buff=0.3),
            box_width=11.4,
        )
        theoreme.next_to(titre, DOWN, buff=0.6)

        with self.voiceover(
            text=(
                "Voici le théorème général qui généralise tout ce que nous "
                "avons vu. À toute force conservative F, on peut associer "
                "une énergie potentielle Ep, telle que la variation de "
                "cette énergie potentielle entre A et B soit égale à "
                "l'opposé du travail de cette force entre A et B."
            )
        ) as tracker:
            self.play(FadeIn(theoreme))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(theoreme))

        # --- Tableau récapitulatif ------------------------------------------------------------
        ligne_titre = VGroup(
            Text("Force conservative", font_size=22, color=YELLOW),
            Text("Énergie potentielle associée", font_size=22, color=YELLOW),
        ).arrange(RIGHT, buff=1.5)
        ligne1 = VGroup(
            Text("Poids", font_size=22),
            MathTex(r"E_{pp} = mgz + \text{Cte}", font_size=26),
        ).arrange(RIGHT, buff=1.9)
        ligne2 = VGroup(
            Text("Tension du ressort", font_size=22),
            MathTex(r"E_{pe} = \dfrac{1}{2}kx^2", font_size=26),
        ).arrange(RIGHT, buff=1.0)

        tableau = VGroup(ligne_titre, ligne1, ligne2).arrange(DOWN, buff=0.45, aligned_edge=LEFT)
        ligne1.align_to(ligne_titre, LEFT)
        ligne2.align_to(ligne_titre, LEFT)
        trait = Line(LEFT * (tableau.width / 2), RIGHT * (tableau.width / 2), color=WHITE)
        trait.next_to(ligne_titre, DOWN, buff=0.15)
        tableau.add(trait)
        tableau.move_to(trait.get_center() + (ligne_titre.get_center() - trait.get_center()))
        tableau.next_to(titre, DOWN, buff=0.8)

        with self.voiceover(
            text=(
                "Résumons dans un tableau les deux énergies potentielles "
                "du programme. Au poids est associée l'énergie potentielle "
                "de pesanteur, m g z plus une constante. À la tension du "
                "ressort est associée l'énergie potentielle élastique, un "
                "demi k x carré."
            )
        ) as tracker:
            self.play(Write(tableau))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(tableau))

        # --- Interprétation qualitative : le signe « moins » ----------------------------------
        signe = warning_box(
            Text(
                _wrap(
                    "Le signe « moins » traduit un échange d'énergie : si "
                    "le travail de F⃗ est moteur, Ep diminue et l'énergie "
                    "cinétique augmente d'autant (et inversement pour un "
                    "travail résistant).",
                    width=54,
                ),
                font_size=22,
            ),
            box_width=11.2,
        )
        signe.next_to(titre, DOWN, buff=0.7)

        with self.voiceover(
            text=(
                "Ce signe moins n'est pas un détail : il traduit un "
                "véritable échange d'énergie. Si le travail de la force "
                "conservative est moteur, l'énergie potentielle diminue, "
                "et cette énergie perdue se retrouve sous forme d'énergie "
                "cinétique. Inversement, si le travail est résistant, "
                "l'énergie potentielle augmente, aux dépens de l'énergie "
                "cinétique."
            )
        ) as tracker:
            self.play(FadeIn(signe))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(signe))

        # --- Positions d'équilibre : minima et maxima de Ep -----------------------------------
        axes = Axes(
            x_range=[-3, 3, 1],
            y_range=[0, 5, 1],
            x_length=6.5,
            y_length=3.6,
            axis_config={"include_tip": True, "stroke_width": 2, "color": WHITE},
        )
        axes.next_to(titre, DOWN, buff=0.6)

        courbe = axes.plot(lambda x: 0.35 * x**2 - 0.06 * x**4 + 2.2, x_range=[-2.85, 2.85], color=ORANGE)

        stable = Dot(axes.c2p(0, 2.2), color=YELLOW, radius=0.08)
        label_stable = Text("équilibre stable\n(minimum de Ep)", font_size=18, color=YELLOW)
        label_stable.next_to(stable, DOWN, buff=0.3)

        instable = Dot(axes.c2p(2.35, 0.35 * 2.35**2 - 0.06 * 2.35**4 + 2.2), color=RED, radius=0.08)
        label_instable = Text("équilibre instable\n(maximum de Ep)", font_size=18, color=RED)
        label_instable.next_to(instable, UP, buff=0.3)

        figure = VGroup(axes, courbe, stable, label_stable, instable, label_instable)

        with self.voiceover(
            text=(
                "Une conséquence qualitative importante concerne les "
                "positions d'équilibre d'un système. Sur une courbe "
                "d'énergie potentielle en fonction de la position, les "
                "creux correspondent à des positions d'équilibre stable : "
                "ce sont des minima de Ep. Les bosses, elles, correspondent "
                "à des positions d'équilibre instable : ce sont des maxima "
                "de Ep."
            )
        ) as tracker:
            self.play(FadeIn(axes))
            self.play(FadeIn(courbe))
            self.play(FadeIn(stable), Write(label_stable))
            self.play(FadeIn(instable), Write(label_instable))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(figure))

        # --- À retenir ------------------------------------------------------------------------
        retenir = essentiel_box(
            Text(
                _wrap(
                    "Force conservative : travail indépendant du chemin "
                    "(nul sur un chemin fermé). ΔEp=-W(F). Poids→Epp, "
                    "tension→Epe. Minima de Ep = équilibre stable, maxima "
                    "= équilibre instable.",
                    width=56,
                ),
                font_size=22,
            )
        )
        retenir.next_to(titre, DOWN, buff=0.6)

        with self.voiceover(
            text=(
                "À retenir : une force conservative a un travail "
                "indépendant du chemin suivi, nul sur un chemin fermé. À "
                "toute force conservative est associée une énergie "
                "potentielle telle que delta Ep égale moins le travail de "
                "cette force. Les minima de Ep correspondent aux positions "
                "d'équilibre stable, les maxima aux positions d'équilibre "
                "instable."
            )
        ) as tracker:
            self.play(FadeIn(retenir))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(titre), FadeOut(retenir))
