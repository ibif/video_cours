"""
scenes/Maths_ExtensionNotionLimite_08.py — Chapitre 7 (1ereC, Maths), scène 08.

Directions asymptotiques et branches infinies : définition de branche
infinie, théorème (admis) des 4 cas selon lim f(x)/x, exemple résolu 9 avec
trois fonctions et leurs figures.
Source : 1ereC/Maths.pdf, chapitre 7, pages 80-90.
"""

import textwrap

from manim import DOWN, LEFT, RIGHT, UP, WHITE, YELLOW, Axes, FadeIn, FadeOut, MathTex, Text, VGroup, Write

from shapes.base_scene import NotionScene
from shapes.boxes import definition_box, essentiel_box, example_box, scene_title, theorem_box


def _wrap(text: str, width: int = 58) -> str:
    return "\n".join(textwrap.fill(line, width=width) for line in text.split("\n"))


class DirectionsAsymptotiquesBranchesInfinies(NotionScene):
    def construct(self):
        titre = scene_title("Directions asymptotiques et branches infinies")
        titre.scale(0.42)
        titre.to_edge(UP)

        # --- Énoncé ----------------------------------------------------------
        enonce = Text(
            "Et quand il n'existe aucune asymptote oblique ?",
            font_size=25,
            color=YELLOW,
            weight="BOLD",
        )
        enonce.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Quand f de x et x tendent tous les deux vers l'infini, la "
                "courbe présente ce qu'on appelle une branche infinie. Mais "
                "cette branche infinie n'a pas toujours une asymptote "
                "oblique : voyons tous les cas possibles."
            )
        ) as tracker:
            self.play(Write(titre))
            self.play(FadeIn(enonce))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(enonce))

        # --- Animation du raisonnement : définition branche infinie -----------
        def_branche = definition_box(
            Text(
                _wrap(
                    "On dit que la courbe de f admet une branche infinie en "
                    "+∞ (ou -∞) lorsque x tend vers +∞ (ou -∞) et que f(x) "
                    "tend aussi vers +∞ ou -∞.",
                    width=54,
                ),
                font_size=23,
            ),
            box_width=10.5,
        )
        def_branche.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Définition : la courbe de f admet une branche infinie en "
                "plus l'infini, ou en moins l'infini, lorsque x tend vers "
                "cet infini et que f de x tend lui aussi vers plus l'infini "
                "ou moins l'infini."
            )
        ) as tracker:
            self.play(FadeIn(def_branche))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(def_branche))

        theoreme = theorem_box(
            MathTex(
                r"""
                \begin{array}{ll}
                \lim\limits_{x\to\infty} \dfrac{f(x)}{x} = 0
                & \text{parabole de direction } (Ox) \\[0.25cm]
                \lim\limits_{x\to\infty} \dfrac{f(x)}{x} = \pm\infty
                & \text{parabole de direction } (Oy) \\[0.25cm]
                \lim\limits_{x\to\infty} \dfrac{f(x)}{x} = a \in \mathbb{R}^{*}
                \text{ et } \lim\limits_{x\to\infty} \big[f(x)-ax\big] = b \in \mathbb{R}
                & \text{asymptote oblique } y=ax+b \\[0.25cm]
                \lim\limits_{x\to\infty} \dfrac{f(x)}{x} = a \in \mathbb{R}^{*}
                \text{ et } \lim\limits_{x\to\infty} \big[f(x)-ax\big] = \pm\infty
                & \text{direction asymptotique } y=ax
                \end{array}
                """,
                font_size=19,
            ),
            box_width=11.6,
        )
        theoreme.next_to(titre, DOWN, buff=0.45)

        with self.voiceover(
            text=(
                "Voici le théorème, admis, qui classe tous les cas selon la "
                "limite de f de x sur x. Si cette limite vaut zéro, la "
                "courbe présente une parabole de direction l'axe des "
                "abscisses. Si elle vaut plus ou moins l'infini, c'est une "
                "parabole de direction l'axe des ordonnées. Si elle vaut un "
                "réel a non nul, et que f de x moins a x tend vers un réel "
                "b, on retrouve l'asymptote oblique déjà étudiée. Et si "
                "elle vaut a mais que f de x moins a x est lui-même "
                "infini, on parle de direction asymptotique y égale a x, "
                "sans asymptote véritable."
            )
        ) as tracker:
            self.play(FadeIn(theoreme))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(theoreme))

        # --- Exemple résolu 9 : trois fonctions ---------------------------
        enonce_ex9 = Text(
            "Exemple 9 — nature de la branche infinie en +∞",
            font_size=25,
            color=YELLOW,
            weight="BOLD",
        )
        enonce_ex9.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Exemple : étudions la nature de la branche infinie en plus "
                "l'infini pour trois fonctions différentes."
            )
        ) as tracker:
            self.play(FadeIn(enonce_ex9))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(enonce_ex9))

        # Cas 1 : x^3 + 2/x -> parabole direction (Oy)
        cas1 = example_box(
            MathTex(
                r"""
                f(x) = x^3+\dfrac{2}{x}
                \ \Longrightarrow\
                \dfrac{f(x)}{x} = x^2+\dfrac{2}{x^2}
                \ \xrightarrow[x\to+\infty]{} \ +\infty
                \ \Longrightarrow\ \text{parabole de direction } (Oy)
                """,
                font_size=20,
            ),
            box_width=11.6,
        )
        cas1.next_to(titre, DOWN, buff=0.55)

        axes1 = Axes(x_range=[0, 2.2, 1], y_range=[0, 8, 2], x_length=3.6, y_length=2.6,
                      axis_config={"color": WHITE, "font_size": 14})
        axes1.next_to(cas1, DOWN, buff=0.3).shift(LEFT * 3.5)
        courbe1 = axes1.plot(lambda x: x**3 + 2 / x, x_range=[0.35, 1.9], color="#1E90FF")
        figure1 = VGroup(axes1, courbe1)

        with self.voiceover(
            text=(
                "Premier cas : f de x égale x au cube plus deux sur x. Le "
                "quotient f de x sur x vaut x carré plus deux sur x carré, "
                "qui tend vers plus l'infini. La courbe présente donc une "
                "parabole de direction l'axe des ordonnées : elle « monte » "
                "beaucoup plus vite que n'importe quelle droite."
            )
        ) as tracker:
            self.play(FadeIn(cas1))
            self.play(FadeIn(figure1))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(cas1), FadeOut(figure1))

        # Cas 2 : x + sqrt(x) -> direction asymptotique y = x
        cas2 = example_box(
            MathTex(
                r"""
                f(x) = x+\sqrt{x}
                \ \Longrightarrow\
                \dfrac{f(x)}{x} = 1+\dfrac{1}{\sqrt{x}} \to 1 = a
                \ ; \ f(x)-x = \sqrt{x} \to +\infty
                \ \Longrightarrow\ \text{direction asymptotique } y=x
                """,
                font_size=19,
            ),
            box_width=11.7,
        )
        cas2.next_to(titre, DOWN, buff=0.55)

        axes2 = Axes(x_range=[0, 6, 1], y_range=[0, 10, 2], x_length=3.6, y_length=2.6,
                      axis_config={"color": WHITE, "font_size": 14})
        axes2.next_to(cas2, DOWN, buff=0.3).shift(LEFT * 3.5)
        courbe2 = axes2.plot(lambda x: x + x**0.5, x_range=[0, 6], color="#1E90FF")
        droite2 = axes2.plot(lambda x: x, x_range=[0, 6], color=YELLOW)
        figure2 = VGroup(axes2, courbe2, droite2)

        with self.voiceover(
            text=(
                "Deuxième cas : f de x égale x plus racine de x. Le "
                "quotient f de x sur x tend vers un, donc a vaut un. Mais f "
                "de x moins x vaut racine de x, qui tend vers plus l'infini "
                "et non vers un réel fini. Il n'y a donc pas d'asymptote "
                "oblique, seulement une direction asymptotique y égale x : "
                "la courbe s'écarte de plus en plus de cette droite, tout "
                "en restant parallèle à elle."
            )
        ) as tracker:
            self.play(FadeIn(cas2))
            self.play(FadeIn(figure2))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(cas2), FadeOut(figure2))

        # Cas 3 : sqrt(x) -> parabole direction (Ox)
        cas3 = example_box(
            MathTex(
                r"""
                f(x) = \sqrt{x}
                \ \Longrightarrow\
                \dfrac{f(x)}{x} = \dfrac{1}{\sqrt{x}}
                \ \xrightarrow[x\to+\infty]{} \ 0
                \ \Longrightarrow\ \text{parabole de direction } (Ox)
                """,
                font_size=21,
            ),
            box_width=10.8,
        )
        cas3.next_to(titre, DOWN, buff=0.55)

        axes3 = Axes(x_range=[0, 9, 2], y_range=[0, 4, 1], x_length=3.6, y_length=2.2,
                      axis_config={"color": WHITE, "font_size": 14})
        axes3.next_to(cas3, DOWN, buff=0.3).shift(LEFT * 3.5)
        courbe3 = axes3.plot(lambda x: x**0.5, x_range=[0, 9], color="#1E90FF")
        figure3 = VGroup(axes3, courbe3)

        with self.voiceover(
            text=(
                "Troisième cas : f de x égale racine de x. Le quotient f de "
                "x sur x vaut un sur racine de x, qui tend vers zéro. La "
                "courbe présente donc une parabole de direction l'axe des "
                "abscisses : elle « monte » beaucoup plus lentement que "
                "n'importe quelle droite non horizontale."
            )
        ) as tracker:
            self.play(FadeIn(cas3))
            self.play(FadeIn(figure3))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(cas3), FadeOut(figure3))

        # --- À retenir -----------------------------------------------------
        retenir = essentiel_box(
            Text(
                _wrap(
                    "Pour classer une branche infinie : calculer d'abord "
                    "lim f(x)/x. Selon sa valeur (0, ±∞, ou réel a), affiner "
                    "avec lim [f(x) - ax] pour distinguer asymptote et "
                    "simple direction.",
                    width=58,
                ),
                font_size=22,
            )
        )
        retenir.next_to(titre, DOWN, buff=0.6)

        with self.voiceover(
            text=(
                "À retenir : pour classer une branche infinie, on calcule "
                "toujours en premier la limite de f de x sur x. Selon "
                "qu'elle vaut zéro, l'infini, ou un réel a, on affine "
                "ensuite, si besoin, avec la limite de f de x moins a x, "
                "pour distinguer une véritable asymptote oblique d'une "
                "simple direction asymptotique."
            )
        ) as tracker:
            self.play(FadeIn(retenir))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(titre), FadeOut(retenir))
