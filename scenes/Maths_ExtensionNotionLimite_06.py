"""
scenes/Maths_ExtensionNotionLimite_06.py — Chapitre 7 (1ereC, Maths), scène 06.

Asymptote verticale et asymptote horizontale : définitions, interprétations
graphiques, exemple résolu complet avec figure sur f(x) = (2x-3)/(x+1).
Source : 1ereC/Maths.pdf, chapitre 7, pages 80-90.
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
    DashedLine,
    FadeIn,
    FadeOut,
    MathTex,
    Text,
    VGroup,
    Write,
)

from shapes.base_scene import NotionScene
from shapes.boxes import definition_box, essentiel_box, example_box, scene_title


def _wrap(text: str, width: int = 58) -> str:
    return "\n".join(textwrap.fill(line, width=width) for line in text.split("\n"))


class AsymptoteVerticaleHorizontale(NotionScene):
    def construct(self):
        titre = scene_title("Asymptote verticale et asymptote horizontale")
        titre.scale(0.46)
        titre.to_edge(UP)

        # --- Énoncé ----------------------------------------------------------
        enonce = Text(
            "Comment traduire une limite infinie en droite « asymptote » ?",
            font_size=24,
            color=YELLOW,
            weight="BOLD",
        )
        enonce.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Nous savons maintenant calculer des limites infinies, en "
                "un point ou à l'infini. Voyons comment ces limites se "
                "traduisent graphiquement par des droites particulières, "
                "appelées asymptotes."
            )
        ) as tracker:
            self.play(Write(titre))
            self.play(FadeIn(enonce))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(enonce))

        # --- Animation du raisonnement : définitions ---------------------------
        def_verticale = definition_box(
            VGroup(
                Text(
                    _wrap(
                        "Si f(x) tend vers +∞ ou -∞ quand x tend vers x₀ (à "
                        "gauche, à droite, ou des deux côtés), on dit que la "
                        "droite d'équation x = x₀ est asymptote verticale à "
                        "la courbe de f.",
                        width=54,
                    ),
                    font_size=21,
                ),
                MathTex(
                    r"\lim_{x \to x_0} f(x) = \pm\infty"
                    r"\ \Longrightarrow\ x = x_0 \text{ asymptote verticale}",
                    font_size=24,
                ),
            ).arrange(DOWN, buff=0.3),
            box_width=11.0,
        )
        def_verticale.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Première définition : si f de x tend vers plus l'infini ou "
                "moins l'infini quand x tend vers x zéro, que ce soit à "
                "gauche, à droite, ou des deux côtés, on dit que la droite "
                "d'équation x égale x zéro est asymptote verticale à la "
                "courbe de f. Graphiquement, la courbe se rapproche "
                "indéfiniment de cette droite verticale sans jamais la "
                "toucher."
            )
        ) as tracker:
            self.play(FadeIn(def_verticale))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(def_verticale))

        def_horizontale = definition_box(
            VGroup(
                Text(
                    _wrap(
                        "Si f(x) tend vers un réel L quand x tend vers +∞ "
                        "(ou -∞), on dit que la droite d'équation y = L est "
                        "asymptote horizontale à la courbe de f, au "
                        "voisinage de +∞ (ou -∞).",
                        width=54,
                    ),
                    font_size=21,
                ),
                MathTex(
                    r"\lim_{x \to \pm\infty} f(x) = L"
                    r"\ \Longrightarrow\ y = L \text{ asymptote horizontale}",
                    font_size=24,
                ),
            ).arrange(DOWN, buff=0.3),
            box_width=11.0,
        )
        def_horizontale.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Seconde définition : si f de x tend vers un réel L quand x "
                "tend vers plus l'infini, ou vers moins l'infini, on dit "
                "que la droite d'équation y égale L est asymptote "
                "horizontale à la courbe de f, au voisinage de l'infini "
                "correspondant. La courbe se rapproche alors de cette "
                "droite horizontale, sans forcément l'atteindre."
            )
        ) as tracker:
            self.play(FadeIn(def_horizontale))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(def_horizontale))

        # --- Exemple résolu 7 --------------------------------------------------
        enonce_ex7 = Text(
            "Exemple 7 — asymptotes de f(x) = (2x - 3)/(x + 1)",
            font_size=25,
            color=YELLOW,
            weight="BOLD",
        )
        enonce_ex7.next_to(titre, DOWN, buff=0.5)

        fonction_ex7 = MathTex(r"f(x) = \dfrac{2x-3}{x+1}", font_size=32)
        fonction_ex7.next_to(enonce_ex7, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Exemple : déterminons toutes les asymptotes de f de x "
                "égale deux x moins trois, sur x plus un."
            )
        ) as tracker:
            self.play(FadeIn(enonce_ex7))
            self.play(Write(fonction_ex7))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(enonce_ex7), FadeOut(fonction_ex7))

        asymptote_verticale_ex7 = example_box(
            MathTex(
                r"""
                \begin{array}{l}
                D_f = \mathbb{R}\setminus\{-1\}, \quad
                \text{numérateur en } -1 : \ 2(-1)-3 = -5 \neq 0 \\[0.2cm]
                \lim_{x \to -1^{-}} f(x) = \dfrac{-5}{0^{-}} = +\infty
                \qquad
                \lim_{x \to -1^{+}} f(x) = \dfrac{-5}{0^{+}} = -\infty
                \end{array}
                """,
                font_size=23,
            ),
            box_width=11.6,
        )
        asymptote_verticale_ex7.next_to(titre, DOWN, buff=0.55)

        with self.voiceover(
            text=(
                "Le dénominateur s'annule en moins un, et le numérateur en "
                "moins un vaut moins cinq, non nul. La limite à gauche en "
                "moins un vaut moins cinq sur zéro moins, soit plus "
                "l'infini ; la limite à droite vaut moins cinq sur zéro "
                "plus, soit moins l'infini. La droite x égale moins un est "
                "donc asymptote verticale."
            )
        ) as tracker:
            self.play(FadeIn(asymptote_verticale_ex7))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(asymptote_verticale_ex7))

        asymptote_horizontale_ex7 = example_box(
            MathTex(
                r"""
                \lim_{x\to+\infty} \dfrac{2x-3}{x+1} = \lim_{x\to+\infty} \dfrac{2x}{x} = 2
                \qquad
                \lim_{x\to-\infty} \dfrac{2x-3}{x+1} = 2
                """,
                font_size=25,
            ),
            box_width=11.4,
        )
        asymptote_horizontale_ex7.next_to(titre, DOWN, buff=0.55)

        with self.voiceover(
            text=(
                "En plus l'infini comme en moins l'infini, f de x a même "
                "limite que deux x sur x, c'est-à-dire deux. La droite y "
                "égale deux est donc asymptote horizontale à la courbe, "
                "aussi bien en plus l'infini qu'en moins l'infini."
            )
        ) as tracker:
            self.play(FadeIn(asymptote_horizontale_ex7))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(asymptote_horizontale_ex7))

        # --- Figure -----------------------------------------------------------
        axes = Axes(
            x_range=[-6, 6, 1],
            y_range=[-4, 6, 1],
            x_length=7.5,
            y_length=4.5,
            axis_config={"color": WHITE, "font_size": 18},
        )
        axes.next_to(titre, DOWN, buff=0.55)

        asymp_v = DashedLine(
            axes.c2p(-1, -4), axes.c2p(-1, 6), color=YELLOW, stroke_width=2
        )
        asymp_h = DashedLine(
            axes.c2p(-6, 2), axes.c2p(6, 2), color=YELLOW, stroke_width=2
        )
        branche_gauche = axes.plot(
            lambda x: (2 * x - 3) / (x + 1), x_range=[-6, -1.35], color="#1E90FF"
        )
        branche_droite = axes.plot(
            lambda x: (2 * x - 3) / (x + 1), x_range=[-0.7, 6], color="#1E90FF"
        )
        label_v = MathTex("x=-1", font_size=22, color=YELLOW).next_to(
            axes.c2p(-1, 6), UP, buff=0.1
        )
        label_h = MathTex("y=2", font_size=22, color=YELLOW).next_to(
            axes.c2p(6, 2), RIGHT, buff=0.1
        )
        figure = VGroup(axes, asymp_v, asymp_h, branche_gauche, branche_droite, label_v, label_h)
        figure.scale(0.95)

        with self.voiceover(
            text=(
                "Voici l'allure de la courbe : elle s'approche "
                "indéfiniment de la droite verticale x égale moins un, en "
                "partant vers plus l'infini d'un côté, et vers moins "
                "l'infini de l'autre. Et loin de l'origine, la courbe se "
                "rapproche de la droite horizontale y égale deux, aussi "
                "bien à gauche qu'à droite."
            )
        ) as tracker:
            self.play(FadeIn(axes))
            self.play(FadeIn(asymp_v), FadeIn(asymp_h), Write(label_v), Write(label_h))
            self.play(FadeIn(branche_gauche), FadeIn(branche_droite))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(figure))

        # --- À retenir -----------------------------------------------------
        retenir = essentiel_box(
            Text(
                _wrap(
                    "Limite infinie en x₀ (fini) → asymptote verticale "
                    "x = x₀. Limite finie L en ±∞ → asymptote horizontale "
                    "y = L. Une même courbe peut avoir les deux à la fois.",
                    width=58,
                ),
                font_size=23,
            )
        )
        retenir.next_to(titre, DOWN, buff=0.6)

        with self.voiceover(
            text=(
                "À retenir : une limite infinie en un point fini x zéro "
                "donne une asymptote verticale d'équation x égale x zéro. "
                "Une limite finie L en plus ou moins l'infini donne une "
                "asymptote horizontale d'équation y égale L. Une même "
                "courbe peut très bien posséder les deux types "
                "d'asymptotes à la fois, comme dans notre exemple."
            )
        ) as tracker:
            self.play(FadeIn(retenir))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(titre), FadeOut(retenir))
