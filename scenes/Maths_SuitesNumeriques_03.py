"""
scenes/Maths_SuitesNumeriques_03.py — Chapitre 15 « Suites numériques »
(1ereC, Maths), scène 03.

Représentation graphique d'une suite (nuage de points) et construction en
« escalier » (toile d'araignée) des termes d'une suite récurrente à l'aide
de la droite y = x. Illustration : u0 = 0, u(n+1) = 0,5 un + 2, convergence
vers le point fixe ℓ = 4.
Source : 1ereC/Maths.pdf, chapitre 15, pages 176-188.
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
    Line,
    MathTex,
    Text,
    VGroup,
    Write,
)

from shapes.base_scene import NotionScene
from shapes.boxes import definition_box, essentiel_box, method_box, scene_title, warning_box


def _wrap(text: str, width: int = 58) -> str:
    return "\n".join(textwrap.fill(line, width=width) for line in text.split("\n"))


class RepresentationGraphiqueEscalier(NotionScene):
    def construct(self):
        titre = scene_title("Représentation graphique — construction en escalier")
        titre.scale(0.44)
        titre.to_edge(UP)
        self.play(Write(titre))

        # --- Énoncé : représentation graphique --------------------------------
        definition = definition_box(
            Text(
                "La représentation graphique d'une suite (un) est l'ensemble\n"
                "des points isolés de coordonnées (n ; un), pour n entier.",
                font_size=23,
            ),
            box_width=10.8,
        )
        definition.next_to(titre, DOWN, buff=0.35)

        with self.voiceover(
            text=(
                "La représentation graphique d'une suite u indice n est "
                "l'ensemble des points de coordonnées n et u indice n, pour "
                "n entier naturel. C'est un nuage de points isolés, "
                "puisque n ne prend que des valeurs entières."
            )
        ) as tracker:
            self.play(FadeIn(definition))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(definition))

        # --- Méthode : construction en escalier -------------------------------
        methode = method_box(
            VGroup(
                Text(
                    "Pour une suite récurrente un+1 = f(un), on construit les\n"
                    "termes sur l'axe des abscisses grâce à la droite y = x :",
                    font_size=21,
                ),
                Text(
                    "1) de (un ; 0), monter jusqu'à la courbe : point (un ; f(un))",
                    font_size=19,
                ),
                Text(
                    "2) de ce point, aller horizontalement jusqu'à y = x :\n"
                    "   point (un+1 ; un+1), puisque f(un) = un+1",
                    font_size=19,
                ),
                Text(
                    "3) redescendre verticalement sur l'axe : on lit un+1",
                    font_size=19,
                ),
            ).arrange(DOWN, buff=0.2),
            box_width=11.5,
        )
        methode.next_to(titre, DOWN, buff=0.3)

        with self.voiceover(
            text=(
                "Méthode de construction en escalier, aussi appelée toile "
                "d'araignée : pour une suite récurrente, on trace la "
                "courbe de f et la droite d'équation y égale x. Première "
                "étape : depuis u indice n sur l'axe, on monte jusqu'à la "
                "courbe, ce qui donne le point d'ordonnée f de u indice n. "
                "Deuxième étape : on part horizontalement jusqu'à "
                "rencontrer la droite y égale x, puisque cette ordonnée "
                "vaut justement u indice n plus un. Troisième étape : on "
                "redescend verticalement sur l'axe des abscisses pour lire "
                "la valeur de u indice n plus un, et on recommence."
            )
        ) as tracker:
            self.play(FadeIn(methode))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(methode))

        # --- Animation du raisonnement : escalier réel --------------------------
        def f(x):
            return 0.5 * x + 2

        axes = Axes(
            x_range=[-0.5, 5, 1],
            y_range=[-0.5, 5, 1],
            x_length=6.0,
            y_length=6.0,
            axis_config={"color": WHITE, "font_size": 16},
        )
        axes.move_to(DOWN * 0.2)
        courbe_f = axes.plot(f, x_range=[-0.3, 4.8], color="#DE7C1F")
        droite_y_x = axes.plot(lambda x: x, x_range=[-0.3, 4.8], color="#288073")
        label_f = MathTex("y=0{,}5x+2", font_size=22, color="#DE7C1F")
        label_f.next_to(axes.c2p(4.6, f(4.6)), RIGHT, buff=0.1)
        label_yx = MathTex("y=x", font_size=22, color="#288073")
        label_yx.next_to(axes.c2p(4.6, 4.6), UP, buff=0.05)

        terms = [0.0]
        for _ in range(5):
            terms.append(f(terms[-1]))

        escalier = VGroup()
        for k in range(len(terms) - 1):
            un = terms[k]
            un1 = terms[k + 1]
            montee = Line(axes.c2p(un, un), axes.c2p(un, un1), color=YELLOW, stroke_width=2.5)
            horizontale = Line(axes.c2p(un, un1), axes.c2p(un1, un1), color=YELLOW, stroke_width=2.5)
            escalier.add(montee, horizontale)

        points_axe = VGroup(*[Dot(axes.c2p(t, 0), color=YELLOW, radius=0.05) for t in terms])
        point_fixe = Dot(axes.c2p(4, 4), color=WHITE, radius=0.06)
        label_fixe = MathTex(r"\ell = 4", font_size=22, color=WHITE)
        label_fixe.next_to(point_fixe, UP + RIGHT, buff=0.1)

        figure = VGroup(axes, courbe_f, droite_y_x, label_f, label_yx)

        with self.voiceover(
            text=(
                "Illustrons avec u zéro égale zéro, et u indice n plus un "
                "égale zéro virgule cinq fois u indice n, plus deux. On "
                "trace la courbe de f, en orange, et la droite y égale x, "
                "en vert."
            )
        ) as tracker:
            self.play(Create(axes))
            self.play(Create(courbe_f), Create(droite_y_x))
            self.play(FadeIn(label_f), FadeIn(label_yx))
            self.wait(tracker.get_remaining_duration())

        with self.voiceover(
            text=(
                "En partant de u zéro égale zéro et en répétant la "
                "construction en escalier, les termes se rapprochent de "
                "plus en plus du point où la courbe de f coupe la droite y "
                "égale x : ce point d'intersection est le point fixe de la "
                "suite, ici ℓ égale quatre. La suite converge vers cette "
                "valeur."
            )
        ) as tracker:
            self.play(Create(escalier), run_time=3)
            self.play(FadeIn(points_axe))
            self.play(FadeIn(point_fixe), FadeIn(label_fixe))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(figure), FadeOut(escalier), FadeOut(points_axe), FadeOut(point_fixe), FadeOut(label_fixe))

        # --- À retenir -----------------------------------------------------------
        retenir = essentiel_box(
            Text(
                _wrap(
                    "La construction en escalier (courbe de f + droite y = "
                    "x) permet de visualiser les termes d'une suite "
                    "récurrente sur l'axe des abscisses, et de deviner sa "
                    "limite éventuelle au point d'intersection.",
                    width=58,
                ),
                font_size=22,
            ),
            box_width=11.3,
        )
        retenir.next_to(titre, DOWN, buff=0.35)

        with self.voiceover(
            text=(
                "À retenir : la construction en escalier, à partir de la "
                "courbe de f et de la droite y égale x, permet de "
                "visualiser directement les termes d'une suite récurrente "
                "sur l'axe des abscisses, et de deviner graphiquement vers "
                "quelle valeur elle converge."
            )
        ) as tracker:
            self.play(FadeIn(retenir))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(retenir))

        # --- Piège à éviter ----------------------------------------------------
        piege = warning_box(
            Text(
                _wrap(
                    "Ne jamais relier les points d'une suite par une "
                    "courbe continue : seule la construction en escalier, "
                    "via la droite y = x, relie f(un) à un+1, sans jamais "
                    "tracer directement le nuage de points comme une "
                    "courbe.",
                    width=56,
                ),
                font_size=22,
            ),
            box_width=11.3,
        )
        piege.next_to(titre, DOWN, buff=0.35)

        with self.voiceover(
            text=(
                "Piège à éviter : il ne faut jamais relier les points du "
                "nuage d'une suite par une courbe continue, comme si u "
                "indice n était une fonction de la variable réelle. Seule "
                "la construction en escalier, qui passe par la droite y "
                "égale x, permet de reporter f de u indice n sur l'axe des "
                "abscisses comme u indice n plus un."
            )
        ) as tracker:
            self.play(FadeIn(piege))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(piege), FadeOut(titre))
