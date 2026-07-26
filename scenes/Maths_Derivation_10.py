"""
scenes/Maths_Derivation_10.py — Chapitre 9 (1ereC, Maths), scène 10.

Théorème fondamental (admis) : signe de f' et sens de variation. Exemple
résolu 13 complet : f(x) = x³-3x+1, dérivée, tableau de signe, tableau de
variation, figure de la courbe.
Source : 1ereC/Maths.pdf, chapitre 9, pages 105-117.
"""

import textwrap

from manim import (
    DOWN,
    LEFT,
    RIGHT,
    UP,
    WHITE,
    YELLOW,
    Axes,
    Create,
    Dot,
    FadeIn,
    FadeOut,
    MathTex,
    Text,
    VGroup,
    Write,
)

from shapes.base_scene import NotionScene
from shapes.boxes import example_box, essentiel_box, scene_title, theorem_box


def _wrap(text: str, width: int = 58) -> str:
    return "\n".join(textwrap.fill(line, width=width) for line in text.split("\n"))


class SigneDeriveeSensVariation(NotionScene):
    def construct(self):
        titre = scene_title("Signe de la dérivée et sens de variation")
        titre.scale(0.48)
        titre.to_edge(UP)

        # --- Énoncé ------------------------------------------------------------
        enonce = Text(
            _wrap(
                "Le signe du coefficient directeur de la tangente en "
                "chaque point donne une indication précieuse : est-ce que "
                "la courbe monte ou descend ?",
                width=56,
            ),
            font_size=24,
            color=YELLOW,
        )
        enonce.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Nous savons que f prime de a est le coefficient directeur "
                "de la tangente au point d'abscisse a. Or, le signe de ce "
                "coefficient directeur donne une indication très précieuse "
                "sur le comportement local de la courbe : monte-t-elle, ou "
                "descend-elle ? C'est ce lien fondamental entre le signe de "
                "la dérivée et les variations de f que nous établissons "
                "maintenant."
            )
        ) as tracker:
            self.play(Write(titre))
            self.play(FadeIn(enonce))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(enonce))

        # --- Théorème fondamental (admis) --------------------------------------------
        theoreme = theorem_box(
            VGroup(
                Text("Soit f dérivable sur un intervalle I (théorème admis) :", font_size=21),
                MathTex(
                    r"f' \geq 0 \text{ sur } I \ \Longrightarrow\ f \text{ croissante sur } I",
                    font_size=25,
                ),
                MathTex(
                    r"f' \leq 0 \text{ sur } I \ \Longrightarrow\ f \text{ décroissante sur } I",
                    font_size=25,
                ),
                MathTex(
                    r"f' = 0 \text{ sur } I \ \Longrightarrow\ f \text{ constante sur } I",
                    font_size=25,
                ),
                Text(
                    "Précision : si f' > 0 sauf en un nombre fini de points où f'=0,\n"
                    "f est STRICTEMENT croissante sur I.",
                    font_size=18,
                ),
            ).arrange(DOWN, buff=0.22),
            box_width=11.2,
        )
        theoreme.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Voici le théorème fondamental, admis. Soit f une fonction "
                "dérivable sur un intervalle I. Si f prime est positive ou "
                "nulle sur I, alors f est croissante sur I. Si f prime est "
                "négative ou nulle sur I, alors f est décroissante sur I. "
                "Et si f prime est nulle sur I tout entier, alors f est "
                "constante sur I. Précision importante : si f prime est "
                "strictement positive, sauf éventuellement en un nombre "
                "fini de points isolés où elle s'annule, alors f est "
                "strictement croissante sur I."
            )
        ) as tracker:
            self.play(FadeIn(theoreme))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(theoreme))

        # --- Exemple résolu 13 : f(x) = x³-3x+1 ----------------------------------------
        enonce_ex = Text("Exemple 13 — étudier les variations de f(x) = x³-3x+1 :", font_size=22, color=YELLOW)
        enonce_ex.next_to(titre, DOWN, buff=0.45)

        with self.voiceover(
            text=(
                "Étudions un exemple complet : soit f de x égale x au cube, "
                "moins trois x, plus un, définie sur l'ensemble des réels."
            )
        ) as tracker:
            self.play(FadeIn(enonce_ex))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(enonce_ex))

        derivee_ex = example_box(
            VGroup(
                MathTex(r"f'(x) = 3x^2-3 = 3(x^2-1) = 3(x-1)(x+1)", font_size=27),
                Text("Racines de f' : x = -1 et x = 1. Signe de 3(x-1)(x+1) :", font_size=21),
                MathTex(
                    r"""
                    \begin{array}{c|ccccccc}
                    x & -\infty & & -1 & & 1 & & +\infty \\
                    \hline
                    f'(x) & & + & 0 & - & 0 & + & \\
                    \end{array}
                    """,
                    font_size=22,
                ),
            ).arrange(DOWN, buff=0.28),
            box_width=11.4,
        )
        derivee_ex.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "On calcule d'abord la dérivée : f prime de x égale trois x "
                "carré moins trois, qui se factorise en trois fois x moins "
                "un, fois x plus un. Les racines de f prime sont donc moins "
                "un et un. Comme le coefficient trois est positif, le "
                "trinôme est positif à l'extérieur des racines, et négatif "
                "entre elles : positif sur moins l'infini, moins un, "
                "négatif sur moins un, un, et de nouveau positif sur un, "
                "plus l'infini."
            )
        ) as tracker:
            self.play(FadeIn(derivee_ex))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(derivee_ex))

        variation_ex = example_box(
            VGroup(
                Text("Tableau de variation :", font_size=21),
                MathTex(
                    r"""
                    \begin{array}{c|ccccccc}
                    x & -\infty & & -1 & & 1 & & +\infty \\
                    \hline
                    f'(x) & & + & 0 & - & 0 & + & \\
                    \hline
                    f & & \nearrow & 3 & \searrow & -1 & \nearrow & \\
                    \end{array}
                    """,
                    font_size=22,
                ),
                Text("f(-1) = -1+3+1 = 3 et f(1) = 1-3+1 = -1.", font_size=20),
            ).arrange(DOWN, buff=0.25),
            box_width=11.4,
        )
        variation_ex.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "On calcule f de moins un, qui vaut trois, et f de un, qui "
                "vaut moins un. D'après le théorème, f est donc croissante "
                "sur moins l'infini, moins un, puis décroissante sur moins "
                "un, un, puis de nouveau croissante sur un, plus l'infini. "
                "Voici le tableau de variation complet."
            )
        ) as tracker:
            self.play(FadeIn(variation_ex))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(variation_ex))

        # --- Figure de la courbe --------------------------------------------------------
        axes = Axes(
            x_range=[-2.5, 2.5, 1],
            y_range=[-3, 4, 1],
            x_length=6.2,
            y_length=4.4,
            axis_config={"include_tip": True, "stroke_width": 2, "color": WHITE},
        )
        axes.next_to(titre, DOWN, buff=0.5)
        courbe = axes.plot(lambda x: x**3 - 3 * x + 1, x_range=[-2.15, 2.15], color=YELLOW)
        dot_max = Dot(axes.c2p(-1, 3), color="#288073", radius=0.06)
        dot_min = Dot(axes.c2p(1, -1), color="#B42E41", radius=0.06)
        label_max = MathTex("(-1;3)", font_size=22).next_to(dot_max, UP, buff=0.12)
        label_min = MathTex("(1;-1)", font_size=22).next_to(dot_min, DOWN, buff=0.12)
        figure = VGroup(axes, courbe, dot_max, dot_min, label_max, label_min)

        with self.voiceover(
            text=(
                "Voici la courbe représentative de f : on voit clairement "
                "la portion croissante jusqu'au point de coordonnées moins "
                "un et trois, puis la portion décroissante jusqu'au point "
                "de coordonnées un et moins un, puis de nouveau croissante. "
                "Ces deux points remarquables, où la tangente est "
                "horizontale, sont précisément les extremums locaux de f, "
                "que nous étudierons en détail dans une prochaine scène."
            )
        ) as tracker:
            self.play(Create(axes), Create(courbe))
            self.play(FadeIn(dot_max), FadeIn(dot_min), Write(label_max), Write(label_min))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(figure))

        # --- À retenir --------------------------------------------------------------------
        retenir = essentiel_box(
            Text(
                _wrap(
                    "Étudier les variations de f = calculer f', étudier "
                    "son signe (souvent par factorisation), puis en "
                    "déduire le sens de variation grâce au théorème "
                    "fondamental. C'est la méthode centrale de ce chapitre.",
                    width=58,
                ),
                font_size=22,
            )
        )
        retenir.next_to(titre, DOWN, buff=0.6)

        with self.voiceover(
            text=(
                "À retenir : étudier les variations d'une fonction f "
                "consiste à calculer sa dérivée f prime, à étudier son "
                "signe, très souvent par factorisation, puis à en déduire "
                "le sens de variation grâce au théorème fondamental. C'est "
                "la méthode centrale que nous réutiliserons dans toutes les "
                "scènes suivantes."
            )
        ) as tracker:
            self.play(FadeIn(retenir))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(titre), FadeOut(retenir))
