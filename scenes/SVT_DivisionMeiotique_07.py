"""
scenes/SVT_DivisionMeiotique_07.py — Chapitre 2 (1ereD, SVT), scène 07.

§ 2.4.1-2.4.2 Méiose, fécondation et cycle de vie (constance de la
formule chromosomique, exemple humain + raisonnement par l'absurde du
doublement) ; comparaison méiose / mitose (tableau comparatif), piège sur
les rôles respectifs. Source : 1ereD/SVT.pdf, pages 26-28.
"""

import textwrap

from manim import DOWN, LEFT, RIGHT, UP, WHITE, YELLOW, FadeIn, FadeOut, MathTex, Text, VGroup, Write

from shapes.base_scene import NotionScene
from shapes.boxes import example_box, property_box, scene_title, warning_box


def _wrap(text: str, width: int = 56) -> str:
    return "\n".join(textwrap.fill(line, width=width) for line in text.split("\n"))


def _bullets(items, font_size=22, color=WHITE, width=52):
    lines = VGroup(
        *[Text(f"• {_wrap(it, width=width)}", font_size=font_size, color=color) for it in items]
    )
    lines.arrange(DOWN, aligned_edge=LEFT, buff=0.22)
    return lines


def _grid_table(cell_matrix, col_gap=0.6, row_gap=0.28):
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


class MeioseFecondationEtComparaisonMitose(NotionScene):
    def construct(self):
        titre = scene_title("2.4 — Méiose, fécondation et comparaison avec la mitose")
        titre.scale(0.52)
        titre.to_edge(UP)

        # --- Énoncé : le cycle méiose / fécondation / mitoses -------------------
        cycle = MathTex(
            r"2n \;\xrightarrow{\text{méiose}}\; n \qquad n + n \;\xrightarrow{\text{fécondation}}\; 2n \qquad 2n \;\xrightarrow{\text{mitoses}}\; 2n",
            font_size=26,
            color=WHITE,
        )
        cycle.next_to(titre, DOWN, buff=0.6)

        with self.voiceover(
            text=(
                "La méiose produit des gamètes haploïdes, à n. Lors de la "
                "fécondation, un gamète mâle et un gamète femelle unissent "
                "leurs noyaux : leurs lots de chromosomes s'additionnent, n "
                "plus n égale deux n, et l'œuf obtenu est à nouveau "
                "diploïde. Cet œuf se divise ensuite par mitoses pour donner "
                "tous les tissus du nouvel individu, dont les futures "
                "gonades où, un jour, la méiose produira de nouveaux "
                "gamètes. Le cycle de vie alterne donc sans fin."
            )
        ) as tracker:
            self.play(Write(titre))
            self.play(Write(cycle))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(cycle))

        propriete = property_box(
            Text(
                _wrap(
                    "La méiose divise par deux le nombre de chromosomes "
                    "(2n donne n) ; la fécondation le rétablit (n+n redonne "
                    "2n). L'alternance méiose-fécondation assure la "
                    "constance du nombre de chromosomes de l'espèce au fil "
                    "des générations.",
                    width=54,
                ),
                font_size=23,
            ),
            box_width=11.8,
        )
        propriete.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Retenons cette propriété essentielle : la méiose divise par "
                "deux le nombre de chromosomes, deux n donne n ; la "
                "fécondation le rétablit, n plus n redonne deux n. "
                "L'alternance méiose-fécondation assure ainsi la constance "
                "du nombre de chromosomes de l'espèce au fil des "
                "générations."
            )
        ) as tracker:
            self.play(FadeIn(propriete))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(propriete))

        # --- Animation du raisonnement : exemple par l'absurde -------------------
        exemple = example_box(
            Text(
                _wrap(
                    "Réalité : spz n=23 + ovule n=23 -> zygote 23+23=46=2n. "
                    "Par l'absurde, SANS méiose : gamètes à 46 chacun -> "
                    "zygote 46+46=92 -> génération suivante "
                    "92+92=184... Le nombre DOUBLERAIT à chaque "
                    "génération : incompatible avec la vie de l'espèce.",
                    width=54,
                ),
                font_size=21,
            ),
            box_width=12.2,
        )
        exemple.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Vérifions ce mécanisme chez l'être humain, puis montrons "
                "par le calcul pourquoi la méiose est indispensable. Les "
                "spermatozoïdes du père contiennent n égale vingt-trois "
                "chromosomes, les ovules de la mère aussi. À la fécondation, "
                "le zygote reçoit vingt-trois plus vingt-trois égale "
                "quarante-six égale deux n chromosomes : la formule de "
                "l'espèce est respectée. Supposons maintenant, par "
                "l'absurde, que les gamètes soient produits sans méiose. Ils "
                "porteraient alors quarante-six chromosomes chacun. Le "
                "zygote de la génération suivante en aurait quarante-six "
                "plus quarante-six, soit quatre-vingt-douze. En continuant "
                "ainsi, la génération d'après recevrait quatre-vingt-douze "
                "plus quatre-vingt-douze, soit cent quatre-vingt-quatre : le "
                "nombre doublerait à chaque génération, ce qui est "
                "incompatible avec la vie de l'espèce. Seule la méiose, en "
                "réduisant de moitié le nombre de chromosomes des gamètes, "
                "permet à la fécondation de maintenir deux n constant."
            )
        ) as tracker:
            self.play(FadeIn(exemple))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(exemple))

        # --- Tableau comparatif méiose / mitose -----------------------------------
        entete_tab = Text("Méiose et mitose : comparaison", font_size=26, color=YELLOW, weight="BOLD")
        entete_tab.next_to(titre, DOWN, buff=0.5)

        rows = [
            ("Critère", "Mitose", "Méiose"),
            ("Nb de divisions", "1", "2"),
            ("Réplication de l'ADN", "1", "1 (avant la 1ère)"),
            ("Cellules filles", "2, identiques, 2n", "4, différentes, n"),
            ("Bivalents / enjambements", "non", "oui (prophase I)"),
            ("Lieu (être humain)", "tout le corps", "gonades"),
            ("Rôle", "croissance", "gamètes"),
        ]
        cell_matrix = []
        for i, row in enumerate(rows):
            color = YELLOW if i == 0 else WHITE
            weight = "BOLD" if i == 0 else "NORMAL"
            cell_matrix.append([Text(val, font_size=18, color=color, weight=weight) for val in row])

        tableau = _grid_table(cell_matrix, col_gap=0.55, row_gap=0.26)
        tableau.next_to(entete_tab, DOWN, buff=0.35)
        tableau.scale(0.9)

        with self.voiceover(
            text=(
                "Comparons maintenant méiose et mitose. La mitose ne compte "
                "qu'une seule division, la méiose en compte deux. Les deux "
                "sont précédées d'une seule réplication de l'ADN. La mitose "
                "donne deux cellules filles identiques, à deux n ; la méiose "
                "en donne quatre, toutes différentes, à n. Les bivalents et "
                "les enjambements n'existent qu'en méiose, en prophase I. "
                "Chez l'être humain, la mitose se produit dans toutes les "
                "cellules du corps, la méiose uniquement dans les gonades. "
                "Enfin, la mitose sert à la croissance et au renouvellement "
                "cellulaire, la méiose à la formation des gamètes."
            )
        ) as tracker:
            self.play(FadeIn(entete_tab))
            self.play(FadeIn(tableau))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(entete_tab), FadeOut(tableau))

        # --- À retenir : 3 indices pour distinguer sur un document -----------------
        indices = _bullets(
            [
                "Des bivalents ou des enjambements visibles -> c'est "
                "forcément la méiose.",
                "Deux divisions (ou 4 cellules au final) -> méiose. Une "
                "seule division, 2 cellules -> mitose.",
                "Cellules filles haploïdes (n) -> méiose. Diploïdes (2n) "
                "-> mitose.",
            ],
            width=52,
        )
        entete_indices = Text("3 indices pour distinguer mitose et méiose", font_size=24, color=YELLOW, weight="BOLD")
        entete_indices.next_to(titre, DOWN, buff=0.5)
        indices.next_to(entete_indices, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Pour distinguer mitose et méiose sur un document, trois "
                "indices suffisent presque toujours. Un : des bivalents, "
                "c'est-à-dire des homologues accolés, ou des enjambements "
                "sont visibles - c'est forcément la méiose. Deux : deux "
                "divisions se succèdent, ou quatre cellules au final : "
                "méiose. Une seule division, deux cellules : mitose. Trois : "
                "les cellules filles sont haploïdes, à n : méiose. Elles "
                "restent diploïdes, à deux n : mitose."
            )
        ) as tracker:
            self.play(FadeIn(entete_indices))
            self.play(FadeIn(indices))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(entete_indices), FadeOut(indices))

        # --- Piège à éviter -------------------------------------------------------------
        piege = warning_box(
            Text(
                _wrap(
                    "N'attribue pas à la méiose le rôle de la mitose : la "
                    "mitose sert à la croissance et au renouvellement des "
                    "cellules (formule 2n conservée, cellules identiques) ; "
                    "la méiose sert uniquement à produire des gamètes "
                    "haploïdes. Écrire « la méiose permet la croissance » ou "
                    "« la mitose produit les gamètes » est une double "
                    "erreur.",
                    width=56,
                ),
                font_size=22,
            ),
            box_width=12.2,
        )
        piege.next_to(titre, DOWN, buff=0.55)

        with self.voiceover(
            text=(
                "Attention à ne pas attribuer à la méiose le rôle de la "
                "mitose. La mitose sert à la croissance et au renouvellement "
                "des cellules : elle conserve la formule deux n et produit "
                "des cellules identiques. La méiose sert uniquement à "
                "produire des cellules reproductrices haploïdes. Écrire que "
                "la méiose permet la croissance, ou que la mitose produit "
                "les gamètes, est une double erreur."
            )
        ) as tracker:
            self.play(FadeIn(piege))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(titre), FadeOut(piege))
