"""
scenes/SVT_ExpressionGenetique_04.py — Chapitre 5 (1ereC, SVT), scène 04.

II. Gène et protéine : le dogme central de la biologie moléculaire.
A. Les protéines (acides aminés, liaisons peptidiques, 20 acides aminés,
fonctions). B. Définition du gène et de la synthèse des protéines.
C. Le dogme central (ADN → ARNm → Protéine), sens unique de circulation.
Source : 1ereC/SVT.pdf, pages 46-47.
"""

import textwrap

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
    Rectangle,
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


class GeneEtDogmeCentral(NotionScene):
    def construct(self):
        titre = scene_title("II — Gène et protéine : le dogme central")
        titre.scale(0.55)
        titre.to_edge(UP)

        with self.voiceover(
            text=(
                "Nous savons maintenant lire la structure de l'ADN. Voyons "
                "à présent à quoi sert cette information : à fabriquer des "
                "protéines, les véritables acteurs de la cellule."
            )
        ) as tracker:
            self.play(Write(titre))
            self.wait(tracker.get_remaining_duration())

        # --- Énoncé : les protéines, chaîne d'acides aminés --------------------
        chaine = VGroup(*[Circle(radius=0.22, color=YELLOW, fill_color=YELLOW, fill_opacity=0.7, stroke_width=1) for _ in range(6)])
        chaine.arrange(RIGHT, buff=0.12)
        label_chaine = Text("chaîne d'acides aminés reliés par des liaisons peptidiques", font_size=17, color=WHITE)
        label_chaine.next_to(chaine, DOWN, buff=0.25)
        bloc_chaine = VGroup(chaine, label_chaine)
        bloc_chaine.next_to(titre, DOWN, buff=0.6)

        with self.voiceover(
            text=(
                "Les protéines sont des macromolécules constituées d'une "
                "chaîne d'acides aminés liés entre eux par des liaisons "
                "peptidiques. Il existe vingt acides aminés différents chez "
                "les êtres vivants. L'ordre des acides aminés dans la "
                "chaîne, la séquence, détermine la forme spatiale de la "
                "protéine, et donc sa fonction."
            )
        ) as tracker:
            self.play(FadeIn(bloc_chaine))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(bloc_chaine))

        entete_fonctions = Text("Les protéines assurent presque toutes les fonctions de la cellule", font_size=20, color=YELLOW, weight="BOLD")
        entete_fonctions.next_to(titre, DOWN, buff=0.5)
        fonctions = _bullets(
            [
                "Enzymes : catalyseurs des réactions chimiques (amylase de "
                "la salive, catalase…).",
                "Protéines de structure : collagène de la peau et des os, "
                "kératine des ongles et des cheveux.",
                "Protéines de transport : hémoglobine, transport du "
                "dioxygène dans le sang.",
                "Hormones protéiques : insuline, régulation de la "
                "glycémie.",
                "Anticorps : défense de l'organisme.",
            ],
            font_size=20,
            width=54,
        )
        fonctions.next_to(entete_fonctions, DOWN, buff=0.35)

        with self.voiceover(
            text=(
                "Les protéines assurent presque toutes les fonctions de la "
                "cellule. Les enzymes catalysent les réactions chimiques, "
                "comme l'amylase de la salive ou la catalase. Les protéines "
                "de structure, comme le collagène de la peau et des os, ou "
                "la kératine des ongles et des cheveux. Les protéines de "
                "transport, comme l'hémoglobine, qui transporte le "
                "dioxygène dans le sang. Les hormones protéiques, comme "
                "l'insuline, qui régule la glycémie. Et les anticorps, qui "
                "assurent la défense de l'organisme."
            )
        ) as tracker:
            self.play(FadeIn(entete_fonctions))
            self.play(FadeIn(fonctions))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(entete_fonctions), FadeOut(fonctions))

        # --- Définitions : gène et synthèse des protéines -----------------------
        definition_gene = definition_box(
            Text(
                _wrap(
                    "Un gène est un segment d'ADN (une portion de "
                    "chromosome) qui porte l'information nécessaire à la "
                    "synthèse d'une protéine déterminée (plus précisément "
                    "d'une chaîne polypeptidique).",
                    width=54,
                ),
                font_size=23,
            ),
            box_width=11.8,
        )
        definition_gene.next_to(titre, DOWN, buff=0.55)

        with self.voiceover(
            text=(
                "Un gène est un segment d'ADN, une portion de chromosome, "
                "qui porte l'information nécessaire à la synthèse d'une "
                "protéine déterminée, plus précisément d'une chaîne "
                "polypeptidique."
            )
        ) as tracker:
            self.play(FadeIn(definition_gene))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(definition_gene))

        definition_synthese = definition_box(
            Text(
                _wrap(
                    "La synthèse des protéines est l'ensemble des "
                    "mécanismes par lesquels la cellule fabrique ses "
                    "protéines à partir de l'information contenue dans ses "
                    "gènes. Elle comporte deux grandes étapes : la "
                    "transcription et la traduction.",
                    width=54,
                ),
                font_size=23,
            ),
            box_width=11.8,
        )
        definition_synthese.next_to(titre, DOWN, buff=0.55)

        with self.voiceover(
            text=(
                "La synthèse des protéines est l'ensemble des mécanismes "
                "par lesquels la cellule fabrique ses protéines à partir de "
                "l'information contenue dans ses gènes. Elle comporte deux "
                "grandes étapes : la transcription et la traduction, que "
                "nous détaillerons chacune dans les scènes suivantes. Tout "
                "caractère héréditaire visible, la couleur des yeux, un "
                "groupe sanguin, la forme de l'hémoglobine, résulte de "
                "l'action de protéines, elles-mêmes programmées par des "
                "gènes."
            )
        ) as tracker:
            self.play(FadeIn(definition_synthese))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(definition_synthese))

        # --- Raisonnement / schéma : le dogme central ---------------------------
        entete_dogme = Text("Le dogme central de la biologie moléculaire", font_size=24, color=YELLOW, weight="BOLD")
        entete_dogme.next_to(titre, DOWN, buff=0.5)

        boite_adn = Rectangle(width=2.6, height=1.1, color=WHITE, stroke_width=2)
        txt_adn = Text("ADN", font_size=24, color=WHITE, weight="BOLD")
        label_adn = Text("(gène, noyau)", font_size=15, color=WHITE)
        bloc_adn = VGroup(boite_adn, txt_adn)
        txt_adn.move_to(boite_adn.get_center())
        label_adn.next_to(bloc_adn, DOWN, buff=0.15)

        boite_arn = Rectangle(width=2.6, height=1.1, color=YELLOW, stroke_width=2)
        txt_arn = Text("ARNm", font_size=24, color=YELLOW, weight="BOLD")
        label_arn = Text("(messager)", font_size=15, color=WHITE)
        bloc_arn = VGroup(boite_arn, txt_arn)
        txt_arn.move_to(boite_arn.get_center())
        label_arn.next_to(bloc_arn, DOWN, buff=0.15)

        boite_prot = Rectangle(width=2.6, height=1.1, color="#4FC3F7", stroke_width=2)
        txt_prot = Text("Protéine", font_size=24, color="#4FC3F7", weight="BOLD")
        label_prot = Text("(cytoplasme)", font_size=15, color=WHITE)
        bloc_prot = VGroup(boite_prot, txt_prot)
        txt_prot.move_to(boite_prot.get_center())
        label_prot.next_to(bloc_prot, DOWN, buff=0.15)

        etapes = VGroup(bloc_adn, bloc_arn, bloc_prot).arrange(RIGHT, buff=1.4)
        fleche1 = Arrow(bloc_adn.get_right(), bloc_arn.get_left(), buff=0.1, color=WHITE)
        label_fleche1 = Text("transcription", font_size=16, color=WHITE)
        label_fleche1.next_to(fleche1, UP, buff=0.1)
        fleche2 = Arrow(bloc_arn.get_right(), bloc_prot.get_left(), buff=0.1, color=WHITE)
        label_fleche2 = Text("traduction", font_size=16, color=WHITE)
        label_fleche2.next_to(fleche2, UP, buff=0.1)

        schema = VGroup(etapes, fleche1, label_fleche1, fleche2, label_fleche2, label_adn, label_arn, label_prot)
        schema.next_to(entete_dogme, DOWN, buff=0.55)

        with self.voiceover(
            text=(
                "L'ADN se trouve dans le noyau, alors que les protéines sont "
                "fabriquées dans le cytoplasme : l'information ne peut donc "
                "pas passer directement de l'ADN à la protéine, il faut un "
                "intermédiaire, l'ARN. C'est le dogme central de la biologie "
                "moléculaire : l'ADN, par transcription, donne un ARN "
                "messager ; l'ARN messager, par traduction, donne une "
                "protéine. La transcription a lieu dans le noyau, la "
                "traduction dans le cytoplasme, au niveau des ribosomes."
            )
        ) as tracker:
            self.play(FadeIn(entete_dogme))
            self.play(FadeIn(schema))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(entete_dogme), FadeOut(schema))

        # --- Piège / point clé : sens unique de l'information ------------------
        piege = warning_box(
            Text(
                _wrap(
                    "L'information génétique circule dans un seul sens : "
                    "ADN → ARN → protéine. Une protéine ne « remonte » "
                    "jamais vers l'ADN pour le modifier : ce sens unique est "
                    "au cœur du dogme central de la biologie moléculaire.",
                    width=54,
                ),
                font_size=23,
            ),
            box_width=11.8,
        )
        piege.next_to(titre, DOWN, buff=0.55)

        with self.voiceover(
            text=(
                "Retenez bien ce point : l'information génétique circule "
                "dans un seul sens, de l'ADN vers l'ARN, puis de l'ARN vers "
                "la protéine. Une protéine ne remonte jamais vers l'ADN pour "
                "le modifier. Ce sens unique de circulation de l'information "
                "est au cœur du dogme central de la biologie moléculaire."
            )
        ) as tracker:
            self.play(FadeIn(piege))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(titre), FadeOut(piege))
