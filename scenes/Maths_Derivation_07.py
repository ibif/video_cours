"""
scenes/Maths_Derivation_07.py — Chapitre 9 (1ereC, Maths), scène 07.

Fonction dérivée f' : définition, remarque sur la distinction f'(a) nombre
/ f' fonction, tableau complet des dérivées usuelles (k, x, x², xⁿ, 1/x,
√x, sin x, cos x) avec domaines de validité.
Source : 1ereC/Maths.pdf, chapitre 9, pages 105-117.
"""

import textwrap

from manim import DOWN, UP, FadeIn, FadeOut, MathTex, Text, VGroup, Write, YELLOW

from shapes.base_scene import NotionScene
from shapes.boxes import definition_box, essentiel_box, scene_title, warning_box


def _wrap(text: str, width: int = 58) -> str:
    return "\n".join(textwrap.fill(line, width=width) for line in text.split("\n"))


class FonctionDeriveeTableauUsuelles(NotionScene):
    def construct(self):
        titre = scene_title("Fonction dérivée — dérivées usuelles")
        titre.scale(0.5)
        titre.to_edge(UP)

        # --- Énoncé ------------------------------------------------------------
        enonce = Text(
            _wrap(
                "Si f est dérivable en chaque point d'un intervalle I, on "
                "peut associer à chaque a de I le nombre f'(a). On obtient "
                "ainsi une nouvelle fonction.",
                width=56,
            ),
            font_size=24,
            color=YELLOW,
        )
        enonce.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Jusqu'ici, nous avons calculé le nombre dérivé en un point "
                "précis. Mais si f est dérivable en chaque point d'un "
                "intervalle I, on peut associer à chaque réel a de I le "
                "nombre f prime de a : on obtient ainsi une nouvelle "
                "fonction, définie sur I tout entier."
            )
        ) as tracker:
            self.play(Write(titre))
            self.play(FadeIn(enonce))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(enonce))

        # --- Définition ----------------------------------------------------------
        definition = definition_box(
            VGroup(
                Text(
                    "Si f est dérivable en tout point d'un intervalle I,\n"
                    "on définit la fonction dérivée de f, notée f', par :",
                    font_size=22,
                ),
                MathTex(r"f' : x \longmapsto f'(x)", font_size=30),
            ).arrange(DOWN, buff=0.3),
            box_width=9.4,
        )
        definition.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Voici la définition : si f est dérivable en tout point "
                "d'un intervalle I, on appelle fonction dérivée de f, notée "
                "f prime, la fonction qui à tout x de I associe le nombre "
                "dérivé f prime de x."
            )
        ) as tracker:
            self.play(FadeIn(definition))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(definition))

        # --- Remarque : distinction f'(a) nombre / f' fonction ----------------------
        remarque = warning_box(
            Text(
                _wrap(
                    "Ne pas confondre : f'(a) est un NOMBRE (la valeur "
                    "de la dérivée en a), alors que f' est une FONCTION "
                    "(définie sur tout l'intervalle I).",
                    width=54,
                ),
                font_size=23,
            ),
            box_width=10.6,
        )
        remarque.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Remarque importante à bien fixer : il ne faut pas "
                "confondre f prime de a, qui est un nombre, la valeur de la "
                "dérivée au point précis a, avec f prime tout court, qui "
                "est une fonction, définie sur tout l'intervalle I."
            )
        ) as tracker:
            self.play(FadeIn(remarque))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(remarque))

        # --- Tableau des dérivées usuelles -------------------------------------------
        entete_tableau = Text("Tableau des dérivées usuelles :", font_size=24, color=YELLOW)
        entete_tableau.next_to(titre, DOWN, buff=0.4)

        tableau = MathTex(
            r"""
            \begin{array}{|l|l|l|}
            \hline
            f(x) & f'(x) & \text{sur} \\
            \hline
            k \ (\text{constante}) & 0 & \mathbb{R} \\
            x & 1 & \mathbb{R} \\
            x^2 & 2x & \mathbb{R} \\
            x^n \ (n \geq 1) & n\,x^{n-1} & \mathbb{R} \\
            \dfrac{1}{x} & -\dfrac{1}{x^2} & \mathbb{R}^* \\
            \sqrt{x} & \dfrac{1}{2\sqrt{x}} & \left]0;+\infty\right[ \\
            \sin x & \cos x & \mathbb{R} \\
            \cos x & -\sin x & \mathbb{R} \\
            \hline
            \end{array}
            """,
            font_size=27,
        )
        tableau.next_to(entete_tableau, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Voici le tableau des dérivées usuelles, à connaître par "
                "cœur. La dérivée d'une constante k est nulle. La dérivée "
                "de x est un. La dérivée de x carré est deux x. Plus "
                "généralement, la dérivée de x puissance n, pour n entier "
                "supérieur ou égal à un, est n fois x puissance n moins un. "
                "La dérivée de un sur x est moins un sur x carré, sur "
                "l'ensemble des réels privé de zéro. La dérivée de racine "
                "de x est un sur deux racine de x, uniquement sur les "
                "réels strictement positifs. Enfin, la dérivée de sinus x "
                "est cosinus x, et la dérivée de cosinus x est moins "
                "sinus x, sur l'ensemble des réels."
            )
        ) as tracker:
            self.play(FadeIn(entete_tableau))
            self.play(Write(tableau))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(entete_tableau), FadeOut(tableau))

        # --- À retenir -----------------------------------------------------------------
        retenir = essentiel_box(
            Text(
                _wrap(
                    "La fonction dérivée f' associe à tout x de I le "
                    "nombre f'(x). Les dérivées de k, x, xⁿ, 1/x, √x, "
                    "sin x, cos x sont à connaître par cœur, avec leur "
                    "domaine de validité (attention à 1/x et √x).",
                    width=58,
                ),
                font_size=22,
            )
        )
        retenir.next_to(titre, DOWN, buff=0.6)

        with self.voiceover(
            text=(
                "À retenir : la fonction dérivée f prime associe à chaque x "
                "de l'intervalle I le nombre f prime de x. Le tableau des "
                "dérivées usuelles est à connaître par cœur, avec une "
                "attention particulière aux domaines de validité, "
                "notamment pour un sur x et racine de x, qui ne sont pas "
                "définis, ou pas dérivables, partout."
            )
        ) as tracker:
            self.play(FadeIn(retenir))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(titre), FadeOut(retenir))
