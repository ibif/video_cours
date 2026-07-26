"""
scenes/SVT_Photosynthese_02.py — Chapitre 10 (1ereC, SVT), scène 02.

§ 10.1.3 L'équation bilan de la photosynthèse : équation MathTex complète
(6CO2+6H2O --lumière,chlorophylle--> C6H12O6+6O2), tableau de lecture
(élément/formule/rôle/origine), méthode point clé « vérification de
l'équilibre » (comptage C, H, O), piège fondamental (l'O2 dégagé vient de
l'eau, pas du CO2).
Source : 1ereC/SVT.pdf, page 107.
"""

import textwrap

from manim import DOWN, LEFT, RIGHT, UP, WHITE, YELLOW, FadeIn, FadeOut, MathTex, Text, VGroup, Write, config

from shapes.base_scene import NotionScene
from shapes.boxes import method_box, scene_title, theorem_box, warning_box


def _wrap(text: str, width: int = 56) -> str:
    return "\n".join(textwrap.fill(line, width=width) for line in text.split("\n"))


def _bullets(items, font_size=22, color=WHITE, width=52):
    lines = VGroup(
        *[Text(f"• {_wrap(it, width=width)}", font_size=font_size, color=color) for it in items]
    )
    lines.arrange(DOWN, aligned_edge=LEFT, buff=0.22)
    return lines


def _cell_text(text: str, x: float, y: float, font_size=14, color=WHITE, bold=False):
    t = Text(text, font_size=font_size, color=color, weight="BOLD" if bold else "NORMAL")
    t.move_to([x, y, 0])
    t.shift(RIGHT * (t.width / 2))
    return t


def _cell_math(latex: str, x: float, y: float, font_size=20, color=WHITE):
    t = MathTex(latex, font_size=font_size, color=color)
    t.move_to([x, y, 0])
    t.shift(RIGHT * (t.width / 2))
    return t


class EquationBilanPhotosynthese(NotionScene):
    def construct(self):
        titre = scene_title("10.1.3 — L'équation bilan de la photosynthèse")
        titre.scale(0.48)
        titre.to_edge(UP)

        # --- Énoncé : l'équation bilan complète -----------------------------
        equation = MathTex(
            r"6\,CO_2 + 6\,H_2O \xrightarrow{\;\text{lumière, chlorophylle}\;} "
            r"C_6H_{12}O_6 + 6\,O_2",
            font_size=32,
            color=WHITE,
        )
        equation.next_to(titre, DOWN, buff=0.7)

        with self.voiceover(
            text=(
                "La photosynthèse se résume par l'équation bilan "
                "suivante : six molécules de dioxyde de carbone plus six "
                "molécules d'eau, en présence de lumière et de "
                "chlorophylle, donnent une molécule de glucose et six "
                "molécules de dioxygène."
            )
        ) as tracker:
            self.play(Write(titre))
            self.play(Write(equation))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(equation))

        # --- Animation du raisonnement : tableau de lecture de l'équation ----
        entete_tab = Text("Lecture de l'équation", font_size=24, color=YELLOW, weight="BOLD")
        entete_tab.next_to(titre, DOWN, buff=0.4)

        x_elem, x_form, x_role, x_orig = -6.6, -3.2, -1.1, 1.9
        headers = ["Élément", "Formule", "Rôle", "Origine"]
        row_y0 = entete_tab.get_bottom()[1] - 0.5
        row_h = 0.8

        header_row = VGroup(
            *[
                _cell_text(h, x, row_y0, font_size=16, color=YELLOW, bold=True)
                for h, x in zip(headers, [x_elem, x_form, x_role, x_orig])
            ]
        )

        rows_data = [
            ("Dioxyde de\ncarbone", r"CO_2", "Réactif (source\nde carbone)", "Air (stomates\ndes feuilles)"),
            ("Eau", r"H_2O", "Réactif (H et O\ndégagé)", "Sol (racines,\nsève brute)"),
            ("Lumière", None, "Source d'énergie", "Soleil (chloro-\nphylle)"),
            ("Chlorophylle", None, "Pigment non\nconsommé", "Chloroplastes"),
            ("Glucose", r"C_6H_{12}O_6", "Produit (matière\norganique)", "Feuille (sève\nélaborée)"),
            ("Dioxygène", r"O_2", "Produit (rejeté\ndans l'air)", "Atmosphère"),
        ]

        data_rows = VGroup()
        for i, (elem, formule, role, origine) in enumerate(rows_data):
            y = row_y0 - (i + 1) * row_h
            cell_elem = _cell_text(elem, x_elem, y, font_size=14)
            if formule is None:
                cell_form = _cell_text("—", x_form, y, font_size=14)
            else:
                cell_form = _cell_math(formule, x_form, y, font_size=18)
            cell_role = _cell_text(role, x_role, y, font_size=14)
            cell_orig = _cell_text(origine, x_orig, y, font_size=14)
            data_rows.add(VGroup(cell_elem, cell_form, cell_role, cell_orig))

        tableau = VGroup(header_row, data_rows)

        # Garde-fou d'auto-scale si le tableau déborde du cadre visible.
        bas_visible = -config.frame_height / 2 + 0.3
        hauteur_dispo = row_y0 - bas_visible + 0.3
        if tableau.height > hauteur_dispo:
            tableau.scale(hauteur_dispo / tableau.height, about_point=[0, row_y0, 0])

        with self.voiceover(
            text=(
                "Lisons cette équation élément par élément. Le dioxyde de "
                "carbone, CO2, est un réactif, source de carbone, "
                "provenant de l'air atmosphérique qui entre par les "
                "stomates des feuilles. L'eau, H2O, est un réactif, "
                "source d'hydrogène et de l'oxygène dégagé, absorbée par "
                "les racines et transportée par la sève brute. La "
                "lumière est la source d'énergie, captée par la "
                "chlorophylle. La chlorophylle elle-même est un pigment "
                "indispensable mais non consommé. Le glucose, C6H12O6, "
                "est le produit, la matière organique fabriquée dans la "
                "feuille et exportée par la sève élaborée. Enfin le "
                "dioxygène, O2, est le produit rejeté dans l'atmosphère."
            )
        ) as tracker:
            self.play(FadeIn(entete_tab))
            self.play(FadeIn(header_row))
            for row in data_rows:
                self.play(FadeIn(row), run_time=0.4)
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(entete_tab), FadeOut(tableau))

        # --- Exemple traité : méthode — vérification de l'équilibre ---------
        verification = method_box(
            _bullets(
                [
                    "Carbone : 6 atomes à gauche (6CO2) ; 6 atomes à "
                    "droite (C6H12O6). Équilibré.",
                    "Hydrogène : 6×2=12 atomes à gauche (6H2O) ; 12 "
                    "atomes à droite (C6H12O6). Équilibré.",
                    "Oxygène : (6×2)+(6×1)=18 atomes à gauche ; "
                    "6+(6×2)=18 atomes à droite. Équilibré.",
                    "La matière se conserve : l'équation est bien "
                    "équilibrée (loi de Lavoisier).",
                ],
                font_size=19,
                width=54,
            ),
            box_width=12.2,
        )
        verification.next_to(titre, DOWN, buff=0.45)

        with self.voiceover(
            text=(
                "Vérifions l'équilibre de cette équation, atome par "
                "atome. Pour le carbone : six atomes à gauche, dans les "
                "six CO2 ; six atomes à droite, dans le glucose C6H12O6. "
                "C'est équilibré. Pour l'hydrogène : six fois deux, soit "
                "douze atomes à gauche, dans les six H2O ; douze atomes à "
                "droite, dans le glucose. C'est équilibré. Pour "
                "l'oxygène : six fois deux plus six fois un, soit dix-huit "
                "atomes à gauche ; six plus six fois deux, soit dix-huit "
                "atomes à droite. C'est équilibré. La matière se "
                "conserve bien : l'équation respecte la loi de Lavoisier."
            )
        ) as tracker:
            self.play(FadeIn(verification))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(verification))

        # --- À retenir : l'équation, à connaître par cœur ---------------------
        essentiel_eq = theorem_box(
            MathTex(
                r"6\,CO_2 + 6\,H_2O \xrightarrow{\;\text{lumière, chlorophylle}\;} "
                r"C_6H_{12}O_6 + 6\,O_2",
                font_size=30,
            ),
            box_width=11.5,
        )
        essentiel_eq.next_to(titre, DOWN, buff=0.6)

        with self.voiceover(
            text=(
                "Retenez cette équation par cœur : six CO2 plus six H2O, "
                "avec lumière et chlorophylle, donnent un glucose et six "
                "O2. C'est le résultat global de tout ce chapitre."
            )
        ) as tracker:
            self.play(FadeIn(essentiel_eq))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(essentiel_eq))

        # --- Piège à éviter : l'origine du dioxygène dégagé --------------------
        piege = warning_box(
            Text(
                _wrap(
                    "Piège fondamental : le dioxygène O2 rejeté ne "
                    "provient PAS du CO2, mais de l'eau, qui est « cassée "
                    "» par la lumière (photolyse). Cela a été démontré "
                    "par des expériences utilisant des isotopes marqués "
                    "(eau enrichie en oxygène 18).",
                    width=54,
                ),
                font_size=21,
            ),
            box_width=12.0,
        )
        piege.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Piège fondamental à ne jamais commettre : le dioxygène "
                "rejeté ne provient pas du dioxyde de carbone, mais de "
                "l'eau, qui est cassée par la lumière — un phénomène "
                "appelé photolyse. Cela a été démontré par des "
                "expériences utilisant des isotopes marqués, de l'eau "
                "enrichie en oxygène dix-huit. Nous y reviendrons en "
                "détail dans la partie consacrée à la phase claire."
            )
        ) as tracker:
            self.play(FadeIn(piege))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(titre), FadeOut(piege))
