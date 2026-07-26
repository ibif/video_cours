"""
scenes/Maths_GeneralitesFonctions_08.py — Chapitre 3 (1ereC, Maths), scène 08.

Exemple de composition (décomposition u∘v), puis restriction et
prolongement d'une fonction.
Source : 1ereC/Maths.pdf, chapitre 3, pages 28-40.
"""

import textwrap

from manim import DOWN, LEFT, RIGHT, UP, WHITE, YELLOW, Axes, Dot, FadeIn, FadeOut, MathTex, Text, VGroup, Write

from shapes.base_scene import NotionScene
from shapes.boxes import definition_box, essentiel_box, example_box, scene_title, warning_box


def _wrap(text: str, width: int = 60) -> str:
    return "\n".join(textwrap.fill(line, width=width) for line in text.split("\n"))


class ExempleCompositionRestrictionProlongement(NotionScene):
    def construct(self):
        titre = scene_title("Composition — restriction et prolongement")
        titre.scale(0.5)
        titre.to_edge(UP)
        self.play(Write(titre))

        # --- Énoncé : exemple 9, décomposition -------------------------------
        enonce_ex9 = Text(
            "Exemple 9 — décomposer f(x) = 1/(x²+1) sur [0;+∞[",
            font_size=24,
            color=YELLOW,
            weight="BOLD",
        )
        enonce_ex9.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Exemple 9 : décomposons la fonction f de x égale un sur "
                "x carré plus un, définie sur zéro, plus l'infini, comme "
                "composée de deux fonctions plus simples."
            )
        ) as tracker:
            self.play(FadeIn(enonce_ex9))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(enonce_ex9))

        decomposition = example_box(
            MathTex(
                r"""
                \begin{array}{l}
                v(x) = x^2+1, \qquad u(t) = \dfrac{1}{t} \\[0.3em]
                (u \circ v)(x) = u(v(x)) = u(x^2+1) = \dfrac{1}{x^2+1} = f(x)
                \end{array}
                """,
                font_size=27,
            ),
            box_width=9.7,
        )
        decomposition.next_to(titre, DOWN, buff=0.55)

        with self.voiceover(
            text=(
                "On pose v de x égale x carré plus un, et u de t égale un "
                "sur t. Alors u rond v de x égale u appliqué à x carré "
                "plus un, soit un sur x carré plus un, qui est exactement "
                "f de x. On a donc bien f égale u rond v : la fonction "
                "carré-plus-un jouée par v, suivie de l'inverse joué par "
                "u."
            )
        ) as tracker:
            self.play(FadeIn(decomposition))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(decomposition))

        # --- Restriction et prolongement -------------------------------------
        def_restriction = definition_box(
            Text(
                _wrap(
                    "La restriction de f à une partie A de Df est la "
                    "fonction notée f|A, définie sur A, qui coïncide avec "
                    "f sur A (mêmes images).",
                    width=56,
                ),
                font_size=23,
            ),
            box_width=10.2,
        )
        def_restriction.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "La restriction de f à une partie A de Df est la fonction "
                "notée f restreinte à A, définie sur A seulement, mais qui "
                "coïncide avec f sur A — elle donne les mêmes images."
            )
        ) as tracker:
            self.play(FadeIn(def_restriction))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(def_restriction))

        def_prolongement = definition_box(
            Text(
                _wrap(
                    "Une fonction g, définie sur un ensemble E qui "
                    "contient Df, est un prolongement de f à E si g "
                    "coïncide avec f sur Df (g|Df = f).",
                    width=56,
                ),
                font_size=23,
            ),
            box_width=10.2,
        )
        def_prolongement.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "À l'inverse, une fonction g, définie sur un ensemble E "
                "qui contient Df, est un prolongement de f à E si g "
                "coïncide avec f sur Df — g étend f à un domaine plus "
                "large."
            )
        ) as tracker:
            self.play(FadeIn(def_prolongement))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(def_prolongement))

        remarques = example_box(
            Text(
                _wrap(
                    "Remarques : une fonction peut avoir plusieurs "
                    "prolongements possibles (rien n'impose qu'il soit "
                    "unique). Restriction et prolongement sont deux "
                    "opérations réciproques l'une de l'autre.",
                    width=56,
                ),
                font_size=22,
            ),
            box_width=10.8,
        )
        remarques.next_to(titre, DOWN, buff=0.55)

        with self.voiceover(
            text=(
                "Deux remarques : une fonction peut avoir plusieurs "
                "prolongements possibles, rien n'impose qu'il soit unique. "
                "Et restriction et prolongement sont deux opérations "
                "réciproques l'une de l'autre : si g prolonge f, alors f "
                "est la restriction de g à Df."
            )
        ) as tracker:
            self.play(FadeIn(remarques))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(remarques))

        # --- Exemple traité 10 -------------------------------------------------
        enonce_ex10 = Text(
            "Exemple 10 — f(x) = (x² − 1)/(x − 1), prolongement à ℝ",
            font_size=23,
            color=YELLOW,
            weight="BOLD",
        )
        enonce_ex10.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Exemple 10 : soit f de x égale x carré moins un, sur x "
                "moins un. Cherchons un prolongement de f à ℝ tout "
                "entier."
            )
        ) as tracker:
            self.play(FadeIn(enonce_ex10))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(enonce_ex10))

        calcul_ex10 = example_box(
            MathTex(
                r"""
                \begin{array}{l}
                D_f = \mathbb{R}\setminus\{1\} \\
                \forall x \neq 1, \ f(x) = \dfrac{(x-1)(x+1)}{x-1} = x+1 \\
                g(x) = x+1, \text{ définie sur } \mathbb{R} : \ g \text{ prolonge } f \text{ à } \mathbb{R}
                \end{array}
                """,
                font_size=25,
            ),
            box_width=9.2,
        )
        calcul_ex10.next_to(titre, DOWN, buff=0.55)

        axes = Axes(
            x_range=[-2, 3, 1],
            y_range=[-1, 4, 1],
            x_length=5.5,
            y_length=3.0,
            axis_config={"color": WHITE, "font_size": 14},
        )
        axes.next_to(calcul_ex10, DOWN, buff=0.35)
        droite = axes.plot(lambda x: x + 1, x_range=[-1.7, 2.7], color=YELLOW)
        trou = Dot(axes.c2p(1, 2), color=YELLOW, radius=0.09)
        trou.set_fill(opacity=0)
        trou.set_stroke(width=2)
        schema = VGroup(axes, droite, trou)

        with self.voiceover(
            text=(
                "Df est ℝ privé de un, car le dénominateur s'annule en x "
                "égale un. Mais pour x différent de un, en factorisant le "
                "numérateur, f de x se simplifie en x plus un. La fonction "
                "g de x égale x plus un, elle, est définie sur ℝ tout "
                "entier, et coïncide avec f partout où f est définie : g "
                "est donc un prolongement de f à ℝ — elle vient combler le "
                "trou de la courbe en x égale un."
            )
        ) as tracker:
            self.play(FadeIn(calcul_ex10))
            self.play(FadeIn(schema))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(calcul_ex10), FadeOut(schema))

        # --- À retenir ---------------------------------------------------
        retenir = essentiel_box(
            Text(
                _wrap(
                    "Restreindre = réduire le domaine sans changer les "
                    "images. Prolonger = agrandir le domaine en gardant "
                    "les mêmes images là où f était déjà définie.",
                    width=56,
                ),
                font_size=24,
            ),
            box_width=10.8,
        )
        retenir.next_to(titre, DOWN, buff=0.6)

        with self.voiceover(
            text=(
                "À retenir : restreindre une fonction, c'est réduire son "
                "domaine sans changer les images. Prolonger une fonction, "
                "c'est agrandir son domaine tout en gardant les mêmes "
                "images là où f était déjà définie."
            )
        ) as tracker:
            self.play(FadeIn(retenir))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(retenir))

        # --- Piège à éviter ----------------------------------------------
        piege = warning_box(
            Text(
                _wrap(
                    "Piège : un prolongement n'est pas unique sans "
                    "précision supplémentaire (continuité, dérivabilité). "
                    "Ne jamais affirmer « LE » prolongement de f sans "
                    "préciser le critère utilisé.",
                    width=56,
                ),
                font_size=23,
            ),
            box_width=10.8,
        )
        piege.next_to(titre, DOWN, buff=0.6)

        with self.voiceover(
            text=(
                "Attention : un prolongement n'est pas unique en général, "
                "sauf si l'on impose un critère supplémentaire, comme la "
                "continuité. Il ne faut donc jamais parler « du » "
                "prolongement de f sans préciser ce critère."
            )
        ) as tracker:
            self.play(FadeIn(piege))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(titre), FadeOut(piege))
