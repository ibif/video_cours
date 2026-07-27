"""
scenes/Physique_EnergieMecanique_03.py — Chapitre 5 « Énergie mécanique »
(1ereC, Physique), scène 03.

Définition de l'énergie mécanique : Em=Ec+Ep (joules, grandeur d'état).
Exemple résolu 1 : balle de 200 g lancée verticalement, à z=3 m avec
v=4 m/s → Em=Ec+Ep=1,6+6=7,6 J.
Source : 1ereC/Physique.pdf, chapitre 5, pages 43-53.
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
    DoubleArrow,
    FadeIn,
    FadeOut,
    Line,
    MathTex,
    Text,
    VGroup,
    Vector,
    Write,
)

from shapes.base_scene import NotionScene
from shapes.boxes import corrige_box, definition_box, essentiel_box, exercise_box, scene_title, warning_box

POIDS_COLOR = "#1E5FA8"
VITESSE_COLOR = "#288073"


def _wrap(text: str, width: int = 56) -> str:
    return "\n".join(textwrap.fill(line, width=width) for line in text.split("\n"))


class DefinitionEnergieMecanique(NotionScene):
    def construct(self):
        titre = scene_title("Définition de l'énergie mécanique")
        titre.scale(0.5)
        titre.to_edge(UP)

        # --- Énoncé : reprise du constat de la scène précédente ---------------------
        intro = Text(
            _wrap(
                "Nous venons de voir qu'en chute libre, la somme Ec+Ep se "
                "conserve. Donnons maintenant une définition générale, "
                "valable pour tout système mécanique.",
                width=54,
            ),
            font_size=24,
        )
        intro.next_to(titre, DOWN, buff=0.6)

        with self.voiceover(
            text=(
                "Nous venons de voir qu'en chute libre, la somme de "
                "l'énergie cinétique et de l'énergie potentielle se "
                "conserve. Donnons maintenant une définition générale de "
                "cette quantité, valable pour tout système mécanique, "
                "qu'il soit en chute libre ou non."
            )
        ) as tracker:
            self.play(Write(titre))
            self.play(FadeIn(intro))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(intro))

        # --- Définition ---------------------------------------------------------------
        definition = definition_box(
            VGroup(
                Text("Énergie mécanique d'un système", font_size=23, weight="BOLD"),
                MathTex(r"E_m = E_c + E_p", font_size=32),
                Text("Ep = Epp + Epe (selon les forces en jeu)", font_size=20),
                Text("Em se mesure en joules (J) — grandeur d'état", font_size=20),
            ).arrange(DOWN, buff=0.22),
            box_width=10.5,
        )
        definition.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Définition : l'énergie mécanique d'un système, notée E m, "
                "est la somme de son énergie cinétique et de son énergie "
                "potentielle, laquelle regroupe l'énergie potentielle de "
                "pesanteur et, le cas échéant, l'énergie potentielle "
                "élastique. L'énergie mécanique se mesure en joules, comme "
                "toutes les énergies, et c'est une grandeur d'état : elle "
                "se calcule à un instant donné, à partir de l'état du "
                "système à cet instant précis."
            )
        ) as tracker:
            self.play(FadeIn(definition))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(definition))

        # --- Raisonnement : Em, un instantané de l'état du système ------------------
        remarque = warning_box(
            Text(
                _wrap(
                    "Em se calcule à CHAQUE instant, comme Ec et Ep : ce "
                    "n'est qu'ensuite qu'on se demandera si sa valeur "
                    "varie ou reste constante entre deux instants.",
                    width=54,
                ),
                font_size=21,
            ),
            box_width=10.8,
        )
        remarque.next_to(titre, DOWN, buff=0.6)

        with self.voiceover(
            text=(
                "Remarque importante : l'énergie mécanique se calcule à "
                "chaque instant, tout comme l'énergie cinétique et "
                "l'énergie potentielle. Ce n'est que dans un second temps "
                "que l'on se demandera si sa valeur varie, ou reste "
                "constante, entre deux instants — c'est l'objet des "
                "scènes suivantes."
            )
        ) as tracker:
            self.play(FadeIn(remarque))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(remarque))

        # --- Exemple traité : balle lancée verticalement ------------------------------
        sol = Line(LEFT * 1.6, RIGHT * 1.6, color=WHITE)
        balle = Dot(UP * 1.4, color=YELLOW, radius=0.13)
        z_fleche = DoubleArrow(sol.get_center() + RIGHT * 1.0, balle.get_center() + RIGHT * 1.0 + DOWN * 0.0, buff=0, stroke_width=2, color=WHITE)
        z_fleche = DoubleArrow(sol.get_center() + RIGHT * 1.0, UP * 1.4 + RIGHT * 1.0, buff=0, stroke_width=2, color=WHITE)
        z_label = MathTex("z", font_size=24).next_to(z_fleche, RIGHT, buff=0.1)
        v_vec = Vector(UP * 0.6, color=VITESSE_COLOR).next_to(balle, LEFT, buff=0.15)
        v_label = MathTex(r"\vec{v}", font_size=22, color=VITESSE_COLOR).next_to(v_vec, LEFT, buff=0.1)
        schema = VGroup(sol, balle, z_fleche, z_label, v_vec, v_label)
        schema.scale(0.9).move_to(LEFT * 3.3)

        enonce = exercise_box(
            Text(
                _wrap(
                    "Une balle de masse 200 g est lancée verticalement. À "
                    "un instant donné, elle se trouve à z=3 m au-dessus du "
                    "sol (référence Epp=0) avec une vitesse v=4 m/s. "
                    "Calculer son énergie mécanique (g=10 N/kg).",
                    width=40,
                ),
                font_size=20,
            ),
            box_width=6.6,
        )
        enonce.next_to(schema, RIGHT, buff=0.5)

        with self.voiceover(
            text=(
                "Exemple résolu. Une balle de masse deux cents grammes est "
                "lancée verticalement. À un instant donné, elle se trouve "
                "à trois mètres au-dessus du sol, pris comme référence des "
                "énergies potentielles, avec une vitesse de quatre mètres "
                "par seconde. On prend g égale dix newtons par kilogramme. "
                "Calculons son énergie mécanique à cet instant."
            )
        ) as tracker:
            self.play(FadeIn(schema), FadeIn(enonce))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(schema), FadeOut(enonce))

        calc = corrige_box(
            VGroup(
                MathTex(r"E_c = \tfrac{1}{2}\times 0{,}2\times 4^2 = 1{,}6\ \text{J}", font_size=27),
                MathTex(r"E_{pp} = 0{,}2\times 10\times 3 = 6\ \text{J}", font_size=27),
                MathTex(r"E_m = E_c + E_{pp} = 1{,}6 + 6 = 7{,}6\ \text{J}", font_size=29, color=YELLOW),
            ).arrange(DOWN, buff=0.3),
            box_width=10.5,
        )
        calc.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "L'énergie cinétique vaut un demi fois zéro virgule deux "
                "fois quatre au carré, soit un virgule six joule. "
                "L'énergie potentielle de pesanteur vaut zéro virgule deux "
                "fois dix fois trois, soit six joules. L'énergie mécanique "
                "vaut donc leur somme : un virgule six plus six, soit sept "
                "virgule six joules."
            )
        ) as tracker:
            self.play(FadeIn(calc))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(calc))

        # --- À retenir -----------------------------------------------------------------
        retenir = essentiel_box(
            MathTex(
                r"E_m = E_c + E_p \quad \text{(en joules, à chaque instant)}",
                font_size=28,
            ),
            box_width=10.2,
        )
        retenir.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Retenons l'essentiel : l'énergie mécanique d'un système "
                "vaut la somme de son énergie cinétique et de son énergie "
                "potentielle, en joules, calculée à chaque instant."
            )
        ) as tracker:
            self.play(FadeIn(retenir))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(retenir))

        # --- Piège à éviter --------------------------------------------------------------
        piege = warning_box(
            Text(
                _wrap(
                    "Ne pas oublier l'énergie potentielle ÉLASTIQUE si un "
                    "ressort est présent dans le système : Ep=Epp+Epe, "
                    "pas seulement Epp.",
                    width=52,
                ),
                font_size=22,
            ),
            box_width=10.6,
        )
        piege.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Piège à éviter : si le système comporte un ressort, il ne "
                "faut surtout pas oublier l'énergie potentielle élastique "
                "dans le calcul de Em. L'énergie potentielle totale est la "
                "somme Epp plus Epe, pas seulement Epp."
            )
        ) as tracker:
            self.play(FadeIn(piege))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(piege), FadeOut(titre))
