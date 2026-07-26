"""
scenes/Chimie_Benzene_06.py — Chapitre 4 (1ereC, Chimie), scène 06.

§ Propriétés physiques du benzène : tableau (liquide incolore, odeur
âcre, Tfus = 5,5 °C, Téb = 80,1 °C, ρ ≈ 0,88 g/mL, insoluble dans l'eau /
soluble dans les solvants organiques, très inflammable, flamme jaune
fuligineuse). warning_box : combustion complète
2 C6H6 + 15 O2 → 12 CO2 + 6 H2O.
Source : 1ereC/Chimie.pdf, chapitre 4, page 39.
"""

import textwrap

from manim import (
    DOWN,
    LEFT,
    RIGHT,
    UP,
    ORANGE,
    WHITE,
    YELLOW,
    FadeIn,
    FadeOut,
    Line,
    MathTex,
    Rectangle,
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


def _tableau(entetes, lignes, col_widths, row_height=0.5, font_size=19):
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

    return VGroup(contour, lignes_h, lignes_v, cells)


class ProprietesPhysiquesBenzene(NotionScene):
    def construct(self):
        titre = scene_title("6. Propriétés physiques du benzène")
        titre.scale(0.55)
        titre.to_edge(UP)

        # --- Énoncé -------------------------------------------------------------
        enonce = Text(
            _wrap(
                "Au-delà de sa structure, le benzène possède des "
                "propriétés physiques bien identifiées, qu'il faut "
                "connaître notamment pour des raisons de sécurité au "
                "laboratoire et en milieu industriel.",
                width=54,
            ),
            font_size=25,
            color=WHITE,
        )
        enonce.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Au-delà de sa structure originale, le benzène possède "
                "des propriétés physiques bien identifiées, qu'il faut "
                "connaître notamment pour des raisons de sécurité, au "
                "laboratoire comme en milieu industriel."
            )
        ) as tracker:
            self.play(Write(titre))
            self.play(FadeIn(enonce))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(enonce))

        # --- Animation du raisonnement : tableau des propriétés ------------------
        entete = Text("Fiche d'identité physique du benzène", font_size=24, color=YELLOW, weight="BOLD")
        entete.next_to(titre, DOWN, buff=0.35)

        tableau = _tableau(
            ["Propriété", "Valeur"],
            [
                ["Aspect", "liquide incolore"],
                ["Odeur", "âcre, caractéristique"],
                ["Température de fusion", "5,5 °C"],
                ["Température d'ébullition", "80,1 °C"],
                ["Masse volumique", "ρ ≈ 0,88 g/mL"],
                ["Solubilité dans l'eau", "insoluble"],
                ["Solubilité solvants organiques", "soluble"],
                ["Inflammabilité", "très inflammable"],
                ["Combustion à l'air libre", "flamme jaune, fuligineuse"],
            ],
            col_widths=[4.2, 3.4],
            row_height=0.42,
            font_size=18,
        )
        tableau.next_to(entete, DOWN, buff=0.3)
        groupe_tab = VGroup(entete, tableau)
        _fit(groupe_tab, titre.get_bottom()[1] - 0.3)

        with self.voiceover(
            text=(
                "Le benzène est un liquide incolore, à l'odeur âcre et "
                "caractéristique. Sa température de fusion est de cinq "
                "virgule cinq degrés Celsius, sa température d'ébullition "
                "de quatre-vingts virgule un degrés Celsius, et sa masse "
                "volumique d'environ zéro virgule quatre-vingt-huit "
                "gramme par millilitre. Il est insoluble dans l'eau, mais "
                "soluble dans les solvants organiques. Enfin, c'est un "
                "liquide très inflammable : sa combustion à l'air libre "
                "produit une flamme jaune et fuligineuse, chargée de "
                "suie — signe d'une combustion incomplète, caractéristique "
                "des composés très riches en carbone."
            )
        ) as tracker:
            self.play(FadeIn(entete))
            self.play(FadeIn(tableau))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(groupe_tab))

        # --- Exemple traité : la flamme, signature d'un hydrocarbure riche en C -
        entete2 = Text("Pourquoi une flamme fuligineuse ?", font_size=24, color=YELLOW, weight="BOLD")
        entete2.next_to(titre, DOWN, buff=0.4)

        explication = Text(
            _wrap(
                "Le rapport H/C du benzène (1:1) est faible comparé à "
                "celui d'un alcane. En combustion à l'air libre "
                "(dioxygène en défaut), une partie du carbone n'est pas "
                "oxydée en CO2 : il se dépose sous forme de fines "
                "particules de suie, visibles dans la flamme jaune.",
                width=50,
            ),
            font_size=22,
            color=WHITE,
        )
        explication.next_to(entete2, DOWN, buff=0.4)
        groupe_expl = VGroup(entete2, explication)
        _fit(groupe_expl, titre.get_bottom()[1] - 0.4)

        with self.voiceover(
            text=(
                "Cette flamme fuligineuse s'explique par le rapport entre "
                "hydrogène et carbone dans la molécule, égal à un pour "
                "un, plus faible que dans un alcane. En combustion à "
                "l'air libre, où le dioxygène est en défaut, une partie "
                "du carbone n'est pas complètement oxydée en dioxyde de "
                "carbone : il se dépose sous forme de fines particules de "
                "suie, que l'on observe dans la flamme jaune."
            )
        ) as tracker:
            self.play(FadeIn(entete2))
            self.play(FadeIn(explication))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(groupe_expl))

        # --- À retenir : la combustion complète, en excès de dioxygène ----------
        entete3 = Text("En excès de dioxygène : combustion complète", font_size=22, color=YELLOW, weight="BOLD")
        entete3.next_to(titre, DOWN, buff=0.4)

        eq_complete = MathTex(
            r"2\,C_6H_6 + 15\,O_2 \rightarrow 12\,CO_2 + 6\,H_2O",
            font_size=32,
            color=WHITE,
        )
        eq_complete.next_to(entete3, DOWN, buff=0.5)
        groupe3 = VGroup(entete3, eq_complete)

        with self.voiceover(
            text=(
                "Mais si le dioxygène est apporté en excès, la combustion "
                "devient complète : deux molécules de benzène réagissent "
                "avec quinze molécules de dioxygène pour donner douze "
                "molécules de dioxyde de carbone et six molécules d'eau. "
                "Retenons bien cette équation, avec ses coefficients pairs "
                "nécessaires pour équilibrer les huit atomes d'oxygène par "
                "molécule de benzène brûlée."
            )
        ) as tracker:
            self.play(FadeIn(entete3))
            self.play(Write(eq_complete))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(groupe3))

        # --- Piège à éviter : bien équilibrer la combustion ----------------------
        piege = warning_box(
            MathTex(
                r"2\,C_6H_6 + 15\,O_2 \rightarrow 12\,CO_2 + 6\,H_2O",
                font_size=30,
            ),
        )
        piege_texte = Text(
            _wrap(
                "Piège fréquent : oublier le coefficient 2 devant C6H6 "
                "(nécessaire car 15 est impair) et écrire une équation "
                "non équilibrée en oxygène.",
                width=44,
            ),
            font_size=20,
            color=YELLOW,
        )
        groupe_piege = VGroup(piege, piege_texte).arrange(DOWN, buff=0.35)
        groupe_piege.next_to(titre, DOWN, buff=0.5)
        _fit(groupe_piege, titre.get_bottom()[1] - 0.4)

        with self.voiceover(
            text=(
                "Attention à un piège classique lors de l'équilibrage : "
                "il faut bien placer le coefficient deux devant le "
                "benzène, car le nombre d'atomes d'oxygène côté "
                "dioxygène, quinze fois deux soit trente, doit égaler "
                "celui côté produits. Une équation non équilibrée, même "
                "avec les bons produits CO2 et H2O, reste fausse."
            )
        ) as tracker:
            self.play(FadeIn(groupe_piege))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(groupe_piege), FadeOut(titre))
