"""
scenes/SVT_MouvementsPlaques_03.py — Chapitre 7 (1ereD, SVT), scène 03.

§ 7.1.3 Les plaques lithosphériques : définition, carte simplifiée et
tableau des principales plaques, exemple de la Côte d'Ivoire sur la plaque
africaine (domaine stable). Source : 1ereD/SVT.pdf, page 92.
"""

import textwrap

from manim import (
    BLUE_E,
    DOWN,
    GREEN_D,
    LEFT,
    ORANGE,
    PURPLE_D,
    RIGHT,
    TEAL_D,
    UP,
    WHITE,
    YELLOW,
    FadeIn,
    FadeOut,
    Polygon,
    Rectangle,
    Star,
    Text,
    VGroup,
    Write,
    MAROON_D,
    GOLD_D,
    RED_D,
)

from shapes.base_scene import NotionScene
from shapes.boxes import definition_box, example_box, scene_title


def _wrap(text: str, width: int = 56) -> str:
    return "\n".join(textwrap.fill(line, width=width) for line in text.split("\n"))


def _grid_table(cell_matrix, col_gap=0.45, row_gap=0.2):
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


def _carte_plaques():
    """Carte du monde très schématique : blocs colorés = grandes plaques."""
    ocean = Rectangle(width=11.5, height=4.6, fill_color=BLUE_E, fill_opacity=0.5, stroke_color=WHITE, stroke_width=1)

    plaque_na = Polygon(
        [-5.2, 1.0, 0], [-3.2, 1.6, 0], [-2.6, -0.2, 0], [-4.8, -0.4, 0],
        fill_color=ORANGE, fill_opacity=0.9, stroke_color=WHITE, stroke_width=1,
    )
    label_na = Text("Nord-américaine", font_size=13, color=WHITE).move_to(plaque_na.get_center())

    plaque_sa = Polygon(
        [-3.6, -0.6, 0], [-2.4, -0.5, 0], [-2.6, -2.0, 0], [-3.8, -1.9, 0],
        fill_color=GREEN_D, fill_opacity=0.9, stroke_color=WHITE, stroke_width=1,
    )
    label_sa = Text("Sud-américaine", font_size=12, color=WHITE).move_to(plaque_sa.get_center())

    plaque_af = Polygon(
        [-1.0, 1.4, 0], [1.1, 1.2, 0], [1.0, -1.7, 0], [-0.6, -1.9, 0],
        fill_color=GOLD_D, fill_opacity=0.9, stroke_color=WHITE, stroke_width=1,
    )
    label_af = Text("Africaine", font_size=14, color=WHITE, weight="BOLD").move_to(plaque_af.get_center())

    ci_point = Star(n=5, outer_radius=0.09, color=RED_D, fill_opacity=1).move_to([-0.15, -0.5, 0])
    label_ci = Text("Côte d'Ivoire", font_size=11, color=RED_D).next_to(ci_point, DOWN, buff=0.08)

    plaque_eur = Polygon(
        [-0.5, 1.7, 0], [3.2, 2.0, 0], [3.6, 0.9, 0], [0.0, 0.9, 0],
        fill_color=PURPLE_D, fill_opacity=0.9, stroke_color=WHITE, stroke_width=1,
    )
    label_eur = Text("Eurasiatique", font_size=13, color=WHITE).move_to(plaque_eur.get_center())

    plaque_indoaus = Polygon(
        [1.4, 0.6, 0], [3.6, 0.5, 0], [3.4, -1.8, 0], [1.6, -1.6, 0],
        fill_color=TEAL_D, fill_opacity=0.9, stroke_color=WHITE, stroke_width=1,
    )
    label_indoaus = Text("Indo-\naustralienne", font_size=12, color=WHITE).move_to(plaque_indoaus.get_center())

    plaque_pac = Polygon(
        [4.0, 1.6, 0], [5.6, 1.6, 0], [5.6, -1.6, 0], [4.0, -1.6, 0],
        fill_color=MAROON_D, fill_opacity=0.9, stroke_color=WHITE, stroke_width=1,
    )
    label_pac = Text("Pacifique", font_size=13, color=WHITE).move_to(plaque_pac.get_center())

    plaque_ant = Polygon(
        [-3.0, -2.1, 0], [3.0, -2.1, 0], [3.0, -2.25, 0], [-3.0, -2.25, 0],
        fill_color=BLUE_E, fill_opacity=1.0, stroke_color=WHITE, stroke_width=1,
    )
    label_ant = Text("Antarctique", font_size=12, color=WHITE).next_to(plaque_ant, DOWN, buff=0.12)

    plaques = VGroup(
        ocean,
        plaque_na, label_na,
        plaque_sa, label_sa,
        plaque_af, label_af,
        plaque_eur, label_eur,
        plaque_indoaus, label_indoaus,
        plaque_pac, label_pac,
        plaque_ant, label_ant,
        ci_point, label_ci,
    )
    return plaques


class PlaquesLithospheriques(NotionScene):
    def construct(self):
        titre = scene_title("7.1.3 — Les plaques lithosphériques")
        titre.scale(0.65)
        titre.to_edge(UP)

        # --- Énoncé : définition ---------------------------------------------
        definition_plaque = definition_box(
            Text(
                _wrap(
                    "Une plaque lithosphérique est un fragment rigide de la "
                    "lithosphère, délimité par des zones actives, qui se "
                    "déplace d'un seul bloc à la surface de l'asthénosphère. "
                    "Une même plaque peut porter continents et océans.",
                    width=54,
                ),
                font_size=23,
            ),
            box_width=11.8,
        )
        definition_plaque.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "La lithosphère n'est pas continue à la surface du globe : "
                "elle est cassée en une dizaine de grands morceaux, séparés "
                "par des zones actives, dorsales, fosses, grandes failles, "
                "où se concentrent séismes et volcans. Une plaque "
                "lithosphérique est un fragment rigide de la lithosphère, "
                "délimité par ces zones actives, qui se déplace d'un seul "
                "bloc à la surface de l'asthénosphère. Point important : une "
                "même plaque peut porter à la fois des continents et des "
                "océans, comme la plaque africaine ou la plaque "
                "sud-américaine."
            )
        ) as tracker:
            self.play(Write(titre))
            self.play(FadeIn(definition_plaque))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(definition_plaque))

        # --- Animation du raisonnement : carte simplifiée des plaques -------
        carte = _carte_plaques()
        carte.scale(0.95)
        carte.next_to(titre, DOWN, buff=0.45)

        with self.voiceover(
            text=(
                "Voici une carte très schématique des principales plaques : "
                "au centre, la plaque africaine, qui porte le continent "
                "africain ; à l'ouest, la plaque sud-américaine, puis la "
                "plaque nord-américaine ; à l'est, la plaque eurasiatique, "
                "puis la plaque indo-australienne ; plus loin encore, "
                "l'immense plaque pacifique ; et tout au sud, la plaque "
                "antarctique. Une étoile rouge repère la Côte d'Ivoire, à "
                "l'intérieur de la plaque africaine."
            )
        ) as tracker:
            self.play(FadeIn(carte))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(carte))

        entete_tab = Text("Les principales plaques lithosphériques", font_size=23, color=YELLOW, weight="BOLD")
        entete_tab.next_to(titre, DOWN, buff=0.5)

        header = [
            Text("Plaque", font_size=17, color=YELLOW, weight="BOLD"),
            Text("Porte notamment", font_size=17, color=YELLOW, weight="BOLD"),
        ]
        rows = [
            ("Africaine", "Afrique, parties Atlantique / Indien"),
            ("Sud-américaine", "Amérique du Sud, ouest Atlantique Sud"),
            ("Nord-américaine", "Amérique du Nord, Groenland, ouest Atlantique Nord"),
            ("Eurasiatique", "Europe et Asie (sauf Inde)"),
            ("Indo-australienne", "Inde, Australie, partie océan Indien"),
            ("Pacifique", "presque uniquement océan Pacifique"),
            ("Antarctique", "continent antarctique et océans bordiers"),
            ("Nazca", "est du Pacifique, au large des Andes"),
        ]
        cell_matrix = [header]
        for nom, contenu in rows:
            cell_matrix.append([
                Text(nom, font_size=16, color=WHITE),
                Text(contenu, font_size=15, color=WHITE),
            ])
        tableau = _grid_table(cell_matrix, col_gap=0.5, row_gap=0.15)
        tableau.next_to(entete_tab, DOWN, buff=0.3)
        tableau.scale(0.85)

        with self.voiceover(
            text=(
                "Récapitulons dans un tableau. La plaque africaine porte "
                "l'Afrique et des morceaux d'Atlantique et d'océan Indien. "
                "La plaque sud-américaine porte l'Amérique du Sud et l'ouest "
                "de l'Atlantique Sud. La plaque nord-américaine porte "
                "l'Amérique du Nord, le Groenland et l'ouest de l'Atlantique "
                "Nord. La plaque eurasiatique porte l'Europe et l'Asie, sauf "
                "l'Inde. La plaque indo-australienne porte l'Inde, "
                "l'Australie et une partie de l'océan Indien. La plaque "
                "pacifique est presque uniquement océanique. La plaque "
                "antarctique porte le continent antarctique et ses océans "
                "bordiers. Et la plaque de Nazca occupe l'est du Pacifique, "
                "au large des Andes."
            )
        ) as tracker:
            self.play(FadeIn(entete_tab))
            self.play(FadeIn(tableau))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(entete_tab), FadeOut(tableau))

        # --- Exemple traité : la Côte d'Ivoire sur la plaque africaine ------
        exemple = example_box(
            Text(
                _wrap(
                    "La plaque africaine : limite ouest = dorsale "
                    "médio-atlantique ; limite est = dorsale de l'océan "
                    "Indien et rift est-africain ; limite nord = "
                    "Méditerranée (plaque eurasiatique). La Côte d'Ivoire est "
                    "à l'intérieur de la plaque africaine, à plus de 3000 km "
                    "de la limite la plus proche : domaine stable, sans "
                    "volcan actif ni séisme important.",
                    width=54,
                ),
                font_size=21,
            ),
            box_width=12.0,
        )
        exemple.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Prenons l'exemple de la plaque africaine. Sa limite ouest "
                "est marquée par la dorsale médio-atlantique ; sa limite "
                "est, par la dorsale de l'océan Indien et par le rift "
                "est-africain ; sa limite nord, par la Méditerranée, "
                "frontière avec la plaque eurasiatique. Où se situe la "
                "Côte d'Ivoire dans tout cela ? Elle se trouve à "
                "l'intérieur de la plaque africaine, à plus de trois mille "
                "kilomètres de la limite la plus proche. C'est donc un "
                "domaine stable, sans volcan actif ni séisme important : "
                "voilà pourquoi la terre ivoirienne ne tremble presque "
                "jamais."
            )
        ) as tracker:
            self.play(FadeIn(exemple))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(titre), FadeOut(exemple))
