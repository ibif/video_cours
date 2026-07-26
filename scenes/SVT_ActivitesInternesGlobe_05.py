"""
scenes/SVT_ActivitesInternesGlobe_05.py — Chapitre 6 (1ereD, SVT), scène 05.

§ 6.2.3 Magnitude et intensité : deux mesures à ne pas confondre + piège
du journal télévisé + application directe : se protéger des séismes
(Accra, 1939). Source : 1ereD/SVT.pdf, page 79.
"""

import textwrap

from manim import (
    DOWN,
    GREEN,
    LEFT,
    ORANGE,
    RED,
    RIGHT,
    UP,
    WHITE,
    YELLOW,
    Circle,
    Dot,
    FadeIn,
    FadeOut,
    Text,
    VGroup,
    Write,
)

from shapes.base_scene import NotionScene
from shapes.boxes import definition_box, scene_title, warning_box


def _wrap(text: str, width: int = 56) -> str:
    return "\n".join(textwrap.fill(line, width=width) for line in text.split("\n"))


def _bullets(items, font_size=23, color=WHITE, width=52):
    lines = VGroup(
        *[Text(f"• {_wrap(it, width=width)}", font_size=font_size, color=color) for it in items]
    )
    lines.arrange(DOWN, aligned_edge=LEFT, buff=0.22)
    return lines


class MagnitudeEtIntensite(NotionScene):
    def construct(self):
        titre = scene_title("6.2.3 — Magnitude et intensité")
        titre.scale(0.72)
        titre.to_edge(UP)

        # --- Énoncé : deux mesures différentes -------------------------------
        definition = definition_box(
            Text(
                _wrap(
                    "La magnitude mesure l'énergie libérée au foyer (échelle "
                    "ouverte de Richter, chaque degré ≈ 30 fois plus "
                    "d'énergie ; un séisme n'a qu'une seule magnitude). "
                    "L'intensité mesure les effets/dégâts en un lieu donné "
                    "(échelle MSK de I à XII ; un même séisme a des "
                    "intensités différentes selon la distance).",
                    width=54,
                ),
                font_size=21,
            ),
            box_width=11.9,
        )
        definition.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Deux mesures d'un séisme sont à ne jamais confondre. La "
                "magnitude mesure l'énergie libérée au foyer, sur l'échelle "
                "ouverte de Richter : chaque degré supplémentaire "
                "correspond à environ trente fois plus d'énergie libérée. "
                "Un séisme donné n'a qu'une seule magnitude, où que l'on se "
                "trouve. L'intensité, elle, mesure les effets et les dégâts "
                "en un lieu précis, sur l'échelle MSK, graduée de un à "
                "douze en chiffres romains : un même séisme a des "
                "intensités différentes selon l'endroit où on l'observe."
            )
        ) as tracker:
            self.play(Write(titre))
            self.play(FadeIn(definition))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(definition))

        # --- Animation du raisonnement : une magnitude, plusieurs intensités --
        epicentre = Dot(point=(0, 0.3, 0), color=RED, radius=0.1)
        zones = VGroup(
            Circle(radius=0.5, color=RED, fill_color=RED, fill_opacity=0.5),
            Circle(radius=1.1, color=ORANGE, fill_color=ORANGE, fill_opacity=0.35),
            Circle(radius=1.7, color=YELLOW, fill_color=YELLOW, fill_opacity=0.25),
            Circle(radius=2.3, color=GREEN, fill_color=GREEN, fill_opacity=0.15),
        )
        for z in zones:
            z.move_to(epicentre.get_center())
        schema = VGroup(*zones, epicentre)
        schema.move_to(LEFT * 3.0 + DOWN * 0.2)

        label_epicentre = Text("Épicentre", font_size=16, color=WHITE)
        label_epicentre.next_to(epicentre, UP, buff=0.15)

        etiquette_ix = Text("Intensité IX", font_size=15, color=WHITE)
        etiquette_ix.move_to(zones[0].get_center())
        etiquette_vi = Text("Intensité VI", font_size=15, color=WHITE).move_to(zones[1].point_at_angle(0.8))
        etiquette_iii = Text("Intensité III", font_size=15, color=WHITE).move_to(zones[2].point_at_angle(2.3))

        magnitude_label = Text("Magnitude unique : 6,5\n(quelle que soit la distance)", font_size=17, color=YELLOW)
        magnitude_label.next_to(schema, RIGHT, buff=1.0)

        with self.voiceover(
            text=(
                "Imaginons un séisme de magnitude six virgule cinq. Cette "
                "magnitude est unique, elle ne change pas, quelle que soit "
                "la distance à laquelle on se place. Mais l'intensité "
                "ressentie diminue au fur et à mesure qu'on s'éloigne de "
                "l'épicentre : intensité neuf tout près, avec des "
                "bâtiments effondrés ; intensité six un peu plus loin, avec "
                "des fissures ; intensité trois encore plus loin, à peine "
                "perceptible."
            )
        ) as tracker:
            self.play(FadeIn(schema), FadeIn(label_epicentre))
            self.play(FadeIn(etiquette_ix))
            self.play(FadeIn(etiquette_vi))
            self.play(FadeIn(etiquette_iii))
            self.play(FadeIn(magnitude_label))
            self.wait(tracker.get_remaining_duration())

        self.play(
            FadeOut(schema), FadeOut(label_epicentre), FadeOut(etiquette_ix),
            FadeOut(etiquette_vi), FadeOut(etiquette_iii), FadeOut(magnitude_label),
        )

        # --- Exemple traité : le piège du journal télévisé -------------------
        piege_jt = warning_box(
            Text(
                _wrap(
                    "Un séisme de magnitude 6 très profond ou en zone "
                    "déserte peut ne faire aucun dégât ; un séisme de "
                    "magnitude 5,5 sous une ville mal construite peut être "
                    "catastrophique. Ne jamais confondre énergie "
                    "(magnitude) et effets (intensité).",
                    width=54,
                ),
                font_size=22,
            ),
            box_width=12.0,
        )
        piege_jt.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Voici le piège du journal télévisé. Un séisme de magnitude "
                "six, s'il est très profond ou situé en zone déserte, peut "
                "ne faire aucun dégât. À l'inverse, un séisme de magnitude "
                "cinq virgule cinq seulement, s'il survient sous une ville "
                "mal construite, peut être catastrophique. Ne confondez "
                "donc jamais l'énergie libérée, la magnitude, avec les "
                "effets observés, l'intensité : les journaux, eux, "
                "confondent souvent les deux."
            )
        ) as tracker:
            self.play(FadeIn(piege_jt))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(piege_jt))

        # --- À retenir : application directe, se protéger des séismes -------
        protection = _bullets(
            [
                "Construire des bâtiments parasismiques.",
                "Fixer les meubles hauts et les objets lourds.",
                "Consigne : s'abriter sous une table solide, s'écarter des façades et des vitres.",
            ],
            width=50,
        )
        entete_protection = Text("Se protéger des séismes", font_size=26, color=YELLOW, weight="BOLD")
        entete_protection.next_to(titre, DOWN, buff=0.5)
        protection.next_to(entete_protection, DOWN, buff=0.4)

        accra_note = Text(
            _wrap(
                "Accra (Ghana), voisine de la Côte d'Ivoire, a été détruite "
                "en partie par un séisme en 1939 : la sous-région n'est pas "
                "totalement à l'abri.",
                width=52,
            ),
            font_size=20,
            color=WHITE,
        )
        accra_note.next_to(protection, DOWN, buff=0.35)

        with self.voiceover(
            text=(
                "Pour se protéger des séismes : construire des bâtiments "
                "parasismiques, capables d'absorber les secousses ; fixer "
                "les meubles hauts et les objets lourds qui pourraient "
                "tomber ; et connaître la consigne de sécurité, s'abriter "
                "sous une table solide et s'écarter des façades et des "
                "vitres. Rappelons qu'Accra, capitale du Ghana, voisine de "
                "la Côte d'Ivoire, a été détruite en partie par un séisme "
                "en mille neuf cent trente-neuf : la sous-région "
                "ouest-africaine n'est donc pas totalement à l'abri."
            )
        ) as tracker:
            self.play(FadeIn(entete_protection))
            self.play(FadeIn(protection))
            self.play(FadeIn(accra_note))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(entete_protection), FadeOut(protection), FadeOut(accra_note))
        self.play(FadeOut(titre))
