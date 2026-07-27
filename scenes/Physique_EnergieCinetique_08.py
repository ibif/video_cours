"""
scenes/Physique_EnergieCinetique_08.py — Chapitre 3 « Énergie cinétique »
(1ereC, Physique), scène 08.

§ Application : pendule simple, étude énergétique. Définition du pendule
simple, bilan des forces (poids + tension, tension perpendiculaire à la
trajectoire donc travail nul), hauteur de descente h=L(1-cosθ₀), théorème
de l'énergie cinétique entre A (lâcher) et B (point bas) :
v_B=√(2gL(1-cosθ₀)). Exemple résolu : L=0,9 m, θ₀=60° → v_B=3 m/s.
Source : 1ereC/Physique.pdf, pages 24-33 (chapitre 3, § 5, partie 4).
"""

import textwrap

import numpy as np

from manim import (
    DOWN,
    LEFT,
    PI,
    RIGHT,
    UP,
    WHITE,
    YELLOW,
    Arc,
    Create,
    DashedLine,
    Dot,
    FadeIn,
    FadeOut,
    Line,
    MathTex,
    Text,
    VGroup,
    Write,
)

from shapes.base_scene import NotionScene
from shapes.boxes import definition_box, essentiel_box, example_box, scene_title, theorem_box


def _wrap(text: str, width: int = 56) -> str:
    return "\n".join(textwrap.fill(line, width=width) for line in text.split("\n"))


class ApplicationPenduleSimple(NotionScene):
    def construct(self):
        titre = scene_title("Application : pendule simple, étude énergétique")
        titre.scale(0.46)
        titre.to_edge(UP)

        # --- Énoncé : définition du pendule simple ---------------------------------
        definition = definition_box(
            VGroup(
                Text("Pendule simple", font_size=23, weight="BOLD"),
                Text(
                    _wrap(
                        "Masse ponctuelle m suspendue à un fil inextensible "
                        "de longueur L, sans masse, fixé en un point O.",
                        width=48,
                    ),
                    font_size=21,
                ),
            ).arrange(DOWN, buff=0.22),
            box_width=10.6,
        )
        definition.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Dernière application du chapitre : le pendule simple. Il "
                "s'agit d'une masse ponctuelle m, suspendue à un fil "
                "inextensible et sans masse, de longueur L, fixé en un "
                "point O."
            )
        ) as tracker:
            self.play(Write(titre))
            self.play(FadeIn(definition))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(definition))

        # --- Schéma : pendule en A (lâché, angle theta0) et en B (point bas) ------
        o_pt = UP * 2.0
        long_fil = 2.6
        theta0 = 60 * PI / 180
        a_pt = o_pt + long_fil * np.array([np.sin(theta0), -np.cos(theta0), 0])
        b_pt = o_pt + DOWN * long_fil
        fil_a = Line(o_pt, a_pt, color=WHITE, stroke_width=2)
        fil_b = DashedLine(o_pt, b_pt, color="#595959", stroke_width=1.5)
        bille_a = Dot(a_pt, color=YELLOW, radius=0.13)
        bille_b = Dot(b_pt, color="#288073", radius=0.13)
        pivot = Dot(o_pt, color=WHITE, radius=0.06)
        angle_arc = Arc(radius=0.7, start_angle=-PI / 2, angle=theta0, arc_center=o_pt, color="#DE7C1F")
        theta_label = MathTex(r"\theta_0", font_size=24, color="#DE7C1F").move_to(
            o_pt + 0.95 * np.array([np.sin(theta0 / 2), -np.cos(theta0 / 2), 0])
        )
        label_a = MathTex("A", font_size=24).next_to(bille_a, RIGHT, buff=0.15)
        label_b = MathTex("B", font_size=24).next_to(bille_b, RIGHT, buff=0.15)
        label_o = MathTex("O", font_size=22).next_to(pivot, UP, buff=0.1)
        # h : différence de hauteur entre A et B
        h_a = DashedLine(a_pt, np.array([b_pt[0] - 0.1, a_pt[1], 0]), color="#B42E41", stroke_width=1.5)
        schema = VGroup(
            fil_b, fil_a, pivot, bille_a, bille_b, angle_arc, theta_label,
            label_a, label_b, label_o, h_a,
        )
        schema.scale(0.85)
        schema.next_to(titre, DOWN, buff=0.3)

        with self.voiceover(
            text=(
                "On lâche le pendule sans vitesse initiale en A, écarté "
                "d'un angle thêta zéro par rapport à la verticale, et on "
                "l'étudie lorsqu'il repasse par le point le plus bas, B. "
                "Deux forces s'exercent sur la masse : son poids, et la "
                "tension du fil."
            )
        ) as tracker:
            self.play(Create(schema))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(schema))

        # --- Raisonnement : bilan des forces, tension ne travaille pas ------------
        bilan = VGroup(
            Text("Bilan des forces sur la masse : poids P⃗ et tension T⃗ du fil.", font_size=21),
            Text(
                "La tension T⃗ est radiale (le long du fil), donc TOUJOURS",
                font_size=21,
            ),
            Text(
                "perpendiculaire à la trajectoire (tangentielle) :  W(T⃗) = 0.",
                font_size=21,
            ),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.2)
        bilan.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Faisons le bilan des forces : le poids P, et la tension T "
                "du fil. La tension est radiale, dirigée le long du fil, "
                "donc toujours perpendiculaire à la trajectoire, qui est "
                "elle-même tangentielle. Son travail est donc nul : la "
                "tension du fil ne travaille jamais."
            )
        ) as tracker:
            self.play(Write(bilan[0]))
            self.play(Write(bilan[1]))
            self.play(Write(bilan[2]))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(bilan))

        # --- Hauteur de descente et théorème --------------------------------------
        calcul = VGroup(
            MathTex(r"h = L(1-\cos\theta_0) \quad \text{(hauteur de descente de A à B)}", font_size=24),
            MathTex(r"\Delta E_c = \dfrac{1}{2}mv_B^2 - 0 = W_{A\to B}(\vec{P}) + \underbrace{W_{A\to B}(\vec{T})}_{=\,0} = mgh", font_size=22),
            MathTex(r"\Longrightarrow\ v_B = \sqrt{2gL(1-\cos\theta_0)}", font_size=30, color=YELLOW),
        ).arrange(DOWN, buff=0.3)
        calcul.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "La hauteur de descente entre A et B vaut h égale L fois, "
                "un moins cosinus de thêta zéro. Le théorème de l'énergie "
                "cinétique donne alors : un demi m v B carré moins zéro "
                "égale le travail du poids, puisque celui de la tension "
                "est nul, soit m g h. On en déduit v B égale racine carrée "
                "de deux g L, un moins cosinus de thêta zéro."
            )
        ) as tracker:
            self.play(Write(calcul[0]))
            self.play(Write(calcul[1]))
            self.play(Write(calcul[2]))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(calcul))

        # --- Formule encadrée --------------------------------------------------------
        formule = theorem_box(
            VGroup(
                Text("Pendule simple — vitesse au point bas", font_size=22, weight="BOLD"),
                MathTex(r"v_B = \sqrt{2gL(1-\cos\theta_0)}", font_size=30),
            ).arrange(DOWN, buff=0.25),
            box_width=11.0,
        )
        formule.next_to(titre, DOWN, buff=0.45)

        with self.voiceover(
            text=(
                "Voici la formule à retenir pour la vitesse du pendule "
                "simple à son point le plus bas : v B égale racine carrée "
                "de deux g L, un moins cosinus de thêta zéro."
            )
        ) as tracker:
            self.play(FadeIn(formule))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(formule))

        # --- Exemple résolu ------------------------------------------------------------
        exemple = example_box(
            VGroup(
                Text("Pendule L = 0,9 m, lâché avec θ₀ = 60° :", font_size=21),
                MathTex(r"v_B = \sqrt{2\times 9{,}8\times 0{,}9\times(1-\cos 60°)} = \sqrt{2\times 9{,}8\times 0{,}9\times 0{,}5} \approx 3\ \text{m/s}", font_size=21),
            ).arrange(DOWN, buff=0.25),
            box_width=12.2,
        )
        exemple.next_to(titre, DOWN, buff=0.45)

        with self.voiceover(
            text=(
                "Exemple résolu : un pendule de longueur zéro virgule neuf "
                "mètre, lâché avec un angle thêta zéro de soixante degrés. "
                "Comme le cosinus de soixante degrés vaut zéro virgule "
                "cinq, on trouve v B égale racine carrée de deux fois neuf "
                "virgule huit fois zéro virgule neuf fois zéro virgule "
                "cinq, soit environ trois mètres par seconde."
            )
        ) as tracker:
            self.play(FadeIn(exemple))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(exemple))

        # --- À retenir -------------------------------------------------------------
        retenir = essentiel_box(
            VGroup(
                Text("À retenir", font_size=24, weight="BOLD"),
                MathTex(r"v_B = \sqrt{2gL(1-\cos\theta_0)}", font_size=28),
                Text("La tension du fil, radiale, ne travaille jamais (W = 0).", font_size=21),
            ).arrange(DOWN, buff=0.25),
            box_width=11.6,
        )
        retenir.next_to(titre, DOWN, buff=0.45)

        with self.voiceover(
            text=(
                "Retenons l'essentiel : la vitesse au point bas d'un "
                "pendule simple vaut racine carrée de deux g L, un moins "
                "cosinus de thêta zéro, et il ne faut jamais oublier que "
                "la tension du fil, étant radiale, ne travaille jamais."
            )
        ) as tracker:
            self.play(FadeIn(retenir))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(retenir), FadeOut(titre))
