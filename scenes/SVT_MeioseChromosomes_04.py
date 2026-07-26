"""
scenes/SVT_MeioseChromosomes_04.py — Chapitre 2 (1ereC, SVT), scène 04.

§ Métaphase I -> Anaphase I -> Télophase I (disposition aléatoire des
bivalents, disjonction des homologues = étape réductionnelle, 2 cellules
filles haploïdes à 2 chromatides) + Exemple résolu 1 (tableau
chromosomes/chromatides/quantité d'ADN, cellule 2n=8, Q=10pg).
Source : 1ereC/SVT.pdf, pages 15-16.
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
    config,
)

from shapes.base_scene import NotionScene
from shapes.boxes import example_box, scene_title

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


def _chromosome_2_chromatides(color=WHITE, height=1.0, width=0.18, gap=0.07):
    gauche = Rectangle(width=width, height=height, fill_color=color, fill_opacity=1, stroke_color=WHITE, stroke_width=1)
    droite = gauche.copy()
    paire = VGroup(gauche, droite).arrange(RIGHT, buff=gap)
    centromere = Dot(radius=0.05, color=YELLOW)
    centromere.move_to(paire.get_center())
    return VGroup(gauche, droite, centromere)


class MetaphaseAnaphaseTelophaseI(NotionScene):
    def construct(self):
        titre = scene_title("2.2 — Métaphase I, anaphase I, télophase I")
        titre.scale(0.6)
        titre.to_edge(UP)

        # --- Énoncé : métaphase I -------------------------------------------
        metaphase_txt = Text(
            _wrap(
                "Métaphase I : les bivalents se disposent sur la plaque "
                "équatoriale. L'orientation de chaque paire est strictement "
                "ALÉATOIRE : le chromosome paternel peut être dirigé vers "
                "un pôle comme vers l'autre, indépendamment des autres "
                "paires — base du brassage interchromosomique.",
                width=56,
            ),
            font_size=22,
            color=WHITE,
        )
        metaphase_txt.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "En métaphase I, les bivalents se disposent sur la plaque "
                "équatoriale de la cellule. L'orientation de chaque paire "
                "est strictement aléatoire : le chromosome d'origine "
                "paternelle peut être dirigé vers un pôle comme vers "
                "l'autre, indépendamment des autres paires. C'est la base "
                "du brassage interchromosomique, que nous détaillerons plus "
                "loin."
            )
        ) as tracker:
            self.play(Write(titre))
            self.play(FadeIn(metaphase_txt))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(metaphase_txt))

        # --- Animation du raisonnement : bivalents -> anaphase I -> télophase I -
        cellule = Ellipse(width=5.5, height=3.0, color=WHITE, stroke_width=2)
        cellule.next_to(titre, DOWN, buff=0.7)
        plaque = Rectangle(width=0.03, height=2.8, color=YELLOW, stroke_width=1)
        plaque.move_to(cellule.get_center())

        biv1 = VGroup(_chromosome_2_chromatides(PATERNEL, height=0.9), _chromosome_2_chromatides(MATERNEL, height=0.9)).arrange(RIGHT, buff=0.05)
        biv2 = VGroup(_chromosome_2_chromatides(PATERNEL, height=0.6), _chromosome_2_chromatides(MATERNEL, height=0.6)).arrange(RIGHT, buff=0.05)
        biv1.move_to(cellule.get_center() + UP * 0.5)
        biv2.move_to(cellule.get_center() + DOWN * 0.5)

        label_meta = Text("2 bivalents alignés sur la plaque équatoriale", font_size=16, color=WHITE)
        label_meta.next_to(cellule, DOWN, buff=0.3)

        with self.voiceover(
            text=(
                "Prenons une cellule à deux n égale quatre, soit deux "
                "bivalents. Les voici alignés sur la plaque équatoriale, "
                "chacun formé d'un chromosome paternel, en rouille, et d'un "
                "chromosome maternel, en vert."
            )
        ) as tracker:
            self.play(FadeIn(cellule), FadeIn(plaque))
            self.play(FadeIn(biv1), FadeIn(biv2))
            self.play(FadeIn(label_meta))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(label_meta))

        # Anaphase I : disjonction des homologues
        label_ana = Text("Anaphase I : disjonction des homologues (réductionnelle)", font_size=16, color=WHITE)
        label_ana.next_to(cellule, DOWN, buff=0.3)

        with self.voiceover(
            text=(
                "En anaphase I, les chromosomes homologues se séparent : "
                "c'est la disjonction. Ils migrent vers les pôles opposés. "
                "Les centromères ne se divisent pas : chaque chromosome qui "
                "migre reste formé de deux chromatides. À chaque pôle, il "
                "n'y a donc plus qu'un seul chromosome de chaque paire "
                "initiale : c'est l'étape réductionnelle."
            )
        ) as tracker:
            self.play(
                biv1[0].animate.shift(UP * 1.0 + LEFT * 0.3),
                biv1[1].animate.shift(DOWN * 1.0 + LEFT * 0.3),
                biv2[0].animate.shift(UP * 1.0 + RIGHT * 0.3),
                biv2[1].animate.shift(DOWN * 1.0 + RIGHT * 0.3),
            )
            self.play(FadeIn(label_ana))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(label_ana))

        # Télophase I : 2 cellules haploïdes
        cell_haut = Ellipse(width=3.0, height=1.7, color=WHITE, stroke_width=2)
        cell_bas = Ellipse(width=3.0, height=1.7, color=WHITE, stroke_width=2)
        contenu_haut = VGroup(biv1[0], biv2[0])
        contenu_bas = VGroup(biv1[1], biv2[1])
        groupe_final = VGroup(cell_haut, cell_bas).arrange(DOWN, buff=0.4)
        groupe_final.move_to(cellule.get_center())

        label_telo = Text("Télophase I : 2 cellules filles haploïdes,\nchromosomes encore à 2 chromatides", font_size=16, color=WHITE)
        label_telo.next_to(groupe_final, DOWN, buff=0.35)

        with self.voiceover(
            text=(
                "En télophase I, les chromosomes arrivent aux pôles ; le "
                "cytoplasme se divise. On obtient deux cellules filles "
                "haploïdes, dont les chromosomes sont encore à deux "
                "chromatides. S'ensuit une très courte intercinèse, sans "
                "aucune réplication d'ADN."
            )
        ) as tracker:
            self.play(FadeOut(cellule), FadeOut(plaque), FadeIn(cell_haut), FadeIn(cell_bas))
            self.play(contenu_haut.animate.move_to(cell_haut.get_center()), contenu_bas.animate.move_to(cell_bas.get_center()))
            self.play(FadeIn(label_telo))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(groupe_final), FadeOut(contenu_haut), FadeOut(contenu_bas), FadeOut(label_telo))

        # --- Exemple traité : tableau chiffré (2n=8, Q=10pg) --------------------
        entete = Text("Exemple résolu 1 — cellule 2n=8, Q=10 pg", font_size=24, color=YELLOW, weight="BOLD")
        entete.next_to(titre, DOWN, buff=0.5)

        rows = [
            ("Étape", "Chr./cellule", "Chromat./chr.", "Total chromat.", "ADN"),
            ("Avant interphase", "8", "1", "8", "Q=10pg"),
            ("Fin d'interphase", "8", "2", "16", "2Q=20pg"),
            ("Métaphase I", "8", "2", "16", "2Q=20pg"),
            ("Fin méiose I (par cellule)", "4", "2", "8", "Q=10pg"),
            ("Métaphase II", "4", "2", "8", "Q=10pg"),
            ("Anaphase II (par cellule)", "8", "1", "8", "Q=10pg"),
            ("Fin méiose II (par cellule)", "4", "1", "4", "Q/2=5pg"),
        ]
        cell_matrix = []
        for i, row in enumerate(rows):
            color = YELLOW if i == 0 else WHITE
            weight = "BOLD" if i == 0 else "NORMAL"
            cell_matrix.append([Text(val, font_size=16, color=color, weight=weight) for val in row])

        tableau = _grid_table(cell_matrix, col_gap=0.45, row_gap=0.22)
        tableau.next_to(entete, DOWN, buff=0.35)

        # Garde-fou auto-scale : le tableau (8 lignes) peut dépasser la
        # hauteur visible ; on réduit alors l'échelle globale pour qu'il
        # tienne entièrement à l'écran (technique de SVT_FonctionsGonades_09.py).
        _bas_visible = -config.frame_height / 2 + 0.3
        _hauteur_dispo = tableau.get_top()[1] - _bas_visible
        if tableau.height > _hauteur_dispo:
            tableau.scale(_hauteur_dispo / tableau.height, about_point=tableau.get_top())

        with self.voiceover(
            text=(
                "Appliquons tout cela à un exemple chiffré. On suit une "
                "cellule animale à deux n égale huit chromosomes, dont la "
                "quantité d'ADN avant réplication vaut Q égale dix "
                "picogrammes. Avant l'interphase : huit chromosomes simples, "
                "Q. Fin d'interphase : huit chromosomes à deux chromatides, "
                "deux Q. En métaphase I, rien ne change encore. À la fin de "
                "la méiose I, chaque cellule fille a quatre chromosomes, "
                "toujours à deux chromatides, et retombe à Q. En métaphase "
                "II, pas de changement. En anaphase II, les centromères se "
                "divisent : chaque cellule a de nouveau huit chromatides "
                "simples réparties vers les deux pôles, mais toujours Q. À "
                "la fin de la méiose II, chaque cellule finale a quatre "
                "chromosomes simples, pour une quantité d'ADN de Q sur deux, "
                "soit cinq picogrammes."
            )
        ) as tracker:
            self.play(FadeIn(entete))
            self.play(FadeIn(tableau))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(entete), FadeOut(tableau))

        # --- À retenir : justification synthétique ------------------------------
        justification = example_box(
            Text(
                _wrap(
                    "La réplication double l'ADN (Q→2Q) sans changer le "
                    "nombre de centromères. La méiose I répartit les "
                    "homologues dans 2 cellules (2Q→Q par cellule, 8→4 "
                    "chromosomes). La méiose II sépare les chromatides "
                    "(Q→Q/2, les chromosomes passent à 1 chromatide).",
                    width=54,
                ),
                font_size=21,
            ),
            box_width=12.2,
        )
        justification.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Retenons la logique : la réplication double l'ADN, de Q à "
                "deux Q, sans changer le nombre de centromères. La méiose I "
                "répartit les chromosomes homologues dans deux cellules, "
                "faisant retomber l'ADN de deux Q à Q par cellule, et le "
                "nombre de chromosomes de huit à quatre. La méiose II, "
                "enfin, sépare les chromatides sœurs : l'ADN passe de Q à Q "
                "sur deux, et les chromosomes passent à une seule "
                "chromatide."
            )
        ) as tracker:
            self.play(FadeIn(justification))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(titre), FadeOut(justification))
