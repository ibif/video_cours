"""
scenes/SVT_Photosynthese_01.py — Chapitre 10 (1ereC, SVT), scène 01.

§ 10.0-10.1 Introduction du chapitre « La photosynthèse » : constat du
maïs de Bouaké (croissance en matière organique carbonée à partir d'eau et
de sels minéraux), définition de la photosynthèse, définition de
l'autotrophie/hétérotrophie, objectifs pédagogiques du chapitre, piège
introductif (confondre matière minérale absorbée et matière organique
fabriquée).
Source : 1ereC/SVT.pdf, pages 106-107.
"""

import textwrap

from manim import DOWN, LEFT, UP, WHITE, YELLOW, FadeIn, FadeOut, Text, VGroup, Write

from shapes.base_scene import NotionScene
from shapes.boxes import definition_box, essentiel_box, scene_title, warning_box


def _wrap(text: str, width: int = 56) -> str:
    return "\n".join(textwrap.fill(line, width=width) for line in text.split("\n"))


def _bullets(items, font_size=22, color=WHITE, width=52):
    lines = VGroup(
        *[Text(f"• {_wrap(it, width=width)}", font_size=font_size, color=color) for it in items]
    )
    lines.arrange(DOWN, aligned_edge=LEFT, buff=0.22)
    return lines


class IntroductionPhotosynthese(NotionScene):
    def construct(self):
        titre = scene_title("Chapitre 10 — La photosynthèse")
        titre.scale(0.62)
        titre.to_edge(UP)

        # --- Énoncé : le constat du maïs de Bouaké --------------------------
        sous_titre = Text("Le constat du maïs de Bouaké", font_size=27, color=YELLOW, weight="BOLD")
        sous_titre.next_to(titre, DOWN, buff=0.5)

        constat = Text(
            _wrap(
                "Un plant de maïs cultivé près de Bouaké passe en quelques "
                "semaines de quelques grammes à plusieurs kilogrammes. "
                "Or il ne prélève dans le sol que de l'eau et des sels "
                "minéraux : des substances sans carbone. D'où vient alors "
                "l'énorme quantité de matière organique carbonée qu'il "
                "fabrique ?",
                width=56,
            ),
            font_size=24,
            color=WHITE,
        )
        constat.next_to(sous_titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Un plant de maïs cultivé près de Bouaké peut passer, en "
                "quelques semaines, de quelques grammes à plusieurs "
                "kilogrammes. Or il ne prélève dans le sol que de l'eau et "
                "des sels minéraux, des substances qui ne contiennent pas "
                "de carbone. D'où provient alors l'énorme quantité de "
                "matière organique — glucides, lipides, protéines — "
                "faite de carbone, qu'il fabrique ?"
            )
        ) as tracker:
            self.play(Write(titre))
            self.play(FadeIn(sous_titre))
            self.play(FadeIn(constat))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(sous_titre), FadeOut(constat))

        # --- Animation du raisonnement : définition de la photosynthèse -----
        definition = definition_box(
            Text(
                _wrap(
                    "La photosynthèse est l'ensemble des réactions par "
                    "lesquelles les végétaux chlorophylliens (plantes "
                    "vertes, algues) fabriquent de la matière organique "
                    "(essentiellement du glucose) à partir de matière "
                    "minérale (dioxyde de carbone et eau), en utilisant "
                    "l'énergie lumineuse captée par la chlorophylle, avec "
                    "dégagement de dioxygène.",
                    width=54,
                ),
                font_size=21,
            ),
            box_width=12.0,
        )
        definition.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "L'expérience montre que les végétaux chlorophylliens, "
                "c'est-à-dire ceux qui possèdent de la chlorophylle, "
                "puisent le carbone dans le dioxyde de carbone de l'air, "
                "grâce à l'énergie de la lumière : c'est la photosynthèse. "
                "Définition : la photosynthèse est l'ensemble des "
                "réactions par lesquelles les végétaux chlorophylliens "
                "fabriquent de la matière organique, essentiellement du "
                "glucose, à partir de matière minérale — dioxyde de "
                "carbone et eau — en utilisant l'énergie lumineuse captée "
                "par la chlorophylle, avec dégagement de dioxygène."
            )
        ) as tracker:
            self.play(FadeIn(definition))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(definition))

        # --- Exemple traité : autotrophie / hétérotrophie --------------------
        autotrophie = definition_box(
            Text(
                _wrap(
                    "Autotrophie (grec autos : soi-même ; trophé : "
                    "nourriture) : un organisme autotrophe fabrique "
                    "lui-même sa matière organique à partir de matière "
                    "minérale. Les végétaux chlorophylliens sont "
                    "autotrophes. Les animaux et les champignons sont "
                    "hétérotrophes : ils doivent consommer de la matière "
                    "organique déjà fabriquée.",
                    width=54,
                ),
                font_size=21,
            ),
            box_width=12.0,
        )
        autotrophie.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Cette capacité définit une notion importante : "
                "l'autotrophie. Un organisme est dit autotrophe — du grec "
                "autos, soi-même, et trophé, nourriture — lorsqu'il "
                "fabrique lui-même sa matière organique à partir de "
                "matière minérale. Les végétaux chlorophylliens sont donc "
                "autotrophes. À l'inverse, les animaux et les champignons "
                "sont hétérotrophes : ils doivent consommer de la matière "
                "organique déjà fabriquée par d'autres êtres vivants."
            )
        ) as tracker:
            self.play(FadeIn(autotrophie))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(autotrophie))

        # --- À retenir : objectifs du chapitre --------------------------------
        objectifs = essentiel_box(
            _bullets(
                [
                    "Définir la photosynthèse et écrire son équation "
                    "bilan équilibrée.",
                    "Localiser la photosynthèse et décrire le "
                    "chloroplaste et ses pigments.",
                    "Expliquer la phase photochimique (photolyse, ATP, "
                    "NADPH,H+) et la phase biochimique (cycle de Calvin).",
                    "Interpréter des expériences avec témoin (O2 dégagé, "
                    "test à l'eau iodée).",
                    "Analyser l'influence de la lumière, du CO2 et de la "
                    "température sur l'intensité photosynthétique.",
                    "Expliquer le rôle de la photosynthèse dans la "
                    "production de matière et l'équilibre du monde vivant.",
                ],
                font_size=18,
                width=54,
            ),
            box_width=12.6,
        )
        objectifs.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "À l'issue de ce chapitre, vous devez être capable de : "
                "définir la photosynthèse et écrire son équation bilan "
                "équilibrée ; localiser la photosynthèse dans la cellule "
                "et décrire la structure du chloroplaste ainsi que le "
                "rôle des pigments chlorophylliens ; expliquer les "
                "mécanismes de la phase photochimique — photolyse de "
                "l'eau, production d'ATP et de NADPH,H plus — et de la "
                "phase biochimique, le cycle de Calvin ; interpréter des "
                "expériences de mise en évidence comportant des témoins ; "
                "déterminer l'influence de la lumière, du dioxyde de "
                "carbone et de la température sur l'intensité "
                "photosynthétique ; et enfin expliquer le rôle "
                "fondamental de la photosynthèse dans la production de la "
                "matière organique et dans l'équilibre du monde vivant."
            )
        ) as tracker:
            self.play(FadeIn(objectifs))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(objectifs))

        # --- Piège à éviter : matière minérale absorbée ≠ matière fabriquée --
        piege = warning_box(
            Text(
                _wrap(
                    "Piège à éviter : ne pas croire que la matière "
                    "organique du maïs provient directement du sol. Les "
                    "racines n'absorbent que de l'eau et des sels "
                    "minéraux (matière minérale, sans carbone) : tout le "
                    "carbone organique du végétal vient du CO2 de l'air, "
                    "capté par les feuilles grâce à l'énergie lumineuse.",
                    width=54,
                ),
                font_size=21,
            ),
            box_width=12.0,
        )
        piege.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Attention à un piège fréquent : il ne faut pas croire "
                "que la matière organique du maïs provient directement du "
                "sol. Les racines n'absorbent que de l'eau et des sels "
                "minéraux, une matière minérale sans carbone. Tout le "
                "carbone organique du végétal provient en réalité du "
                "dioxyde de carbone de l'air, capté par les feuilles "
                "grâce à l'énergie lumineuse : c'est tout l'objet de ce "
                "chapitre."
            )
        ) as tracker:
            self.play(FadeIn(piege))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(titre), FadeOut(piege))
