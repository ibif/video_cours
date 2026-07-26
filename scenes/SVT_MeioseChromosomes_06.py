"""
scenes/SVT_MeioseChromosomes_06.py — Chapitre 2 (1ereC, SVT), scène 06.

§ Le brassage interchromosomique : orientation aléatoire des bivalents en
métaphase I, formule 2^n types de gamètes, exemple résolu 2 (cellule 2n=4,
grande paire P/M + petite paire p/m, les 4 combinaisons possibles),
application à l'Homme (2^23 types de gamètes).
Source : 1ereC/SVT.pdf, pages 17-18.
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
from shapes.boxes import example_box, property_box, scene_title

PATERNEL = "#B5651D"
MATERNEL = "#2E8B57"


def _wrap(text: str, width: int = 56) -> str:
    return "\n".join(textwrap.fill(line, width=width) for line in text.split("\n"))


def _grid_table(cell_matrix, col_gap=0.5, row_gap=0.26):
    n_rows = len(cell_matrix)
    n_cols = len(cell_matrix[0])
    col_widths = [max(cell_matrix[r][c].width for r in range(n_rows)) for c in range(n_cols)]
    row_height = max(cell.height for row in cell_matrix for cell in row)

    col_x = []
    x = 0.0
    for c in range(n_cols):
        col_x.append(x)
        x += col_widths[c] + col_gap

    table = VGroup()
    y = 0.0
    for r in range(n_rows):
        for c in range(n_cols):
            cell = cell_matrix[r][c]
            cell.move_to([col_x[c] + cell.width / 2, y, 0])
            table.add(cell)
        y -= row_height + row_gap
    return table


def _chr_double(color, height=0.9, width=0.16, gap=0.06):
    left = Rectangle(width=width, height=height, fill_color=color, fill_opacity=1, stroke_color=WHITE, stroke_width=1)
    right = left.copy()
    paire = VGroup(left, right).arrange(RIGHT, buff=gap)
    dot = Dot(radius=0.045, color=YELLOW)
    dot.move_to(paire.get_center())
    return VGroup(left, right, dot)


class BrassageInterchromosomique(NotionScene):
    def construct(self):
        titre = scene_title("2.4 — Le brassage interchromosomique")
        titre.scale(0.62)
        titre.to_edge(UP)

        # --- Énoncé : orientation aléatoire des bivalents ------------------------
        enonce = Text(
            _wrap(
                "En métaphase I, l'orientation de chaque paire d'homologues "
                "sur la plaque équatoriale est aléatoire : pour chaque "
                "paire, le chromosome paternel peut migrer vers un pôle ou "
                "vers l'autre, indépendamment des autres paires. En "
                "anaphase I, la séparation se fait donc au hasard.",
                width=56,
            ),
            font_size=22,
            color=WHITE,
        )
        enonce.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "En métaphase I, l'orientation de chaque paire d'homologues "
                "sur la plaque équatoriale est aléatoire : pour chaque "
                "paire, le chromosome d'origine paternelle peut migrer vers "
                "un pôle ou vers l'autre, indépendamment des autres paires. "
                "En anaphase I, la séparation des homologues se fait donc au "
                "hasard : c'est le brassage interchromosomique."
            )
        ) as tracker:
            self.play(Write(titre))
            self.play(FadeIn(enonce))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(enonce))

        # --- Animation du raisonnement : 2 orientations possibles pour 2 paires -
        sous_titre = Text("Deux orientations possibles pour une cellule à 2n=4", font_size=20, color=YELLOW, weight="BOLD")
        sous_titre.next_to(titre, DOWN, buff=0.5)

        def _cellule_orientation(grand_haut, petit_haut):
            cell = Ellipse(width=2.6, height=2.0, color=WHITE, stroke_width=2)
            grand = _chr_double(PATERNEL if grand_haut else MATERNEL, height=0.7)
            grand_bas = _chr_double(MATERNEL if grand_haut else PATERNEL, height=0.7)
            petit = _chr_double(PATERNEL if petit_haut else MATERNEL, height=0.45)
            petit_bas = _chr_double(MATERNEL if petit_haut else PATERNEL, height=0.45)
            haut = VGroup(grand, petit).arrange(RIGHT, buff=0.2)
            bas = VGroup(grand_bas, petit_bas).arrange(RIGHT, buff=0.2)
            haut.move_to(cell.get_center() + UP * 0.5)
            bas.move_to(cell.get_center() + DOWN * 0.5)
            return VGroup(cell, haut, bas)

        orient1 = _cellule_orientation(True, True)
        orient2 = _cellule_orientation(True, False)
        deux_orients = VGroup(orient1, orient2).arrange(RIGHT, buff=1.2)
        deux_orients.next_to(sous_titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Pour une cellule à deux n égale quatre, donc deux paires "
                "d'homologues, deux orientations sont possibles en "
                "métaphase I. Dans la première, les deux chromosomes "
                "paternels se retrouvent du même côté. Dans la seconde, ils "
                "se répartissent chacun d'un côté différent. Chaque "
                "orientation conduit, après anaphase I, à des gamètes de "
                "composition différente."
            )
        ) as tracker:
            self.play(FadeIn(sous_titre))
            self.play(FadeIn(deux_orients))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(sous_titre), FadeOut(deux_orients))

        # --- Propriété : formule 2^n --------------------------------------------
        formule = property_box(
            VGroup(
                Text(
                    "Une cellule à n paires d'homologues peut produire, par\n"
                    "brassage interchromosomique, 2ⁿ types de gamètes différents.",
                    font_size=21,
                ),
                Text(
                    "2n=4 (n=2) → 2² = 4 types    2n=6 (n=3) → 2³ = 8 types",
                    font_size=19,
                    color=YELLOW,
                ),
            ).arrange(DOWN, buff=0.3),
            box_width=12.2,
        )
        formule.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "On en tire une propriété générale : une cellule possédant "
                "n paires de chromosomes homologues peut produire, par "
                "brassage interchromosomique, deux puissance n types de "
                "gamètes différents. Pour une cellule à deux n égale quatre, "
                "soit deux paires, cela donne deux puissance deux, soit "
                "quatre types de gamètes. Pour une cellule à deux n égale "
                "six, soit trois paires, cela donne deux puissance trois, "
                "soit huit types de gamètes."
            )
        ) as tracker:
            self.play(FadeIn(formule))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(formule))

        # --- Exemple résolu 2 : cellule 2n=4, tableau des 4 combinaisons -------
        entete = Text("Exemple résolu 2 — cellule 2n=4 (P/M grande paire, p/m petite paire)", font_size=19, color=YELLOW, weight="BOLD")
        entete.next_to(titre, DOWN, buff=0.5)

        rows = [
            ("Combinaison n°", "Contenu du gamète"),
            ("1", "P + p"),
            ("2", "P + m"),
            ("3", "M + p"),
            ("4", "M + m"),
        ]
        cell_matrix = []
        for i, row in enumerate(rows):
            color = YELLOW if i == 0 else WHITE
            weight = "BOLD" if i == 0 else "NORMAL"
            cell_matrix.append([Text(val, font_size=20, color=color, weight=weight) for val in row])

        tableau = _grid_table(cell_matrix, col_gap=0.8, row_gap=0.24)
        tableau.next_to(entete, DOWN, buff=0.35)

        conclusion = Text("Soit 2² = 4 types de gamètes, avec toujours 1 grand + 1 petit chromosome", font_size=17, color=WHITE)
        conclusion.next_to(tableau, DOWN, buff=0.35)

        with self.voiceover(
            text=(
                "Une cellule possède deux n égale quatre chromosomes : une "
                "grande paire, P pour paternel et M pour maternel, et une "
                "petite paire, p pour paternel et m pour maternel. À "
                "l'anaphase I, chaque cellule fille reçoit un chromosome de "
                "chaque paire. Les combinaisons possibles sont : P plus p, P "
                "plus m, M plus p, et M plus m. Soit deux puissance deux, "
                "quatre types de gamètes. Chaque gamète contient bien un "
                "représentant de chaque paire, toujours un grand et un "
                "petit, mais l'origine, paternelle ou maternelle, varie."
            )
        ) as tracker:
            self.play(FadeIn(entete))
            self.play(FadeIn(tableau))
            self.play(FadeIn(conclusion))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(entete), FadeOut(tableau), FadeOut(conclusion))

        # --- À retenir : application à l'Homme -----------------------------------
        homme = example_box(
            VGroup(
                Text(
                    "Chez l'Homme (n=23 paires) :",
                    font_size=23,
                    color=WHITE,
                ),
                Text(
                    "2²³ = 8 388 608 types de spermatozoïdes\nou d'ovules différents possibles !",
                    font_size=21,
                    color=YELLOW,
                ),
            ).arrange(DOWN, buff=0.3),
            box_width=11.6,
        )
        homme.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Appliquons ceci à l'espèce humaine, qui compte vingt-trois "
                "paires de chromosomes homologues. Le nombre de types de "
                "gamètes possibles, par le seul brassage interchromosomique, "
                "vaut deux puissance vingt-trois, soit huit millions trois "
                "cent quatre-vingt-huit mille six cent huit types de "
                "spermatozoïdes ou d'ovules différents possibles !"
            )
        ) as tracker:
            self.play(FadeIn(homme))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(titre), FadeOut(homme))
