"""
scenes/SVT_TectoniquePlaques_11.py — Chapitre 8 (1ereC, SVT), scène 11.

IV.C Les frontières transformantes — les failles transformantes
(définition, coulissage horizontal sans création ni destruction de
lithosphère, décalage des axes de dorsale, séismes superficiels parfois
violents, pas de volcanisme, exemples faille Romanche golfe de Guinée,
faille San Andreas) + schéma récapitulatif des 3 types de frontières côte
à côte. Source : 1ereC/SVT.pdf, page 91-92.
"""

import textwrap

from manim import (
    BLUE_E,
    DOWN,
    LEFT,
    ORANGE,
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


class FrontieresTransformantes(NotionScene):
    def construct(self):
        titre = scene_title("IV.C Les frontières transformantes")
        titre.scale(0.6)
        titre.to_edge(UP)
        self.play(Write(titre))

        # --- Énoncé : définition -------------------------------------------------
        d_faille = definition_box(
            Text(
                _wrap(
                    "Faille transformante : faille verticale le long de "
                    "laquelle deux plaques coulissent horizontalement l'une "
                    "contre l'autre, sans création ni destruction de "
                    "lithosphère.",
                    width=52,
                ),
                font_size=23,
            ),
            box_width=11.5,
        )
        d_faille.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Une faille transformante est une faille verticale le long "
                "de laquelle deux plaques coulissent horizontalement l'une "
                "contre l'autre, sans création ni destruction de "
                "lithosphère : ni accrétion, ni subduction."
            )
        ) as tracker:
            self.play(FadeIn(d_faille))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(d_faille))

        # --- Animation du raisonnement : schéma vue en plan ----------------------
        bloc_a = Rectangle(width=3.0, height=1.5, fill_color=BLUE_E, fill_opacity=0.6, stroke_color=WHITE, stroke_width=1)
        bloc_a.move_to([-2.0, 0.75, 0])
        bloc_b = Rectangle(width=3.0, height=1.5, fill_color=BLUE_E, fill_opacity=0.6, stroke_color=WHITE, stroke_width=1)
        bloc_b.move_to([2.0, -0.75, 0])
        faille_ligne = Rectangle(width=6.0, height=0.05, fill_color=YELLOW, fill_opacity=1, stroke_width=0)
        faille_ligne.move_to([0, 0, 0])

        label_a = Text("Plaque A", font_size=16, color=WHITE).move_to(bloc_a.get_center())
        label_b = Text("Plaque B", font_size=16, color=WHITE).move_to(bloc_b.get_center())

        fleche_a = Arrow(start=[-3.2, 0.9, 0], end=[-1.2, 0.9, 0], color=WHITE, buff=0, stroke_width=3)
        fleche_b = Arrow(start=[3.2, -0.9, 0], end=[1.2, -0.9, 0], color=WHITE, buff=0, stroke_width=3)

        zone_active = Rectangle(width=1.0, height=0.3, fill_color=ORANGE, fill_opacity=0.8, stroke_width=0)
        zone_active.move_to([0, 0, 0])
        label_zone = Text("zone active (sismique)", font_size=13, color=ORANGE).next_to(zone_active, UP, buff=0.15)

        schema = VGroup(bloc_a, bloc_b, faille_ligne, label_a, label_b, fleche_a, fleche_b, zone_active, label_zone)
        schema.next_to(titre, DOWN, buff=0.55)

        with self.voiceover(
            text=(
                "Le mouvement est un simple coulissage horizontal. Les "
                "failles transformantes décalent souvent les axes des "
                "dorsales en segments : la zone active, sismique, se situe "
                "précisément entre les deux segments de dorsale. On observe "
                "des séismes superficiels, parfois violents, mais aucun "
                "volcanisme, puisqu'il n'y a ni écartement ni compression "
                "qui produirait du magma."
            )
        ) as tracker:
            self.play(FadeIn(bloc_a), FadeIn(bloc_b), FadeIn(label_a), FadeIn(label_b))
            self.play(Create(faille_ligne))
            self.play(Create(fleche_a), Create(fleche_b))
            self.play(FadeIn(zone_active), FadeIn(label_zone))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(schema))

        # --- Exemple traité : Romanche et San Andreas -----------------------------
        exemples = _bullets(
            [
                "Failles transformantes atlantiques, dont la faille "
                "Romanche, dans le golfe de Guinée, qui décale la dorsale "
                "médio-atlantique de plus de 600 km.",
                "Faille San Andreas, en Californie, entre les plaques "
                "pacifique et nord-américaine.",
            ],
            font_size=22,
            width=52,
        )
        exemples.next_to(titre, DOWN, buff=0.55)

        with self.voiceover(
            text=(
                "Deux exemples à connaître : les failles transformantes "
                "atlantiques, dont la faille Romanche, dans le golfe de "
                "Guinée, non loin de la Côte d'Ivoire, qui décale la "
                "dorsale médio-atlantique de plus de six cents kilomètres ; "
                "et la célèbre faille San Andreas, en Californie, entre les "
                "plaques pacifique et nord-américaine."
            )
        ) as tracker:
            self.play(FadeIn(exemples))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(exemples))

        # --- À retenir : schéma récapitulatif des 3 types côte à côte -----------
        entete_recap = Text("Les trois types de frontières, côte à côte", font_size=22, color=YELLOW, weight="BOLD")
        entete_recap.next_to(titre, DOWN, buff=0.4)

        # Mini-schéma A : dorsale (divergence)
        mini_ocean_a = Rectangle(width=2.4, height=0.9, fill_color=BLUE_E, fill_opacity=0.5, stroke_width=0)
        mini_flanc_ga = Polygon([-1.2, -0.45, 0], [-0.15, -0.45, 0], [-0.05, 0.3, 0], [-1.2, 0.05, 0], fill_color=ORANGE, fill_opacity=0.8, stroke_width=0.5, stroke_color=WHITE)
        mini_flanc_da = Polygon([1.2, -0.45, 0], [0.15, -0.45, 0], [0.05, 0.3, 0], [1.2, 0.05, 0], fill_color=ORANGE, fill_opacity=0.8, stroke_width=0.5, stroke_color=WHITE)
        mini_fa = Arrow(start=[-0.1, 0, 0], end=[-0.9, 0, 0], color=WHITE, buff=0, stroke_width=2)
        mini_fb = Arrow(start=[0.1, 0, 0], end=[0.9, 0, 0], color=WHITE, buff=0, stroke_width=2)
        mini_A = VGroup(mini_ocean_a, mini_flanc_ga, mini_flanc_da, mini_fa, mini_fb)
        label_A = Text("A. Dorsale (divergence)", font_size=16, color=WHITE)
        bloc_A = VGroup(mini_A, label_A).arrange(DOWN, buff=0.2)

        # Mini-schéma B : subduction (convergence)
        mini_cont_b = Polygon([0.2, -0.6, 0], [1.4, -0.6, 0], [1.4, 0.5, 0], [0.2, 0.5, 0], fill_color=ORANGE, fill_opacity=0.7, stroke_width=0.5, stroke_color=WHITE)
        mini_ocean_b = Polygon([-1.4, 0.2, 0], [0.1, 0.2, 0], [0.2, -0.2, 0], [-0.6, -1.2, 0], [-1.4, -0.9, 0], fill_color=BLUE_E, fill_opacity=0.8, stroke_width=0.5, stroke_color=WHITE)
        mini_volc_b = Polygon([0.5, 0.5, 0], [0.75, 1.0, 0], [1.0, 0.5, 0], fill_color=ORANGE, fill_opacity=0.9, stroke_width=0.5, stroke_color=WHITE)
        mini_fleche_b = Arrow(start=[-1.0, -0.1, 0], end=[-0.4, -0.7, 0], color=WHITE, buff=0, stroke_width=2)
        mini_B = VGroup(mini_ocean_b, mini_cont_b, mini_volc_b, mini_fleche_b)
        label_B = Text("B. Subduction (convergence)", font_size=16, color=WHITE)
        bloc_B = VGroup(mini_B, label_B).arrange(DOWN, buff=0.2)

        # Mini-schéma C : faille transformante (coulissage)
        mini_a_c = Rectangle(width=1.4, height=0.8, fill_color=BLUE_E, fill_opacity=0.6, stroke_color=WHITE, stroke_width=0.5)
        mini_a_c.move_to([-0.5, 0.4, 0])
        mini_b_c = Rectangle(width=1.4, height=0.8, fill_color=BLUE_E, fill_opacity=0.6, stroke_color=WHITE, stroke_width=0.5)
        mini_b_c.move_to([0.5, -0.4, 0])
        mini_faille_c = Rectangle(width=2.8, height=0.03, fill_color=YELLOW, fill_opacity=1, stroke_width=0)
        mini_fc1 = Arrow(start=[-1.5, 0.6, 0], end=[-0.7, 0.6, 0], color=WHITE, buff=0, stroke_width=2)
        mini_fc2 = Arrow(start=[1.5, -0.6, 0], end=[0.7, -0.6, 0], color=WHITE, buff=0, stroke_width=2)
        mini_C = VGroup(mini_a_c, mini_b_c, mini_faille_c, mini_fc1, mini_fc2)
        label_C = Text("C. Faille transformante\n(coulissage)", font_size=16, color=WHITE)
        bloc_C = VGroup(mini_C, label_C).arrange(DOWN, buff=0.2)

        trois_schemas = VGroup(bloc_A, bloc_B, bloc_C).arrange(RIGHT, buff=0.8, aligned_edge=UP)
        trois_schemas.next_to(entete_recap, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Pour conclure cette étude des trois types de frontières, "
                "voici une vue d'ensemble comparative. En A, la dorsale, "
                "avec ses deux flancs qui s'écartent. En B, la subduction, "
                "avec sa plaque océanique qui plonge sous un continent et "
                "son volcanisme. En C, la faille transformante, avec ses "
                "deux blocs qui coulissent horizontalement, sans "
                "écartement ni rapprochement."
            )
        ) as tracker:
            self.play(FadeIn(entete_recap))
            self.play(FadeIn(bloc_A))
            self.play(FadeIn(bloc_B))
            self.play(FadeIn(bloc_C))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(entete_recap), FadeOut(trois_schemas), FadeOut(titre))
