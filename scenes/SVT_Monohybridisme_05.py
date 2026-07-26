"""
scenes/SVT_Monohybridisme_05.py — Chapitre 4 (1ereD, SVT), scène 05.

§ 4.4 Interprétation chromosomique : l'échiquier de croisement. Rôle de la
méiose et de la fécondation, méthode de construction en 5 étapes, exemple
animé de l'échiquier F1 x F1 (V/v x V/v), tableau des 3 croisements
fondamentaux, attention aux proportions théoriques. Source : 1ereD/SVT.pdf,
pages 53-55.
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


def _echiquier(col_gametes, row_gametes, resultat_fn, cell_size=1.35, font_size=32):
    """
    Construit un échiquier de croisement (tableau à double entrée) sous
    forme d'une grille de Rectangle + MathTex, plutôt qu'un environnement
    LaTeX `array` (plus simple à animer case par case, et sans risque lié
    au correctif 5 sur `\\\\` suivi de `[`).
    `col_gametes` = gamètes du parent en colonnes (ex. ["V", "v"]).
    `row_gametes` = gamètes du parent en lignes (ex. ["V", "v"]).
    `resultat_fn(gamete_col, gamete_row)` -> texte LaTeX du génotype obtenu.
    """
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


class EchiquierDeCroisement(NotionScene):
    def construct(self):
        titre = scene_title("4.4 — L'échiquier de croisement")
        titre.scale(0.72)
        titre.to_edge(UP)

        # --- Énoncé : rôle de la méiose et de la fécondation --------------------
        intro = Text(
            _wrap(
                "Pourquoi ces proportions exactes de 1/4, 1/2, 1/4 ? Deux "
                "faits de cytologie l'expliquent : à la méiose, chaque "
                "gamète ne reçoit qu'un allèle du gène ; à la "
                "fécondation, la rencontre des gamètes se fait au hasard.",
                width=56,
            ),
            font_size=25,
            color=WHITE,
        )
        intro.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Pourquoi ces proportions exactes d'un quart, un demi, un "
                "quart ? La réponse tient en deux faits de cytologie. À la "
                "méiose, les deux chromosomes homologues se séparent : "
                "chaque gamète ne reçoit qu'un seul allèle du gène. Chez un "
                "hybride V sur v, la moitié des gamètes reçoit V, l'autre "
                "moitié reçoit v. À la fécondation, la rencontre entre un "
                "gamète mâle et un gamète femelle se fait au hasard : "
                "chaque combinaison a la même probabilité de se produire. Il "
                "suffit alors de dénombrer toutes les combinaisons "
                "possibles : c'est exactement ce que fait l'échiquier de "
                "croisement."
            )
        ) as tracker:
            self.play(Write(titre))
            self.play(FadeIn(intro))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(intro))

        # --- Animation du raisonnement : méthode en 5 étapes --------------------
        methode = method_box(
            Text(
                _wrap(
                    "1. Écrire le génotype des 2 parents croisés.\n"
                    "2. Écrire les gamètes produits par chacun.\n"
                    "3. Tracer un tableau à double entrée (gamètes du "
                    "père en colonnes, de la mère en lignes).\n"
                    "4. Remplir chaque case en réunissant les 2 allèles "
                    "qui se rencontrent.\n"
                    "5. Compter les génotypes, regrouper par phénotypes, "
                    "conclure en proportions (quarts).",
                    width=54,
                ),
                font_size=21,
            ),
            box_width=12.3,
        )
        methode.next_to(titre, DOWN, buff=0.45)

        with self.voiceover(
            text=(
                "Voici la méthode pour construire et exploiter un échiquier "
                "de croisement. Étape un : écrire le génotype des deux "
                "parents croisés. Étape deux : écrire les gamètes produits "
                "par chaque parent. Étape trois : tracer un tableau à "
                "double entrée, avec en tête de colonnes les gamètes du "
                "parent mâle, et en tête de lignes les gamètes du parent "
                "femelle. Étape quatre : remplir chaque case en réunissant "
                "les deux allèles qui se rencontrent, en écrivant "
                "l'allèle dominant en premier par habitude. Étape cinq : "
                "compter les génotypes obtenus, les regrouper par "
                "phénotypes, et conclure en proportions, en quarts, sur les "
                "quatre cases."
            )
        ) as tracker:
            self.play(FadeIn(methode))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(methode))

        # --- Exemple traité : l'échiquier animé du croisement F1 x F1 ----------
        entete_ex = Text("Exemple : croisement F1 x F1 (V/v x V/v)", font_size=25, color=YELLOW, weight="BOLD")
        entete_ex.next_to(titre, DOWN, buff=0.5)

        genotypes_parents = MathTex(r"V/v \;\times\; V/v", font_size=32, color=WHITE)
        genotypes_parents.next_to(entete_ex, DOWN, buff=0.35)

        with self.voiceover(
            text=(
                "Dressons l'échiquier de croisement de deux plants de maïs "
                "hybrides, V sur v, croisés entre eux, et prévoyons la "
                "descendance. Étape un, les génotypes des parents : V sur v "
                "croisé avec V sur v."
            )
        ) as tracker:
            self.play(FadeIn(entete_ex))
            self.play(Write(genotypes_parents))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(genotypes_parents))

        def resultat_maize(gc, gr):
            # allèle dominant V en premier, par convention
            allele1, allele2 = (gc, gr) if gc == "V" else (gr, gc)
            return f"{allele1}/{allele2}"

        ech = _echiquier(["V", "v"], ["V", "v"], resultat_maize)
        ech["ensemble"].next_to(entete_ex, DOWN, buff=0.5).shift(LEFT * 2.2)

        label_pere = Text("Gamètes du père", font_size=18, color=YELLOW)
        label_pere.next_to(ech["col_headers"], UP, buff=0.2)
        label_mere = Text("Gamètes\nde la mère", font_size=18, color=YELLOW)
        label_mere.next_to(ech["row_headers"], LEFT, buff=0.35)

        with self.voiceover(
            text=(
                "Étape deux, les gamètes : chaque parent produit un demi de "
                "gamètes V et un demi de gamètes v. Étapes trois et quatre, "
                "construisons le tableau à double entrée : en colonnes, les "
                "gamètes du père ; en lignes, les gamètes de la mère."
            )
        ) as tracker:
            self.play(Create(ech["grid"]))
            self.play(FadeIn(ech["corner"]))
            self.play(FadeIn(label_pere), Write(ech["col_headers"]))
            self.play(FadeIn(label_mere), Write(ech["row_headers"]))
            self.wait(tracker.get_remaining_duration())

        with self.voiceover(
            text=(
                "Remplissons chaque case en réunissant les deux allèles qui "
                "se rencontrent. Gamète V du père et gamète V de la mère "
                "donnent V sur V. Gamète v du père et gamète V de la mère "
                "donnent V sur v. Gamète V du père et gamète v de la mère "
                "donnent V sur v. Gamète v du père et gamète v de la mère "
                "donnent v sur v."
            )
        ) as tracker:
            for ligne in ech["cellules"]:
                self.play(*[Write(cell) for cell in ligne])
            self.wait(tracker.get_remaining_duration())

        decompte = MathTex(
            r"\dfrac{1}{4}\,V/V \qquad \dfrac{1}{2}\,V/v \qquad \dfrac{1}{4}\,v/v",
            font_size=28,
            color=YELLOW,
        )
        decompte.next_to(ech["ensemble"], RIGHT, buff=0.9)

        phenotypes = MathTex(
            r"\dfrac{3}{4}\,[V] \qquad \dfrac{1}{4}\,[v]",
            font_size=30,
            color=WHITE,
        )
        phenotypes.next_to(decompte, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Étape cinq, le décompte. Sur quatre cases équiprobables : V "
                "sur V occupe une case, soit un quart ; V sur v occupe deux "
                "cases, soit un demi ; v sur v occupe une case, soit un "
                "quart. En phénotypes, V sur V et V sur v donnent tous deux "
                "le phénotype violet, donc trois quarts de plants à grains "
                "violets ; v sur v donne le phénotype blanc, donc un quart "
                "de plants à grains blancs. La descendance du croisement V "
                "sur v croisé avec V sur v est donc théoriquement composée "
                "de trois quarts de phénotype dominant et un quart de "
                "phénotype récessif, conformément à la deuxième loi de "
                "Mendel."
            )
        ) as tracker:
            self.play(FadeIn(decompte))
            self.play(FadeIn(phenotypes))
            self.wait(tracker.get_remaining_duration())

        self.play(
            FadeOut(entete_ex),
            FadeOut(ech["ensemble"]),
            FadeOut(label_pere),
            FadeOut(label_mere),
            FadeOut(decompte),
            FadeOut(phenotypes),
        )

        # --- À retenir : les 3 croisements fondamentaux -------------------------
        entete_tab = Text("Les 3 croisements fondamentaux à connaître", font_size=24, color=YELLOW, weight="BOLD")
        entete_tab.next_to(titre, DOWN, buff=0.5)

        tab = _bullets(
            [
                "V/V x V/V : descendance 100% V/V, phénotype 100% [V].",
                "V/v x V/v : descendance 1/4 V/V, 1/2 V/v, 1/4 v/v ; "
                "phénotypes 3/4 [V], 1/4 [v].",
                "V/V x v/v : descendance 100% V/v ; phénotype 100% [V].",
            ],
            font_size=23,
            width=54,
        )
        tab.next_to(entete_tab, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Il faut connaître par cœur trois croisements fondamentaux. "
                "V sur V croisé avec V sur V donne une descendance à cent "
                "pour cent V sur V, donc cent pour cent de phénotype "
                "dominant. V sur v croisé avec V sur v, le cas de la F1 "
                "entre elle, donne un quart V sur V, un demi V sur v, un "
                "quart v sur v, soit trois quarts de dominant et un quart de "
                "récessif. Et V sur V croisé avec v sur v, le cas de la F1, "
                "donne cent pour cent V sur v, donc cent pour cent de "
                "phénotype dominant."
            )
        ) as tracker:
            self.play(FadeIn(entete_tab))
            self.play(FadeIn(tab))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(entete_tab), FadeOut(tab))

        # --- Piège à éviter : les proportions sont théoriques -------------------
        piege = warning_box(
            Text(
                _wrap(
                    "Les proportions 3/4-1/4 sont des probabilités, "
                    "valables en moyenne sur de GRANDS effectifs. Sur une "
                    "petite portée, le hasard peut s'écarter des "
                    "proportions sans contredire les lois. Toujours "
                    "comparer effectifs observés et effectifs théoriques "
                    "calculés sur le même total ; de faibles écarts sont "
                    "acceptés.",
                    width=54,
                ),
                font_size=22,
            ),
            box_width=12.3,
        )
        piege.next_to(titre, DOWN, buff=0.55)

        with self.voiceover(
            text=(
                "Attention : les proportions trois quarts, un quart sont "
                "des probabilités. Elles décrivent ce qui se passe en "
                "moyenne sur de grands effectifs. Sur une petite portée, "
                "par exemple quatre descendants, le hasard de la rencontre "
                "des gamètes peut donner quatre dominants, ou deux et deux, "
                "sans que les lois soient contredites. C'est pourquoi "
                "Mendel comptait des centaines de descendants. Dans les "
                "exercices, on compare toujours les effectifs observés aux "
                "effectifs théoriques calculés sur le même total, et de "
                "faibles écarts sont acceptés."
            )
        ) as tracker:
            self.play(FadeIn(piege))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(titre), FadeOut(piege))
