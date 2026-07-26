"""
scenes/Chimie_EsterificationHydrolyse_06.py — Chapitre 8 « Estérification et
hydrolyse d'un ester » (1ereC, Chimie), scène 06.

§ L'équilibre d'estérification-hydrolyse : tableau d'avancement (acide +
alcool ⇌ ester + eau, état initial n;n;0;0, équilibre n-xe;n-xe;xe;xe).
Tableau des limites selon classe d'alcool (primaire ≈2/3, secondaire ≈60%,
tertiaire ≈5%). theorem_box limite 2/3 pour alcool primaire, indépendante
de T et du catalyseur. definition_box taux d'avancement/rendement τ.
Exemple résolu 1 (0,10mol acide+0,10mol alcool, 0,033mol acide restant →
τ=67%).
Source : 1ereC/Chimie.pdf, chapitre 8, pages 78-79.
"""

import textwrap

from manim import (
    DOWN,
    UP,
    WHITE,
    YELLOW,
    FadeIn,
    FadeOut,
    Line,
    MathTex,
    Rectangle,
    Table,
    Text,
    VGroup,
    Write,
    config,
)

from shapes.base_scene import NotionScene
from shapes.boxes import definition_box, example_box, scene_title, theorem_box


def _wrap(text: str, width: int = 56) -> str:
    return "\n".join(textwrap.fill(line, width=width) for line in text.split("\n"))


def _fit(mobject, top_y):
    bas_visible = -config.frame_height / 2 + 0.25
    hauteur_dispo = top_y - bas_visible
    if mobject.height > hauteur_dispo:
        mobject.scale(hauteur_dispo / mobject.height, about_point=mobject.get_top())
    return mobject


class EquilibreLimiteTauxAvancement(NotionScene):
    def construct(self):
        titre = scene_title("6. L'équilibre : limite et taux d'avancement")
        titre.scale(0.5)
        titre.to_edge(UP)

        # --- Énoncé -----------------------------------------------------------
        enonce = Text(
            _wrap(
                "Puisque l'estérification s'arrête à un équilibre, "
                "peut-on prévoir précisément la quantité d'ester obtenue "
                "à la fin ? Construisons un tableau d'avancement.",
                width=54,
            ),
            font_size=25,
            color=WHITE,
        )
        enonce.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Puisque l'estérification s'arrête à un équilibre, "
                "peut-on prévoir précisément la quantité d'ester obtenue "
                "à la fin ? Construisons pour cela un tableau "
                "d'avancement."
            )
        ) as tracker:
            self.play(Write(titre))
            self.play(FadeIn(enonce))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(enonce))

        # --- Raisonnement : tableau d'avancement ------------------------------------
        entete = Text("Tableau d'avancement", font_size=24, color=YELLOW, weight="BOLD")
        entete.next_to(titre, DOWN, buff=0.35)

        eq_tab = MathTex(r"acide + alcool \;\rightleftharpoons\; ester + eau", font_size=26, color=WHITE)
        eq_tab.next_to(entete, DOWN, buff=0.25)

        col_labels_txt = ["état", "acide", "alcool", "ester", "eau"]
        row_labels_txt = ["état initial (x=0)", "à l'équilibre (x=xe)"]
        maths_cells = [
            ["n", "n", "0", "0"],
            ["n - x_e", "n - x_e", "x_e", "x_e"],
        ]
        col_widths = [3.2, 1.9, 1.9, 1.7, 1.7]
        row_height = 0.6
        n_cols = len(col_labels_txt)
        n_rows = 1 + len(row_labels_txt)
        x_positions = [0.0]
        for w in col_widths:
            x_positions.append(x_positions[-1] + w)
        largeur_totale = x_positions[-1]
        x_centres = [(x_positions[j] + x_positions[j + 1]) / 2 - largeur_totale / 2 for j in range(n_cols)]

        cells = VGroup()
        for j, label in enumerate(col_labels_txt):
            c = Text(label, font_size=17, color=YELLOW, weight="BOLD")
            c.move_to([x_centres[j], (n_rows - 1) / 2 * row_height, 0])
            cells.add(c)
        for i, row_label in enumerate(row_labels_txt):
            c = Text(row_label, font_size=15, color=WHITE)
            c.move_to([x_centres[0], ((n_rows - 1) / 2 - (i + 1)) * row_height, 0])
            cells.add(c)
            for j, expr in enumerate(maths_cells[i]):
                c2 = MathTex(expr, font_size=24, color=WHITE)
                c2.move_to([x_centres[j + 1], ((n_rows - 1) / 2 - (i + 1)) * row_height, 0])
                cells.add(c2)

        hauteur_totale = n_rows * row_height
        contour = Rectangle(width=largeur_totale, height=hauteur_totale, color=WHITE, stroke_width=2)
        contour.move_to([0, 0, 0])
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
        table = VGroup(contour, lignes_h, lignes_v, cells)
        table.next_to(eq_tab, DOWN, buff=0.3)

        groupe = VGroup(entete, eq_tab, table)
        _fit(groupe, titre.get_bottom()[1] - 0.35)

        with self.voiceover(
            text=(
                "Partons d'un mélange initial contenant n mol d'acide et "
                "n mol d'alcool, sans ester ni eau. Au cours du temps, "
                "l'avancement x augmente, jusqu'à une valeur d'équilibre "
                "notée xe. À l'équilibre, il reste n moins xe mol d'acide "
                "et n moins xe mol d'alcool, et il s'est formé xe mol "
                "d'ester et xe mol d'eau. Tout l'enjeu est de déterminer "
                "cette valeur xe."
            )
        ) as tracker:
            self.play(FadeIn(entete))
            self.play(Write(eq_tab))
            self.play(FadeIn(table))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(groupe))

        # --- Exemple traité : tableau des limites selon la classe de l'alcool -------
        entete2 = Text("La limite dépend de la classe de l'alcool", font_size=22, color=YELLOW, weight="BOLD")
        entete2.next_to(titre, DOWN, buff=0.35)

        rows2 = [
            ["alcool primaire", "≈ 2/3 (≈ 67 %)"],
            ["alcool secondaire", "≈ 60 %"],
            ["alcool tertiaire", "≈ 5 %"],
        ]
        table2 = Table(
            rows2,
            col_labels=[Text(c, font_size=18, weight="BOLD") for c in ["classe de l'alcool", "limite (% d'ester)"]],
            element_to_mobject=Text,
            element_to_mobject_config={"font_size": 18},
            line_config={"color": WHITE, "stroke_width": 1},
            include_outer_lines=True,
            v_buff=0.25,
            h_buff=0.35,
        )
        table2.get_entries().set_color(WHITE)
        table2.get_col_labels().set_color(YELLOW)
        for line in table2.get_horizontal_lines():
            line.set_color(WHITE)
        for line in table2.get_vertical_lines():
            line.set_color(WHITE)
        table2.next_to(entete2, DOWN, buff=0.3)

        groupe2 = VGroup(entete2, table2)
        _fit(groupe2, titre.get_bottom()[1] - 0.35)

        with self.voiceover(
            text=(
                "La valeur de cette limite dépend en réalité de la classe "
                "de l'alcool utilisé. Avec un alcool primaire, la limite "
                "avoisine deux tiers, soit environ soixante-sept pour "
                "cent d'ester. Avec un alcool secondaire, elle est plus "
                "faible, environ soixante pour cent. Et avec un alcool "
                "tertiaire, la limite chute à seulement environ cinq pour "
                "cent : la réaction est alors très peu avancée à "
                "l'équilibre, à cause de l'encombrement autour du carbone "
                "fonctionnel."
            )
        ) as tracker:
            self.play(FadeIn(entete2))
            self.play(FadeIn(table2))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(groupe2))

        # --- À retenir : theorem_box + definition_box taux d'avancement -------------
        theoreme = theorem_box(
            Text(
                _wrap(
                    "Pour un mélange équimolaire acide + alcool primaire, "
                    "la limite de 2/3 d'ester (67 %) est "
                    "INDÉPENDANTE de la température ET du catalyseur "
                    "utilisé : c'est une propriété du système chimique "
                    "lui-même, à l'équilibre.",
                    width=48,
                ),
                font_size=22,
            ),
        )
        theoreme.next_to(titre, DOWN, buff=0.4)
        _fit(theoreme, titre.get_bottom()[1] - 0.4)

        with self.voiceover(
            text=(
                "Retenons ce théorème : pour un mélange équimolaire d'un "
                "acide et d'un alcool primaire, la limite des deux tiers "
                "d'ester, soit soixante-sept pour cent, est indépendante "
                "de la température et du catalyseur utilisé. C'est une "
                "propriété du système chimique lui-même à l'équilibre, "
                "pas des conditions expérimentales."
            )
        ) as tracker:
            self.play(FadeIn(theoreme))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(theoreme))

        definition = definition_box(
            MathTex(
                r"\tau = \dfrac{x_e}{x_{max}}",
                font_size=40,
            ),
        )
        definition_legende = Text(
            "τ : taux d'avancement final (ou rendement) de l'estérification",
            font_size=20,
            color=WHITE,
        )
        bloc_def = VGroup(definition, definition_legende).arrange(DOWN, buff=0.3)
        bloc_def.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "On définit alors le taux d'avancement final, aussi "
                "appelé rendement de l'estérification, noté tau : c'est "
                "le rapport de l'avancement à l'équilibre xe sur "
                "l'avancement maximal théorique x-max, celui qu'on "
                "aurait si la réaction était totale."
            )
        ) as tracker:
            self.play(FadeIn(bloc_def))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(bloc_def))

        # --- Exemple résolu 1 -----------------------------------------------------------
        exemple = example_box(
            VGroup(
                Text(
                    _wrap(
                        "0,10 mol d'acide + 0,10 mol d'alcool primaire "
                        "(mélange équimolaire). À l'équilibre, il reste "
                        "0,033 mol d'acide.",
                        width=46,
                    ),
                    font_size=21,
                ),
                MathTex(
                    r"x_e = n - n_{acide,eq} = 0{,}10 - 0{,}033 = 0{,}067\ mol",
                    font_size=24,
                ),
                MathTex(
                    r"\tau = \dfrac{x_e}{n} = \dfrac{0{,}067}{0{,}10} \approx 0{,}67 = 67\ \%",
                    font_size=26,
                ),
            ).arrange(DOWN, buff=0.3),
            box_width=11.5,
        )
        exemple.next_to(titre, DOWN, buff=0.4)
        _fit(exemple, titre.get_bottom()[1] - 0.4)

        with self.voiceover(
            text=(
                "Appliquons cela sur un exemple chiffré. On mélange zéro "
                "virgule dix mole d'acide et zéro virgule dix mole d'un "
                "alcool primaire. À l'équilibre, un dosage indique qu'il "
                "reste zéro virgule zéro trente-trois mole d'acide. "
                "L'avancement à l'équilibre vaut donc xe égale n moins "
                "cette quantité restante, soit zéro virgule zéro "
                "soixante-sept mole. Le taux d'avancement final vaut "
                "alors xe sur n, soit environ zéro virgule soixante-sept, "
                "c'est-à-dire soixante-sept pour cent : on retrouve bien "
                "la limite des deux tiers annoncée pour un alcool "
                "primaire."
            )
        ) as tracker:
            self.play(FadeIn(exemple))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(exemple), FadeOut(titre))
