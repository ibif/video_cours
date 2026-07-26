"""
scenes/Chimie_GeneralitesComposesOrganiques_07.py — Chapitre 1 (1ereC, Chimie), scène 07.

Exemple résolu 2 (glucose : détermination complète de la formule brute
C6H12O6), remarque importante ((CH2O)n, motif le plus simple), et démarche
récapitulative (tableau des 5 étapes). Source : 1ereC/Chimie.pdf, page 8.
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


class ExempleGlucoseEtDemarche(NotionScene):
    def construct(self):
        titre = scene_title("Exemple résolu — Formule brute du glucose")
        titre.scale(0.55)
        titre.to_edge(UP)

        # --- Énoncé : les données de l'analyse du glucose -----------------------
        enonce = Text(
            _wrap(
                "L'analyse élémentaire du glucose, sucre présent dans de "
                "nombreux fruits tropicaux, donne : %C = 40,0 ; %H = 6,7 ; "
                "%O = 53,3. Sa masse molaire vaut M = 180 g/mol. "
                "Déterminons sa formule brute CₓHᵧOᵤ.",
                width=54,
            ),
            font_size=23,
            color=WHITE,
        )
        enonce.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Prenons un exemple complet. L'analyse élémentaire du "
                "glucose, un sucre présent dans de nombreux fruits "
                "tropicaux, donne quarante pour cent de carbone, six "
                "virgule sept pour cent d'hydrogène, cinquante-trois "
                "virgule trois pour cent d'oxygène. Sa masse molaire vaut "
                "cent quatre-vingts grammes par mole. Déterminons sa "
                "formule brute."
            )
        ) as tracker:
            self.play(Write(titre))
            self.play(FadeIn(enonce))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(enonce))

        # --- Animation du raisonnement : application de la relation ------------
        exemple = example_box(
            VGroup(
                MathTex(r"\dfrac{M}{100} = \dfrac{180}{100} = 1{,}8", font_size=28),
                MathTex(r"x = \dfrac{1{,}8 \times 40{,}0}{12} = 6", font_size=28),
                MathTex(r"y = 1{,}8 \times 6{,}7 = 12", font_size=28),
                MathTex(r"z = \dfrac{1{,}8 \times 53{,}3}{16} = 6", font_size=28),
            ).arrange(DOWN, buff=0.3),
            box_width=10.0,
        )
        exemple.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Appliquons la relation fondamentale, avec M sur cent qui "
                "vaut ici cent quatre-vingts sur cent, soit un virgule "
                "huit. On trouve x égale un virgule huit fois quarante sur "
                "douze, soit six. On trouve y égale un virgule huit fois "
                "six virgule sept, soit douze. On trouve z égale un "
                "virgule huit fois cinquante-trois virgule trois sur "
                "seize, soit six."
            )
        ) as tracker:
            self.play(FadeIn(exemple))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(exemple))

        # --- Exemple traité : conclusion, formule brute du glucose -------------
        conclusion = example_box(
            MathTex(r"\text{La formule brute du glucose est } C_6H_{12}O_6", font_size=30),
            box_width=10.0,
        )
        conclusion.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text="La formule brute du glucose est donc C six H douze O six."
        ) as tracker:
            self.play(FadeIn(conclusion))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(conclusion))

        # --- Piège à éviter : remarque importante sur (CH2O)n -------------------
        remarque = warning_box(
            Text(
                _wrap(
                    "Les pourcentages massiques seuls ne donnent que la "
                    "formule la plus simple, le « motif ». Tous les "
                    "composés de formule (CH₂O)ₙ — CH₂O, C₂H₄O₂, C₆H₁₂O₆… "
                    "— conduisent aux mêmes pourcentages. La connaissance "
                    "de la masse molaire est indispensable pour fixer la "
                    "formule brute.",
                    width=48,
                ),
                font_size=23,
            ),
        )
        remarque.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Remarque importante : les pourcentages massiques seuls ne "
                "donnent que la formule la plus simple, le motif. Tous les "
                "composés de formule CH deux O indice n — comme CH deux O, "
                "C deux H quatre O deux, ou C six H douze O six, le "
                "glucose — conduisent exactement aux mêmes pourcentages. "
                "La connaissance de la masse molaire est donc "
                "indispensable pour fixer la véritable formule brute."
            )
        ) as tracker:
            self.play(FadeIn(remarque))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(remarque))

        # --- À retenir : démarche récapitulative en 5 étapes --------------------
        entete = Text("Démarche récapitulative en 5 étapes", font_size=24, color=YELLOW, weight="BOLD")
        entete.next_to(titre, DOWN, buff=0.35)

        etapes = VGroup(
            Text("1. Combustion de m ; pesée de CO₂ et H₂O → m(CO₂), m(H₂O)", font_size=19),
            Text("2. Calcul de m(C) et m(H) → %C et %H", font_size=19),
            Text("3. Différence 100 − %C − %H → %O", font_size=19),
            Text("4. Mesure de M (densité de vapeur, ou donnée) → M", font_size=19),
            Text("5. Relation 12x/%C = y/%H = 16z/%O = M/100 → formule brute", font_size=19),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.28)
        etapes.next_to(entete, DOWN, buff=0.4)
        _fit(etapes, entete.get_bottom()[1] - 0.4)

        groupe_demarche = VGroup(entete, etapes)

        with self.voiceover(
            text=(
                "Récapitulons la démarche complète en cinq étapes. Un : "
                "combustion d'une masse m connue, pesée du CO2 et de "
                "l'eau. Deux : calcul des masses de carbone et "
                "d'hydrogène, pour obtenir leurs pourcentages. Trois : "
                "pourcentage d'oxygène par différence. Quatre : mesure de "
                "la masse molaire M. Cinq : application de la relation "
                "fondamentale pour obtenir la formule brute."
            )
        ) as tracker:
            self.play(FadeIn(entete))
            self.play(FadeIn(etapes))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(groupe_demarche), FadeOut(titre))
