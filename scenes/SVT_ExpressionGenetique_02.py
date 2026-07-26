"""
scenes/SVT_ExpressionGenetique_02.py — Chapitre 5 (1ereC, SVT), scène 02.

I.B-C. Le nucléotide (désoxyribose, phosphate, base azotée — A/G/T/C),
orientation 5'/3', la double hélice de Watson-Crick (brins antiparallèles),
règle de complémentarité des bases (A-T 2 liaisons H, G-C 3 liaisons H),
Exemple résolu 1 (brin complémentaire de 5'-ATGCCGTA-3').
Source : 1ereC/SVT.pdf, pages 45-46.
"""

import textwrap

from manim import (
    BLUE,
    DOWN,
    GREEN,
    LEFT,
    ORANGE,
    RIGHT,
    UP,
    WHITE,
    YELLOW,
    Circle,
    FadeIn,
    FadeOut,
    Line,
    MathTex,
    Rectangle,
    Text,
    VGroup,
    Write,
)

from shapes.base_scene import NotionScene
from shapes.boxes import definition_box, example_box, method_box, scene_title, theorem_box


def _wrap(text: str, width: int = 56) -> str:
    return "\n".join(textwrap.fill(line, width=width) for line in text.split("\n"))


def _nucleotide(base_label, base_color):
    """Schéma simplifié d'un nucléotide : sucre (pentagone approx. par
    cercle), phosphate (petit cercle), base azotée (rectangle coloré)."""
    sucre = Circle(radius=0.22, color=BLUE, fill_color=BLUE, fill_opacity=0.6, stroke_width=1)
    phosphate = Circle(radius=0.14, color=ORANGE, fill_color=ORANGE, fill_opacity=0.8, stroke_width=1)
    phosphate.next_to(sucre, LEFT, buff=0.05)
    base = Rectangle(width=0.55, height=0.32, fill_color=base_color, fill_opacity=0.85, stroke_width=1)
    base.next_to(sucre, RIGHT, buff=0.08)
    base_txt = Text(base_label, font_size=16, color=WHITE, weight="BOLD")
    base_txt.move_to(base.get_center())
    return VGroup(sucre, phosphate, base, base_txt)


class NucleotideEtDoubleHelice(NotionScene):
    def construct(self):
        titre = scene_title("I.B-C — Le nucléotide et la double hélice")
        titre.scale(0.55)
        titre.to_edge(UP)

        with self.voiceover(
            text=(
                "Chaque brin d'ADN est un polynucléotide : une longue chaîne "
                "de nucléotides liés les uns aux autres. Voyons d'abord de "
                "quoi est fait un seul nucléotide."
            )
        ) as tracker:
            self.play(Write(titre))
            self.wait(tracker.get_remaining_duration())

        # --- Énoncé : les trois éléments d'un nucléotide ----------------------
        nuc = _nucleotide("A", GREEN)
        nuc.scale(2.3)
        nuc.next_to(titre, DOWN, buff=0.7)

        label_sucre = Text("1. désoxyribose (sucre)", font_size=18, color=WHITE)
        label_phosphate = Text("2. groupement phosphate", font_size=18, color=WHITE)
        label_base = Text("3. base azotée (A, G, T ou C)", font_size=18, color=WHITE)
        labels = VGroup(label_sucre, label_phosphate, label_base).arrange(DOWN, aligned_edge=LEFT, buff=0.25)
        labels.next_to(nuc, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Un nucléotide comprend toujours trois éléments : un sucre à "
                "cinq atomes de carbone, le désoxyribose ; un groupement "
                "phosphate ; et une base azotée, qui peut être de quatre "
                "sortes : adénine, guanine, thymine ou cytosine, notées A, G, "
                "T et C. L'adénine et la guanine sont des purines, la thymine "
                "et la cytosine des pyrimidines."
            )
        ) as tracker:
            self.play(FadeIn(nuc))
            self.play(FadeIn(labels))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(nuc), FadeOut(labels))

        # --- Orientation 5'/3' -------------------------------------------------
        methode_53 = method_box(
            Text(
                _wrap(
                    "Les nucléotides sont reliés par des liaisons "
                    "phosphodiester. Chaque brin possède une orientation, "
                    "repérée par deux extrémités 5' et 3' : un brin d'ADN "
                    "s'écrit toujours dans le sens 5'→3', le sens dans "
                    "lequel il est lu et synthétisé.",
                    width=54,
                ),
                font_size=23,
            ),
            box_width=11.8,
        )
        methode_53.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Les nucléotides sont reliés entre eux par des liaisons "
                "phosphodiester, entre le phosphate d'un nucléotide et le "
                "sucre du nucléotide suivant. Chaque brin possède donc une "
                "orientation, repérée par deux extrémités notées cinq prime "
                "et trois prime. Point clé à retenir : un brin d'ADN s'écrit "
                "toujours dans le sens cinq prime vers trois prime, c'est "
                "dans ce sens qu'il est lu et synthétisé."
            )
        ) as tracker:
            self.play(FadeIn(methode_53))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(methode_53))

        # --- Raisonnement : la double hélice (schéma en échelle) --------------
        entete_helice = Text("La double hélice de Watson et Crick (1953)", font_size=24, color=YELLOW, weight="BOLD")
        entete_helice.next_to(titre, DOWN, buff=0.45)

        top_seq = "ATGC"
        bottom_seq = "TACG"
        colors = {"A": GREEN, "T": ORANGE, "G": BLUE, "C": YELLOW}
        n_bonds = {"A-T": 2, "G-C": 3}

        rungs = VGroup()
        top_labels = VGroup()
        bottom_labels = VGroup()
        x = 0.0
        step = 1.3
        for tb, bb in zip(top_seq, bottom_seq):
            rung = Line(UP * 0.65, DOWN * 0.65, color=WHITE, stroke_width=2)
            n_h = n_bonds["A-T"] if {tb, bb} == {"A", "T"} else n_bonds["G-C"]
            hbonds = VGroup(
                *[Line(LEFT * 0.06, RIGHT * 0.06, stroke_width=1.5, color=WHITE).shift(UP * (0.2 * (i - (n_h - 1) / 2))) for i in range(n_h)]
            )
            hbonds.move_to(rung.get_center())
            tlabel = Text(tb, font_size=20, color=colors[tb], weight="BOLD")
            tlabel.next_to(rung, UP, buff=0.08)
            blabel = Text(bb, font_size=20, color=colors[bb], weight="BOLD")
            blabel.next_to(rung, DOWN, buff=0.08)
            group = VGroup(rung, hbonds, tlabel, blabel)
            group.shift(RIGHT * x)
            rungs.add(group)
            x += step

        backbone_top = Line(rungs[0][2].get_center() + UP * 0.15 + LEFT * 0.3, rungs[-1][2].get_center() + UP * 0.15 + RIGHT * 0.3, color=BLUE, stroke_width=4)
        backbone_bottom = Line(rungs[0][3].get_center() + DOWN * 0.15 + LEFT * 0.3, rungs[-1][3].get_center() + DOWN * 0.15 + RIGHT * 0.3, color=BLUE, stroke_width=4)

        echelle = VGroup(backbone_top, rungs, backbone_bottom)
        echelle.next_to(entete_helice, DOWN, buff=0.55)

        label_53_top = Text("5'", font_size=18, color=WHITE).next_to(backbone_top, LEFT, buff=0.15)
        label_33_top = Text("3'", font_size=18, color=WHITE).next_to(backbone_top, RIGHT, buff=0.15)
        label_53_bottom = Text("3'", font_size=18, color=WHITE).next_to(backbone_bottom, LEFT, buff=0.15)
        label_33_bottom = Text("5'", font_size=18, color=WHITE).next_to(backbone_bottom, RIGHT, buff=0.15)
        extremites = VGroup(label_53_top, label_33_top, label_53_bottom, label_33_bottom)

        with self.voiceover(
            text=(
                "En 1953, Watson et Crick, en s'appuyant sur les travaux de "
                "Rosalind Franklin et de Maurice Wilkins, ont proposé le "
                "modèle de la double hélice. La molécule d'ADN est formée de "
                "deux brins antiparallèles, l'un orienté cinq prime vers "
                "trois prime, l'autre trois prime vers cinq prime, enroulés "
                "l'un autour de l'autre. Les sucres et les phosphates "
                "forment le squelette externe de chaque brin ; les bases "
                "azotées, tournées vers l'intérieur, s'associent deux à deux "
                "par des liaisons hydrogène, formant les barreaux de "
                "l'échelle hélicoïdale."
            )
        ) as tracker:
            self.play(FadeIn(entete_helice))
            self.play(FadeIn(echelle), FadeIn(extremites))
            self.wait(tracker.get_remaining_duration())

        # --- Théorème : complémentarité des bases ------------------------------
        theoreme = theorem_box(
            Text(
                _wrap(
                    "Dans une molécule d'ADN, l'adénine fait toujours face à "
                    "la thymine (2 liaisons hydrogène), et la guanine fait "
                    "toujours face à la cytosine (3 liaisons hydrogène). Si "
                    "l'on connaît un brin, on écrit automatiquement le brin "
                    "complémentaire.",
                    width=54,
                ),
                font_size=22,
            ),
            box_width=11.8,
        )
        theoreme.next_to(entete_helice, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Ces associations obéissent à une règle stricte, la "
                "complémentarité des bases : l'adénine fait toujours face à "
                "la thymine, avec deux liaisons hydrogène ; la guanine fait "
                "toujours face à la cytosine, avec trois liaisons hydrogène. "
                "Conséquence essentielle : si l'on connaît la séquence d'un "
                "brin, on peut écrire automatiquement celle de son brin "
                "complémentaire."
            )
        ) as tracker:
            self.play(FadeOut(echelle), FadeOut(extremites), FadeIn(theoreme))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(entete_helice), FadeOut(theoreme))

        # --- Exemple résolu 1 : brin complémentaire ----------------------------
        enonce = MathTex(r"5'\text{-ATGCCGTA-}3'", font_size=32, color=WHITE)
        fleche_txt = Text("brin complémentaire, antiparallèle :", font_size=20, color=YELLOW)
        reponse = MathTex(r"3'\text{-TACGGCAT-}5'", font_size=32, color=GREEN)
        bloc_calcul = VGroup(enonce, fleche_txt, reponse).arrange(DOWN, buff=0.35)

        exemple = example_box(bloc_calcul, box_width=10.5)
        exemple.next_to(titre, DOWN, buff=0.6)

        with self.voiceover(
            text=(
                "Exemple résolu. On donne le brin d'ADN suivant : cinq prime, "
                "A T G C C G T A, trois prime. Pour écrire le brin "
                "complémentaire, on associe à chaque base sa base "
                "complémentaire, A avec T, G avec C, puis on inverse le sens "
                "car les brins sont antiparallèles. On obtient : trois "
                "prime, T A C G G C A T, cinq prime."
            )
        ) as tracker:
            self.play(FadeIn(exemple))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(exemple))

        # --- À retenir : définition ADN (nucléotide) ---------------------------
        definition = definition_box(
            Text(
                _wrap(
                    "Un nucléotide = 1 sucre (désoxyribose) + 1 phosphate + "
                    "1 base azotée (A, G, T ou C). Un brin d'ADN se lit "
                    "5'→3'. Les deux brins de la double hélice sont "
                    "antiparallèles et complémentaires (A-T, G-C).",
                    width=54,
                ),
                font_size=23,
            ),
            box_width=11.8,
        )
        definition.next_to(titre, DOWN, buff=0.55)

        with self.voiceover(
            text=(
                "Retenons l'essentiel : un nucléotide, c'est un sucre, un "
                "phosphate et une base azotée. Un brin d'ADN se lit toujours "
                "dans le sens cinq prime vers trois prime. Et les deux brins "
                "de la double hélice sont antiparallèles et complémentaires, "
                "A avec T, G avec C."
            )
        ) as tracker:
            self.play(FadeIn(definition))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(titre), FadeOut(definition))
