"""
scenes/SVT_Monohybridisme_08.py — Chapitre 4 (1ereD, SVT), scène 08.

§ 4.6.3 Application à l'espèce humaine : l'albinisme (probabilités
1/4-1/2-1/4 dans une famille), attention à choisir le bon modèle selon le
type de croisement, et L'ESSENTIEL DU CHAPITRE en clôture. Source :
1ereD/SVT.pdf, pages 59-62.
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
    config,
)

from shapes.base_scene import NotionScene
from shapes.boxes import essentiel_box, example_box, scene_title, warning_box


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


class AlbinismeEtEssentielDuChapitre(NotionScene):
    def construct(self):
        titre = scene_title("4.6.3 — L'albinisme et essentiel du chapitre")
        titre.scale(0.6)
        titre.to_edge(UP)

        # --- Énoncé : l'albinisme, un caractère récessif chez l'Homme ----------
        application = example_box(
            Text(
                _wrap(
                    "L'albinisme est l'absence de mélanine (pigment de la "
                    "peau, des cheveux, des yeux). Chez l'Homme, la "
                    "pigmentation normale est dominante (A) ; l'albinisme "
                    "ne s'exprime qu'à l'état homozygote a/a. Une "
                    "personne A/a est porteuse : saine, mais peut "
                    "transmettre a.",
                    width=54,
                ),
                font_size=23,
            ),
            box_width=12.2,
        )
        application.next_to(titre, DOWN, buff=0.45)

        with self.voiceover(
            text=(
                "Appliquons tout ce chapitre à un exemple humain : "
                "l'albinisme. C'est l'absence de mélanine, le pigment qui "
                "colore la peau, les cheveux et les yeux. Chez l'Homme, la "
                "pigmentation normale est commandée par l'allèle dominant "
                "A ; l'albinisme ne s'exprime qu'à l'état homozygote a sur "
                "a. Une personne albinos est donc de génotype a sur a ; une "
                "personne de pigmentation normale est A sur A ou A sur a — "
                "dans ce dernier cas, on dit qu'elle est porteuse : elle ne "
                "présente pas le caractère, mais peut le transmettre."
            )
        ) as tracker:
            self.play(Write(titre))
            self.play(FadeIn(application))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(application))

        # --- Animation du raisonnement : couple de porteurs A/a x A/a ----------
        entete_echiquier = Text("Couple de porteurs : A/a x A/a", font_size=24, color=YELLOW, weight="BOLD")
        entete_echiquier.next_to(titre, DOWN, buff=0.5)

        def resultat_albinisme(gc, gr):
            allele1, allele2 = (gc, gr) if gc == "A" else (gr, gc)
            return f"{allele1}/{allele2}"

        ech = _echiquier(["A", "a"], ["A", "a"], resultat_albinisme)
        ech["ensemble"].next_to(entete_echiquier, DOWN, buff=0.4).shift(LEFT * 2.4)

        probas = MathTex(
            r"\dfrac{1}{4}\,A/A \quad \dfrac{1}{2}\,A/a \quad \dfrac{1}{4}\,a/a",
            font_size=24,
            color=WHITE,
        )
        probas.next_to(ech["ensemble"], DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Considérons un couple de porteurs, A sur a croisé avec A "
                "sur a. L'échiquier de croisement se construit exactement "
                "comme pour le maïs ou les belles-de-nuit : chaque parent "
                "produit un demi de gamètes A et un demi de gamètes a. On "
                "obtient un quart A sur A, un demi A sur a, un quart a sur "
                "a."
            )
        ) as tracker:
            self.play(FadeIn(entete_echiquier))
            self.play(Create(ech["grid"]))
            self.play(FadeIn(ech["corner"]), Write(ech["col_headers"]), Write(ech["row_headers"]))
            for ligne in ech["cellules"]:
                self.play(*[Write(cell) for cell in ligne])
            self.play(FadeIn(probas))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(entete_echiquier), FadeOut(ech["ensemble"]), FadeOut(probas))

        # --- Exemple traité : probabilités à chaque naissance ------------------
        exemple = example_box(
            Text(
                _wrap(
                    "Un couple de porteurs (A/a x A/a) a, À CHAQUE "
                    "naissance : 1/4 de risque d'enfant albinos (a/a), "
                    "1/2 de chance d'enfant porteur sain (A/a), 1/4 de "
                    "chance d'enfant sain non porteur (A/A). Ces "
                    "probabilités sont indépendantes d'une naissance à "
                    "l'autre : 2 enfants sains n'« épuisent » pas le "
                    "risque.",
                    width=54,
                ),
                font_size=22,
            ),
            box_width=12.3,
        )
        exemple.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Un couple de porteurs a, à chaque naissance, une "
                "probabilité d'un quart d'avoir un enfant albinos, a sur a, "
                "une probabilité d'un demi d'avoir un enfant porteur sain, "
                "A sur a, et une probabilité d'un quart d'avoir un enfant "
                "sain non porteur, A sur A. Ces probabilités sont "
                "indépendantes d'une naissance à l'autre : deux enfants "
                "sains n'épuisent pas le risque pour le troisième. En Côte "
                "d'Ivoire, où le soleil est intense, les personnes albinos "
                "doivent en outre se protéger la peau et les yeux des "
                "rayons ultraviolets : comprendre la génétique de ce "
                "caractère aide aussi à lutter contre les préjugés — "
                "l'albinisme est une simple question d'allèles, rien "
                "d'autre."
            )
        ) as tracker:
            self.play(FadeIn(exemple))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(exemple))

        # --- Piège à éviter : choisir le bon modèle avant de calculer ----------
        piege = warning_box(
            Text(
                _wrap(
                    "Avant de calculer, identifiez la situation : F1 de "
                    "lignées pures (100% dominants) ; F1xF1 avec "
                    "dominance complète (3/4-1/4) ; croisement-test (100% "
                    "ou 1/2-1/2) ; codominance (1/4-1/2-1/4, 3 "
                    "phénotypes) ; allèle létal (2/3-1/3 parmi les "
                    "vivants). Écrire « 3/4-1/4 » automatiquement à "
                    "chaque énoncé est l'erreur la plus grave du chapitre.",
                    width=54,
                ),
                font_size=21,
            ),
            box_width=12.4,
        )
        piege.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Attention, avant d'annoncer une proportion, il faut "
                "identifier la situation du problème. F1 de lignées pures : "
                "cent pour cent de dominants. F1 croisée avec F1, avec "
                "dominance complète : trois quarts, un quart. "
                "Croisement-test : cent pour cent, ou bien moitié-moitié. "
                "Codominance : un quart, un demi, un quart, avec trois "
                "phénotypes. Allèle létal : deux tiers, un tiers parmi les "
                "vivants. Écrire trois quarts, un quart automatiquement à "
                "chaque énoncé est l'erreur la plus grave du chapitre : la "
                "proportion dépend toujours du croisement réalisé."
            )
        ) as tracker:
            self.play(FadeIn(piege))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(piege))

        # --- À retenir : L'ESSENTIEL DU CHAPITRE (clôture) -----------------------
        essentiel = essentiel_box(
            _bullets(
                [
                    "Caractère héréditaire -> gène (locus) -> allèles ; "
                    "diploïde = 2 allèles/gène, séparés à la méiose "
                    "(pureté des gamètes).",
                    "Génotype (ex. V/v) commande le phénotype observable "
                    "(ex. [V]).",
                    "Homozygote = lignée pure (2 allèles identiques) ; "
                    "hétérozygote = hybride (2 allèles différents).",
                    "Dominant s'exprime même en 1 exemplaire ; récessif "
                    "seulement en 2. Phénotype récessif -> génotype "
                    "connu ; dominant -> inconnu (V/V ou V/v).",
                    "1ère loi de Mendel : 2 lignées pures croisées -> F1 "
                    "uniforme, de phénotype dominant.",
                    "2e loi de Mendel : F2 (F1xF1) = 3/4 dominant, 1/4 "
                    "récessif (génotypes 1/4-1/2-1/4), démontré par "
                    "l'échiquier de croisement.",
                    "Croisement-test (dominant x récessif) révèle le "
                    "génotype testé : 100% dominants si V/V, 1/2-1/2 si "
                    "V/v.",
                    "Codominance -> F2 en 1/4-1/2-1/4 (3 phénotypes) ; "
                    "allèle létal -> survivants en 2/3-1/3.",
                    "Toutes ces proportions sont théoriques : elles se "
                    "vérifient sur de grands effectifs, le hasard "
                    "explique les petits écarts.",
                ],
                font_size=18,
                width=54,
            ),
            box_width=12.8,
        )
        essentiel.next_to(titre, DOWN, buff=0.3)

        # Garde-fou : si le contenu (9 points) dépasse la hauteur visible du
        # cadre, on réduit l'échelle globale de la boîte pour qu'elle tienne
        # entièrement à l'écran (technique reprise de SVT_FonctionsGonades_09).
        _bas_visible = -config.frame_height / 2 + 0.3
        _hauteur_dispo = essentiel.get_top()[1] - _bas_visible
        if essentiel.height > _hauteur_dispo:
            essentiel.scale(_hauteur_dispo / essentiel.height, about_point=essentiel.get_top())

        with self.voiceover(
            text=(
                "Voici l'essentiel du chapitre. Un caractère héréditaire "
                "est commandé par un gène, situé à une place précise du "
                "chromosome, le locus ; les versions du gène sont les "
                "allèles. Un individu diploïde possède deux allèles par "
                "gène ; à la méiose, ils se séparent, chaque gamète n'en "
                "reçoit qu'un seul, c'est la pureté des gamètes. Le "
                "génotype commande le phénotype. Homozygote signifie deux "
                "allèles identiques, lignée pure ; hétérozygote signifie "
                "deux allèles différents, hybride. Un allèle dominant "
                "s'exprime même en un seul exemplaire ; un allèle récessif "
                "ne s'exprime qu'en deux exemplaires : un phénotype "
                "récessif révèle le génotype, un phénotype dominant le "
                "cache. Première loi de Mendel : le croisement de deux "
                "lignées pures donne une F1 uniforme, de phénotype "
                "dominant. Deuxième loi de Mendel : la F2 issue du "
                "croisement F1 fois F1 comporte trois quarts de phénotype "
                "dominant et un quart de phénotype récessif, ce que "
                "démontre l'échiquier de croisement. Le croisement-test "
                "révèle le génotype testé : cent pour cent de dominants si "
                "homozygote, moitié-moitié si hétérozygote. En codominance, "
                "l'hétérozygote a un phénotype intermédiaire, et la F2 "
                "compte un quart, un demi, un quart, avec trois "
                "phénotypes. Avec un allèle létal, un génotype meurt avant "
                "la naissance, et les proportions chez les vivants "
                "deviennent deux tiers, un tiers. Enfin, toutes ces "
                "proportions sont théoriques : elles se vérifient sur de "
                "grands effectifs, et le hasard de la fécondation explique "
                "les petits écarts."
            )
        ) as tracker:
            self.play(FadeIn(essentiel))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(titre), FadeOut(essentiel))
