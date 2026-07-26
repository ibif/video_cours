"""
scenes/SVT_GametogeneseMammiferes_01.py — Chapitre 3 (1ereC, SVT), scène 01.

Introduction du chapitre « La gamétogénèse chez les mammifères » :
définition (spermatogenèse / ovogenèse), rappels ploïdie et méiose
(2n→n), vocabulaire de la lignée germinale (tableau des cellules et de
leur ploïdie à chaque étape), objectifs du chapitre.
Source : 1ereC/SVT.pdf, pages 22-23.
"""

import textwrap

from manim import (
    DOWN,
    LEFT,
    UP,
    WHITE,
    YELLOW,
    FadeIn,
    FadeOut,
    MathTex,
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


class IntroductionGametogeneseMammiferes(NotionScene):
    def construct(self):
        titre = scene_title("Chapitre 3 — La gamétogénèse chez les mammifères")
        titre.scale(0.6)
        titre.to_edge(UP)

        # --- Énoncé : définition ---------------------------------------------
        definition = definition_box(
            Text(
                _wrap(
                    "La gamétogénèse est l'ensemble des processus de "
                    "formation des gamètes, cellules reproductrices "
                    "haploïdes, à partir des cellules germinales diploïdes "
                    "des gonades. Chez le mâle : spermatogenèse, dans les "
                    "tubules séminifères des testicules. Chez la "
                    "femelle : ovogenèse, dans les follicules ovariques "
                    "des ovaires.",
                    width=54,
                ),
                font_size=23,
            ),
            box_width=12.0,
        )
        definition.next_to(titre, DOWN, buff=0.45)

        with self.voiceover(
            text=(
                "La gamétogénèse est l'ensemble des processus de formation "
                "des gamètes, ces cellules reproductrices haploïdes, à "
                "partir des cellules germinales diploïdes situées dans les "
                "gonades. Chez le mâle, ce processus porte le nom de "
                "spermatogenèse et se déroule dans les tubules séminifères "
                "des testicules. Chez la femelle, il porte le nom "
                "d'ovogenèse et se déroule dans les follicules ovariques "
                "des ovaires."
            )
        ) as tracker:
            self.play(Write(titre))
            self.play(FadeIn(definition))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(definition))

        # --- Animation du raisonnement : ploïdie et méiose ---------------------
        entete_meiose = Text("Rappel : ploïdie et méiose", font_size=27, color=YELLOW, weight="BOLD")
        entete_meiose.next_to(titre, DOWN, buff=0.5)

        rappel = _bullets(
            [
                "Cellules somatiques et germinales souches : diploïdes "
                "(2n chromosomes). Chez l'être humain : 2n=46.",
                "Gamètes : haploïdes (n chromosomes). Chez l'être "
                "humain : n=23.",
                "La méiose : 1 cellule à 2n chromosomes → 4 cellules à "
                "n chromosomes, génétiquement différentes.",
            ],
            font_size=22,
            width=50,
        )
        rappel.next_to(entete_meiose, DOWN, buff=0.35)

        cascade = MathTex(
            r"2n \xrightarrow{\text{méiose I}} n \xrightarrow{\text{méiose II}} n \ (\times 4)",
            font_size=30,
            color=YELLOW,
        )
        cascade.next_to(rappel, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Rappelons deux notions indispensables. D'une part, les "
                "cellules somatiques et les cellules germinales souches "
                "sont diploïdes, à deux n chromosomes : deux n égale "
                "quarante-six chez l'être humain. Les gamètes, eux, sont "
                "haploïdes, à n chromosomes, soit n égale vingt-trois. "
                "D'autre part, la méiose est la division qui, à partir "
                "d'une cellule à deux n chromosomes, produit quatre "
                "cellules à n chromosomes, génétiquement différentes les "
                "unes des autres : d'abord la méiose un, qui sépare les "
                "chromosomes homologues et fait passer de deux n à n, puis "
                "la méiose deux, qui sépare les chromatides sœurs. Sans "
                "cette réduction, le nombre de chromosomes doublerait à "
                "chaque génération : la gamétogénèse assure donc la "
                "constance de la formule chromosomique de l'espèce."
            )
        ) as tracker:
            self.play(FadeIn(entete_meiose))
            self.play(FadeIn(rappel))
            self.play(Write(cascade))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(entete_meiose), FadeOut(rappel), FadeOut(cascade))

        # --- Exemple traité : vocabulaire de la lignée germinale ---------------
        entete_vocab = Text("Vocabulaire de la lignée germinale", font_size=25, color=YELLOW, weight="BOLD")
        entete_vocab.next_to(titre, DOWN, buff=0.45)

        vocab = _bullets(
            [
                "Spermatogonies / ovogonies (2n) : renouvellement de la "
                "lignée par mitoses.",
                "Spermatocyte I / ovocyte I (2n, chromosomes à 2 "
                "chromatides) : entrée en méiose.",
                "Spermatocyte II / ovocyte II (n, chromosomes à 2 "
                "chromatides) : division équationnelle.",
                "Spermatides / ovotide et globules polaires (n) : "
                "différenciation en gamètes.",
                "Spermatozoïde / ovule (n) : gamètes prêts pour la "
                "fécondation.",
            ],
            font_size=20,
            width=52,
        )
        vocab.next_to(entete_vocab, DOWN, buff=0.35)

        with self.voiceover(
            text=(
                "Fixons le vocabulaire de la lignée germinale, que nous "
                "retrouverons tout au long du chapitre. Les spermatogonies, "
                "côté mâle, et les ovogonies, côté femelle, sont les "
                "cellules souches diploïdes qui renouvellent la lignée par "
                "mitoses. Le spermatocyte de premier ordre et l'ovocyte de "
                "premier ordre, encore diploïdes mais avec des chromosomes "
                "à deux chromatides, entrent en méiose. Le spermatocyte de "
                "second ordre et l'ovocyte de second ordre, désormais "
                "haploïdes, réalisent la division équationnelle. Les "
                "spermatides d'un côté, l'ovotide et les globules polaires "
                "de l'autre, se différencient ensuite en gamètes : le "
                "spermatozoïde et l'ovule, tous deux haploïdes, prêts pour "
                "la fécondation."
            )
        ) as tracker:
            self.play(FadeIn(entete_vocab))
            self.play(FadeIn(vocab))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(entete_vocab), FadeOut(vocab))

        # --- À retenir : objectifs du chapitre ----------------------------------
        entete_objectifs = Text("Objectifs du chapitre", font_size=27, color=YELLOW, weight="BOLD")
        entete_objectifs.next_to(titre, DOWN, buff=0.5)

        objectifs = _bullets(
            [
                "Définir la gamétogénèse et situer son déroulement dans "
                "les gonades.",
                "Décrire les étapes de la spermatogenèse et de "
                "l'ovogenèse à partir de coupes histologiques.",
                "Comparer les deux processus (rythme, durée, production, "
                "période d'activité).",
                "Annoter les schémas de structure des gamètes et relier "
                "chaque structure à sa fonction.",
                "Interpréter des spermogrammes et des données de "
                "fertilité pour expliquer fécondité et infécondité.",
            ],
            font_size=21,
            width=52,
        )
        objectifs.next_to(entete_objectifs, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "À l'issue de ce chapitre, l'élève doit être capable de "
                "définir la gamétogénèse et de situer son déroulement dans "
                "les gonades des mammifères ; de décrire les étapes de la "
                "spermatogenèse et de l'ovogenèse à partir de coupes "
                "histologiques de testicule et d'ovaire ; de comparer les "
                "deux processus de gamétogénèse, leur rythme, leur durée, "
                "leur production et leur période d'activité ; d'annoter les "
                "schémas de structure des gamètes, spermatozoïde et ovule, "
                "et de relier chaque structure à sa fonction ; et enfin "
                "d'interpréter des spermogrammes et des données de "
                "fertilité pour expliquer les notions de fécondité et "
                "d'infécondité."
            )
        ) as tracker:
            self.play(FadeIn(entete_objectifs))
            self.play(FadeIn(objectifs))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(entete_objectifs), FadeOut(objectifs))

        # --- Piège à éviter --------------------------------------------------
        piege = warning_box(
            Text(
                _wrap(
                    "Ne confonds pas gamétogénèse et méiose : la méiose "
                    "n'est que l'étape centrale de la gamétogénèse. La "
                    "gamétogénèse inclut aussi la multiplication par "
                    "mitoses, la croissance et la différenciation finale "
                    "en gamète (spermiogenèse ou maturation de l'ovule).",
                    width=54,
                ),
                font_size=23,
            ),
            box_width=12.0,
        )
        piege.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Attention à ne pas confondre gamétogénèse et méiose : la "
                "méiose n'est que l'étape centrale de la gamétogénèse, "
                "celle qui réduit le nombre de chromosomes. La "
                "gamétogénèse, elle, inclut aussi la multiplication par "
                "mitoses, la croissance, et la différenciation finale en "
                "gamète, c'est-à-dire la spermiogenèse chez le mâle ou la "
                "maturation de l'ovule chez la femelle."
            )
        ) as tracker:
            self.play(FadeIn(piege))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(titre), FadeOut(piege))
