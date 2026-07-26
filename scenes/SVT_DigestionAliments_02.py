"""
scenes/SVT_DigestionAliments_02.py — Chapitre 12 (1ereD, SVT), scène 02.

§ 12.1 Aliments, nutriments et digestion : définitions d'aliment et de
nutriment (exemples attiéké / poisson / huile de palme), définition de la
digestion (transformations mécaniques ET chimiques), exemple amidon →
maltose → glucose, pièges « aliment/nutriment » et « digestion seulement
dans l'estomac ».
Source : 1ereD/SVT.pdf, pages 156-157.
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
    FadeIn,
    FadeOut,
    MathTex,
    Text,
    VGroup,
    Write,
)

from shapes.base_scene import NotionScene
from shapes.boxes import definition_box, example_box, scene_title, warning_box


def _wrap(text: str, width: int = 56) -> str:
    return "\n".join(textwrap.fill(line, width=width) for line in text.split("\n"))


def _bullets(items, font_size=23, color=WHITE, width=52):
    lines = VGroup(
        *[Text(f"• {_wrap(it, width=width)}", font_size=font_size, color=color) for it in items]
    )
    lines.arrange(DOWN, aligned_edge=LEFT, buff=0.24)
    return lines


class AlimentsNutrimentsEtDigestion(NotionScene):
    def construct(self):
        titre = scene_title("12.1 — Aliments, nutriments, digestion")
        titre.scale(0.62)
        titre.to_edge(UP)

        # --- Énoncé : définition aliment / nutriment ----------------------
        definition = definition_box(
            Text(
                _wrap(
                    "Un aliment est une substance consommée par l'organisme "
                    "et qui contient un ou plusieurs nutriments. Un "
                    "nutriment est une substance simple, contenue dans un "
                    "aliment, directement utilisable par les cellules de "
                    "l'organisme après absorption.",
                    width=54,
                ),
                font_size=23,
            ),
            box_width=11.9,
        )
        definition.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Un aliment est une substance consommée par l'organisme et "
                "qui contient un ou plusieurs nutriments. Un nutriment est "
                "une substance simple, contenue dans un aliment, "
                "directement utilisable par les cellules de l'organisme "
                "après absorption."
            )
        ) as tracker:
            self.play(Write(titre))
            self.play(FadeIn(definition))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(definition))

        # --- Animation du raisonnement : trois aliments, trois familles ---
        entete = Text("Trois aliments du repas d'Awa", font_size=26, color=YELLOW, weight="BOLD")
        entete.next_to(titre, DOWN, buff=0.5)

        lignes = _bullets(
            [
                "Attiéké → riche en amidon (un glucide).",
                "Poisson → riche en protéines.",
                "Huile de palme → riche en lipides.",
            ],
            font_size=24,
            width=48,
        )
        lignes.next_to(entete, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "L'attiéké est un aliment riche en amidon, qui est un "
                "glucide ; le poisson est un aliment riche en protéines ; "
                "l'huile de palme est un aliment riche en lipides. Ces "
                "trois familles de nutriments — glucides, protéines, "
                "lipides — sont formées de grosses molécules."
            )
        ) as tracker:
            self.play(FadeIn(entete))
            self.play(FadeIn(lignes))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(entete), FadeOut(lignes))

        remarque_taille = Text(
            _wrap(
                "Une molécule d'amidon est une longue chaîne de centaines "
                "de molécules de glucose liées entre elles. Une grosse "
                "molécule, souvent insoluble, ne peut pas traverser la "
                "paroi de l'intestin : elle n'est pas assimilable en "
                "l'état. À l'inverse, eau, sels minéraux et vitamines sont "
                "de petites molécules, absorbées directement.",
                width=54,
            ),
            font_size=22,
            color=WHITE,
        )
        remarque_taille.next_to(titre, DOWN, buff=0.55)

        with self.voiceover(
            text=(
                "Par exemple, une molécule d'amidon est une longue chaîne "
                "de centaines de molécules de glucose liées les unes aux "
                "autres. Or une grosse molécule, souvent insoluble, ne "
                "peut pas traverser la paroi de l'intestin : elle n'est "
                "pas assimilable en l'état. À l'inverse, l'eau, les sels "
                "minéraux et les vitamines sont de petites molécules "
                "simples : ils sont absorbés directement, sans aucune "
                "transformation chimique."
            )
        ) as tracker:
            self.play(FadeIn(remarque_taille))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(remarque_taille))

        # --- Définition de la digestion -----------------------------------
        def_digestion = definition_box(
            Text(
                _wrap(
                    "La digestion est l'ensemble des transformations que "
                    "subissent les aliments dans le tube digestif pour "
                    "être convertis en nutriments assimilables. Elle "
                    "comprend des transformations mécaniques (mastication, "
                    "brassage, péristaltisme) et des transformations "
                    "chimiques (découpage par les enzymes des sucs "
                    "digestifs).",
                    width=54,
                ),
                font_size=22,
            ),
            box_width=12.0,
        )
        def_digestion.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "La digestion est l'ensemble des transformations que "
                "subissent les aliments dans le tube digestif pour être "
                "convertis en nutriments assimilables. Elle comprend deux "
                "types de transformations : des transformations "
                "mécaniques, qui fragmentent, mélangent et déplacent les "
                "aliments — mastication, brassage, péristaltisme ; et des "
                "transformations chimiques, qui découpent les grosses "
                "molécules en petites molécules sous l'action des enzymes "
                "contenues dans les sucs digestifs."
            )
        ) as tracker:
            self.play(FadeIn(def_digestion))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(def_digestion))

        # --- Exemple traité : amidon → maltose → glucose -------------------
        exemple_titre = Text(
            "Exemple : le devenir de l'amidon de l'attiéké", font_size=24, color=YELLOW, weight="BOLD"
        )
        exemple_titre.next_to(titre, DOWN, buff=0.55)

        schema = MathTex(
            r"\text{amidon} \;\longrightarrow\; \text{maltose} \;\longrightarrow\; \text{glucose}",
            font_size=38,
            color=WHITE,
        )
        schema.next_to(exemple_titre, DOWN, buff=0.55)

        legende = Text(
            _wrap(
                "Le glucose, petite molécule soluble dans l'eau, pourra "
                "traverser la paroi de l'intestin grêle et passer dans le "
                "sang.",
                width=52,
            ),
            font_size=22,
            color=WHITE,
        )
        legende.next_to(schema, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Prenons l'amidon de l'attiéké. Cette grosse molécule est "
                "découpée en deux temps : d'abord en maltose, un sucre "
                "formé de deux glucoses liés, puis le maltose est "
                "lui-même séparé en deux molécules de glucose. Le glucose, "
                "petite molécule soluble dans l'eau, pourra traverser la "
                "paroi de l'intestin grêle et passer dans le sang."
            )
        ) as tracker:
            self.play(FadeIn(exemple_titre))
            self.play(Write(schema))
            self.play(FadeIn(legende))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(exemple_titre), FadeOut(schema), FadeOut(legende))

        # --- À retenir : produits finaux de chaque famille ------------------
        a_retenir = _bullets(
            [
                "Glucide complexe (amidon) → sucre simple (glucose).",
                "Protéine → acides aminés.",
                "Lipide → acides gras et glycérol.",
                "Ce sont ces petites molécules qui seront absorbées.",
            ],
            font_size=23,
            width=52,
        )
        entete_retenir = Text("À retenir", font_size=26, color=YELLOW, weight="BOLD")
        entete_retenir.next_to(titre, DOWN, buff=0.55)
        a_retenir.next_to(entete_retenir, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "À retenir : le produit final de la digestion d'un "
                "glucide complexe comme l'amidon est un sucre simple, le "
                "glucose ; celui d'une protéine est un ensemble d'acides "
                "aminés ; celui d'un lipide est un mélange d'acides gras "
                "et de glycérol. Ce sont ces petites molécules qui seront "
                "absorbées."
            )
        ) as tracker:
            self.play(FadeIn(entete_retenir))
            self.play(FadeIn(a_retenir))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(entete_retenir), FadeOut(a_retenir))

        # --- Pièges à éviter -------------------------------------------------
        piege = warning_box(
            Text(
                _wrap(
                    "Deux confusions à éviter : (1) ne pas confondre "
                    "« aliment » et « nutriment » — le placali est un "
                    "aliment, le glucose issu de son amidon est un "
                    "nutriment. (2) la digestion ne se déroule pas "
                    "seulement dans l'estomac : elle commence dans la "
                    "bouche, se poursuit dans l'estomac et s'achève dans "
                    "l'intestin grêle.",
                    width=54,
                ),
                font_size=21,
            ),
            box_width=12.0,
        )
        piege.next_to(titre, DOWN, buff=0.55)

        with self.voiceover(
            text=(
                "Deux confusions à éviter. Ne confonds pas aliment et "
                "nutriment : le placali est un aliment, le glucose issu "
                "de son amidon est un nutriment. Et ne crois pas que la "
                "digestion se déroule seulement dans l'estomac : elle "
                "commence dans la bouche, se poursuit dans l'estomac et "
                "s'achève dans l'intestin grêle."
            )
        ) as tracker:
            self.play(FadeIn(piege))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(titre), FadeOut(piege))
