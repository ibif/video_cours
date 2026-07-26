"""
scenes/SVT_ProductionMatiere_07.py — Chapitre 11 (1ereD, SVT), scène 07.

§ 11.4.1-11.4.2 Le bilan de l'assimilation chlorophyllienne : vocabulaire
(photosynthèse, autotrophie/hétérotrophie), équation bilan (MathTex),
exemple de vérification de l'équilibrage (carbone, hydrogène, oxygène).
Source : 1ereD/SVT.pdf, pages 151-152.
"""

import textwrap

from manim import DOWN, LEFT, RIGHT, UP, WHITE, YELLOW, FadeIn, FadeOut, MathTex, Text, VGroup, Write

from shapes.base_scene import NotionScene
from shapes.boxes import definition_box, example_box, scene_title, theorem_box


def _wrap(text: str, width: int = 56) -> str:
    return "\n".join(textwrap.fill(line, width=width) for line in text.split("\n"))


def _bullets(items, font_size=22, color=WHITE, width=52):
    lines = VGroup(
        *[Text(f"• {_wrap(it, width=width)}", font_size=font_size, color=color) for it in items]
    )
    lines.arrange(DOWN, aligned_edge=LEFT, buff=0.22)
    return lines


class BilanAssimilationChlorophyllienne(NotionScene):
    def construct(self):
        # --- Énoncé : vocabulaire ------------------------------------------
        titre = scene_title("11.4 — Le bilan de l'assimilation chlorophyllienne")
        titre.scale(0.48)
        titre.to_edge(UP)

        vocabulaire = definition_box(
            Text(
                _wrap(
                    "L'assimilation chlorophyllienne, ou photosynthèse, "
                    "est l'ensemble des réactions par lesquelles le "
                    "végétal vert, à la lumière, fabrique de la matière "
                    "organique à partir de matière minérale (CO2 et eau), "
                    "avec dégagement de dioxygène. Le végétal produisant "
                    "lui-même sa matière est dit autotrophe ; les animaux "
                    "et champignons, qui doivent la trouver toute faite, "
                    "sont hétérotrophes.",
                    width=54,
                ),
                font_size=20,
            ),
            box_width=11.8,
        )
        vocabulaire.next_to(titre, DOWN, buff=0.45)

        with self.voiceover(
            text=(
                "L'assimilation chlorophyllienne, appelée aussi "
                "photosynthèse, est l'ensemble des réactions par "
                "lesquelles le végétal vert, à la lumière, fabrique de la "
                "matière organique à partir de matière minérale, dioxyde "
                "de carbone et eau, avec dégagement de dioxygène. Grâce à "
                "ce mécanisme, le végétal vert produit lui-même sa "
                "matière : on dit qu'il est autotrophe, du grec autos, "
                "soi-même, et trophê, nourriture. Les animaux et les "
                "champignons, qui doivent trouver leur matière organique "
                "toute faite dans leur nourriture, sont hétérotrophes."
            )
        ) as tracker:
            self.play(Write(titre))
            self.play(FadeIn(vocabulaire))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(vocabulaire))

        # --- Animation du raisonnement : construire l'équation bilan --------------
        with self.voiceover(
            text=(
                "En additionnant tout ce qui entre et tout ce qui sort, on "
                "obtient l'équation bilan complète : six molécules de "
                "dioxyde de carbone plus douze molécules d'eau donnent une "
                "molécule de glucose, six molécules de dioxygène, et six "
                "molécules d'eau, en présence de lumière et de "
                "chlorophylle."
            )
        ) as tracker:
            equation_complete = MathTex(
                r"6\,CO_2 + 12\,H_2O \longrightarrow C_6H_{12}O_6 + 6\,O_2 + 6\,H_2O",
                font_size=32,
                color=WHITE,
            )
            equation_complete.next_to(titre, DOWN, buff=0.7)
            self.play(Write(equation_complete))
            self.wait(tracker.get_remaining_duration())

        with self.voiceover(
            text=(
                "On la simplifie souvent ainsi : six molécules de dioxyde "
                "de carbone et six molécules d'eau donnent une molécule de "
                "glucose et six molécules de dioxygène."
            )
        ) as tracker:
            equation_simple = MathTex(
                r"6\,CO_2 + 6\,H_2O \longrightarrow C_6H_{12}O_6 + 6\,O_2",
                font_size=34,
                color=YELLOW,
            )
            equation_simple.next_to(equation_complete, DOWN, buff=0.5)
            self.play(Write(equation_simple))
            self.wait(tracker.get_remaining_duration())

        legende = Text(
            "en présence de lumière et de chlorophylle",
            font_size=18,
            color=WHITE,
        )
        legende.next_to(equation_simple, DOWN, buff=0.3)

        with self.voiceover(
            text=(
                "Lisons-la mot à mot : six molécules de dioxyde de carbone "
                "et six molécules d'eau donnent une molécule de glucose et "
                "six molécules de dioxygène, en présence de lumière et de "
                "chlorophylle. Le glucose est la première matière "
                "organique fabriquée ; il sert ensuite de brique de départ "
                "à toutes les autres, amidon, cellulose, lipides, "
                "protides."
            )
        ) as tracker:
            self.play(FadeIn(legende))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(equation_complete), FadeOut(equation_simple), FadeOut(legende))

        # --- Exemple traité : équation bilan en boîte théorème --------------------
        theoreme = theorem_box(
            MathTex(
                r"6\,CO_2 + 6\,H_2O \longrightarrow C_6H_{12}O_6 + 6\,O_2",
                font_size=32,
            ),
            box_width=10.5,
        )
        theoreme.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Voici donc l'équation bilan de l'assimilation "
                "chlorophyllienne, à retenir par cœur pour le "
                "baccalauréat."
            )
        ) as tracker:
            self.play(FadeIn(theoreme))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(theoreme))

        # --- À retenir : vérification de l'équilibrage (entièrement résolue) ------
        exemple = example_box(
            _bullets(
                [
                    "Carbone : gauche 6×1=6 ; droite, le glucose en "
                    "contient 6. Équilibré.",
                    "Hydrogène : gauche 6×2=12 ; droite, le glucose en "
                    "contient 12. Équilibré.",
                    "Oxygène : gauche 6×2+6×1=18 ; droite, 6 (glucose) + "
                    "6×2=12 (O2) = 18. Équilibré.",
                    "Les trois éléments sont conservés : l'équation est "
                    "correctement équilibrée.",
                ],
                font_size=19,
                width=56,
            ),
            box_width=12.0,
        )
        exemple.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Vérifions que cette équation conserve chaque élément. "
                "Carbone : à gauche, six fois un, soit six atomes ; à "
                "droite, le glucose en contient six. Équilibré. "
                "Hydrogène : à gauche, six fois deux, soit douze atomes ; "
                "à droite, le glucose en contient douze. Équilibré. "
                "Oxygène : à gauche, six fois deux plus six fois un, soit "
                "douze plus six, dix-huit atomes ; à droite, six dans le "
                "glucose et six fois deux, soit douze, dans le dioxygène, "
                "soit six plus douze, dix-huit. Équilibré. Les trois "
                "éléments sont conservés : l'équation est correctement "
                "équilibrée."
            )
        ) as tracker:
            self.play(FadeIn(exemple))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(titre), FadeOut(exemple))
