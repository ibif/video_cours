"""
scenes/SVT_FecondationMammiferes_06.py — Chapitre 4 (1ereC, SVT), scène 06.

§ 4. Les conséquences de la fécondation : restauration de la diploïdie +
détermination du sexe de l'embryon (tableau de croisement gamète femelle/
mâle -> zygote -> sexe, méthode "échiquier") + piège "jamais la faute de
la mère". Source : 1ereC/SVT.pdf, page 39.
"""

import textwrap

from manim import DOWN, LEFT, RIGHT, UP, WHITE, YELLOW, FadeIn, FadeOut, MathTex, Text, VGroup, Write

from shapes.base_scene import NotionScene
from shapes.boxes import example_box, method_box, scene_title, warning_box


def _wrap(text: str, width: int = 56) -> str:
    return "\n".join(textwrap.fill(line, width=width) for line in text.split("\n"))


def _bullets(items, font_size=23, color=WHITE, width=50):
    lines = VGroup(
        *[Text(f"• {_wrap(it, width=width)}", font_size=font_size, color=color) for it in items]
    )
    lines.arrange(DOWN, aligned_edge=LEFT, buff=0.22)
    return lines


def _grid_table(cell_matrix, col_gap=0.5, row_gap=0.26):
    n_rows = len(cell_matrix)
    n_cols = len(cell_matrix[0])
    col_widths = [max(cell_matrix[r][c].width for r in range(n_rows)) for c in range(n_cols)]

    col_x = []
    x = 0.0
    for c in range(n_cols):
        col_x.append(x)
        x += col_widths[c] + col_gap

    table = VGroup()
    y = 0.0
    for r in range(n_rows):
        row_height = max(cell_matrix[r][c].height for c in range(n_cols))
        for c in range(n_cols):
            cell = cell_matrix[r][c]
            cell.move_to([col_x[c] + cell.width / 2, y - row_height / 2, 0])
            table.add(cell)
        y -= row_height + row_gap
    return table


class DeterminationSexeEmbryon(NotionScene):
    def construct(self):
        titre = scene_title("4.4 — La détermination du sexe de l'embryon")
        titre.scale(0.6)
        titre.to_edge(UP)

        # --- Énoncé : diploïdie restaurée + gonosomes ------------------------------
        intro = Text(
            _wrap(
                "Chez l'Homme, les 46 chromosomes comprennent 22 paires "
                "de chromosomes ordinaires (autosomes) et 1 paire de "
                "chromosomes sexuels (gonosomes) : la femme a deux "
                "chromosomes X (44+XX) ; l'homme a un X et un Y (44+XY).",
                width=56,
            ),
            font_size=24,
            color=WHITE,
        )
        intro.next_to(titre, DOWN, buff=0.55)

        with self.voiceover(
            text=(
                "Nous venons de voir que la fécondation restaure la "
                "diploïdie. Elle fixe aussi le sexe de l'embryon. Chez "
                "l'Homme, les quarante-six chromosomes comprennent "
                "vingt-deux paires de chromosomes ordinaires, appelés "
                "autosomes, et une paire de chromosomes sexuels, les "
                "gonosomes. La femme possède deux chromosomes X, son "
                "caryotype s'écrit quarante-quatre plus X X. L'homme "
                "possède un chromosome X et un chromosome Y : "
                "quarante-quatre plus X Y."
            )
        ) as tracker:
            self.play(Write(titre))
            self.play(FadeIn(intro))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(intro))

        # --- Raisonnement : tableau de croisement (échiquier) ---------------------
        entete_tab = Text("Tableau de croisement (échiquier)", font_size=25, color=YELLOW, weight="BOLD")
        entete_tab.next_to(titre, DOWN, buff=0.45)

        rows = [
            ("Gamète femelle", "Gamète mâle", "Zygote", "Sexe"),
            ("22+X", "22+X", "44+XX", "Fille"),
            ("22+X", "22+Y", "44+XY", "Garçon"),
        ]
        cell_matrix = []
        for i, row in enumerate(rows):
            color = YELLOW if i == 0 else WHITE
            weight = "BOLD" if i == 0 else "NORMAL"
            cell_matrix.append([Text(val, font_size=22, color=color, weight=weight) for val in row])

        tableau = _grid_table(cell_matrix, col_gap=0.6, row_gap=0.3)
        tableau.next_to(entete_tab, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Au cours de la gamétogenèse, la méiose sépare les "
                "chromosomes de chaque paire : tous les ovules portent un "
                "chromosome X, vingt-deux plus X. En revanche, la moitié "
                "des spermatozoïdes porte un chromosome X et l'autre "
                "moitié un chromosome Y. Raisonnons en tableau de "
                "croisement : un ovule vingt-deux plus X, fécondé par un "
                "spermatozoïde vingt-deux plus X, donne un zygote "
                "quarante-quatre plus X X, une fille. Le même ovule, "
                "fécondé par un spermatozoïde vingt-deux plus Y, donne un "
                "zygote quarante-quatre plus X Y, un garçon."
            )
        ) as tracker:
            self.play(FadeIn(entete_tab))
            self.play(FadeIn(tableau))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(entete_tab), FadeOut(tableau))

        # --- Exemple traité : probabilité sur une population ------------------------
        exemple = example_box(
            VGroup(
                Text(
                    _wrap(
                        "Sur 100 conceptions, la probabilité étant de 1/2 "
                        "à chaque fois : environ 50 conceptions donnent "
                        "un zygote XX (fille), et environ 50 donnent un "
                        "zygote XY (garçon), et cela indépendamment du "
                        "sexe des naissances précédentes dans la même "
                        "famille.",
                        width=52,
                    ),
                    font_size=21,
                ),
                MathTex(r"P(\text{fille}) = P(\text{garçon}) = \dfrac{1}{2}", font_size=28, color="#1A1A1A"),
            ).arrange(DOWN, buff=0.3),
            box_width=12.2,
        )
        exemple.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Prenons un exemple chiffré : sur cent conceptions, la "
                "probabilité étant de un demi à chaque fois, environ "
                "cinquante conceptions donnent un zygote X X, une fille, "
                "et environ cinquante donnent un zygote X Y, un garçon. "
                "Cela reste vrai indépendamment du sexe des naissances "
                "précédentes dans la même famille : chaque conception est "
                "un tirage indépendant."
            )
        ) as tracker:
            self.play(FadeIn(exemple))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(exemple))

        # --- À retenir : le père est le déterminant --------------------------------
        methode = method_box(
            Text(
                _wrap(
                    "Le sexe de l'enfant dépend uniquement du "
                    "spermatozoïde qui féconde l'ovule : le père est donc "
                    "le « déterminant » du sexe. La probabilité d'avoir "
                    "une fille ou un garçon est de 1/2 à chaque "
                    "grossesse, indépendamment des naissances "
                    "précédentes.",
                    width=54,
                ),
                font_size=22,
            ),
            box_width=12.4,
        )
        methode.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Retenons ce point clé : le sexe de l'enfant dépend "
                "uniquement du spermatozoïde qui féconde l'ovule ; c'est "
                "donc le père qui est le « déterminant » du sexe. La "
                "probabilité d'avoir une fille ou un garçon est de un "
                "demi à chaque grossesse, indépendamment des naissances "
                "précédentes."
            )
        ) as tracker:
            self.play(FadeIn(methode))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(methode))

        # --- Piège à éviter : jamais la faute de la mère ---------------------------
        piege = warning_box(
            Text(
                _wrap(
                    "Il est faux et injuste de « reprocher » à une femme "
                    "de ne donner naissance qu'à des filles (croyance "
                    "encore répandue). La mère ne fournit que des ovules "
                    "à chromosome X ; c'est le spermatozoïde du père (X "
                    "ou Y) qui fixe le sexe.",
                    width=54,
                ),
                font_size=23,
            ),
            box_width=12.2,
        )
        piege.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Attention à une croyance encore répandue et injuste : il "
                "est faux de reprocher à une femme de ne donner naissance "
                "qu'à des filles. La mère ne fournit que des ovules à "
                "chromosome X ; c'est uniquement le spermatozoïde du "
                "père, porteur d'un X ou d'un Y, qui fixe le sexe de "
                "l'enfant."
            )
        ) as tracker:
            self.play(FadeIn(piege))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(titre), FadeOut(piege))
