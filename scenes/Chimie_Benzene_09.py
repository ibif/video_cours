"""
scenes/Chimie_Benzene_09.py — Chapitre 4 (1ereC, Chimie), scène 09.

§ Comparaison benzène / alcènes + additions en conditions drastiques :
tableau comparatif (électrons π, eau de brome, dibrome + FeBr3, type de
réaction privilégié, dégagement gazeux). property_box : test
caractéristique (le benzène ne décolore PAS l'eau de brome). Additions en
conditions drastiques : hydrogénation (Ni/Pt, 150 °C) → cyclohexane,
chloration sous UV → hexachlorocyclohexane — le caractère aromatique est
alors détruit.
Source : 1ereC/Chimie.pdf, chapitre 4, page 42.
"""

import textwrap

from manim import (
    DOWN,
    LEFT,
    RIGHT,
    UP,
    WHITE,
    YELLOW,
    RED,
    GREEN,
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
from shapes.boxes import property_box, scene_title


def _wrap(text: str, width: int = 56) -> str:
    return "\n".join(textwrap.fill(line, width=width) for line in text.split("\n"))


def _fit(mobject, top_y):
    bas_visible = -config.frame_height / 2 + 0.25
    hauteur_dispo = top_y - bas_visible
    if mobject.height > hauteur_dispo:
        mobject.scale(hauteur_dispo / mobject.height, about_point=mobject.get_top())
    return mobject


def _tableau(entetes, lignes, col_widths, row_height=0.5, font_size=16):
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
            couleur = RED if val == "NON" else (GREEN if val == "OUI" else WHITE)
            c = Text(val, font_size=font_size, color=couleur)
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


class ComparaisonBenzeneAlcenes(NotionScene):
    def construct(self):
        titre = scene_title("9. Benzène et alcènes : comparaison")
        titre.scale(0.55)
        titre.to_edge(UP)

        # --- Énoncé ---------------------------------------------------------------
        enonce = Text(
            _wrap(
                "Le benzène et les alcènes possèdent tous deux des "
                "électrons π. Pourtant, leur comportement chimique "
                "diffère radicalement dans les conditions usuelles. "
                "Comparons-les.",
                width=52,
            ),
            font_size=25,
            color=WHITE,
        )
        enonce.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Le benzène et les alcènes possèdent tous deux des "
                "électrons pi. Pourtant, leur comportement chimique "
                "diffère radicalement dans les conditions usuelles. "
                "Comparons-les point par point."
            )
        ) as tracker:
            self.play(Write(titre))
            self.play(FadeIn(enonce))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(enonce))

        # --- Animation du raisonnement : tableau comparatif ------------------------
        entete = Text("Tableau comparatif", font_size=24, color=YELLOW, weight="BOLD")
        entete.next_to(titre, DOWN, buff=0.3)

        tableau = _tableau(
            ["Critère", "Alcènes", "Benzène"],
            [
                ["Électrons π", "localisés (C=C)", "délocalisés (cycle)"],
                ["Décolore eau de brome", "OUI", "NON"],
                ["Réagit Br2 + FeBr3", "addition rapide", "substitution"],
                ["Réaction privilégiée", "ADDITION", "SUBSTITUTION"],
                ["Dégagement gazeux", "aucun (addition)", "HBr (substitution)"],
            ],
            col_widths=[3.4, 3.2, 3.4],
            row_height=0.48,
            font_size=16,
        )
        tableau.next_to(entete, DOWN, buff=0.3)
        groupe_tab = VGroup(entete, tableau)
        _fit(groupe_tab, titre.get_bottom()[1] - 0.3)

        with self.voiceover(
            text=(
                "Chez les alcènes, les électrons pi sont localisés sur "
                "une double liaison précise ; chez le benzène, ils sont "
                "délocalisés sur tout le cycle. Un alcène décolore l'eau "
                "de brome, pas le benzène. Face au dibrome en présence de "
                "tribromure de fer, l'alcène effectue une addition "
                "rapide, sans catalyseur nécessaire, tandis que le "
                "benzène effectue une substitution, qui exige un "
                "catalyseur. La réaction privilégiée est donc l'addition "
                "pour l'alcène, la substitution pour le benzène — et "
                "cette dernière s'accompagne d'un dégagement de bromure "
                "d'hydrogène gazeux, absent d'une simple addition."
            )
        ) as tracker:
            self.play(FadeIn(entete))
            self.play(FadeIn(tableau))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(groupe_tab))

        # --- Exemple traité : property_box, le test caractéristique ---------------
        test = property_box(
            Text(
                _wrap(
                    "Test caractéristique : un alcène décolore l'eau de "
                    "brome (addition), tandis que le benzène ne la "
                    "décolore PAS dans les conditions usuelles — c'est un "
                    "moyen simple de les distinguer expérimentalement.",
                    width=48,
                ),
                font_size=24,
            ),
        )
        test.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Retenons ce test caractéristique, très utile au "
                "laboratoire : un alcène décolore l'eau de brome, par "
                "addition, tandis que le benzène ne la décolore pas dans "
                "les conditions usuelles. C'est un moyen simple et "
                "rapide de distinguer les deux familles de composés."
            )
        ) as tracker:
            self.play(FadeIn(test))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(test))

        # --- Pièges à éviter : additions en conditions drastiques ------------------
        entete2 = Text("Attention : additions en conditions DRASTIQUES", font_size=21, color=YELLOW, weight="BOLD")
        entete2.next_to(titre, DOWN, buff=0.35)

        drastiques = VGroup(
            MathTex(r"C_6H_6 + 3H_2 \xrightarrow[150^{\circ}C]{Ni/Pt} C_6H_{12}", font_size=26, color=WHITE),
            MathTex(r"C_6H_6 + 3Cl_2 \xrightarrow{UV} C_6H_6Cl_6", font_size=26, color=WHITE),
        ).arrange(DOWN, buff=0.4)
        drastiques.next_to(entete2, DOWN, buff=0.4)

        precision = Text(
            _wrap(
                "Dans ces conditions extrêmes (catalyseur métallique + "
                "température élevée, ou rayonnement UV), une addition "
                "devient possible : le caractère aromatique du cycle est "
                "alors détruit.",
                width=48,
            ),
            font_size=20,
            color=RED,
        )
        precision.next_to(drastiques, DOWN, buff=0.35)

        groupe2 = VGroup(entete2, drastiques, precision)
        _fit(groupe2, titre.get_bottom()[1] - 0.35)

        with self.voiceover(
            text=(
                "Attention cependant à ne pas généraliser trop vite : "
                "dans des conditions dites drastiques, une addition sur "
                "le benzène devient possible. Une hydrogénation, en "
                "présence de nickel ou de platine et vers cent "
                "cinquante degrés, transforme le benzène en cyclohexane. "
                "Une chloration sous rayonnement ultraviolet donne, elle, "
                "de l'hexachlorocyclohexane. Dans ces deux cas "
                "particuliers, le caractère aromatique du cycle est "
                "détruit : ce ne sont pas des exceptions à la règle "
                "générale de substitution, mais des conditions "
                "expérimentales volontairement extrêmes, à ne jamais "
                "confondre avec le comportement usuel du benzène."
            )
        ) as tracker:
            self.play(FadeIn(entete2))
            self.play(Write(drastiques))
            self.play(FadeIn(precision))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(groupe2), FadeOut(titre))
