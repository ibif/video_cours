"""
scenes/Maths_LimitesContinuite_01.py — Chapitre 5 « Limites et continuité »
(1ereC, Maths), scène 01.

Limite en +∞ / -∞ (infinie et finie), asymptote horizontale.
Source : 1ereC/Maths.pdf, chapitre 5, pages 52-65.
"""

import textwrap

from manim import (
    DOWN,
    LEFT,
    RIGHT,
    UP,
    WHITE,
    YELLOW,
    DashedLine,
    FadeIn,
    FadeOut,
    MathTex,
    Text,
    VGroup,
    Write,
)

from shapes.base_scene import NotionScene
from shapes.boxes import definition_box, essentiel_box, scene_title, warning_box


def _wrap(text: str, width: int = 58) -> str:
    return "\n".join(textwrap.fill(line, width=width) for line in text.split("\n"))


class LimiteInfinieEtAsymptoteHorizontale(NotionScene):
    def construct(self):
        titre = scene_title("Limite en +∞ / -∞ — asymptote horizontale")
        titre.scale(0.5)
        titre.to_edge(UP)
        self.play(Write(titre))

        # --- Énoncé : trois définitions --------------------------------------
        def_infinie = definition_box(
            VGroup(
                MathTex(r"\lim_{x\to+\infty} f(x) = +\infty", font_size=30),
                Text(
                    _wrap(
                        "f(x) devient aussi grand que l'on veut dès que x "
                        "est assez grand.",
                        width=52,
                    ),
                    font_size=22,
                ),
            ).arrange(DOWN, buff=0.25),
            box_width=9.5,
        )
        def_infinie.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Première définition : on dit que f de x tend vers plus "
                "l'infini quand x tend vers plus l'infini si f de x devient "
                "aussi grand que l'on veut, dès que x est pris assez grand."
            )
        ) as tracker:
            self.play(FadeIn(def_infinie))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(def_infinie))

        def_finie = definition_box(
            VGroup(
                MathTex(r"\lim_{x\to+\infty} f(x) = \ell", font_size=30),
                Text(
                    _wrap(
                        "f(x) se rapproche d'un réel ℓ d'aussi près que "
                        "l'on veut dès que x est assez grand.",
                        width=52,
                    ),
                    font_size=22,
                ),
            ).arrange(DOWN, buff=0.25),
            box_width=9.5,
        )
        def_finie.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Deuxième définition : on dit que f de x tend vers un réel "
                "ℓ quand x tend vers plus l'infini si f de x se rapproche "
                "de ℓ d'aussi près que l'on veut, dès que x est pris assez "
                "grand. On définit de la même façon les limites quand x "
                "tend vers moins l'infini."
            )
        ) as tracker:
            self.play(FadeIn(def_finie))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(def_finie))

        def_asymptote = definition_box(
            Text(
                _wrap(
                    "Si lim f(x) = ℓ (en +∞ ou en -∞), la droite d'équation "
                    "y = ℓ est asymptote horizontale à la courbe de f.",
                    width=54,
                ),
                font_size=24,
            ),
            box_width=10.5,
        )
        def_asymptote.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Troisième définition : lorsque la limite de f en plus ou "
                "moins l'infini est un réel ℓ, la droite d'équation y égale "
                "ℓ est appelée asymptote horizontale à la courbe "
                "représentative de f : la courbe se rapproche de cette "
                "droite sans jamais forcément la toucher."
            )
        ) as tracker:
            self.play(FadeIn(def_asymptote))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(def_asymptote))

        # --- Animation du raisonnement : figure -------------------------------
        from manim import Axes

        axes = Axes(
            x_range=[0.3, 8, 1],
            y_range=[0, 3, 1],
            x_length=6.5,
            y_length=3.5,
            axis_config={"color": WHITE, "font_size": 18},
        )
        courbe = axes.plot(lambda x: 1 + 1 / x, x_range=[0.35, 8], color=YELLOW)
        asymptote = DashedLine(
            axes.c2p(0.3, 1), axes.c2p(8, 1), color="#B42E41"
        )
        label_l = MathTex("y = \\ell", font_size=26, color="#B42E41")
        label_l.next_to(axes.c2p(8, 1), UP, buff=0.15)
        figure = VGroup(axes, courbe, asymptote, label_l)
        figure.move_to(DOWN * 0.3)

        with self.voiceover(
            text=(
                "Regardons une courbe qui illustre cela : quand x devient "
                "très grand, la courbe se rapproche de plus en plus près de "
                "la droite horizontale d'équation y égale ℓ, sans jamais la "
                "traverser. Cette droite est l'asymptote horizontale de la "
                "courbe en plus l'infini."
            )
        ) as tracker:
            self.play(FadeIn(figure))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(figure))

        # --- Exemple traité ----------------------------------------------------
        exemple_titre = Text(
            "Exemple — f(x) = 1 + 1/x en +∞ :", font_size=25, color=YELLOW, weight="BOLD"
        )
        exemple_titre.next_to(titre, DOWN, buff=0.4)
        exemple_calc = MathTex(
            r"\lim_{x\to+\infty} \dfrac{1}{x} = 0 \ \Longrightarrow\ "
            r"\lim_{x\to+\infty} \left(1+\dfrac{1}{x}\right) = 1",
            font_size=28,
        )
        exemple_calc.next_to(exemple_titre, DOWN, buff=0.4)
        exemple_concl = MathTex(
            r"\text{La droite } y=1 \text{ est asymptote horizontale en } +\infty",
            font_size=26,
        )
        exemple_concl.next_to(exemple_calc, DOWN, buff=0.35)

        with self.voiceover(
            text=(
                "Exemple : soit f de x égale un plus un sur x. Comme un sur "
                "x tend vers zéro quand x tend vers plus l'infini, f de x "
                "tend vers un. La droite d'équation y égale un est donc "
                "asymptote horizontale à la courbe de f en plus l'infini."
            )
        ) as tracker:
            self.play(FadeIn(exemple_titre))
            self.play(Write(exemple_calc))
            self.play(FadeIn(exemple_concl))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(exemple_titre), FadeOut(exemple_calc), FadeOut(exemple_concl))

        # --- À retenir -----------------------------------------------------------
        retenir = essentiel_box(
            Text(
                _wrap(
                    "Limite finie en l'infini = asymptote horizontale. "
                    "Une fonction peut tendre vers +∞, -∞, ou une limite "
                    "finie ℓ, en +∞ comme en -∞, indépendamment l'une de "
                    "l'autre.",
                    width=56,
                ),
                font_size=23,
            ),
            box_width=11.0,
        )
        retenir.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "À retenir : une limite finie en l'infini se traduit "
                "toujours par une asymptote horizontale. Le comportement en "
                "plus l'infini et en moins l'infini sont deux études "
                "indépendantes : rien n'oblige les deux limites à être "
                "égales, ni même à exister toutes les deux."
            )
        ) as tracker:
            self.play(FadeIn(retenir))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(retenir))

        # --- Pièges à éviter -------------------------------------------------
        piege = warning_box(
            Text(
                _wrap(
                    "Quand elle existe, la limite est unique. Les fonctions "
                    "sinus et cosinus n'ont pas de limite en +∞ ni en -∞ "
                    "(elles oscillent). Parler de limite en +∞ n'a de sens "
                    "que si le domaine de f n'est pas majoré (idem en -∞, "
                    "non minoré).",
                    width=56,
                ),
                font_size=22,
            ),
            box_width=11.2,
        )
        piege.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Attention à trois pièges. D'abord, quand elle existe, la "
                "limite d'une fonction en un point donné est unique. "
                "Ensuite, sinus et cosinus n'ont pas de limite en plus ou "
                "moins l'infini, car ils oscillent perpétuellement entre "
                "moins un et un. Enfin, chercher une limite en plus "
                "l'infini n'a de sens que si le domaine de définition de f "
                "n'est pas majoré."
            )
        ) as tracker:
            self.play(FadeIn(piege))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(piege), FadeOut(titre))
