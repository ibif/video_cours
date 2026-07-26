"""
scenes/Chimie_Benzene_05.py — Chapitre 4 (1ereC, Chimie), scène 05.

§ Électronégativité et liaisons dans le benzène : definition_box
électronégativité (échelle de Pauling, C = 2,55 vs H = 2,20), liaison C–H
faiblement polarisée, carbone trigonal plus électronégatif que
tétragonal, nuage π = région riche en électrons attirant les
électrophiles. Tableau récapitulatif des représentations (Kekulé /
hybride / formule brute) + tableau des caractéristiques géométriques
(angles 120°, C–C 140 pm, C–H 108 pm). Exemple résolu 1 : quantité de
matière dans 44 mL de benzène liquide.
Source : 1ereC/Chimie.pdf, chapitre 4, pages 38-39.
"""

import textwrap

from manim import (
    DOWN,
    LEFT,
    RIGHT,
    UP,
    ORIGIN,
    WHITE,
    YELLOW,
    RED,
    BLUE,
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
from shapes.boxes import definition_box, example_box, scene_title


def _wrap(text: str, width: int = 56) -> str:
    return "\n".join(textwrap.fill(line, width=width) for line in text.split("\n"))


def _fit(mobject, top_y):
    bas_visible = -config.frame_height / 2 + 0.25
    hauteur_dispo = top_y - bas_visible
    if mobject.height > hauteur_dispo:
        mobject.scale(hauteur_dispo / mobject.height, about_point=mobject.get_top())
    return mobject


def _tableau(entetes, lignes, col_width=2.6, row_height=0.5, font_size=19):
    """Tableau simple construit avec Line + Text (cohérent avec le style
    déjà utilisé dans Chimie_AlcenesAlcynes_02.py) — pas de Table Manim."""
    n_cols = len(entetes)
    n_rows = 1 + len(lignes)

    cells = VGroup()
    for j, entete in enumerate(entetes):
        c = Text(entete, font_size=font_size, color=YELLOW, weight="BOLD")
        c.move_to([(j - (n_cols - 1) / 2) * col_width, (n_rows - 1) / 2 * row_height, 0])
        cells.add(c)

    for i, ligne in enumerate(lignes):
        for j, val in enumerate(ligne):
            c = Text(val, font_size=font_size, color=WHITE)
            c.move_to([(j - (n_cols - 1) / 2) * col_width, ((n_rows - 1) / 2 - (i + 1)) * row_height, 0])
            cells.add(c)

    largeur_totale = n_cols * col_width
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
                [(-n_cols / 2 + k) * col_width, hauteur_totale / 2, 0],
                [(-n_cols / 2 + k) * col_width, -hauteur_totale / 2, 0],
                color=WHITE,
                stroke_width=1,
            )
            for k in range(n_cols + 1)
        ]
    )

    return VGroup(contour, lignes_h, lignes_v, cells)


class ElectronegativiteLiaisonsBenzene(NotionScene):
    def construct(self):
        titre = scene_title("5. Électronégativité et liaisons dans le benzène")
        titre.scale(0.42)
        titre.to_edge(UP)

        # --- Énoncé : definition_box électronégativité ---------------------------
        definition = definition_box(
            Text(
                _wrap(
                    "L'électronégativité mesure la capacité d'un atome à "
                    "attirer vers lui les électrons d'une liaison "
                    "covalente. Sur l'échelle de Pauling : carbone = "
                    "2,55 ; hydrogène = 2,20.",
                    width=48,
                ),
                font_size=25,
            ),
        )
        definition.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "L'électronégativité mesure la capacité d'un atome à "
                "attirer vers lui les électrons d'une liaison covalente. "
                "Sur l'échelle de Pauling, le carbone vaut deux "
                "virgule cinquante-cinq, et l'hydrogène deux virgule "
                "vingt."
            )
        ) as tracker:
            self.play(Write(titre))
            self.play(FadeIn(definition))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(definition))

        # --- Animation du raisonnement : polarisation C-H et nuage π riche -----
        entete = Text("Une liaison C–H peu polarisée, un nuage π riche", font_size=22, color=YELLOW, weight="BOLD")
        entete.next_to(titre, DOWN, buff=0.4)

        ch = MathTex(r"\overset{\delta^-}{C} - \overset{\delta^+}{H}", font_size=44, color=WHITE)
        ch_note = Text("polarisation très faible (2,55 proche de 2,20)", font_size=18, color=WHITE)
        bloc_ch = VGroup(ch, ch_note).arrange(DOWN, buff=0.25)

        note2 = Text(
            _wrap(
                "Un carbone trigonal (comme dans le benzène) est "
                "légèrement plus électronégatif qu'un carbone tétragonal "
                "(comme dans un alcane).",
                width=48,
            ),
            font_size=20,
            color=WHITE,
        )

        note3 = Text(
            "le nuage π : une région riche en électrons,\nqui attire les réactifs électrophiles",
            font_size=20,
            color=RED,
        )

        bloc = VGroup(bloc_ch, note2, note3).arrange(DOWN, buff=0.4)
        bloc.next_to(entete, DOWN, buff=0.4)
        groupe_raisonnement = VGroup(entete, bloc)
        _fit(groupe_raisonnement, titre.get_bottom()[1] - 0.4)

        with self.voiceover(
            text=(
                "Ces valeurs étant proches, la liaison carbone-hydrogène "
                "du benzène est seulement faiblement polarisée. On note "
                "aussi qu'un carbone trigonal, comme ceux du cycle "
                "benzénique, est légèrement plus électronégatif qu'un "
                "carbone tétragonal, comme ceux d'un alcane. Mais surtout, "
                "retenons que le nuage électronique π délocalisé "
                "constitue une région riche en électrons : il attire "
                "naturellement les réactifs électrophiles, c'est-à-dire "
                "pauvres en électrons — c'est cette attirance qui "
                "déclenchera les réactions de substitution étudiées plus "
                "loin."
            )
        ) as tracker:
            self.play(FadeIn(entete))
            self.play(FadeIn(bloc_ch))
            self.play(FadeIn(note2))
            self.play(FadeIn(note3))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(groupe_raisonnement))

        # --- Exemple traité : quantité de matière dans 44 mL de benzène --------
        enonce_ex = Text(
            _wrap(
                "Exemple résolu : quelle quantité de matière de benzène "
                "contient un volume V = 44 mL de benzène liquide, de "
                "masse volumique ρ = 0,88 g/mL et de masse molaire "
                "M = 78 g/mol ?",
                width=50,
            ),
            font_size=23,
            color=WHITE,
        )
        enonce_ex.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Passons à un exemple résolu. Quelle quantité de matière "
                "de benzène contient un volume de quarante-quatre "
                "millilitres de benzène liquide, de masse volumique zéro "
                "virgule quatre-vingt-huit gramme par millilitre, et de "
                "masse molaire soixante-dix-huit grammes par mole ?"
            )
        ) as tracker:
            self.play(FadeIn(enonce_ex))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(enonce_ex))

        etape1 = MathTex(r"m = \rho \times V = 0{,}88 \times 44 = 38{,}7\ g", font_size=30, color=WHITE)
        etape2 = MathTex(r"n = \dfrac{m}{M} = \dfrac{38{,}7}{78} \approx 0{,}50\ mol", font_size=30, color=YELLOW)
        etapes = VGroup(etape1, etape2).arrange(DOWN, buff=0.5)
        etapes.next_to(titre, DOWN, buff=0.6)

        with self.voiceover(
            text=(
                "On calcule d'abord la masse à partir de la masse "
                "volumique et du volume : zéro virgule quatre-vingt-huit "
                "fois quarante-quatre, soit environ trente-huit virgule "
                "sept grammes. On en déduit la quantité de matière en "
                "divisant par la masse molaire : trente-huit virgule "
                "sept divisé par soixante-dix-huit, soit environ zéro "
                "virgule cinquante mole."
            )
        ) as tracker:
            self.play(Write(etape1))
            self.play(Write(etape2))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(etapes))

        # --- À retenir : deux tableaux récapitulatifs ---------------------------
        entete_tab1 = Text("Les représentations du benzène", font_size=22, color=YELLOW, weight="BOLD")
        entete_tab1.next_to(titre, DOWN, buff=0.35)

        tableau1 = _tableau(
            ["Représentation", "Ce qu'elle montre"],
            [
                ["Formule brute", "C6H6"],
                ["Formes de Kekulé", "2 formes mésomères (3 C=C)"],
                ["Hybride de résonance", "hexagone + cercle"],
            ],
            col_width=3.4,
        )
        tableau1.next_to(entete_tab1, DOWN, buff=0.3)
        groupe_tab1 = VGroup(entete_tab1, tableau1)
        _fit(groupe_tab1, titre.get_bottom()[1] - 0.4)

        with self.voiceover(
            text=(
                "Récapitulons maintenant les trois représentations du "
                "benzène rencontrées : la formule brute C six H six, les "
                "deux formes mésomères de Kekulé avec leurs trois doubles "
                "liaisons, et l'hybride de résonance, représenté par un "
                "hexagone portant un cercle."
            )
        ) as tracker:
            self.play(FadeIn(entete_tab1))
            self.play(FadeIn(tableau1))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(groupe_tab1))

        entete_tab2 = Text("Caractéristiques géométriques", font_size=22, color=YELLOW, weight="BOLD")
        entete_tab2.next_to(titre, DOWN, buff=0.35)

        tableau2 = _tableau(
            ["Grandeur", "Valeur"],
            [
                ["Angle de liaison", "120°"],
                ["Longueur C–C", "140 pm"],
                ["Longueur C–H", "108 pm"],
            ],
            col_width=3.4,
        )
        tableau2.next_to(entete_tab2, DOWN, buff=0.3)
        groupe_tab2 = VGroup(entete_tab2, tableau2)
        _fit(groupe_tab2, titre.get_bottom()[1] - 0.4)

        with self.voiceover(
            text=(
                "Et retenons les caractéristiques géométriques de la "
                "molécule : des angles de liaison de cent vingt degrés, "
                "une longueur de liaison carbone-carbone de cent quarante "
                "picomètres, et une longueur de liaison carbone-hydrogène "
                "de cent huit picomètres — une molécule parfaitement "
                "plane et régulière."
            )
        ) as tracker:
            self.play(FadeIn(entete_tab2))
            self.play(FadeIn(tableau2))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(groupe_tab2), FadeOut(titre))
