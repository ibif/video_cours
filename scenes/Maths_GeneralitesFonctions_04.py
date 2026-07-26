"""
scenes/Maths_GeneralitesFonctions_04.py — Chapitre 3 (1ereC, Maths), scène 04.

Sens de variation : croissance, décroissance, stricte monotonie, taux de
variation, lien entre le signe du taux et le sens de variation.
Source : 1ereC/Maths.pdf, chapitre 3, pages 28-40.
"""

import textwrap

from manim import DOWN, LEFT, RIGHT, UP, WHITE, YELLOW, Axes, FadeIn, FadeOut, MathTex, Text, VGroup, Write

from shapes.base_scene import NotionScene
from shapes.boxes import definition_box, essentiel_box, example_box, scene_title, theorem_box, warning_box


def _wrap(text: str, width: int = 60) -> str:
    return "\n".join(textwrap.fill(line, width=width) for line in text.split("\n"))


class SensDeVariation(NotionScene):
    def construct(self):
        titre = scene_title("Sens de variation")
        titre.scale(0.6)
        titre.to_edge(UP)
        self.play(Write(titre))

        # --- Énoncé : croissance / décroissance / stricte monotonie ---------
        def_croissance = definition_box(
            MathTex(
                r"""
                \begin{array}{l}
                f \text{ croissante sur } I : \ \forall a,b \in I,\ a \leq b \ \Longrightarrow \ f(a) \leq f(b) \\
                f \text{ décroissante sur } I : \ \forall a,b \in I,\ a \leq b \ \Longrightarrow \ f(a) \geq f(b) \\
                \text{stricte : inégalités strictes pour } a \neq b
                \end{array}
                """,
                font_size=25,
            ),
            box_width=11.0,
        )
        def_croissance.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Une fonction f est croissante sur un intervalle I si, "
                "pour tous a et b de I, a inférieur ou égal à b entraîne f "
                "de a inférieur ou égal à f de b. Elle est décroissante si "
                "l'inégalité s'inverse. On parle de stricte monotonie "
                "quand les inégalités sont strictes dès que a est "
                "différent de b."
            )
        ) as tracker:
            self.play(FadeIn(def_croissance))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(def_croissance))

        # --- Taux de variation ---------------------------------------------
        def_taux = definition_box(
            MathTex(
                r"\tau(a,b) = \dfrac{f(b)-f(a)}{b-a}, \qquad a \neq b, \ a,b \in D_f",
                font_size=30,
            )
        )
        def_taux.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "On introduit le taux de variation de f entre a et b, noté "
                "tau de a et b, défini comme f de b moins f de a, le tout "
                "divisé par b moins a, pour a différent de b."
            )
        ) as tracker:
            self.play(FadeIn(def_taux))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(def_taux))

        # --- Animation du raisonnement : théorème signe du taux ---------------
        theo_taux = theorem_box(
            MathTex(
                r"""
                \begin{array}{l}
                f \text{ croissante sur } I \ \Longleftrightarrow \ \forall a \neq b \in I,\ \tau(a,b) \geq 0 \\
                f \text{ décroissante sur } I \ \Longleftrightarrow \ \forall a \neq b \in I,\ \tau(a,b) \leq 0
                \end{array}
                """,
                font_size=25,
            ),
            box_width=11.2,
        )
        theo_taux.next_to(titre, DOWN, buff=0.55)

        with self.voiceover(
            text=(
                "Théorème : f est croissante sur I si, et seulement si, "
                "son taux de variation est positif ou nul entre deux "
                "points quelconques distincts de I. Elle est décroissante "
                "si, et seulement si, ce taux est négatif ou nul."
            )
        ) as tracker:
            self.play(FadeIn(theo_taux))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(theo_taux))

        demo_taux = example_box(
            Text(
                _wrap(
                    "Démonstration (sens direct) : si f est croissante et "
                    "a < b, alors f(a) ≤ f(b), donc f(b) − f(a) ≥ 0 et "
                    "b − a > 0 : le quotient τ(a,b) est donc ≥ 0. Le "
                    "raisonnement se transpose pour a > b, et de façon "
                    "analogue pour la décroissance.",
                    width=56,
                ),
                font_size=22,
            ),
            box_width=11.0,
        )
        demo_taux.next_to(titre, DOWN, buff=0.6)

        with self.voiceover(
            text=(
                "Démonstration rapide du sens direct : si f est croissante "
                "et a strictement inférieur à b, alors f de a est "
                "inférieur ou égal à f de b, donc le numérateur f de b "
                "moins f de a est positif ou nul, et le dénominateur b "
                "moins a est strictement positif : le quotient, c'est-à-"
                "dire le taux de variation, est donc positif ou nul."
            )
        ) as tracker:
            self.play(FadeIn(demo_taux))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(demo_taux))

        # --- Exemple traité 5 : f(x) = x² -------------------------------------
        enonce_ex5 = Text(
            "Exemple 5 — f(x) = x², démonstration par factorisation",
            font_size=24,
            color=YELLOW,
            weight="BOLD",
        )
        enonce_ex5.next_to(titre, DOWN, buff=0.5)

        axes = Axes(
            x_range=[-3, 3, 1],
            y_range=[-1, 6, 1],
            x_length=5.5,
            y_length=3.3,
            axis_config={"color": WHITE, "font_size": 16},
        )
        axes.next_to(enonce_ex5, DOWN, buff=0.35).shift(LEFT * 2.7)
        courbe = axes.plot(lambda x: x**2, x_range=[-2.3, 2.3], color=YELLOW)
        schema = VGroup(axes, courbe)

        with self.voiceover(
            text=(
                "Exemple 5 : montrons que f de x égale x carré est "
                "strictement croissante sur zéro, plus infini, et "
                "strictement décroissante sur moins infini, zéro."
            )
        ) as tracker:
            self.play(FadeIn(enonce_ex5))
            self.play(FadeIn(schema))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(enonce_ex5), FadeOut(schema))

        demo_ex5 = example_box(
            MathTex(
                r"""
                \begin{array}{l}
                f(b)-f(a) = b^2-a^2 = (b-a)(b+a) \\
                \tau(a,b) = \dfrac{(b-a)(b+a)}{b-a} = a+b \\
                \text{Sur } [0;+\infty[,\ a+b>0 \Rightarrow \tau>0 \Rightarrow f \text{ strict. croissante} \\
                \text{Sur } ]-\infty;0],\ a+b<0 \Rightarrow \tau<0 \Rightarrow f \text{ strict. décroissante}
                \end{array}
                """,
                font_size=23,
            ),
            box_width=11.2,
        )
        demo_ex5.next_to(titre, DOWN, buff=0.55)

        with self.voiceover(
            text=(
                "On factorise : f de b moins f de a égale b carré moins a "
                "carré, soit b moins a, fois b plus a. Le taux de "
                "variation tau de a et b vaut donc a plus b, après "
                "simplification par b moins a. Sur zéro, plus infini, a "
                "plus b est strictement positif, donc f y est strictement "
                "croissante. Sur moins infini, zéro, a plus b est "
                "strictement négatif, donc f y est strictement "
                "décroissante."
            )
        ) as tracker:
            self.play(FadeIn(demo_ex5))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(demo_ex5))

        # --- À retenir ---------------------------------------------------
        retenir = essentiel_box(
            Text(
                _wrap(
                    "Le signe du taux de variation τ(a,b) sur un "
                    "intervalle donne directement le sens de variation : "
                    "positif → croissante, négatif → décroissante.",
                    width=56,
                ),
                font_size=24,
            ),
            box_width=10.8,
        )
        retenir.next_to(titre, DOWN, buff=0.6)

        with self.voiceover(
            text=(
                "À retenir : le signe du taux de variation tau de a et b "
                "sur un intervalle donne directement le sens de "
                "variation de la fonction sur cet intervalle — positif "
                "signifie croissante, négatif signifie décroissante."
            )
        ) as tracker:
            self.play(FadeIn(retenir))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(retenir))

        # --- Piège à éviter ----------------------------------------------
        piege = warning_box(
            Text(
                _wrap(
                    "Piège : le sens de variation dépend TOUJOURS de "
                    "l'intervalle considéré — x² n'est ni croissante ni "
                    "décroissante sur ℝ tout entier, seulement sur chacun "
                    "des deux intervalles séparément.",
                    width=56,
                ),
                font_size=23,
            ),
            box_width=10.8,
        )
        piege.next_to(titre, DOWN, buff=0.6)

        with self.voiceover(
            text=(
                "Attention : le sens de variation dépend toujours de "
                "l'intervalle considéré. La fonction x carré n'est ni "
                "croissante ni décroissante sur ℝ tout entier — elle ne "
                "l'est que sur chacun des deux intervalles pris "
                "séparément."
            )
        ) as tracker:
            self.play(FadeIn(piege))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(titre), FadeOut(piege))
