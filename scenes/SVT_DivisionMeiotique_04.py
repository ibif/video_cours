"""
scenes/SVT_DivisionMeiotique_04.py — Chapitre 2 (1ereD, SVT), scène 04.

§ 2.2.3-2.2.4 Intercinèse + deuxième division, équationnelle (prophase II
à télophase II - séparation des chromatides sœurs), bilan chiffré (tableau
des effectifs, quantité d'ADN), exemple de l'insecte 2n=6, les 3 pièges de
la méiose, méthode de reconnaissance d'une étape sur un document.
Source : 1ereD/SVT.pdf, pages 21-23.
"""

import textwrap

from manim import (
    BLUE,
    DOWN,
    LEFT,
    MAROON,
    RIGHT,
    UP,
    WHITE,
    YELLOW,
    Dot,
    Ellipse,
    FadeIn,
    FadeOut,
    MathTex,
    Rectangle,
    Text,
    VGroup,
    Write,
)

from shapes.base_scene import NotionScene
from shapes.boxes import example_box, method_box, scene_title, warning_box


def _wrap(text: str, width: int = 56) -> str:
    return "\n".join(textwrap.fill(line, width=width) for line in text.split("\n"))


def _bullets(items, font_size=21, color=WHITE, width=52):
    lines = VGroup(
        *[Text(f"• {_wrap(it, width=width)}", font_size=font_size, color=color) for it in items]
    )
    lines.arrange(DOWN, aligned_edge=LEFT, buff=0.22)
    return lines


def _grid_table(cell_matrix, col_gap=0.55, row_gap=0.28):
    """
    Tableau à partir d'une matrice de Mobjects, avec une hauteur de ligne
    COMMUNE à tout le tableau (y fixe par ligne), pour éviter le décalage
    vertical cumulatif qu'un simple VGroup(*colonnes).arrange(...) par
    colonne indépendante peut produire (colonnes de hauteurs légèrement
    différentes selon le contenu).
    """
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


def _chr_double(color, height=1.0, width=0.18, gap=0.06):
    left = Rectangle(width=width, height=height, fill_color=color, fill_opacity=1, stroke_color=WHITE, stroke_width=1)
    right = left.copy()
    paire = VGroup(left, right).arrange(RIGHT, buff=gap)
    dot = Dot(radius=0.045, color=YELLOW)
    dot.move_to(paire.get_center())
    return VGroup(left, right, dot)


def _chr_simple(color, height=1.0, width=0.18):
    rect = Rectangle(width=width, height=height, fill_color=color, fill_opacity=1, stroke_color=WHITE, stroke_width=1)
    dot = Dot(radius=0.045, color=YELLOW)
    dot.move_to(rect.get_center())
    return VGroup(rect, dot)


class DeuxiemeDivisionEtBilanChiffre(NotionScene):
    def construct(self):
        titre = scene_title("2.2 — 2ème division et bilan chiffré")
        titre.scale(0.62)
        titre.to_edge(UP)

        # --- Énoncé : intercinèse + 2e division -------------------------------
        intercinese = Text(
            _wrap(
                "Entre les deux divisions, courte pause : l'intercinèse. "
                "AUCUNE réplication de l'ADN ne s'y produit. Puis chaque "
                "cellule se divise à nouveau, comme dans une mitose : c'est "
                "la division ÉQUATIONNELLE, car elle ne change pas le nombre "
                "de chromosomes.",
                width=56,
            ),
            font_size=24,
            color=WHITE,
        )
        intercinese.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Entre les deux divisions, la cellule marque une courte pause "
                "appelée intercinèse. Il n'y a pas de réplication de l'ADN "
                "pendant cette pause. Puis chacune des deux cellules se "
                "divise à nouveau, exactement comme dans une mitose : on dit "
                "que cette division est équationnelle, car elle ne change pas "
                "le nombre de chromosomes."
            )
        ) as tracker:
            self.play(Write(titre))
            self.play(FadeIn(intercinese))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(intercinese))

        # --- Animation du raisonnement : schéma P II -> T II ------------------
        sous_titre = Text("2ème division = division ÉQUATIONNELLE", font_size=24, color=YELLOW, weight="BOLD")
        sous_titre.next_to(titre, DOWN, buff=0.45)

        cell_haut = Ellipse(width=3.2, height=1.9, color=WHITE, stroke_width=2)
        cell_bas = Ellipse(width=3.2, height=1.9, color=WHITE, stroke_width=2)
        cell_haut.next_to(sous_titre, DOWN, buff=1.05).shift(UP * 1.0)
        cell_bas.next_to(sous_titre, DOWN, buff=1.05).shift(DOWN * 1.0)

        long_h = _chr_double(BLUE, height=0.9)
        court_h = _chr_double(BLUE, height=0.55)
        grp_haut = VGroup(long_h, court_h).arrange(RIGHT, buff=0.25).move_to(cell_haut.get_center())

        long_b = _chr_double(MAROON, height=0.9)
        court_b = _chr_double(MAROON, height=0.55)
        grp_bas = VGroup(long_b, court_b).arrange(RIGHT, buff=0.25).move_to(cell_bas.get_center())

        label_p2 = Text("Prophase II : recondensation, chromosomes toujours dédoublés", font_size=16, color=WHITE)
        label_p2.next_to(cell_bas, DOWN, buff=0.3)

        with self.voiceover(
            text=(
                "Prophase II. Dans chacune des deux cellules issues de la "
                "première division, les chromosomes, toujours dédoublés, se "
                "recondensent ; la membrane nucléaire disparaît de nouveau."
            )
        ) as tracker:
            self.play(FadeIn(sous_titre))
            self.play(FadeIn(cell_haut), FadeIn(cell_bas))
            self.play(FadeIn(grp_haut), FadeIn(grp_bas))
            self.play(FadeIn(label_p2))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(label_p2))

        label_m2 = Text("Métaphase II : alignement dans chaque cellule", font_size=17, color=WHITE)
        label_m2.next_to(cell_bas, DOWN, buff=0.3)
        with self.voiceover(text="Métaphase II. Dans chaque cellule, les chromosomes se rangent sur le plan équatorial.") as tracker:
            self.play(FadeIn(label_m2))
            self.wait(tracker.get_remaining_duration())
        self.play(FadeOut(label_m2))

        # Anaphase II : scission des centromères -> chromatides séparées (simples)
        label_a2 = Text(
            "Anaphase II : les CENTROMÈRES se scindent,\nles chromatides sœurs se séparent",
            font_size=17,
            color=WHITE,
        )
        label_a2.next_to(cell_bas, DOWN, buff=0.3)

        with self.voiceover(
            text=(
                "Anaphase II. Cette fois, les centromères se scindent : les "
                "deux chromatides sœurs de chaque chromosome se séparent et "
                "migrent vers les pôles opposés. Chaque chromatide devient "
                "alors un chromosome simple, à une seule chromatide."
            )
        ) as tracker:
            self.play(
                FadeOut(long_h[2]), FadeOut(court_h[2]), FadeOut(long_b[2]), FadeOut(court_b[2]),
                long_h[0].animate.shift(UP * 0.18 + LEFT * 0.15),
                long_h[1].animate.shift(DOWN * 0.18 + RIGHT * 0.15),
                court_h[0].animate.shift(UP * 0.18 + LEFT * 0.08),
                court_h[1].animate.shift(DOWN * 0.18 + RIGHT * 0.08),
                long_b[0].animate.shift(UP * 0.18 + LEFT * 0.15),
                long_b[1].animate.shift(DOWN * 0.18 + RIGHT * 0.15),
                court_b[0].animate.shift(UP * 0.18 + LEFT * 0.08),
                court_b[1].animate.shift(DOWN * 0.18 + RIGHT * 0.08),
            )
            self.play(FadeIn(label_a2))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(label_a2))

        # Télophase II : 4 cellules haploïdes à chromosomes simples
        c1 = Ellipse(width=1.5, height=1.2, color=WHITE, stroke_width=2)
        c2 = c1.copy()
        c3 = c1.copy()
        c4 = c1.copy()
        finales = VGroup(c1, c2, c3, c4).arrange(RIGHT, buff=0.5)
        finales.move_to(VGroup(cell_haut, cell_bas).get_center())

        contenus = VGroup()
        for cell, col in zip([c1, c2, c3, c4], [BLUE, BLUE, MAROON, MAROON]):
            g = VGroup(_chr_simple(col, height=0.5), _chr_simple(col, height=0.3)).arrange(RIGHT, buff=0.1)
            g.move_to(cell.get_center())
            contenus.add(g)

        label_t2 = Text("Télophase II : 4 cellules haploïdes, chromosomes simples", font_size=18, color=WHITE)
        label_t2.next_to(finales, DOWN, buff=0.3)

        with self.voiceover(
            text=(
                "Télophase II. Les noyaux se reforment et les deux cellules "
                "se partagent chacune en deux : on obtient au total quatre "
                "cellules haploïdes, dont les chromosomes sont simples."
            )
        ) as tracker:
            self.play(
                FadeOut(cell_haut), FadeOut(cell_bas), FadeOut(grp_haut), FadeOut(grp_bas),
                FadeIn(finales), FadeIn(contenus),
            )
            self.play(FadeIn(label_t2))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(finales), FadeOut(contenus), FadeOut(label_t2), FadeOut(sous_titre))

        # --- Tableau récapitulatif (2n=4) + quantité d'ADN ---------------------
        entete_tab = Text("Bilan pour une cellule mère à 2n=4", font_size=24, color=YELLOW, weight="BOLD")
        entete_tab.next_to(titre, DOWN, buff=0.5)

        rows = [
            ("Étape", "Cellules", "Chromosomes", "Chromat./chr.", "Formule"),
            ("Mère (avant réplication)", "1", "4", "1", "2n"),
            ("Fin interphase (ADN répliqué)", "1", "4", "2", "2n"),
            ("Fin 1ère division", "2", "2", "2", "n"),
            ("Fin 2ème division", "4", "2", "1", "n"),
        ]
        cell_matrix = []
        for i, row in enumerate(rows):
            color = YELLOW if i == 0 else WHITE
            weight = "BOLD" if i == 0 else "NORMAL"
            cell_matrix.append([Text(val, font_size=17, color=color, weight=weight) for val in row])

        tableau = _grid_table(cell_matrix, col_gap=0.5, row_gap=0.26)
        tableau.next_to(entete_tab, DOWN, buff=0.35)
        tableau.scale(0.95)

        with self.voiceover(
            text=(
                "Résumons les huit étapes pour une cellule mère de formule "
                "deux n égale quatre. Avant réplication : une cellule, "
                "quatre chromosomes simples, formule deux n. Après "
                "réplication, en fin d'interphase : toujours une cellule, "
                "quatre chromosomes, mais deux chromatides chacun. À la fin "
                "de la première division : deux cellules, deux chromosomes "
                "chacune, encore dédoublés, formule n. À la fin de la "
                "deuxième division : quatre cellules, deux chromosomes "
                "chacune, redevenus simples, formule n."
            )
        ) as tracker:
            self.play(FadeIn(entete_tab))
            self.play(FadeIn(tableau))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(entete_tab), FadeOut(tableau))

        adn_titre = Text("Quantité d'ADN par cellule", font_size=24, color=YELLOW, weight="BOLD")
        adn_titre.next_to(titre, DOWN, buff=0.5)
        adn = MathTex(r"Q \;\longrightarrow\; 2Q \;\longrightarrow\; Q \;\longrightarrow\; \dfrac{Q}{2}", font_size=32, color=WHITE)
        adn_labels = Text(
            "réplication         1ère division         2ème division",
            font_size=16,
            color=WHITE,
        )
        bloc_adn = VGroup(adn, adn_labels).arrange(DOWN, buff=0.3)
        bloc_adn.next_to(adn_titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "On peut aussi suivre la quantité d'ADN. Si la cellule mère "
                "contient une quantité Q d'ADN avant réplication, Q devient "
                "deux Q après la réplication, puis Q dans chaque cellule "
                "après la première division, puis Q sur deux dans chaque "
                "cellule après la deuxième division. Chaque division partage "
                "la quantité d'ADN en deux, alors que le nombre de "
                "chromosomes n'est réduit qu'à la première division."
            )
        ) as tracker:
            self.play(FadeIn(adn_titre))
            self.play(Write(adn))
            self.play(FadeIn(adn_labels))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(adn_titre), FadeOut(bloc_adn))

        # --- Exemple traité : insecte 2n=6 --------------------------------------
        exemple = example_box(
            Text(
                _wrap(
                    "Insecte à 2n=6. Q1 : bivalents en prophase I ? "
                    "6÷2=3 paires -> 3 bivalents. Q2 : chromosomes/"
                    "chromatides par cellule en fin de 1ère division ? "
                    "n=3 chromosomes, encore dédoublés -> 3×2=6 "
                    "chromatides. Q3 : total final ? Chaque cellule se "
                    "divise en 2 -> 4 cellules, formule n=3, chromosomes "
                    "simples.",
                    width=54,
                ),
                font_size=21,
            ),
            box_width=12.2,
        )
        exemple.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Chez un insecte de formule deux n égale six, on suit une "
                "cellule mère de testicule qui entre en méiose. Combien de "
                "bivalents en prophase I ? Deux n égale six signifie six "
                "divisé par deux, soit trois paires d'homologues : on observe "
                "donc trois bivalents. Combien de chromosomes et de "
                "chromatides à la fin de la première division ? Chaque "
                "cellule fille a reçu n égale trois chromosomes, encore "
                "dédoublés, soit trois fois deux égale six chromatides. "
                "Combien de cellules au final ? La deuxième division sépare "
                "les chromatides sœurs ; chacune des deux cellules donne deux "
                "cellules, soit quatre cellules au total, chacune haploïde, "
                "de formule n égale trois, avec des chromosomes simples."
            )
        ) as tracker:
            self.play(FadeIn(exemple))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(exemple))

        # --- À retenir : méthode de reconnaissance d'une étape -------------------
        methode = method_box(
            _bullets(
                [
                    "Combien de cellules ? 1 grande cellule -> 1ère "
                    "division ; 2 cellules -> 2ème division ; 4 cellules -> "
                    "méiose terminée.",
                    "Les chromosomes sont-ils appariés en bivalents ? Si "
                    "oui -> prophase I ou métaphase I (les bivalents "
                    "n'existent qu'en 1ère division).",
                    "Qu'est-ce qui se sépare ? Chromosomes encore dédoublés "
                    "-> anaphase I. Chromatides simples -> anaphase II.",
                ],
                font_size=20,
                width=52,
            ),
            box_width=12.2,
        )
        methode.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Face à une image de cellule en division, pose-toi trois "
                "questions, toujours dans le même ordre. Combien de cellules "
                "voit-on ? Une seule grande cellule : première division. "
                "Deux cellules : deuxième division. Quatre cellules : la "
                "méiose est terminée. Les chromosomes sont-ils appariés en "
                "bivalents ? Si oui, il s'agit de la prophase I ou de la "
                "métaphase I. Enfin, qu'est-ce qui est en train de se "
                "séparer ? Des chromosomes encore dédoublés : anaphase I. "
                "Des chromatides simples : anaphase II."
            )
        ) as tracker:
            self.play(FadeIn(methode))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(methode))

        # --- Piège à éviter : les 3 pièges de la méiose ---------------------------
        piege = warning_box(
            _bullets(
                [
                    "En anaphase I : séparation des homologues, centromères "
                    "intacts. En anaphase II : séparation des chromatides "
                    "sœurs, centromères scindés. Les inverser est l'erreur "
                    "classique du bac.",
                    "La réplication a lieu en interphase, jamais entre les "
                    "deux divisions : l'intercinèse est SANS réplication.",
                    "Après la 1ère division, les cellules sont déjà "
                    "haploïdes même si leurs chromosomes ont encore 2 "
                    "chromatides : c'est le nombre de centromères qui "
                    "définit la formule.",
                ],
                font_size=19,
                width=52,
            ),
            box_width=12.4,
        )
        piege.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Trois pièges à éviter absolument. Un : en anaphase un, ce "
                "sont les homologues qui se séparent et les centromères "
                "restent intacts ; en anaphase deux, ce sont les chromatides "
                "sœurs qui se séparent et les centromères se scindent. "
                "Inverser les deux est l'erreur classique du baccalauréat. "
                "Deux : la réplication de l'ADN a lieu avant la méiose, "
                "pendant l'interphase, jamais entre les deux divisions : "
                "l'intercinèse est sans réplication. Trois : après la "
                "première division, les cellules sont déjà haploïdes même si "
                "leurs chromosomes possèdent encore deux chromatides ; c'est "
                "le nombre de centromères, donc de chromosomes, qui définit "
                "la formule chromosomique."
            )
        ) as tracker:
            self.play(FadeIn(piege))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(titre), FadeOut(piege))
