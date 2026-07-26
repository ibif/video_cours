"""
scenes/SVT_HerediteMendelienne_11.py — Chapitre 6 (1ereC, SVT), scène 11.

§ VII.1-VII.2 Transmission autosomique vs transmission liée au sexe
(autosomes/gonosomes), le daltonisme (tableau des 5 cas), méthode
point clé (le garçon n'a qu'un seul X, reçu de sa mère), Exemple résolu
6 (croisement XDXd x XDY). Source : 1ereC/SVT.pdf, page 63.
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
from shapes.boxes import definition_box, method_box, scene_title


def _wrap(text: str, width: int = 56) -> str:
    return "\n".join(textwrap.fill(line, width=width) for line in text.split("\n"))


def _bullets(items, font_size=23, color=WHITE, width=54):
    lines = VGroup(
        *[Text(f"• {_wrap(it, width=width)}", font_size=font_size, color=color) for it in items]
    )
    lines.arrange(DOWN, aligned_edge=LEFT, buff=0.22)
    return lines


def _tableau(headers, rows, col_widths=None, row_height=0.62, header_font=18, cell_font=17):
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


class AutosomiqueLieAuSexeDaltonisme(NotionScene):
    def construct(self):
        titre = scene_title("6.11 — Transmission liée au sexe : le daltonisme")
        titre.scale(0.58)
        titre.to_edge(UP)

        # --- Énoncé : autosomes et gonosomes -----------------------------------
        intro = Text(
            _wrap(
                "Chez l'Homme, les 23 paires de chromosomes comprennent : "
                "22 paires d'autosomes, identiques chez l'homme et la "
                "femme, et 1 paire de gonosomes (chromosomes sexuels) : "
                "XX chez la femme, XY chez l'homme.",
                width=56,
            ),
            font_size=23,
            color=WHITE,
        )
        intro.next_to(titre, DOWN, buff=0.55)

        with self.voiceover(
            text=(
                "Chez l'Homme, les vingt-trois paires de chromosomes "
                "comprennent vingt-deux paires d'autosomes, identiques "
                "chez l'homme et la femme, et une paire de gonosomes, ou "
                "chromosomes sexuels : X X chez la femme, X Y chez "
                "l'homme."
            )
        ) as tracker:
            self.play(Write(titre))
            self.play(FadeIn(intro))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(intro))

        # --- Animation du raisonnement : les deux définitions -----------------------
        def_auto = definition_box(
            Text(
                _wrap(
                    "Transmission autosomique : le gène est porté par un "
                    "autosome. Le caractère se transmet de la même façon "
                    "aux garçons et aux filles. Ex : drépanocytose, "
                    "albinisme, groupes sanguins.",
                    width=48,
                ),
                font_size=21,
            ),
            box_width=11.0,
        )
        def_auto.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Un caractère est à transmission autosomique lorsque son "
                "gène est porté par un autosome. Il se transmet alors de "
                "la même façon aux garçons et aux filles, qui sont "
                "atteints avec la même fréquence : par exemple la "
                "drépanocytose, l'albinisme, ou les groupes sanguins, que "
                "nous venons d'étudier."
            )
        ) as tracker:
            self.play(FadeIn(def_auto))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(def_auto))

        def_sexe = definition_box(
            Text(
                _wrap(
                    "Transmission liée au sexe : le gène est porté par un "
                    "gonosome, en général le chromosome X. Garçons et "
                    "filles ne sont alors pas égaux devant la maladie.",
                    width=48,
                ),
                font_size=22,
            ),
            box_width=11.0,
        )
        def_sexe.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Un caractère est à transmission liée au sexe lorsque son "
                "gène est porté par un gonosome, en général le chromosome "
                "X. Garçons et filles ne sont alors plus égaux devant la "
                "maladie, comme nous allons le voir avec le daltonisme."
            )
        ) as tracker:
            self.play(FadeIn(def_sexe))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(def_sexe))

        # --- Exemple traité : le tableau complet du daltonisme ----------------------
        entete_dalt = Text("Le daltonisme (allèle récessif d, sur X)", font_size=22, color=YELLOW, weight="BOLD")
        entete_dalt.next_to(titre, DOWN, buff=0.45)

        tab_dalt = _tableau(
            headers=["Sexe", "Génotype", "Phénotype"],
            rows=[
                ["Femme", r"$X^DX^D$", "Saine"],
                ["Femme", r"$X^DX^d$", "Saine, conductrice"],
                ["Femme", r"$X^dX^d$", "Daltonienne (rare)"],
                ["Homme", r"$X^DY$", "Sain"],
                ["Homme", r"$X^dY$", "Daltonien"],
            ],
            col_widths=[2.2, 2.6, 3.6],
            row_height=0.58,
        )
        tab_dalt.next_to(entete_dalt, DOWN, buff=0.35)

        with self.voiceover(
            text=(
                "Le daltonisme est une anomalie de la vision des "
                "couleurs, confusion du rouge et du vert, due à un "
                "allèle récessif d, porté par le chromosome X ; l'allèle "
                "normal est noté D. Le chromosome Y, beaucoup plus petit, "
                "ne porte pas ce gène. Voici les cinq cas possibles : une "
                "femme X D X D est saine ; une femme X D X d est saine "
                "mais conductrice, c'est-à-dire porteuse ; une femme X d "
                "X d est daltonienne, un cas rare ; un homme X D Y est "
                "sain ; un homme X d Y est daltonien."
            )
        ) as tracker:
            self.play(FadeIn(entete_dalt))
            self.play(Create(tab_dalt[0]))
            self.play(Write(tab_dalt[1]))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(entete_dalt), FadeOut(tab_dalt))

        # --- Méthode point clé -------------------------------------------------------
        methode = method_box(
            Text(
                _wrap(
                    "Le garçon ne possède qu'un seul chromosome X, reçu de "
                    "sa mère (le père lui transmet toujours Y). Il lui "
                    "suffit donc d'un seul allèle d pour être daltonien : "
                    "d'où la plus grande fréquence des garçons atteints. "
                    "Une fille n'est daltonienne que si elle reçoit Xd de "
                    "son père ET de sa mère.",
                    width=50,
                ),
                font_size=21,
            ),
            box_width=11.3,
        )
        methode.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Voici le point clé à retenir absolument : le garçon ne "
                "possède qu'un seul chromosome X, reçu de sa mère, car le "
                "père lui transmet toujours Y. Il lui suffit donc d'un "
                "seul allèle d pour être daltonien : c'est pourquoi les "
                "garçons sont beaucoup plus souvent atteints que les "
                "filles. Une fille, elle, ne peut être daltonienne que si "
                "elle reçoit X d à la fois de son père et de sa mère."
            )
        ) as tracker:
            self.play(FadeIn(methode))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(methode))

        # --- Exemple résolu 6 --------------------------------------------------------
        entete_ex6 = Text(
            "Exemple résolu 6 : femme conductrice x homme sain", font_size=20, color=YELLOW, weight="BOLD"
        )
        entete_ex6.next_to(titre, DOWN, buff=0.5)

        genotypes_6 = MathTex(r"X^DX^d \;\times\; X^DY", font_size=30, color=WHITE)
        genotypes_6.next_to(entete_ex6, DOWN, buff=0.35)

        def _ligne_mixte(prefixe, formule_latex, suffixe):
            return VGroup(
                Text(f"• {prefixe}", font_size=20, color=WHITE),
                MathTex(formule_latex, font_size=24, color=YELLOW),
                Text(suffixe, font_size=20, color=WHITE),
            ).arrange(RIGHT, buff=0.15)

        ligne_gametes = _ligne_mixte(
            "Gamètes de la mère : ", r"X^D,\, X^d", " ; gamètes du père : X-D, Y."
        )
        ligne_filles = _ligne_mixte(
            "Filles : ", r"X^DX^D,\; X^DX^d", " → toutes saines, 1/2 conductrices."
        )
        ligne_garcons = _ligne_mixte(
            "Garçons : ", r"X^DY,\; X^dY", " → 1/2 sains, 1/2 daltoniens."
        )
        resultats_6 = VGroup(ligne_gametes, ligne_filles, ligne_garcons).arrange(DOWN, aligned_edge=LEFT, buff=0.3)
        resultats_6.scale(0.95)
        resultats_6.next_to(genotypes_6, DOWN, buff=0.45)

        with self.voiceover(
            text=(
                "Croisons une femme conductrice, X D X d, avec un homme "
                "sain, X D Y. La mère produit des gamètes X D et X d ; le "
                "père produit des gamètes X D et Y. Parmi les filles, on "
                "obtient X D X D, saine, et X D X d, saine conductrice : "
                "toutes les filles sont donc saines, mais la moitié sont "
                "conductrices. Parmi les garçons, on obtient X D Y, sain, "
                "et X d Y, daltonien : la moitié des garçons sont sains, "
                "l'autre moitié daltoniens."
            )
        ) as tracker:
            self.play(FadeIn(entete_ex6))
            self.play(Write(genotypes_6))
            self.play(FadeIn(resultats_6))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(titre), FadeOut(entete_ex6), FadeOut(genotypes_6), FadeOut(resultats_6))
