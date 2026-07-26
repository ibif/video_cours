"""
scenes/SVT_Gametogenese_02.py — Chapitre 3 (1ereD, SVT), scène 02.

§ 3.1 Rappels : reproduction sexuée, gamètes, cellule œuf ; cellules
diploïdes/haploïdes (2n/n) ; conservation du nombre de chromosomes ;
exemple du maïs (2n=20) ; attention aux deux confusions 2n/n.
Source : 1ereD/SVT.pdf, pages 31-32.
"""

import textwrap

from manim import (
    DOWN,
    LEFT,
    RIGHT,
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
from shapes.boxes import definition_box, example_box, property_box, scene_title, warning_box


def _wrap(text: str, width: int = 56) -> str:
    return "\n".join(textwrap.fill(line, width=width) for line in text.split("\n"))


def _bullets(items, font_size=23, color=WHITE, width=52):
    lines = VGroup(
        *[Text(f"• {_wrap(it, width=width)}", font_size=font_size, color=color) for it in items]
    )
    lines.arrange(DOWN, aligned_edge=LEFT, buff=0.22)
    return lines


class RappelsReproductionEtChromosomes(NotionScene):
    def construct(self):
        titre = scene_title("3.1 — Rappels : reproduction, gamètes, chromosomes")
        titre.scale(0.62)
        titre.to_edge(UP)

        # --- Énoncé : la reproduction sexuée -------------------------------
        definition = definition_box(
            Text(
                _wrap(
                    "Un gamète est une cellule reproductrice spécialisée "
                    "dans la fécondation : le spermatozoïde (gamète mâle, "
                    "produit par les testicules) et l'ovule (gamète "
                    "femelle, produit par les ovaires). La fécondation, "
                    "union d'un spermatozoïde et d'un ovule, donne une "
                    "cellule œuf, première cellule du nouvel individu.",
                    width=54,
                ),
                font_size=23,
            ),
            box_width=12.0,
        )
        definition.next_to(titre, DOWN, buff=0.45)

        with self.voiceover(
            text=(
                "La plupart des êtres vivants supérieurs, dont l'être "
                "humain, se reproduisent par reproduction sexuée, un mode de "
                "reproduction qui fait intervenir deux individus de sexe "
                "différent et deux cellules spécialisées appelées gamètes. "
                "Un gamète est une cellule reproductrice spécialisée dans la "
                "fécondation : le gamète mâle, le spermatozoïde, produit par "
                "les testicules, et le gamète femelle, l'ovule, produit par "
                "les ovaires. La fécondation est l'union d'un spermatozoïde "
                "et d'un ovule ; elle donne une cellule unique appelée "
                "cellule œuf, ou zygote, première cellule du nouvel "
                "individu."
            )
        ) as tracker:
            self.play(Write(titre))
            self.play(FadeIn(definition))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(definition))

        enchainement = MathTex(
            r"\text{gamète mâle} + \text{gamète femelle} \xrightarrow{\text{fécondation}} "
            r"\text{cellule œuf} \xrightarrow{\text{mitoses}} \text{nouvel individu}",
            font_size=26,
            color=YELLOW,
        )
        enchainement.set(width=min(enchainement.width, 11.5))
        enchainement.next_to(titre, DOWN, buff=0.7)

        with self.voiceover(
            text=(
                "Retenons l'enchaînement fondamental : gamète mâle plus "
                "gamète femelle, par fécondation, donnent une cellule œuf, "
                "qui, par divisions répétées, des mitoses, donne un "
                "embryon, puis un fœtus, puis un enfant."
            )
        ) as tracker:
            self.play(Write(enchainement))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(enchainement))

        # --- Raisonnement : diploïde / haploïde ----------------------------
        entete_dh = Text("Cellules diploïdes et haploïdes", font_size=27, color=YELLOW, weight="BOLD")
        entete_dh.next_to(titre, DOWN, buff=0.5)

        diploide = VGroup(
            Text("Cellule diploïde", font_size=24, color=WHITE, weight="BOLD"),
            MathTex(r"2n = 46 \text{ chez l'être humain}", font_size=28, color=WHITE),
            Text("(chromosomes par paires)", font_size=20, color=WHITE),
        ).arrange(DOWN, buff=0.2)

        haploide = VGroup(
            Text("Cellule haploïde", font_size=24, color=WHITE, weight="BOLD"),
            MathTex(r"n = 23 \text{ chez l'être humain}", font_size=28, color=WHITE),
            Text("(un seul chromosome par paire)", font_size=20, color=WHITE),
        ).arrange(DOWN, buff=0.2)

        deux_blocs = VGroup(diploide, haploide).arrange(RIGHT, buff=1.4)
        deux_blocs.next_to(entete_dh, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Dans le noyau de chaque cellule humaine se trouvent "
                "quarante-six chromosomes, groupés en vingt-trois paires : "
                "dans chaque paire, l'un vient du père, l'autre de la mère, "
                "ce sont des chromosomes homologues. Une cellule est dite "
                "diploïde lorsqu'elle possède les chromosomes par paires : "
                "on note sa formule chromosomique deux n, soit "
                "quarante-six chez l'être humain. Une cellule est dite "
                "haploïde lorsqu'elle ne possède qu'un seul chromosome de "
                "chaque paire : on note sa formule n, soit vingt-trois chez "
                "l'être humain."
            )
        ) as tracker:
            self.play(FadeIn(entete_dh))
            self.play(FadeIn(diploide))
            self.play(FadeIn(haploide))
            self.wait(tracker.get_remaining_duration())

        remarque = Text(
            _wrap(
                "Toutes les cellules du corps (cellules somatiques) sont "
                "diploïdes ; seuls les gamètes sont haploïdes. Lors de la "
                "fécondation, n+n=2n : 23+23=46, ce qui rétablit la "
                "diploïdie dans la cellule œuf.",
                width=52,
            ),
            font_size=22,
            color=WHITE,
        )
        remarque.next_to(deux_blocs, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Toutes les cellules du corps, cellules de la peau, des "
                "muscles, du sang, sont diploïdes : on les appelle cellules "
                "somatiques. En revanche, les gamètes sont haploïdes. Cette "
                "particularité est indispensable : lors de la fécondation, "
                "le noyau du spermatozoïde, n égale vingt-trois, fusionne "
                "avec le noyau de l'ovule, n égale vingt-trois, ce qui "
                "rétablit le nombre diploïde dans la cellule œuf : n plus n "
                "égale deux n, soit vingt-trois plus vingt-trois égale "
                "quarante-six."
            )
        ) as tracker:
            self.play(FadeIn(remarque))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(entete_dh), FadeOut(deux_blocs), FadeOut(remarque))

        # --- Propriété : conservation du nombre de chromosomes -------------
        propriete = property_box(
            Text(
                _wrap(
                    "Au cours des générations, le nombre de chromosomes "
                    "caractéristique de l'espèce est conservé : la "
                    "formation des gamètes le divise par deux (2n→n), puis "
                    "la fécondation le double à nouveau (n+n=2n).",
                    width=54,
                ),
                font_size=24,
            ),
            box_width=11.8,
        )
        propriete.next_to(titre, DOWN, buff=0.5)

        cycle = MathTex(
            r"2n \;\xrightarrow{\text{gamétogénèse}}\; n \;\xrightarrow{\text{fécondation}}\; 2n",
            font_size=28,
            color=YELLOW,
        )
        cycle.next_to(propriete, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Au cours des générations, le nombre de chromosomes "
                "caractéristique de l'espèce est conservé, parce que la "
                "formation des gamètes divise ce nombre par deux, deux n "
                "devient n, puis la fécondation le double à nouveau, n plus "
                "n redonne deux n."
            )
        ) as tracker:
            self.play(FadeIn(propriete))
            self.play(Write(cycle))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(propriete), FadeOut(cycle))

        # --- Exemple traité : le maïs ---------------------------------------
        exemple = example_box(
            Text(
                _wrap(
                    "Le maïs, cultivé dans le nord de la Côte d'Ivoire, "
                    "possède 2n=20 chromosomes. 1) Ses gamètes sont "
                    "haploïdes : n=20/2=10. 2) La fécondation réunit deux "
                    "gamètes : n+n=10+10=20. La cellule œuf, puis le plant "
                    "qui en dérive, possèdent bien 2n=20 chromosomes, comme "
                    "leurs parents.",
                    width=54,
                ),
                font_size=23,
            ),
            box_width=12.0,
        )
        exemple.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Le maïs, céréale largement cultivée dans le nord de la "
                "Côte d'Ivoire, possède deux n égale vingt chromosomes dans "
                "ses cellules somatiques. Cherchons la formule "
                "chromosomique de ses gamètes et de sa cellule œuf. "
                "Premièrement, les gamètes sont haploïdes : n égale vingt "
                "divisé par deux, soit dix ; le maïs produit donc des "
                "gamètes à dix chromosomes. Deuxièmement, la fécondation "
                "réunit deux gamètes : dix plus dix égale vingt. La "
                "cellule œuf, puis le plant qui en dérive, possèdent bien "
                "deux n égale vingt chromosomes, comme leurs parents. Le "
                "nombre de chromosomes de l'espèce maïs est ainsi maintenu "
                "de génération en génération."
            )
        ) as tracker:
            self.play(FadeIn(exemple))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(exemple))

        # --- Piège à éviter : confusions 2n / n -----------------------------
        piege = warning_box(
            Text(
                _wrap(
                    "Ne confonds pas 2n et n : 2n désigne le stock complet "
                    "par paires (cellules du corps), n désigne un seul "
                    "exemplaire de chaque paire (gamètes) — écrire que le "
                    "spermatozoïde a 2n=46 chromosomes est une erreur "
                    "grave. Et n varie selon l'espèce : n=23 chez l'être "
                    "humain, n=10 chez le maïs, ce n'est pas un nombre "
                    "universel.",
                    width=54,
                ),
                font_size=22,
            ),
            box_width=12.0,
        )
        piege.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Deux confusions fréquentes à éviter. D'abord, ne confonds "
                "pas deux n et n : deux n désigne le stock complet par "
                "paires, dans les cellules du corps, tandis que n désigne "
                "un seul exemplaire de chaque paire, dans les gamètes ; "
                "écrire que le spermatozoïde possède deux n égale "
                "quarante-six chromosomes est une erreur grave. Ensuite, le "
                "nombre n varie d'une espèce à l'autre : vingt-trois chez "
                "l'être humain, dix chez le maïs. Ce n'est pas un nombre "
                "universel."
            )
        ) as tracker:
            self.play(FadeIn(piege))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(titre), FadeOut(piege))
