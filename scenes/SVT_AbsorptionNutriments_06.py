"""
scenes/SVT_AbsorptionNutriments_06.py — Chapitre 13 (1ereD, SVT), scène 06.

§ 13.3.1 Les mécanismes de l'absorption — les transports passifs :
définition de la diffusion, et trois exemples (diffusion simple des acides
gras/glycérol, diffusion facilitée du fructose, osmose de l'eau).
Source : 1ereD/SVT.pdf, pages 172-173.
"""

import textwrap

from manim import (
    DOWN,
    LEFT,
    RIGHT,
    UP,
    WHITE,
    YELLOW,
    BLUE,
    GREEN,
    ORANGE,
    Arrow,
    FadeIn,
    FadeOut,
    Rectangle,
    Text,
    VGroup,
    Write,
)

from shapes.base_scene import NotionScene
from shapes.boxes import definition_box, example_box, scene_title, warning_box


def _wrap(text: str, width: int = 56) -> str:
    return "\n".join(textwrap.fill(line, width=width) for line in text.split("\n"))


def _bullets(items, font_size=23, color=WHITE, width=52):
    lines = VGroup(
        *[Text(f"• {_wrap(it, width=width)}", font_size=font_size, color=color) for it in items]
    )
    lines.arrange(DOWN, aligned_edge=LEFT, buff=0.24)
    return lines


class TransportsPassifs(NotionScene):
    def construct(self):
        titre = scene_title("13.3 — Les mécanismes de l'absorption")
        titre.scale(0.6)
        titre.to_edge(UP)

        # --- Énoncé : deux grands types de mécanismes -------------------------
        intro = Text(
            _wrap(
                "Comment les nutriments traversent-ils la membrane des "
                "entérocytes ? Deux grands types de mécanismes coexistent "
                ": les transports passifs, qui ne demandent aucune "
                "énergie, et le transport actif, qui en consomme.",
                width=56,
            ),
            font_size=24,
            color=WHITE,
        )
        intro.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Comment les nutriments traversent-ils la membrane des "
                "entérocytes ? Deux grands types de mécanismes coexistent "
                ": les transports passifs, qui ne demandent aucune "
                "énergie, et le transport actif, qui en consomme. "
                "Intéressons-nous d'abord aux transports passifs."
            )
        ) as tracker:
            self.play(Write(titre))
            self.play(FadeIn(intro))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(intro))

        definition = definition_box(
            Text(
                _wrap(
                    "La diffusion est le déplacement d'une substance du "
                    "milieu où elle est la plus concentrée vers le milieu "
                    "où elle est la moins concentrée. C'est un phénomène "
                    "passif : il ne nécessite aucune dépense d'énergie de "
                    "la part de la cellule.",
                    width=54,
                ),
                font_size=22,
            ),
            box_width=11.9,
        )
        definition.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "La diffusion est le déplacement d'une substance du "
                "milieu où elle est la plus concentrée vers le milieu où "
                "elle est la moins concentrée. C'est un phénomène passif : "
                "il ne nécessite aucune dépense d'énergie de la part de la "
                "cellule."
            )
        ) as tracker:
            self.play(FadeIn(definition))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(definition))

        # --- Animation du raisonnement : schéma du gradient de concentration -
        membrane = Rectangle(width=0.35, height=2.6, color=WHITE, fill_color=WHITE, fill_opacity=0.5, stroke_width=2)

        zone_riche = Rectangle(width=2.6, height=2.6, color=ORANGE, fill_color=ORANGE, fill_opacity=0.3, stroke_width=2)
        zone_riche.next_to(membrane, LEFT, buff=0)
        riche_label = Text("milieu riche\n(lumière intestinale)", font_size=15, color=ORANGE, line_spacing=0.8)
        riche_label.next_to(zone_riche, UP, buff=0.15)

        zone_pauvre = Rectangle(width=2.6, height=2.6, color=BLUE, fill_color=BLUE, fill_opacity=0.15, stroke_width=2)
        zone_pauvre.next_to(membrane, RIGHT, buff=0)
        pauvre_label = Text("milieu pauvre\n(entérocyte)", font_size=15, color=BLUE, line_spacing=0.8)
        pauvre_label.next_to(zone_pauvre, UP, buff=0.15)

        fleche = Arrow(
            zone_riche.get_center(), zone_pauvre.get_center(),
            buff=1.0, color=YELLOW, stroke_width=6,
        )
        fleche_label = Text("sens de la diffusion", font_size=16, color=YELLOW)
        fleche_label.next_to(VGroup(zone_riche, membrane, zone_pauvre), DOWN, buff=0.3)

        schema = VGroup(zone_riche, membrane, zone_pauvre, riche_label, pauvre_label, fleche, fleche_label)
        schema.scale(0.85)
        schema.next_to(titre, DOWN, buff=0.6)

        with self.voiceover(
            text=(
                "Voici le principe : d'un côté de la membrane, un milieu "
                "riche en une substance — ici, la lumière intestinale ; de "
                "l'autre côté, un milieu pauvre en cette même substance — "
                "l'entérocyte. Sans aucune dépense d'énergie, la substance "
                "se déplace spontanément du milieu riche vers le milieu "
                "pauvre : c'est le sens de la diffusion, celui du gradient "
                "de concentration."
            )
        ) as tracker:
            self.play(FadeIn(schema))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(schema))

        # --- Exemple traité : trois exemples de transports passifs ------------
        exemple = example_box(
            _bullets(
                [
                    "Diffusion simple : acides gras et glycérol, solubles dans les graisses, traversent directement la membrane lipidique.",
                    "Diffusion facilitée : le fructose emprunte un transporteur membranaire, sans dépense d'énergie, dans le sens du gradient.",
                    "Osmose : l'eau suit passivement les solutés absorbés, du milieu le moins concentré vers le plus concentré en solutés.",
                ],
                font_size=19,
                width=54,
            ),
            box_width=12.2,
        )
        exemple.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Trois exemples illustrent les transports passifs. La "
                "diffusion simple concerne les substances qui traversent "
                "directement la membrane lipidique : c'est le cas des "
                "acides gras et du glycérol, molécules solubles dans les "
                "graisses, qui pénètrent ainsi dans l'entérocyte. La "
                "diffusion facilitée concerne des substances qui "
                "empruntent un canal ou un transporteur membranaire sans "
                "dépense d'énergie, toujours dans le sens du gradient de "
                "concentration : le fructose, le sucre des fruits, est "
                "absorbé de cette manière. Enfin, l'eau est absorbée par "
                "osmose : elle suit passivement les solutés — sels, "
                "nutriments — dont l'absorption élève la concentration en "
                "solutés à l'intérieur des cellules et du sang ; l'eau "
                "passe ainsi du milieu le moins concentré vers le milieu "
                "le plus concentré en solutés."
            )
        ) as tracker:
            self.play(FadeIn(exemple))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(exemple))

        # --- À retenir ------------------------------------------------------------
        a_retenir = _bullets(
            [
                "Transports passifs = aucune dépense d'énergie de la cellule.",
                "La diffusion (simple ou facilitée) descend toujours le gradient de concentration.",
                "L'eau suit les solutés par osmose.",
            ],
            font_size=22,
            width=52,
        )
        entete_retenir = Text("À retenir", font_size=26, color=YELLOW, weight="BOLD")
        entete_retenir.next_to(titre, DOWN, buff=0.55)
        a_retenir.next_to(entete_retenir, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "À retenir : les transports passifs ne demandent aucune "
                "dépense d'énergie de la part de la cellule ; la "
                "diffusion, simple ou facilitée, descend toujours le "
                "gradient de concentration, du milieu riche vers le milieu "
                "pauvre ; et l'eau suit les solutés par osmose."
            )
        ) as tracker:
            self.play(FadeIn(entete_retenir))
            self.play(FadeIn(a_retenir))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(entete_retenir), FadeOut(a_retenir))

        # --- Piège à éviter : diffusion facilitée n'est pas transport actif ----
        piege = warning_box(
            Text(
                _wrap(
                    "La diffusion facilitée utilise un transporteur "
                    "membranaire, mais elle reste un transport PASSIF : "
                    "aucune énergie n'est dépensée, et le sens du "
                    "déplacement suit toujours le gradient de "
                    "concentration. Ne pas la confondre avec le transport "
                    "actif (scène suivante), qui lui exige de l'ATP.",
                    width=54,
                ),
                font_size=21,
            ),
            box_width=12.0,
        )
        piege.next_to(titre, DOWN, buff=0.55)

        with self.voiceover(
            text=(
                "Attention à un piège fréquent : la diffusion facilitée "
                "utilise un transporteur membranaire, mais elle reste un "
                "transport passif. Aucune énergie n'est dépensée, et le "
                "sens du déplacement suit toujours le gradient de "
                "concentration. Ne la confonds pas avec le transport "
                "actif, que nous étudierons maintenant, et qui lui exige "
                "de l'ATP."
            )
        ) as tracker:
            self.play(FadeIn(piege))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(titre), FadeOut(piege))
