"""
scenes/SVT_HerediteMendelienne_09.py — Chapitre 6 (1ereC, SVT), scène 09.

§ VI.1-VI.3 Exemples de transmission (1/2) : chez les plantes (pois,
maïs), chez les animaux (pelage du cobaye), et les groupes sanguins ABO
chez l'Homme (codominance, 3 allèles, Exemple résolu 4 : croisement
AO x BO). Source : 1ereC/SVT.pdf, pages 61-62.
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
from shapes.boxes import scene_title


def _wrap(text: str, width: int = 56) -> str:
    return "\n".join(textwrap.fill(line, width=width) for line in text.split("\n"))


def _bullets(items, font_size=23, color=WHITE, width=54):
    lines = VGroup(
        *[Text(f"• {_wrap(it, width=width)}", font_size=font_size, color=color) for it in items]
    )
    lines.arrange(DOWN, aligned_edge=LEFT, buff=0.22)
    return lines


def _tableau(headers, rows, col_width=2.9, row_height=0.72, header_font=20, cell_font=18):
    n_cols = len(headers)
    n_rows = len(rows) + 1

    grid = VGroup()
    row_groups = []
    for r in range(n_rows):
        cells = VGroup(
            *[Rectangle(width=col_width, height=row_height, stroke_color=WHITE, stroke_width=2) for _ in range(n_cols)]
        )
        cells.arrange(RIGHT, buff=0)
        row_groups.append(cells)
        grid.add(cells)
    grid.arrange(DOWN, buff=0)

    texts = VGroup()
    for c, h in enumerate(headers):
        t = Text(h, font_size=header_font, color=YELLOW, weight="BOLD")
        t.set(width=min(t.width, col_width - 0.2))
        t.move_to(row_groups[0][c].get_center())
        texts.add(t)

    for r, row in enumerate(rows):
        for c, cell in enumerate(row):
            t = Text(cell, font_size=cell_font, color=WHITE)
            t.set(width=min(t.width, col_width - 0.2))
            t.move_to(row_groups[r + 1][c].get_center())
            texts.add(t)

    return VGroup(grid, texts)


def _echiquier(col_gametes, row_gametes, resultat_fn, cell_size=1.2, font_size=28):
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
            m = MathTex(resultat_fn(gc, gr), font_size=font_size - 4, color=WHITE)
            m.move_to(row_groups[r + 1][c + 1].get_center())
            ligne.append(m)
            cellules_group.add(m)
        cellules.append(ligne)

    ensemble = VGroup(grid, corner, col_headers, row_headers, cellules_group)
    return {"grid": grid, "corner": corner, "col_headers": col_headers, "row_headers": row_headers,
            "cellules": cellules, "ensemble": ensemble}


class ExemplesTransmission1(NotionScene):
    def construct(self):
        titre = scene_title("6.9 — Exemples de transmission (1/2)")
        titre.scale(0.68)
        titre.to_edge(UP)

        # --- Énoncé : chez les plantes ---------------------------------------------
        entete_plantes = Text("Chez les plantes", font_size=25, color=YELLOW, weight="BOLD")
        entete_plantes.next_to(titre, DOWN, buff=0.5)

        plantes = _bullets(
            [
                "Pois : la couleur des fleurs obéit aux mêmes lois : "
                "l'allèle « fleurs violettes » (V) domine l'allèle "
                "« fleurs blanches » (v). En F2, Mendel obtient 705 "
                "fleurs violettes et 224 blanches, soit environ 3,15 "
                "pour 1, proche de 3/4 - 1/4.",
                "Maïs : la couleur des grains (pourpres ou jaunes) se "
                "transmet de la même façon ; base de la sélection des "
                "variétés cultivées en Côte d'Ivoire.",
            ],
            font_size=22,
            width=54,
        )
        plantes.next_to(entete_plantes, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Voyons maintenant d'autres exemples de transmission. "
                "Chez le pois, la couleur des fleurs obéit aux mêmes "
                "lois : l'allèle fleurs violettes domine l'allèle fleurs "
                "blanches. En F deux, Mendel obtint sept cent cinq fleurs "
                "violettes et deux cent vingt-quatre blanches, soit un "
                "rapport d'environ trois virgule quinze pour un, très "
                "proche de trois quarts, un quart. Chez le maïs, la "
                "couleur des grains, pourpres ou jaunes, se transmet de "
                "la même façon : c'est la base de la sélection des "
                "variétés cultivées en Côte d'Ivoire."
            )
        ) as tracker:
            self.play(Write(titre))
            self.play(FadeIn(entete_plantes))
            self.play(FadeIn(plantes))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(entete_plantes), FadeOut(plantes))

        # --- Animation du raisonnement : chez les animaux ---------------------------
        entete_animaux = Text("Chez les animaux : le cobaye", font_size=25, color=YELLOW, weight="BOLD")
        entete_animaux.next_to(titre, DOWN, buff=0.5)

        animaux = Text(
            _wrap(
                "Chez le cobaye, l'allèle « pelage noir » (N) domine "
                "l'allèle « pelage blanc » (n). Un mâle noir peut être "
                "NN ou Nn : seul un test-cross avec une femelle blanche "
                "(nn) permet de trancher.",
                width=52,
            ),
            font_size=23,
        )
        animaux.next_to(entete_animaux, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Chez le cobaye, le cochon d'Inde, l'allèle pelage noir "
                "domine l'allèle pelage blanc. Un éleveur peut donc se "
                "demander si un mâle noir est de race pure, N N, ou "
                "hybride, N n : seul un test-cross avec une femelle "
                "blanche, n n, permet de répondre, exactement comme nous "
                "venons de le voir."
            )
        ) as tracker:
            self.play(FadeIn(entete_animaux))
            self.play(FadeIn(animaux))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(entete_animaux), FadeOut(animaux))

        # --- Exemple traité : les groupes sanguins ABO ------------------------------
        entete_abo = Text("Chez l'Homme : les groupes sanguins ABO", font_size=22, color=YELLOW, weight="BOLD")
        entete_abo.next_to(titre, DOWN, buff=0.5)

        abo_texte = Text(
            _wrap(
                "Le groupe sanguin est commandé par un gène à 3 allèles : "
                "A, B et O. A et B sont codominants (s'expriment "
                "ensemble). O est récessif par rapport à A et B.",
                width=54,
            ),
            font_size=21,
        )
        abo_texte.next_to(entete_abo, DOWN, buff=0.35)

        tab_abo = _tableau(
            headers=["Groupe", "Génotypes"],
            rows=[["[A]", "AA ou AO"], ["[B]", "BB ou BO"], ["[AB]", "AB"], ["[O]", "OO"]],
            col_width=2.6,
            row_height=0.62,
        )
        tab_abo.next_to(abo_texte, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Chez l'Homme, le groupe sanguin est commandé par un gène "
                "qui existe sous trois allèles : A, B et O. Les allèles A "
                "et B sont codominants, ils s'expriment tous les deux "
                "chez un individu A B ; l'allèle O est récessif par "
                "rapport à A et à B. Voici les correspondances : le "
                "groupe A correspond au génotype A A ou A O ; le groupe B "
                "correspond à B B ou B O ; le groupe A B correspond "
                "uniquement au génotype A B ; le groupe O correspond "
                "uniquement au génotype O O."
            )
        ) as tracker:
            self.play(FadeIn(entete_abo))
            self.play(FadeIn(abo_texte))
            self.play(Create(tab_abo[0]))
            self.play(Write(tab_abo[1]))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(entete_abo), FadeOut(abo_texte), FadeOut(tab_abo))

        # --- Exemple résolu 4 : croisement AO x BO ----------------------------------
        entete_ex4 = Text("Exemple résolu 4 : croisement AO x BO", font_size=22, color=YELLOW, weight="BOLD")
        entete_ex4.next_to(titre, DOWN, buff=0.5)

        genotypes_4 = MathTex(r"AO \;\times\; BO", font_size=30, color=WHITE)
        genotypes_4.next_to(entete_ex4, DOWN, buff=0.35)

        def resultat_abo(gc, gr):
            allele1 = gc  # colonnes = homme A/O
            allele2 = gr  # lignes = femme B/O
            return f"{allele1}{allele2}"

        ech4 = _echiquier(["A", "O"], ["B", "O"], resultat_abo, cell_size=1.15)
        ech4["ensemble"].next_to(genotypes_4, DOWN, buff=0.5).shift(LEFT * 2.4)

        label_h = Text("Gamètes de l'homme (A, O)", font_size=16, color=YELLOW)
        label_h.next_to(ech4["col_headers"], UP, buff=0.2)
        label_f = Text("Gamètes\nde la femme\n(B, O)", font_size=15, color=YELLOW)
        label_f.next_to(ech4["row_headers"], LEFT, buff=0.3)

        with self.voiceover(
            text=(
                "Croisons un homme de groupe A, génotype A O, avec une "
                "femme de groupe B, génotype B O. L'homme produit des "
                "gamètes A et des gamètes O ; la femme produit des "
                "gamètes B et des gamètes O."
            )
        ) as tracker:
            self.play(FadeIn(entete_ex4))
            self.play(Write(genotypes_4))
            self.play(Create(ech4["grid"]), FadeIn(ech4["corner"]))
            self.play(FadeIn(label_h), Write(ech4["col_headers"]))
            self.play(FadeIn(label_f), Write(ech4["row_headers"]))
            self.play(*[Write(c) for l in ech4["cellules"] for c in l])
            self.wait(tracker.get_remaining_duration())

        resultat_4 = MathTex(
            r"\tfrac14[AB]\;\; \tfrac14[B]\;\; \tfrac14[A]\;\; \tfrac14[O]",
            font_size=24,
            color=YELLOW,
        )
        resultat_4.next_to(ech4["ensemble"], RIGHT, buff=0.6)

        with self.voiceover(
            text=(
                "Les quatre cases de l'échiquier donnent : A B, B O, A O "
                "et O O. Les enfants peuvent donc être, chacun avec une "
                "chance sur quatre : de groupe A B, de groupe B, de "
                "groupe A, ou de groupe O. Tous les groupes sanguins sont "
                "donc possibles pour ce couple, ce qui surprend souvent, "
                "et illustre bien la richesse du système à trois allèles."
            )
        ) as tracker:
            self.play(FadeIn(resultat_4))
            self.wait(tracker.get_remaining_duration())

        self.play(
            FadeOut(titre),
            FadeOut(entete_ex4),
            FadeOut(genotypes_4),
            FadeOut(ech4["ensemble"]),
            FadeOut(label_h),
            FadeOut(label_f),
            FadeOut(resultat_4),
        )
