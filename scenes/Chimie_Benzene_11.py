"""
scenes/Chimie_Benzene_11.py — Chapitre 4 (1ereC, Chimie), scène 11.

§ Méthodes, pièges à éviter et essentiel : method_box × 3 (bilan de
matière stœchiométrique, déterminer une formule brute par analyse
élémentaire, distinguer benzène/alcène par le test à l'eau de brome —
protocole avec conclusion après observation). warning_box × 4 (pièges
classiques : décoloration eau de brome / addition sans conditions
particulières ; conditions de réaction catalyseur/température ; second
produit de nitration = H2O et non HNO2, second produit d'halogénation =
HX ; équilibrage correct de la combustion). Masses molaires utiles.
essentiel_box récapitulatif final du chapitre.
Source : synthèse du chapitre 4, 1ereC/Chimie.pdf, pages 35-44.
"""

import textwrap

from manim import (
    DOWN,
    LEFT,
    RIGHT,
    UP,
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
from shapes.boxes import essentiel_box, method_box, scene_title, warning_box


def _wrap(text: str, width: int = 56) -> str:
    return "\n".join(textwrap.fill(line, width=width) for line in text.split("\n"))


def _fit(mobject, top_y):
    bas_visible = -config.frame_height / 2 + 0.25
    hauteur_dispo = top_y - bas_visible
    if mobject.height > hauteur_dispo:
        mobject.scale(hauteur_dispo / mobject.height, about_point=mobject.get_top())
    return mobject


def _bullets(items, font_size=22, color=WHITE, width=52):
    lines = VGroup(
        *[Text(f"• {_wrap(it, width=width)}", font_size=font_size, color=color) for it in items]
    )
    lines.arrange(DOWN, aligned_edge=LEFT, buff=0.22)
    return lines


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


class MethodesPiegesEssentielBenzene(NotionScene):
    def construct(self):
        titre = scene_title("11. Méthodes, pièges et essentiel")
        titre.scale(0.55)
        titre.to_edge(UP)

        # --- Énoncé --------------------------------------------------------------
        enonce = Text(
            _wrap(
                "Pour clore ce chapitre, rassemblons les méthodes à "
                "maîtriser, les pièges classiques à éviter, et "
                "l'essentiel à retenir sur le benzène.",
                width=52,
            ),
            font_size=25,
            color=WHITE,
        )
        enonce.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Pour clore ce chapitre, rassemblons les méthodes à "
                "maîtriser, les pièges classiques à éviter, et "
                "l'essentiel à retenir sur le benzène."
            )
        ) as tracker:
            self.play(Write(titre))
            self.play(FadeIn(enonce))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(enonce))

        # --- Animation du raisonnement / exemple traité : 3 method_box -----------
        methode1 = method_box(
            Text(
                _wrap(
                    "Méthode — Bilan de matière stœchiométrique : 1) "
                    "calculer n = m/M du réactif limitant ; 2) utiliser "
                    "les coefficients de l'équation pour trouver n du "
                    "produit ; 3) calculer m = n × M du produit.",
                    width=46,
                ),
                font_size=22,
            ),
        )
        methode1.next_to(titre, DOWN, buff=0.45)

        with self.voiceover(
            text=(
                "Première méthode à maîtriser : le bilan de matière "
                "stœchiométrique. On calcule d'abord la quantité de "
                "matière du réactif, avec n égale m sur M. On utilise "
                "ensuite les coefficients de l'équation, comme le un "
                "pour un rencontré pour la bromation, pour trouver la "
                "quantité de matière du produit. On calcule enfin sa "
                "masse, avec m égale n fois M."
            )
        ) as tracker:
            self.play(FadeIn(methode1))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(methode1))

        methode2 = method_box(
            Text(
                _wrap(
                    "Méthode — Déterminer une formule brute par analyse "
                    "élémentaire : identifier les éléments présents, "
                    "calculer leurs pourcentages massiques, en déduire "
                    "le rapport molaire entre atomes, puis ajuster avec "
                    "la masse molaire connue.",
                    width=46,
                ),
                font_size=22,
            ),
        )
        methode2.next_to(titre, DOWN, buff=0.45)

        with self.voiceover(
            text=(
                "Deuxième méthode : déterminer une formule brute par "
                "analyse élémentaire. On identifie d'abord les éléments "
                "présents dans le composé, on calcule leurs pourcentages "
                "massiques, on en déduit le rapport molaire entre les "
                "atomes, puis on ajuste ce rapport à l'aide de la masse "
                "molaire connue du composé — c'est ainsi qu'a été établie "
                "la formule C six H six du benzène."
            )
        ) as tracker:
            self.play(FadeIn(methode2))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(methode2))

        methode3 = method_box(
            Text(
                _wrap(
                    "Méthode — Distinguer benzène et alcène par le test à "
                    "l'eau de brome : verser le composé dans de l'eau de "
                    "brome, sans catalyseur ni chauffage. Observer : "
                    "décoloration → alcène (addition) ; pas de "
                    "décoloration → benzène (pas de réaction).",
                    width=46,
                ),
                font_size=21,
            ),
        )
        methode3.next_to(titre, DOWN, buff=0.45)
        _fit(methode3, titre.get_bottom()[1] - 0.4)

        with self.voiceover(
            text=(
                "Troisième méthode, un protocole expérimental à bien "
                "connaître : pour distinguer un benzène d'un alcène par "
                "le test à l'eau de brome, on verse simplement le "
                "composé à tester dans de l'eau de brome, sans "
                "catalyseur ni chauffage. On observe ensuite : si l'eau "
                "de brome se décolore, il s'agit d'un alcène, qui a "
                "additionné le dibrome ; si elle reste inchangée, il "
                "s'agit de benzène, qui n'a subi aucune réaction dans ces "
                "conditions usuelles."
            )
        ) as tracker:
            self.play(FadeIn(methode3))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(methode3))

        # --- Pièges à éviter : 4 warning_box ---------------------------------------
        piege1 = warning_box(
            Text(
                _wrap(
                    "Piège 1 : ne jamais dire que le benzène décolore "
                    "l'eau de brome, ni qu'il additionne Br2 sans "
                    "préciser des conditions particulières (catalyseur, "
                    "chauffage, UV) — dans les conditions usuelles, "
                    "aucune réaction n'a lieu.",
                    width=46,
                ),
                font_size=20,
            ),
        )
        piege1.next_to(titre, DOWN, buff=0.4)
        _fit(piege1, titre.get_bottom()[1] - 0.35)

        with self.voiceover(
            text=(
                "Premier piège à éviter : ne jamais affirmer que le "
                "benzène décolore l'eau de brome, ni qu'il additionne le "
                "dibrome, sans préciser des conditions particulières et "
                "extrêmes, comme un catalyseur, un fort chauffage ou un "
                "rayonnement ultraviolet. Dans les conditions usuelles, "
                "il ne se passe strictement rien."
            )
        ) as tracker:
            self.play(FadeIn(piege1))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(piege1))

        piege2 = warning_box(
            Text(
                _wrap(
                    "Piège 2 : ne pas oublier les conditions de réaction "
                    "(catalyseur ET température) dans une équation de "
                    "substitution — FeBr3 pour la bromation, FeCl3 pour "
                    "la chloration, H2SO4 et 50-60 °C pour la nitration.",
                    width=46,
                ),
                font_size=20,
            ),
        )
        piege2.next_to(titre, DOWN, buff=0.4)
        _fit(piege2, titre.get_bottom()[1] - 0.35)

        with self.voiceover(
            text=(
                "Deuxième piège : ne pas oublier les conditions de "
                "réaction, catalyseur et température, au-dessus de la "
                "flèche d'une équation de substitution — tribromure de "
                "fer pour la bromation, trichlorure de fer pour la "
                "chloration, acide sulfurique et une température de "
                "cinquante à soixante degrés pour la nitration."
            )
        ) as tracker:
            self.play(FadeIn(piege2))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(piege2))

        piege3 = warning_box(
            Text(
                _wrap(
                    "Piège 3 : le second produit de la nitration est "
                    "H2O, pas HNO2. Le second produit d'une halogénation "
                    "est HX (HBr, HCl), pas X2 ni H2.",
                    width=46,
                ),
                font_size=21,
            ),
        )
        piege3.next_to(titre, DOWN, buff=0.4)
        _fit(piege3, titre.get_bottom()[1] - 0.35)

        with self.voiceover(
            text=(
                "Troisième piège, fréquent dans les équations bilans : "
                "le second produit de la nitration est l'eau, H deux O, "
                "et non de l'acide nitreux H N O deux. De même, le "
                "second produit d'une halogénation est un halogénure "
                "d'hydrogène, H X, comme H Br ou H Cl — jamais le "
                "dihalogène ou le dihydrogène."
            )
        ) as tracker:
            self.play(FadeIn(piege3))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(piege3))

        piege4 = warning_box(
            MathTex(
                r"2\,C_6H_6 + 15\,O_2 \rightarrow 12\,CO_2 + 6\,H_2O",
                font_size=28,
            ),
        )
        piege4.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Quatrième et dernier piège : bien équilibrer l'équation "
                "de la combustion complète du benzène. Il faut deux "
                "molécules de benzène pour quinze molécules de "
                "dioxygène, donnant douze molécules de dioxyde de "
                "carbone et six molécules d'eau — un équilibrage à "
                "vérifier systématiquement, atome par atome."
            )
        ) as tracker:
            self.play(FadeIn(piege4))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(piege4))

        # --- Masses molaires utiles -------------------------------------------------
        entete_mm = Text("Masses molaires utiles", font_size=23, color=YELLOW, weight="BOLD")
        entete_mm.next_to(titre, DOWN, buff=0.35)

        tableau_mm = _tableau(
            ["Composé", "M (g/mol)"],
            [
                ["C6H6 (benzène)", "78"],
                ["C6H5Br (bromobenzène)", "157"],
                ["C6H5NO2 (nitrobenzène)", "123"],
                ["C6H12 (cyclohexane)", "84"],
            ],
            col_widths=[4.6, 2.6],
            row_height=0.45,
            font_size=18,
        )
        tableau_mm.next_to(entete_mm, DOWN, buff=0.3)
        groupe_mm = VGroup(entete_mm, tableau_mm)
        _fit(groupe_mm, titre.get_bottom()[1] - 0.35)

        with self.voiceover(
            text=(
                "Gardons enfin sous la main ces masses molaires utiles : "
                "soixante-dix-huit grammes par mole pour le benzène, "
                "cent cinquante-sept pour le bromobenzène, cent "
                "vingt-trois pour le nitrobenzène, et quatre-vingt-quatre "
                "pour le cyclohexane."
            )
        ) as tracker:
            self.play(FadeIn(entete_mm))
            self.play(FadeIn(tableau_mm))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(groupe_mm))

        # --- À retenir : essentiel_box récapitulatif final --------------------------
        essentiel = essentiel_box(
            Text(
                _wrap(
                    "Le benzène C6H6 est un hydrocarbure aromatique "
                    "plan et hexagonal, dont la vraie structure est "
                    "l'hybride de résonance (nuage π délocalisé), pas "
                    "une simple alternance de liaisons de Kekulé. Ce "
                    "nuage privilégie les réactions de substitution "
                    "électrophile (halogénation, nitration) sur "
                    "l'addition : le benzène ne décolore pas l'eau de "
                    "brome. Précieux industriellement (styrène, phénol, "
                    "aniline, nylon…), il reste toxique et doit être "
                    "manipulé avec les précautions adaptées.",
                    width=50,
                ),
                font_size=22,
            ),
        )
        essentiel.next_to(titre, DOWN, buff=0.5)
        _fit(essentiel, titre.get_bottom()[1] - 0.4)

        with self.voiceover(
            text=(
                "Retenons l'essentiel de ce chapitre. Le benzène, de "
                "formule C six H six, est un hydrocarbure aromatique "
                "plan et hexagonal, dont la vraie structure est "
                "l'hybride de résonance, avec son nuage d'électrons pi "
                "délocalisés — et non une simple alternance de liaisons "
                "de Kekulé. Ce nuage, riche en électrons, privilégie les "
                "réactions de substitution électrophile, comme "
                "l'halogénation ou la nitration, plutôt que l'addition : "
                "le benzène ne décolore pas l'eau de brome. Précieux "
                "industriellement — à l'origine du styrène, du phénol, "
                "de l'aniline ou du nylon — il n'en reste pas moins "
                "toxique, et doit toujours être manipulé avec les "
                "précautions de sécurité adaptées."
            )
        ) as tracker:
            self.play(FadeIn(essentiel))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(essentiel), FadeOut(titre))
