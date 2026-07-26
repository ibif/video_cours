"""
scenes/Chimie_OxydoreductionVoieSeche_04.py — Chapitre 13 « Oxydoréduction
par voie sèche » (1ereC, Chimie), scène 04.

§ 2 (suite). Exemple résolu 2 : n.o. du manganèse dans KMnO₄, n.o. du
chrome dans Cr₂O₇²⁻. Tableau récapitulatif de n.o. usuels (O₂, H₂O, CO,
CO₂, SO₂, H₂SO₄, CuO, Cu, Fe₂O₃, Al₂O₃, KMnO₄, MnO₂).
Source : 1ereC/Chimie.pdf, chapitre 13, pages 127-128.
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
    FadeIn,
    FadeOut,
    Line,
    MathTex,
    Text,
    VGroup,
    Write,
    config,
)

from shapes.base_scene import NotionScene
from shapes.boxes import example_box, scene_title, warning_box


def _wrap(text: str, width: int = 56) -> str:
    return "\n".join(textwrap.fill(line, width=width) for line in text.split("\n"))


def _fit(mobject, top_y):
    bas_visible = -config.frame_height / 2 + 0.25
    hauteur_dispo = top_y - bas_visible
    if mobject.height > hauteur_dispo:
        mobject.scale(hauteur_dispo / mobject.height, about_point=mobject.get_top())
    return mobject


def _tableau_no_usuels():
    """Tableau récapitulatif des n.o. usuels, construit avec des
    primitives Manim de base (Line, Text, VGroup)."""
    lignes = [
        ("O₂", "O : 0"),
        ("H₂O", "H : +I  O : −II"),
        ("CO", "C : +II  O : −II"),
        ("CO₂", "C : +IV  O : −II"),
        ("SO₂", "S : +IV  O : −II"),
        ("H₂SO₄", "S : +VI"),
        ("CuO", "Cu : +II  O : −II"),
        ("Cu", "Cu : 0"),
        ("Fe₂O₃", "Fe : +III  O : −II"),
        ("Al₂O₃", "Al : +III  O : −II"),
        ("KMnO₄", "Mn : +VII"),
        ("MnO₂", "Mn : +IV  O : −II"),
    ]

    col1 = VGroup(*[Text(t[0], font_size=18, color=YELLOW) for t in lignes])
    col2 = VGroup(*[Text(t[1], font_size=18, color=WHITE) for t in lignes])
    col1.arrange(DOWN, buff=0.18, aligned_edge=LEFT)
    for a, b in zip(col1, col2):
        b.next_to(a, RIGHT, buff=0.6)

    # Deux colonnes de composés côte à côte pour tenir sur l'écran.
    gauche = VGroup(*[VGroup(col1[i], col2[i]) for i in range(6)]).arrange(DOWN, buff=0.22, aligned_edge=LEFT)
    droite = VGroup(*[VGroup(col1[i], col2[i]) for i in range(6, 12)]).arrange(DOWN, buff=0.22, aligned_edge=LEFT)
    droite.next_to(gauche, RIGHT, buff=1.0)

    ligne_sep = Line(
        [gauche.get_right()[0] + 0.5, gauche.get_top()[1] + 0.1, 0],
        [gauche.get_right()[0] + 0.5, gauche.get_bottom()[1] - 0.1, 0],
        color=WHITE, stroke_width=1,
    )

    return VGroup(gauche, droite, ligne_sep)


class ExemplesCalculNoTableau(NotionScene):
    def construct(self):
        titre = scene_title("13.2 Exemples de calcul de n.o. — tableau récapitulatif")
        titre.scale(0.42)
        titre.to_edge(UP)

        # --- Énoncé -------------------------------------------------------------
        intro = Text(
            _wrap(
                "Entraînons-nous sur deux exemples classiques, où l'élément "
                "recherché appartient à un ion polyatomique.",
                width=56,
            ),
            font_size=24, color=WHITE,
        )
        intro.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Entraînons-nous à présent sur deux exemples classiques, "
                "où l'élément recherché appartient cette fois à un ion "
                "polyatomique."
            )
        ) as tracker:
            self.play(Write(titre))
            self.play(FadeIn(intro))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(intro))

        # --- Raisonnement : n.o. du Mn dans KMnO4 --------------------------------
        formule_mn = MathTex(r"KMnO_4", font_size=32)
        e1 = Text("K : +I (métal alcalin)   O : −II × 4", font_size=19)
        e2 = Text("(+1) + n.o.(Mn) + 4 × (−2) = 0", font_size=20)
        e3 = Text("n.o.(Mn) = −1 + 8 = +7", font_size=20)
        r1 = MathTex(r"n.o.(Mn) = +VII", font_size=26, color=ORANGE)
        contenu_mn = VGroup(formule_mn, e1, e2, e3, r1).arrange(DOWN, buff=0.28)
        boite_mn = example_box(contenu_mn, box_width=11.0)
        boite_mn.next_to(titre, DOWN, buff=0.35)
        _fit(boite_mn, titre.get_bottom()[1] - 0.15)

        with self.voiceover(
            text=(
                "Premier exemple : le nombre d'oxydation du manganèse dans "
                "le permanganate de potassium, K-Mn-O-quatre. Le potassium, "
                "métal alcalin, vaut toujours plus un. L'oxygène vaut moins "
                "deux, pour quatre atomes. La molécule est neutre : plus "
                "un, plus n point o de Mn, plus quatre fois moins deux, "
                "égale zéro. On isole : n point o de Mn égale plus sept. "
                "Le manganèse est donc au degré d'oxydation plus sept "
                "romain dans le permanganate."
            )
        ) as tracker:
            self.play(FadeIn(boite_mn))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(boite_mn))

        # --- Exemple traité : n.o. du Cr dans Cr2O7 2- ---------------------------
        formule_cr = MathTex(r"Cr_2O_7^{\,2-}", font_size=32)
        f1 = Text("Ion polyatomique : somme des n.o. = charge = −2", font_size=19)
        f2 = Text("2 × n.o.(Cr) + 7 × (−2) = −2", font_size=20)
        f3 = Text("2 × n.o.(Cr) = −2 + 14 = 12  →  n.o.(Cr) = +6", font_size=20)
        r2 = MathTex(r"n.o.(Cr) = +VI", font_size=26, color=ORANGE)
        contenu_cr = VGroup(formule_cr, f1, f2, f3, r2).arrange(DOWN, buff=0.28)
        boite_cr = example_box(contenu_cr, box_width=11.6)
        boite_cr.next_to(titre, DOWN, buff=0.35)
        _fit(boite_cr, titre.get_bottom()[1] - 0.15)

        with self.voiceover(
            text=(
                "Deuxième exemple, avec un ion polyatomique cette fois : "
                "le nombre d'oxydation du chrome dans l'ion dichromate, "
                "Cr-deux-O-sept deux moins. La somme des n.o. égale ici la "
                "charge de l'ion, soit moins deux : deux fois n point o de "
                "Cr, plus sept fois moins deux, égale moins deux. On "
                "résout : deux fois n point o de Cr égale douze, donc n "
                "point o de Cr égale plus six romain."
            )
        ) as tracker:
            self.play(FadeIn(boite_cr))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(boite_cr))

        # --- À retenir : tableau récapitulatif ------------------------------------
        entete_tab = Text("Tableau récapitulatif de n.o. usuels", font_size=22, color=YELLOW, weight="BOLD")
        entete_tab.next_to(titre, DOWN, buff=0.35)

        tableau = _tableau_no_usuels()
        tableau.next_to(entete_tab, DOWN, buff=0.4)
        groupe_tab = VGroup(entete_tab, tableau)
        _fit(groupe_tab, titre.get_bottom()[1] - 0.15)
        groupe_tab.next_to(titre, DOWN, buff=0.25)

        with self.voiceover(
            text=(
                "Voici un tableau récapitulatif de nombres d'oxydation "
                "usuels, à connaître pour la suite du chapitre : le "
                "dioxygène et le cuivre métal ont un n.o. de zéro ; l'eau, "
                "le monoxyde et le dioxyde de carbone, le dioxyde de "
                "soufre et l'acide sulfurique ; l'oxyde de cuivre, l'oxyde "
                "de fer trois, l'oxyde d'aluminium ; et enfin le "
                "permanganate et le dioxyde de manganèse. Ces valeurs "
                "reviendront très souvent dans les exercices."
            )
        ) as tracker:
            self.play(FadeIn(entete_tab))
            self.play(FadeIn(tableau))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(groupe_tab))

        # --- Piège à éviter ---------------------------------------------------------
        piege = warning_box(
            Text(
                _wrap(
                    "Pour un ion polyatomique, la somme des n.o. est égale "
                    "à la CHARGE DE L'ION, PAS À ZÉRO. Oublier ce point est "
                    "une erreur fréquente (ex : pour Cr₂O₇²⁻, la somme "
                    "vaut −2, pas 0).",
                    width=48,
                ),
                font_size=21,
            ),
        )
        piege.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Attention à un piège très fréquent : pour un ion "
                "polyatomique, la somme des nombres d'oxydation est égale "
                "à la charge de l'ion, et non à zéro. Oublier ce point est "
                "l'erreur la plus courante : pour l'ion dichromate, la "
                "somme vaut moins deux, pas zéro."
            )
        ) as tracker:
            self.play(FadeIn(piege))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(piege), FadeOut(titre))
