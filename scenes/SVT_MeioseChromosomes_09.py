"""
scenes/SVT_MeioseChromosomes_09.py — Chapitre 2 (1ereC, SVT), scène 09.

§ Anomalies de la méiose : non-disjonction chromosomique (mécanisme,
gamètes à n+1/n-1), trisomie 21 (définition, caryotype 47,XX,+21,
caractéristiques, risque lié à l'âge maternel, dépistage par
amniocentèse) + Exemple résolu 3 (non-disjonction paire 21, ovules à
24/22 chromosomes, zygotes trisomiques/monosomiques après fécondation).
Source : 1ereC/SVT.pdf, pages 19-20.
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
    Rectangle,
    Text,
    VGroup,
    Write,
)

from shapes.base_scene import NotionScene
from shapes.boxes import definition_box, example_box, scene_title, warning_box

PATERNEL = "#B5651D"
MATERNEL = "#2E8B57"


def _wrap(text: str, width: int = 56) -> str:
    return "\n".join(textwrap.fill(line, width=width) for line in text.split("\n"))


def _bullets(items, font_size=21, color=WHITE, width=52):
    lines = VGroup(
        *[Text(f"• {_wrap(it, width=width)}", font_size=font_size, color=color) for it in items]
    )
    lines.arrange(DOWN, aligned_edge=LEFT, buff=0.22)
    return lines


def _chr_double(color, height=0.7, width=0.14, gap=0.05):
    left = Rectangle(width=width, height=height, fill_color=color, fill_opacity=1, stroke_color=WHITE, stroke_width=1)
    right = left.copy()
    paire = VGroup(left, right).arrange(RIGHT, buff=gap)
    dot = Dot(radius=0.04, color=YELLOW)
    dot.move_to(paire.get_center())
    return VGroup(left, right, dot)


class AnomaliesDeLaMeioseTrisomie21(NotionScene):
    def construct(self):
        titre = scene_title("2.7 — Les anomalies de la méiose")
        titre.scale(0.62)
        titre.to_edge(UP)

        # --- Énoncé : la non-disjonction chromosomique --------------------------
        definition = definition_box(
            Text(
                _wrap(
                    "Non-disjonction : accident où un couple de chromosomes "
                    "homologues ne se sépare pas en anaphase I (ou deux "
                    "chromatides sœurs ne se séparent pas en anaphase II). "
                    "Les deux homologues migrent alors vers le même pôle.",
                    width=54,
                ),
                font_size=21,
            ),
            box_width=11.8,
        )
        definition.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Il arrive qu'un couple de chromosomes homologues ne se "
                "sépare pas en anaphase I, ou que deux chromatides sœurs ne "
                "se séparent pas en anaphase II : c'est une non-disjonction. "
                "Les deux homologues migrent alors vers le même pôle, au "
                "lieu de se répartir normalement."
            )
        ) as tracker:
            self.play(Write(titre))
            self.play(FadeIn(definition))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(definition))

        # --- Animation du raisonnement : schéma non-disjonction ------------------
        cell_h = Ellipse(width=2.6, height=1.7, color=WHITE, stroke_width=2)
        cell_b = Ellipse(width=2.6, height=1.7, color=WHITE, stroke_width=2)
        VGroup(cell_h, cell_b).arrange(DOWN, buff=0.4).next_to(titre, DOWN, buff=0.7)

        paire_haut = VGroup(_chr_double(PATERNEL), _chr_double(MATERNEL)).arrange(RIGHT, buff=0.08)
        paire_haut.move_to(cell_h.get_center())

        label_normal = Text("Normal : 1 homologue par pôle → gamètes à n", font_size=15, color=WHITE)
        label_normal.next_to(cell_h, RIGHT, buff=0.4)

        with self.voiceover(
            text=(
                "Normalement, chaque pôle reçoit un seul chromosome de "
                "chaque paire d'homologues : les gamètes obtenus ont bien n "
                "chromosomes."
            )
        ) as tracker:
            self.play(FadeIn(cell_h), FadeIn(paire_haut), FadeIn(label_normal))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(label_normal))

        paire_bas = VGroup(_chr_double(PATERNEL), _chr_double(PATERNEL)).arrange(RIGHT, buff=0.08)
        paire_bas.move_to(cell_b.get_center())
        label_anormal = Text("Non-disjonction : les 2 homologues migrent\nensemble → gamètes à n+1 et n−1", font_size=15, color=YELLOW)
        label_anormal.next_to(cell_b, RIGHT, buff=0.4)

        with self.voiceover(
            text=(
                "Lors d'une non-disjonction, au contraire, les deux "
                "homologues migrent ensemble vers le même pôle. Cela "
                "produit des gamètes anormaux à n plus un chromosome, un "
                "chromosome en double, et d'autres à n moins un chromosome, "
                "un chromosome manquant."
            )
        ) as tracker:
            self.play(FadeIn(cell_b), FadeIn(paire_bas), FadeIn(label_anormal))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(cell_h), FadeOut(cell_b), FadeOut(paire_haut), FadeOut(paire_bas), FadeOut(label_anormal))

        # --- Exemple traité : la trisomie 21 --------------------------------------
        trisomie_def = definition_box(
            Text(
                _wrap(
                    "Trisomie 21 : anomalie chromosomique caractérisée par "
                    "la présence de trois chromosomes 21 au lieu de deux. "
                    "Caryotype : 47,XX,+21 (fille) ou 47,XY,+21 (garçon). "
                    "Résulte le plus souvent d'une non-disjonction de la "
                    "paire 21, généralement chez la mère.",
                    width=54,
                ),
                font_size=20,
            ),
            box_width=12.0,
        )
        trisomie_def.next_to(titre, DOWN, buff=0.5)

        equation = MathTex(
            r"\text{gamète anormal } (24) \;+\; \text{gamète normal } (23) \;\longrightarrow\; \text{zygote } (47, +21)",
            font_size=22,
            color=WHITE,
        )
        equation.next_to(trisomie_def, DOWN, buff=0.35)

        with self.voiceover(
            text=(
                "La trisomie vingt-et-un est une anomalie chromosomique "
                "caractérisée par la présence de trois chromosomes "
                "vingt-et-un au lieu de deux. Le caryotype s'écrit "
                "quarante-sept, X X, plus vingt-et-un, pour une fille, ou "
                "quarante-sept, X Y, plus vingt-et-un, pour un garçon. Si un "
                "gamète à n plus un égale vingt-quatre chromosomes, porteur "
                "de deux exemplaires du chromosome vingt-et-un, fusionne "
                "avec un gamète normal à vingt-trois chromosomes, le zygote "
                "possède quarante-sept chromosomes, dont trois chromosomes "
                "vingt-et-un. Elle résulte le plus souvent d'une "
                "non-disjonction de la paire vingt-et-un au cours de la "
                "méiose, généralement chez la mère."
            )
        ) as tracker:
            self.play(FadeIn(trisomie_def))
            self.play(Write(equation))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(trisomie_def), FadeOut(equation))

        # Caractéristiques + dépistage
        caracteristiques = _bullets(
            [
                "Traits caractéristiques : yeux bridés, visage rond, "
                "retard mental variable, parfois malformations (cœur, "
                "appareil digestif).",
                "Risque lié à l'âge maternel : faible avant 30 ans, "
                "nettement plus élevé après 38 ans.",
                "Dépistage prénatal : caryotype sur cellules fœtales "
                "prélevées par amniocentèse (liquide amniotique) ou sur "
                "le placenta.",
            ],
            font_size=19,
            width=54,
        )
        caracteristiques.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Les personnes trisomiques présentent des traits du visage "
                "caractéristiques, des yeux bridés, un visage rond, un "
                "retard mental plus ou moins marqué, et parfois des "
                "malformations, du cœur ou de l'appareil digestif. Le risque "
                "d'avoir un enfant trisomique augmente avec l'âge de la "
                "mère : il est faible avant trente ans, et nettement plus "
                "élevé après trente-huit ans. Le dépistage peut se faire "
                "avant la naissance, par un caryotype réalisé sur des "
                "cellules fœtales prélevées dans le liquide amniotique, "
                "c'est l'amniocentèse, ou sur le placenta."
            )
        ) as tracker:
            self.play(FadeIn(caracteristiques))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(caracteristiques))

        # --- À retenir : Exemple résolu 3 (ovules 24/22, zygotes) --------------
        exemple = example_box(
            Text(
                _wrap(
                    "Exemple résolu 3 : non-disjonction de la paire 21 en "
                    "anaphase I chez une femme. Ovules produits : certains à "
                    "n+1=24 chromosomes (2 chromosomes 21), d'autres à "
                    "n-1=22 chromosomes (aucun chromosome 21). Après "
                    "fécondation par un spermatozoïde normal (n=23) : "
                    "ovule 24 + spz 23 → zygote 47 (trisomie 21) ; "
                    "ovule 22 + spz 23 → zygote 45 (monosomie 21, non "
                    "viable, fausse couche précoce).",
                    width=54,
                ),
                font_size=19,
            ),
            box_width=12.4,
        )
        exemple.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Reprenons un exemple résolu complet. Une non-disjonction "
                "de la paire de chromosomes vingt-et-un se produit en "
                "anaphase I chez une femme. La paire vingt-et-un ne se "
                "sépare pas : certains ovules reçoivent alors deux "
                "chromosomes vingt-et-un, soit n plus un égale vingt-quatre "
                "chromosomes ; d'autres n'en reçoivent aucun, soit n moins "
                "un égale vingt-deux chromosomes. Après fécondation par un "
                "spermatozoïde normal à vingt-trois chromosomes : un ovule à "
                "vingt-quatre chromosomes donne un zygote à quarante-sept "
                "chromosomes, en trisomie vingt-et-un ; un ovule à "
                "vingt-deux chromosomes donne un zygote à quarante-cinq "
                "chromosomes, en monosomie vingt-et-un, non viable, "
                "aboutissant à une fausse couche précoce."
            )
        ) as tracker:
            self.play(FadeIn(exemple))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(exemple))

        # --- Piège à éviter : pas une mutation ------------------------------------
        piege = warning_box(
            Text(
                _wrap(
                    "Ne confonds pas la trisomie 21 avec une mutation : "
                    "aucun gène n'est modifié, c'est un accident de "
                    "RÉPARTITION des chromosomes (un chromosome entier en "
                    "trop), pas un changement de l'ADN lui-même.",
                    width=54,
                ),
                font_size=21,
            ),
            box_width=12.0,
        )
        piege.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Attention à ne pas confondre la trisomie vingt-et-un avec "
                "une mutation : aucun gène n'est modifié, c'est un accident "
                "de répartition des chromosomes, un chromosome entier en "
                "trop, et non un changement de l'ADN lui-même."
            )
        ) as tracker:
            self.play(FadeIn(piege))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(titre), FadeOut(piege))
