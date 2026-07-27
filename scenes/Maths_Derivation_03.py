"""
scenes/Maths_Derivation_03.py — Chapitre 9 (1ereC, Maths), scène 03.

Exemple résolu 4 : dérivabilité de √x en a > 0 par la quantité conjuguée.
Puis deux fonctions non dérivables : √x en 0 (demi-tangente verticale) et
|x| en 0 (point anguleux, limites latérales différentes).
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
    MathTex,
    Text,
    VGroup,
    Write,
)

from shapes.base_scene import NotionScene
from shapes.boxes import example_box, essentiel_box, scene_title, warning_box


def _wrap(text: str, width: int = 58) -> str:
    return "\n".join(textwrap.fill(line, width=width) for line in text.split("\n"))


class RacineCarreeEtNonDerivabilite(NotionScene):
    def construct(self):
        titre = scene_title("Racine carrée et non-dérivabilité")
        titre.scale(0.5)
        titre.to_edge(UP)
        self.play(Write(titre))

        # --- Exemple résolu 4 : √x dérivable pour a > 0 -------------------------
        enonce = Text("Exemple 4 — f(x) = √x est-elle dérivable en a > 0 ?", font_size=24, color=YELLOW)
        enonce.next_to(titre, DOWN, buff=0.45)

        with self.voiceover(
            text=(
                "Étudions maintenant la fonction racine carrée. Est-elle "
                "dérivable en un réel a strictement positif ? Pour "
                "répondre, nous allons calculer le taux d'accroissement en "
                "utilisant la technique de la quantité conjuguée."
            )
        ) as tracker:
            self.play(FadeIn(enonce))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(enonce))

        calcul = example_box(
            VGroup(
                MathTex(
                    r"\dfrac{\sqrt{a+h}-\sqrt{a}}{h}"
                    r" = \dfrac{(\sqrt{a+h}-\sqrt{a})(\sqrt{a+h}+\sqrt{a})}"
                    r"{h(\sqrt{a+h}+\sqrt{a})}",
                    font_size=24,
                ),
                MathTex(
                    r"= \dfrac{(a+h)-a}{h(\sqrt{a+h}+\sqrt{a})}"
                    r" = \dfrac{1}{\sqrt{a+h}+\sqrt{a}}",
                    font_size=26,
                ),
                MathTex(
                    r"\xrightarrow[h \to 0]{}\quad f'(a) = \dfrac{1}{2\sqrt{a}}"
                    r"\qquad (a > 0)",
                    font_size=28,
                ),
            ).arrange(DOWN, buff=0.3),
            box_width=11.5,
        )
        calcul.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "On multiplie le taux d'accroissement, en haut et en bas, "
                "par la quantité conjuguée racine de a plus h plus racine "
                "de a. Au numérateur, une identité remarquable fait "
                "disparaître les racines : il ne reste que a plus h moins "
                "a, c'est-à-dire h. On simplifie par h, et il reste un sur "
                "racine de a plus h plus racine de a. Quand h tend vers "
                "zéro, cette expression tend vers un sur deux racine de a. "
                "Donc racine de x est dérivable en tout a strictement "
                "positif, et sa dérivée vaut un sur deux racine de a."
            )
        ) as tracker:
            self.play(FadeIn(calcul))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(calcul))

        # --- Cas 1 : √x non dérivable en 0 (demi-tangente verticale) ------------
        axes1 = Axes(
            x_range=[-0.5, 3, 1],
            y_range=[-0.5, 2, 1],
            x_length=5.2,
            y_length=3.6,
            axis_config={"include_tip": True, "stroke_width": 2, "color": WHITE},
        )
        axes1.next_to(titre, DOWN, buff=0.5).shift(LEFT * 2.7)
        courbe1 = axes1.plot(lambda x: x**0.5, x_range=[0, 2.6], color=YELLOW)
        origine1 = Dot(axes1.c2p(0, 0), color=WHITE, radius=0.06)
        legende1 = Text("Demi-tangente verticale en 0", font_size=20, color=YELLOW)
        legende1.next_to(axes1, RIGHT, buff=0.4)
        figure1 = VGroup(axes1, courbe1, origine1)

        cas1 = warning_box(
            VGroup(
                Text("Cas 1 : f(x) = √x n'est pas dérivable en 0.", font_size=22),
                MathTex(
                    r"\dfrac{\sqrt{0+h}-\sqrt{0}}{h} = \dfrac{1}{\sqrt{h}}"
                    r"\xrightarrow[h \to 0^{+}]{} +\infty",
                    font_size=25,
                ),
                Text("La courbe admet une demi-tangente verticale à l'origine.", font_size=20),
            ).arrange(DOWN, buff=0.25),
            box_width=11.2,
        )
        cas1.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Mais attention : en zéro, c'est différent. Le taux "
                "d'accroissement de racine de x en zéro vaut un sur racine "
                "de h, qui tend vers plus l'infini quand h tend vers zéro "
                "par valeurs positives. La limite n'est pas finie : f n'est "
                "donc pas dérivable en zéro. Graphiquement, la courbe "
                "admet une demi-tangente verticale à l'origine — on le "
                "voit bien, la courbe part quasiment à la verticale."
            )
        ) as tracker:
            self.play(FadeIn(cas1))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(cas1))

        with self.voiceover(
            text=(
                "Voici la courbe de la fonction racine carrée au voisinage "
                "de zéro : on observe que la tangente y serait verticale, "
                "confirmant qu'il n'y a pas de nombre dérivé fini en ce "
                "point."
            )
        ) as tracker:
            self.play(Create(axes1))
            self.play(Create(courbe1), FadeIn(origine1))
            self.play(FadeIn(legende1))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(figure1), FadeOut(legende1))

        # --- Cas 2 : |x| non dérivable en 0 (point anguleux) --------------------
        axes2 = Axes(
            x_range=[-2, 2, 1],
            y_range=[-0.5, 2.5, 1],
            x_length=5.2,
            y_length=3.6,
            axis_config={"include_tip": True, "stroke_width": 2, "color": WHITE},
        )
        axes2.next_to(titre, DOWN, buff=0.5).shift(LEFT * 2.7)
        branche_g = axes2.plot(lambda x: -x, x_range=[-2, 0], color=YELLOW)
        branche_d = axes2.plot(lambda x: x, x_range=[0, 2], color=YELLOW)
        origine2 = Dot(axes2.c2p(0, 0), color=WHITE, radius=0.06)
        legende2 = VGroup(
            Text("Point anguleux en 0", font_size=20, color=YELLOW),
            Text("(deux demi-tangentes distinctes)", font_size=18),
        ).arrange(DOWN, buff=0.1)
        legende2.next_to(axes2, RIGHT, buff=0.4)
        figure2 = VGroup(axes2, branche_g, branche_d, origine2)

        cas2 = warning_box(
            VGroup(
                Text("Cas 2 : f(x) = |x| n'est pas dérivable en 0.", font_size=22),
                MathTex(
                    r"\dfrac{|h|-|0|}{h} = \dfrac{h}{h} = 1 \ (h>0)"
                    r"\qquad \dfrac{|h|-|0|}{h} = \dfrac{-h}{h} = -1 \ (h<0)",
                    font_size=22,
                ),
                Text("Limites à gauche (-1) et à droite (1) différentes : point anguleux.", font_size=19),
            ).arrange(DOWN, buff=0.25),
            box_width=11.6,
        )
        cas2.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Deuxième cas classique : la fonction valeur absolue en "
                "zéro. Pour h positif, le taux d'accroissement vaut h sur "
                "h, c'est-à-dire un. Pour h négatif, il vaut moins h sur h, "
                "c'est-à-dire moins un. La limite à droite vaut un, la "
                "limite à gauche vaut moins un : elles sont différentes, "
                "donc il n'y a pas de limite globale, et f n'est pas "
                "dérivable en zéro. Graphiquement, la courbe présente un "
                "point anguleux : deux demi-tangentes de pentes "
                "différentes se rejoignent en ce point."
            )
        ) as tracker:
            self.play(FadeIn(cas2))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(cas2))

        with self.voiceover(
            text=(
                "On le visualise très clairement sur la courbe en V de la "
                "valeur absolue : à gauche de zéro, la pente est moins un ; "
                "à droite, la pente est plus un. Le point à l'origine est "
                "un point anguleux, pas un point où la courbe est lisse."
            )
        ) as tracker:
            self.play(Create(axes2))
            self.play(Create(branche_g), Create(branche_d), FadeIn(origine2))
            self.play(FadeIn(legende2))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(figure2), FadeOut(legende2))

        # --- À retenir -----------------------------------------------------------
        retenir = essentiel_box(
            Text(
                _wrap(
                    "Une fonction n'est pas dérivable en un point si le "
                    "taux d'accroissement n'a pas de limite finie : "
                    "limite infinie (demi-tangente verticale, cas √x en "
                    "0) ou limites latérales différentes (point anguleux, "
                    "cas |x| en 0).",
                    width=58,
                ),
                font_size=22,
            )
        )
        retenir.next_to(titre, DOWN, buff=0.6)

        with self.voiceover(
            text=(
                "À retenir : une fonction n'est pas dérivable en un point "
                "dès que le taux d'accroissement n'admet pas de limite "
                "finie en ce point. Deux scénarios typiques : une limite "
                "infinie, qui donne une demi-tangente verticale, comme pour "
                "racine de x en zéro ; ou des limites latérales "
                "différentes, qui donnent un point anguleux, comme pour la "
                "valeur absolue en zéro."
            )
        ) as tracker:
            self.play(FadeIn(retenir))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(titre), FadeOut(retenir))
