"""
scenes/SVT_TectoniquePlaques_07.py — Chapitre 8 (1ereC, SVT), scène 07.

IV. Les trois types de frontières de plaques : définition générale +
grand tableau récapitulatif (dorsale divergente / subduction convergente /
collision convergente / faille transformante). Source : 1ereC/SVT.pdf,
page 89.
"""

import textwrap

from manim import DOWN, LEFT, UP, WHITE, YELLOW, FadeIn, FadeOut, Table, Text, VGroup, Write, config

from shapes.base_scene import NotionScene
from shapes.boxes import definition_box, scene_title


def _wrap(text: str, width: int = 56) -> str:
    return "\n".join(textwrap.fill(line, width=width) for line in text.split("\n"))


class TroisTypesDeFrontieres(NotionScene):
    def construct(self):
        titre = scene_title("IV. Les trois types de frontières de plaques")
        titre.scale(0.56)
        titre.to_edge(UP)
        self.play(Write(titre))

        # --- Énoncé : définition générale ------------------------------------
        definition_frontiere = definition_box(
            Text(
                _wrap(
                    "Frontière (ou limite) de plaques : zone étroite et "
                    "active qui sépare deux plaques lithosphériques. On "
                    "distingue trois types : les frontières divergentes "
                    "(dorsales), les frontières convergentes (subduction, "
                    "collision) et les frontières transformantes (failles "
                    "transformantes).",
                    width=54,
                ),
                font_size=22,
            ),
            box_width=12.2,
        )
        definition_frontiere.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Une frontière, ou limite, de plaques est une zone étroite "
                "et active qui sépare deux plaques lithosphériques. On en "
                "distingue trois types : les frontières divergentes, au "
                "niveau des dorsales ; les frontières convergentes, "
                "subduction ou collision ; et les frontières "
                "transformantes, au niveau des failles transformantes. "
                "Détaillons chacune d'elles dans les scènes suivantes, mais "
                "commençons par une vue d'ensemble comparative."
            )
        ) as tracker:
            self.play(FadeIn(definition_frontiere))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(definition_frontiere))

        # --- Animation du raisonnement / à retenir : tableau récapitulatif ---
        entete = Text("Tableau récapitulatif des frontières", font_size=25, color=YELLOW, weight="BOLD")
        entete.next_to(titre, DOWN, buff=0.4)

        rows = [
            [
                "Dorsale\n(divergente)",
                "Écartement",
                "Ride médiane,\nvallée axiale (rift)",
                "Basaltique,\neffusif",
                "Superficielle,\nfaible à modérée",
            ],
            [
                "Subduction\n(convergente)",
                "Rapprochement",
                "Fosse océanique,\narc volcanique",
                "Andésitique,\nexplosif",
                "Superficielle à\nprofonde (≤700 km)",
            ],
            [
                "Collision\n(convergente)",
                "Rapprochement",
                "Chaîne de\nmontagnes, suture",
                "Quasi absent",
                "Superficielle,\nlarge zone",
            ],
            [
                "Faille\ntransformante",
                "Coulissage",
                "Décalage des axes\nde dorsales",
                "Absent",
                "Superficielle,\nparfois violente",
            ],
        ]
        col_labels = ["Type", "Mouvement", "Structures", "Magmatisme", "Séismicité"]

        table = Table(
            rows,
            col_labels=[Text(c, font_size=17, weight="BOLD") for c in col_labels],
            element_to_mobject=Text,
            element_to_mobject_config={"font_size": 15},
            line_config={"color": WHITE, "stroke_width": 1},
            include_outer_lines=True,
            v_buff=0.35,
            h_buff=0.35,
        )
        table.get_entries().set_color(WHITE)
        table.get_col_labels().set_color(YELLOW)
        for line in table.get_horizontal_lines():
            line.set_color(WHITE)
        for line in table.get_vertical_lines():
            line.set_color(WHITE)

        table.next_to(entete, DOWN, buff=0.3)

        # Garde-fou d'auto-scale : si le tableau (5 colonnes x 4 lignes)
        # dépasse la hauteur ou la largeur disponibles, on le réduit pour
        # qu'il tienne entièrement à l'écran (voir SVT_FonctionsGonades_09).
        _bas_visible = -config.frame_height / 2 + 0.3
        _hauteur_dispo = table.get_top()[1] - _bas_visible
        if table.height > _hauteur_dispo:
            table.scale(_hauteur_dispo / table.height, about_point=table.get_top())
        _largeur_dispo = config.frame_width - 0.6
        if table.width > _largeur_dispo:
            table.scale(_largeur_dispo / table.width, about_point=table.get_top())
        table.next_to(entete, DOWN, buff=0.3)

        with self.voiceover(
            text=(
                "Voici les quatre familles de frontières, à comparer ligne "
                "par ligne. La dorsale, frontière divergente : les plaques "
                "s'écartent, on y trouve une ride médiane avec une vallée "
                "axiale, un magmatisme basaltique effusif, et une "
                "sismicité superficielle, faible à modérée. La subduction, "
                "frontière convergente : les plaques se rapprochent, avec "
                "une fosse océanique et un arc volcanique, un magmatisme "
                "andésitique explosif, et une sismicité qui va de la "
                "surface jusqu'à sept cents kilomètres de profondeur. La "
                "collision, autre frontière convergente : toujours un "
                "rapprochement, mais avec une chaîne de montagnes et une "
                "ligne de suture, un magmatisme quasiment absent, et une "
                "sismicité superficielle répartie sur une large zone. "
                "Enfin, la faille transformante : un simple coulissage, "
                "avec un décalage des axes de dorsales, aucun magmatisme, "
                "et une sismicité superficielle, parfois très violente."
            )
        ) as tracker:
            self.play(FadeIn(entete))
            self.play(FadeIn(table))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(entete), FadeOut(table))

        # --- Piège à éviter : ne pas confondre les deux types de convergence
        piege = Text(
            _wrap(
                "À retenir avant de détailler chaque type : subduction et "
                "collision sont TOUTES DEUX des frontières convergentes, "
                "mais elles se distinguent par la nature des plaques en "
                "jeu — au moins une plaque océanique pour la subduction, "
                "deux plaques continentales pour la collision.",
                width=54,
            ),
            font_size=22,
            color=WHITE,
        )
        piege.next_to(titre, DOWN, buff=0.6)

        with self.voiceover(
            text=(
                "Avant de détailler chaque type dans les scènes suivantes, "
                "retenez ceci : subduction et collision sont toutes deux "
                "des frontières convergentes, mais elles se distinguent "
                "par la nature des plaques en présence. La subduction "
                "implique au moins une plaque océanique ; la collision "
                "concerne deux plaques continentales."
            )
        ) as tracker:
            self.play(FadeIn(piege))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(piege), FadeOut(titre))
