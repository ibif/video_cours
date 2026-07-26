"""
scenes/SVT_ExpressionGenetique_05.py — Chapitre 5 (1ereC, SVT), scène 05.

II.D. Les acides ribonucléiques (ARN) : tableau comparatif ADN/ARN (sucre,
bases, structure, localisation) et les 3 types d'ARN impliqués dans la
synthèse des protéines (ARNm, ARNt, ARNr) avec leur rôle.
Source : 1ereC/SVT.pdf, page 47.
"""

import textwrap

from manim import DOWN, UP, WHITE, YELLOW, FadeIn, FadeOut, MathTex, Text, VGroup, Write

from shapes.base_scene import NotionScene
from shapes.boxes import definition_box, scene_title, warning_box


def _wrap(text: str, width: int = 56) -> str:
    return "\n".join(textwrap.fill(line, width=width) for line in text.split("\n"))


def _grid_table(cell_matrix, col_gap=0.7, row_gap=0.3):
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


class LesAcidesRibonucleiques(NotionScene):
    def construct(self):
        titre = scene_title("II.D — Les acides ribonucléiques (ARN)")
        titre.scale(0.55)
        titre.to_edge(UP)

        with self.voiceover(
            text=(
                "L'ARN est l'intermédiaire indispensable entre l'ADN et la "
                "protéine. Comparons-le d'abord à l'ADN, avant de découvrir "
                "les trois types d'ARN qui participent à la synthèse des "
                "protéines."
            )
        ) as tracker:
            self.play(Write(titre))
            self.wait(tracker.get_remaining_duration())

        # --- Énoncé / raisonnement : tableau comparatif ADN / ARN --------------
        entete_tab = Text("Comparaison ADN / ARN", font_size=25, color=YELLOW, weight="BOLD")
        entete_tab.next_to(titre, DOWN, buff=0.45)

        rows = [
            ("Sucre", "désoxyribose", "ribose"),
            ("Bases azotées", "A, T, G, C", "A, U, G, C"),
            ("Structure", "double brin", "simple brin (général.)"),
            ("Localisation", "noyau", "fabriqué au noyau, agit au cytoplasme"),
        ]
        cell_matrix = [[
            Text("Caractère", font_size=20, color=YELLOW, weight="BOLD"),
            Text("ADN", font_size=20, color=YELLOW, weight="BOLD"),
            Text("ARN", font_size=20, color=YELLOW, weight="BOLD"),
        ]]
        for carac, adn, arn in rows:
            cell_matrix.append([
                Text(carac, font_size=19, color=WHITE),
                Text(adn, font_size=19, color=WHITE),
                Text(arn, font_size=19, color=WHITE),
            ])
        tableau = _grid_table(cell_matrix, col_gap=0.55, row_gap=0.28)
        tableau.next_to(entete_tab, DOWN, buff=0.4)
        tableau.scale(0.85)

        with self.voiceover(
            text=(
                "Les ARN sont des acides nucléiques voisins de l'ADN, avec "
                "trois différences importantes. Le sucre : désoxyribose "
                "pour l'ADN, ribose pour l'ARN. Les bases azotées : A, T, G, "
                "C pour l'ADN ; mais dans l'ARN, l'uracile U remplace la "
                "thymine, on a donc A, U, G, C. La structure : l'ADN est "
                "double brin, en double hélice ; l'ARN est généralement "
                "simple brin. Enfin la localisation : l'ADN reste dans le "
                "noyau, tandis que l'ARN, fabriqué dans le noyau, agit "
                "surtout dans le cytoplasme."
            )
        ) as tracker:
            self.play(FadeIn(entete_tab))
            self.play(FadeIn(tableau))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(entete_tab), FadeOut(tableau))

        # --- Piège : U remplace T, et l'appariement A-U -------------------------
        appariement = MathTex(r"A \;-\; U \quad (2\ \text{liaisons hydrogène})", font_size=28, color=WHITE)
        piege = warning_box(
            VGroup(
                Text(
                    _wrap(
                        "Dans les ARN, l'uracile U remplace la thymine T. "
                        "L'uracile est complémentaire de l'adénine :",
                        width=54,
                    ),
                    font_size=22,
                ),
                appariement,
            ).arrange(DOWN, buff=0.25),
            box_width=11.8,
        )
        piege.next_to(titre, DOWN, buff=0.55)

        with self.voiceover(
            text=(
                "Retenez bien cette différence : dans les ARN, l'uracile U "
                "remplace la thymine T. L'uracile est complémentaire de "
                "l'adénine, avec le même nombre de liaisons hydrogène que la "
                "paire A-T : deux liaisons hydrogène."
            )
        ) as tracker:
            self.play(FadeIn(piege))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(piege))

        # --- À retenir : les 3 types d'ARN --------------------------------------
        entete_types = Text("Trois types d'ARN pour la synthèse des protéines", font_size=22, color=YELLOW, weight="BOLD")
        entete_types.next_to(titre, DOWN, buff=0.5)

        types_cells = [[
            Text("Type", font_size=19, color=YELLOW, weight="BOLD"),
            Text("Nom complet", font_size=19, color=YELLOW, weight="BOLD"),
            Text("Rôle", font_size=19, color=YELLOW, weight="BOLD"),
        ]]
        data_types = [
            ("ARNm", "ARN messager", "porte la copie de l'info. du gène,\ndu noyau vers le cytoplasme"),
            ("ARNt", "ARN de transfert", "transporte les acides aminés,\nreconnaît les codons de l'ARNm"),
            ("ARNr", "ARN ribosomique", "constituant principal\ndes ribosomes"),
        ]
        for sym, nom, role in data_types:
            types_cells.append([
                Text(sym, font_size=19, color=WHITE, weight="BOLD"),
                Text(nom, font_size=18, color=WHITE),
                Text(role, font_size=16, color=WHITE),
            ])
        tableau_types = _grid_table(types_cells, col_gap=0.5, row_gap=0.3)
        tableau_types.next_to(entete_types, DOWN, buff=0.4)
        tableau_types.scale(0.85)

        with self.voiceover(
            text=(
                "Trois types d'ARN participent directement à la synthèse des "
                "protéines. L'ARN messager, ou ARNm, porte la copie de "
                "l'information du gène, du noyau vers le cytoplasme. L'ARN "
                "de transfert, ou ARNt, transporte les acides aminés jusqu'au "
                "ribosome et reconnaît les codons de l'ARNm. Et l'ARN "
                "ribosomique, ou ARNr, est le constituant principal des "
                "ribosomes, l'atelier où se fabriquent les protéines."
            )
        ) as tracker:
            self.play(FadeIn(entete_types))
            self.play(FadeIn(tableau_types))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(entete_types), FadeOut(tableau_types))

        definition = definition_box(
            Text(
                _wrap(
                    "L'ARN diffère de l'ADN par son sucre (ribose), sa base "
                    "uracile (U, à la place de T) et sa structure "
                    "généralement simple brin. Trois types d'ARN "
                    "interviennent dans la synthèse des protéines : ARNm "
                    "(messager), ARNt (transfert) et ARNr (ribosomique).",
                    width=54,
                ),
                font_size=22,
            ),
            box_width=11.8,
        )
        definition.next_to(titre, DOWN, buff=0.55)

        with self.voiceover(
            text=(
                "Retenons l'essentiel : l'ARN diffère de l'ADN par son "
                "sucre, le ribose, par sa base uracile qui remplace la "
                "thymine, et par sa structure généralement simple brin. "
                "Trois types d'ARN interviennent dans la synthèse des "
                "protéines : l'ARN messager, l'ARN de transfert et l'ARN "
                "ribosomique. Nous allons maintenant détailler la première "
                "grande étape : la transcription."
            )
        ) as tracker:
            self.play(FadeIn(definition))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(titre), FadeOut(definition))
