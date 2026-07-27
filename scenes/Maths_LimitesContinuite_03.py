"""
scenes/Maths_LimitesContinuite_03.py — Chapitre 5 « Limites et continuité »
(1ereC, Maths), scène 03.

Tableau des limites de référence : en l'infini (xⁿ, 1/xⁿ, √x, 1/√x,
sin/cos sans limite) et en un point (1/x, 1/x², 1/√x, ax+b, sin, cos).
Source : 1ereC/Maths.pdf, chapitre 5, pages 52-65.
"""

import textwrap

from manim import DOWN, UP, FadeIn, FadeOut, MathTex, Text, VGroup, Write

from shapes.base_scene import NotionScene
from shapes.boxes import property_box, scene_title, warning_box


def _wrap(text: str, width: int = 58) -> str:
    return "\n".join(textwrap.fill(line, width=width) for line in text.split("\n"))


class LimitesDeReference(NotionScene):
    def construct(self):
        titre = scene_title("Limites de référence")
        titre.scale(0.6)
        titre.to_edge(UP)

        intro = Text(
            _wrap(
                "Certaines limites, très fréquentes, doivent être connues "
                "par cœur : elles servent de point de départ à tous les "
                "calculs de limites.",
                width=56,
            ),
            font_size=24,
        )
        intro.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Avant de calculer des limites plus compliquées, il faut "
                "connaître par cœur un petit nombre de limites de "
                "référence, qui serviront de brique de base à tous les "
                "calculs."
            )
        ) as tracker:
            self.play(Write(titre))
            self.play(FadeIn(intro))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(intro))

        # --- Tableau 1 : limites en l'infini -----------------------------------
        tab_infini_titre = Text("En l'infini (n entier ≥ 1) :", font_size=24, color="#288073", weight="BOLD")
        tab_infini_titre.next_to(titre, DOWN, buff=0.35)

        tab_infini = MathTex(
            r"""
            \begin{array}{|c|c|c|}
            \hline
            f(x) & \text{en } +\infty & \text{en } -\infty \\
            \hline
            x^n & +\infty & +\infty \text{ (n pair)},\ -\infty \text{ (n impair)}\\
            \dfrac{1}{x^n} & 0 & 0 \\
            \sqrt{x} & +\infty & \text{(non défini)} \\
            \dfrac{1}{\sqrt{x}} & 0 & \text{(non défini)} \\
            \sin x,\ \cos x & \text{pas de limite} & \text{pas de limite} \\
            \hline
            \end{array}
            """,
            font_size=22,
        )
        tab_infini.next_to(tab_infini_titre, DOWN, buff=0.3)
        tab_infini_box = property_box(VGroup(tab_infini), box_width=11.5)
        tab_infini_box.next_to(tab_infini_titre, DOWN, buff=0.25)

        with self.voiceover(
            text=(
                "En l'infini, on retient : x puissance n tend vers plus "
                "l'infini en plus l'infini ; en moins l'infini, cela dépend "
                "de la parité de n. Un sur x puissance n tend toujours vers "
                "zéro. Racine de x tend vers plus l'infini en plus "
                "l'infini, et n'est pas définie en moins l'infini. Un sur "
                "racine de x tend vers zéro en plus l'infini. Enfin, sinus "
                "et cosinus n'ont pas de limite, ni en plus ni en moins "
                "l'infini."
            )
        ) as tracker:
            self.play(FadeIn(tab_infini_titre))
            self.play(FadeIn(tab_infini_box))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(tab_infini_titre), FadeOut(tab_infini_box))

        # --- Tableau 2 : limites en un point x0 ---------------------------------
        tab_point_titre = Text("En un point x0 :", font_size=24, color="#288073", weight="BOLD")
        tab_point_titre.next_to(titre, DOWN, buff=0.35)

        tab_point = MathTex(
            r"""
            \begin{array}{|c|c|}
            \hline
            f(x) & \lim_{x\to x_0} f(x) \\
            \hline
            \dfrac{1}{x} \ (x_0=0) & +\infty \text{ à droite},\ -\infty \text{ à gauche} \\
            \dfrac{1}{x^2} \ (x_0=0) & +\infty \\
            \dfrac{1}{\sqrt{x}} \ (x_0=0) & +\infty \\
            ax+b & a x_0 + b \\
            \sin x,\ \cos x & \sin x_0,\ \cos x_0 \\
            \hline
            \end{array}
            """,
            font_size=22,
        )
        tab_point_box = property_box(VGroup(tab_point), box_width=11.5)
        tab_point_box.next_to(tab_point_titre, DOWN, buff=0.25)

        with self.voiceover(
            text=(
                "En un point x zéro, on retient : un sur x, en zéro, tend "
                "vers plus l'infini à droite et moins l'infini à gauche. Un "
                "sur x carré et un sur racine de x tendent vers plus "
                "l'infini en zéro. Une fonction affine a x plus b tend vers "
                "a x zéro plus b. Enfin, sinus et cosinus, qui sont "
                "continues sur ℝ, tendent simplement vers sinus de x zéro "
                "et cosinus de x zéro."
            )
        ) as tracker:
            self.play(FadeIn(tab_point_titre))
            self.play(FadeIn(tab_point_box))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(tab_point_titre), FadeOut(tab_point_box))

        # --- À retenir / piège --------------------------------------------------
        piege = warning_box(
            Text(
                _wrap(
                    "Pour 1/x en 0, la limite dépend du côté (gauche ou "
                    "droite) : sans précision, on ne peut pas parler « de "
                    "la » limite en 0.",
                    width=54,
                ),
                font_size=22,
            ),
            box_width=10.5,
        )
        piege.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Point de vigilance : pour un sur x en zéro, le signe de la "
                "limite dépend entièrement du côté par lequel on approche "
                "zéro. Sans précision du signe de x, on ne peut pas parler "
                "d'une limite unique en zéro."
            )
        ) as tracker:
            self.play(FadeIn(piege))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(piege), FadeOut(titre))
