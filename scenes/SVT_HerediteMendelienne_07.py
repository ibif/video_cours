"""
scenes/SVT_HerediteMendelienne_07.py — Chapitre 6 (1ereC, SVT), scène 07.

§ IV. L'échiquier de croisement : méthode de construction en 4 étapes,
Exemple résolu 1 (Ll x Ll, tableau complet), Exemple résolu 2
(LL x ll, F1 100% Ll), remarque sur les proportions-probabilités.
Source : 1ereC/SVT.pdf, pages 60-61.
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
from shapes.boxes import method_box, scene_title, warning_box


def _wrap(text: str, width: int = 56) -> str:
    return "\n".join(textwrap.fill(line, width=width) for line in text.split("\n"))


def _bullets(items, font_size=23, color=WHITE, width=54):
    lines = VGroup(
        *[Text(f"• {_wrap(it, width=width)}", font_size=font_size, color=color) for it in items]
    )
    lines.arrange(DOWN, aligned_edge=LEFT, buff=0.22)
    return lines


def _echiquier(col_gametes, row_gametes, resultat_fn, cell_size=1.25, font_size=30):
    """Grille Rectangle + MathTex pour un échiquier de croisement (Punnett)."""
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
    return {
        "grid": grid,
        "corner": corner,
        "col_headers": col_headers,
        "row_headers": row_headers,
        "cellules": cellules,
        "ensemble": ensemble,
    }


def _resultat_pois(gc, gr):
    allele1, allele2 = (gc, gr) if gc == "L" else (gr, gc)
    return f"{allele1}{allele2}"


class EchiquierDeCroisement(NotionScene):
    def construct(self):
        titre = scene_title("6.7 — L'échiquier de croisement")
        titre.scale(0.7)
        titre.to_edge(UP)

        # --- Énoncé : la méthode en 4 étapes --------------------------------------
        methode = method_box(
            Text(
                _wrap(
                    "1. Écrire les génotypes des parents et déterminer "
                    "leurs gamètes (un seul allèle par gamète).\n"
                    "2. Placer les gamètes d'un parent en tête de "
                    "colonne, ceux de l'autre en tête de ligne.\n"
                    "3. Remplir chaque case en réunissant les deux "
                    "allèles : ce sont les génotypes possibles des "
                    "descendants, tous équiprobables.\n"
                    "4. Regrouper les génotypes par phénotype pour "
                    "obtenir les proportions phénotypiques.",
                    width=54,
                ),
                font_size=21,
            ),
            box_width=12.2,
        )
        methode.next_to(titre, DOWN, buff=0.45)

        with self.voiceover(
            text=(
                "L'échiquier de croisement, aussi appelé tableau de "
                "Punnett, est un tableau à double entrée qui permet de "
                "prévoir toutes les combinaisons possibles de la "
                "fécondation, en quatre étapes. Un : on écrit les "
                "génotypes des parents et on détermine leurs gamètes, un "
                "seul allèle par gamète. Deux : on place les gamètes d'un "
                "parent en tête de colonne, ceux de l'autre parent en "
                "tête de ligne. Trois : on remplit chaque case en "
                "réunissant les deux allèles correspondants, ce qui donne "
                "les génotypes possibles des descendants, tous "
                "équiprobables. Quatre : on regroupe les génotypes par "
                "phénotype pour obtenir les proportions phénotypiques."
            )
        ) as tracker:
            self.play(Write(titre))
            self.play(FadeIn(methode))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(methode))

        # --- Animation du raisonnement : exemple résolu 1 (Ll x Ll) --------------
        entete_1 = Text("Exemple résolu 1 : croisement Ll x Ll", font_size=24, color=YELLOW, weight="BOLD")
        entete_1.next_to(titre, DOWN, buff=0.5)

        genotypes_1 = MathTex(r"Ll \;\times\; Ll", font_size=32, color=WHITE)
        genotypes_1.next_to(entete_1, DOWN, buff=0.35)

        ech1 = _echiquier(["L", "l"], ["L", "l"], _resultat_pois)
        ech1["ensemble"].next_to(genotypes_1, DOWN, buff=0.55).shift(LEFT * 2.5)

        label_p1 = Text("Gamètes parent 1", font_size=17, color=YELLOW)
        label_p1.next_to(ech1["col_headers"], UP, buff=0.2)
        label_p2 = Text("Gamètes\nparent 2", font_size=17, color=YELLOW)
        label_p2.next_to(ech1["row_headers"], LEFT, buff=0.3)

        with self.voiceover(
            text=(
                "Prenons l'exemple résolu du croisement de deux hybrides, "
                "L l croisé avec L l, exactement le croisement des F un "
                "entre eux. Chaque parent produit des gamètes L et des "
                "gamètes l en proportions égales. Construisons "
                "l'échiquier : gamètes du premier parent en colonnes, "
                "gamètes du second parent en lignes."
            )
        ) as tracker:
            self.play(FadeIn(entete_1))
            self.play(Write(genotypes_1))
            self.play(Create(ech1["grid"]))
            self.play(FadeIn(ech1["corner"]))
            self.play(FadeIn(label_p1), Write(ech1["col_headers"]))
            self.play(FadeIn(label_p2), Write(ech1["row_headers"]))
            self.wait(tracker.get_remaining_duration())

        with self.voiceover(
            text=(
                "Remplissons chaque case : L rencontre L donne L L ; l "
                "rencontre L donne L l ; L rencontre l donne L l ; l "
                "rencontre l donne l l."
            )
        ) as tracker:
            for ligne in ech1["cellules"]:
                self.play(*[Write(cell) for cell in ligne])
            self.wait(tracker.get_remaining_duration())

        proportions_1 = VGroup(
            MathTex(r"\dfrac{1}{4}LL \quad \dfrac{1}{2}Ll \quad \dfrac{1}{4}ll", font_size=26, color=YELLOW),
            MathTex(r"\dfrac{3}{4}[L] \quad \dfrac{1}{4}[l]", font_size=28, color=WHITE),
        ).arrange(DOWN, buff=0.35)
        proportions_1.next_to(ech1["ensemble"], RIGHT, buff=0.7)

        with self.voiceover(
            text=(
                "On obtient donc, en proportions génotypiques, un quart "
                "L L, deux quarts, soit un demi, L l, et un quart l l. En "
                "proportions phénotypiques : L L et L l donnent tous les "
                "deux crochet L, donc trois quarts de phénotype lisse, et "
                "l l donne crochet l, donc un quart de phénotype ridée. "
                "On retrouve exactement les chiffres de la deuxième loi "
                "de Mendel."
            )
        ) as tracker:
            self.play(FadeIn(proportions_1))
            self.wait(tracker.get_remaining_duration())

        self.play(
            FadeOut(entete_1),
            FadeOut(genotypes_1),
            FadeOut(ech1["ensemble"]),
            FadeOut(label_p1),
            FadeOut(label_p2),
            FadeOut(proportions_1),
        )

        # --- Exemple traité : exemple résolu 2 (LL x ll) --------------------------
        entete_2 = Text("Exemple résolu 2 : croisement LL x ll", font_size=24, color=YELLOW, weight="BOLD")
        entete_2.next_to(titre, DOWN, buff=0.5)

        genotypes_2 = MathTex(r"LL \;\times\; ll", font_size=32, color=WHITE)
        genotypes_2.next_to(entete_2, DOWN, buff=0.35)

        ech2 = _echiquier(["L"], ["l"], _resultat_pois, cell_size=1.4)
        ech2["ensemble"].next_to(genotypes_2, DOWN, buff=0.55)

        conclusion_2 = MathTex(r"F_1 : 100\%\; Ll,\; \text{tous}\; [L]", font_size=28, color=YELLOW)
        conclusion_2.next_to(ech2["ensemble"], DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Second exemple : le croisement de deux lignées pures, L "
                "L croisé avec l l. Le parent L L ne produit que des "
                "gamètes L ; le parent l l ne produit que des gamètes l. "
                "Un seul type de case est donc possible : L l. La F un "
                "est donc cent pour cent L l, de phénotype crochet L : on "
                "retrouve ainsi, par l'échiquier, la loi d'uniformité de "
                "la F un vue précédemment."
            )
        ) as tracker:
            self.play(FadeIn(entete_2))
            self.play(Write(genotypes_2))
            self.play(Create(ech2["grid"]))
            self.play(FadeIn(ech2["corner"]))
            self.play(Write(ech2["col_headers"]), Write(ech2["row_headers"]))
            self.play(*[Write(cell) for ligne in ech2["cellules"] for cell in ligne])
            self.play(Write(conclusion_2))
            self.wait(tracker.get_remaining_duration())

        self.play(
            FadeOut(entete_2),
            FadeOut(genotypes_2),
            FadeOut(ech2["ensemble"]),
            FadeOut(conclusion_2),
        )

        # --- À retenir : remarque sur les proportions-probabilités ---------------
        remarque = warning_box(
            Text(
                _wrap(
                    "Les proportions théoriques (3/4-1/4, 1/2-1/2) sont "
                    "des probabilités : elles ne sont vérifiées que sur un "
                    "grand nombre de descendants. Sur une petite portée, "
                    "les effectifs réels peuvent s'écarter des "
                    "proportions par le seul effet du hasard.",
                    width=50,
                ),
                font_size=22,
            ),
            box_width=11.3,
        )
        remarque.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Une remarque importante pour conclure : les proportions "
                "théoriques, trois quarts, un quart, ou un demi, un demi, "
                "sont des probabilités. Elles ne sont vérifiées que sur "
                "un grand nombre de descendants, comme les milliers de "
                "graines comptées par Mendel. Sur une petite portée, les "
                "effectifs réels peuvent s'écarter de ces proportions, "
                "simplement par l'effet du hasard."
            )
        ) as tracker:
            self.play(FadeIn(remarque))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(titre), FadeOut(remarque))
