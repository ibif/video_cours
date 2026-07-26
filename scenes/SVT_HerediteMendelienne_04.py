"""
scenes/SVT_HerediteMendelienne_04.py — Chapitre 6 (1ereC, SVT), scène 04.

§ II. Dominance, récessivité, homozygotie et hétérozygotie : allèle
dominant / récessif, tableau génotype-état-phénotype-gamètes, piège
"un phénotype récessif est obligatoirement homozygote", et la
codominance (annonce de l'exemple ABO). Source : 1ereC/SVT.pdf, page 59.
"""

import textwrap

from manim import (
    DOWN,
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
from shapes.boxes import definition_box, scene_title, warning_box


def _wrap(text: str, width: int = 56) -> str:
    return "\n".join(textwrap.fill(line, width=width) for line in text.split("\n"))


def _bullets(items, font_size=23, color=WHITE, width=54):
    lines = VGroup(
        *[Text(f"• {_wrap(it, width=width)}", font_size=font_size, color=color) for it in items]
    )
    lines.arrange(DOWN, aligned_edge=LEFT, buff=0.22)
    return lines


def _tableau(headers, rows, col_width=2.9, row_height=0.75, header_font=20, cell_font=18):
    """
    Construit un tableau simple sous forme de grille de Rectangle + Text,
    même esprit que l'échiquier de croisement (formes géométriques
    simples, pas d'environnement LaTeX `array`).
    `headers` : liste de labels de colonnes (str).
    `rows` : liste de listes de cellules (str), une liste par ligne.
    """
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


class DominanceRecessiviteCodominance(NotionScene):
    def construct(self):
        titre = scene_title("6.4 — Dominance, récessivité, codominance")
        titre.scale(0.65)
        titre.to_edge(UP)

        # --- Énoncé : deux comportements possibles pour un allèle ---------------
        intro = Text(
            _wrap(
                "Chez un hétérozygote, les deux allèles ne s'expriment "
                "pas forcément de la même façon dans le phénotype. On "
                "distingue allèle dominant et allèle récessif.",
                width=56,
            ),
            font_size=25,
            color=WHITE,
        )
        intro.next_to(titre, DOWN, buff=0.55)

        with self.voiceover(
            text=(
                "Chez un hétérozygote, les deux allèles portés ne "
                "s'expriment pas forcément de la même façon dans le "
                "phénotype observé. On distingue donc l'allèle dominant "
                "et l'allèle récessif."
            )
        ) as tracker:
            self.play(Write(titre))
            self.play(FadeIn(intro))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(intro))

        # --- Animation du raisonnement : les deux définitions --------------------
        def_dom = definition_box(
            Text(
                _wrap(
                    "Un allèle est dominant lorsqu'il s'exprime dans le "
                    "phénotype dès qu'il est présent en un seul exemplaire "
                    "(homozygote LL ou hétérozygote Ll).",
                    width=50,
                ),
                font_size=23,
            ),
            box_width=11.3,
        )
        def_dom.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Un allèle est dominant lorsqu'il s'exprime dans le "
                "phénotype dès qu'il est présent en un seul exemplaire, "
                "c'est-à-dire aussi bien à l'état homozygote L L qu'à "
                "l'état hétérozygote L l."
            )
        ) as tracker:
            self.play(FadeIn(def_dom))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(def_dom))

        def_rec = definition_box(
            Text(
                _wrap(
                    "Un allèle est récessif lorsqu'il ne s'exprime dans le "
                    "phénotype qu'à l'état homozygote (ll). À l'état "
                    "hétérozygote (Ll), son effet est masqué : "
                    "l'individu est porteur de l'allèle récessif.",
                    width=50,
                ),
                font_size=23,
            ),
            box_width=11.3,
        )
        def_rec.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Un allèle est récessif lorsqu'il ne s'exprime dans le "
                "phénotype qu'à l'état homozygote, l l. À l'état "
                "hétérozygote, L l, son effet est masqué par l'allèle "
                "dominant : on dit que l'individu est porteur de l'allèle "
                "récessif, sans être malade ou atteint pour ce caractère."
            )
        ) as tracker:
            self.play(FadeIn(def_rec))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(def_rec))

        # --- Exemple traité : le tableau génotype / état / phénotype / gamètes --
        entete_tab = Text("Tableau récapitulatif (exemple lisse/ridée)", font_size=23, color=YELLOW, weight="BOLD")
        entete_tab.next_to(titre, DOWN, buff=0.5)

        tableau = _tableau(
            headers=["Génotype", "État", "Phénotype", "Gamètes"],
            rows=[
                ["LL", "Homo. dominant", "[L] lisse", "100% L"],
                ["Ll", "Hétérozygote", "[L] lisse", "1/2 L, 1/2 l"],
                ["ll", "Homo. récessif", "[l] ridée", "100% l"],
            ],
            col_width=2.9,
            row_height=0.72,
        )
        tableau.next_to(entete_tab, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Résumons dans un tableau. Génotype L L : homozygote "
                "dominant, phénotype crochet L, lisse, il produit cent "
                "pour cent de gamètes L. Génotype L l : hétérozygote, "
                "phénotype crochet L, lisse également, car L domine, il "
                "produit un demi de gamètes L et un demi de gamètes l. "
                "Génotype l l : homozygote récessif, phénotype crochet l, "
                "ridée, il produit cent pour cent de gamètes l."
            )
        ) as tracker:
            self.play(FadeIn(entete_tab))
            self.play(Create(tableau[0]))
            self.play(Write(tableau[1]))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(entete_tab), FadeOut(tableau))

        # --- Piège à éviter -------------------------------------------------------
        piege = warning_box(
            Text(
                _wrap(
                    "Un individu de phénotype récessif [l] est "
                    "OBLIGATOIREMENT homozygote (ll) : c'est le seul cas "
                    "où le génotype peut être connu à coup sûr à partir du "
                    "seul phénotype.",
                    width=50,
                ),
                font_size=23,
            ),
            box_width=11.3,
        )
        piege.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Attention à un point souvent mal compris : un individu de "
                "phénotype récessif, crochet l, est obligatoirement "
                "homozygote, l l. C'est en réalité le seul cas où l'on "
                "peut connaître le génotype à coup sûr à partir du seul "
                "phénotype observé ; pour un phénotype dominant, en "
                "revanche, deux génotypes restent possibles."
            )
        ) as tracker:
            self.play(FadeIn(piege))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(piege))

        # --- À retenir : la codominance -------------------------------------------
        def_codom = definition_box(
            VGroup(
                Text(
                    _wrap(
                        "Il y a codominance lorsque les deux allèles d'un "
                        "gène s'expriment simultanément et pleinement chez "
                        "l'hétérozygote, dont le phénotype est alors "
                        "différent de celui des deux homozygotes.",
                        width=48,
                    ),
                    font_size=22,
                ),
                MathTex(r"\text{Exemple à venir : groupes sanguins ABO}", font_size=22, color=YELLOW),
            ).arrange(DOWN, buff=0.3),
            box_width=11.3,
        )
        def_codom.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Dans certains cas, aucun des deux allèles ne domine "
                "l'autre : les deux allèles s'expriment ensemble chez "
                "l'hétérozygote. On parle alors de codominance : les deux "
                "allèles s'expriment simultanément et pleinement, et le "
                "phénotype obtenu est différent de celui des deux "
                "homozygotes. Nous étudierons plus loin l'exemple "
                "fondamental de la codominance chez l'Homme : le système "
                "des groupes sanguins A B O."
            )
        ) as tracker:
            self.play(FadeIn(def_codom))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(titre), FadeOut(def_codom))
