"""
scenes/SVT_ExpressionGenetique_01.py — Chapitre 5 (1ereC, SVT), scène 01.

I. Rappels sur l'ADN, support de l'information génétique — A. Localisation
et rôle de l'ADN. Introduction du chapitre : où se trouve l'ADN, pourquoi
il est le support de l'hérédité, définition de l'ADN, et objectifs du
chapitre. Source : 1ereC/SVT.pdf, pages 44-45.
"""

import math
import textwrap

import numpy as np

from manim import (
    DOWN,
    LEFT,
    RIGHT,
    UP,
    WHITE,
    YELLOW,
    Arrow,
    Circle,
    FadeIn,
    FadeOut,
    Line,
    Text,
    VGroup,
    Write,
)

from shapes.base_scene import NotionScene
from shapes.boxes import definition_box, scene_title, warning_box


def _wrap(text: str, width: int = 56) -> str:
    return "\n".join(textwrap.fill(line, width=width) for line in text.split("\n"))


def _bullets(items, font_size=22, color=WHITE, width=52):
    lines = VGroup(
        *[Text(f"• {_wrap(it, width=width)}", font_size=font_size, color=color) for it in items]
    )
    lines.arrange(DOWN, aligned_edge=LEFT, buff=0.22)
    return lines


def _cellule_avec_noyau():
    """Schéma simple : cellule (grand cercle) contenant un noyau (cercle
    plus petit) où loge l'ADN (petits traits enchevêtrés)."""
    cellule = Circle(radius=1.9, color=WHITE, stroke_width=2)
    noyau = Circle(radius=0.85, color=YELLOW, stroke_width=2)
    noyau.shift(RIGHT * 0.1)
    adn_traits = VGroup(
        *[
            Line(
                noyau.get_center() + 0.4 * np.array([math.cos(a), math.sin(a), 0]),
                noyau.get_center() + 0.15 * np.array([math.cos(a + 1.3), math.sin(a + 1.3), 0]),
                color=YELLOW,
                stroke_width=2,
            )
            for a in [0, 1.2, 2.4, 3.6, 4.8]
        ]
    )
    label_noyau = Text("noyau : ADN", font_size=16, color=YELLOW)
    label_noyau.next_to(noyau, DOWN, buff=0.12)
    label_cellule = Text("cellule eucaryote", font_size=16, color=WHITE)
    label_cellule.next_to(cellule, DOWN, buff=0.35)
    return VGroup(cellule, noyau, adn_traits, label_noyau, label_cellule)


class LocalisationEtRoleADN(NotionScene):
    def construct(self):
        titre = scene_title("Chapitre 5 — La synthèse des protéines")
        titre.scale(0.55)
        titre.to_edge(UP)

        sous_titre = Text(
            "I. Rappels sur l'ADN, support de l'information génétique",
            font_size=22,
            color=YELLOW,
        )
        sous_titre.next_to(titre, DOWN, buff=0.25)

        with self.voiceover(
            text=(
                "Bienvenue dans le chapitre cinq : la synthèse des protéines. "
                "C'est le chapitre le plus dense et le plus calculatoire du "
                "programme, prévu sur environ trois semaines : prenons donc "
                "le temps de bien poser chaque notion, une à la fois. "
                "Commençons par un rappel essentiel sur l'ADN, le support de "
                "l'information génétique."
            )
        ) as tracker:
            self.play(Write(titre))
            self.play(FadeIn(sous_titre))
            self.wait(tracker.get_remaining_duration())

        # --- Énoncé : localisation de l'ADN dans la cellule ---------------
        schema = _cellule_avec_noyau()
        schema.scale(0.95)
        schema.next_to(sous_titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Chez les êtres vivants à noyau, c'est-à-dire les cellules "
                "eucaryotes, l'ADN, l'acide désoxyribonucléique, se trouve "
                "principalement dans le noyau, au sein des structures "
                "appelées chromosomes. C'est là que réside l'information "
                "génétique de tout être vivant."
            )
        ) as tracker:
            self.play(FadeIn(schema))
            self.wait(tracker.get_remaining_duration())

        # --- Raisonnement : transmission héréditaire ------------------------
        cellule_mere = Circle(radius=0.55, color=WHITE, stroke_width=2)
        noyau_mere = Circle(radius=0.25, color=YELLOW, stroke_width=2).move_to(cellule_mere.get_center())
        bloc_mere = VGroup(cellule_mere, noyau_mere)
        fleche = Arrow(LEFT * 0.6, RIGHT * 0.6, buff=0, color=WHITE)
        label_fleche = Text("division cellulaire", font_size=14, color=WHITE)
        label_fleche.next_to(fleche, UP, buff=0.08)

        cellule_fille_1 = VGroup(
            Circle(radius=0.5, color=WHITE, stroke_width=2),
            Circle(radius=0.22, color=YELLOW, stroke_width=2),
        )
        cellule_fille_1[1].move_to(cellule_fille_1[0].get_center())
        cellule_fille_2 = cellule_fille_1.copy()
        filles = VGroup(cellule_fille_1, cellule_fille_2).arrange(DOWN, buff=0.25)

        transmission = VGroup(bloc_mere, fleche, label_fleche, filles).arrange(RIGHT, buff=0.5)
        transmission.next_to(sous_titre, DOWN, buff=0.6)
        label_transmission = Text(
            "l'ADN est transmis intégralement à chaque génération",
            font_size=18,
            color=WHITE,
        )
        label_transmission.next_to(transmission, DOWN, buff=0.3)

        with self.voiceover(
            text=(
                "L'ADN est transmis intégralement de génération en "
                "génération, lors de la reproduction : c'est en cela qu'il "
                "est le support de l'hérédité. Chaque cellule fille reçoit "
                "une copie fidèle de l'information génétique portée par la "
                "cellule mère."
            )
        ) as tracker:
            self.play(FadeOut(schema))
            self.play(FadeIn(transmission), FadeIn(label_transmission))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(transmission), FadeOut(label_transmission))

        # --- À retenir : définition de l'ADN ---------------------------------
        definition = definition_box(
            Text(
                _wrap(
                    "L'ADN est une macromolécule constituée de deux brins "
                    "enroulés en double hélice, formés chacun d'une "
                    "succession de nucléotides. Il porte l'information "
                    "génétique sous forme de la séquence de ses bases "
                    "azotées.",
                    width=54,
                ),
                font_size=24,
            ),
            box_width=11.8,
        )
        definition.next_to(sous_titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Retenons cette définition. L'ADN est une macromolécule "
                "constituée de deux brins enroulés en double hélice, formés "
                "chacun d'une succession de nucléotides. Il porte "
                "l'information génétique sous la forme de la séquence de ses "
                "bases azotées. Dans les scènes suivantes, nous allons "
                "décortiquer chacun de ces mots : nucléotide, double hélice, "
                "bases azotées."
            )
        ) as tracker:
            self.play(FadeIn(definition))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(definition))

        # --- Piège à éviter : ADN ne fabrique pas directement le caractère --
        piege = warning_box(
            Text(
                _wrap(
                    "L'ADN n'agit jamais directement sur l'organisme : "
                    "aucun caractère visible ne sort tout seul du noyau. "
                    "C'est en passant par la fabrication de protéines que "
                    "l'information de l'ADN devient un caractère observable "
                    "— c'est tout l'objet de ce chapitre.",
                    width=54,
                ),
                font_size=23,
            ),
            box_width=11.8,
        )
        piege.next_to(sous_titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Attention à un piège fréquent : l'ADN n'agit jamais "
                "directement sur l'organisme. Aucun caractère visible ne "
                "sort tout seul du noyau. C'est en passant par la "
                "fabrication de protéines que l'information portée par "
                "l'ADN devient un caractère observable : la couleur des "
                "yeux, la forme des globules rouges, un groupe sanguin. "
                "Comprendre ce passage de l'ADN à la protéine, c'est "
                "exactement l'objet de ce chapitre."
            )
        ) as tracker:
            self.play(FadeIn(piege))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(piege))

        # --- Objectifs du chapitre --------------------------------------------
        entete_obj = Text("Objectifs du chapitre", font_size=26, color=YELLOW, weight="BOLD")
        entete_obj.next_to(sous_titre, DOWN, buff=0.45)
        objectifs = _bullets(
            [
                "Décrire la structure de l'ADN et calculer des pourcentages "
                "de bases ou des liaisons hydrogène.",
                "Énoncer le dogme central de la biologie moléculaire.",
                "Passer du brin transcrit d'ADN à l'ARNm, et inversement.",
                "Traduire un ARNm en séquence d'acides aminés grâce au code "
                "génétique.",
                "Expliquer les rôles de l'ARN polymérase, des ribosomes et "
                "des ARNt.",
                "Analyser les conséquences d'une mutation sur une protéine, "
                "à travers l'exemple de la drépanocytose.",
            ],
            font_size=20,
            width=54,
        )
        objectifs.next_to(entete_obj, DOWN, buff=0.35)

        with self.voiceover(
            text=(
                "Voici les six objectifs de ce chapitre. Décrire la "
                "structure de l'ADN et savoir calculer des pourcentages de "
                "bases ou un nombre de liaisons hydrogène. Énoncer le dogme "
                "central de la biologie moléculaire. Passer du brin transcrit "
                "d'ADN à l'ARN messager, et inversement. Traduire un ARN "
                "messager en séquence d'acides aminés grâce à la table du "
                "code génétique. Expliquer les rôles de l'ARN polymérase, des "
                "ribosomes et des ARN de transfert. Et enfin, analyser les "
                "conséquences d'une mutation sur une protéine, à travers "
                "l'exemple de la drépanocytose, une maladie très présente en "
                "Afrique de l'Ouest."
            )
        ) as tracker:
            self.play(FadeIn(entete_obj))
            self.play(FadeIn(objectifs))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(titre), FadeOut(sous_titre), FadeOut(entete_obj), FadeOut(objectifs))
