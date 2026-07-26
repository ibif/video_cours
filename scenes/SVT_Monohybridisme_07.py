"""
scenes/SVT_Monohybridisme_07.py — Chapitre 4 (1ereD, SVT), scène 07.

§ 4.6.1-4.6.2 Cas particuliers : la codominance et les allèles létaux.
Définitions, échiquier animé des belles-de-nuit (R/B x R/B, 3 phénotypes),
définition de l'allèle létal et exemple des souris jaunes (J/j x J/j,
létalité -> 2/3-1/3 parmi les vivants). Source : 1ereD/SVT.pdf, pages
57-59.
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
from shapes.boxes import definition_box, example_box, scene_title, warning_box


def _wrap(text: str, width: int = 56) -> str:
    return "\n".join(textwrap.fill(line, width=width) for line in text.split("\n"))


def _bullets(items, font_size=23, color=WHITE, width=54):
    lines = VGroup(
        *[Text(f"• {_wrap(it, width=width)}", font_size=font_size, color=color) for it in items]
    )
    lines.arrange(DOWN, aligned_edge=LEFT, buff=0.22)
    return lines


def _echiquier(col_gametes, row_gametes, resultat_fn, cell_size=1.25, font_size=28):
    """Grille Rectangle + MathTex d'un échiquier de croisement (voir scène 05)."""
    n_cols = len(col_gametes)
    n_rows = len(row_gametes)

    grid = VGroup()
    row_groups = []
    for _r in range(n_rows + 1):
        row_rects = VGroup(
            *[
                Rectangle(width=cell_size, height=cell_size, stroke_color=WHITE, stroke_width=2)
                for _ in range(n_cols + 1)
            ]
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


class CodominanceEtAlleleLetal(NotionScene):
    def construct(self):
        titre = scene_title("4.6 — Codominance et allèles létaux")
        titre.scale(0.7)
        titre.to_edge(UP)

        # --- Énoncé : la codominance --------------------------------------------
        definition_codom = definition_box(
            Text(
                _wrap(
                    "Deux allèles sont codominants lorsqu'aucun ne domine "
                    "l'autre : chez l'hétérozygote, les deux s'expriment "
                    "et le phénotype est intermédiaire. On note alors les "
                    "allèles par deux lettres distinctes (ex. R et B).",
                    width=54,
                ),
                font_size=24,
            ),
            box_width=11.8,
        )
        definition_codom.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Premier cas particulier : la codominance. Deux allèles "
                "sont codominants lorsqu'aucun ne domine l'autre : chez "
                "l'hétérozygote, les deux s'expriment, et le phénotype est "
                "intermédiaire, ou mixte, entre ceux des deux homozygotes. "
                "Faute de dominance, on renonce aux majuscules et "
                "minuscules : on note les allèles par deux lettres "
                "distinctes, par exemple R et B."
            )
        ) as tracker:
            self.play(Write(titre))
            self.play(FadeIn(definition_codom))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(definition_codom))

        intro_belle = Text(
            _wrap(
                "Exemple classique : la belle-de-nuit. Lignée pure rouge "
                "(R/R) x lignée pure blanche (B/B) donne une F1 uniforme... "
                "mais ROSE (R/B), un phénotype nouveau, intermédiaire. La "
                "1ère loi de Mendel reste vraie : la F1 est uniforme.",
                width=56,
            ),
            font_size=24,
            color=WHITE,
        )
        intro_belle.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Prenons l'exemple classique de la belle-de-nuit, une "
                "plante ornementale. Le croisement d'une lignée pure à "
                "fleurs rouges, R sur R, avec une lignée pure à fleurs "
                "blanches, B sur B, donne une F1 uniforme... mais rose, R "
                "sur B : un phénotype nouveau, intermédiaire. La F1 est "
                "uniforme, donc la première loi de Mendel reste vraie ; en "
                "revanche, en F2, on n'obtient plus trois quarts, un quart, "
                "car chaque génotype correspond désormais à un phénotype "
                "distinct."
            )
        ) as tracker:
            self.play(FadeIn(intro_belle))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(intro_belle))

        # --- Animation du raisonnement : échiquier des belles-de-nuit ----------
        entete_ex1 = Text("Échiquier : R/B x R/B (jardin botanique de Bingerville)", font_size=21, color=YELLOW, weight="BOLD")
        entete_ex1.next_to(titre, DOWN, buff=0.5)

        def resultat_belle(gc, gr):
            allele1, allele2 = (gc, gr) if gc == "R" else (gr, gc)
            return f"{allele1}/{allele2}"

        ech1 = _echiquier(["R", "B"], ["R", "B"], resultat_belle)
        ech1["ensemble"].next_to(entete_ex1, DOWN, buff=0.4).shift(LEFT * 2.4)

        decompte1 = MathTex(
            r"\dfrac{1}{4}\,R/R \;[\text{rouge}] \quad \dfrac{1}{2}\,R/B \;[\text{rose}] \quad \dfrac{1}{4}\,B/B \;[\text{blanc}]",
            font_size=22,
            color=WHITE,
        )
        decompte1.next_to(ech1["ensemble"], DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Au jardin botanique de Bingerville, un jardinier croise "
                "deux plants de belles-de-nuit à fleurs roses, R sur B "
                "croisé avec R sur B. Chaque parent produit un demi de "
                "gamètes R et un demi de gamètes B. L'échiquier donne : R "
                "du père et R de la mère font R sur R ; B du père et R de "
                "la mère font R sur B ; R du père et B de la mère font R "
                "sur B ; B du père et B de la mère font B sur B."
            )
        ) as tracker:
            self.play(FadeIn(entete_ex1))
            self.play(Create(ech1["grid"]))
            self.play(FadeIn(ech1["corner"]), Write(ech1["col_headers"]), Write(ech1["row_headers"]))
            for ligne in ech1["cellules"]:
                self.play(*[Write(cell) for cell in ligne])
            self.wait(tracker.get_remaining_duration())

        with self.voiceover(
            text=(
                "Décompte des génotypes : un quart R sur R, un demi R sur "
                "B, un quart B sur B. Par codominance, R sur R donne des "
                "fleurs rouges, R sur B donne des fleurs roses, B sur B "
                "donne des fleurs blanches. La descendance comprend donc un "
                "quart de plants à fleurs rouges, un demi de plants à "
                "fleurs roses et un quart de plants à fleurs blanches. Trois "
                "phénotypes au lieu de deux : c'est la signature de la "
                "codominance."
            )
        ) as tracker:
            self.play(FadeIn(decompte1))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(entete_ex1), FadeOut(ech1["ensemble"]), FadeOut(decompte1))

        # --- Exemple traité : les allèles létaux (souris jaunes) --------------
        definition_letal = definition_box(
            Text(
                _wrap(
                    "Un allèle est dit létal lorsque sa présence (souvent "
                    "à l'état homozygote) provoque la mort de l'individu, "
                    "avant la naissance. Les individus concernés manquent "
                    "dans les comptages : les proportions sont modifiées.",
                    width=54,
                ),
                font_size=23,
            ),
            box_width=11.9,
        )
        definition_letal.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Deuxième cas particulier : les allèles létaux. Un allèle "
                "est dit létal lorsque sa présence, en général à l'état "
                "homozygote, provoque la mort de l'individu, souvent avant "
                "la naissance. Les individus concernés manquant dans les "
                "comptages, les proportions de la descendance sont "
                "modifiées. Exemple classique : la souris à pelage jaune. "
                "L'allèle J, jaune, domine l'allèle j, gris, mais J est "
                "létal à l'état homozygote : les embryons J sur J meurent "
                "dans l'utérus. Toutes les souris jaunes vivantes sont donc "
                "obligatoirement hétérozygotes J sur j."
            )
        ) as tracker:
            self.play(FadeIn(definition_letal))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(definition_letal))

        exemple = example_box(
            Text(
                _wrap(
                    "Croisement J/j x J/j. Échiquier : 1/4 J/J, 1/2 J/j, "
                    "1/4 j/j. Mais les J/J meurent avant la naissance -> "
                    "3/4 de survivants seulement. Parmi eux : jaunes "
                    "(J/j) = (2/4)/(3/4) = 2/3 ; grises (j/j) = "
                    "(1/4)/(3/4) = 1/3. Une proportion 2/3-1/3 doit faire "
                    "penser à un allèle létal.",
                    width=54,
                ),
                font_size=21,
            ),
            box_width=12.3,
        )
        exemple.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "On croise deux souris jaunes, J sur j croisé avec J sur j. "
                "Quelles proportions observe-t-on parmi les souriceaux nés "
                "vivants ? Chaque parent produit un demi de gamètes J et un "
                "demi de gamètes j. L'échiquier donne, parmi les œufs "
                "fécondés : un quart J sur J, un demi J sur j, un quart j "
                "sur j. Il faut tenir compte de la létalité : le quart J "
                "sur J meurt avant la naissance, il n'apparaît pas dans les "
                "comptages. Parmi les trois quarts de survivants, il y a "
                "deux quarts de J sur j, jaunes, et un quart de j sur j, "
                "grises. En rapportant au total des vivants : les jaunes "
                "représentent deux tiers, et les grises un tiers. "
                "Conclusion : parmi les souriceaux nés vivants, on compte "
                "deux tiers de souris jaunes et un tiers de souris grises — "
                "et non trois quarts, un quart. Une proportion deux tiers, "
                "un tiers dans une descendance doit faire penser à un "
                "allèle létal."
            )
        ) as tracker:
            self.play(FadeIn(exemple))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(exemple))

        # --- À retenir --------------------------------------------------------------
        entete_retenir = Text("À retenir", font_size=27, color=YELLOW, weight="BOLD")
        entete_retenir.next_to(titre, DOWN, buff=0.5)

        retenir = _bullets(
            [
                "Codominance : hétérozygote = phénotype intermédiaire ; "
                "F2 en 1/4 - 1/2 - 1/4 avec 3 phénotypes distincts.",
                "Allèle létal : un génotype meurt avant la naissance ; "
                "proportions chez les vivants modifiées (ex. 2/3 - 1/3).",
            ],
            font_size=22,
            width=54,
        )
        retenir.next_to(entete_retenir, DOWN, buff=0.35)

        with self.voiceover(
            text=(
                "Retenons l'essentiel de ces deux cas particuliers. En cas "
                "de codominance, l'hétérozygote présente un phénotype "
                "intermédiaire, et la F2 se répartit en un quart, un demi, "
                "un quart, avec trois phénotypes distincts. En cas d'allèle "
                "létal, un génotype meurt avant la naissance, et les "
                "proportions chez les vivants sont modifiées, par exemple "
                "en deux tiers, un tiers."
            )
        ) as tracker:
            self.play(FadeIn(entete_retenir))
            self.play(FadeIn(retenir))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(entete_retenir), FadeOut(retenir))

        # --- Piège à éviter -----------------------------------------------------------
        piege = warning_box(
            Text(
                _wrap(
                    "La codominance et l'allèle létal NE remettent PAS en "
                    "cause la 1ère loi de Mendel : la F1 reste uniforme "
                    "dans les 2 cas. Ce qui change, c'est UNIQUEMENT la "
                    "F2 : elle n'est plus 3/4-1/4 car chaque génotype "
                    "compte, ou parce que certains génotypes manquent.",
                    width=54,
                ),
                font_size=22,
            ),
            box_width=12.3,
        )
        piege.next_to(titre, DOWN, buff=0.55)

        with self.voiceover(
            text=(
                "Attention à ne pas croire que la codominance ou l'allèle "
                "létal remettent en cause la première loi de Mendel : la F1 "
                "reste parfaitement uniforme dans les deux cas. Ce qui "
                "change, c'est uniquement la F2 : elle n'est plus trois "
                "quarts, un quart, soit parce que chaque génotype produit "
                "désormais son propre phénotype, comme pour la "
                "codominance, soit parce que certains génotypes manquent à "
                "l'appel, comme pour l'allèle létal."
            )
        ) as tracker:
            self.play(FadeIn(piege))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(titre), FadeOut(piege))
