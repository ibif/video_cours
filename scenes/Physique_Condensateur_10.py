"""
scenes/Physique_Condensateur_10.py — Chapitre 9 « Le condensateur »
(1ereC, Physique), scène 10.

§ 6b. Constante de temps τ=RC. Définition τ=RC (secondes). Interprétation
qualitative : τ donne l'ordre de grandeur de la durée du régime
transitoire ; à t=τ, il reste environ 37 % (décharge) ou l'on a atteint
environ 63 % (charge) ; le phénomène est considéré comme terminé à 5τ.
Exemple résolu 7 : R=10 kΩ, C=100 µF → τ=1 s, durée totale ≈5 s.
Source : 1ereC/Physique.pdf, pages 88-98 (chapitre 9, § 6b).
"""

import textwrap

import numpy as np

from manim import (
    DOWN,
    LEFT,
    RIGHT,
    UP,
    WHITE,
    YELLOW,
    Axes,
    Create,
    DashedLine,
    Dot,
    FadeIn,
    FadeOut,
    MathTex,
    Text,
    VGroup,
    Write,
)

from shapes.base_scene import NotionScene
from shapes.boxes import definition_box, essentiel_box, example_box, scene_title, warning_box


def _wrap(text: str, width: int = 56) -> str:
    return "\n".join(textwrap.fill(line, width=width) for line in text.split("\n"))


class ConstanteTempsTauRC(NotionScene):
    def construct(self):
        titre = scene_title("La constante de temps τ = RC")
        titre.scale(0.48)
        titre.to_edge(UP)

        # --- Énoncé -------------------------------------------------------
        mise_en_situation = Text(
            _wrap(
                "Les courbes de charge et décharge s'étalent plus ou moins "
                "vite selon R et C. Existe-t-il une grandeur qui donne, "
                "d'un coup d'œil, l'ordre de grandeur de la durée du "
                "phénomène ?",
                width=56,
            ),
            font_size=23,
        )
        mise_en_situation.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Les courbes de charge et de décharge s'étalent plus ou "
                "moins vite selon les valeurs de R et de C. Existe-t-il une "
                "grandeur qui donne, d'un coup d'œil, l'ordre de grandeur "
                "de la durée du phénomène ?"
            )
        ) as tracker:
            self.play(Write(titre))
            self.play(FadeIn(mise_en_situation))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(mise_en_situation))

        # --- Raisonnement : définition de τ ---------------------------------------
        definition_tau = definition_box(
            VGroup(
                Text("La constante de temps du circuit RC est définie par :", font_size=21),
                MathTex(r"\tau = R\, C", font_size=34, color=YELLOW),
                Text("R en ohms (Ω), C en farads (F), τ en SECONDES (s).", font_size=20),
                MathTex(r"1\ \Omega \times 1\ \text{F} = 1\ \text{s}", font_size=24),
            ).arrange(DOWN, buff=0.22),
            box_width=10.6,
        )
        definition_tau.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "La constante de temps du circuit R C est définie par tau "
                "égale R fois C, avec R en ohms, C en farads. Le produit "
                "d'un ohm par un farad donne exactement une seconde : tau "
                "s'exprime donc en secondes."
            )
        ) as tracker:
            self.play(FadeIn(definition_tau))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(definition_tau))

        # --- Repères 63% / 37% / 5τ sur la courbe de charge -----------------------
        axes = Axes(
            x_range=[0, 5, 1],
            y_range=[0, 6, 1],
            x_length=6.0,
            y_length=3.6,
            axis_config={"include_tip": True, "stroke_width": 2, "color": WHITE},
        )
        axes.next_to(titre, DOWN, buff=0.55).shift(LEFT * 2.2)
        E_val = 5
        courbe = axes.plot(lambda t: E_val * (1 - np.exp(-t)), x_range=[0, 5], color=YELLOW)
        asymptote = DashedLine(axes.c2p(0, E_val), axes.c2p(5, E_val), color=WHITE, stroke_width=1.5)

        point_tau = Dot(axes.c2p(1, E_val * (1 - np.exp(-1))), color="#4FA8FF", radius=0.07)
        ligne_tau_v = DashedLine(axes.c2p(1, 0), axes.c2p(1, E_val * (1 - np.exp(-1))), color="#4FA8FF", stroke_width=1.5)
        label_tau = MathTex(r"\tau", font_size=22, color="#4FA8FF").next_to(ligne_tau_v, DOWN, buff=0.1)
        label_63 = Text("≈ 63 % de E", font_size=17, color="#4FA8FF").next_to(point_tau, UP, buff=0.15)

        point_5tau = Dot(axes.c2p(5, E_val * (1 - np.exp(-5))), color="#FF7A5C", radius=0.07)
        label_5tau = Text("phénomène terminé", font_size=16, color="#FF7A5C").next_to(point_5tau, DOWN, buff=0.2).shift(LEFT * 0.3)
        label_5tau2 = MathTex(r"\approx 5\tau", font_size=20, color="#FF7A5C").next_to(label_5tau, DOWN, buff=0.08)

        graphe = VGroup(axes, courbe, asymptote, point_tau, ligne_tau_v, label_tau, label_63, point_5tau, label_5tau, label_5tau2)

        with self.voiceover(
            text=(
                "Sur la courbe de charge, au bout d'une durée égale à tau, "
                "la tension a déjà atteint environ soixante-trois pourcents "
                "de sa valeur finale E. Symétriquement, sur une décharge, "
                "il resterait environ trente-sept pourcents de la tension "
                "initiale au bout de tau. Et l'on considère, par "
                "convention, que le phénomène est pratiquement terminé au "
                "bout d'une durée d'environ cinq tau."
            )
        ) as tracker:
            self.play(Create(axes), Create(courbe), FadeIn(asymptote))
            self.play(FadeIn(point_tau), Create(ligne_tau_v), Write(label_tau), FadeIn(label_63))
            self.play(FadeIn(point_5tau), FadeIn(label_5tau), FadeIn(label_5tau2))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(graphe))

        # --- Exemple résolu 7 ------------------------------------------------------
        exemple = example_box(
            VGroup(
                Text("Un circuit RC a R = 10 kΩ et C = 100 µF.", font_size=21),
                MathTex(r"\tau = R\,C = 10\,000 \times 100\times10^{-6} = 1\ \text{s}", font_size=27),
                Text("La charge (ou la décharge) est donc pratiquement terminée", font_size=20),
                MathTex(r"\text{au bout d'environ } 5\tau = 5\ \text{s}.", font_size=25),
            ).arrange(DOWN, buff=0.22),
            box_width=11.6,
        )
        exemple.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Exemple résolu : un circuit R C a une résistance de dix "
                "kilohms et une capacité de cent microfarads. Sa constante "
                "de temps vaut R C, soit dix mille fois cent fois dix "
                "puissance moins six, c'est-à-dire une seconde. La charge, "
                "ou la décharge, de ce condensateur est donc pratiquement "
                "terminée au bout d'environ cinq tau, soit cinq secondes."
            )
        ) as tracker:
            self.play(FadeIn(exemple))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(exemple))

        # --- À retenir -------------------------------------------------------------
        retenir = essentiel_box(
            VGroup(
                Text("À retenir", font_size=24, weight="BOLD"),
                MathTex(r"\tau = R\,C \ \ (\text{secondes})", font_size=28),
                Text("À t = τ : ≈ 63 % de E atteints (charge) ou ≈ 37 % restants", font_size=19),
                Text("(décharge). Phénomène terminé à environ 5τ.", font_size=19),
            ).arrange(DOWN, buff=0.2),
            box_width=11.6,
        )
        retenir.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Retenons l'essentiel : tau égale R C, en secondes. À "
                "l'instant tau, on a atteint environ soixante-trois "
                "pourcents de E en charge, ou il reste environ trente-sept "
                "pourcents en décharge. Le phénomène est considéré comme "
                "terminé au bout d'environ cinq tau."
            )
        ) as tracker:
            self.play(FadeIn(retenir))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(retenir))

        # --- Pièges à éviter --------------------------------------------------------
        pieges = warning_box(
            VGroup(
                Text("• Convertir R en OHMS et C en FARADS avant de multiplier", font_size=20),
                Text("   (kΩ → Ω, µF → F), sinon τ n'a pas la bonne valeur.", font_size=20),
                Text("• À t = τ, le phénomène n'est PAS terminé (seulement 63 %", font_size=20),
                Text("   ou 37 %) : il faut attendre environ 5τ pour le considérer", font_size=20),
                Text("   comme achevé.", font_size=20),
            ).arrange(DOWN, aligned_edge=LEFT, buff=0.16),
            box_width=12.2,
        )
        pieges.next_to(titre, DOWN, buff=0.35)

        with self.voiceover(
            text=(
                "Deux pièges à éviter. Il faut convertir R en ohms et C en "
                "farads avant de les multiplier : oublier de convertir les "
                "kilohms ou les microfarads fausse complètement la valeur "
                "de tau. Et à l'instant tau, le phénomène n'est pas encore "
                "terminé, seulement soixante-trois ou trente-sept pourcents "
                "accomplis : il faut attendre environ cinq tau pour le "
                "considérer comme achevé."
            )
        ) as tracker:
            self.play(FadeIn(pieges))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(pieges), FadeOut(titre))
