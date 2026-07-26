"""
scenes/Chimie_DosagesOxydoreduction_06.py — Chapitre 12 « Dosages
d'oxydoréduction » (1ereC, Chimie), scène 06.

§ Iodométrie indirecte. Principe en 2 étapes (formation du diiode par excès
d'iodure, puis dosage du diiode par le thiosulfate). Exemple fondamental de
l'hypochlorite de l'eau de Javel (ClO⁻+2I⁻+2H⁺→I₂+Cl⁻+H₂O), relation
n(ClO⁻)=n(I₂)=n(S₂O₃²⁻)/2.
Source : 1ereC/Chimie.pdf, chapitre 12, pages 118-119.
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
    Rectangle,
    Text,
    VGroup,
    Write,
    config,
)

from shapes.base_scene import NotionScene
from shapes.boxes import definition_box, scene_title, warning_box


def _wrap(text: str, width: int = 56) -> str:
    return "\n".join(textwrap.fill(line, width=width) for line in text.split("\n"))


def _fit(mobject, top_y):
    bas_visible = -config.frame_height / 2 + 0.25
    hauteur_dispo = top_y - bas_visible
    if mobject.height > hauteur_dispo:
        mobject.scale(hauteur_dispo / mobject.height, about_point=mobject.get_top())
    return mobject


def _schema_deux_etapes():
    """Diagramme de flux en 2 étapes de l'iodométrie indirecte, construit
    avec des primitives Manim de base (Rectangle, Arrow, Text/MathTex,
    VGroup) — aucune bibliothèque externe."""
    boite1 = Rectangle(width=5.0, height=1.3, color=YELLOW, stroke_width=2)
    texte1 = Text(
        "Étape 1 : oxydant X à doser\n+ excès d'ions I⁻ (milieu acide)\n"
        "→ formation de diiode I₂",
        font_size=16, color=WHITE, line_spacing=0.9,
    )
    texte1.move_to(boite1.get_center())
    groupe1 = VGroup(boite1, texte1)

    fleche = Arrow(LEFT, RIGHT, color=WHITE, stroke_width=3, max_tip_length_to_length_ratio=0.25)

    boite2 = Rectangle(width=5.0, height=1.3, color=YELLOW, stroke_width=2)
    texte2 = Text(
        "Étape 2 : le diiode I₂ formé\nest dosé par le thiosulfate\n"
        "S₂O₃²⁻ (dosage direct classique)",
        font_size=16, color=WHITE, line_spacing=0.9,
    )
    texte2.move_to(boite2.get_center())
    groupe2 = VGroup(boite2, texte2)

    schema = VGroup(groupe1, fleche, groupe2).arrange(RIGHT, buff=0.4)
    return schema


class IodometrieIndirecte(NotionScene):
    def construct(self):
        titre = scene_title("12.6 L'iodométrie indirecte")
        titre.scale(0.5)
        titre.to_edge(UP)

        # --- Énoncé ----------------------------------------------------------------------
        intro = Text(
            _wrap(
                "Certains oxydants, comme l'ion hypochlorite de l'eau de "
                "Javel, ne peuvent pas être dosés directement par le "
                "thiosulfate. On utilise alors un intermédiaire : le "
                "diiode. C'est l'iodométrie indirecte.",
                width=54,
            ),
            font_size=23,
            color=WHITE,
        )
        intro.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Certains oxydants, comme l'ion hypochlorite de l'eau de "
                "Javel, ne réagissent pas directement, ou pas de façon "
                "exploitable, avec le thiosulfate. On utilise alors un "
                "intermédiaire : le diiode. Cette méthode en deux temps "
                "s'appelle l'iodométrie indirecte."
            )
        ) as tracker:
            self.play(Write(titre))
            self.play(FadeIn(intro))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(intro))

        # --- Raisonnement : principe en 2 étapes -----------------------------------------
        entete_principe = Text("Le principe en 2 étapes", font_size=23, color=YELLOW, weight="BOLD")
        entete_principe.next_to(titre, DOWN, buff=0.4)

        schema = _schema_deux_etapes()
        schema.scale(0.95)
        schema.next_to(entete_principe, DOWN, buff=0.4)
        groupe_principe = VGroup(entete_principe, schema)
        _fit(groupe_principe, titre.get_bottom()[1] - 0.4)

        with self.voiceover(
            text=(
                "Le principe se déroule en deux étapes. Première étape : "
                "on met l'oxydant à doser en présence d'un excès d'ions "
                "iodure, en milieu acide ; il se forme alors du diiode, "
                "en quantité proportionnelle à l'oxydant initial. "
                "Deuxième étape : ce diiode formé est ensuite dosé par le "
                "thiosulfate, exactement comme dans un dosage direct "
                "classique, déjà vu dans la scène précédente."
            )
        ) as tracker:
            self.play(FadeIn(entete_principe))
            self.play(FadeIn(schema))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(groupe_principe))

        # --- Exemple traité : l'eau de Javel ----------------------------------------------
        entete_javel = Text("Exemple fondamental : l'eau de Javel", font_size=22, color=YELLOW, weight="BOLD")
        entete_javel.next_to(titre, DOWN, buff=0.4)

        texte_javel = Text(
            _wrap(
                "L'eau de Javel contient l'ion hypochlorite ClO⁻, un "
                "oxydant. En présence d'un excès d'iodure, en milieu "
                "acide, il libère du diiode :",
                width=52,
            ),
            font_size=20,
            color=WHITE,
        )

        equation1 = MathTex(
            r"ClO^- + 2\,I^- + 2\,H^+ \longrightarrow I_2 + Cl^- + H_2O",
            font_size=27, color=YELLOW,
        )

        bloc_javel = VGroup(texte_javel, equation1).arrange(DOWN, buff=0.35)
        bloc_javel.next_to(entete_javel, DOWN, buff=0.3)
        groupe_javel = VGroup(entete_javel, bloc_javel)
        _fit(groupe_javel, titre.get_bottom()[1] - 0.4)

        with self.voiceover(
            text=(
                "Prenons l'exemple fondamental de l'eau de Javel, qui "
                "contient l'ion hypochlorite, C-l-O moins, un oxydant. En "
                "présence d'un excès d'ions iodure, en milieu acide, il "
                "libère du diiode selon l'équation : C-l-O moins, plus "
                "deux I moins, plus deux H plus, donne I-2, plus C-l "
                "moins, plus H-2-O."
            )
        ) as tracker:
            self.play(FadeIn(entete_javel))
            self.play(FadeIn(texte_javel))
            self.play(Write(equation1))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(groupe_javel))

        # --- Relation générale n(ClO-) = n(I2) = n(S2O3)/2 --------------------------------
        relation = MathTex(
            r"n(ClO^-) = n(I_2) = \dfrac{n(S_2O_3^{2-})}{2}",
            font_size=30, color=YELLOW,
        )
        relation.next_to(titre, DOWN, buff=0.6)

        explication = Text(
            _wrap(
                "Le diiode formé (étape 1) est ensuite dosé par le "
                "thiosulfate (étape 2, comme en iodométrie directe).",
                width=52,
            ),
            font_size=19,
            color=WHITE,
        )
        explication.next_to(relation, DOWN, buff=0.4)
        groupe_relation = VGroup(relation, explication)

        with self.voiceover(
            text=(
                "Puisque l'équation de la première étape montre une "
                "molécule de diiode formée pour un ion hypochlorite "
                "consommé, on a directement n de ClO moins égale n de "
                "I-2. Et comme le diiode formé est ensuite dosé par le "
                "thiosulfate exactement comme dans un dosage direct, on "
                "obtient la relation complète : n de ClO moins égale n "
                "de I-2 égale n de S-2-O-3 deux moins, sur deux."
            )
        ) as tracker:
            self.play(Write(relation))
            self.play(FadeIn(explication))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(groupe_relation))

        # --- À retenir ------------------------------------------------------------------
        retenir = definition_box(
            VGroup(
                Text(
                    "Iodométrie indirecte : on ne dose pas X directement, on "
                    "dose le diiode qu'il a fait apparaître.",
                    font_size=20,
                ),
                MathTex(r"n(X) = n(I_2) = \dfrac{n(S_2O_3^{2-})}{2}", font_size=25, color="#1A1A1A"),
            ).arrange(DOWN, buff=0.3),
            box_width=11.8,
        )
        retenir.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Retenons l'essentiel de l'iodométrie indirecte : on ne "
                "dose jamais directement l'oxydant X qui nous intéresse, "
                "on dose le diiode qu'il a fait apparaître en réagissant "
                "avec un excès d'iodure. On en déduit : n de X égale n de "
                "I-2 égale n de S-2-O-3 deux moins, sur deux."
            )
        ) as tracker:
            self.play(FadeIn(retenir))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(retenir))

        # --- Piège à éviter ---------------------------------------------------------------
        piege = warning_box(
            Text(
                _wrap(
                    "Piège : l'iodure doit être en EXCÈS lors de l'étape 1, "
                    "sinon tout l'oxydant X n'est pas transformé en "
                    "diiode, et la quantité de I₂ formée ne représente "
                    "plus fidèlement n(X) — le calcul final serait faux "
                    "par défaut.",
                    width=48,
                ),
                font_size=19,
            ),
            box_width=12.2,
        )
        piege.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Attention à un piège important : l'iodure doit "
                "impérativement être en excès lors de la première étape. "
                "S'il n'y en a pas assez, tout l'oxydant X n'est pas "
                "transformé en diiode, et la quantité de diiode formée "
                "ne représente plus fidèlement la quantité initiale de "
                "X : le calcul final serait alors faux par défaut."
            )
        ) as tracker:
            self.play(FadeIn(piege))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(piege), FadeOut(titre))
