"""
scenes/SVT_HerediteMendelienne_12.py — Chapitre 6 (1ereC, SVT), scène 12.

§ VII.3 L'hémophilie (génotypes similaires au daltonisme, contexte
historique de la reine Victoria) et résumé "deux signatures d'une
transmission récessive liée à X". Source : 1ereC/SVT.pdf, page 63.
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
    Line,
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


def _tableau(headers, rows, col_widths=None, row_height=0.58, header_font=18, cell_font=17):
    n_cols = len(headers)
    n_rows = len(rows) + 1
    if col_widths is None:
        col_widths = [2.6] * n_cols

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
        t.set(width=min(t.width, col_widths[c] - 0.15))
        t.move_to(row_groups[0][c].get_center())
        texts.add(t)

    for r, row in enumerate(rows):
        for c, cell in enumerate(row):
            if cell.startswith("$"):
                t = MathTex(cell.strip("$"), font_size=cell_font + 4, color=WHITE)
            else:
                t = Text(cell, font_size=cell_font, color=WHITE)
            t.set(width=min(t.width, col_widths[c] - 0.15))
            t.move_to(row_groups[r + 1][c].get_center())
            texts.add(t)

    return VGroup(grid, texts)


class Hemophilie(NotionScene):
    def construct(self):
        titre = scene_title("6.12 — L'hémophilie")
        titre.scale(0.78)
        titre.to_edge(UP)

        # --- Énoncé : présentation de la maladie -----------------------------------
        intro = Text(
            _wrap(
                "L'hémophilie est une maladie du sang qui ne coagule pas "
                "normalement (hémorragies prolongées). Elle est due à un "
                "allèle récessif h lié au chromosome X ; l'allèle normal "
                "est noté H.",
                width=56,
            ),
            font_size=24,
            color=WHITE,
        )
        intro.next_to(titre, DOWN, buff=0.55)

        with self.voiceover(
            text=(
                "L'hémophilie est une maladie du sang qui ne coagule pas "
                "normalement, provoquant des hémorragies prolongées. Elle "
                "est due à un allèle récessif, noté h, lié au chromosome "
                "X ; l'allèle normal est noté H."
            )
        ) as tracker:
            self.play(Write(titre))
            self.play(FadeIn(intro))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(intro))

        # --- Animation du raisonnement : les mêmes génotypes que le daltonisme ---
        entete_geno = Text("Les mêmes règles que le daltonisme", font_size=22, color=YELLOW, weight="BOLD")
        entete_geno.next_to(titre, DOWN, buff=0.45)

        tab_hemo = _tableau(
            headers=["Sexe", "Génotype", "Phénotype"],
            rows=[
                ["Femme", r"$X^HX^H$", "Saine"],
                ["Femme", r"$X^HX^h$", "Saine, conductrice"],
                ["Femme", r"$X^hX^h$", "Hémophile (très rare)"],
                ["Homme", r"$X^HY$", "Sain"],
                ["Homme", r"$X^hY$", "Hémophile"],
            ],
            col_widths=[2.2, 2.6, 3.8],
            row_height=0.55,
        )
        tab_hemo.next_to(entete_geno, DOWN, buff=0.35)

        with self.voiceover(
            text=(
                "Les génotypes et les règles de transmission sont "
                "exactement les mêmes que pour le daltonisme, avec H et "
                "h au lieu de D et d. Femme X H X H : saine. Femme X H X "
                "h : saine, conductrice. Femme X h X h : hémophile, un "
                "cas très rare. Homme X H Y : sain. Homme X h Y : "
                "hémophile."
            )
        ) as tracker:
            self.play(FadeIn(entete_geno))
            self.play(Create(tab_hemo[0]))
            self.play(Write(tab_hemo[1]))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(entete_geno), FadeOut(tab_hemo))

        # --- Exemple traité : le contexte historique --------------------------------
        entete_hist = Text("Un exemple historique célèbre", font_size=23, color=YELLOW, weight="BOLD")
        entete_hist.next_to(titre, DOWN, buff=0.5)

        # Petit schéma symbolique : une couronne (socle + pointes verticales).
        base = Rectangle(width=1.0, height=0.35, color=YELLOW, fill_color=YELLOW, fill_opacity=0.6)
        pointes = VGroup(
            *[Line([0, 0, 0], [0, 0.4, 0], color=YELLOW, stroke_width=4) for _ in range(3)]
        ).arrange(RIGHT, buff=0.25)
        pointes.next_to(base, UP, buff=-0.05)
        couronne = VGroup(base, pointes)
        couronne.next_to(entete_hist, DOWN, buff=0.5)

        histoire = Text(
            _wrap(
                "La reine Victoria d'Angleterre était conductrice de "
                "l'hémophilie et a transmis l'allèle h à plusieurs "
                "familles royales d'Europe.",
                width=48,
            ),
            font_size=22,
        )
        histoire.next_to(couronne, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Cette maladie est historiquement célèbre : la reine "
                "Victoria d'Angleterre était conductrice de l'hémophilie, "
                "et a transmis l'allèle h à plusieurs familles royales "
                "d'Europe, à travers ses descendants."
            )
        ) as tracker:
            self.play(FadeIn(entete_hist))
            self.play(Create(couronne))
            self.play(FadeIn(histoire))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(entete_hist), FadeOut(couronne), FadeOut(histoire))

        # --- À retenir : les deux signatures ------------------------------------------
        resume = warning_box(
            _bullets(
                [
                    "Les personnes atteintes sont presque toujours des "
                    "garçons.",
                    "Un père atteint ne transmet JAMAIS la maladie à ses "
                    "fils (il leur donne Y), mais transmet son allèle "
                    "(Xd ou Xh) à TOUTES ses filles, qui deviennent "
                    "conductrices.",
                ],
                font_size=22,
                width=48,
            ),
            box_width=11.3,
        )
        resume.next_to(titre, DOWN, buff=0.5)

        entete_resume = Text(
            "Résumé — deux signatures d'une transmission récessive liée à X",
            font_size=19,
            color=YELLOW,
            weight="BOLD",
        )
        entete_resume.next_to(titre, DOWN, buff=0.35)
        resume.next_to(entete_resume, DOWN, buff=0.35)

        with self.voiceover(
            text=(
                "Retenons le résumé de ces deux maladies, deux signatures "
                "caractéristiques d'une transmission récessive liée au "
                "chromosome X. Premièrement, les personnes atteintes sont "
                "presque toujours des garçons. Deuxièmement, un père "
                "atteint ne transmet jamais la maladie à ses fils, "
                "puisqu'il leur donne le chromosome Y, mais il transmet "
                "son allèle, X d ou X h, à toutes ses filles, qui "
                "deviennent alors conductrices sans être malades "
                "elles-mêmes."
            )
        ) as tracker:
            self.play(FadeIn(entete_resume))
            self.play(FadeIn(resume))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(titre), FadeOut(entete_resume), FadeOut(resume))
