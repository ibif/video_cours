"""
scenes/SVT_MeioseChromosomes_02.py — Chapitre 2 (1ereC, SVT), scène 02.

§ Rappels sur les chromosomes : structure (chromatide, centromère, formes à
1 ou 2 chromatides), règle d'or (compter les centromères), chromosomes
homologues, caryotype humain (2n=46), diploïde / haploïde.
Source : 1ereC/SVT.pdf, pages 13-14.
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
    FadeIn,
    FadeOut,
    MathTex,
    Rectangle,
    Text,
    VGroup,
    Write,
)

from shapes.base_scene import NotionScene
from shapes.boxes import definition_box, example_box, method_box, scene_title

PATERNEL = "#B5651D"   # rouille — origine paternelle (cohérent tout le chapitre)
MATERNEL = "#2E8B57"   # vert — origine maternelle (cohérent tout le chapitre)


def _wrap(text: str, width: int = 56) -> str:
    return "\n".join(textwrap.fill(line, width=width) for line in text.split("\n"))


def _bullets(items, font_size=21, color=WHITE, width=52):
    lines = VGroup(
        *[Text(f"• {_wrap(it, width=width)}", font_size=font_size, color=color) for it in items]
    )
    lines.arrange(DOWN, aligned_edge=LEFT, buff=0.22)
    return lines


def _chromosome_1_chromatide(color=WHITE, height=1.4, width=0.22):
    barre = Rectangle(width=width, height=height, fill_color=color, fill_opacity=1, stroke_color=WHITE, stroke_width=1)
    centromere = Dot(radius=0.05, color=YELLOW)
    centromere.move_to(barre.get_center())
    return VGroup(barre, centromere)


def _chromosome_2_chromatides(color=WHITE, height=1.4, width=0.22, gap=0.08):
    gauche = Rectangle(width=width, height=height, fill_color=color, fill_opacity=1, stroke_color=WHITE, stroke_width=1)
    droite = gauche.copy()
    paire = VGroup(gauche, droite).arrange(RIGHT, buff=gap)
    centromere = Dot(radius=0.06, color=YELLOW)
    centromere.move_to(paire.get_center())
    return VGroup(gauche, droite, centromere)


class RappelsSurLesChromosomes(NotionScene):
    def construct(self):
        titre = scene_title("2.1 — Rappels sur les chromosomes")
        titre.scale(0.65)
        titre.to_edge(UP)

        # --- Énoncé : structure d'un chromosome ---------------------------------
        definition = definition_box(
            Text(
                _wrap(
                    "Chromosome : structure du noyau constituée d'une "
                    "longue molécule d'ADN associée à des protéines "
                    "(histones). Il devient visible au microscope pendant "
                    "la division, lorsqu'il se condense.",
                    width=54,
                ),
                font_size=22,
            ),
            box_width=11.8,
        )
        definition.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Le chromosome est une structure du noyau cellulaire, "
                "constituée d'une longue molécule d'ADN associée à des "
                "protéines appelées histones. Il ne devient visible au "
                "microscope optique que pendant la division cellulaire, "
                "lorsqu'il se condense, c'est-à-dire se spiralise."
            )
        ) as tracker:
            self.play(Write(titre))
            self.play(FadeIn(definition))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(definition))

        # --- Animation du raisonnement : 1 vs 2 chromatides ---------------------
        chr1 = _chromosome_1_chromatide()
        chr2 = _chromosome_2_chromatides()
        groupe = VGroup(chr1, chr2).arrange(RIGHT, buff=2.2)
        groupe.next_to(titre, DOWN, buff=1.0)

        label1 = Text("1 chromatide\n(avant réplication)", font_size=17, color=WHITE)
        label1.next_to(chr1, DOWN, buff=0.3)
        label2 = Text("2 chromatides sœurs\n(après réplication)", font_size=17, color=WHITE)
        label2.next_to(chr2, DOWN, buff=0.3)

        centromere_note = Text("point jaune = centromère", font_size=15, color=YELLOW)
        centromere_note.next_to(groupe, DOWN, buff=0.9)

        with self.voiceover(
            text=(
                "Selon le moment du cycle cellulaire, un chromosome se "
                "présente sous deux formes. Avant la réplication de l'ADN, "
                "et après l'anaphase II, il n'a qu'une seule chromatide : un "
                "seul bâtonnet. Après la réplication, et jusqu'à l'anaphase "
                "II, il possède deux chromatides sœurs, deux bâtonnets "
                "identiques réunis par le centromère, ce qui lui donne un "
                "aspect en X. La chromatide est chacun des deux filaments "
                "identiques du chromosome répliqué ; le centromère est la "
                "région étranglée où elles sont fixées, et c'est aussi le "
                "point d'attache des fibres du fuseau pendant la division."
            )
        ) as tracker:
            self.play(FadeIn(chr1), FadeIn(chr2))
            self.play(FadeIn(label1), FadeIn(label2))
            self.play(FadeIn(centromere_note))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(groupe), FadeOut(label1), FadeOut(label2), FadeOut(centromere_note))

        # --- Règle d'or : compter les centromères -------------------------------
        regle = method_box(
            VGroup(
                Text(
                    _wrap(
                        "On compte les chromosomes en comptant les "
                        "centromères. Un chromosome à 2 chromatides compte "
                        "pour UN seul chromosome.",
                        width=52,
                    ),
                    font_size=22,
                ),
                MathTex(
                    r"\text{fin d'interphase} \;:\; 46 \text{ chromosomes} \;-\; 92 \text{ chromatides}",
                    font_size=24,
                    color=WHITE,
                ),
            ).arrange(DOWN, buff=0.35),
            box_width=12.2,
        )
        regle.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Retenez cette règle d'or : on compte les chromosomes en "
                "comptant les centromères. Un chromosome à deux chromatides "
                "compte pour un seul chromosome. Ainsi, à la fin de "
                "l'interphase, la cellule humaine contient quarante-six "
                "chromosomes, mais quatre-vingt-douze chromatides."
            )
        ) as tracker:
            self.play(FadeIn(regle))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(regle))

        # --- Chromosomes homologues ---------------------------------------------
        homologues_def = definition_box(
            Text(
                _wrap(
                    "Chromosomes homologues : deux chromosomes de même "
                    "forme, même taille, portant les mêmes gènes aux mêmes "
                    "emplacements (locus). L'un vient du père, l'autre de "
                    "la mère : ils forment une paire.",
                    width=54,
                ),
                font_size=21,
            ),
            box_width=11.8,
        )
        homologues_def.next_to(titre, DOWN, buff=0.5)

        chr_p = _chromosome_2_chromatides(color=PATERNEL, height=1.3)
        chr_m = _chromosome_2_chromatides(color=MATERNEL, height=1.3)
        paire = VGroup(chr_p, chr_m).arrange(RIGHT, buff=0.5)
        paire.next_to(homologues_def, DOWN, buff=0.5)
        legende_paire = Text("origine paternelle          origine maternelle", font_size=16, color=WHITE)
        legende_paire.next_to(paire, DOWN, buff=0.25)

        with self.voiceover(
            text=(
                "Deux chromosomes sont dits homologues lorsqu'ils ont la "
                "même forme, la même taille, et portent les mêmes gènes aux "
                "mêmes emplacements, appelés locus. L'un provient du père, "
                "l'autre de la mère : ils forment une paire. Dans une "
                "cellule diploïde, les chromosomes se rangent donc par "
                "paires d'homologues."
            )
        ) as tracker:
            self.play(FadeIn(homologues_def))
            self.play(FadeIn(paire))
            self.play(FadeIn(legende_paire))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(homologues_def), FadeOut(paire), FadeOut(legende_paire))

        # --- Exemple traité : le caryotype humain -------------------------------
        caryotype = example_box(
            Text(
                _wrap(
                    "Caryotype humain normal : 46 chromosomes, soit 23 "
                    "paires (2n=46) — 22 paires d'autosomes (numérotées 1 "
                    "à 22) + 1 paire de gonosomes (XX chez la femme, XY "
                    "chez l'homme). Formule : 46,XX (femme) ou 46,XY "
                    "(homme).",
                    width=54,
                ),
                font_size=21,
            ),
            box_width=12.2,
        )
        caryotype.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Le caryotype est la photographie ordonnée de l'ensemble "
                "des chromosomes d'une cellule, classés par paires "
                "d'homologues selon leur taille décroissante. Le caryotype "
                "humain normal comprend quarante-six chromosomes, soit "
                "vingt-trois paires : on écrit deux n égale quarante-six. "
                "Vingt-deux paires sont des autosomes, numérotées de un à "
                "vingt-deux ; une paire est constituée de gonosomes, les "
                "chromosomes sexuels : X X chez la femme, X Y chez l'homme. "
                "La formule chromosomique s'écrit quarante-six, X X pour la "
                "femme, ou quarante-six, X Y pour l'homme."
            )
        ) as tracker:
            self.play(FadeIn(caryotype))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(caryotype))

        # --- À retenir : diploïde / haploïde ------------------------------------
        dip_hap = _bullets(
            [
                "Cellule diploïde (2n) : possède les chromosomes par "
                "paires d'homologues (cellules somatiques humaines, 2n=46).",
                "Cellule haploïde (n) : ne possède qu'un seul chromosome "
                "de chaque paire (gamètes humains, n=23).",
            ],
            font_size=21,
            width=52,
        )
        dip_hap.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Pour conclure ces rappels : une cellule diploïde, notée "
                "deux n, possède les chromosomes par paires d'homologues — "
                "c'est le cas des cellules somatiques humaines, à "
                "quarante-six chromosomes. Une cellule haploïde, notée n, "
                "ne possède qu'un seul chromosome de chaque paire — c'est "
                "le cas des gamètes humains, à vingt-trois chromosomes."
            )
        ) as tracker:
            self.play(FadeIn(dip_hap))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(titre), FadeOut(dip_hap))
