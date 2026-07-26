"""
scenes/Maths_GeneralitesFonctions_05.py — Chapitre 3 (1ereC, Maths), scène 05.

Exemple de sens de variation (fonction affine), propriétés opératoires du
sens de variation (somme, produit par une constante, inverse), et tableau
de variation.
Source : 1ereC/Maths.pdf, chapitre 3, pages 28-40.
"""

import textwrap

from manim import DOWN, LEFT, RIGHT, UP, WHITE, YELLOW, Arrow, FadeIn, FadeOut, MathTex, Text, VGroup, Write

from shapes.base_scene import NotionScene
from shapes.boxes import definition_box, essentiel_box, example_box, property_box, scene_title, warning_box


def _wrap(text: str, width: int = 60) -> str:
    return "\n".join(textwrap.fill(line, width=width) for line in text.split("\n"))


class ExempleVariationTableau(NotionScene):
    def construct(self):
        titre = scene_title("Exemple de variation — tableau de variation")
        titre.scale(0.5)
        titre.to_edge(UP)
        self.play(Write(titre))

        # --- Énoncé : exemple 6 ---------------------------------------------
        enonce_ex6 = Text(
            "Exemple 6 — f(x) = −2x + 5, par le taux de variation",
            font_size=25,
            color=YELLOW,
            weight="BOLD",
        )
        enonce_ex6.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Exemple 6 : étudions le sens de variation de f de x égale "
                "moins deux x plus cinq, à l'aide du taux de variation."
            )
        ) as tracker:
            self.play(FadeIn(enonce_ex6))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(enonce_ex6))

        # --- Animation du raisonnement ---------------------------------------
        calcul_ex6 = example_box(
            MathTex(
                r"""
                \begin{array}{l}
                \tau(a,b) = \dfrac{f(b)-f(a)}{b-a} = \dfrac{(-2b+5)-(-2a+5)}{b-a} \\[0.4em]
                = \dfrac{-2(b-a)}{b-a} = -2
                \end{array}
                """,
                font_size=28,
            ),
            box_width=9.5,
        )
        calcul_ex6.next_to(titre, DOWN, buff=0.55)

        with self.voiceover(
            text=(
                "On calcule le taux de variation entre deux réels a et b "
                "quelconques : f de b moins f de a, sur b moins a. Après "
                "simplification, tous les termes en x disparaissent et il "
                "reste exactement moins deux, une constante négative."
            )
        ) as tracker:
            self.play(FadeIn(calcul_ex6))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(calcul_ex6))

        conclusion_ex6 = example_box(
            Text(
                "τ(a,b) = −2 < 0, quels que soient a ≠ b : f est strictement décroissante sur ℝ.",
                font_size=25,
            ),
            box_width=10.5,
        )
        conclusion_ex6.next_to(titre, DOWN, buff=0.6)

        with self.voiceover(
            text=(
                "Le taux de variation est constant et strictement négatif, "
                "quels que soient a et b distincts : f est donc "
                "strictement décroissante sur ℝ tout entier — ce qui est "
                "cohérent avec le coefficient directeur négatif de cette "
                "fonction affine."
            )
        ) as tracker:
            self.play(FadeIn(conclusion_ex6))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(conclusion_ex6))

        # --- Propriétés opératoires -----------------------------------------
        proprietes = property_box(
            MathTex(
                r"""
                \begin{array}{l}
                f,g \text{ croissantes sur } I \ \Longrightarrow \ f+g \text{ croissante sur } I \\
                k>0 : \ kf \text{ même sens que } f \ ; \qquad k<0 : \ kf \text{ sens contraire de } f \\
                f \text{ de signe constant, } f \neq 0 : \ \dfrac{1}{f} \text{ varie en sens contraire de } f
                \end{array}
                """,
                font_size=24,
            ),
            box_width=11.3,
        )
        proprietes.next_to(titre, DOWN, buff=0.55)

        with self.voiceover(
            text=(
                "Propriétés opératoires utiles : la somme de deux "
                "fonctions croissantes sur un même intervalle I est "
                "croissante sur I. Pour un réel k, si k est positif, k "
                "fois f varie dans le même sens que f ; si k est négatif, "
                "k fois f varie en sens contraire. Enfin, si f garde un "
                "signe constant et ne s'annule pas, un sur f varie en sens "
                "contraire de f."
            )
        ) as tracker:
            self.play(FadeIn(proprietes))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(proprietes))

        # --- Exemple traité : tableau de variation ---------------------------
        def_tableau = definition_box(
            Text(
                _wrap(
                    "Le tableau de variation résume, sur une ligne, les "
                    "intervalles où f est croissante (flèche montante) ou "
                    "décroissante (flèche descendante), et les valeurs de "
                    "f aux bornes de ces intervalles.",
                    width=56,
                ),
                font_size=23,
            ),
            box_width=10.6,
        )
        def_tableau.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Le tableau de variation résume tout cela visuellement : "
                "sur une ligne, on indique les intervalles où f est "
                "croissante par une flèche montante, où elle est "
                "décroissante par une flèche descendante, ainsi que les "
                "valeurs prises par f aux bornes de ces intervalles."
            )
        ) as tracker:
            self.play(FadeIn(def_tableau))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(def_tableau))

        # Illustration simple d'un tableau de variation pour f(x) = x²
        ligne_x = MathTex(r"x", font_size=26)
        val_x = MathTex(r"-\infty \qquad\qquad 0 \qquad\qquad +\infty", font_size=26)
        val_x.next_to(ligne_x, RIGHT, buff=0.6)
        ligne_f = MathTex(r"x^2", font_size=26)
        ligne_f.next_to(ligne_x, DOWN, buff=0.9)
        fleche_bas = Arrow(
            val_x.get_left() + LEFT * 0.1 + DOWN * 0.9,
            val_x.get_center() + DOWN * 0.9,
            color=WHITE,
            buff=0,
            stroke_width=3,
        )
        fleche_haut = Arrow(
            val_x.get_center() + DOWN * 0.9,
            val_x.get_right() + RIGHT * 0.1 + DOWN * 0.9,
            color=WHITE,
            buff=0,
            stroke_width=3,
        )
        tableau = VGroup(ligne_x, val_x, ligne_f, fleche_bas, fleche_haut)
        tableau.move_to(titre.get_center() + DOWN * 2.5)

        with self.voiceover(
            text=(
                "Par exemple, pour f de x égale x carré : le tableau "
                "affiche une flèche descendante de moins l'infini à zéro, "
                "puis une flèche montante de zéro à plus l'infini, "
                "traduisant exactement l'étude faite précédemment."
            )
        ) as tracker:
            self.play(FadeIn(tableau))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(tableau))

        # --- À retenir ---------------------------------------------------
        retenir = essentiel_box(
            Text(
                _wrap(
                    "Un tableau de variation résume le sens de variation "
                    "sur chaque intervalle par une flèche ; il se lit de "
                    "gauche à droite comme les valeurs croissantes de x.",
                    width=56,
                ),
                font_size=24,
            ),
            box_width=10.8,
        )
        retenir.next_to(titre, DOWN, buff=0.6)

        with self.voiceover(
            text=(
                "À retenir : le tableau de variation résume le sens de "
                "variation sur chaque intervalle par une flèche montante "
                "ou descendante, et se lit toujours de gauche à droite, "
                "dans le sens des x croissants."
            )
        ) as tracker:
            self.play(FadeIn(retenir))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(retenir))

        # --- Piège à éviter ----------------------------------------------
        piege = warning_box(
            Text(
                _wrap(
                    "Piège : la somme d'une fonction croissante et d'une "
                    "fonction décroissante n'a en général AUCUN sens de "
                    "variation garanti — il faut étudier directement le "
                    "taux de variation de la somme.",
                    width=56,
                ),
                font_size=23,
            ),
            box_width=10.8,
        )
        piege.next_to(titre, DOWN, buff=0.6)

        with self.voiceover(
            text=(
                "Attention : contrairement à la somme de deux fonctions "
                "croissantes, la somme d'une fonction croissante et d'une "
                "fonction décroissante n'a, en général, aucun sens de "
                "variation garanti. Dans ce cas, il faut étudier "
                "directement le taux de variation de la somme."
            )
        ) as tracker:
            self.play(FadeIn(piege))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(titre), FadeOut(piege))
