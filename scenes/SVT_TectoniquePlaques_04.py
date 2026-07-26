"""
scenes/SVT_TectoniquePlaques_04.py — Chapitre 8 (1ereC, SVT), scène 04.

III. Les arguments de l'expansion océanique.
§A hypothèse de Hess (1962), définitions dorsale/accrétion océanique/
expansion océanique ; §B.1-2 le paléomagnétisme (aimantation rémanente,
point de Curie) et les inversions du champ magnétique terrestre (polarité
normale/inversée, échelle de temps magnétique). Source : 1ereC/SVT.pdf,
pages 87-88.
"""

import textwrap

from manim import (
    BLUE_D,
    BLUE_E,
    DOWN,
    LEFT,
    ORANGE,
    RED,
    RIGHT,
    UP,
    WHITE,
    YELLOW,
    Arrow,
    Create,
    FadeIn,
    FadeOut,
    Polygon,
    Rectangle,
    Text,
    VGroup,
    Write,
)

from shapes.base_scene import NotionScene
from shapes.boxes import definition_box, scene_title


def _wrap(text: str, width: int = 56) -> str:
    return "\n".join(textwrap.fill(line, width=width) for line in text.split("\n"))


def _bullets(items, font_size=24, color=WHITE, width=54):
    lines = VGroup(
        *[Text(f"• {_wrap(it, width=width)}", font_size=font_size, color=color) for it in items]
    )
    lines.arrange(DOWN, aligned_edge=LEFT, buff=0.22)
    return lines


class ExpansionOceaniqueEtPaleomagnetisme(NotionScene):
    def construct(self):
        titre = scene_title("III. L'expansion océanique (Hess, 1962)")
        titre.scale(0.62)
        titre.to_edge(UP)
        self.play(Write(titre))

        # --- Énoncé : l'hypothèse de Hess -----------------------------------
        intro = Text(
            _wrap(
                "En 1962, le géologue américain Harry Hess propose que les "
                "fonds océaniques se renouvellent en permanence : le "
                "matériau du manteau remonte au niveau des dorsales, se "
                "solidifie, et forme une nouvelle croûte océanique qui "
                "s'écarte ensuite symétriquement de l'axe.",
                width=56,
            ),
            font_size=24,
            color=WHITE,
        )
        intro.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "En dix-neuf cent soixante-deux, le géologue américain "
                "Harry Hess propose que les fonds océaniques se "
                "renouvellent en permanence : le matériau du manteau "
                "remonte au niveau des dorsales, se solidifie, et forme une "
                "nouvelle croûte océanique, qui s'écarte ensuite "
                "symétriquement de part et d'autre de l'axe."
            )
        ) as tracker:
            self.play(FadeIn(intro))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(intro))

        # --- Schéma simplifié d'une dorsale ---------------------------------
        ocean = Rectangle(width=9.0, height=1.2, fill_color=BLUE_E, fill_opacity=0.5, stroke_width=0)
        flanc_g = Polygon(
            [-4.5, -0.6, 0], [-0.6, -0.6, 0], [-0.15, 0.55, 0], [-4.5, 0.15, 0],
            fill_color=ORANGE, fill_opacity=0.75, stroke_color=WHITE, stroke_width=1,
        )
        flanc_d = Polygon(
            [4.5, -0.6, 0], [0.6, -0.6, 0], [0.15, 0.55, 0], [4.5, 0.15, 0],
            fill_color=ORANGE, fill_opacity=0.75, stroke_color=WHITE, stroke_width=1,
        )
        rift = Polygon(
            [-0.6, -0.6, 0], [0.6, -0.6, 0], [0.15, 0.55, 0], [-0.15, 0.55, 0],
            fill_color=RED, fill_opacity=0.85, stroke_color=WHITE, stroke_width=1,
        )
        fleche_g = Arrow(start=[-0.5, 0.0, 0], end=[-2.2, 0.0, 0], color=WHITE, buff=0, stroke_width=3)
        fleche_d = Arrow(start=[0.5, 0.0, 0], end=[2.2, 0.0, 0], color=WHITE, buff=0, stroke_width=3)
        label_dorsale = Text("Dorsale (axe = rift)", font_size=18, color=WHITE)
        label_dorsale.next_to(rift, UP, buff=0.15)

        schema = VGroup(ocean, flanc_g, flanc_d, rift, fleche_g, fleche_d, label_dorsale)
        schema.next_to(titre, DOWN, buff=0.55)

        with self.voiceover(
            text=(
                "Voici le principe : au centre, l'axe de la dorsale, où le "
                "magma remonte et se solidifie en nouvelle croûte. De part "
                "et d'autre, cette croûte s'écarte symétriquement : c'est "
                "l'accrétion et l'expansion océaniques."
            )
        ) as tracker:
            self.play(FadeIn(ocean))
            self.play(Create(flanc_g), Create(flanc_d), Create(rift), FadeIn(label_dorsale))
            self.play(Create(fleche_g), Create(fleche_d))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(schema))

        # --- Animation du raisonnement : les 3 définitions -------------------
        d1 = definition_box(
            Text(
                _wrap(
                    "Dorsale : ride sous-marine surélevée, longue de "
                    "plusieurs milliers de km, au milieu des océans, où se "
                    "forme en permanence de la nouvelle lithosphère "
                    "océanique.",
                    width=52,
                ),
                font_size=21,
            ),
            box_width=11.5,
        )
        d1.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Trois définitions à retenir. Une dorsale est une ride "
                "sous-marine surélevée, longue de plusieurs milliers de "
                "kilomètres, située au milieu des océans, où se forme en "
                "permanence de la nouvelle lithosphère océanique."
            )
        ) as tracker:
            self.play(FadeIn(d1))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(d1))

        d2 = definition_box(
            Text(
                _wrap(
                    "Accrétion océanique : formation continue de nouvelle "
                    "croûte (lithosphère) océanique au niveau des dorsales, "
                    "à partir du magma issu du manteau.",
                    width=52,
                ),
                font_size=22,
            ),
            box_width=11.5,
        )
        d2.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "L'accrétion océanique est la formation continue de "
                "nouvelle croûte océanique au niveau des dorsales, à partir "
                "du magma issu du manteau."
            )
        ) as tracker:
            self.play(FadeIn(d2))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(d2))

        d3 = definition_box(
            Text(
                _wrap(
                    "Expansion océanique : écartement progressif des fonds "
                    "océaniques de part et d'autre des dorsales, dû à "
                    "l'accrétion océanique ; il s'accompagne de la dérive "
                    "des continents voisins.",
                    width=52,
                ),
                font_size=22,
            ),
            box_width=11.5,
        )
        d3.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Et l'expansion océanique est l'écartement progressif des "
                "fonds océaniques de part et d'autre des dorsales, dû à "
                "l'accrétion océanique ; elle s'accompagne de la dérive des "
                "continents voisins."
            )
        ) as tracker:
            self.play(FadeIn(d3))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(d3))

        # --- Exemple traité : aimantation rémanente et point de Curie -------
        entete_paleo = Text("Le paléomagnétisme", font_size=27, color=YELLOW, weight="BOLD")
        entete_paleo.next_to(titre, DOWN, buff=0.5)

        paleo = _bullets(
            [
                "Les basaltes contiennent des minéraux ferromagnétiques "
                "(magnétite). Au-dessus du point de Curie (≈580°C), ces "
                "minéraux ne sont pas aimantés.",
                "Quand la lave refroidit sous le point de Curie, les "
                "minéraux s'aimantent selon le champ magnétique terrestre "
                "du moment : la roche garde une aimantation rémanente "
                "(fossile), comme une boussole figée dans la pierre.",
            ],
            font_size=21,
            width=52,
        )
        paleo.next_to(entete_paleo, DOWN, buff=0.35)

        with self.voiceover(
            text=(
                "Comment dater et suivre cette expansion ? Grâce au "
                "paléomagnétisme. Les basaltes contiennent des minéraux "
                "ferromagnétiques, la magnétite. Au-dessus d'une "
                "température appelée point de Curie, environ cinq cent "
                "quatre-vingts degrés pour la magnétite, ces minéraux ne "
                "possèdent aucune aimantation. Mais lorsque la lave "
                "refroidit en dessous du point de Curie, les minéraux "
                "s'aimantent selon la direction du champ magnétique "
                "terrestre de l'époque : la roche conserve alors une "
                "aimantation rémanente, ou fossile, telle une boussole "
                "figée dans la pierre."
            )
        ) as tracker:
            self.play(FadeIn(entete_paleo))
            self.play(FadeIn(paleo))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(entete_paleo), FadeOut(paleo))

        # --- À retenir : les inversions du champ magnétique ------------------
        entete_inv = Text("Les inversions du champ magnétique", font_size=25, color=YELLOW, weight="BOLD")
        entete_inv.next_to(titre, DOWN, buff=0.5)

        inv = _bullets(
            [
                "Le champ magnétique terrestre s'est inversé de nombreuses "
                "fois : le pôle Nord magnétique prend la place du pôle Sud "
                "et inversement.",
                "Époque actuelle : polarité normale (Brunhes), précédée "
                "d'époques de polarité inversée (Matuyama, etc.).",
                "Toutes les roches du monde enregistrent les mêmes "
                "inversions aux mêmes dates : on dispose d'une échelle de "
                "temps magnétique datée.",
            ],
            font_size=20,
            width=52,
        )
        inv.next_to(entete_inv, DOWN, buff=0.35)

        with self.voiceover(
            text=(
                "Autre phénomène essentiel : le champ magnétique terrestre "
                "s'est inversé de nombreuses fois au cours des temps "
                "géologiques, le pôle Nord magnétique prenant alors la "
                "place du pôle Sud, et inversement. L'époque actuelle est "
                "dite de polarité normale, l'époque de Brunhes ; elle a été "
                "précédée d'époques de polarité inversée, comme celle de "
                "Matuyama. Or toutes les roches du monde enregistrent les "
                "mêmes inversions, aux mêmes dates : on dispose ainsi d'une "
                "véritable échelle de temps magnétique, datée, qui va nous "
                "servir à lire l'histoire des fonds océaniques."
            )
        ) as tracker:
            self.play(FadeIn(entete_inv))
            self.play(FadeIn(inv))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(entete_inv), FadeOut(inv), FadeOut(titre))
