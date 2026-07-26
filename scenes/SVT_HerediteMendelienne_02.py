"""
scenes/SVT_HerediteMendelienne_02.py — Chapitre 6 (1ereC, SVT), scène 02.

§ I.2 Le gène, les allèles et le locus : définitions, schéma d'une paire
de chromosomes homologues portant le même locus avec deux allèles, et
notation (majuscule = dominant, minuscule = récessif).
Source : 1ereC/SVT.pdf, page 58.
"""

import textwrap

from manim import (
    DOWN,
    LEFT,
    RIGHT,
    UP,
    WHITE,
    YELLOW,
    BLUE,
    RED,
    Create,
    FadeIn,
    FadeOut,
    Line,
    MathTex,
    RoundedRectangle,
    Text,
    VGroup,
    Write,
)

from shapes.base_scene import NotionScene
from shapes.boxes import definition_box, scene_title


def _wrap(text: str, width: int = 56) -> str:
    return "\n".join(textwrap.fill(line, width=width) for line in text.split("\n"))


def _bullets(items, font_size=23, color=WHITE, width=54):
    lines = VGroup(
        *[Text(f"• {_wrap(it, width=width)}", font_size=font_size, color=color) for it in items]
    )
    lines.arrange(DOWN, aligned_edge=LEFT, buff=0.22)
    return lines


def _chromosome(color, height=3.2, width=0.55):
    """Un chromosome schématique : bâtonnet arrondi vertical."""
    return RoundedRectangle(
        width=width,
        height=height,
        corner_radius=width / 2,
        stroke_color=color,
        stroke_width=3,
        fill_color=color,
        fill_opacity=0.25,
    )


class GeneAlleleLocus(NotionScene):
    def construct(self):
        titre = scene_title("6.2 — Gène, allèle et locus")
        titre.scale(0.72)
        titre.to_edge(UP)

        # --- Énoncé : les chromosomes homologues ---------------------------------
        intro = Text(
            _wrap(
                "Les caractères héréditaires sont portés par les "
                "chromosomes du noyau. Chez un individu diploïde, les "
                "chromosomes existent par paires de chromosomes "
                "homologues : un chromosome vient du père, l'autre de la "
                "mère.",
                width=56,
            ),
            font_size=25,
            color=WHITE,
        )
        intro.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Les caractères héréditaires sont portés par les "
                "chromosomes, situés dans le noyau des cellules. Chez un "
                "individu diploïde, les chromosomes existent par paires de "
                "chromosomes homologues : un chromosome vient du père, "
                "l'autre vient de la mère."
            )
        ) as tracker:
            self.play(Write(titre))
            self.play(FadeIn(intro))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(intro))

        # --- Animation du raisonnement : les 3 définitions ------------------------
        def_gene = definition_box(
            Text(
                _wrap(
                    "Un gène est un segment de chromosome (une portion de "
                    "la molécule d'ADN) qui commande l'expression d'un "
                    "caractère héréditaire déterminé.",
                    width=50,
                ),
                font_size=24,
            ),
            box_width=11.0,
        )
        def_gene.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Un gène est un segment de chromosome, une portion de la "
                "molécule d'ADN, qui commande l'expression d'un caractère "
                "héréditaire déterminé."
            )
        ) as tracker:
            self.play(FadeIn(def_gene))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(def_gene))

        def_allele = definition_box(
            Text(
                _wrap(
                    "Les allèles sont les différentes versions possibles "
                    "d'un même gène. Un individu diploïde possède, pour "
                    "chaque gène, deux allèles (un sur chaque chromosome "
                    "homologue), identiques ou différents.",
                    width=50,
                ),
                font_size=23,
            ),
            box_width=11.0,
        )
        def_allele.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Les allèles sont les différentes versions possibles d'un "
                "même gène. Un individu diploïde possède, pour chaque "
                "gène, deux allèles, un sur chaque chromosome homologue, "
                "identiques ou différents."
            )
        ) as tracker:
            self.play(FadeIn(def_allele))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(def_allele))

        def_locus = definition_box(
            Text(
                _wrap(
                    "Le locus est l'emplacement précis qu'occupe un gène "
                    "sur un chromosome. Pour un gène donné, le locus est le "
                    "même sur les deux chromosomes homologues.",
                    width=50,
                ),
                font_size=24,
            ),
            box_width=11.0,
        )
        def_locus.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Le locus est l'emplacement précis qu'occupe un gène sur "
                "un chromosome. Pour un gène donné, le locus est le même "
                "sur les deux chromosomes homologues : c'est ce qui permet "
                "aux deux allèles de se faire face."
            )
        ) as tracker:
            self.play(FadeIn(def_locus))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(def_locus))

        # --- Exemple traité : schéma d'une paire de chromosomes homologues ------
        entete_ex = Text(
            "Une paire de chromosomes homologues (individu Aa)", font_size=24, color=YELLOW, weight="BOLD"
        )
        entete_ex.next_to(titre, DOWN, buff=0.5)

        chr_pere = _chromosome(BLUE)
        chr_mere = _chromosome(RED)
        paire = VGroup(chr_pere, chr_mere).arrange(RIGHT, buff=1.4)
        paire.next_to(entete_ex, DOWN, buff=0.8)

        label_pere = Text("Origine paternelle", font_size=18, color=BLUE)
        label_pere.next_to(chr_pere, UP, buff=0.2)
        label_mere = Text("Origine maternelle", font_size=18, color=RED)
        label_mere.next_to(chr_mere, UP, buff=0.2)

        locus_y = chr_pere.get_center()[1]
        trait_pere = Line(
            chr_pere.get_left() + [0, locus_y - chr_pere.get_center()[1], 0],
            chr_pere.get_right() + [0, locus_y - chr_pere.get_center()[1], 0],
            color=YELLOW,
            stroke_width=3,
        )
        trait_mere = Line(
            chr_mere.get_left() + [0, locus_y - chr_mere.get_center()[1], 0],
            chr_mere.get_right() + [0, locus_y - chr_mere.get_center()[1], 0],
            color=YELLOW,
            stroke_width=3,
        )
        allele_A = MathTex("A", font_size=34, color=YELLOW).next_to(chr_pere, RIGHT, buff=0.15).align_to(trait_pere, UP)
        allele_a = MathTex("a", font_size=34, color=YELLOW).next_to(chr_mere, RIGHT, buff=0.15).align_to(trait_mere, UP)
        locus_label = Text("même locus", font_size=18, color=YELLOW)
        locus_label.next_to(VGroup(trait_pere, trait_mere), DOWN, buff=1.6)

        with self.voiceover(
            text=(
                "Voici, par exemple, une paire de chromosomes homologues "
                "chez un individu hétérozygote, noté A a. Le chromosome "
                "d'origine paternelle, en bleu, porte l'allèle A ; le "
                "chromosome d'origine maternelle, en rouge, porte l'allèle "
                "a. Les deux allèles occupent exactement le même "
                "emplacement sur les deux chromosomes : c'est le locus du "
                "gène considéré."
            )
        ) as tracker:
            self.play(FadeIn(entete_ex))
            self.play(Create(paire), FadeIn(label_pere), FadeIn(label_mere))
            self.play(Create(trait_pere), Create(trait_mere))
            self.play(Write(allele_A), Write(allele_a))
            self.play(FadeIn(locus_label))
            self.wait(tracker.get_remaining_duration())

        self.play(
            FadeOut(entete_ex),
            FadeOut(paire),
            FadeOut(label_pere),
            FadeOut(label_mere),
            FadeOut(trait_pere),
            FadeOut(trait_mere),
            FadeOut(allele_A),
            FadeOut(allele_a),
            FadeOut(locus_label),
        )

        # --- À retenir : la notation ---------------------------------------------
        entete_not = Text("Notation des allèles", font_size=25, color=YELLOW, weight="BOLD")
        entete_not.next_to(titre, DOWN, buff=0.5)

        notation = _bullets(
            [
                "MAJUSCULE = allèle dominant. Exemple : L pour « graine "
                "lisse ».",
                "minuscule = allèle récessif. Exemple : l pour « graine "
                "ridée ».",
            ],
            font_size=25,
            width=48,
        )
        notation.next_to(entete_not, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Retenez la convention de notation utilisée dans tout ce "
                "chapitre : la majuscule désigne l'allèle dominant, par "
                "exemple L pour graine lisse ; la minuscule désigne "
                "l'allèle récessif, par exemple l pour graine ridée. Cette "
                "notation nous servira pour tous les croisements étudiés."
            )
        ) as tracker:
            self.play(FadeIn(entete_not))
            self.play(FadeIn(notation))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(titre), FadeOut(entete_not), FadeOut(notation))
