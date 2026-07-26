"""
scenes/Maths_EquationsInequationsSecondDegre_06.py — Chapitre 1 (1ereC,
Maths), scène 06.

Interprétation graphique : la parabole représentant y = ax² + bx + c selon
le signe de a, son sommet, le lien entre les racines et les points
d'intersection avec l'axe des abscisses (deux figures : signe lu sur la
parabole pour a > 0, Δ > 0 ; puis les trois positions Δ > 0 / Δ = 0 / Δ < 0).
Source : 1ereC/Maths.pdf, chapitre 1, pages 4-13.
"""

from manim import (
    BLUE,
    DOWN,
    GREEN,
    LEFT,
    ORANGE,
    RED,
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
from shapes.boxes import scene_title


def _mini_axes(x_range=(-3, 5, 1), y_range=(-3, 5, 1), size=3.2):
    ax = Axes(
        x_range=list(x_range),
        y_range=list(y_range),
        x_length=size,
        y_length=size,
        axis_config={"include_tip": False, "stroke_width": 2, "color": WHITE},
    )
    return ax


class InterpretationGraphiqueParabole(NotionScene):
    def construct(self):
        titre = scene_title("Interprétation graphique")
        titre.scale(0.65)
        titre.to_edge(UP)
        self.play(Write(titre))

        # --- Énoncé : la courbe représentative -----------------------------
        enonce = Text(
            "La courbe de y = ax² + bx + c est une parabole,\n"
            "tournée vers le haut si a > 0, vers le bas si a < 0.",
            font_size=26,
        )
        enonce.next_to(titre, DOWN, buff=0.4)
        sommet = MathTex(
            r"\text{Sommet } S\left(-\dfrac{b}{2a}\, ;\, -\dfrac{\Delta}{4a}\right)",
            font_size=30,
        )
        sommet.next_to(enonce, DOWN, buff=0.35)

        with self.voiceover(
            text=(
                "La représentation graphique de la fonction y égale a x "
                "carré plus b x plus c est une parabole. Elle est tournée "
                "vers le haut si a est positif, vers le bas si a est "
                "négatif. Son sommet a pour coordonnées moins b sur deux "
                "a, et moins delta sur quatre a — c'est exactement le "
                "point qui apparaît dans la forme canonique."
            )
        ) as tracker:
            self.play(FadeIn(enonce))
            self.play(Write(sommet))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(enonce), FadeOut(sommet))

        # --- Animation du raisonnement : figure 1, signe lu sur la parabole ---
        ax1 = Axes(
            x_range=[-1, 5, 1],
            y_range=[-3, 3, 1],
            x_length=6.5,
            y_length=4.2,
            axis_config={"include_tip": True, "stroke_width": 2, "color": WHITE},
        )
        ax1.next_to(titre, DOWN, buff=0.5).shift(LEFT * 2.3)

        # a > 0, Δ > 0, racines en x = 1 et x = 3.5
        courbe1 = ax1.plot(lambda x: 0.6 * (x - 1) * (x - 3.5), x_range=[-0.3, 4.7], color=BLUE)
        x1_dot = Dot(ax1.c2p(1, 0), color=YELLOW)
        x2_dot = Dot(ax1.c2p(3.5, 0), color=YELLOW)
        x1_label = MathTex("x_1", font_size=26, color=YELLOW).next_to(x1_dot, DOWN, buff=0.15)
        x2_label = MathTex("x_2", font_size=26, color=YELLOW).next_to(x2_dot, DOWN, buff=0.15)

        signe_moins = MathTex("-", font_size=34, color=RED).move_to(ax1.c2p(2.25, -0.9))
        signe_plus_g = MathTex("+", font_size=34, color=GREEN).move_to(ax1.c2p(0.1, 1.1))
        signe_plus_d = MathTex("+", font_size=34, color=GREEN).move_to(ax1.c2p(4.4, 1.1))

        legende1 = VGroup(
            Text("Cas a > 0, Δ > 0 :", font_size=24, color=YELLOW),
            Text("+ au-dessus de l'axe, − en-dessous.", font_size=22),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.15)
        legende1.next_to(ax1, RIGHT, buff=0.6).shift(UP * 0.5)

        with self.voiceover(
            text=(
                "Regardons le cas a strictement positif, delta strictement "
                "positif. La parabole coupe l'axe des abscisses en deux "
                "points, x un et x deux, qui sont exactement les racines "
                "du trinôme. Là où la courbe est au-dessus de l'axe, le "
                "trinôme est positif ; là où elle est en-dessous, entre "
                "les deux racines, le trinôme est négatif. On retrouve "
                "exactement le tableau de signe étudié précédemment, mais "
                "cette fois lu directement sur le graphique."
            )
        ) as tracker:
            self.play(Create(ax1))
            self.play(Create(courbe1))
            self.play(FadeIn(x1_dot), FadeIn(x2_dot), Write(x1_label), Write(x2_label))
            self.play(
                Write(signe_moins), Write(signe_plus_g), Write(signe_plus_d), FadeIn(legende1)
            )
            self.wait(tracker.get_remaining_duration())

        figure1 = VGroup(
            ax1, courbe1, x1_dot, x2_dot, x1_label, x2_label,
            signe_moins, signe_plus_g, signe_plus_d, legende1,
        )
        self.play(FadeOut(figure1))

        # --- Exemple traité : les trois positions selon Δ ----------------------
        entete = Text("Les trois positions possibles de la parabole (a > 0) :", font_size=24, color=YELLOW)
        entete.next_to(titre, DOWN, buff=0.4)

        # On positionne d'abord les trois repères (avant de tracer les
        # courbes) pour que les courbes, calculées via c2p à partir des
        # repères déjà en place, restent alignées avec eux.
        axA = _mini_axes()
        axB = _mini_axes()
        axC = _mini_axes()
        figure2_axes = VGroup(axA, axB, axC).arrange(RIGHT, buff=0.9)
        figure2_axes.next_to(entete, DOWN, buff=0.7)

        # Δ > 0 : deux racines distinctes
        courbeA = axA.plot(lambda x: 0.5 * (x - 0.5) * (x - 2.5), x_range=[-1.3, 3.7], color=BLUE)
        dotA1 = Dot(axA.c2p(0.5, 0), color=YELLOW, radius=0.06)
        dotA2 = Dot(axA.c2p(2.5, 0), color=YELLOW, radius=0.06)
        labelA = MathTex(r"\Delta > 0", font_size=26).next_to(axA, DOWN, buff=0.3)

        # Δ = 0 : racine double
        courbeB = axB.plot(lambda x: 0.5 * (x - 1) ** 2, x_range=[-1.3, 3.7], color=BLUE)
        dotB = Dot(axB.c2p(1, 0), color=YELLOW, radius=0.06)
        labelB = MathTex(r"\Delta = 0", font_size=26).next_to(axB, DOWN, buff=0.3)

        # Δ < 0 : aucune racine réelle
        courbeC = axC.plot(lambda x: 0.5 * (x - 1) ** 2 + 1, x_range=[-1.3, 3.7], color=BLUE)
        labelC = MathTex(r"\Delta < 0", font_size=26).next_to(axC, DOWN, buff=0.3)

        with self.voiceover(
            text=(
                "Voici les trois positions possibles de la parabole par "
                "rapport à l'axe des abscisses, dans le cas où a est "
                "positif. Quand delta est strictement positif, la "
                "parabole traverse l'axe en deux points distincts : deux "
                "racines. Quand delta est nul, elle touche l'axe en un "
                "seul point, le sommet : une racine double. Quand delta "
                "est strictement négatif, la parabole reste entièrement "
                "au-dessus de l'axe : aucune racine réelle."
            )
        ) as tracker:
            self.play(FadeIn(entete))
            self.play(Create(axA), Create(axB), Create(axC))
            self.play(Create(courbeA), Create(courbeB), Create(courbeC))
            self.play(
                FadeIn(dotA1), FadeIn(dotA2), FadeIn(dotB),
                Write(labelA), Write(labelB), Write(labelC),
            )
            self.wait(tracker.get_remaining_duration())

        # --- À retenir -----------------------------------------------------------
        self.play(
            FadeOut(entete), FadeOut(axA), FadeOut(axB), FadeOut(axC),
            FadeOut(courbeA), FadeOut(courbeB), FadeOut(courbeC),
            FadeOut(dotA1), FadeOut(dotA2), FadeOut(dotB),
            FadeOut(labelA), FadeOut(labelB), FadeOut(labelC),
        )

        retenir = Text(
            "À retenir : les racines du trinôme sont les abscisses des\n"
            "points d'intersection de la parabole avec l'axe des abscisses.",
            font_size=26,
        )
        retenir.next_to(titre, DOWN, buff=0.8)

        with self.voiceover(
            text=(
                "À retenir : les racines du trinôme sont exactement les "
                "abscisses des points où la parabole coupe l'axe des "
                "abscisses. Le nombre de ces points d'intersection, zéro, "
                "un ou deux, est directement donné par le signe de delta."
            )
        ) as tracker:
            self.play(FadeIn(retenir))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(titre), FadeOut(retenir))
