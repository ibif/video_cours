"""
scenes/Maths_ExtensionNotionLimite_09.py — Chapitre 7 (1ereC, Maths), scène 09.

Position relative d'une courbe par rapport à son asymptote (méthode du
signe de d(x) = f(x) - (ax+b)), exemple résolu 10 (reprise de
f(x) = 2x+1-2/(x+1)), puis méthode du plan d'étude complet d'une fonction en
7 étapes.
Source : 1ereC/Maths.pdf, chapitre 7, pages 80-90.
"""

import textwrap

from manim import (
    DOWN,
    RIGHT,
    UP,
    WHITE,
    YELLOW,
    Axes,
    DashedLine,
    FadeIn,
    FadeOut,
    MathTex,
    Text,
    VGroup,
    Write,
)

from shapes.base_scene import NotionScene
from shapes.boxes import essentiel_box, example_box, method_box, scene_title


def _wrap(text: str, width: int = 58) -> str:
    return "\n".join(textwrap.fill(line, width=width) for line in text.split("\n"))


class PositionRelativeCourbeAsymptote(NotionScene):
    def construct(self):
        titre = scene_title("Position relative courbe / asymptote — plan d'étude")
        titre.scale(0.4)
        titre.to_edge(UP)

        # --- Énoncé ----------------------------------------------------------
        enonce = Text(
            "La courbe est-elle au-dessus ou en dessous de son asymptote ?",
            font_size=23,
            color=YELLOW,
            weight="BOLD",
        )
        enonce.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Une fois une asymptote trouvée, une question naturelle se "
                "pose : la courbe reste-t-elle au-dessus, ou en dessous, de "
                "cette asymptote ? Et de quel côté change-t-elle "
                "éventuellement de position ?"
            )
        ) as tracker:
            self.play(Write(titre))
            self.play(FadeIn(enonce))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(enonce))

        # --- Animation du raisonnement : méthode du signe de d(x) --------------
        methode_signe = method_box(
            VGroup(
                Text(
                    "Étudier le signe de d(x) = f(x) - (ax+b) :",
                    font_size=22,
                    weight="BOLD",
                ),
                MathTex(
                    r"""
                    \begin{array}{lll}
                    d(x) > 0 & \Longrightarrow & \mathcal{C}_f \text{ au-dessus de } \Delta \\
                    d(x) < 0 & \Longrightarrow & \mathcal{C}_f \text{ en dessous de } \Delta \\
                    d(x) = 0 & \Longrightarrow & \mathcal{C}_f \text{ coupe } \Delta
                    \end{array}
                    """,
                    font_size=25,
                ),
            ).arrange(DOWN, buff=0.3),
            box_width=10.5,
        )
        methode_signe.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "La méthode consiste à étudier le signe de d de x, "
                "différence entre f de x et a x plus b. Là où cette "
                "différence est strictement positive, la courbe est "
                "au-dessus de l'asymptote Delta. Là où elle est strictement "
                "négative, la courbe est en dessous. Et là où elle "
                "s'annule, la courbe traverse son asymptote."
            )
        ) as tracker:
            self.play(FadeIn(methode_signe))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(methode_signe))

        # --- Exemple résolu 10 --------------------------------------------------
        enonce_ex10 = Text(
            "Exemple 10 — position de f(x) = 2x+1 - 2/(x+1) par rapport à Δ : y = 2x+1",
            font_size=20,
            color=YELLOW,
            weight="BOLD",
        )
        enonce_ex10.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Exemple : reprenons f de x égale deux x plus un, moins "
                "deux sur x plus un, dont nous avions déjà trouvé "
                "l'asymptote oblique Delta d'équation y égale deux x plus "
                "un."
            )
        ) as tracker:
            self.play(FadeIn(enonce_ex10))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(enonce_ex10))

        calcul_d = example_box(
            MathTex(
                r"""
                d(x) = f(x)-(2x+1) = -\dfrac{2}{x+1}
                """,
                font_size=30,
            ),
            box_width=8.0,
        )
        calcul_d.next_to(titre, DOWN, buff=0.55)

        with self.voiceover(
            text=(
                "On calcule d de x, différence entre f de x et deux x plus "
                "un : il ne reste que moins deux sur x plus un, exactement "
                "le reste obtenu lors de la division euclidienne."
            )
        ) as tracker:
            self.play(FadeIn(calcul_d))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(calcul_d))

        signe_d = example_box(
            MathTex(
                r"""
                \begin{array}{l}
                \text{Si } x>-1 : \ x+1>0 \Longrightarrow d(x)<0
                \Longrightarrow \mathcal{C}_f \text{ en dessous de } \Delta \\
                \text{Si } x<-1 : \ x+1<0 \Longrightarrow d(x)>0
                \Longrightarrow \mathcal{C}_f \text{ au-dessus de } \Delta
                \end{array}
                """,
                font_size=23,
            ),
            box_width=11.3,
        )
        signe_d.next_to(titre, DOWN, buff=0.55)

        with self.voiceover(
            text=(
                "Le signe de d de x est celui de moins deux sur x plus un. "
                "Si x est supérieur à moins un, x plus un est positif, donc "
                "d de x est négatif : la courbe est en dessous de "
                "l'asymptote. Si x est inférieur à moins un, x plus un est "
                "négatif, donc d de x est positif : la courbe est "
                "au-dessus de l'asymptote. La courbe ne coupe jamais "
                "l'asymptote, puisque d de x ne s'annule jamais."
            )
        ) as tracker:
            self.play(FadeIn(signe_d))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(signe_d))

        # Figure
        axes = Axes(
            x_range=[-6, 4, 1],
            y_range=[-8, 8, 2],
            x_length=7.0,
            y_length=4.4,
            axis_config={"color": WHITE, "font_size": 15},
        )
        axes.next_to(titre, DOWN, buff=0.55)
        asymp = DashedLine(axes.c2p(-6, -11), axes.c2p(4, 9), color=YELLOW, stroke_width=2)
        branche_g = axes.plot(lambda x: 2 * x + 1 - 2 / (x + 1), x_range=[-6, -1.3], color="#1E90FF")
        branche_d = axes.plot(lambda x: 2 * x + 1 - 2 / (x + 1), x_range=[-0.75, 4], color="#1E90FF")
        figure = VGroup(axes, asymp, branche_g, branche_d)
        figure.scale(0.92)

        with self.voiceover(
            text=(
                "Sur la figure, on voit bien que la branche de gauche, "
                "avant l'asymptote verticale, reste au-dessus de la droite "
                "oblique, tandis que la branche de droite reste en dessous "
                "— conformément au signe que nous venons de trouver."
            )
        ) as tracker:
            self.play(FadeIn(figure))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(figure))

        # --- Méthode : plan d'étude complet en 7 étapes ---------------------
        plan_etude = method_box(
            MathTex(
                r"""
                \begin{array}{l}
                1. \ \text{Ensemble de définition } D_f \\
                2. \ \text{Limites aux bornes de } D_f \text{ et asymptotes} \\
                3. \ \text{Calcul de } f' \text{ et étude de son signe} \\
                4. \ \text{Tableau de variation} \\
                5. \ \text{Éléments de symétrie (parité, centre, axe)} \\
                6. \ \text{Position de } \mathcal{C}_f \text{ par rapport à ses asymptotes} \\
                7. \ \text{Tableau de valeurs et tracé de } \mathcal{C}_f
                \end{array}
                """,
                font_size=24,
            ),
            box_width=9.5,
        )
        plan_etude.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Nous disposons maintenant de tous les outils pour mener "
                "l'étude complète d'une fonction, en sept étapes bien "
                "définies. Un : déterminer l'ensemble de définition D "
                "indice f. Deux : calculer les limites aux bornes de cet "
                "ensemble, et en déduire les asymptotes. Trois : calculer "
                "la dérivée et étudier son signe. Quatre : dresser le "
                "tableau de variation. Cinq : rechercher d'éventuels "
                "éléments de symétrie, parité, centre ou axe. Six : étudier "
                "la position de la courbe par rapport à ses asymptotes. Et "
                "sept : dresser un tableau de valeurs, puis tracer la "
                "courbe."
            )
        ) as tracker:
            self.play(FadeIn(plan_etude))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(plan_etude))

        # --- À retenir -----------------------------------------------------
        retenir = essentiel_box(
            Text(
                _wrap(
                    "Position relative : signe de d(x) = f(x) - (ax+b). Plan "
                    "d'étude : Df, limites/asymptotes, dérivée/variation, "
                    "symétries, position relative, tableau de valeurs/tracé.",
                    width=58,
                ),
                font_size=22,
            )
        )
        retenir.next_to(titre, DOWN, buff=0.6)

        with self.voiceover(
            text=(
                "À retenir : la position relative se lit dans le signe de d "
                "de x, la différence entre f de x et son asymptote. Et le "
                "plan d'étude complet enchaîne toujours les mêmes sept "
                "étapes : domaine, limites et asymptotes, dérivée et "
                "variation, symétries, position relative, puis tableau de "
                "valeurs et tracé."
            )
        ) as tracker:
            self.play(FadeIn(retenir))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(titre), FadeOut(retenir))
