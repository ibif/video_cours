"""
scenes/SVT_Photosynthese_10.py — Chapitre 10 (1ereC, SVT), scène 10.

§ 10.4.4 Tableau comparatif des deux phases (lieu, lumière, réactifs,
produits, réactions clés, rôle énergétique) + schéma récapitulatif global
des deux phases dans le chloroplaste (phase claire -> ATP/NADPH,H+ ->
phase sombre -> glucose).
Source : 1ereC/SVT.pdf, page 110.
"""

import textwrap

from manim import (
    DOWN,
    LEFT,
    RIGHT,
    UP,
    WHITE,
    YELLOW,
    Arrow,
    FadeIn,
    FadeOut,
    RoundedRectangle,
    Text,
    VGroup,
    Write,
    config,
)

from shapes.base_scene import NotionScene
from shapes.boxes import definition_box, scene_title, warning_box


def _wrap(text: str, width: int = 56) -> str:
    return "\n".join(textwrap.fill(line, width=width) for line in text.split("\n"))


def _cell(text: str, x: float, y: float, font_size=13, color=WHITE, bold=False):
    t = Text(text, font_size=font_size, color=color, weight="BOLD" if bold else "NORMAL")
    t.move_to([x, y, 0])
    t.shift(RIGHT * (t.width / 2))
    return t


def _schema_recapitulatif():
    """Schéma global : phase claire (thylakoïdes, en haut) reliée à la
    phase sombre (stroma, en bas) par l'ATP et le NADPH,H+, avec les
    échanges de gaz et de matière avec l'extérieur du chloroplaste."""
    # Les deux boîtes sont créées ET arrangées AVANT tout positionnement
    # relatif (labels, flèches) : `arrange()` déplace les Mobjects, donc
    # tout élément positionné par rapport à eux doit être calculé APRÈS.
    boite_claire = RoundedRectangle(width=5.2, height=1.4, corner_radius=0.15, fill_color="#1F7A3D", fill_opacity=0.35, stroke_color="#3FCB63", stroke_width=2)
    boite_sombre = RoundedRectangle(width=5.2, height=1.4, corner_radius=0.15, fill_color="#5A3D1F", fill_opacity=0.35, stroke_color="#DE7C1F", stroke_width=2)
    boites = VGroup(boite_claire, boite_sombre).arrange(DOWN, buff=1.4)

    label_claire = Text("Phase claire (thylakoïdes)", font_size=16, color="#3FCB63", weight="BOLD")
    label_claire.move_to(boite_claire.get_center())

    label_sombre = Text("Phase sombre : cycle de Calvin (stroma)", font_size=15, color="#DE7C1F", weight="BOLD")
    label_sombre.move_to(boite_sombre.get_center())

    # Entrées / sorties de la phase claire.
    in_lum = Arrow(LEFT * 1.0, RIGHT * 0.05, color=YELLOW, buff=0).scale(0.8)
    in_lum.next_to(boite_claire, LEFT, buff=0.1).shift(UP * 0.25)
    label_lum = Text("lumière", font_size=12, color=YELLOW).next_to(in_lum, UP, buff=0.05)

    in_eau = Arrow(LEFT * 1.0, RIGHT * 0.05, color="#5AA9E6", buff=0).scale(0.8)
    in_eau.next_to(boite_claire, LEFT, buff=0.1).shift(DOWN * 0.35)
    label_eau = Text("H2O", font_size=12, color="#5AA9E6").next_to(in_eau, DOWN, buff=0.05)

    out_o2 = Arrow(LEFT * 0.05, RIGHT * 1.0, color="#3FCB63", buff=0).scale(0.8)
    out_o2.next_to(boite_claire, RIGHT, buff=0.1)
    label_o2 = Text("O2 dégagé", font_size=12, color="#3FCB63").next_to(out_o2, UP, buff=0.05)

    # Flèche descendante : ATP + NADPH,H+ de la phase claire vers la sombre.
    fleche_descend = Arrow(boite_claire.get_bottom(), boite_sombre.get_top(), color="#F1C40F", buff=0.1)
    label_descend = Text("ATP, NADPH,H+", font_size=13, color="#F1C40F").next_to(fleche_descend, LEFT, buff=0.15)

    # Flèche montante : ADP+Pi, NADP+ recyclés vers la phase claire.
    fleche_monte = Arrow(boite_sombre.get_top() + RIGHT * 1.4, boite_claire.get_bottom() + RIGHT * 1.4, color="#AAAAAA", buff=0.1)
    label_monte = Text("ADP+Pi, NADP+", font_size=12, color="#AAAAAA").next_to(fleche_monte, RIGHT, buff=0.1)

    # Entrées / sorties de la phase sombre.
    in_co2 = Arrow(LEFT * 1.0, RIGHT * 0.05, color="#888888", buff=0).scale(0.8)
    in_co2.next_to(boite_sombre, LEFT, buff=0.1)
    label_co2 = Text("CO2 (air)", font_size=12, color="#888888").next_to(in_co2, DOWN, buff=0.05)

    out_glucose = Arrow(LEFT * 0.05, RIGHT * 1.0, color="#E8D9A0", buff=0).scale(0.8)
    out_glucose.next_to(boite_sombre, RIGHT, buff=0.1)
    label_glucose = Text("glucose", font_size=12, color="#E8D9A0").next_to(out_glucose, DOWN, buff=0.05)

    return VGroup(
        boites, label_claire, label_sombre,
        in_lum, label_lum, in_eau, label_eau, out_o2, label_o2,
        fleche_descend, label_descend, fleche_monte, label_monte,
        in_co2, label_co2, out_glucose, label_glucose,
    )


class ComparaisonEtSchemaGlobal(NotionScene):
    def construct(self):
        titre = scene_title("10.4.4 — Comparaison des deux phases")
        titre.scale(0.55)
        titre.to_edge(UP)

        # --- Énoncé : deux phases complémentaires -----------------------------
        intro = Text(
            _wrap(
                "Nous avons étudié séparément les deux phases de la "
                "photosynthèse. Comparons-les maintenant terme à terme, "
                "avant de les replacer ensemble dans le chloroplaste.",
                width=56,
            ),
            font_size=23,
            color=WHITE,
        )
        intro.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Nous avons étudié séparément la phase claire et la "
                "phase sombre de la photosynthèse. Comparons-les "
                "maintenant terme à terme, avant de les replacer "
                "ensemble dans le chloroplaste."
            )
        ) as tracker:
            self.play(Write(titre))
            self.play(FadeIn(intro))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(intro))

        # --- Animation du raisonnement : tableau comparatif ---------------------
        entete_tab = Text("Tableau comparatif des deux phases", font_size=21, color=YELLOW, weight="BOLD")
        entete_tab.next_to(titre, DOWN, buff=0.35)

        x_crit, x_claire, x_sombre = -6.4, -2.0, 2.5
        headers = ["Critère", "Phase claire", "Phase sombre"]
        row_y0 = entete_tab.get_bottom()[1] - 0.45
        row_h = 0.78

        header_row = VGroup(
            *[_cell(h, x, row_y0, font_size=15, color=YELLOW, bold=True) for h, x in zip(headers, [x_crit, x_claire, x_sombre])]
        )

        rows_data = [
            ("Lieu", "Membranes des\nthylakoïdes (grana)", "Stroma"),
            ("Lumière", "Indispensable", "Non indispensable\ndirectement"),
            ("Réactifs\nprincipaux", "H2O, NADP+,\nADP, Pi", "CO2, ATP,\nNADPH,H+, RuBP"),
            ("Produits", "O2, ATP,\nNADPH,H+", "Glucose (PGAL),\nNADP+, ADP, Pi"),
            ("Réactions\nclés", "Photolyse de l'eau,\nphotophosphorylation", "Fixation CO2 (Rubisco),\nréduction, régénération"),
            ("Rôle\nénergétique", "Conversion lumière\n-> énergie chimique", "Utilisation énergie\nchimique -> sucre"),
        ]

        data_rows = VGroup()
        for i, (crit, claire, sombre) in enumerate(rows_data):
            y = row_y0 - (i + 1) * row_h
            data_rows.add(
                VGroup(
                    _cell(crit, x_crit, y, font_size=13, color=YELLOW),
                    _cell(claire, x_claire, y, font_size=12, color="#3FCB63"),
                    _cell(sombre, x_sombre, y, font_size=12, color="#DE7C1F"),
                )
            )

        tableau = VGroup(header_row, data_rows)
        bas_visible = -config.frame_height / 2 + 0.25
        hauteur_dispo = row_y0 - bas_visible + 0.25
        if tableau.height > hauteur_dispo:
            tableau.scale(hauteur_dispo / tableau.height, about_point=[0, row_y0, 0])

        with self.voiceover(
            text=(
                "Voici le tableau comparatif complet. Le lieu : "
                "membranes des thylakoïdes pour la phase claire, stroma "
                "pour la phase sombre. La lumière : indispensable pour "
                "la première, non indispensable directement pour la "
                "seconde. Les réactifs principaux : eau, NADP plus, ADP "
                "et phosphate pour la phase claire ; CO2, ATP, "
                "NADPH,H plus et RuBP pour la phase sombre. Les "
                "produits : O2, ATP et NADPH,H plus pour la première ; "
                "glucose, NADP plus, ADP et phosphate pour la seconde. "
                "Les réactions clés : photolyse de l'eau et "
                "photophosphorylation d'un côté ; fixation du CO2 par la "
                "Rubisco, réduction et régénération du RuBP de l'autre. "
                "Et le rôle énergétique : conversion de la lumière en "
                "énergie chimique pour la phase claire ; utilisation de "
                "cette énergie chimique pour fabriquer le sucre pour la "
                "phase sombre."
            )
        ) as tracker:
            self.play(FadeIn(entete_tab))
            self.play(FadeIn(header_row))
            for row in data_rows:
                self.play(FadeIn(row), run_time=0.35)
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(entete_tab), FadeOut(tableau))

        # --- Exemple traité : schéma récapitulatif global -----------------------
        schema = _schema_recapitulatif()
        schema.scale(0.85)
        schema.next_to(titre, DOWN, buff=0.6)

        with self.voiceover(
            text=(
                "Replaçons maintenant les deux phases ensemble dans le "
                "chloroplaste. Dans les thylakoïdes, la phase claire "
                "reçoit la lumière et l'eau, et dégage du dioxygène ; "
                "elle produit de l'ATP et du NADPH,H plus, qui migrent "
                "vers le stroma voisin. Là, dans le stroma, la phase "
                "sombre utilise cet ATP et ce NADPH,H plus pour fixer le "
                "CO2 de l'air et fabriquer du glucose, tout en "
                "régénérant l'ADP, le phosphate et le NADP plus, qui "
                "repartent vers les thylakoïdes pour un nouveau cycle. "
                "Les deux phases forment ainsi un couple parfaitement "
                "coordonné."
            )
        ) as tracker:
            self.play(FadeIn(schema))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(schema))

        # --- À retenir -----------------------------------------------------------
        essentiel = definition_box(
            Text(
                _wrap(
                    "À retenir : les deux phases sont interdépendantes. "
                    "La phase claire (thylakoïdes) fournit l'énergie "
                    "(ATP) et le pouvoir réducteur (NADPH,H+) à la phase "
                    "sombre (stroma), qui les utilise pour fixer le CO2 "
                    "et fabriquer le glucose, tout en recyclant ADP, Pi "
                    "et NADP+ vers la phase claire.",
                    width=54,
                ),
                font_size=19,
            ),
            box_width=12.2,
        )
        essentiel.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Retenons l'essentiel : les deux phases sont "
                "interdépendantes. La phase claire fournit l'énergie et "
                "le pouvoir réducteur à la phase sombre, qui les utilise "
                "pour fixer le CO2 et fabriquer le glucose, tout en "
                "recyclant l'ADP, le phosphate et le NADP plus vers la "
                "phase claire."
            )
        ) as tracker:
            self.play(FadeIn(essentiel))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(essentiel))

        # --- Piège à éviter : les deux phases se déroulent simultanément -----
        piege = warning_box(
            Text(
                _wrap(
                    "Piège à éviter : ne pas imaginer les deux phases "
                    "comme deux étapes successives dans le temps "
                    "(d'abord l'une, puis l'autre, à la fin de la "
                    "journée). Elles se déroulent SIMULTANÉMENT, à la "
                    "lumière, dans deux compartiments voisins reliés en "
                    "continu par l'ATP et le NADPH,H+.",
                    width=54,
                ),
                font_size=19,
            ),
            box_width=12.0,
        )
        piege.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Attention à ne pas imaginer les deux phases comme deux "
                "étapes successives dans le temps, d'abord l'une, puis "
                "l'autre à la fin de la journée. Elles se déroulent au "
                "contraire simultanément, à la lumière, dans deux "
                "compartiments voisins du chloroplaste, reliés en "
                "continu par les navettes d'ATP et de NADPH,H plus."
            )
        ) as tracker:
            self.play(FadeIn(piege))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(titre), FadeOut(piege))
