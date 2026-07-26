"""
scenes/Chimie_GeneralitesComposesOrganiques_01.py — Chapitre 1 (1ereC, Chimie), scène 01.

§ 1.1-1.2 Introduction : chimie minérale vs chimie organique, la « force
vitale », la synthèse de l'urée par Wöhler (1828), définition de la chimie
organique, et les éléments présents dans les composés organiques (C, H, O,
N, et plus rarement S/P/halogènes). Source : 1ereC/Chimie.pdf, pages 4-5.
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
    Text,
    VGroup,
    Write,
    config,
)

from shapes.base_scene import NotionScene
from shapes.boxes import definition_box, scene_title, warning_box


def _wrap(text: str, width: int = 56) -> str:
    return "\n".join(textwrap.fill(line, width=width) for line in text.split("\n"))


def _bullets(items, font_size=24, color=WHITE, width=54):
    lines = VGroup(
        *[Text(f"• {_wrap(it, width=width)}", font_size=font_size, color=color) for it in items]
    )
    lines.arrange(DOWN, aligned_edge=LEFT, buff=0.22)
    return lines


def _fit(mobject, top_y):
    bas_visible = -config.frame_height / 2 + 0.25
    hauteur_dispo = top_y - bas_visible
    if mobject.height > hauteur_dispo:
        mobject.scale(hauteur_dispo / mobject.height, about_point=mobject.get_top())
    return mobject


class IntroductionChimieOrganique(NotionScene):
    def construct(self):
        titre = scene_title("1. La chimie organique et les composés organiques")
        titre.scale(0.55)
        titre.to_edge(UP)

        # --- Énoncé : chimie minérale vs organique, la « force vitale » -------
        histoire = Text(
            _wrap(
                "Longtemps, on a opposé la chimie minérale, qui étudie les "
                "corps du monde minéral, à la chimie organique, qui "
                "étudiait les substances tirées des êtres vivants. On "
                "croyait qu'une « force vitale » propre au vivant était "
                "indispensable pour fabriquer un composé organique.",
                width=56,
            ),
            font_size=24,
            color=WHITE,
        )
        histoire.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Longtemps, on a opposé la chimie minérale, qui étudie les "
                "corps tirés du monde minéral, à la chimie organique, qui "
                "étudiait les substances extraites des organismes vivants, "
                "végétaux ou animaux. On pensait même qu'une « force "
                "vitale », propre au vivant, était indispensable pour "
                "élaborer un composé organique, et qu'elle resterait à "
                "jamais inaccessible au laboratoire."
            )
        ) as tracker:
            self.play(Write(titre))
            self.play(FadeIn(histoire))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(histoire))

        # --- Animation du raisonnement : Wöhler, 1828 --------------------------
        entete = Text("1828 — la synthèse de l'urée par Wöhler", font_size=25, color=YELLOW, weight="BOLD")
        entete.next_to(titre, DOWN, buff=0.5)

        wohler = Text(
            _wrap(
                "En 1828, le chimiste allemand Friedrich Wöhler synthétise "
                "l'urée — un composé organique — à partir de réactifs "
                "purement minéraux. Aucune « force vitale » n'est "
                "intervenue : cette barrière tombe définitivement.",
                width=54,
            ),
            font_size=25,
            color=WHITE,
        )
        wohler.next_to(entete, DOWN, buff=0.5)

        schema = VGroup(
            Text("réactifs minéraux", font_size=22, color=WHITE),
            Text("→", font_size=30, color=YELLOW),
            Text("urée (composé organique)", font_size=22, color=WHITE),
        ).arrange(RIGHT, buff=0.4)
        schema.next_to(wohler, DOWN, buff=0.5)

        groupe_wohler = VGroup(entete, wohler, schema)

        with self.voiceover(
            text=(
                "En dix-huit cent vingt-huit, le chimiste allemand "
                "Friedrich Wöhler synthétisa l'urée, un composé organique, "
                "à partir de réactifs purement minéraux. Aucune force "
                "vitale n'était intervenue : cette barrière tomba "
                "définitivement, et la chimie organique put alors se "
                "définir autrement."
            )
        ) as tracker:
            self.play(FadeIn(entete))
            self.play(FadeIn(wohler))
            self.play(FadeIn(schema))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(groupe_wohler))

        # --- Exemple traité : définition de la chimie organique ---------------
        definition = definition_box(
            Text(
                _wrap(
                    "La chimie organique est la chimie des composés du "
                    "carbone, que ceux-ci existent à l'état naturel ou "
                    "qu'ils aient été synthétisés par l'homme.",
                    width=48,
                ),
                font_size=26,
            ),
        )
        definition.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "On peut désormais poser une définition précise : la "
                "chimie organique est la chimie des composés du carbone, "
                "que ceux-ci existent à l'état naturel ou qu'ils aient été "
                "synthétisés par l'homme."
            )
        ) as tracker:
            self.play(FadeIn(definition))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(definition))

        # --- À retenir : les éléments présents dans les composés organiques ---
        entete2 = Text("Les éléments des composés organiques", font_size=26, color=YELLOW, weight="BOLD")
        entete2.next_to(titre, DOWN, buff=0.4)

        elements = _bullets(
            [
                "Carbone C : toujours présent",
                "Hydrogène H : presque toujours présent — hydrocarbures "
                "CₓHᵧ (méthane, éthane, benzène…)",
                "Oxygène O : très fréquent — composés oxygénés CₓHᵧOᵤ "
                "(éthanol, glucose…)",
                "Azote N : composés azotés (acides aminés, protéines, "
                "urée CH₄N₂O…)",
                "Plus rarement : soufre S, phosphore P, halogènes "
                "(Cl, F, Br, I)",
            ],
            font_size=22,
            width=52,
        )
        elements.next_to(entete2, DOWN, buff=0.4)
        _fit(elements, entete2.get_bottom()[1] - 0.4)

        groupe_elements = VGroup(entete2, elements)

        with self.voiceover(
            text=(
                "L'analyse élémentaire montre que les composés organiques "
                "ne contiennent qu'un petit nombre d'éléments. Le carbone "
                "est toujours présent. L'hydrogène est presque toujours "
                "présent : les composés ne contenant que du carbone et de "
                "l'hydrogène, de formule générale C indice x H indice y, "
                "sont appelés hydrocarbures. L'oxygène est très fréquent : "
                "on parle alors de composés oxygénés. L'azote se retrouve "
                "dans les composés azotés, comme les acides aminés, les "
                "protéines ou l'urée. Plus rarement, on trouve aussi le "
                "soufre, le phosphore ou des halogènes."
            )
        ) as tracker:
            self.play(FadeIn(entete2))
            self.play(FadeIn(elements))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(groupe_elements))

        # --- Pièges à éviter : ce qui n'est PAS de la chimie organique --------
        piege = warning_box(
            Text(
                _wrap(
                    "On exclut du domaine de la chimie organique le "
                    "carbone lui-même, le monoxyde de carbone CO, le "
                    "dioxyde de carbone CO₂, ainsi que les carbonates et "
                    "hydrogénocarbonates (ions CO₃²⁻ et HCO₃⁻), qui "
                    "relèvent de la chimie minérale.",
                    width=48,
                ),
                font_size=25,
            ),
        )
        piege.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Attention à un piège classique : on exclut du domaine de "
                "la chimie organique le carbone lui-même, le monoxyde de "
                "carbone, le dioxyde de carbone, ainsi que les carbonates "
                "et les hydrogénocarbonates, qui relèvent en réalité de la "
                "chimie minérale, malgré la présence de l'élément carbone."
            )
        ) as tracker:
            self.play(FadeIn(piege))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(piege), FadeOut(titre))
