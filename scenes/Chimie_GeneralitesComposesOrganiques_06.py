"""
scenes/Chimie_GeneralitesComposesOrganiques_06.py — Chapitre 1 (1ereC, Chimie), scène 06.

§ 3.3, 3.4 Pourcentage massique d'oxygène par différence + détermination de
la formule brute (définition, relation fondamentale) + mesure de M par
densité de vapeur. Source : 1ereC/Chimie.pdf, pages 7-8.
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
from shapes.boxes import definition_box, property_box, scene_title


def _wrap(text: str, width: int = 56) -> str:
    return "\n".join(textwrap.fill(line, width=width) for line in text.split("\n"))


def _fit(mobject, top_y):
    bas_visible = -config.frame_height / 2 + 0.25
    hauteur_dispo = top_y - bas_visible
    if mobject.height > hauteur_dispo:
        mobject.scale(hauteur_dispo / mobject.height, about_point=mobject.get_top())
    return mobject


class OxygeneEtFormuleBrute(NotionScene):
    def construct(self):
        titre = scene_title("3.3-3.4 — Oxygène par différence et formule brute")
        titre.scale(0.52)
        titre.to_edge(UP)

        # --- Énoncé : pourcentage d'oxygène par différence ----------------------
        propriete_o = property_box(
            VGroup(
                Text(
                    _wrap(
                        "L'oxygène n'étant pas dosé directement, son "
                        "pourcentage s'obtient par différence :",
                        width=46,
                    ),
                    font_size=24,
                ),
                MathTex(r"\%O = 100 - \%C - \%H \; (- \%N \text{ si azoté})", font_size=28),
            ).arrange(DOWN, buff=0.35),
        )
        propriete_o.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "L'oxygène n'étant pas dosé directement, son pourcentage "
                "s'obtient par différence : cent moins le pourcentage de "
                "carbone, moins le pourcentage d'hydrogène, moins "
                "éventuellement le pourcentage d'azote si le composé en "
                "contient. Dans notre exemple précédent, cent moins "
                "soixante moins dix donne trente pour cent : le composé A "
                "est donc un composé oxygéné."
            )
        ) as tracker:
            self.play(Write(titre))
            self.play(FadeIn(propriete_o))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(propriete_o))

        # --- Animation du raisonnement : définition de la formule brute --------
        definition = definition_box(
            Text(
                _wrap(
                    "La formule brute d'un composé indique la nature et le "
                    "nombre des atomes qui constituent la molécule "
                    "(exemple : C₂H₆O).",
                    width=48,
                ),
                font_size=26,
            ),
        )
        definition.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Il nous reste à déterminer la formule brute du composé. "
                "La formule brute d'un composé indique la nature et le "
                "nombre des atomes qui constituent la molécule, comme "
                "C deux H six O pour l'éthanol."
            )
        ) as tracker:
            self.play(FadeIn(definition))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(definition))

        # --- Exemple traité : la relation fondamentale --------------------------
        entete = Text("La relation fondamentale", font_size=25, color=YELLOW, weight="BOLD")
        entete.next_to(titre, DOWN, buff=0.4)

        explication = Text(
            _wrap(
                "Pour un composé de formule CₓHᵧOᵤNₜ et de masse molaire "
                "M : dans une mole, la masse de carbone 12x représente "
                "%C de M ; de même pour y, 16z et 14t.",
                width=52,
            ),
            font_size=21,
        )
        explication.next_to(entete, DOWN, buff=0.35)

        relation = MathTex(
            r"\dfrac{12x}{\%C} = \dfrac{y}{\%H} = \dfrac{16z}{\%O} = \dfrac{14t}{\%N} = \dfrac{M}{100}",
            font_size=34,
        )
        relation.next_to(explication, DOWN, buff=0.45)

        groupe_relation = VGroup(entete, explication, relation)
        _fit(groupe_relation, titre.get_bottom()[1] - 0.4)

        with self.voiceover(
            text=(
                "Soit un composé de formule brute C indice x, H indice y, "
                "O indice z, N indice t, de masse molaire M connue. Dans "
                "une mole de composé, la masse de carbone, douze x, "
                "représente le pourcentage de carbone de la masse molaire "
                "M ; de même pour l'hydrogène, l'oxygène et l'azote. On "
                "obtient ainsi la relation fondamentale : douze x sur "
                "pourcentage de carbone, égale y sur pourcentage "
                "d'hydrogène, égale seize z sur pourcentage d'oxygène, "
                "égale quatorze t sur pourcentage d'azote, égale M sur "
                "cent."
            )
        ) as tracker:
            self.play(FadeIn(entete))
            self.play(FadeIn(explication))
            self.play(Write(relation))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(groupe_relation))

        # --- À retenir : densité de vapeur pour mesurer M -----------------------
        propriete_m = property_box(
            VGroup(
                Text(
                    _wrap(
                        "Si le composé est volatil, on détermine M à "
                        "partir de sa densité de vapeur d par rapport à "
                        "l'air :",
                        width=46,
                    ),
                    font_size=24,
                ),
                MathTex(r"d = \dfrac{M}{29} \iff M = 29\,d \quad (M \text{ en } g/mol)", font_size=30),
            ).arrange(DOWN, buff=0.35),
        )
        propriete_m.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Enfin, si le composé est volatil, on détermine sa masse "
                "molaire M à partir de sa densité de vapeur d par rapport "
                "à l'air, grâce à la relation M égale vingt-neuf d, avec M "
                "exprimée en gramme par mole."
            )
        ) as tracker:
            self.play(FadeIn(propriete_m))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(propriete_m), FadeOut(titre))
