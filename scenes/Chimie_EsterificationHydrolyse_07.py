"""
scenes/Chimie_EsterificationHydrolyse_07.py — Chapitre 8 « Estérification et
hydrolyse d'un ester » (1ereC, Chimie), scène 07.

§ Vérification de l'équilibre par l'hydrolyse (exemple résolu 2 : hydrolyse
0,20mol ester+0,20mol eau → 0,066mol acide formé, vérification retrouve
1/3-2/3) + graphique d'évolution montrant n(ester)→2/3 et n(acide)→1/3 au
cours du temps, stabilisation à l'équilibre.
Source : 1ereC/Chimie.pdf, chapitre 8, page 79.
"""

import textwrap

from manim import (
    DOWN,
    RIGHT,
    UP,
    WHITE,
    YELLOW,
    BLUE,
    ORANGE,
    Axes,
    Create,
    FadeIn,
    FadeOut,
    MathTex,
    Text,
    VGroup,
    Write,
    config,
)

from shapes.base_scene import NotionScene
from shapes.boxes import example_box, scene_title


def _wrap(text: str, width: int = 56) -> str:
    return "\n".join(textwrap.fill(line, width=width) for line in text.split("\n"))


def _fit(mobject, top_y):
    bas_visible = -config.frame_height / 2 + 0.25
    hauteur_dispo = top_y - bas_visible
    if mobject.height > hauteur_dispo:
        mobject.scale(hauteur_dispo / mobject.height, about_point=mobject.get_top())
    return mobject


class VerificationEquilibreParHydrolyse(NotionScene):
    def construct(self):
        titre = scene_title("7. Vérifier l'équilibre en partant de l'ester")
        titre.scale(0.48)
        titre.to_edge(UP)

        # --- Énoncé -----------------------------------------------------------
        enonce = Text(
            _wrap(
                "Si l'équilibre acide + alcool ⇌ ester + eau est vraiment "
                "le même quel que soit le sens de départ, alors partir "
                "directement d'ester et d'eau doit conduire à la même "
                "position d'équilibre. Vérifions-le.",
                width=54,
            ),
            font_size=23,
            color=WHITE,
        )
        enonce.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Si l'équilibre entre acide, alcool, ester et eau est "
                "vraiment le même quel que soit le sens de départ, alors "
                "partir directement d'ester et d'eau doit conduire "
                "exactement à la même position d'équilibre. Vérifions "
                "cela sur un exemple chiffré."
            )
        ) as tracker:
            self.play(Write(titre))
            self.play(FadeIn(enonce))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(enonce))

        # --- Raisonnement / exemple résolu 2 ----------------------------------------
        exemple = example_box(
            VGroup(
                Text(
                    _wrap(
                        "On part cette fois de 0,20 mol d'ester + 0,20 mol "
                        "d'eau (hydrolyse). À l'équilibre, un dosage "
                        "indique qu'il s'est formé 0,066 mol d'acide.",
                        width=46,
                    ),
                    font_size=20,
                ),
                MathTex(
                    r"n_{ester,eq} = 0{,}20 - 0{,}066 = 0{,}134\ mol",
                    font_size=22,
                ),
                MathTex(
                    r"\dfrac{n_{ester,eq}}{n_{acide,eq}} = \dfrac{0{,}134}{0{,}066} \approx 2",
                    font_size=24,
                ),
                Text(
                    "→ soit exactement le rapport 2/3 - 1/3 déjà observé !",
                    font_size=20,
                    color=YELLOW,
                    weight="BOLD",
                ),
            ).arrange(DOWN, buff=0.25),
            box_width=11.8,
        )
        exemple.next_to(titre, DOWN, buff=0.4)
        _fit(exemple, titre.get_bottom()[1] - 0.4)

        with self.voiceover(
            text=(
                "On part cette fois de zéro virgule vingt mole d'ester "
                "et zéro virgule vingt mole d'eau, et l'on déclenche "
                "l'hydrolyse. À l'équilibre, un dosage indique qu'il "
                "s'est formé zéro virgule zéro soixante-six mole "
                "d'acide. Il reste donc zéro virgule cent trente-quatre "
                "mole d'ester. Le rapport entre l'ester restant et "
                "l'acide formé vaut environ deux : on retrouve "
                "exactement le même rapport deux tiers, un tiers, déjà "
                "observé en partant de l'acide et de l'alcool. "
                "L'équilibre est bien unique, quel que soit le sens de "
                "départ."
            )
        ) as tracker:
            self.play(FadeIn(exemple))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(exemple))

        # --- Exemple traité : graphique d'évolution temporelle ------------------------
        entete_graphe = Text("Évolution des quantités de matière au cours du temps", font_size=20, color=YELLOW, weight="BOLD")
        entete_graphe.next_to(titre, DOWN, buff=0.35)

        axes = Axes(
            x_range=[0, 6, 1],
            y_range=[0, 0.11, 0.02],
            x_length=8.5,
            y_length=4.0,
            axis_config={"color": WHITE, "stroke_width": 2, "include_tip": True, "font_size": 16},
        )
        x_label = Text("temps (h)", font_size=16, color=WHITE).next_to(axes.x_axis, RIGHT, buff=0.15)
        y_label = Text("n (mol)", font_size=16, color=WHITE).next_to(axes.y_axis, UP, buff=0.15)

        n0 = 0.10
        n_acide_eq = 0.033
        n_ester_eq = 0.067

        courbe_acide = axes.plot(
            lambda t: n_acide_eq + (n0 - n_acide_eq) * (2.718281828 ** (-1.1 * t)),
            x_range=[0, 6],
            color=ORANGE,
            stroke_width=3,
        )
        courbe_ester = axes.plot(
            lambda t: n_ester_eq * (1 - 2.718281828 ** (-1.1 * t)),
            x_range=[0, 6],
            color=BLUE,
            stroke_width=3,
        )

        label_acide = Text("n(acide) → 1/3 · n₀", font_size=16, color=ORANGE)
        label_acide.next_to(axes.c2p(4.5, n_acide_eq), UP, buff=0.15)
        label_ester = Text("n(ester) → 2/3 · n₀", font_size=16, color=BLUE)
        label_ester.next_to(axes.c2p(4.5, n_ester_eq), UP, buff=0.15)

        graphe = VGroup(axes, x_label, y_label, courbe_acide, courbe_ester, label_acide, label_ester)
        graphe.next_to(entete_graphe, DOWN, buff=0.3)
        _fit(graphe, entete_graphe.get_bottom()[1] - 0.3)

        with self.voiceover(
            text=(
                "Représentons cette évolution sur un graphique : les "
                "quantités de matière en fonction du temps, pour un "
                "mélange équimolaire de départ. La courbe orange, celle "
                "de l'acide, décroît puis se stabilise vers le tiers de "
                "la quantité initiale. La courbe bleue, celle de "
                "l'ester, croît puis se stabilise vers les deux tiers. "
                "Une fois l'équilibre atteint, les deux courbes "
                "deviennent parfaitement horizontales : les quantités de "
                "matière n'évoluent plus, macroscopiquement."
            )
        ) as tracker:
            self.play(FadeIn(entete_graphe))
            self.play(Create(axes), FadeIn(x_label), FadeIn(y_label))
            self.play(Create(courbe_acide), Create(courbe_ester))
            self.play(FadeIn(label_acide), FadeIn(label_ester))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(entete_graphe), FadeOut(graphe))

        # --- À retenir --------------------------------------------------------------
        retenir = Text(
            _wrap(
                "L'état d'équilibre d'estérification-hydrolyse est UNIQUE "
                "pour un système donné : on l'atteint aussi bien en "
                "partant de l'acide et de l'alcool qu'en partant de "
                "l'ester et de l'eau. C'est la signature d'un véritable "
                "équilibre chimique, et non d'un simple arrêt de "
                "réaction.",
                width=48,
            ),
            font_size=23,
            color=WHITE,
        )
        retenir.next_to(titre, DOWN, buff=0.5)
        _fit(retenir, titre.get_bottom()[1] - 0.5)

        with self.voiceover(
            text=(
                "Retenons ce point essentiel : l'état d'équilibre "
                "d'estérification-hydrolyse est unique pour un système "
                "donné. On l'atteint aussi bien en partant de l'acide et "
                "de l'alcool qu'en partant directement de l'ester et de "
                "l'eau. C'est la signature d'un véritable équilibre "
                "chimique dynamique, et non d'un simple arrêt de "
                "réaction."
            )
        ) as tracker:
            self.play(FadeIn(retenir))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(retenir), FadeOut(titre))
