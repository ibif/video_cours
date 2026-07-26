"""
scenes/Maths_GeneralitesFonctions_01.py — Chapitre 3 (1ereC, Maths), scène 01.

Ensemble de définition, image et antécédent d'un élément, courbe
représentative d'une fonction numérique.
Source : 1ereC/Maths.pdf, chapitre 3, pages 28-40.
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
    Dot,
    FadeIn,
    FadeOut,
    MathTex,
    Text,
    VGroup,
    Write,
)

from shapes.base_scene import NotionScene
from shapes.boxes import definition_box, essentiel_box, example_box, scene_title, warning_box


def _wrap(text: str, width: int = 60) -> str:
    return "\n".join(textwrap.fill(line, width=width) for line in text.split("\n"))


class EnsembleDefinitionImage(NotionScene):
    def construct(self):
        titre = scene_title("Ensemble de définition — image d'un élément")
        titre.scale(0.55)
        titre.to_edge(UP)

        # --- Énoncé : fonction numérique, Df -------------------------------
        def_fonction = definition_box(
            Text(
                _wrap(
                    "Une fonction numérique f associe, à certains réels x "
                    "d'un ensemble D, un unique réel noté f(x). L'ensemble "
                    "des réels x pour lesquels f(x) existe s'appelle "
                    "l'ensemble de définition de f, noté Df.",
                    width=58,
                ),
                font_size=24,
            )
        )
        def_fonction.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Une fonction numérique f associe, à certains réels x d'un "
                "ensemble D, un unique réel noté f de x. L'ensemble des "
                "réels x pour lesquels f de x existe s'appelle l'ensemble "
                "de définition de f, noté D indice f."
            )
        ) as tracker:
            self.play(Write(titre))
            self.play(FadeIn(def_fonction))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(def_fonction))

        # --- Animation du raisonnement : règles pratiques -------------------
        regles = definition_box(
            MathTex(
                r"""
                \begin{array}{ll}
                \text{Polynôme } P(x) & D_f = \mathbb{R} \\
                {} \dfrac{u(x)}{v(x)} & D_f = \{x, \ v(x) \neq 0\} \\
                \sqrt{u(x)} & D_f = \{x, \ u(x) \geq 0\} \\
                \dfrac{\sqrt{u(x)}}{v(x)} & D_f = \{x, \ u(x)\geq 0 \text{ et } v(x)\neq 0\}
                \end{array}
                """,
                font_size=30,
            ),
            box_width=10.5,
        )
        regles.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "En pratique, on retient quatre règles : un polynôme est "
                "défini sur ℝ tout entier ; un quotient u sur v est défini "
                "là où le dénominateur v de x est différent de zéro ; une "
                "racine carrée de u de x est définie là où u de x est "
                "positif ou nul ; et pour un quotient contenant une racine "
                "carrée, on combine les deux conditions avec un « et »."
            )
        ) as tracker:
            self.play(FadeIn(regles))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(regles))

        # --- Image, antécédent, courbe représentative -----------------------
        def_image = definition_box(
            Text(
                _wrap(
                    "Si f(x) = y, on dit que y est l'image de x par f, et "
                    "que x est un antécédent de y par f. Un réel a "
                    "au plus une image, mais peut avoir plusieurs "
                    "antécédents (ou aucun).",
                    width=58,
                ),
                font_size=24,
            )
        )
        def_image.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Si f de x est égal à y, on dit que y est l'image de x par "
                "f, et que x est un antécédent de y par f. Un réel a au "
                "plus une image, mais peut avoir plusieurs antécédents, ou "
                "aucun."
            )
        ) as tracker:
            self.play(FadeIn(def_image))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(def_image))

        def_courbe = definition_box(
            MathTex(
                r"\mathcal{C}_f = \{ M(x\,;f(x)) \ / \ x \in D_f \}",
                font_size=32,
            )
        )
        def_courbe.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "La courbe représentative de f, notée C indice f, est "
                "l'ensemble des points M de coordonnées x et f de x, "
                "lorsque x décrit l'ensemble de définition Df."
            )
        ) as tracker:
            self.play(FadeIn(def_courbe))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(def_courbe))

        # --- Exemple traité 1 : calcul de trois ensembles de définition -----
        enonce_ex1 = Text(
            "Exemple 1 — déterminer les ensembles de définition de :",
            font_size=24,
            color=YELLOW,
            weight="BOLD",
        )
        enonce_ex1.next_to(titre, DOWN, buff=0.4)

        fonctions_ex1 = MathTex(
            r"f(x) = \dfrac{3x+1}{x^2-x-6} \qquad g(x) = \sqrt{5-2x} "
            r"\qquad h(x) = \dfrac{\sqrt{x+3}}{x-1}",
            font_size=28,
        )
        fonctions_ex1.next_to(enonce_ex1, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Exemple : déterminons les ensembles de définition de trois "
                "fonctions : f de x égale trois x plus un, sur x carré "
                "moins x moins six ; g de x égale racine carrée de cinq "
                "moins deux x ; et h de x égale racine carrée de x plus "
                "trois, sur x moins un."
            )
        ) as tracker:
            self.play(FadeIn(enonce_ex1))
            self.play(Write(fonctions_ex1))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(enonce_ex1), FadeOut(fonctions_ex1))

        calcul_f = example_box(
            MathTex(
                r"""
                \begin{array}{l}
                x^2 - x - 6 = 0 \ \Longrightarrow \ x = -2 \text{ ou } x = 3 \\
                D_f = \mathbb{R} \setminus \{-2\,;3\}
                \end{array}
                """,
                font_size=28,
            ),
            box_width=9.5,
        )
        calcul_f.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Pour f, le dénominateur s'annule quand x carré moins x "
                "moins six vaut zéro, c'est-à-dire pour x égale moins deux "
                "ou x égale trois. Donc Df est ℝ privé de moins deux et de "
                "trois."
            )
        ) as tracker:
            self.play(FadeIn(calcul_f))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(calcul_f))

        calcul_g = example_box(
            MathTex(
                r"""
                \begin{array}{l}
                5-2x \geq 0 \ \Longleftrightarrow \ x \leq \dfrac{5}{2} \\
                D_g = \left]-\infty\,;\dfrac{5}{2}\right]
                \end{array}
                """,
                font_size=28,
            ),
            box_width=8.5,
        )
        calcul_g.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Pour g, il faut que cinq moins deux x soit positif ou nul, "
                "ce qui équivaut à x inférieur ou égal à cinq demis. Donc "
                "Dg est l'intervalle moins infini, cinq demis, fermé à "
                "droite."
            )
        ) as tracker:
            self.play(FadeIn(calcul_g))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(calcul_g))

        calcul_h = example_box(
            MathTex(
                r"""
                \begin{array}{l}
                x+3 \geq 0 \text{ et } x-1 \neq 0 \ \Longleftrightarrow \ x \geq -3 \text{ et } x \neq 1\\
                D_h = [-3\,;1[ \, \cup \, ]1\,;+\infty[
                \end{array}
                """,
                font_size=26,
            ),
            box_width=10.5,
        )
        calcul_h.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Pour h, il faut à la fois que x plus trois soit positif "
                "ou nul, et que x moins un soit différent de zéro, "
                "c'est-à-dire x supérieur ou égal à moins trois, et x "
                "différent de un. Donc Dh est la réunion de l'intervalle "
                "moins trois, un, fermé à gauche ouvert à droite, et de "
                "l'intervalle un, plus infini."
            )
        ) as tracker:
            self.play(FadeIn(calcul_h))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(calcul_h))

        # --- Exemple traité 2 : images et antécédents -----------------------
        enonce_ex2 = Text(
            "Exemple 2 — pour f(x) = x² − 4x + 3 :",
            font_size=25,
            color=YELLOW,
            weight="BOLD",
        )
        enonce_ex2.next_to(titre, DOWN, buff=0.5)

        axes = Axes(
            x_range=[-1, 5, 1],
            y_range=[-2, 4, 1],
            x_length=5.5,
            y_length=3.5,
            axis_config={"color": WHITE, "font_size": 18},
        )
        axes.next_to(enonce_ex2, DOWN, buff=0.35).shift(LEFT * 2.6)
        courbe_f = axes.plot(lambda x: x**2 - 4 * x + 3, x_range=[-0.3, 4.3], color=YELLOW)
        points_images = VGroup(
            Dot(axes.c2p(0, 3), color=WHITE, radius=0.06),
            Dot(axes.c2p(1, 0), color=WHITE, radius=0.06),
            Dot(axes.c2p(2, -1), color=WHITE, radius=0.06),
        )
        schema = VGroup(axes, courbe_f, points_images)

        images = MathTex(
            r"""
            \begin{array}{l}
            f(0) = 3 \\
            f(1) = 0 \\
            f(2) = -1
            \end{array}
            """,
            font_size=28,
        )
        images.next_to(enonce_ex2, DOWN, buff=0.35).shift(RIGHT * 3.0)

        with self.voiceover(
            text=(
                "Reprenons f de x égale x carré moins quatre x plus trois. "
                "Les images de zéro, un et deux se calculent directement : "
                "f de zéro vaut trois, f de un vaut zéro, et f de deux vaut "
                "moins un."
            )
        ) as tracker:
            self.play(FadeIn(enonce_ex2))
            self.play(FadeIn(schema), Write(images))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(enonce_ex2), FadeOut(schema), FadeOut(images))

        antecedents = example_box(
            MathTex(
                r"""
                \begin{array}{l}
                f(x) = 3 \ \Longleftrightarrow \ x^2-4x = 0 \ \Longleftrightarrow \ x = 0 \text{ ou } x = 4 \\
                f(x) = -1 \ \Longleftrightarrow \ (x-2)^2 = 0 \ \Longleftrightarrow \ x = 2 \\
                f(x) = -2 \ \Longleftrightarrow \ x^2-4x+5=0,\ \Delta = -4 < 0 \ \Longrightarrow \ \text{pas d'antécédent}
                \end{array}
                """,
                font_size=24,
            ),
            box_width=11.2,
        )
        antecedents.next_to(titre, DOWN, buff=0.55)

        with self.voiceover(
            text=(
                "Cherchons maintenant les antécédents. Trois a pour "
                "antécédents zéro et quatre, solutions de x carré moins "
                "quatre x égale zéro. Moins un a un seul antécédent, deux, "
                "car x moins deux au carré égale zéro. Quant à moins deux, "
                "l'équation associée a un discriminant négatif, moins "
                "quatre : elle n'a donc aucun antécédent."
            )
        ) as tracker:
            self.play(FadeIn(antecedents))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(antecedents))

        # --- À retenir -------------------------------------------------------
        retenir = essentiel_box(
            Text(
                _wrap(
                    "Pour trouver Df : combiner « dénominateur ≠ 0 » et "
                    "« expression sous une racine ≥ 0 ». Un réel a au plus "
                    "une image, mais un nombre quelconque d'antécédents.",
                    width=58,
                ),
                font_size=24,
            )
        )
        retenir.next_to(titre, DOWN, buff=0.6)

        with self.voiceover(
            text=(
                "À retenir : pour trouver l'ensemble de définition, on "
                "combine systématiquement « dénominateur différent de "
                "zéro » et « expression sous une racine positive ou "
                "nulle ». Un réel a au plus une image par f, mais peut "
                "avoir zéro, un, ou plusieurs antécédents."
            )
        ) as tracker:
            self.play(FadeIn(retenir))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(retenir))

        # --- Piège à éviter ----------------------------------------------
        piege = warning_box(
            Text(
                _wrap(
                    "Piège : oublier une des conditions (dénominateur ou "
                    "racine) ou mal combiner deux conditions avec un « et » "
                    "— l'intersection, pas la réunion — donne un Df faux.",
                    width=58,
                ),
                font_size=24,
            )
        )
        piege.next_to(titre, DOWN, buff=0.6)

        with self.voiceover(
            text=(
                "Attention : oublier une des conditions, ou mal combiner "
                "deux conditions avec un « et » — c'est-à-dire prendre "
                "l'intersection et non la réunion — est l'erreur la plus "
                "fréquente sur cette notion."
            )
        ) as tracker:
            self.play(FadeIn(piege))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(titre), FadeOut(piege))
