"""
scenes/Maths_EtudeGraphiqueFonctions_07.py — Chapitre 11 (1ereC, Maths), scène 07.

Fonctions rationnelles et asymptote oblique : théorème d'existence
(deg numérateur = deg dénominateur + 1) par division euclidienne, exemple
résolu complet f(x) = (x²-3x+3)/(x-2).
Source : 1ereC/Maths.pdf, chapitre 11, pages 130-141.
"""

import textwrap

from manim import DOWN, LEFT, RIGHT, UP, WHITE, YELLOW, Axes, DashedLine, Dot, FadeIn, FadeOut, MathTex, Text, VGroup, Write

from shapes.base_scene import NotionScene
from shapes.boxes import essentiel_box, example_box, scene_title, theorem_box, warning_box


def _wrap(text: str, width: int = 58) -> str:
    return "\n".join(textwrap.fill(line, width=width) for line in text.split("\n"))


class FonctionsRationnellesAsymptoteOblique(NotionScene):
    def construct(self):
        titre = scene_title("Fonctions rationnelles et asymptote oblique")
        titre.scale(0.46)
        titre.to_edge(UP)

        # --- Énoncé ------------------------------------------------------------
        enonce = Text(
            "Quand une fonction rationnelle a-t-elle une asymptote oblique ?",
            font_size=24,
            color=YELLOW,
            weight="BOLD",
        )
        enonce.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Troisième famille : les fonctions rationnelles générales, "
                "quotients de deux polynômes. Voyons à quelle condition "
                "leur courbe admet une asymptote oblique."
            )
        ) as tracker:
            self.play(Write(titre))
            self.play(FadeIn(enonce))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(enonce))

        # --- Théorème existence asymptote oblique --------------------------
        theo_existence = theorem_box(
            Text(
                _wrap(
                    "Pour f = N/D avec N, D polynômes : Cf admet une "
                    "asymptote oblique en ±∞ si et seulement si "
                    "deg(N) = deg(D) + 1.",
                    width=56,
                ),
                font_size=23,
            ),
            box_width=10.6,
        )
        theo_existence.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Théorème : pour une fonction f égale N sur D, quotient de "
                "deux polynômes, la courbe admet une asymptote oblique en "
                "plus ou moins l'infini si et seulement si le degré du "
                "numérateur est exactement égal au degré du dénominateur, "
                "plus un."
            )
        ) as tracker:
            self.play(FadeIn(theo_existence))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(theo_existence))

        methode_division = example_box(
            MathTex(
                r"\text{Division euclidienne : } N(x) = D(x)\times(ax+b) + r"
                r"\ \Longrightarrow \ f(x) = ax+b+\dfrac{r}{D(x)}",
                font_size=26,
            ),
            box_width=11.4,
        )
        methode_division.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "On obtient a et b par division euclidienne de N de x par D "
                "de x : N de x égale D de x, fois a x plus b, plus un reste "
                "r constant. On en déduit f de x égale a x plus b, plus r "
                "sur D de x, ce dernier terme tendant vers zéro à l'infini."
            )
        ) as tracker:
            self.play(FadeIn(methode_division))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(methode_division))

        # --- Exemple résolu complet : f(x) = (x²-3x+3)/(x-2) --------------------
        enonce_ex = Text(
            "Exemple résolu — f(x) = (x²-3x+3)/(x-2)",
            font_size=27,
            color=YELLOW,
            weight="BOLD",
        )
        enonce_ex.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Étudions complètement f de x égale x carré moins trois x "
                "plus trois, sur x moins deux. Le numérateur est de degré "
                "deux, le dénominateur de degré un : une asymptote oblique "
                "est donc attendue."
            )
        ) as tracker:
            self.play(FadeIn(enonce_ex))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(enonce_ex))

        etape_domaine = example_box(
            MathTex(
                r"D_f = \mathbb{R} \setminus \{2\} \qquad "
                r"\lim_{x\to 2^{-}} f(x) = -\infty \qquad \lim_{x\to 2^{+}} f(x) = +\infty",
                font_size=24,
            ),
            box_width=11.6,
        )
        etape_domaine.next_to(titre, DOWN, buff=0.55)

        with self.voiceover(
            text=(
                "Domaine : ℝ privé de deux. En deux, le numérateur tend "
                "vers un, non nul, donc les limites latérales sont "
                "infinies : x égale deux est asymptote verticale."
            )
        ) as tracker:
            self.play(FadeIn(etape_domaine))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(etape_domaine))

        etape_division = example_box(
            MathTex(
                r"""
                x^2-3x+3 = (x-2)(x-1) + 1
                \ \Longrightarrow \
                f(x) = (x-1) + \dfrac{1}{x-2}
                """,
                font_size=26,
            ),
            box_width=10.8,
        )
        etape_division.next_to(titre, DOWN, buff=0.55)

        with self.voiceover(
            text=(
                "La division euclidienne donne x carré moins trois x plus "
                "trois égale x moins deux, fois x moins un, plus un. Donc f "
                "de x égale x moins un, plus un sur x moins deux, ce "
                "dernier terme tendant vers zéro à l'infini : la droite y "
                "égale x moins un est asymptote oblique."
            )
        ) as tracker:
            self.play(FadeIn(etape_division))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(etape_division))

        etape_derivee = example_box(
            MathTex(
                r"""
                f'(x) = \dfrac{(2x-3)(x-2)-(x^2-3x+3)}{(x-2)^2}
                = \dfrac{x^2-4x+3}{(x-2)^2}
                = \dfrac{(x-1)(x-3)}{(x-2)^2}
                """,
                font_size=23,
            ),
            box_width=11.6,
        )
        etape_derivee.next_to(titre, DOWN, buff=0.55)

        with self.voiceover(
            text=(
                "La dérivée se calcule avec la formule du quotient : après "
                "simplification, f prime de x égale x moins un, fois x "
                "moins trois, sur x moins deux au carré. Le dénominateur "
                "étant toujours positif, le signe de f prime est celui du "
                "produit x moins un, fois x moins trois."
            )
        ) as tracker:
            self.play(FadeIn(etape_derivee))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(etape_derivee))

        tableau_ex = MathTex(
            r"""
            \begin{array}{c|ccccccccc}
            x & -\infty & & 1 & & 2 & & 3 & & +\infty \\
            \hline
            f'(x) & & + & 0 & - & \| & - & 0 & + & \\
            \hline
            f(x) & & \nearrow & -1 & \searrow & \| & \searrow & 3 & \nearrow &
            \end{array}
            """,
            font_size=18,
        )
        tableau_ex.next_to(titre, DOWN, buff=0.6)

        with self.voiceover(
            text=(
                "Le tableau de variation présente trois valeurs "
                "remarquables : un, où f prime s'annule en changeant de "
                "signe positif à négatif, un maximum local de moins un ; "
                "deux, valeur exclue avec double barre ; et trois, où f "
                "prime s'annule en changeant de signe négatif à positif, "
                "un minimum local de trois."
            )
        ) as tracker:
            self.play(FadeIn(tableau_ex))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(tableau_ex))

        etape_symetrie = example_box(
            MathTex(r"\Omega(2\,;1) \text{ centre de symétrie de } C_f", font_size=28),
            box_width=8.0,
        )
        etape_symetrie.next_to(titre, DOWN, buff=0.55)

        with self.voiceover(
            text=(
                "Le point oméga de coordonnées deux et un — intersection "
                "de l'asymptote verticale x égale deux et de l'asymptote "
                "oblique y égale x moins un, calculée en x égale deux — est "
                "centre de symétrie de la courbe."
            )
        ) as tracker:
            self.play(FadeIn(etape_symetrie))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(etape_symetrie))

        # --- Tracé de la courbe ------------------------------------------------
        axes = Axes(
            x_range=[-2, 6, 1], y_range=[-2, 8, 2], x_length=7.0, y_length=4.5,
            axis_config={"color": WHITE, "font_size": 16},
        )
        axes.move_to(titre.get_center() + DOWN * 3.5)

        def f(x):
            return (x**2 - 3 * x + 3) / (x - 2)

        courbe_gauche = axes.plot(f, x_range=[-1.6, 1.85], color="#1E90FF")
        courbe_droite = axes.plot(f, x_range=[2.15, 5.6], color="#1E90FF")
        asym_v = DashedLine(axes.c2p(2, -2), axes.c2p(2, 8), color=YELLOW)
        asym_o = axes.plot(lambda x: x - 1, x_range=[-2, 6], color=YELLOW)
        pt_omega = Dot(axes.c2p(2, 1), color="#B42E41")
        schema = VGroup(axes, courbe_gauche, courbe_droite, asym_v, asym_o, pt_omega)

        with self.voiceover(
            text=(
                "Voici le tracé final, avec ses deux asymptotes en "
                "pointillés jaunes et son centre de symétrie oméga en "
                "rouge."
            )
        ) as tracker:
            self.play(FadeIn(schema))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(schema))

        # --- À retenir ---------------------------------------------------------
        retenir = essentiel_box(
            Text(
                _wrap(
                    "Asymptote oblique ⟺ deg(N) = deg(D) + 1. On l'obtient "
                    "par division euclidienne : f(x) = (ax+b) + r/D(x). "
                    "Étudier ensuite f'(x) sur chaque intervalle de Df "
                    "comme pour un quotient classique.",
                    width=58,
                ),
                font_size=22,
            ),
            box_width=11.2,
        )
        retenir.next_to(titre, DOWN, buff=0.6)

        with self.voiceover(
            text=(
                "À retenir : l'asymptote oblique existe exactement quand "
                "le degré du numérateur dépasse celui du dénominateur "
                "d'une unité. On l'obtient toujours par division "
                "euclidienne, puis on étudie la dérivée comme pour un "
                "quotient classique, intervalle par intervalle."
            )
        ) as tracker:
            self.play(FadeIn(retenir))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(retenir))

        # --- Piège à éviter ------------------------------------------------
        piege = warning_box(
            Text(
                _wrap(
                    "Piège : la courbe ne coupe JAMAIS son asymptote "
                    "verticale, mais elle PEUT couper son asymptote "
                    "oblique — résoudre f(x) = ax+b pour vérifier, ne "
                    "jamais l'exclure par principe.",
                    width=58,
                ),
                font_size=22,
            ),
            box_width=11.0,
        )
        piege.next_to(titre, DOWN, buff=0.6)

        with self.voiceover(
            text=(
                "Piège important : la courbe ne coupe jamais son asymptote "
                "verticale, puisque f n'y est pas définie. Mais elle peut "
                "parfaitement couper son asymptote oblique — il faut "
                "résoudre f de x égale a x plus b pour vérifier, jamais "
                "exclure cette possibilité par principe."
            )
        ) as tracker:
            self.play(FadeIn(piege))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(titre), FadeOut(piege))
