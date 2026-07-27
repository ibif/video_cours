"""
scenes/Physique_EnergiePotentielleElectrostatique_01.py — Chapitre « Énergie
potentielle électrostatique » (1ereC, Physique), scène 01.

Potentiel électrique d'un point et différence de potentiel (tension) entre
deux points : définitions, propriétés (U_BA=-U_AB, indépendance de la
référence, U_AA=0), exemple résolu.
Source : 1ereC/Physique.pdf, pages 66-75.
"""

import textwrap

from manim import (
    BLUE,
    DOWN,
    LEFT,
    RED,
    RIGHT,
    UP,
    WHITE,
    YELLOW,
    Arrow,
    Dot,
    FadeIn,
    FadeOut,
    MathTex,
    Rectangle,
    Text,
    VGroup,
    Write,
)

from shapes.base_scene import NotionScene
from shapes.boxes import definition_box, essentiel_box, example_box, property_box, scene_title


def _wrap(text: str, width: int = 56) -> str:
    return "\n".join(textwrap.fill(line, width=width) for line in text.split("\n"))


def _plaques_chargees(sep: float = 4.4, hauteur: float = 2.6):
    """Deux plaques planes chargées (+ à gauche, - à droite) créant un champ
    uniforme entre elles, matérialisé par trois flèches."""
    plaque_pos = Rectangle(width=0.14, height=hauteur, color=RED, fill_color=RED, fill_opacity=1.0)
    plaque_neg = Rectangle(width=0.14, height=hauteur, color=BLUE, fill_color=BLUE, fill_opacity=1.0)
    plaque_pos.move_to(LEFT * sep / 2)
    plaque_neg.move_to(RIGHT * sep / 2)
    label_pos = Text("+", font_size=30, color=RED).next_to(plaque_pos, UP, buff=0.1)
    label_neg = Text("−", font_size=30, color=BLUE).next_to(plaque_neg, UP, buff=0.1)
    fleches = VGroup(
        *[
            Arrow(
                plaque_pos.get_right() + UP * y + RIGHT * 0.05,
                plaque_neg.get_left() + UP * y + LEFT * 0.05,
                color=YELLOW,
                buff=0,
                stroke_width=3,
            )
            for y in [-0.9, 0.0, 0.9]
        ]
    )
    return VGroup(plaque_pos, plaque_neg, label_pos, label_neg, fleches)


class PotentielElectriqueDDP(NotionScene):
    def construct(self):
        titre = scene_title("Potentiel électrique et différence de potentiel")
        titre.scale(0.46)
        titre.to_edge(UP)

        # --- Énoncé : état électrique d'un point ---------------------------------
        schema = _plaques_chargees()
        point_m = Dot(schema.get_center() + UP * 0.3 + LEFT * 0.4, color=WHITE, radius=0.08)
        label_m = MathTex("M", font_size=28).next_to(point_m, UP, buff=0.15)
        schema_complet = VGroup(schema, point_m, label_m)
        schema_complet.next_to(titre, DOWN, buff=0.6)

        with self.voiceover(
            text=(
                "Entre deux plaques chargées, l'une positivement, l'autre "
                "négativement, règne un champ électrostatique uniforme. Un "
                "point M placé entre les plaques possède, du seul fait de "
                "sa position, un état électrique bien précis. Comment "
                "caractériser cet état électrique ?"
            )
        ) as tracker:
            self.play(FadeIn(schema))
            self.play(FadeIn(point_m), Write(label_m))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(point_m), FadeOut(label_m))
        self.play(schema.animate.scale(0.55).to_corner(UP + RIGHT).shift(DOWN * 0.2))

        # --- Définition : potentiel électrique -----------------------------------
        definition_v = definition_box(
            VGroup(
                Text("Potentiel électrique en un point M :", font_size=23),
                MathTex(r"V_M \; \text{(en volts, V)}", font_size=28),
                Text(
                    "Défini à une constante près (référence arbitraire,",
                    font_size=20,
                ),
                Text("souvent la Terre, où V=0).", font_size=20),
            ).arrange(DOWN, buff=0.22),
            box_width=9.4,
        )
        definition_v.next_to(titre, DOWN, buff=0.6).to_edge(LEFT, buff=0.6)

        with self.voiceover(
            text=(
                "On associe à chaque point M de l'espace une grandeur "
                "appelée potentiel électrique, notée V indice M, exprimée "
                "en volts. Comme pour l'énergie potentielle de pesanteur, "
                "le potentiel électrique est défini à une constante près : "
                "on choisit une référence arbitraire, souvent la Terre, "
                "pour laquelle le potentiel est pris égal à zéro."
            )
        ) as tracker:
            self.play(FadeIn(definition_v))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(definition_v))

        # --- Définition : différence de potentiel --------------------------------
        definition_u = definition_box(
            VGroup(
                Text("Différence de potentiel (tension) entre A et B :", font_size=22),
                MathTex(r"U_{AB} = V_A - V_B \; \text{(en volts, V)}", font_size=28),
                Text("Se mesure directement au voltmètre.", font_size=20),
            ).arrange(DOWN, buff=0.25),
            box_width=10.6,
        )
        definition_u.next_to(titre, DOWN, buff=0.6)

        with self.voiceover(
            text=(
                "On définit surtout la différence de potentiel entre deux "
                "points A et B, aussi appelée tension, notée U indice A B, "
                "égale à V indice A moins V indice B, en volts. À la "
                "différence du potentiel seul, cette tension se mesure "
                "directement avec un voltmètre, sans avoir besoin de "
                "connaître de référence."
            )
        ) as tracker:
            self.play(FadeIn(definition_u))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(definition_u))

        # --- Raisonnement : propriétés de U_AB -----------------------------------
        proprietes = property_box(
            VGroup(
                MathTex(r"U_{BA} = -\,U_{AB} \quad \text{(grandeur algébrique)}", font_size=25),
                Text("U_AB ne dépend pas de la référence choisie.", font_size=21),
                MathTex(r"U_{AA} = 0", font_size=25),
            ).arrange(DOWN, buff=0.3),
            box_width=10.2,
        )
        proprietes.next_to(titre, DOWN, buff=0.6)

        with self.voiceover(
            text=(
                "Trois propriétés importantes découlent de cette "
                "définition. D'abord, U B A est égal à moins U A B : la "
                "tension est une grandeur algébrique, qui change de signe "
                "quand on inverse l'ordre des points. Ensuite, U A B ne "
                "dépend jamais de la référence choisie pour les potentiels, "
                "puisque la constante de référence s'élimine dans la "
                "soustraction. Enfin, U A A est nul : la tension entre un "
                "point et lui-même est toujours nulle."
            )
        ) as tracker:
            self.play(Write(proprietes))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(proprietes))

        # --- Exemple résolu 1 -----------------------------------------------------
        enonce = Text(
            _wrap(
                "Exemple : au point A, V_A=150 V ; au point B, V_B=40 V. "
                "Calculer U_AB puis U_BA.",
                width=54,
            ),
            font_size=23,
        )
        enonce.next_to(titre, DOWN, buff=0.6)

        with self.voiceover(
            text=(
                "Prenons un exemple. Au point A, le potentiel vaut 150 "
                "volts ; au point B, il vaut 40 volts. Calculons la tension "
                "U A B, puis la tension U B A."
            )
        ) as tracker:
            self.play(Write(enonce))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(enonce))

        calcul = example_box(
            VGroup(
                MathTex(r"U_{AB} = V_A - V_B = 150 - 40 = 110\ \text{V}", font_size=27),
                MathTex(r"U_{BA} = -\,U_{AB} = -110\ \text{V}", font_size=27),
            ).arrange(DOWN, buff=0.3),
            box_width=9.6,
        )
        calcul.next_to(titre, DOWN, buff=0.6)

        with self.voiceover(
            text=(
                "U A B vaut V A moins V B, soit 150 moins 40, c'est-à-dire "
                "110 volts. Et U B A, l'opposé, vaut moins 110 volts. Le "
                "signe indique le sens : de A vers B, le potentiel "
                "diminue."
            )
        ) as tracker:
            self.play(FadeIn(calcul))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(calcul), FadeOut(schema))

        # --- À retenir --------------------------------------------------------------
        retenir = essentiel_box(
            Text(
                _wrap(
                    "Potentiel V_M (volts, défini à une constante près). "
                    "Tension U_AB=V_A-V_B (mesurable au voltmètre, "
                    "indépendante de la référence). U_BA=-U_AB et U_AA=0.",
                    width=56,
                ),
                font_size=22,
            )
        )
        retenir.next_to(titre, DOWN, buff=0.6)

        with self.voiceover(
            text=(
                "À retenir : le potentiel V M, en volts, est défini à une "
                "constante près. La tension U A B, égale à V A moins V B, "
                "se mesure directement au voltmètre et ne dépend pas de la "
                "référence. Elle vérifie U B A égale moins U A B, et U A A "
                "est nulle. Dans la scène suivante, nous allons relier "
                "cette tension au travail de la force électrostatique."
            )
        ) as tracker:
            self.play(FadeIn(retenir))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(titre), FadeOut(retenir))
