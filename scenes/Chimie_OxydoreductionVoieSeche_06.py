"""
scenes/Chimie_OxydoreductionVoieSeche_06.py — Chapitre 13 « Oxydoréduction
par voie sèche » (1ereC, Chimie), scène 06.

§ 3 (fin) + § 4 (début). Contre-exemple : CaCO₃ → CaO + CO₂ (aucun n.o. ne
varie, ce n'est pas une oxydoréduction). Tableau des combustions de
métaux dans O₂ (Mg, Al, Fe → Fe₃O₄, Cu → CuO) avec équations et
observations. Remarque : n.o. moyen du fer dans Fe₃O₄ (+8/3).
Source : 1ereC/Chimie.pdf, chapitre 13, pages 129-130.
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
from shapes.boxes import property_box, scene_title, warning_box


def _wrap(text: str, width: int = 56) -> str:
    return "\n".join(textwrap.fill(line, width=width) for line in text.split("\n"))


def _fit(mobject, top_y):
    bas_visible = -config.frame_height / 2 + 0.25
    hauteur_dispo = top_y - bas_visible
    if mobject.height > hauteur_dispo:
        mobject.scale(hauteur_dispo / mobject.height, about_point=mobject.get_top())
    return mobject


def _tableau_combustions():
    """Tableau des combustions de métaux dans O₂, construit avec des
    primitives Manim de base (Line, Text, MathTex, VGroup)."""
    lignes = [
        (r"2\,Mg + O_2 \rightarrow 2\,MgO", "flamme blanche éblouissante"),
        (r"4\,Al + 3\,O_2 \rightarrow 2\,Al_2O_3", "flamme blanche intense"),
        (r"3\,Fe + 2\,O_2 \rightarrow Fe_3O_4", "combustion vive, étincelles"),
        (r"2\,Cu + O_2 \rightarrow 2\,CuO", "surface qui noircit (à chaud)"),
    ]

    col1 = VGroup(*[MathTex(t[0], font_size=22, color=WHITE) for t in lignes])
    col1.arrange(DOWN, buff=0.4, aligned_edge=LEFT)
    col2 = VGroup(*[Text(t[1], font_size=18, color=WHITE) for t in lignes])
    for a, b in zip(col1, col2):
        b.next_to(a, RIGHT, buff=0.6)

    ligne_sep = Line(
        [col1.get_left()[0] - 0.15, col1.get_top()[1] + 0.15, 0],
        [col2.get_right()[0] + 0.15, col1.get_bottom()[1] - 0.15, 0],
        color=WHITE, stroke_width=0,
    )

    return VGroup(col1, col2, ligne_sep)


class ContreExempleCombustionMetaux(NotionScene):
    def construct(self):
        titre = scene_title("13.3-4 Contre-exemple et combustion des métaux")
        titre.scale(0.44)
        titre.to_edge(UP)

        # --- Énoncé : le contre-exemple CaCO3 -----------------------------
        equation_cc = MathTex(r"CaCO_3 \longrightarrow CaO + CO_2", font_size=30)
        question = Text("Est-ce une oxydoréduction ?", font_size=22, color=YELLOW)
        groupe_q = VGroup(equation_cc, question).arrange(DOWN, buff=0.4)
        groupe_q.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Attention : toute réaction chimique n'est pas une "
                "oxydoréduction. Prenons la décomposition thermique du "
                "carbonate de calcium : CaCO trois donne CaO plus CO deux. "
                "Est-ce une oxydoréduction ? Calculons les nombres "
                "d'oxydation pour trancher."
            )
        ) as tracker:
            self.play(Write(titre))
            self.play(FadeIn(groupe_q))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(groupe_q))

        # --- Raisonnement : calcul des n.o. avant/après --------------------
        ligne_ca = Text("Ca : +II (dans CaCO₃) → +II (dans CaO)   AUCUN CHANGEMENT", font_size=19)
        ligne_c = Text("C : +IV (dans CaCO₃) → +IV (dans CO₂)   AUCUN CHANGEMENT", font_size=19)
        ligne_o = Text("O : −II (dans CaCO₃) → −II (dans CaO et CO₂)   AUCUN CHANGEMENT", font_size=19)
        conclusion_cc = Text("Aucun n.o. ne varie : ce N'EST PAS une oxydoréduction !", font_size=21, color=ORANGE, weight="BOLD")
        contenu_cc = VGroup(ligne_ca, ligne_c, ligne_o, conclusion_cc).arrange(DOWN, buff=0.3)
        contenu_cc.next_to(titre, DOWN, buff=0.5)
        _fit(contenu_cc, titre.get_bottom()[1] - 0.15)

        with self.voiceover(
            text=(
                "Le calcium reste au n.o. plus deux, avant comme après. Le "
                "carbone reste au n.o. plus quatre. L'oxygène reste au "
                "n.o. moins deux. Aucun nombre d'oxydation ne varie : "
                "cette réaction n'est donc PAS une oxydoréduction, malgré "
                "les apparences d'une réaction par voie sèche à haute "
                "température. C'est simplement une décomposition "
                "thermique."
            )
        ) as tracker:
            self.play(FadeIn(contenu_cc))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(contenu_cc))

        # --- Exemple traité : tableau des combustions de métaux ------------
        entete_tab = Text("Combustions de métaux dans le dioxygène", font_size=22, color=YELLOW, weight="BOLD")
        entete_tab.next_to(titre, DOWN, buff=0.35)

        tableau = _tableau_combustions()
        tableau.next_to(entete_tab, DOWN, buff=0.4)
        groupe_tab = VGroup(entete_tab, tableau)
        _fit(groupe_tab, titre.get_bottom()[1] - 0.1)
        groupe_tab.next_to(titre, DOWN, buff=0.3)

        with self.voiceover(
            text=(
                "À l'inverse, la combustion des métaux dans le dioxygène "
                "est bien une oxydoréduction : le magnésium donne une "
                "flamme blanche éblouissante en formant MgO, l'aluminium "
                "une flamme blanche intense en formant l'alumine, "
                "Al deux O trois, le fer brûle vivement en projetant des "
                "étincelles pour former l'oxyde magnétique Fe trois O "
                "quatre, et le cuivre chauffé à l'air voit sa surface "
                "noircir en formant l'oxyde de cuivre, CuO."
            )
        ) as tracker:
            self.play(FadeIn(entete_tab))
            self.play(FadeIn(tableau))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(groupe_tab))

        # --- À retenir : critère de reconnaissance --------------------------
        retenir = property_box(
            Text(
                _wrap(
                    "Le seul critère fiable pour reconnaître une "
                    "oxydoréduction est la VARIATION D'AU MOINS UN "
                    "NOMBRE D'OXYDATION entre les réactifs et les "
                    "produits — pas l'aspect spectaculaire (chaleur, "
                    "flamme) de la réaction.",
                    width=46,
                ),
                font_size=22,
            ),
        )
        retenir.next_to(titre, DOWN, buff=0.45)

        with self.voiceover(
            text=(
                "Retenons l'essentiel : le seul critère fiable pour "
                "reconnaître une oxydoréduction est la variation d'au "
                "moins un nombre d'oxydation entre les réactifs et les "
                "produits, et non l'aspect spectaculaire, chaleur ou "
                "flamme, de la réaction."
            )
        ) as tracker:
            self.play(FadeIn(retenir))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(retenir))

        # --- Piège à éviter : n.o. moyen fractionnaire de Fe3O4 --------------
        piege_contenu = VGroup(
            MathTex(r"n.o._{\text{moyen}}(Fe\ \text{dans}\ Fe_3O_4) = +\dfrac{8}{3}", font_size=26),
            Text(
                _wrap(
                    "Ce n.o. fractionnaire n'est qu'une MOYENNE : Fe₃O₄ "
                    "contient en réalité 1 atome de fer +III et 2 atomes "
                    "de fer +II (ou l'inverse selon la formule retenue), "
                    "jamais un fer « +8/3 » isolé.",
                    width=46,
                ),
                font_size=20,
            ),
        ).arrange(DOWN, buff=0.35)
        piege = warning_box(piege_contenu, box_width=12.2)
        piege.next_to(titre, DOWN, buff=0.45)
        _fit(piege, titre.get_bottom()[1] - 0.15)

        with self.voiceover(
            text=(
                "Remarque importante à propos de Fe trois O quatre : le "
                "calcul direct donne un n.o. moyen du fer de plus huit "
                "tiers, une valeur fractionnaire ! Ce n'est qu'une "
                "moyenne : Fe trois O quatre contient en réalité des "
                "atomes de fer à des n.o. différents, du fer plus deux et "
                "du fer plus trois, jamais un fer isolé à plus huit "
                "tiers. Ne soyez donc pas surpris par un n.o. non entier : "
                "c'est le signe d'un mélange de degrés d'oxydation."
            )
        ) as tracker:
            self.play(FadeIn(piege))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(piege), FadeOut(titre))
