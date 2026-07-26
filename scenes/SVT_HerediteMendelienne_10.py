"""
scenes/SVT_HerediteMendelienne_10.py — Chapitre 6 (1ereC, SVT), scène 10.

§ VI.4 Exemples de transmission (2/2) : la drépanocytose chez l'Homme
(tableau génotype-état-dénomination), Exemple résolu 5 (croisement
AS x AS, échiquier, proportions 1/4-1/2-1/4), et remarque sur la
résistance au paludisme conférée par l'allèle S. Source : 1ereC/SVT.pdf,
page 62.
"""

import textwrap

from manim import (
    DOWN,
    GREY,
    LEFT,
    RIGHT,
    UP,
    WHITE,
    YELLOW,
    Create,
    FadeIn,
    FadeOut,
    MathTex,
    Rectangle,
    Text,
    VGroup,
    Write,
)

from shapes.base_scene import NotionScene
from shapes.boxes import scene_title, warning_box


def _wrap(text: str, width: int = 56) -> str:
    return "\n".join(textwrap.fill(line, width=width) for line in text.split("\n"))


def _bullets(items, font_size=23, color=WHITE, width=54):
    lines = VGroup(
        *[Text(f"• {_wrap(it, width=width)}", font_size=font_size, color=color) for it in items]
    )
    lines.arrange(DOWN, aligned_edge=LEFT, buff=0.22)
    return lines


def _tableau(headers, rows, col_widths=None, row_height=0.85, header_font=19, cell_font=16):
    n_cols = len(headers)
    n_rows = len(rows) + 1
    if col_widths is None:
        col_widths = [3.0] * n_cols

    grid = VGroup()
    row_groups = []
    for r in range(n_rows):
        cells = VGroup(
            *[Rectangle(width=col_widths[c], height=row_height, stroke_color=WHITE, stroke_width=2) for c in range(n_cols)]
        )
        cells.arrange(RIGHT, buff=0)
        row_groups.append(cells)
        grid.add(cells)
    grid.arrange(DOWN, buff=0)

    texts = VGroup()
    for c, h in enumerate(headers):
        t = Text(h, font_size=header_font, color=YELLOW, weight="BOLD")
        t.set(width=min(t.width, col_widths[c] - 0.2))
        t.move_to(row_groups[0][c].get_center())
        texts.add(t)

    for r, row in enumerate(rows):
        for c, cell in enumerate(row):
            t = Text(cell, font_size=cell_font, color=WHITE)
            t.set(width=min(t.width, col_widths[c] - 0.2))
            t.move_to(row_groups[r + 1][c].get_center())
            texts.add(t)

    return VGroup(grid, texts)


def _resultat_as(gc, gr):
    allele1, allele2 = (gc, gr) if gc == "A" else (gr, gc)
    return f"{allele1}{allele2}"


def _echiquier(col_gametes, row_gametes, resultat_fn=_resultat_as, cell_size=1.25, font_size=30):
    n_cols = len(col_gametes)
    n_rows = len(row_gametes)

    grid = VGroup()
    row_groups = []
    for _r in range(n_rows + 1):
        row_rects = VGroup(
            *[Rectangle(width=cell_size, height=cell_size, stroke_color=WHITE, stroke_width=2) for _ in range(n_cols + 1)]
        )
        row_rects.arrange(RIGHT, buff=0)
        row_groups.append(row_rects)
        grid.add(row_rects)
    grid.arrange(DOWN, buff=0)

    corner = MathTex(r"\times", font_size=font_size, color=GREY)
    corner.move_to(row_groups[0][0].get_center())

    col_headers = VGroup()
    for c, g in enumerate(col_gametes):
        h = MathTex(g, font_size=font_size, color=YELLOW)
        h.move_to(row_groups[0][c + 1].get_center())
        col_headers.add(h)

    row_headers = VGroup()
    for r, g in enumerate(row_gametes):
        h = MathTex(g, font_size=font_size, color=YELLOW)
        h.move_to(row_groups[r + 1][0].get_center())
        row_headers.add(h)

    cellules = []
    cellules_group = VGroup()
    for r, gr in enumerate(row_gametes):
        ligne = []
        for c, gc in enumerate(col_gametes):
            m = MathTex(resultat_fn(gc, gr), font_size=font_size - 2, color=WHITE)
            m.move_to(row_groups[r + 1][c + 1].get_center())
            ligne.append(m)
            cellules_group.add(m)
        cellules.append(ligne)

    ensemble = VGroup(grid, corner, col_headers, row_headers, cellules_group)
    return {"grid": grid, "corner": corner, "col_headers": col_headers, "row_headers": row_headers,
            "cellules": cellules, "ensemble": ensemble}


class Drepanocytose(NotionScene):
    def construct(self):
        titre = scene_title("6.10 — La drépanocytose")
        titre.scale(0.75)
        titre.to_edge(UP)

        # --- Énoncé : présentation de la maladie -----------------------------------
        intro = Text(
            _wrap(
                "La drépanocytose est une maladie héréditaire du sang, "
                "fréquente en Afrique de l'Ouest et donc en Côte "
                "d'Ivoire. Elle est due à un allèle anormal S du gène de "
                "l'hémoglobine ; l'allèle normal est noté A.",
                width=56,
            ),
            font_size=24,
            color=WHITE,
        )
        intro.next_to(titre, DOWN, buff=0.55)

        with self.voiceover(
            text=(
                "La drépanocytose est une maladie héréditaire du sang, "
                "fréquente en Afrique de l'Ouest, et donc en Côte "
                "d'Ivoire. Elle est due à un allèle anormal, noté S, du "
                "gène de l'hémoglobine ; l'allèle normal est noté A."
            )
        ) as tracker:
            self.play(Write(titre))
            self.play(FadeIn(intro))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(intro))

        # --- Animation du raisonnement : le tableau génotype-état-dénomination ---
        entete_tab = Text("Génotypes et dénominations", font_size=24, color=YELLOW, weight="BOLD")
        entete_tab.next_to(titre, DOWN, buff=0.5)

        tableau = _tableau(
            headers=["Génotype", "État de santé", "Dénomination"],
            rows=[
                ["AA", "Sain, globules\nnormaux", "Sain"],
                ["AS", "Sain en général,\nporteur de l'allèle", "Porteur sain"],
                ["SS", "Gravement malade,\ncrises douloureuses", "Drépanocytaire"],
            ],
            col_widths=[2.4, 3.6, 2.9],
            row_height=1.0,
        )
        tableau.next_to(entete_tab, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Voici les trois génotypes possibles. Génotype A A : "
                "individu sain, globules rouges normaux, dénommé sain. "
                "Génotype A S : individu sain en général, mais porteur de "
                "l'allèle, dénommé porteur sain, ou porteur du trait "
                "drépanocytaire. Génotype S S : individu gravement "
                "malade, avec anémie sévère et crises douloureuses, "
                "dénommé drépanocytaire."
            )
        ) as tracker:
            self.play(FadeIn(entete_tab))
            self.play(Create(tableau[0]))
            self.play(Write(tableau[1]))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(entete_tab), FadeOut(tableau))

        # --- Exemple traité : exemple résolu 5, croisement AS x AS -----------------
        entete_ex = Text("Exemple résolu 5 : croisement AS x AS", font_size=22, color=YELLOW, weight="BOLD")
        entete_ex.next_to(titre, DOWN, buff=0.5)

        genotypes_5 = MathTex(r"AS \;\times\; AS", font_size=30, color=WHITE)
        genotypes_5.next_to(entete_ex, DOWN, buff=0.35)

        ech5 = _echiquier(["A", "S"], ["A", "S"])
        ech5["ensemble"].next_to(genotypes_5, DOWN, buff=0.55).shift(LEFT * 2.2)

        with self.voiceover(
            text=(
                "Croisons deux porteurs sains, A S et A S. Chaque parent "
                "produit deux sortes de gamètes, A et S, en proportions "
                "égales. Construisons l'échiquier de ce croisement."
            )
        ) as tracker:
            self.play(FadeIn(entete_ex))
            self.play(Write(genotypes_5))
            self.play(Create(ech5["grid"]), FadeIn(ech5["corner"]))
            self.play(Write(ech5["col_headers"]), Write(ech5["row_headers"]))
            self.play(*[Write(c) for l in ech5["cellules"] for c in l])
            self.wait(tracker.get_remaining_duration())

        proportions_5 = VGroup(
            MathTex(r"\tfrac14\,AA \quad \tfrac12\,AS \quad \tfrac14\,SS", font_size=26, color=YELLOW),
            Text("Probabilité d'un enfant atteint (SS) : 1/4", font_size=19, color=WHITE),
        ).arrange(DOWN, buff=0.35)
        proportions_5.next_to(ech5["ensemble"], RIGHT, buff=0.6)

        with self.voiceover(
            text=(
                "On obtient un quart A A, sain ; un demi A S, porteur "
                "sain ; et un quart S S, drépanocytaire. À chaque "
                "naissance, ce couple a donc une probabilité d'un quart "
                "d'avoir un enfant atteint."
            )
        ) as tracker:
            self.play(FadeIn(proportions_5))
            self.wait(tracker.get_remaining_duration())

        self.play(
            FadeOut(entete_ex),
            FadeOut(genotypes_5),
            FadeOut(ech5["ensemble"]),
            FadeOut(proportions_5),
        )

        # --- À retenir : la résistance au paludisme ---------------------------------
        remarque = warning_box(
            Text(
                _wrap(
                    "L'allèle S confère aux porteurs AS une meilleure "
                    "résistance au paludisme. Cet avantage explique la "
                    "fréquence élevée de l'allèle S en Afrique de l'Ouest, "
                    "où le paludisme est endémique (10 à 25% de porteurs "
                    "AS selon les régions).",
                    width=50,
                ),
                font_size=22,
            ),
            box_width=11.3,
        )
        remarque.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Une remarque essentielle pour comprendre pourquoi cet "
                "allèle persiste : l'allèle S confère aux porteurs A S "
                "une meilleure résistance au paludisme. Cet avantage "
                "explique la fréquence élevée de l'allèle S dans les "
                "régions où le paludisme est endémique, comme l'Afrique "
                "de l'Ouest, où une part importante de la population, "
                "souvent estimée entre dix et vingt-cinq pour cent selon "
                "les régions, est porteuse saine, A S."
            )
        ) as tracker:
            self.play(FadeIn(remarque))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(titre), FadeOut(remarque))
