"""
scenes/SVT_HerediteMendelienne_08.py — Chapitre 6 (1ereC, SVT), scène 08.

§ V. Le test-cross : problème posé, définition, interprétation (testeur
ll), Exemple résolu 3 (les 2 cas, avec 2 échiquiers), tableau conclusion
et méthode point clé. Source : 1ereC/SVT.pdf, page 61.
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


def _echiquier(col_gametes, row_gametes, resultat_fn, cell_size=1.1, font_size=28):
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


def _resultat_pois(gc, gr):
    allele1, allele2 = (gc, gr) if gc == "L" else (gr, gc)
    return f"{allele1}{allele2}"


class TestCross(NotionScene):
    def construct(self):
        titre = scene_title("6.8 — Le test-cross")
        titre.scale(0.75)
        titre.to_edge(UP)

        # --- Énoncé : le problème posé --------------------------------------------
        intro = Text(
            _wrap(
                "Un individu de phénotype dominant [L] peut être "
                "homozygote (LL) ou hétérozygote (Ll) : son seul aspect "
                "ne permet pas de trancher. Comment connaître son "
                "génotype ?",
                width=56,
            ),
            font_size=25,
            color=WHITE,
        )
        intro.next_to(titre, DOWN, buff=0.55)

        with self.voiceover(
            text=(
                "Un individu de phénotype dominant, crochet L, peut être "
                "homozygote, L L, ou hétérozygote, L l : son seul aspect "
                "extérieur ne permet pas de trancher. Comment connaître "
                "son génotype avec certitude ?"
            )
        ) as tracker:
            self.play(Write(titre))
            self.play(FadeIn(intro))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(intro))

        # --- Animation du raisonnement : définition et interprétation ------------
        def_test = definition_box(
            Text(
                _wrap(
                    "Le test-cross (croisement test) est le croisement "
                    "d'un individu de phénotype dominant, de génotype "
                    "inconnu, avec un individu de phénotype récessif, "
                    "nécessairement homozygote (ll), appelé testeur.",
                    width=50,
                ),
                font_size=23,
            ),
            box_width=11.3,
        )
        def_test.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Pour répondre, on réalise un test-cross, ou croisement "
                "test : on croise l'individu de phénotype dominant, dont "
                "le génotype est inconnu, avec un individu de phénotype "
                "récessif, nécessairement homozygote, l l, appelé le "
                "testeur."
            )
        ) as tracker:
            self.play(FadeIn(def_test))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(def_test))

        interp = Text(
            _wrap(
                "Le testeur ll ne produit que des gamètes l : les allèles "
                "apportés par l'individu testé se retrouvent donc "
                "« révélés » dans les phénotypes de la descendance.",
                width=54,
            ),
            font_size=24,
            color=WHITE,
        )
        interp.next_to(titre, DOWN, buff=0.55)

        with self.voiceover(
            text=(
                "L'idée est simple : le testeur, l l, ne produit que des "
                "gamètes l. Les allèles apportés par l'individu testé se "
                "retrouvent donc révélés, sans être masqués, dans les "
                "phénotypes de la descendance."
            )
        ) as tracker:
            self.play(FadeIn(interp))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(interp))

        # --- Exemple traité : les deux cas --------------------------------------
        entete_ex = Text("Exemple résolu 3 : test-cross d'une graine lisse", font_size=21, color=YELLOW, weight="BOLD")
        entete_ex.next_to(titre, DOWN, buff=0.4)

        cas1_titre = Text("1er cas : individu testé LL", font_size=19, color=YELLOW)
        ech1 = _echiquier(["L"], ["l"], _resultat_pois, cell_size=0.95, font_size=24)
        res1 = MathTex(r"100\%\,Ll \;\to\; 100\%\,[L]", font_size=20, color=WHITE)
        bloc1 = VGroup(cas1_titre, ech1["ensemble"], res1).arrange(DOWN, buff=0.3)

        cas2_titre = Text("2e cas : individu testé Ll", font_size=19, color=YELLOW)
        ech2 = _echiquier(["L", "l"], ["l"], _resultat_pois, cell_size=0.95, font_size=24)
        res2 = MathTex(r"\tfrac{1}{2}Ll\,[L] \;;\; \tfrac{1}{2}ll\,[l]", font_size=20, color=WHITE)
        bloc2 = VGroup(cas2_titre, ech2["ensemble"], res2).arrange(DOWN, buff=0.3)

        deux_blocs = VGroup(bloc1, bloc2).arrange(RIGHT, buff=1.2, aligned_edge=UP)
        deux_blocs.next_to(entete_ex, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Premier cas : l'individu testé est homozygote, L L. "
                "L'échiquier ne donne qu'un seul type de case, L l : la "
                "descendance est donc cent pour cent L l, soit cent pour "
                "cent de phénotype dominant, crochet L."
            )
        ) as tracker:
            self.play(FadeIn(entete_ex))
            self.play(FadeIn(cas1_titre))
            self.play(Create(ech1["grid"]), Write(ech1["col_headers"]), Write(ech1["row_headers"]))
            self.play(*[Write(c) for l in ech1["cellules"] for c in l])
            self.play(Write(res1))
            self.wait(tracker.get_remaining_duration())

        with self.voiceover(
            text=(
                "Second cas : l'individu testé est hétérozygote, L l. "
                "L'échiquier donne cette fois deux types de cases, L l et "
                "l l, en proportions égales : la descendance est donc un "
                "demi L l, phénotype dominant, et un demi l l, phénotype "
                "récessif. C'est exactement la signature qui permet de "
                "distinguer les deux cas."
            )
        ) as tracker:
            self.play(FadeIn(cas2_titre))
            self.play(Create(ech2["grid"]), Write(ech2["col_headers"]), Write(ech2["row_headers"]))
            self.play(*[Write(c) for l in ech2["cellules"] for c in l])
            self.play(Write(res2))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(entete_ex), FadeOut(deux_blocs))

        # --- À retenir : tableau conclusion + méthode ------------------------------
        entete_tab = Text("Conclusion du test-cross", font_size=23, color=YELLOW, weight="BOLD")
        entete_tab.next_to(titre, DOWN, buff=0.5)

        conclusion = _bullets(
            [
                "100% de descendants de phénotype dominant → l'individu "
                "testé est homozygote (LL).",
                "1/2 dominants - 1/2 récessifs → l'individu testé est "
                "hétérozygote (Ll).",
            ],
            font_size=23,
            width=50,
        )
        conclusion.next_to(entete_tab, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "On peut donc résumer la conclusion du test-cross ainsi : "
                "si l'on obtient cent pour cent de descendants de "
                "phénotype dominant, l'individu testé était homozygote, L "
                "L. Si l'on obtient un demi de dominants et un demi de "
                "récessifs, l'individu testé était hétérozygote, L l."
            )
        ) as tracker:
            self.play(FadeIn(entete_tab))
            self.play(FadeIn(conclusion))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(entete_tab), FadeOut(conclusion))

        methode = method_box(
            Text(
                _wrap(
                    "Les proportions 1/2-1/2 à l'issue d'un test-cross "
                    "prouvent que l'individu testé est hétérozygote. "
                    "C'est un outil très utilisé en sélection agricole "
                    "pour vérifier la pureté des lignées.",
                    width=50,
                ),
                font_size=23,
            ),
            box_width=11.3,
        )
        methode.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Retenez ce point clé : les proportions un demi, un demi, "
                "à l'issue d'un test-cross, prouvent que l'individu testé "
                "est hétérozygote. C'est un outil très utilisé en "
                "sélection agricole, pour vérifier la pureté des lignées "
                "avant de les multiplier."
            )
        ) as tracker:
            self.play(FadeIn(methode))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(titre), FadeOut(methode))
