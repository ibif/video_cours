"""
scenes/Maths_LimitesContinuite_02.py — Chapitre 5 « Limites et continuité »
(1ereC, Maths), scène 02.

Limite en un point x0, asymptote verticale, limite à gauche / à droite,
théorème d'existence de la limite. Exemple résolu 1 et contre-exemple
(partie entière).
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
from shapes.boxes import definition_box, example_box, property_box, scene_title, theorem_box, warning_box


def _wrap(text: str, width: int = 58) -> str:
    return "\n".join(textwrap.fill(line, width=width) for line in text.split("\n"))


class LimiteEnUnPointEtLimitesLaterales(NotionScene):
    def construct(self):
        titre = scene_title("Limite en un point — limites à gauche / à droite")
        titre.scale(0.48)
        titre.to_edge(UP)
        self.play(Write(titre))

        # --- Énoncé : limite infinie en x0, asymptote verticale ---------------
        def_infinie = definition_box(
            VGroup(
                MathTex(r"\lim_{x\to x_0} f(x) = +\infty", font_size=28),
                Text(
                    _wrap(
                        "f(x) devient aussi grand que l'on veut dès que x "
                        "est assez proche de x0.",
                        width=50,
                    ),
                    font_size=21,
                ),
            ).arrange(DOWN, buff=0.25),
            box_width=9.5,
        )
        def_infinie.next_to(titre, DOWN, buff=0.35)

        with self.voiceover(
            text=(
                "On dit que f de x tend vers plus l'infini quand x tend "
                "vers x zéro si f de x devient aussi grand que l'on veut, "
                "dès que x est assez proche de x zéro."
            )
        ) as tracker:
            self.play(FadeIn(def_infinie))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(def_infinie))

        def_asymptote_v = definition_box(
            Text(
                _wrap(
                    "Si lim f(x) = ±∞ quand x tend vers x0, la droite "
                    "d'équation x = x0 est asymptote verticale à la courbe.",
                    width=52,
                ),
                font_size=23,
            ),
            box_width=10.5,
        )
        def_asymptote_v.next_to(titre, DOWN, buff=0.35)

        with self.voiceover(
            text=(
                "Quand f de x tend vers plus ou moins l'infini lorsque x "
                "tend vers x zéro, la droite verticale d'équation x égale "
                "x zéro est asymptote verticale à la courbe représentative "
                "de f."
            )
        ) as tracker:
            self.play(FadeIn(def_asymptote_v))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(def_asymptote_v))

        prop_continue = property_box(
            MathTex(
                r"\text{Si } x_0 \in D_f \text{ et } \lim_{x\to x_0} f(x) \text{ existe, alors } "
                r"\lim_{x\to x_0} f(x) = f(x_0)",
                font_size=24,
            ),
            box_width=11.0,
        )
        prop_continue.next_to(titre, DOWN, buff=0.35)

        with self.voiceover(
            text=(
                "Propriété admise : si x zéro appartient au domaine de "
                "définition de f et que la limite de f en x zéro existe, "
                "alors cette limite est nécessairement égale à f de x "
                "zéro : la valeur de la fonction et sa limite coïncident."
            )
        ) as tracker:
            self.play(FadeIn(prop_continue))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(prop_continue))

        # --- Limites à gauche / à droite + théorème d'existence ---------------
        def_laterales = definition_box(
            VGroup(
                MathTex(r"\lim_{x\to x_0^{-}} f(x) \quad (x<x_0)", font_size=27),
                MathTex(r"\lim_{x\to x_0^{+}} f(x) \quad (x>x_0)", font_size=27),
            ).arrange(DOWN, buff=0.25),
            box_width=8.5,
        )
        def_laterales.next_to(titre, DOWN, buff=0.35)

        with self.voiceover(
            text=(
                "On définit aussi la limite à gauche de x zéro, en ne "
                "considérant que les x inférieurs à x zéro, et la limite à "
                "droite de x zéro, en ne considérant que les x supérieurs à "
                "x zéro."
            )
        ) as tracker:
            self.play(FadeIn(def_laterales))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(def_laterales))

        theo_existence = theorem_box(
            MathTex(
                r"\lim_{x\to x_0} f(x) \text{ existe} \ \Longleftrightarrow\ "
                r"\lim_{x\to x_0^{-}} f(x) = \lim_{x\to x_0^{+}} f(x)",
                font_size=27,
            ),
            box_width=10.5,
        )
        theo_existence.next_to(titre, DOWN, buff=0.35)

        with self.voiceover(
            text=(
                "Théorème : la limite de f en x zéro existe si et seulement "
                "si les limites à gauche et à droite existent et sont "
                "égales. Dans ce cas, la limite commune est la limite de f "
                "en x zéro."
            )
        ) as tracker:
            self.play(FadeIn(theo_existence))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(theo_existence))

        # --- Exemple résolu 1 : f(x) = |x-1|/(x-1) ------------------------------
        ex1_titre = Text(
            "Exemple 1 — f(x) = |x-1| / (x-1) en x0 = 1 :",
            font_size=24,
            color=YELLOW,
            weight="BOLD",
        )
        ex1_titre.next_to(titre, DOWN, buff=0.35)
        ex1_calc = MathTex(
            r"""
            \begin{array}{l}
            x>1 : |x-1|=x-1 \ \Rightarrow\ f(x)=1 \ \Rightarrow\ \lim_{x\to 1^{+}} f(x)=1\\
            x<1 : |x-1|=1-x \ \Rightarrow\ f(x)=-1 \ \Rightarrow\ \lim_{x\to 1^{-}} f(x)=-1
            \end{array}
            """,
            font_size=25,
        )
        ex1_calc.next_to(ex1_titre, DOWN, buff=0.35)
        ex1_concl = MathTex(
            r"-1 \neq 1 \ \Longrightarrow\ \lim_{x\to 1} f(x) \text{ n'existe pas}",
            font_size=27,
            color="#B42E41",
        )
        ex1_concl.next_to(ex1_calc, DOWN, buff=0.3)

        with self.voiceover(
            text=(
                "Exemple : soit f de x égale la valeur absolue de x moins "
                "un, sur x moins un. Pour x supérieur à un, on trouve f de "
                "x égale un, donc la limite à droite vaut un. Pour x "
                "inférieur à un, on trouve f de x égale moins un, donc la "
                "limite à gauche vaut moins un. Les deux limites latérales "
                "étant différentes, la limite de f en un n'existe pas."
            )
        ) as tracker:
            self.play(FadeIn(ex1_titre))
            self.play(Write(ex1_calc))
            self.play(FadeIn(ex1_concl))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(ex1_titre), FadeOut(ex1_calc), FadeOut(ex1_concl))

        # --- Contre-exemple visuel : partie entière -----------------------------
        axes = Axes(
            x_range=[-0.5, 3.5, 1],
            y_range=[-0.5, 3.5, 1],
            x_length=5.5,
            y_length=3.5,
            axis_config={"color": WHITE, "font_size": 18},
        )
        marches = VGroup()
        from manim import Dot, Line

        for k in range(0, 3):
            seg = Line(axes.c2p(k, k), axes.c2p(k + 1, k), color=YELLOW)
            dot_plein = Dot(axes.c2p(k, k), color=YELLOW, radius=0.06)
            dot_vide = Dot(axes.c2p(k + 1, k), color=YELLOW, radius=0.06, fill_opacity=0)
            dot_vide.set_stroke(YELLOW, width=2)
            marches.add(seg, dot_plein, dot_vide)
        schema = VGroup(axes, marches)
        schema.next_to(titre, DOWN, buff=0.35)

        legende = Text(
            "Partie entière E(x) : saut en chaque entier, pas de limite",
            font_size=20,
        )
        legende.next_to(schema, DOWN, buff=0.3)

        with self.voiceover(
            text=(
                "Autre contre-exemple classique : la fonction partie "
                "entière. En chaque entier, elle fait un saut : la limite à "
                "gauche et la limite à droite sont différentes, donc la "
                "fonction partie entière n'a pas de limite en chaque "
                "entier, bien qu'elle y soit définie."
            )
        ) as tracker:
            self.play(FadeIn(schema))
            self.play(FadeIn(legende))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(schema), FadeOut(legende))

        # --- Pièges à éviter -------------------------------------------------
        piege = warning_box(
            Text(
                _wrap(
                    "Ne pas confondre « f est définie en x0 » et « f a une "
                    "limite en x0 » : les deux notions sont indépendantes, "
                    "comme le montrent |x-1|/(x-1) et la partie entière.",
                    width=54,
                ),
                font_size=22,
            ),
            box_width=11.0,
        )
        piege.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Attention : « f est définie en x zéro » et « f admet une "
                "limite en x zéro » sont deux notions bien distinctes, "
                "comme viennent de le montrer nos deux exemples."
            )
        ) as tracker:
            self.play(FadeIn(piege))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(piege), FadeOut(titre))
