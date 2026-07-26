"""
scenes/SVT_Photosynthese_04.py — Chapitre 10 (1ereC, SVT), scène 04.

§ 10.2.2 Structure du chloroplaste : organite ovoïde de 4-10µm, double
membrane, schéma complet (membrane externe/interne, stroma, thylakoïdes
empilés en grana, lamelles intergranaires, grains d'amidon) + tableau des
deux compartiments (stroma / thylakoïdes : description et rôle).
Source : 1ereC/SVT.pdf, page 108.
"""

import textwrap

from manim import (
    DOWN,
    LEFT,
    RIGHT,
    UP,
    WHITE,
    YELLOW,
    Dot,
    Ellipse,
    FadeIn,
    FadeOut,
    Line,
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


def _cell(text: str, x: float, y: float, font_size=15, color=WHITE, bold=False):
    t = Text(text, font_size=font_size, color=color, weight="BOLD" if bold else "NORMAL")
    t.move_to([x, y, 0])
    t.shift(RIGHT * (t.width / 2))
    return t


def _granum(x, y, n=4, color="#1F7A3D"):
    """Empilement de n thylakoïdes (granum), sous forme de petits
    disques aplatis superposés."""
    disques = VGroup(
        *[
            Ellipse(width=0.42, height=0.12, fill_color=color, fill_opacity=0.95, stroke_color="#0F5A22", stroke_width=1)
            for _ in range(n)
        ]
    )
    disques.arrange(UP, buff=0.03)
    disques.move_to([x, y, 0])
    return disques


def _schema_chloroplaste():
    membrane_ext = Ellipse(width=7.4, height=3.6, stroke_color=WHITE, stroke_width=2.5, fill_opacity=0)
    membrane_int = Ellipse(width=7.0, height=3.25, stroke_color="#AACBAA", stroke_width=1.5, fill_opacity=0)
    stroma = Ellipse(width=7.0, height=3.25, fill_color="#2E5B3A", fill_opacity=0.35, stroke_width=0)

    grana_positions = [(-2.6, 0.2), (-1.2, -0.5), (0.1, 0.4), (1.4, -0.4), (2.6, 0.3)]
    grana = VGroup(*[_granum(x, y) for x, y in grana_positions])

    # Lamelles intergranaires : relient les sommets des grana voisins.
    lamelles = VGroup(
        *[
            Line(grana[i].get_right() + RIGHT * 0.02, grana[i + 1].get_left() + LEFT * 0.02,
                 color="#66A876", stroke_width=1.5)
            for i in range(len(grana) - 1)
        ]
    )

    amidon = VGroup(
        *[
            Dot(radius=0.11, color="#E8D9A0")
            for _ in range(3)
        ]
    )
    amidon_positions = [(-1.9, 1.15), (1.9, 1.05), (0.4, -1.15)]
    for a, (dx, dy) in zip(amidon, amidon_positions):
        a.move_to([dx, dy, 0])

    corps = VGroup(membrane_ext, membrane_int, stroma, grana, lamelles, amidon)

    # Étiquettes reliées par de petits traits (lignes de rappel), avec des
    # points d'ancrage EXPLICITES (plutôt que point_at_angle) pour garder un
    # contrôle total sur l'espacement et éviter tout chevauchement de texte.
    def _label(text, point, direction, color=WHITE, buff=1.1, fs=14):
        lbl = Text(text, font_size=fs, color=color)
        lbl.move_to(point + direction * buff)
        trait = Line(point, lbl.get_center() - direction * (lbl.width / 2 + 0.05), color=color, stroke_width=1)
        return VGroup(trait, lbl)

    # Point le plus à droite de la membrane externe -> étiquette à droite.
    label_mext = _label("membrane externe", [3.7, 0, 0], RIGHT, color="#DDDDDD", buff=1.0)
    # Point le plus à gauche de la membrane interne -> étiquette à gauche.
    label_mint = _label("membrane interne", [-3.5, 0, 0], LEFT, color="#AACBAA", buff=1.0)
    label_stroma = Text("stroma", font_size=14, color="#8FCB9A")
    label_stroma.move_to([0, -1.55, 0])
    # Granum central (le plus haut) -> étiquette au-dessus, bien séparée.
    label_granum = _label("granum (thylakoïdes\nempilés)", grana[2].get_top(), UP, color="#3FCB63", buff=0.55)
    label_lamelle = _label("lamelle\nintergranaire", lamelles[1].get_center(), DOWN, color="#66A876", buff=0.55)
    label_amidon = _label("grain d'amidon", amidon[0].get_center(), UP + LEFT * 0.2, color="#E8D9A0", buff=0.55)

    return VGroup(
        corps, label_mext, label_mint, label_stroma, label_granum, label_lamelle, label_amidon,
    )


class StructureChloroplaste(NotionScene):
    def construct(self):
        titre = scene_title("10.2.2 — La structure du chloroplaste")
        titre.scale(0.55)
        titre.to_edge(UP)

        # --- Énoncé : le chloroplaste, un organite ovoïde --------------------
        intro = Text(
            _wrap(
                "Le chloroplaste est un organite cellulaire ovoïde de 4 "
                "à 10 micromètres de long, entouré d'une double "
                "membrane. C'est à l'intérieur qu'ont lieu toutes les "
                "réactions de la photosynthèse.",
                width=56,
            ),
            font_size=23,
            color=WHITE,
        )
        intro.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Le chloroplaste est un organite cellulaire ovoïde, "
                "long de quatre à dix micromètres, entouré d'une double "
                "membrane. C'est à l'intérieur de cet organite "
                "qu'ont lieu toutes les réactions de la photosynthèse."
            )
        ) as tracker:
            self.play(Write(titre))
            self.play(FadeIn(intro))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(intro))

        # --- Animation du raisonnement : schéma complet du chloroplaste ------
        schema = _schema_chloroplaste()
        schema.scale(0.92)
        schema.next_to(titre, DOWN, buff=0.55)

        with self.voiceover(
            text=(
                "Observons son schéma complet. Deux membranes, externe "
                "et interne, délimitent l'organite. À l'intérieur, un "
                "gel, le stroma, remplit tout l'espace. Dans ce stroma "
                "baignent des empilements de sacculets membranaires "
                "aplatis, les thylakoïdes, regroupés en colonnes "
                "appelées grana, singulier granum, reliés entre eux par "
                "des lamelles intergranaires. Le stroma peut aussi "
                "contenir des grains d'amidon, forme de réserve du "
                "glucose produit."
            )
        ) as tracker:
            self.play(FadeIn(schema))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(schema))

        # --- Exemple traité : les deux compartiments (tableau) ---------------
        entete_tab = Text("Les deux compartiments du chloroplaste", font_size=23, color=YELLOW, weight="BOLD")
        entete_tab.next_to(titre, DOWN, buff=0.4)

        x_comp, x_desc, x_role = -6.4, -3.2, 2.6
        headers = ["Compartiment", "Description", "Rôle"]
        row_y0 = entete_tab.get_bottom()[1] - 0.55
        row_h = 1.15

        header_row = VGroup(
            *[_cell(h, x, row_y0, font_size=16, color=YELLOW, bold=True) for h, x in zip(headers, [x_comp, x_desc, x_role])]
        )

        rows_data = [
            (
                "Stroma",
                "Matrice fondamentale (gel)\nremplissant l'espace interne ;\nenzymes du cycle de Calvin,\nADN chloroplastique, ribosomes",
                "Siège de la phase\nbiochimique\n(phase sombre)",
            ),
            (
                "Thylakoïdes",
                "Sacculets membranaires\naplatis, empilés en grana,\nreliés par des lamelles\nintergranaires ; portent les\npigments",
                "Siège de la phase\nphotochimique\n(phase claire)",
            ),
        ]

        data_rows = VGroup()
        for i, (comp, desc, role) in enumerate(rows_data):
            y = row_y0 - (i + 1) * row_h
            data_rows.add(
                VGroup(
                    _cell(comp, x_comp, y, font_size=15, color=YELLOW),
                    _cell(desc, x_desc, y, font_size=13),
                    _cell(role, x_role, y, font_size=14),
                )
            )

        tableau = VGroup(header_row, data_rows)
        bas_visible = -config.frame_height / 2 + 0.3
        hauteur_dispo = row_y0 - bas_visible + 0.3
        if tableau.height > hauteur_dispo:
            tableau.scale(hauteur_dispo / tableau.height, about_point=[0, row_y0, 0])

        with self.voiceover(
            text=(
                "On distingue deux compartiments essentiels. Le stroma "
                "est la matrice fondamentale, un gel qui remplit "
                "l'espace interne ; il contient les enzymes du cycle de "
                "Calvin, l'ADN chloroplastique et des ribosomes : c'est "
                "le siège de la phase biochimique, la phase sombre. Les "
                "thylakoïdes sont des sacculets membranaires aplatis, "
                "empilés en grana, reliés entre eux par des lamelles "
                "intergranaires ; leurs membranes portent les pigments "
                "chlorophylliens : ce sont eux le siège de la phase "
                "photochimique, la phase claire."
            )
        ) as tracker:
            self.play(FadeIn(entete_tab))
            self.play(FadeIn(header_row))
            for row in data_rows:
                self.play(FadeIn(row), run_time=0.5)
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(entete_tab), FadeOut(tableau))

        # --- À retenir ----------------------------------------------------------
        essentiel = definition_box(
            Text(
                _wrap(
                    "À retenir : le chloroplaste = double membrane + "
                    "stroma (phase sombre, enzymes, ADN, amidon) + "
                    "thylakoïdes empilés en grana (phase claire, "
                    "pigments), reliés par des lamelles intergranaires.",
                    width=54,
                ),
                font_size=21,
            ),
            box_width=12.0,
        )
        essentiel.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Retenons donc : le chloroplaste, c'est une double "
                "membrane entourant un stroma, siège de la phase sombre, "
                "avec ses enzymes, son ADN et ses grains d'amidon, et des "
                "thylakoïdes empilés en grana, siège de la phase claire, "
                "porteurs des pigments, le tout relié par des lamelles "
                "intergranaires."
            )
        ) as tracker:
            self.play(FadeIn(essentiel))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(essentiel))

        # --- Piège à éviter : ne pas confondre les deux compartiments --------
        piege = warning_box(
            Text(
                _wrap(
                    "Piège à éviter : ne pas confondre les deux "
                    "compartiments. La phase claire (photolyse, ATP, "
                    "NADPH,H+) se déroule DANS les membranes des "
                    "thylakoïdes, pas dans le stroma ; la phase sombre "
                    "(cycle de Calvin) se déroule dans le stroma, pas "
                    "dans les thylakoïdes.",
                    width=54,
                ),
                font_size=20,
            ),
            box_width=12.0,
        )
        piege.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Attention à ne pas confondre les deux compartiments : la "
                "phase claire, avec la photolyse de l'eau et la "
                "production d'ATP et de NADPH,H plus, se déroule dans les "
                "membranes des thylakoïdes, et non dans le stroma ; la "
                "phase sombre, le cycle de Calvin, se déroule dans le "
                "stroma, et non dans les thylakoïdes. Nous détaillerons "
                "ces deux phases dans les prochaines scènes."
            )
        ) as tracker:
            self.play(FadeIn(piege))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(titre), FadeOut(piege))
