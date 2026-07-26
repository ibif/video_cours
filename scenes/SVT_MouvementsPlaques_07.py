"""
scenes/SVT_MouvementsPlaques_07.py — Chapitre 7 (1ereD, SVT), scène 07.

§ 7.3.3 Le coulissage (faille transformante, San Andreas), le tableau
récapitulatif des trois types de limites et la méthode d'identification
du type de limite à partir de documents. Source : 1ereD/SVT.pdf, pages
96-97.
"""

import textwrap

from manim import (
    DOWN,
    GRAY_C,
    LEFT,
    ORANGE,
    RIGHT,
    UP,
    WHITE,
    YELLOW,
    Arrow,
    FadeIn,
    FadeOut,
    Rectangle,
    Text,
    VGroup,
    Write,
    config,
)

from shapes.base_scene import NotionScene
from shapes.boxes import definition_box, method_box, scene_title


def _wrap(text: str, width: int = 56) -> str:
    return "\n".join(textwrap.fill(line, width=width) for line in text.split("\n"))


def _bullets(items, font_size=22, color=WHITE, width=52):
    lines = VGroup(
        *[Text(f"• {_wrap(it, width=width)}", font_size=font_size, color=color) for it in items]
    )
    lines.arrange(DOWN, aligned_edge=LEFT, buff=0.25)
    return lines


def _grid_table(cell_matrix, col_gap=0.4, row_gap=0.2):
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


def _schema_coulissage():
    """Deux blocs de lithosphère qui glissent horizontalement l'un contre l'autre."""
    bloc_haut = Rectangle(width=6.5, height=0.8, fill_color=ORANGE, fill_opacity=0.75, stroke_color=WHITE, stroke_width=1)
    bloc_bas = Rectangle(width=6.5, height=0.8, fill_color=GRAY_C, fill_opacity=0.85, stroke_color=WHITE, stroke_width=1)
    bloc_haut.move_to(UP * 0.42)
    bloc_bas.move_to(DOWN * 0.42)

    faille = Rectangle(width=6.5, height=0.04, fill_color=YELLOW, fill_opacity=1, stroke_width=0)

    fleche_haut = Arrow(start=[-1.0, 0.42, 0], end=[1.0, 0.42, 0], color=WHITE, buff=0, stroke_width=4)
    fleche_bas = Arrow(start=[1.0, -0.42, 0], end=[-1.0, -0.42, 0], color=WHITE, buff=0, stroke_width=4)

    label_faille = Text("faille transformante", font_size=15, color=YELLOW)
    label_faille.next_to(VGroup(bloc_haut, bloc_bas), DOWN, buff=0.35)

    return VGroup(bloc_haut, bloc_bas, faille, fleche_haut, fleche_bas, label_faille)


class CoulissageEtSynthese(NotionScene):
    def construct(self):
        titre = scene_title("7.3.3 — Le coulissage et synthèse des limites")
        titre.scale(0.58)
        titre.to_edge(UP)

        # --- Énoncé : définition de la faille transformante --------------------
        definition_faille = definition_box(
            Text(
                _wrap(
                    "Deux plaques coulissent horizontalement le long d'une "
                    "faille transformante. Ni création ni destruction de "
                    "lithosphère. Le frottement provoque des séismes "
                    "fréquents mais superficiels, aucun volcanisme. Exemple : "
                    "faille de San Andreas en Californie (plaque pacifique "
                    "coulisse le long de la plaque nord-américaine).",
                    width=54,
                ),
                font_size=20,
            ),
            box_width=11.8,
        )
        definition_faille.next_to(titre, DOWN, buff=0.5)

        schema_coul = _schema_coulissage()
        schema_coul.next_to(definition_faille, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Il existe un troisième et dernier type de limite : le "
                "coulissage. Deux plaques coulissent alors horizontalement "
                "l'une contre l'autre, le long d'une faille dite "
                "transformante. Il n'y a ici ni création ni destruction de "
                "lithosphère. Le frottement entre les deux plaques provoque "
                "des séismes fréquents, mais superficiels, et aucun "
                "volcanisme. L'exemple le plus célèbre est la faille de "
                "San Andreas, en Californie, où la plaque pacifique "
                "coulisse le long de la plaque nord-américaine."
            )
        ) as tracker:
            self.play(Write(titre))
            self.play(FadeIn(definition_faille))
            self.play(FadeIn(schema_coul))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(definition_faille), FadeOut(schema_coul))

        # --- Animation du raisonnement : tableau récapitulatif des 3+1 types --
        entete_tab = Text("Tableau récapitulatif des limites de plaques", font_size=21, color=YELLOW, weight="BOLD")
        entete_tab.next_to(titre, DOWN, buff=0.4)

        header = [
            Text("Type", font_size=15, color=YELLOW, weight="BOLD"),
            Text("Mouvement", font_size=15, color=YELLOW, weight="BOLD"),
            Text("Relief", font_size=15, color=YELLOW, weight="BOLD"),
            Text("Séismes", font_size=15, color=YELLOW, weight="BOLD"),
            Text("Volcanisme", font_size=15, color=YELLOW, weight="BOLD"),
            Text("Exemple", font_size=15, color=YELLOW, weight="BOLD"),
        ]
        rows = [
            ("Divergente", "écartement", "dorsale / rift", "superficiels", "basaltes fluides", "dorsale médio-\natlantique"),
            ("Convergente\n(subduction)", "rapprochement\n+ plongée", "fosse / arc\nvolcanique", "superf. à très\nprofonds (700km)", "explosif", "Andes, Japon"),
            ("Convergente\n(collision)", "rapprochement\n+ déformation", "chaîne de\nmontagnes", "superficiels", "absent", "Himalaya"),
            ("Transformante", "coulissage", "faille", "superficiels", "absent", "San Andreas"),
        ]
        cell_matrix = [header]
        for row in rows:
            cell_matrix.append([Text(v, font_size=13, color=WHITE) for v in row])
        tableau = _grid_table(cell_matrix, col_gap=0.3, row_gap=0.15)
        tableau.next_to(entete_tab, DOWN, buff=0.3)
        tableau.scale(0.85)

        _bas_visible = -config.frame_height / 2 + 0.3
        _hauteur_dispo = tableau.get_top()[1] - _bas_visible
        if tableau.height > _hauteur_dispo:
            tableau.scale(_hauteur_dispo / tableau.height, about_point=tableau.get_top())

        with self.voiceover(
            text=(
                "Récapitulons les quatre situations dans un tableau. Limite "
                "divergente : écartement, dorsale ou rift, séismes "
                "superficiels, volcanisme de basaltes fluides, exemple la "
                "dorsale médio-atlantique. Limite convergente en "
                "subduction : rapprochement et plongée, fosse et arc "
                "volcanique, séismes superficiels à très profonds, jusqu'à "
                "sept cents kilomètres, volcanisme explosif, exemple les "
                "Andes ou le Japon. Limite convergente en collision : "
                "rapprochement et déformation, chaîne de montagnes, séismes "
                "superficiels, aucun volcanisme, exemple l'Himalaya. Limite "
                "transformante : coulissage, faille, séismes superficiels, "
                "aucun volcanisme, exemple San Andreas."
            )
        ) as tracker:
            self.play(FadeIn(entete_tab))
            self.play(FadeIn(tableau))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(entete_tab), FadeOut(tableau))

        # --- À retenir : méthode d'identification du type de limite -----------
        methode = method_box(
            _bullets(
                [
                    "Étape 1 : relever les indices (fosse ? volcans ? chaîne de "
                    "montagnes ? faille ? profondeur des séismes ?).",
                    "Étape 2 : en déduire le mouvement relatif des plaques.",
                    "Étape 3 : nommer la limite et citer un exemple "
                    "géographique conforme.",
                ],
                font_size=21,
                width=52,
            ),
            box_width=12.0,
        )
        methode.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Face à des documents inconnus, comment identifier le type "
                "de limite de plaques ? Suivez toujours la même méthode en "
                "trois étapes. Un : relève les indices présents, présence "
                "d'une fosse, de volcans, d'une chaîne de montagnes, d'une "
                "faille, profondeur des séismes. Deux : déduis-en le "
                "mouvement relatif des plaques, écartement, rapprochement "
                "ou coulissage. Trois : nomme précisément la limite, "
                "divergente, convergente en subduction, convergente en "
                "collision, ou transformante, et cite un exemple "
                "géographique conforme."
            )
        ) as tracker:
            self.play(FadeIn(methode))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(titre), FadeOut(methode))
