"""
scenes/Maths_ExtensionNotionLimite_07.py — Chapitre 7 (1ereC, Maths), scène 07.

Asymptote oblique : définition, interprétation graphique (distance NM → 0),
méthode de la division euclidienne pour une fraction rationnelle, méthode du
calcul de a puis b par limites. Exemple résolu 8 sur (2x²+3x-1)/(x+1).
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
from shapes.boxes import definition_box, essentiel_box, example_box, method_box, scene_title


def _wrap(text: str, width: int = 58) -> str:
    return "\n".join(textwrap.fill(line, width=width) for line in text.split("\n"))


class AsymptoteOblique(NotionScene):
    def construct(self):
        titre = scene_title("Asymptote oblique")
        titre.scale(0.5)
        titre.to_edge(UP)

        # --- Énoncé ----------------------------------------------------------
        enonce = Text(
            "Et si la courbe s'approche d'une droite... ni verticale, ni horizontale ?",
            font_size=22,
            color=YELLOW,
            weight="BOLD",
        )
        enonce.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Nous avons vu les asymptotes verticales et horizontales. "
                "Mais une courbe peut aussi s'approcher indéfiniment d'une "
                "droite oblique, ni verticale ni horizontale. C'est ce "
                "troisième type d'asymptote que nous étudions maintenant."
            )
        ) as tracker:
            self.play(Write(titre))
            self.play(FadeIn(enonce))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(enonce))

        # --- Animation du raisonnement : définition ----------------------------
        definition = definition_box(
            VGroup(
                Text(
                    _wrap(
                        "La droite d'équation y = ax + b (a ≠ 0) est "
                        "asymptote oblique à la courbe de f au voisinage de "
                        "+∞ (ou -∞) si :",
                        width=54,
                    ),
                    font_size=21,
                ),
                MathTex(
                    r"\lim_{x \to +\infty} \big[f(x)-(ax+b)\big] = 0"
                    r"\quad \text{(ou en } -\infty \text{)}",
                    font_size=25,
                ),
            ).arrange(DOWN, buff=0.3),
            box_width=10.8,
        )
        definition.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Définition : la droite d'équation y égale a x plus b, avec "
                "a différent de zéro, est asymptote oblique à la courbe de "
                "f au voisinage de plus l'infini, ou de moins l'infini, si "
                "la limite de f de x moins la quantité a x plus b vaut "
                "zéro."
            )
        ) as tracker:
            self.play(FadeIn(definition))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(definition))

        # Interprétation graphique : distance NM -> 0
        axes = Axes(
            x_range=[-1, 6, 1],
            y_range=[-1, 8, 1],
            x_length=6.0,
            y_length=4.2,
            axis_config={"color": WHITE, "font_size": 18},
        )
        axes.next_to(titre, DOWN, buff=0.5)
        droite = axes.plot(lambda x: x + 1, x_range=[-1, 6], color=YELLOW)
        courbe = axes.plot(lambda x: x + 1 + 3 / (x + 1.4), x_range=[-0.3, 6], color="#1E90FF")
        x0 = 4.3
        point_m = Dot(axes.c2p(x0, x0 + 1 + 3 / (x0 + 1.4)), color="#1E90FF", radius=0.06)
        point_n = Dot(axes.c2p(x0, x0 + 1), color=YELLOW, radius=0.06)
        segment_mn = Line(point_m.get_center(), point_n.get_center(), color=WHITE, stroke_width=2)
        label_m = MathTex("M", font_size=22, color="#1E90FF").next_to(point_m, RIGHT, buff=0.1)
        label_n = MathTex("N", font_size=22, color=YELLOW).next_to(point_n, DOWN, buff=0.1)
        figure_interp = VGroup(axes, droite, courbe, point_m, point_n, segment_mn, label_m, label_n)

        interpretation = MathTex(
            r"M(x\,;f(x)) \in \mathcal{C}_f, \quad N(x\,;ax+b) \in \Delta"
            r"\quad \Longrightarrow \quad MN \to 0 \text{ quand } x \to +\infty",
            font_size=22,
        )
        interpretation.next_to(figure_interp, DOWN, buff=0.35)

        with self.voiceover(
            text=(
                "Interprétation graphique : pour un x donné, notons M le "
                "point de la courbe d'abscisse x, et N le point de la "
                "droite Delta de même abscisse. Dire que la droite est "
                "asymptote oblique, c'est dire que la distance M N tend "
                "vers zéro quand x tend vers plus l'infini : la courbe "
                "colle de plus en plus à la droite, sans forcément la "
                "toucher."
            )
        ) as tracker:
            self.play(FadeIn(figure_interp))
            self.play(Write(interpretation))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(figure_interp), FadeOut(interpretation))

        # --- Méthode : division euclidienne -------------------------------
        methode_division = method_box(
            VGroup(
                Text(
                    "Pour une fraction rationnelle P(x)/Q(x) avec deg P = "
                    "deg Q + 1 : effectuer la division euclidienne de P par Q",
                    font_size=20,
                    weight="BOLD",
                ),
                MathTex(
                    r"P(x) = Q(x)(ax+b) + R(x)"
                    r"\ \Longrightarrow\ "
                    r"\dfrac{P(x)}{Q(x)} = (ax+b) + \dfrac{R(x)}{Q(x)}",
                    font_size=25,
                ),
                Text(
                    "avec deg R < deg Q, donc R(x)/Q(x) → 0 en ±∞.",
                    font_size=19,
                ),
            ).arrange(DOWN, buff=0.3),
            box_width=11.2,
        )
        methode_division.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Première méthode, la plus directe pour une fraction "
                "rationnelle : on effectue la division euclidienne de P par "
                "Q. On écrit P de x égale Q de x, fois a x plus b, plus un "
                "reste R de x. En divisant par Q de x, on obtient f de x "
                "égale a x plus b, plus R de x sur Q de x, ce dernier "
                "quotient tendant vers zéro en plus ou moins l'infini, car "
                "le degré du reste est strictement inférieur à celui de Q."
            )
        ) as tracker:
            self.play(FadeIn(methode_division))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(methode_division))

        methode_ab = method_box(
            VGroup(
                Text(
                    "Méthode générale : calculer a puis b par limites",
                    font_size=21,
                    weight="BOLD",
                ),
                MathTex(
                    r"a = \lim_{x\to\pm\infty} \dfrac{f(x)}{x}"
                    r"\qquad\qquad "
                    r"b = \lim_{x\to\pm\infty} \big[f(x)-ax\big]",
                    font_size=25,
                ),
            ).arrange(DOWN, buff=0.3),
            box_width=10.5,
        )
        methode_ab.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Méthode plus générale, valable même sans fraction "
                "rationnelle : on calcule d'abord a comme la limite de f de "
                "x sur x, puis, une fois a connu, on calcule b comme la "
                "limite de f de x moins a x. Cette méthode servira dans la "
                "prochaine scène pour les branches infinies."
            )
        ) as tracker:
            self.play(FadeIn(methode_ab))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(methode_ab))

        # --- Exemple résolu 8 --------------------------------------------------
        enonce_ex8 = Text(
            "Exemple 8 — asymptote oblique de f(x) = (2x²+3x-1)/(x+1)",
            font_size=22,
            color=YELLOW,
            weight="BOLD",
        )
        enonce_ex8.next_to(titre, DOWN, buff=0.5)

        fonction_ex8 = MathTex(r"f(x) = \dfrac{2x^2+3x-1}{x+1}", font_size=30)
        fonction_ex8.next_to(enonce_ex8, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Exemple : déterminons l'asymptote oblique de f de x égale "
                "deux x carré plus trois x moins un, sur x plus un. Le "
                "degré du numérateur vaut deux, celui du dénominateur vaut "
                "un : la division euclidienne s'impose."
            )
        ) as tracker:
            self.play(FadeIn(enonce_ex8))
            self.play(Write(fonction_ex8))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(enonce_ex8), FadeOut(fonction_ex8))

        division_ex8 = example_box(
            MathTex(
                r"""
                2x^2+3x-1 = (x+1)(2x+1) - 2
                \quad \Longrightarrow \quad
                f(x) = 2x+1 - \dfrac{2}{x+1}
                """,
                font_size=27,
            ),
            box_width=11.0,
        )
        division_ex8.next_to(titre, DOWN, buff=0.55)

        with self.voiceover(
            text=(
                "La division euclidienne de deux x carré plus trois x moins "
                "un par x plus un donne un quotient deux x plus un, et un "
                "reste moins deux. On peut donc écrire f de x égale deux x "
                "plus un, moins deux sur x plus un."
            )
        ) as tracker:
            self.play(FadeIn(division_ex8))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(division_ex8))

        conclusion_ex8 = example_box(
            MathTex(
                r"""
                \lim_{x\to\pm\infty} \left(-\dfrac{2}{x+1}\right) = 0
                \quad \Longrightarrow \quad
                y = 2x+1 \text{ est asymptote oblique en } +\infty \text{ et } -\infty
                """,
                font_size=23,
            ),
            box_width=11.6,
        )
        conclusion_ex8.next_to(titre, DOWN, buff=0.55)

        with self.voiceover(
            text=(
                "Comme moins deux sur x plus un tend vers zéro en plus "
                "l'infini comme en moins l'infini, la droite d'équation y "
                "égale deux x plus un est asymptote oblique à la courbe, "
                "dans les deux directions infinies."
            )
        ) as tracker:
            self.play(FadeIn(conclusion_ex8))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(conclusion_ex8))

        # Figure de l'exemple 8
        axes8 = Axes(
            x_range=[-6, 5, 1],
            y_range=[-8, 10, 2],
            x_length=7.0,
            y_length=4.6,
            axis_config={"color": WHITE, "font_size": 16},
        )
        axes8.next_to(titre, DOWN, buff=0.55)
        asymp_oblique = DashedLine(
            axes8.c2p(-6, 2 * (-6) + 1), axes8.c2p(5, 2 * 5 + 1), color=YELLOW, stroke_width=2
        )
        asymp_v8 = DashedLine(axes8.c2p(-1, -8), axes8.c2p(-1, 10), color="#FF6666", stroke_width=2)
        branche_g8 = axes8.plot(lambda x: (2 * x**2 + 3 * x - 1) / (x + 1), x_range=[-6, -1.2], color="#1E90FF")
        branche_d8 = axes8.plot(lambda x: (2 * x**2 + 3 * x - 1) / (x + 1), x_range=[-0.75, 5], color="#1E90FF")
        figure8 = VGroup(axes8, asymp_oblique, asymp_v8, branche_g8, branche_d8)
        figure8.scale(0.92)

        with self.voiceover(
            text=(
                "Sur la figure, on observe la courbe de f qui longe de plus "
                "en plus près la droite oblique y égale deux x plus un, "
                "aussi bien à gauche qu'à droite du domaine, tout en "
                "gardant aussi une asymptote verticale en x égale moins un."
            )
        ) as tracker:
            self.play(FadeIn(figure8))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(figure8))

        # --- À retenir -----------------------------------------------------
        retenir = essentiel_box(
            Text(
                _wrap(
                    "y = ax+b est asymptote oblique si lim[f(x)-(ax+b)] = 0. "
                    "Fraction rationnelle : division euclidienne. Cas "
                    "général : a = lim f(x)/x, puis b = lim [f(x) - ax].",
                    width=58,
                ),
                font_size=22,
            )
        )
        retenir.next_to(titre, DOWN, buff=0.6)

        with self.voiceover(
            text=(
                "À retenir : la droite y égale a x plus b est asymptote "
                "oblique si la limite de f de x moins a x plus b vaut zéro. "
                "Pour une fraction rationnelle, la division euclidienne "
                "donne directement a et b. Dans le cas général, on calcule "
                "a comme limite de f de x sur x, puis b comme limite de f "
                "de x moins a x."
            )
        ) as tracker:
            self.play(FadeIn(retenir))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(titre), FadeOut(retenir))
