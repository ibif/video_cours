"""
scenes/Maths_Derivation_05.py — Chapitre 9 (1ereC, Maths), scène 05.

De la sécante à la tangente, définition de la tangente, théorème de
l'équation de la tangente y = f'(a)(x-a)+f(a), exemple résolu 5 complet
(f(x) = x²-2x, a = 3), cas particuliers (tangente horizontale, demi-
tangente verticale).
Source : 1ereC/Maths.pdf, chapitre 9, pages 105-117.
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
from shapes.boxes import definition_box, essentiel_box, example_box, scene_title, theorem_box


def _wrap(text: str, width: int = 58) -> str:
    return "\n".join(textwrap.fill(line, width=width) for line in text.split("\n"))


class TangenteCourbe(NotionScene):
    def construct(self):
        titre = scene_title("Tangente à une courbe")
        titre.scale(0.6)
        titre.to_edge(UP)

        # --- Énoncé : de la sécante à la tangente ---------------------------------
        axes = Axes(
            x_range=[-0.5, 3, 1],
            y_range=[-0.5, 6, 1],
            x_length=5.6,
            y_length=4.0,
            axis_config={"include_tip": True, "stroke_width": 2, "color": WHITE},
        )
        axes.next_to(titre, DOWN, buff=0.5).shift(LEFT * 2.5)
        courbe = axes.plot(lambda x: x**2, x_range=[-0.3, 2.4], color=YELLOW)
        a_val = 1.0
        point_a = Dot(axes.c2p(a_val, a_val**2), color=WHITE, radius=0.07)

        secante1 = Line(axes.c2p(-0.2, 3.5), axes.c2p(2.2, -0.9), color="#DE7C1F")
        secante2 = Line(axes.c2p(-0.2, 1.5), axes.c2p(2.2, 3.9), color="#A42A5A")
        tangente_ligne = Line(axes.c2p(-0.2, -0.4), axes.c2p(2.2, 4.4), color="#288073")

        legende = Text("h → 0 : la sécante pivote vers la tangente", font_size=20, color=YELLOW)
        legende.next_to(axes, RIGHT, buff=0.4)

        with self.voiceover(
            text=(
                "Reprenons notre sécante, qui passait par le point A "
                "d'abscisse a et un point voisin M d'abscisse a plus h. "
                "Quand h se rapproche de zéro, le point M se rapproche du "
                "point A le long de la courbe, et la sécante pivote "
                "progressivement autour de A. La position limite de cette "
                "sécante, quand elle existe, s'appelle la tangente à la "
                "courbe au point A."
            )
        ) as tracker:
            self.play(Write(titre))
            self.play(Create(axes), Create(courbe), FadeIn(point_a))
            self.play(Create(secante1))
            self.play(Create(secante2))
            self.play(Create(tangente_ligne), FadeIn(legende))
            self.wait(tracker.get_remaining_duration())

        self.play(
            FadeOut(axes), FadeOut(courbe), FadeOut(point_a),
            FadeOut(secante1), FadeOut(secante2), FadeOut(tangente_ligne), FadeOut(legende),
        )

        # --- Définition -------------------------------------------------------------
        definition = definition_box(
            Text(
                _wrap(
                    "Si f est dérivable en a, la tangente à la courbe de "
                    "f au point A(a ; f(a)) est la position limite des "
                    "sécantes (AM) quand M tend vers A le long de la "
                    "courbe.",
                    width=54,
                ),
                font_size=23,
            ),
            box_width=11.0,
        )
        definition.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Formellement : si f est dérivable en a, la tangente à la "
                "courbe de f au point A de coordonnées a et f de a est la "
                "position limite des sécantes A M, quand M tend vers A le "
                "long de la courbe."
            )
        ) as tracker:
            self.play(FadeIn(definition))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(definition))

        # --- Théorème : équation de la tangente -------------------------------------
        theoreme = theorem_box(
            VGroup(
                Text("Équation de la tangente au point A(a ; f(a)) :", font_size=23),
                MathTex(r"y = f'(a)(x-a) + f(a)", font_size=32),
            ).arrange(DOWN, buff=0.3),
            box_width=9.6,
        )
        theoreme.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Le nombre dérivé f prime de a est donc le coefficient "
                "directeur de cette tangente. L'équation de la tangente au "
                "point A, d'abscisse a, est y égale f prime de a, fois x "
                "moins a, plus f de a."
            )
        ) as tracker:
            self.play(FadeIn(theoreme))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(theoreme))

        # --- Exemple résolu 5 : f(x)=x²-2x, tangente en a=3 -----------------------
        exemple = example_box(
            VGroup(
                Text("Exemple 5 — f(x) = x²-2x, tangente au point d'abscisse a = 3 :", font_size=20),
                MathTex(
                    r"f(3) = 9-6 = 3 \qquad "
                    r"\dfrac{f(3+h)-f(3)}{h} = \dfrac{(3+h)^2-2(3+h)-3}{h}",
                    font_size=22,
                ),
                MathTex(
                    r"= \dfrac{9+6h+h^2-6-2h-3}{h} = \dfrac{4h+h^2}{h} = 4+h"
                    r"\ \xrightarrow[h \to 0]{}\ 4",
                    font_size=22,
                ),
                MathTex(
                    r"f'(3) = 4 \quad\Longrightarrow\quad y = 4(x-3)+3 = 4x-9",
                    font_size=27,
                ),
            ).arrange(DOWN, buff=0.28),
            box_width=11.6,
        )
        exemple.next_to(titre, DOWN, buff=0.45)

        with self.voiceover(
            text=(
                "Exemple : soit f de x égale x carré moins deux x, et "
                "cherchons l'équation de la tangente au point d'abscisse a "
                "égale trois. D'abord, f de trois vaut neuf moins six, "
                "c'est-à-dire trois. Ensuite, on calcule le taux "
                "d'accroissement en trois : après développement et "
                "simplification par h, on obtient quatre plus h, qui tend "
                "vers quatre quand h tend vers zéro. Donc f prime de trois "
                "vaut quatre. L'équation de la tangente est alors y égale "
                "quatre fois x moins trois, plus trois, ce qui se simplifie "
                "en y égale quatre x moins neuf."
            )
        ) as tracker:
            self.play(FadeIn(exemple))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(exemple))

        # --- Figure : tangente au point a = 3 -----------------------------------
        axes2 = Axes(
            x_range=[0, 5, 1],
            y_range=[-2, 8, 2],
            x_length=5.6,
            y_length=4.0,
            axis_config={"include_tip": True, "stroke_width": 2, "color": WHITE},
        )
        axes2.next_to(titre, DOWN, buff=0.5).shift(LEFT * 2.5)
        courbe2 = axes2.plot(lambda x: x**2 - 2 * x, x_range=[0.2, 4.8], color=YELLOW)
        tangente2 = axes2.plot(lambda x: 4 * x - 9, x_range=[1.3, 4.5], color="#288073")
        point3 = Dot(axes2.c2p(3, 3), color=WHITE, radius=0.07)
        label3 = MathTex("A(3;3)", font_size=24).next_to(point3, RIGHT, buff=0.15)
        figure2 = VGroup(axes2, courbe2, tangente2, point3, label3)

        with self.voiceover(
            text=(
                "Voici la courbe de f et sa tangente au point A de "
                "coordonnées trois et trois : on retrouve bien une droite "
                "de pente quatre, tangente à la parabole en ce point."
            )
        ) as tracker:
            self.play(Create(axes2), Create(courbe2))
            self.play(FadeIn(point3), Write(label3))
            self.play(Create(tangente2))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(figure2))

        # --- Cas particuliers ----------------------------------------------------
        cas = theorem_box(
            VGroup(
                Text("Cas particuliers :", font_size=22),
                MathTex(r"f'(a) = 0 \ \Longrightarrow\ \text{tangente horizontale } (y=f(a))", font_size=24),
                Text(
                    "Si le taux d'accroissement tend vers ±∞ : demi-tangente\n"
                    "verticale (cas de √x en 0, voir scène 3).",
                    font_size=20,
                ),
            ).arrange(DOWN, buff=0.25),
            box_width=11.4,
        )
        cas.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Deux cas particuliers à connaître. Si f prime de a est "
                "nul, la tangente est horizontale, d'équation y égale f de "
                "a. Et si le taux d'accroissement tend vers plus ou moins "
                "l'infini, comme nous l'avons vu pour racine de x en zéro, "
                "la courbe admet alors une demi-tangente verticale."
            )
        ) as tracker:
            self.play(FadeIn(cas))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(cas))

        # --- À retenir -------------------------------------------------------------
        retenir = essentiel_box(
            Text(
                _wrap(
                    "La tangente en A(a ; f(a)) a pour équation "
                    "y = f'(a)(x-a) + f(a). f'(a) est le coefficient "
                    "directeur de cette tangente : c'est la pente de la "
                    "courbe au point A.",
                    width=58,
                ),
                font_size=23,
            )
        )
        retenir.next_to(titre, DOWN, buff=0.6)

        with self.voiceover(
            text=(
                "À retenir : l'équation de la tangente en A est y égale f "
                "prime de a, fois x moins a, plus f de a. Le nombre dérivé "
                "f prime de a est donc la pente de la courbe au point A — "
                "une lecture géométrique essentielle du nombre dérivé."
            )
        ) as tracker:
            self.play(FadeIn(retenir))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(titre), FadeOut(retenir))
