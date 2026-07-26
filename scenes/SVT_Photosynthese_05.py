"""
scenes/SVT_Photosynthese_05.py — Chapitre 10 (1ereC, SVT), scène 05.

§ 10.2.3 Les pigments chlorophylliens : définition, tableau des 4 pigments
(chlorophylle a/b, carotène, xanthophylle : couleur et rôle) + méthode
point clé « pourquoi les feuilles sont vertes » (absorption rouge/bleu-
violet, réflexion du vert).
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
    Arrow,
    FadeIn,
    FadeOut,
    Rectangle,
    Text,
    VGroup,
    Write,
)

from shapes.base_scene import NotionScene
from shapes.boxes import definition_box, method_box, scene_title, warning_box


def _wrap(text: str, width: int = 56) -> str:
    return "\n".join(textwrap.fill(line, width=width) for line in text.split("\n"))


def _cell(text: str, x: float, y: float, font_size=16, color=WHITE, bold=False):
    t = Text(text, font_size=font_size, color=color, weight="BOLD" if bold else "NORMAL")
    t.move_to([x, y, 0])
    t.shift(RIGHT * (t.width / 2))
    return t


def _schema_spectre():
    """Petit spectre schématique : bandes de couleur avec flèches
    d'absorption (rouge, bleu-violet) et de réflexion (vert)."""
    couleurs = ["#7B2FBE", "#3355DD", "#2E9E4F", "#E6C619", "#E07A1F", "#C0392B"]
    noms = ["violet", "bleu", "vert", "jaune", "orange", "rouge"]
    bandes = VGroup(
        *[Rectangle(width=1.0, height=0.6, fill_color=c, fill_opacity=1.0, stroke_width=1) for c in couleurs]
    )
    bandes.arrange(RIGHT, buff=0.05)

    labels = VGroup(*[Text(n, font_size=12, color=WHITE) for n in noms])
    for lbl, bande in zip(labels, bandes):
        lbl.next_to(bande, DOWN, buff=0.1)

    fleche_absorbe_1 = Arrow(DOWN * 0.7, UP * 0.05, color="#E8E8E8", buff=0).scale(0.7)
    fleche_absorbe_1.next_to(bandes[0], UP, buff=0.15)
    fleche_absorbe_2 = Arrow(DOWN * 0.7, UP * 0.05, color="#E8E8E8", buff=0).scale(0.7)
    fleche_absorbe_2.next_to(bandes[5], UP, buff=0.15)
    label_absorbe = Text("absorbées (efficaces)", font_size=13, color="#E8E8E8")
    label_absorbe.next_to(VGroup(fleche_absorbe_1, fleche_absorbe_2), UP, buff=0.15)

    fleche_reflechie = Arrow(UP * 0.05, DOWN * 0.7, color="#3FCB63", buff=0).scale(0.7)
    fleche_reflechie.next_to(bandes[2], DOWN, buff=0.55)
    label_reflechie = Text("réfléchie -> feuille verte", font_size=13, color="#3FCB63")
    label_reflechie.next_to(fleche_reflechie, DOWN, buff=0.1)

    return VGroup(
        bandes, labels,
        fleche_absorbe_1, fleche_absorbe_2, label_absorbe,
        fleche_reflechie, label_reflechie,
    )


class PigmentsChlorophylliens(NotionScene):
    def construct(self):
        titre = scene_title("10.2.3 — Les pigments chlorophylliens")
        titre.scale(0.55)
        titre.to_edge(UP)

        # --- Énoncé : définition du pigment chlorophyllien -------------------
        definition = definition_box(
            Text(
                _wrap(
                    "Un pigment chlorophyllien est une molécule colorée, "
                    "située dans la membrane des thylakoïdes, capable "
                    "d'absorber l'énergie lumineuse et de la convertir "
                    "en énergie chimique.",
                    width=54,
                ),
                font_size=22,
            ),
            box_width=12.0,
        )
        definition.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Comment la lumière est-elle captée ? Grâce aux pigments "
                "chlorophylliens. Un pigment chlorophyllien est une "
                "molécule colorée, située dans la membrane des "
                "thylakoïdes, capable d'absorber l'énergie lumineuse et "
                "de la convertir en énergie chimique."
            )
        ) as tracker:
            self.play(Write(titre))
            self.play(FadeIn(definition))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(definition))

        # --- Animation du raisonnement : les 4 pigments (tableau) ------------
        entete_tab = Text("Quatre pigments, séparables par chromatographie", font_size=21, color=YELLOW, weight="BOLD")
        entete_tab.next_to(titre, DOWN, buff=0.4)

        x_pig, x_coul, x_role = -6.2, -1.6, 0.7
        headers = ["Pigment", "Couleur", "Rôle"]
        row_y0 = entete_tab.get_bottom()[1] - 0.55
        row_h = 0.95

        header_row = VGroup(
            *[_cell(h, x, row_y0, font_size=16, color=YELLOW, bold=True) for h, x in zip(headers, [x_pig, x_coul, x_role])]
        )

        rows_data = [
            ("Chlorophylle a", "vert bleu", "Pigment principal :\ndéclenche la conversion\nd'énergie"),
            ("Chlorophylle b", "vert jaune", "Pigment accessoire :\ncapte la lumière, transmet\nà la chlorophylle a"),
            ("Carotène", "orange", "Pigment accessoire\n(caroténoïde)"),
            ("Xanthophylle", "jaune", "Pigment accessoire\n(caroténoïde)"),
        ]

        data_rows = VGroup()
        for i, (pig, coul, role) in enumerate(rows_data):
            y = row_y0 - (i + 1) * row_h
            data_rows.add(
                VGroup(
                    _cell(pig, x_pig, y, font_size=15, color=YELLOW),
                    _cell(coul, x_coul, y, font_size=15),
                    _cell(role, x_role, y, font_size=14),
                )
            )

        tableau = VGroup(header_row, data_rows)

        with self.voiceover(
            text=(
                "Les chloroplastes contiennent en réalité plusieurs "
                "pigments, séparables par chromatographie sur papier. La "
                "chlorophylle a, vert bleu, est le pigment principal : "
                "c'est elle qui déclenche la conversion de l'énergie "
                "lumineuse. La chlorophylle b, vert jaune, est un "
                "pigment accessoire : elle capte la lumière et transmet "
                "l'énergie à la chlorophylle a. Le carotène, orange, et "
                "la xanthophylle, jaune, sont deux autres pigments "
                "accessoires, de la famille des caroténoïdes."
            )
        ) as tracker:
            self.play(FadeIn(entete_tab))
            self.play(FadeIn(header_row))
            for row in data_rows:
                self.play(FadeIn(row), run_time=0.5)
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(entete_tab), FadeOut(tableau))

        # --- Exemple traité : pourquoi les feuilles sont-elles vertes ? ------
        pourquoi_texte = Text(
            _wrap(
                "Les chlorophylles absorbent surtout la lumière rouge et "
                "bleu-violet, et réfléchissent la lumière verte, qui "
                "frappe notre œil.",
                width=48,
            ),
            font_size=19,
            color=WHITE,
        )
        pourquoi_texte.to_edge(LEFT, buff=0.5).shift(UP * 1.0)

        spectre = _schema_spectre()
        spectre.scale(0.95)
        spectre.next_to(pourquoi_texte, DOWN, buff=0.6).align_to(pourquoi_texte, LEFT).shift(RIGHT * 0.3)

        methode = method_box(
            Text(
                "Pourquoi les feuilles sont-elles vertes ?",
                font_size=19,
                weight="BOLD",
            ),
            box_width=8.5,
        )
        methode.to_edge(UP).shift(DOWN * 1.0 + RIGHT * 0.0)
        methode.next_to(titre, DOWN, buff=0.3)

        with self.voiceover(
            text=(
                "Un point clé à comprendre : pourquoi les feuilles "
                "sont-elles vertes ? Les chlorophylles absorbent surtout "
                "la lumière rouge et la lumière bleu-violet — c'est cette "
                "énergie absorbée qui alimente la photosynthèse — et "
                "elles réfléchissent la lumière verte, qui frappe notre "
                "œil : d'où la couleur verte des végétaux. La lumière "
                "verte est donc peu efficace pour la photosynthèse, "
                "contrairement aux lumières rouge et bleu-violet."
            )
        ) as tracker:
            self.play(FadeIn(methode))
            self.play(FadeIn(pourquoi_texte))
            self.play(FadeIn(spectre))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(methode), FadeOut(pourquoi_texte), FadeOut(spectre))

        # --- À retenir -----------------------------------------------------------
        essentiel = definition_box(
            Text(
                _wrap(
                    "À retenir : 4 pigments dans le chloroplaste — "
                    "chlorophylle a (principale), chlorophylle b, "
                    "carotène, xanthophylle (accessoires). Ensemble, ils "
                    "absorbent le rouge et le bleu-violet, réfléchissent "
                    "le vert : d'où la couleur verte des feuilles.",
                    width=54,
                ),
                font_size=20,
            ),
            box_width=12.0,
        )
        essentiel.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Retenons : le chloroplaste contient quatre pigments, la "
                "chlorophylle a, principale, et trois pigments "
                "accessoires, chlorophylle b, carotène et xanthophylle. "
                "Ensemble, ils absorbent surtout le rouge et le "
                "bleu-violet et réfléchissent le vert, ce qui donne leur "
                "couleur aux feuilles."
            )
        ) as tracker:
            self.play(FadeIn(essentiel))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(essentiel))

        # --- Piège à éviter : les 4 pigments coexistent toujours -------------
        piege = warning_box(
            Text(
                _wrap(
                    "Piège à éviter : ne pas croire que seule la "
                    "chlorophylle a colore la feuille. Les 4 pigments "
                    "coexistent en permanence ; en automne, la "
                    "chlorophylle (verte) se dégrade plus vite que les "
                    "caroténoïdes (orange, jaune), qui deviennent alors "
                    "visibles : d'où les feuilles jaunes et orangées.",
                    width=54,
                ),
                font_size=20,
            ),
            box_width=12.0,
        )
        piege.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Attention à un piège classique : il ne faut pas croire "
                "que seule la chlorophylle colore la feuille. En "
                "réalité, les quatre pigments coexistent en permanence. "
                "En automne, la chlorophylle, verte, se dégrade plus "
                "vite que les caroténoïdes, orange et jaune, qui "
                "deviennent alors visibles : c'est ce qui explique les "
                "feuilles jaunes et orangées de la saison sèche."
            )
        ) as tracker:
            self.play(FadeIn(piege))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(titre), FadeOut(piege))
