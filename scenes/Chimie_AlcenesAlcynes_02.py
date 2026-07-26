"""
scenes/Chimie_AlcenesAlcynes_02.py — Chapitre 3 (1ereC, Chimie), scène 02.

Formule brute générale des alcènes : définition (hydrocarbure non cyclique
possédant une double liaison C=C), formule CnH2n (n≥2), et tableau
comparatif alcanes / alcènes / alcynes (liaison caractéristique, formule
brute générale, exemple). Source : 1ereC/Chimie.pdf, chapitre 3, page 26.
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
    Line,
    MathTex,
    Rectangle,
    Text,
    VGroup,
    Write,
    config,
)

from shapes.base_scene import NotionScene
from shapes.boxes import definition_box, scene_title


def _wrap(text: str, width: int = 56) -> str:
    return "\n".join(textwrap.fill(line, width=width) for line in text.split("\n"))


def _fit(mobject, top_y):
    bas_visible = -config.frame_height / 2 + 0.25
    hauteur_dispo = top_y - bas_visible
    if mobject.height > hauteur_dispo:
        mobject.scale(hauteur_dispo / mobject.height, about_point=mobject.get_top())
    return mobject


def _tableau_comparatif():
    """Tableau à 4 colonnes (famille / liaison / formule générale / exemple)
    construit avec des primitives simples (Line + Text/MathTex), pas de
    Table Manim, pour rester cohérent avec le style du chapitre 1."""
    entetes = ["Famille", "Liaison", "Formule générale", "Exemple"]
    lignes_txt = [
        ["Alcane", r"C-C", r"C_nH_{2n+2}", r"C_2H_6"],
        ["Alcène", r"C=C", r"C_nH_{2n}", r"C_2H_4"],
        ["Alcyne", r"C \equiv C", r"C_nH_{2n-2}", r"C_2H_2"],
    ]

    col_width = 2.7
    n_cols = 4
    n_rows = 1 + len(lignes_txt)
    row_height = 0.55

    cells = VGroup()
    for j, entete in enumerate(entetes):
        c = Text(entete, font_size=20, color=YELLOW, weight="BOLD")
        c.move_to([(j - (n_cols - 1) / 2) * col_width, (n_rows - 1) / 2 * row_height, 0])
        cells.add(c)

    for i, ligne in enumerate(lignes_txt):
        for j, val in enumerate(ligne):
            if j == 0:
                c = Text(val, font_size=20, color=WHITE)
            else:
                c = MathTex(val, font_size=26, color=WHITE)
            c.move_to([(j - (n_cols - 1) / 2) * col_width, ((n_rows - 1) / 2 - (i + 1)) * row_height, 0])
            cells.add(c)

    largeur_totale = n_cols * col_width
    hauteur_totale = n_rows * row_height
    contour = Rectangle(width=largeur_totale, height=hauteur_totale, color=WHITE, stroke_width=2)

    lignes_h = VGroup(
        *[
            Line(
                [-largeur_totale / 2, (n_rows / 2 - k) * row_height, 0],
                [largeur_totale / 2, (n_rows / 2 - k) * row_height, 0],
                color=WHITE,
                stroke_width=1,
            )
            for k in range(n_rows + 1)
        ]
    )
    lignes_v = VGroup(
        *[
            Line(
                [(-n_cols / 2 + k) * col_width, hauteur_totale / 2, 0],
                [(-n_cols / 2 + k) * col_width, -hauteur_totale / 2, 0],
                color=WHITE,
                stroke_width=1,
            )
            for k in range(n_cols + 1)
        ]
    )

    return VGroup(contour, lignes_h, lignes_v, cells)


class FormuleBruteAlcenes(NotionScene):
    def construct(self):
        titre = scene_title("2. Formule brute générale des alcènes")
        titre.scale(0.55)
        titre.to_edge(UP)

        # --- Énoncé : définition d'un alcène ------------------------------------
        definition = definition_box(
            Text(
                _wrap(
                    "Un alcène est un hydrocarbure non cyclique dont la "
                    "molécule possède une seule double liaison C=C.",
                    width=48,
                ),
                font_size=26,
            ),
        )
        definition.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Posons la définition générale : un alcène est un "
                "hydrocarbure non cyclique dont la molécule possède une "
                "seule double liaison carbone-carbone."
            )
        ) as tracker:
            self.play(Write(titre))
            self.play(FadeIn(definition))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(definition))

        # --- Animation du raisonnement : formule générale CnH2n ------------------
        entete = Text("La formule brute générale", font_size=25, color=YELLOW, weight="BOLD")
        entete.next_to(titre, DOWN, buff=0.4)

        formule = MathTex(r"C_nH_{2n} \quad (n \geq 2)", font_size=40, color=WHITE)
        formule.next_to(entete, DOWN, buff=0.5)

        exemples = MathTex(
            r"n=2: C_2H_4 \qquad n=3: C_3H_6 \qquad n=4: C_4H_8",
            font_size=28,
            color=WHITE,
        )
        exemples.next_to(formule, DOWN, buff=0.5)

        groupe1 = VGroup(entete, formule, exemples)

        with self.voiceover(
            text=(
                "Tout alcène a pour formule brute générale C indice n, H "
                "indice 2 n, avec n supérieur ou égal à 2, puisqu'il faut "
                "au moins deux atomes de carbone pour former une double "
                "liaison. Pour n égal 2, on retrouve l'éthylène, C deux H "
                "quatre. Pour n égal 3, le propène, C trois H six. Pour n "
                "égal 4, le butène, C quatre H huit."
            )
        ) as tracker:
            self.play(FadeIn(entete))
            self.play(FadeIn(formule))
            self.play(FadeIn(exemples))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(groupe1))

        # --- Exemple traité : tableau comparatif alcane/alcène/alcyne -----------
        entete2 = Text("Comparaison alcanes / alcènes / alcynes", font_size=23, color=YELLOW, weight="BOLD")
        entete2.next_to(titre, DOWN, buff=0.35)

        tableau = _tableau_comparatif()
        tableau.next_to(entete2, DOWN, buff=0.4)
        _fit(tableau, entete2.get_bottom()[1] - 0.4)

        groupe2 = VGroup(entete2, tableau)

        with self.voiceover(
            text=(
                "Ce tableau résume les trois familles d'hydrocarbures que "
                "l'on rencontre au programme. L'alcane ne possède que des "
                "liaisons simples carbone-carbone, avec la formule "
                "générale C indice n H indice deux n plus deux : l'éthane "
                "en est un exemple. L'alcène possède une double liaison, "
                "formule C indice n H indice deux n : l'éthylène en est un "
                "exemple. L'alcyne possède une triple liaison, formule C "
                "indice n H indice deux n moins deux : l'acétylène en est "
                "un exemple."
            )
        ) as tracker:
            self.play(FadeIn(entete2))
            self.play(FadeIn(tableau))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(groupe2))

        # --- À retenir -------------------------------------------------------------
        retenir = definition_box(
            Text(
                _wrap(
                    "Pour un même nombre n d'atomes de carbone, un alcène "
                    "possède toujours 2 atomes d'hydrogène de moins qu'un "
                    "alcane : c'est la signature de la double liaison.",
                    width=48,
                ),
                font_size=25,
            ),
        )
        retenir.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Retenons l'essentiel : pour un même nombre n d'atomes de "
                "carbone, un alcène possède toujours deux atomes "
                "d'hydrogène de moins qu'un alcane. C'est la signature "
                "numérique de la double liaison."
            )
        ) as tracker:
            self.play(FadeIn(retenir))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(retenir))

        # --- Pièges à éviter ---------------------------------------------------
        piege = Text(
            _wrap(
                "Piège fréquent : un hydrocarbure cyclique saturé "
                "(cyclopentane, cyclohexane…) a lui aussi la formule "
                "CₙH₂ₙ, identique à celle d'un alcène, sans pourtant "
                "posséder de double liaison. La formule brute seule ne "
                "suffit donc pas à identifier un alcène.",
                width=52,
            ),
            font_size=24,
            color=WHITE,
        )
        piege.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Attention à un piège classique : un hydrocarbure "
                "cyclique saturé, comme le cyclopentane ou le "
                "cyclohexane, possède lui aussi la formule brute C indice "
                "n H indice deux n, identique à celle d'un alcène, alors "
                "qu'il ne contient aucune double liaison. La formule "
                "brute seule ne suffit donc jamais à identifier un "
                "alcène : il faut vérifier la présence de la double "
                "liaison C=C."
            )
        ) as tracker:
            self.play(FadeIn(piege))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(piege), FadeOut(titre))
