"""
scenes/SVT_MeioseChromosomes_08.py — Chapitre 2 (1ereC, SVT), scène 08.

§ Comparaison méiose/mitose (tableau complet à 9 critères) + conséquences
de la méiose (cycle méiose→fécondation→mitoses qui maintient le caryotype
constant).
Source : 1ereC/SVT.pdf, pages 18-19.
"""

import textwrap

from manim import (
    DOWN,
    LEFT,
    RIGHT,
    UP,
    WHITE,
    YELLOW,
    FadeIn,
    FadeOut,
    MathTex,
    Text,
    VGroup,
    Write,
    config,
)

from shapes.base_scene import NotionScene
from shapes.boxes import method_box, scene_title


def _wrap(text: str, width: int = 56) -> str:
    return "\n".join(textwrap.fill(line, width=width) for line in text.split("\n"))


def _bullets(items, font_size=21, color=WHITE, width=52):
    lines = VGroup(
        *[Text(f"• {_wrap(it, width=width)}", font_size=font_size, color=color) for it in items]
    )
    lines.arrange(DOWN, aligned_edge=LEFT, buff=0.22)
    return lines


def _grid_table(cell_matrix, col_gap=0.5, row_gap=0.22):
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


class ComparaisonMeioseEtMitoseConsequences(NotionScene):
    def construct(self):
        titre = scene_title("2.6 — Méiose vs mitose")
        titre.scale(0.65)
        titre.to_edge(UP)

        # --- Énoncé : pourquoi comparer -------------------------------------
        enonce = Text(
            _wrap(
                "La méiose et la mitose sont les deux seuls modes de "
                "division cellulaire de l'Homme. Elles diffèrent sur presque "
                "tous les points : lieu, nombre de divisions, résultat.",
                width=54,
            ),
            font_size=22,
            color=WHITE,
        )
        enonce.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "La méiose et la mitose sont les deux seuls modes de "
                "division cellulaire de l'être humain. Elles diffèrent "
                "pourtant sur presque tous les points : le lieu où elles se "
                "déroulent, le nombre de divisions, et le résultat final. "
                "Comparons-les critère par critère."
            )
        ) as tracker:
            self.play(Write(titre))
            self.play(FadeIn(enonce))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(enonce))

        # --- Animation du raisonnement : tableau comparatif complet -------------
        entete = Text("Tableau comparatif", font_size=24, color=YELLOW, weight="BOLD")
        entete.next_to(titre, DOWN, buff=0.4)

        rows = [
            ("Critère", "Mitose", "Méiose"),
            ("Lieu", "Cellules somatiques", "Gonades uniquement"),
            ("Nb de divisions", "1", "2 (réduct. + équat.)"),
            ("Nb de réplications", "1", "1 (pour 2 divisions)"),
            ("Appariement homologues", "Non", "Oui (bivalents, proph. I)"),
            ("Crossing-over", "Non", "Oui (prophase I)"),
            ("Nb de cellules filles", "2", "4"),
            ("Stock chromosomique", "2n (diploïde)", "n (haploïde)"),
            ("Patrimoine génétique", "Identique à la mère", "Différent (brassages)"),
            ("Rôle", "Croissance, réparation", "Formation des gamètes"),
        ]
        cell_matrix = []
        for i, row in enumerate(rows):
            color = YELLOW if i == 0 else WHITE
            weight = "BOLD" if i == 0 else "NORMAL"
            cell_matrix.append([Text(val, font_size=15, color=color, weight=weight) for val in row])

        tableau = _grid_table(cell_matrix, col_gap=0.4, row_gap=0.2)
        tableau.next_to(entete, DOWN, buff=0.3)

        # Garde-fou auto-scale : le tableau (9 lignes x 3 colonnes) peut
        # dépasser la hauteur visible du cadre ; on réduit l'échelle globale
        # pour qu'il tienne entièrement à l'écran.
        _bas_visible = -config.frame_height / 2 + 0.3
        _hauteur_dispo = tableau.get_top()[1] - _bas_visible
        if tableau.height > _hauteur_dispo:
            tableau.scale(_hauteur_dispo / tableau.height, about_point=tableau.get_top())

        with self.voiceover(
            text=(
                "Voici le tableau comparatif complet. La mitose se déroule "
                "dans toutes les cellules somatiques, la méiose uniquement "
                "dans les gonades. La mitose ne compte qu'une seule "
                "division, la méiose en compte deux, réductionnelle puis "
                "équationnelle, pour une seule réplication de l'ADN. Il n'y "
                "a pas d'appariement des homologues ni de crossing-over en "
                "mitose ; les deux existent en méiose, en prophase I. La "
                "mitose produit deux cellules filles diploïdes, identiques à "
                "la cellule mère ; la méiose en produit quatre, haploïdes, "
                "génétiquement différentes, grâce aux brassages. Enfin, la "
                "mitose assure la croissance et la réparation des tissus, "
                "tandis que la méiose assure la formation des gamètes."
            )
        ) as tracker:
            self.play(FadeIn(entete))
            self.play(FadeIn(tableau))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(entete), FadeOut(tableau))

        # --- À retenir : point clé synthétique -----------------------------------
        point_cle = method_box(
            Text(
                _wrap(
                    "La mitose CONSERVE (même nombre de chromosomes, même "
                    "information génétique) ; la méiose RÉDUIT et "
                    "DIVERSIFIE (moitié de chromosomes, cellules toutes "
                    "différentes).",
                    width=52,
                ),
                font_size=22,
            ),
            box_width=11.8,
        )
        point_cle.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Retenez ce point clé : la mitose conserve — même nombre de "
                "chromosomes, même information génétique — tandis que la "
                "méiose réduit et diversifie — moitié de chromosomes, "
                "cellules toutes différentes."
            )
        ) as tracker:
            self.play(FadeIn(point_cle))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(point_cle))

        # --- Exemple traité : conséquences, le cycle méiose-fécondation --------
        cycle_titre = Text("Conséquences : le cycle méiose - fécondation", font_size=22, color=YELLOW, weight="BOLD")
        cycle_titre.next_to(titre, DOWN, buff=0.5)

        cycle = MathTex(
            r"\text{adulte } (2n) \xrightarrow{\text{méiose}} \text{gamètes } (n) "
            r"\xrightarrow{\text{fécondation}} \text{zygote } (2n) "
            r"\xrightarrow{\text{mitoses}} \text{adulte } (2n)",
            font_size=22,
            color=WHITE,
        )
        cycle.next_to(cycle_titre, DOWN, buff=0.5)

        cycle_texte = Text(
            _wrap(
                "La méiose fait passer le stock chromosomique de 2n à n. "
                "Sans elle, le nombre de chromosomes doublerait à chaque "
                "génération lors de la fécondation. L'alternance "
                "méiose-fécondation forme un cycle qui maintient le "
                "caryotype constant.",
                width=54,
            ),
            font_size=20,
            color=WHITE,
        )
        cycle_texte.next_to(cycle, DOWN, buff=0.45)

        with self.voiceover(
            text=(
                "La méiose fait passer le stock chromosomique de deux n à "
                "n. Sans elle, le nombre de chromosomes doublerait à chaque "
                "génération lors de la fécondation. L'alternance entre "
                "méiose et fécondation forme donc un cycle : un adulte, à "
                "deux n chromosomes, produit par méiose des gamètes à n "
                "chromosomes ; la fécondation reforme un zygote à deux n "
                "chromosomes ; les mitoses développent ce zygote en un "
                "nouvel adulte, toujours à deux n chromosomes. Ce cycle "
                "maintient le caryotype constant, génération après "
                "génération."
            )
        ) as tracker:
            self.play(FadeIn(cycle_titre))
            self.play(Write(cycle))
            self.play(FadeIn(cycle_texte))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(titre), FadeOut(cycle_titre), FadeOut(cycle), FadeOut(cycle_texte))
