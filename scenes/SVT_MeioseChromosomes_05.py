"""
scenes/SVT_MeioseChromosomes_05.py — Chapitre 2 (1ereC, SVT), scène 05.

§ Méiose II (prophase II → métaphase II → anaphase II → télophase II,
séparation des chromatides sœurs) + bilan de la méiose (1 cellule 2n → 2
cellules n → 4 cellules n, schéma vue d'ensemble, code couleur
paternel/maternel).
Source : 1ereC/SVT.pdf, page 16.
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
    Rectangle,
    Text,
    VGroup,
    Write,
)

from shapes.base_scene import NotionScene
from shapes.boxes import property_box, scene_title

PATERNEL = "#B5651D"
MATERNEL = "#2E8B57"


def _wrap(text: str, width: int = 56) -> str:
    return "\n".join(textwrap.fill(line, width=width) for line in text.split("\n"))


def _chr_double(color, height=0.9, width=0.16, gap=0.06):
    left = Rectangle(width=width, height=height, fill_color=color, fill_opacity=1, stroke_color=WHITE, stroke_width=1)
    right = left.copy()
    paire = VGroup(left, right).arrange(RIGHT, buff=gap)
    dot = Dot(radius=0.045, color=YELLOW)
    dot.move_to(paire.get_center())
    return VGroup(left, right, dot)


def _chr_simple(color, height=0.9, width=0.16):
    rect = Rectangle(width=width, height=height, fill_color=color, fill_opacity=1, stroke_color=WHITE, stroke_width=1)
    dot = Dot(radius=0.045, color=YELLOW)
    dot.move_to(rect.get_center())
    return VGroup(rect, dot)


class MeioseIIEtBilan(NotionScene):
    def construct(self):
        titre = scene_title("2.3 — Méiose II et bilan de la méiose")
        titre.scale(0.6)
        titre.to_edge(UP)

        # --- Énoncé : la méiose II ressemble à une mitose -----------------------
        intro_txt = Text(
            _wrap(
                "La méiose II ressemble à une mitose, mais elle s'effectue "
                "sur des cellules déjà haploïdes.",
                width=54,
            ),
            font_size=23,
            color=WHITE,
        )
        intro_txt.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "La deuxième division de la méiose ressemble beaucoup à une "
                "mitose ordinaire, mais elle s'effectue sur des cellules "
                "déjà haploïdes, issues de la méiose I."
            )
        ) as tracker:
            self.play(Write(titre))
            self.play(FadeIn(intro_txt))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(intro_txt))

        # --- Animation du raisonnement : P II -> M II -> A II -> T II -----------
        cell_h = Ellipse(width=2.6, height=1.7, color=WHITE, stroke_width=2)
        cell_b = Ellipse(width=2.6, height=1.7, color=WHITE, stroke_width=2)
        VGroup(cell_h, cell_b).arrange(RIGHT, buff=1.0).next_to(titre, DOWN, buff=0.8)

        chr_h = _chr_double(PATERNEL)
        chr_h.move_to(cell_h.get_center())
        chr_b = _chr_double(MATERNEL)
        chr_b.move_to(cell_b.get_center())

        label_p2 = Text("Prophase II : recondensation, pas de réplication", font_size=16, color=WHITE)
        label_p2.next_to(VGroup(cell_h, cell_b), DOWN, buff=0.3)

        with self.voiceover(
            text=(
                "Prophase II : dans chacune des deux cellules issues de la "
                "première division, les chromosomes, toujours à deux "
                "chromatides, se recondensent ; un nouveau fuseau se forme. "
                "Il n'y a pas de réplication de l'ADN."
            )
        ) as tracker:
            self.play(FadeIn(cell_h), FadeIn(cell_b))
            self.play(FadeIn(chr_h), FadeIn(chr_b))
            self.play(FadeIn(label_p2))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(label_p2))

        label_m2 = Text("Métaphase II : alignement individuel sur la plaque équatoriale", font_size=15, color=WHITE)
        label_m2.next_to(VGroup(cell_h, cell_b), DOWN, buff=0.3)
        with self.voiceover(
            text=(
                "Métaphase II : les chromosomes, à deux chromatides, "
                "s'alignent individuellement sur la plaque équatoriale de "
                "chaque cellule."
            )
        ) as tracker:
            self.play(FadeIn(label_m2))
            self.wait(tracker.get_remaining_duration())
        self.play(FadeOut(label_m2))

        label_a2 = Text("Anaphase II : les CENTROMÈRES se divisent,\nles chromatides sœurs se séparent", font_size=15, color=WHITE)
        label_a2.next_to(VGroup(cell_h, cell_b), DOWN, buff=0.3)

        with self.voiceover(
            text=(
                "Anaphase II : les centromères se divisent ; les "
                "chromatides sœurs se séparent et migrent vers les pôles "
                "opposés. Chaque chromatide devient alors un chromosome à "
                "une seule chromatide."
            )
        ) as tracker:
            self.play(
                FadeOut(chr_h[2]), FadeOut(chr_b[2]),
                chr_h[0].animate.shift(UP * 0.35), chr_h[1].animate.shift(DOWN * 0.35),
                chr_b[0].animate.shift(UP * 0.35), chr_b[1].animate.shift(DOWN * 0.35),
            )
            self.play(FadeIn(label_a2))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(label_a2))

        # Télophase II : 4 cellules
        c1 = Ellipse(width=1.4, height=1.1, color=WHITE, stroke_width=2)
        c2, c3, c4 = c1.copy(), c1.copy(), c1.copy()
        finales = VGroup(c1, c2, c3, c4).arrange(RIGHT, buff=0.45)
        finales.move_to(VGroup(cell_h, cell_b).get_center())

        contenus = VGroup()
        for cell, col in zip([c1, c2, c3, c4], [PATERNEL, PATERNEL, MATERNEL, MATERNEL]):
            s = _chr_simple(col, height=0.5)
            s.move_to(cell.get_center())
            contenus.add(s)

        label_t2 = Text("Télophase II : 4 cellules haploïdes,\nnoyaux reformés, cytokinèse achevée", font_size=15, color=WHITE)
        label_t2.next_to(finales, DOWN, buff=0.3)

        with self.voiceover(
            text=(
                "Télophase II : les noyaux se reforment, et la cytokinèse "
                "achève la division dans chacune des deux cellules. On "
                "obtient au total quatre cellules haploïdes."
            )
        ) as tracker:
            self.play(
                FadeOut(cell_h), FadeOut(cell_b), FadeOut(chr_h), FadeOut(chr_b),
                FadeIn(finales), FadeIn(contenus),
            )
            self.play(FadeIn(label_t2))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(finales), FadeOut(contenus), FadeOut(label_t2))

        # --- Exemple traité : vue d'ensemble (bilan schématique) ----------------
        entete = Text("Vue d'ensemble : 1 cellule (2n) → 4 cellules (n)", font_size=22, color=YELLOW, weight="BOLD")
        entete.next_to(titre, DOWN, buff=0.5)

        mere = Ellipse(width=1.6, height=1.3, color=WHITE, stroke_width=2)
        contenu_mere = VGroup(_chr_double(PATERNEL, height=0.55), _chr_double(MATERNEL, height=0.55)).arrange(RIGHT, buff=0.1)
        contenu_mere.move_to(mere.get_center())
        bloc_mere = VGroup(mere, contenu_mere)

        filles_2 = VGroup(*[Ellipse(width=1.2, height=1.0, color=WHITE, stroke_width=2) for _ in range(2)]).arrange(RIGHT, buff=0.4)
        contenus_2 = VGroup(
            VGroup(_chr_double(PATERNEL, height=0.45)),
            VGroup(_chr_double(MATERNEL, height=0.45)),
        )
        for cell, cont in zip(filles_2, contenus_2):
            cont.move_to(cell.get_center())
        bloc_2 = VGroup(filles_2, contenus_2)

        filles_4 = VGroup(*[Ellipse(width=0.9, height=0.75, color=WHITE, stroke_width=2) for _ in range(4)]).arrange(RIGHT, buff=0.3)
        couleurs_4 = [PATERNEL, PATERNEL, MATERNEL, MATERNEL]
        contenus_4 = VGroup()
        for cell, col in zip(filles_4, couleurs_4):
            s = _chr_simple(col, height=0.35)
            s.move_to(cell.get_center())
            contenus_4.add(s)
        bloc_4 = VGroup(filles_4, contenus_4)

        ligne = VGroup(bloc_mere, bloc_2, bloc_4).arrange(RIGHT, buff=1.0)
        ligne.next_to(entete, DOWN, buff=0.6)

        fleche1 = Text("méiose I", font_size=15, color=YELLOW)
        fleche1.move_to((bloc_mere.get_right() + bloc_2.get_left()) / 2 + UP * 0.1)
        fleche2 = Text("méiose II", font_size=15, color=YELLOW)
        fleche2.move_to((bloc_2.get_right() + bloc_4.get_left()) / 2 + UP * 0.1)

        with self.voiceover(
            text=(
                "Voici le bilan complet, en une seule image. Une cellule "
                "mère diploïde, à deux n chromosomes chacun à deux "
                "chromatides, donne, après la méiose I, deux cellules "
                "haploïdes, à n chromosomes encore à deux chromatides. La "
                "méiose II sépare ensuite les chromatides sœurs et donne, au "
                "total, quatre cellules haploïdes, à n chromosomes simples, "
                "toutes génétiquement différentes."
            )
        ) as tracker:
            self.play(FadeIn(entete))
            self.play(FadeIn(bloc_mere))
            self.play(FadeIn(fleche1), FadeIn(bloc_2))
            self.play(FadeIn(fleche2), FadeIn(bloc_4))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(entete), FadeOut(ligne), FadeOut(fleche1), FadeOut(fleche2))

        # --- À retenir : bilan (property_box) ------------------------------------
        bilan = property_box(
            Text(
                _wrap(
                    "À partir d'une cellule mère diploïde (2n chromosomes "
                    "à 2 chromatides), on obtient quatre cellules filles "
                    "haploïdes (n chromosomes à 1 chromatide), toutes "
                    "génétiquement différentes.\n\n"
                    "1 cellule (2n) → méiose I → 2 cellules (n)\n"
                    "→ méiose II → 4 cellules (n)",
                    width=52,
                ),
                font_size=22,
            ),
            box_width=12.0,
        )
        bilan.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Retenons donc le bilan de la méiose : à partir d'une "
                "cellule mère diploïde, à deux n chromosomes, chacun à deux "
                "chromatides, on obtient quatre cellules filles haploïdes, à "
                "n chromosomes, chacun à une seule chromatide, et toutes "
                "génétiquement différentes. Une cellule à deux n, après la "
                "méiose I, donne deux cellules à n ; après la méiose II, ces "
                "deux cellules donnent quatre cellules à n."
            )
        ) as tracker:
            self.play(FadeIn(bilan))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(titre), FadeOut(bilan))
