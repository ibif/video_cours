"""
scenes/Physique_AmplificateurOperationnel_02.py — Chapitre « L'amplificateur
opérationnel » (1ereC, Physique), scène 02.

§ 2. Caractéristique de transfert Vs = f(ε) : trois zones (saturation
haute, régime linéaire, saturation basse). Zone linéaire : Vs = A0·ε avec
A0 ≈ 10^5 à 10^6. AO idéal : A0 infini, résistance d'entrée infinie,
résistance de sortie nulle → en régime linéaire, i+ = i- = 0 et ε = 0
(V+ = V-). Tableau des deux régimes de fonctionnement.
Source : 1ereC/Physique.pdf, pages 99-107 (§ 2).
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
    Axes,
    FadeIn,
    FadeOut,
    MathTex,
    Text,
    VGroup,
    Write,
)

from shapes.base_scene import NotionScene
from shapes.boxes import definition_box, essentiel_box, property_box, scene_title, theorem_box, warning_box


def _wrap(text: str, width: int = 56) -> str:
    return "\n".join(textwrap.fill(line, width=width) for line in text.split("\n"))


def _caracteristique_transfert():
    """Axes + courbe Vs = f(ε) avec les 3 zones : saturation basse
    (plateau -Vsat), régime linéaire (pente très raide autour de ε=0),
    saturation haute (plateau +Vsat). Pente exagérée pour la lisibilité
    (A0 réel est bien plus grand, il faut l'imaginer quasi vertical)."""
    axes = Axes(
        x_range=[-3, 3, 1],
        y_range=[-15, 15, 5],
        x_length=6.4,
        y_length=4.4,
        axis_config={"include_tip": True, "stroke_width": 2, "color": WHITE},
    )
    courbe = axes.plot(lambda x: max(-12, min(12, 300 * x)), x_range=[-3, 3], color=YELLOW)

    x_lab = MathTex(r"\varepsilon", font_size=26).next_to(axes.x_axis.get_end(), DOWN, buff=0.15)
    y_lab = MathTex(r"V_s", font_size=26).next_to(axes.y_axis.get_end(), UP, buff=0.1)

    vsat_haut = MathTex(r"+V_{sat}", font_size=20, color=ORANGE).next_to(
        axes.c2p(-2.8, 12), UP, buff=0.1
    )
    vsat_bas = MathTex(r"-V_{sat}", font_size=20, color=ORANGE).next_to(
        axes.c2p(-2.8, -12), DOWN, buff=0.1
    )

    return VGroup(axes, courbe, x_lab, y_lab, vsat_haut, vsat_bas)


class CaracteristiqueTransfertAOIdeal(NotionScene):
    def construct(self):
        titre = scene_title("Caractéristique de transfert et AO idéal")
        titre.scale(0.42)
        titre.to_edge(UP)

        # --- Énoncé -------------------------------------------------------
        mise_en_situation = Text(
            _wrap(
                "La sortie de l'AO ne réagit pas toujours proportionnellement "
                "à ce qu'on lui applique en entrée. Comment évolue-t-elle "
                "réellement en fonction de ε, et que signifie considérer "
                "un AO comme « idéal » ?",
                width=58,
            ),
            font_size=22,
        )
        mise_en_situation.next_to(titre, DOWN, buff=0.35)

        with self.voiceover(
            text=(
                "La tension de sortie de l'AO ne réagit pas toujours "
                "proportionnellement à ce qu'on lui applique en entrée. "
                "Comment évolue-t-elle réellement en fonction de epsilon, "
                "et que signifie considérer un AO comme idéal ?"
            )
        ) as tracker:
            self.play(Write(titre))
            self.play(FadeIn(mise_en_situation))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(mise_en_situation))

        # --- Raisonnement : caractéristique de transfert --------------------
        graphe = _caracteristique_transfert()
        graphe.scale(0.85)
        graphe.next_to(titre, DOWN, buff=0.4).shift(LEFT * 2.6)

        zones = VGroup(
            Text("Saturation basse : Vs = −Vsat", font_size=19, color=ORANGE),
            Text("Régime linéaire : Vs = A0 · ε", font_size=19, color=YELLOW),
            Text("Saturation haute : Vs = +Vsat", font_size=19, color=ORANGE),
            Text("(A0 ≈ 10⁵ à 10⁶)", font_size=18),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.2)
        zones.next_to(graphe, RIGHT, buff=0.6)

        with self.voiceover(
            text=(
                "La caractéristique de transfert, c'est-à-dire la courbe "
                "Vs égale f de epsilon, présente trois zones. Loin de zéro, "
                "la sortie plafonne à moins Vsat : c'est la saturation "
                "basse. Autour de epsilon égale zéro, une zone très étroite "
                "où Vs égale A0 fois epsilon : c'est le régime linéaire, "
                "avec A0 de l'ordre de cent mille à un million. Enfin, la "
                "sortie plafonne à plus Vsat : c'est la saturation haute."
            )
        ) as tracker:
            self.play(FadeIn(graphe))
            self.play(FadeIn(zones))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(graphe), FadeOut(zones))

        # --- Raisonnement : AO idéal → relations fondamentales --------------
        ao_ideal = theorem_box(
            VGroup(
                Text("AO idéal : A0 infini, résistance d'entrée infinie,", font_size=20),
                Text("résistance de sortie nulle.", font_size=20),
                Text("Conséquence en régime linéaire (A0 → ∞) :", font_size=20),
                MathTex(r"i_+ = i_- = 0 \quad \text{et} \quad \varepsilon = 0 \ (V_+ = V_-)", font_size=28),
            ).arrange(DOWN, buff=0.2),
            box_width=11.4,
        )
        ao_ideal.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "On modélise l'AO comme idéal : son amplification A0 est "
                "supposée infinie, sa résistance d'entrée infinie, et sa "
                "résistance de sortie nulle. Conséquence essentielle : "
                "puisque la résistance d'entrée est infinie, aucun courant "
                "n'entre par les bornes E plus et E moins, donc i plus "
                "égale i moins égale zéro. Et puisque Vs reste fini alors "
                "que A0 tend vers l'infini, epsilon doit tendre vers zéro "
                "en régime linéaire : V plus égale V moins."
            )
        ) as tracker:
            self.play(FadeIn(ao_ideal))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(ao_ideal))

        # --- Exemple : tableau des deux régimes ------------------------------
        tableau = property_box(
            VGroup(
                Text("Régime LINÉAIRE : réaction négative ET |Vs| < Vsat", font_size=19),
                Text("   → i+ = i− = 0  et  ε = 0", font_size=19, color=YELLOW),
                Text("Régime SATURÉ : pas de réaction négative, ε ≠ 0", font_size=19),
                Text("   → Vs = +Vsat si ε > 0 ; Vs = −Vsat si ε < 0", font_size=19, color=YELLOW),
            ).arrange(DOWN, aligned_edge=LEFT, buff=0.2),
            box_width=11.6,
        )
        tableau.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Retenons les deux régimes possibles. En régime linéaire, "
                "il existe une réaction négative de la sortie vers "
                "l'entrée E moins, et la tension de sortie reste inférieure "
                "à Vsat en valeur absolue : alors i plus, i moins et "
                "epsilon sont nuls. En régime saturé, il n'y a pas de "
                "réaction négative, epsilon n'est PAS nul, et la sortie "
                "vaut plus Vsat ou moins Vsat selon le signe de epsilon."
            )
        ) as tracker:
            self.play(FadeIn(tableau))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(tableau))

        # --- À retenir --------------------------------------------------------
        retenir = essentiel_box(
            VGroup(
                Text("À retenir", font_size=24, weight="BOLD"),
                MathTex(r"\text{Linéaire : } i_+=i_-=0,\ \varepsilon=0 \ (V_+=V_-)", font_size=25),
                MathTex(r"\text{Saturé : } V_s = \pm V_{sat} \ \text{selon le signe de } \varepsilon", font_size=25),
            ).arrange(DOWN, buff=0.22),
            box_width=12.0,
        )
        retenir.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Retenons l'essentiel. En régime linéaire, i plus égale i "
                "moins égale zéro, et epsilon est nul, donc V plus égale V "
                "moins. En régime saturé, la sortie vaut plus ou moins "
                "Vsat selon le signe de epsilon, qui lui n'est plus nul."
            )
        ) as tracker:
            self.play(FadeIn(retenir))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(retenir))

        # --- Pièges à éviter --------------------------------------------------
        pieges = warning_box(
            VGroup(
                Text("• La relation ε = 0 n'est vraie QU'EN régime linéaire", font_size=19),
                Text("   (avec réaction négative) : jamais en saturation.", font_size=19),
                Text("• i+ = i− = 0 vient de la résistance d'entrée infinie,", font_size=19),
                Text("   PAS du fait que le courant « ne passe pas dans", font_size=19),
                Text("   l'AO » — c'est une hypothèse du modèle idéal.", font_size=19),
            ).arrange(DOWN, aligned_edge=LEFT, buff=0.15),
            box_width=12.0,
        )
        pieges.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Deux pièges à éviter. D'abord, la relation epsilon égale "
                "zéro n'est vraie qu'en régime linéaire, avec réaction "
                "négative : jamais en saturation. Ensuite, i plus égale i "
                "moins égale zéro vient de l'hypothèse d'une résistance "
                "d'entrée infinie du modèle idéal, et non du fait que le "
                "courant ne passerait pas dans l'AO."
            )
        ) as tracker:
            self.play(FadeIn(pieges))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(pieges), FadeOut(titre))
