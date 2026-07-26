"""
scenes/Chimie_CorrosionProtectionMetaux_02.py — Chapitre 15 « Corrosion et
protection des métaux » (1ereC, Chimie), scène 02.

§ 2. Conditions de la corrosion du fer : les expériences témoins. Protocole
des 3 tubes à essai (1 : eau + air → rouille ; 2 : eau bouillie + huile,
sans air → rien ; 3 : air sec avec CaCl2, sans eau → rien), schéma des 3
tubes construit avec des primitives Manim de base, tableau récapitulatif
des observations.
Source : 1ereC/Chimie.pdf, chapitre 15, pages 145-146.
"""

import textwrap

from manim import (
    DOWN,
    LEFT,
    ORANGE,
    RIGHT,
    UP,
    WHITE,
    YELLOW,
    BLUE,
    GREY,
    FadeIn,
    FadeOut,
    Circle,
    Line,
    Rectangle,
    RoundedRectangle,
    Text,
    VGroup,
    Write,
    config,
)

from shapes.base_scene import NotionScene
from shapes.boxes import scene_title, warning_box


def _wrap(text: str, width: int = 56) -> str:
    return "\n".join(textwrap.fill(line, width=width) for line in text.split("\n"))


def _fit(mobject, top_y):
    bas_visible = -config.frame_height / 2 + 0.25
    hauteur_dispo = top_y - bas_visible
    if mobject.height > hauteur_dispo:
        mobject.scale(hauteur_dispo / mobject.height, about_point=mobject.get_top())
    return mobject


def _tableau(entetes, lignes, col_widths, row_height=0.5, font_size=18):
    n_cols = len(entetes)
    n_rows = 1 + len(lignes)
    x_positions = [0.0]
    for w in col_widths:
        x_positions.append(x_positions[-1] + w)
    largeur_totale = x_positions[-1]
    x_centres = [(x_positions[j] + x_positions[j + 1]) / 2 - largeur_totale / 2 for j in range(n_cols)]

    cells = VGroup()
    for j, entete in enumerate(entetes):
        c = Text(entete, font_size=font_size, color=YELLOW, weight="BOLD")
        c.move_to([x_centres[j], (n_rows - 1) / 2 * row_height, 0])
        cells.add(c)

    for i, ligne in enumerate(lignes):
        for j, val in enumerate(ligne):
            c = Text(val, font_size=font_size, color=WHITE)
            c.move_to([x_centres[j], ((n_rows - 1) / 2 - (i + 1)) * row_height, 0])
            cells.add(c)

    hauteur_totale = n_rows * row_height
    contour = Rectangle(width=largeur_totale, height=hauteur_totale, color=WHITE, stroke_width=2)

    lignes_h = VGroup(
        *[
            Line(
                [-largeur_totale / 2, (n_rows / 2 - k) * row_height, 0],
                [largeur_totale / 2, (n_rows / 2 - k) * row_height, 0],
                color=WHITE,
                stroke_width=1,
            )
            for k in range(n_rows + 1)
        ]
    )
    lignes_v = VGroup(
        *[
            Line(
                [x_positions[k] - largeur_totale / 2, hauteur_totale / 2, 0],
                [x_positions[k] - largeur_totale / 2, -hauteur_totale / 2, 0],
                color=WHITE,
                stroke_width=1,
            )
            for k in range(n_cols + 1)
        ]
    )

    return VGroup(contour, lignes_h, lignes_v, cells)


def _tube(contenu_couleur, contenu_hauteur_ratio, label, clou_color=GREY, largeur=1.1, hauteur=3.0):
    """Un tube à essai simplifié : contour, contenu (liquide/rien), petit
    clou en fer à l'intérieur. Primitives Manim de base uniquement."""
    corps = RoundedRectangle(
        width=largeur, height=hauteur, corner_radius=largeur / 2,
        stroke_color=WHITE, stroke_width=2.5, fill_opacity=0,
    )
    elements = [corps]

    if contenu_hauteur_ratio > 0:
        h_liquide = hauteur * contenu_hauteur_ratio
        liquide = Rectangle(
            width=largeur - 0.12, height=h_liquide,
            fill_color=contenu_couleur, fill_opacity=0.55, stroke_width=0,
        )
        liquide.align_to(corps, DOWN).shift(UP * 0.1)
        elements.append(liquide)

    clou = Line(UP * 0.5, DOWN * 0.5, color=clou_color, stroke_width=6)
    clou.move_to(corps.get_center())
    elements.append(clou)

    etiquette = Text(label, font_size=16, color=WHITE)
    etiquette.next_to(corps, DOWN, buff=0.2)
    elements.append(etiquette)

    return VGroup(*elements)


def _schema_trois_tubes():
    tube1 = _tube(BLUE, 0.55, "Tube 1 : eau + air", clou_color=ORANGE)
    tube2 = _tube(ORANGE, 0.55, "Tube 2 : eau bouillie\n+ huile, sans air")
    tube3 = _tube(None, 0, "Tube 3 : air sec\n(CaCl2), sans eau")

    bouchon2 = Rectangle(width=0.9, height=0.15, fill_color="#8B5A2B", fill_opacity=1, stroke_width=0)
    bouchon2.move_to(tube2[0].get_top() + DOWN * 0.5)

    dessicant3 = Circle(radius=0.35, color=WHITE, stroke_width=1.5)
    dessicant3.move_to(tube3[0].get_bottom() + UP * 0.5)
    label_cacl2 = Text("CaCl2", font_size=13, color=WHITE)
    label_cacl2.move_to(dessicant3.get_center())

    groupe = VGroup(tube1, tube2, VGroup(tube3, dessicant3, label_cacl2))
    groupe.arrange(RIGHT, buff=1.0)
    tube2.add(bouchon2)
    return groupe


class ConditionsCorrosionExperiencesTemoins(NotionScene):
    def construct(self):
        titre = scene_title("15.2 Conditions de la corrosion : expériences témoins")
        titre.scale(0.44)
        titre.to_edge(UP)

        # --- Énoncé : question -------------------------------------------------
        question = Text(
            _wrap(
                "Le fer rouille dehors, mais pas toujours. Quelles sont "
                "exactement les conditions nécessaires à la corrosion ? "
                "Trois tubes à essai témoins vont permettre de le "
                "déterminer expérimentalement.",
                width=54,
            ),
            font_size=23,
            color=WHITE,
        )
        question.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Le fer rouille dehors, mais pas toujours et pas partout "
                "de la même façon. Quelles sont exactement les conditions "
                "nécessaires à la corrosion ? Pour le déterminer, on "
                "réalise trois tubes à essai témoins, dans des conditions "
                "différentes, et on compare les résultats après quelques "
                "jours."
            )
        ) as tracker:
            self.play(Write(titre))
            self.play(FadeIn(question))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(question))

        # --- Raisonnement : schéma des 3 tubes ---------------------------------
        entete_schema = Text("Le protocole : trois tubes contenant un clou de fer", font_size=20, color=YELLOW, weight="BOLD")
        entete_schema.next_to(titre, DOWN, buff=0.35)

        schema = _schema_trois_tubes()
        schema.next_to(entete_schema, DOWN, buff=0.5)
        groupe_schema = VGroup(entete_schema, schema)
        _fit(groupe_schema, titre.get_bottom()[1] - 0.25)

        with self.voiceover(
            text=(
                "Dans chaque tube, on place un clou de fer identique. "
                "Premier tube : de l'eau non bouillie, en contact avec "
                "l'air. Deuxième tube : de l'eau qui a été bouillie pour "
                "en chasser le dioxygène dissous, recouverte d'un film "
                "d'huile qui empêche tout nouveau contact avec l'air. "
                "Troisième tube : de l'air parfaitement sec, asséché par "
                "du chlorure de calcium, sans une seule goutte d'eau."
            )
        ) as tracker:
            self.play(FadeIn(entete_schema))
            self.play(FadeIn(schema))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(groupe_schema))

        # --- Exemple traité : tableau des observations -------------------------
        entete_tab = Text("Observations après quelques jours", font_size=21, color=YELLOW, weight="BOLD")
        entete_tab.next_to(titre, DOWN, buff=0.35)

        tableau = _tableau(
            ["Tube", "Conditions", "Observation"],
            [
                ["1", "eau + air", "le clou rouille"],
                ["2", "eau bouillie + huile\n(sans air)", "aucun changement"],
                ["3", "air sec (CaCl2)\n(sans eau)", "aucun changement"],
            ],
            col_widths=[1.2, 3.6, 3.4],
            row_height=0.65,
            font_size=17,
        )
        tableau.next_to(entete_tab, DOWN, buff=0.35)
        groupe_tab = VGroup(entete_tab, tableau)
        _fit(groupe_tab, titre.get_bottom()[1] - 0.3)

        with self.voiceover(
            text=(
                "Voici les observations après quelques jours. Dans le "
                "tube un, avec de l'eau et de l'air, le clou se recouvre "
                "bel et bien de rouille. Dans le tube deux, où l'eau "
                "bouillie est isolée de l'air par l'huile, rien ne se "
                "passe : le clou reste intact. Dans le tube trois, où "
                "l'air est présent mais totalement sec, rien ne se passe "
                "non plus : le clou reste intact également."
            )
        ) as tracker:
            self.play(FadeIn(entete_tab))
            self.play(FadeIn(tableau))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(groupe_tab))

        # --- À retenir / piège : bien identifier ce que chaque tube isole -------
        piege = warning_box(
            Text(
                _wrap(
                    "Chaque tube n'isole qu'un seul facteur à la fois : le "
                    "tube 2 supprime l'air (garde l'eau), le tube 3 "
                    "supprime l'eau (garde l'air). C'est cette comparaison "
                    "« deux à deux » qui permet de conclure — un seul tube "
                    "isolé ne suffirait pas.",
                    width=48,
                ),
                font_size=20,
            ),
        )
        piege.next_to(titre, DOWN, buff=0.45)
        _fit(piege, titre.get_bottom()[1] - 0.35)

        with self.voiceover(
            text=(
                "Un point méthodologique essentiel : chaque tube témoin "
                "n'isole qu'un seul facteur à la fois. Le tube deux "
                "supprime l'air tout en gardant l'eau ; le tube trois "
                "supprime l'eau tout en gardant l'air. C'est cette "
                "comparaison deux à deux avec le tube un, où les deux "
                "facteurs sont réunis, qui permettra de conclure sur les "
                "conditions réelles de la corrosion."
            )
        ) as tracker:
            self.play(FadeIn(piege))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(piege), FadeOut(titre))
