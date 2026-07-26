"""
scenes/SVT_MeioseChromosomes_01.py — Chapitre 2 (1ereC, SVT), scène 01.

§ Situation-problème (famille d'Abidjan, 4 enfants), constat 46 vs 23
chromosomes, définition de la méiose, double intérêt (réduction +
diversification), objectifs du chapitre.
Source : 1ereC/SVT.pdf, pages 12-13.
"""

import textwrap

from manim import (
    DOWN,
    LEFT,
    RIGHT,
    UP,
    WHITE,
    YELLOW,
    Dot,
    Ellipse,
    FadeIn,
    FadeOut,
    MathTex,
    Text,
    VGroup,
    Write,
)

from shapes.base_scene import NotionScene
from shapes.boxes import definition_box, method_box, property_box, scene_title


def _wrap(text: str, width: int = 56) -> str:
    return "\n".join(textwrap.fill(line, width=width) for line in text.split("\n"))


def _bullets(items, font_size=21, color=WHITE, width=52):
    lines = VGroup(
        *[Text(f"• {_wrap(it, width=width)}", font_size=font_size, color=color) for it in items]
    )
    lines.arrange(DOWN, aligned_edge=LEFT, buff=0.22)
    return lines


def _famille_schema():
    """4 petites cellules ovales avec des points de couleurs différentes
    pour symboliser 4 enfants ayant chacun 46 chromosomes mais des
    combinaisons différentes."""
    couleurs = [YELLOW, WHITE, YELLOW, WHITE]
    cellules = VGroup()
    for i in range(4):
        cell = Ellipse(width=1.5, height=1.9, color=WHITE, stroke_width=2)
        pts = VGroup(
            *[
                Dot(radius=0.05, color=couleurs[(i + k) % 4])
                for k in range(6)
            ]
        ).arrange_in_grid(rows=3, cols=2, buff=0.13)
        pts.move_to(cell.get_center())
        label = Text("46", font_size=16, color=YELLOW, weight="BOLD")
        label.next_to(cell, DOWN, buff=0.12)
        cellules.add(VGroup(cell, pts, label))
    cellules.arrange(RIGHT, buff=0.5)
    return cellules


class SituationProblemeEtDefinitionMeiose(NotionScene):
    def construct(self):
        titre = scene_title("Chapitre 2 — La division méiotique")
        titre.scale(0.6)
        titre.to_edge(UP)

        # --- Énoncé : situation-problème ---------------------------------------
        situation = Text(
            _wrap(
                "Dans une famille d'Abidjan, un couple a quatre enfants. "
                "Chaque enfant possède, comme ses parents, 46 chromosomes "
                "dans ses cellules ; pourtant, aucun ne ressemble "
                "exactement à ses frères et sœurs. Comment le nombre de "
                "chromosomes reste-t-il constant de génération en "
                "génération ? Pourquoi les enfants d'un même couple "
                "sont-ils tous différents ?",
                width=56,
            ),
            font_size=23,
            color=WHITE,
        )
        situation.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Dans une famille d'Abidjan, un couple a quatre enfants. "
                "Chaque enfant possède, comme ses parents, quarante-six "
                "chromosomes dans ses cellules ; pourtant, aucun ne "
                "ressemble exactement à ses frères et sœurs. Comment le "
                "nombre de chromosomes reste-t-il constant de génération en "
                "génération ? Et pourquoi les enfants d'un même couple "
                "sont-ils tous différents ? La réponse à ces deux questions "
                "tient en un mot : la méiose."
            )
        ) as tracker:
            self.play(Write(titre))
            self.play(FadeIn(situation))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(situation))

        # --- Animation du raisonnement : 4 enfants, 46 chromosomes chacun,
        # mais des combinaisons différentes -------------------------------------
        famille = _famille_schema()
        famille.next_to(titre, DOWN, buff=0.8)
        legende = Text(
            "4 enfants — 46 chromosomes chacun — 4 combinaisons différentes",
            font_size=18,
            color=WHITE,
        )
        legende.next_to(famille, DOWN, buff=0.35)

        with self.voiceover(
            text=(
                "Représentons les quatre enfants. Chacun a bien quarante-six "
                "chromosomes, comme l'indique le nombre sous chaque cellule, "
                "mais l'agencement des couleurs, qui symbolise l'origine "
                "paternelle ou maternelle des chromosomes, n'est jamais "
                "identique d'un enfant à l'autre."
            )
        ) as tracker:
            self.play(FadeIn(famille))
            self.play(FadeIn(legende))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(famille), FadeOut(legende))

        # --- Constat : 46 vs 23, fécondation ------------------------------------
        constat_titre = Text("Le constat", font_size=26, color=YELLOW, weight="BOLD")
        constat_titre.next_to(titre, DOWN, buff=0.5)

        equation = MathTex(
            r"\text{spermatozoïde } (n{=}23) \;+\; \text{ovule } (n{=}23) \;\longrightarrow\; \text{zygote } (2n{=}46)",
            font_size=26,
            color=WHITE,
        )
        equation.next_to(constat_titre, DOWN, buff=0.5)

        constat_texte = Text(
            _wrap(
                "Cellules somatiques : 46 chromosomes. Gamètes "
                "(spermatozoïdes, ovules) : 23 chromosomes seulement. Il "
                "existe donc, dans les gonades, un mécanisme de division "
                "particulier qui divise par deux le nombre de chromosomes : "
                "la méiose.",
                width=54,
            ),
            font_size=22,
            color=WHITE,
        )
        constat_texte.next_to(equation, DOWN, buff=0.45)

        with self.voiceover(
            text=(
                "Voici le constat de départ. Les cellules du corps, dites "
                "cellules somatiques, possèdent quarante-six chromosomes. Or "
                "les gamètes, spermatozoïdes et ovules, n'en possèdent que "
                "vingt-trois. Lors de la fécondation, la fusion des deux "
                "gamètes rétablit le nombre quarante-six dans la cellule "
                "œuf, ou zygote. Il existe donc, dans les gonades, "
                "testicules et ovaires, un mécanisme de division particulier "
                "qui divise par deux le nombre de chromosomes : c'est la "
                "méiose."
            )
        ) as tracker:
            self.play(FadeIn(constat_titre))
            self.play(Write(equation))
            self.play(FadeIn(constat_texte))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(constat_titre), FadeOut(equation), FadeOut(constat_texte))

        # --- Exemple traité : définition de la méiose --------------------------
        definition = definition_box(
            Text(
                _wrap(
                    "Méiose : ensemble de deux divisions cellulaires "
                    "successives, précédées d'une seule réplication de "
                    "l'ADN, qui transforme une cellule mère diploïde (2n "
                    "chromosomes) en quatre cellules filles haploïdes (n "
                    "chromosomes), génétiquement différentes de la cellule "
                    "mère et différentes entre elles. 1ère division = "
                    "réductionnelle (2n→n). 2ème division = équationnelle "
                    "(n reste n).",
                    width=54,
                ),
                font_size=21,
            ),
            box_width=12.2,
        )
        definition.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "La méiose est un ensemble de deux divisions cellulaires "
                "successives, précédées d'une seule réplication de l'ADN, "
                "qui transforme une cellule mère diploïde, à deux n "
                "chromosomes, en quatre cellules filles haploïdes, à n "
                "chromosomes, génétiquement différentes de la cellule mère "
                "et différentes entre elles. La première division est dite "
                "réductionnelle : elle réduit le nombre de chromosomes de "
                "moitié, de deux n à n. La seconde est dite équationnelle : "
                "elle conserve le nombre n."
            )
        ) as tracker:
            self.play(FadeIn(definition))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(definition))

        # --- À retenir : double intérêt de la méiose ----------------------------
        interet = property_box(
            _bullets(
                [
                    "Réduction du nombre de chromosomes : en produisant des "
                    "gamètes à n chromosomes, la méiose permet à la "
                    "fécondation de rétablir 2n. Le caryotype de l'espèce "
                    "reste stable de génération en génération.",
                    "Diversification génétique : grâce aux brassages "
                    "génétiques, les quatre cellules issues de la méiose "
                    "sont toutes différentes — source de variabilité des "
                    "individus et d'évolution des espèces.",
                ],
                font_size=21,
                width=52,
            ),
            box_width=12.2,
        )
        interet.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "La méiose présente un double intérêt. D'une part, la "
                "réduction du nombre de chromosomes : en produisant des "
                "gamètes à n chromosomes, elle permet à la fécondation de "
                "rétablir le nombre deux n ; le caryotype de l'espèce reste "
                "ainsi constant d'une génération à l'autre. D'autre part, la "
                "diversification génétique : grâce aux brassages "
                "génétiques, les quatre cellules issues de la méiose sont "
                "toutes différentes. La méiose est donc une source de "
                "diversité génétique, base de la variabilité des individus "
                "et de l'évolution des espèces."
            )
        ) as tracker:
            self.play(FadeIn(interet))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(interet))

        # --- Point clé / objectifs du chapitre ----------------------------------
        point_cle = method_box(
            Text(
                _wrap(
                    "La méiose n'a lieu que dans les gonades, au cours de "
                    "la gamétogenèse. Elle ne concerne que la lignée "
                    "germinale, jamais les cellules somatiques, qui se "
                    "divisent par mitose.",
                    width=54,
                ),
                font_size=22,
            ),
            box_width=12.0,
        )
        point_cle.next_to(titre, DOWN, buff=0.5)

        objectifs = _bullets(
            [
                "Décrire la structure d'un chromosome et interpréter un "
                "caryotype humain.",
                "Expliquer le déroulement des deux divisions de la méiose.",
                "Démontrer que les brassages sont sources de diversité "
                "génétique.",
                "Comparer méiose et mitose.",
                "Interpréter une anomalie de la méiose (trisomie 21).",
            ],
            font_size=19,
            width=52,
        )
        objectifs.next_to(point_cle, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Retenez ce point clé : la méiose n'a lieu que dans les "
                "gonades, au cours de la gamétogenèse. Elle ne concerne que "
                "la lignée germinale, jamais les cellules somatiques, qui se "
                "divisent par mitose. Ce chapitre nous permettra de décrire "
                "la structure d'un chromosome et d'interpréter un caryotype "
                "humain, d'expliquer le déroulement des deux divisions de la "
                "méiose, de démontrer que les brassages génétiques sont "
                "sources de diversité, de comparer la méiose à la mitose, et "
                "enfin d'interpréter une anomalie de la méiose, la trisomie "
                "vingt-et-un."
            )
        ) as tracker:
            self.play(FadeIn(point_cle))
            self.play(FadeIn(objectifs))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(titre), FadeOut(point_cle), FadeOut(objectifs))
