"""
scenes/Maths_Derivation_02.py — Chapitre 9 (1ereC, Maths), scène 02.

Nombre dérivé et dérivabilité en un point : définition comme limite du taux
d'accroissement, écriture équivalente avec x → a, exemples résolus complets
pour f(x) = x² et f(x) = 1/x.
Source : 1ereC/Maths.pdf, chapitre 9, pages 105-117.
"""

import textwrap

from manim import DOWN, UP, FadeIn, FadeOut, MathTex, Text, VGroup, Write, YELLOW

from shapes.base_scene import NotionScene
from shapes.boxes import definition_box, essentiel_box, example_box, scene_title


def _wrap(text: str, width: int = 58) -> str:
    return "\n".join(textwrap.fill(line, width=width) for line in text.split("\n"))


class NombreDeriveDefinition(NotionScene):
    def construct(self):
        titre = scene_title("Nombre dérivé — dérivabilité")
        titre.scale(0.5)
        titre.to_edge(UP)

        # --- Énoncé ------------------------------------------------------------
        enonce = Text(
            _wrap(
                "Dans l'exemple précédent, τ₁(h) se rapproche de 2 quand h "
                "tend vers 0. Ce nombre limite porte un nom : le nombre "
                "dérivé.",
                width=56,
            ),
            font_size=25,
            color=YELLOW,
        )
        enonce.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Nous avons vu que le taux d'accroissement de x carré entre "
                "un et un plus h se rapproche de deux quand h tend vers "
                "zéro. Cette limite du taux d'accroissement porte un nom "
                "précis en mathématiques : le nombre dérivé."
            )
        ) as tracker:
            self.play(Write(titre))
            self.play(FadeIn(enonce))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(enonce))

        # --- Définition ----------------------------------------------------------
        definition = definition_box(
            VGroup(
                Text(
                    _wrap(
                        "f est dérivable en a si le taux d'accroissement "
                        "τ_a(h) admet une limite finie quand h tend vers 0. "
                        "Cette limite s'appelle le nombre dérivé de f en a, "
                        "noté f'(a) :",
                        width=54,
                    ),
                    font_size=22,
                ),
                MathTex(
                    r"f'(a) = \lim_{h \to 0} \dfrac{f(a+h)-f(a)}{h}",
                    font_size=32,
                ),
            ).arrange(DOWN, buff=0.3),
            box_width=11.3,
        )
        definition.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Voici la définition. On dit que f est dérivable en a si le "
                "taux d'accroissement tau indice a de h admet une limite "
                "finie quand h tend vers zéro. Cette limite s'appelle le "
                "nombre dérivé de f en a, noté f prime de a, et elle vaut "
                "la limite, quand h tend vers zéro, de f de a plus h moins "
                "f de a, sur h."
            )
        ) as tracker:
            self.play(FadeIn(definition))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(definition))

        # --- Écriture équivalente avec x → a --------------------------------
        equivalence = definition_box(
            VGroup(
                Text("Écriture équivalente, en posant x = a+h :", font_size=22),
                MathTex(
                    r"f'(a) = \lim_{x \to a} \dfrac{f(x)-f(a)}{x-a}",
                    font_size=32,
                ),
            ).arrange(DOWN, buff=0.3),
            box_width=10.5,
        )
        equivalence.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Il existe une écriture équivalente, très utilisée aussi : "
                "en posant x égale a plus h, donc x qui tend vers a quand h "
                "tend vers zéro, le nombre dérivé s'écrit comme la limite, "
                "quand x tend vers a, de f de x moins f de a, sur x moins "
                "a. Les deux écritures sont rigoureusement équivalentes."
            )
        ) as tracker:
            self.play(FadeIn(equivalence))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(equivalence))

        # --- Exemple résolu 2 : f(x) = x², dérivée en a quelconque ---------------
        exemple2 = example_box(
            VGroup(
                Text("Exemple 2 — f(x) = x², nombre dérivé en un réel a :", font_size=22),
                MathTex(
                    r"\dfrac{f(a+h)-f(a)}{h} = \dfrac{(a+h)^2-a^2}{h}"
                    r" = \dfrac{2ah+h^2}{h} = 2a+h",
                    font_size=26,
                ),
                MathTex(
                    r"\lim_{h \to 0} (2a+h) = 2a "
                    r"\quad\Longrightarrow\quad f'(a) = 2a",
                    font_size=28,
                ),
            ).arrange(DOWN, buff=0.3),
            box_width=11.4,
        )
        exemple2.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Exemple deux : reprenons f de x égale x carré, mais avec "
                "un a quelconque cette fois. Le taux d'accroissement vaut a "
                "plus h au carré, moins a carré, sur h, ce qui se "
                "simplifie en deux a h plus h carré, sur h, donc deux a "
                "plus h. Quand h tend vers zéro, cette expression tend vers "
                "deux a. Donc f est dérivable en tout réel a, et f prime de "
                "a vaut deux a."
            )
        ) as tracker:
            self.play(FadeIn(exemple2))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(exemple2))

        # --- Exemple résolu 3 : f(x) = 1/x, dérivée en a ≠ 0 -------------------
        exemple3 = example_box(
            VGroup(
                Text("Exemple 3 — f(x) = 1/x, nombre dérivé en a ≠ 0 :", font_size=22),
                MathTex(
                    r"\dfrac{f(a+h)-f(a)}{h} = \dfrac{1}{h}"
                    r"\left(\dfrac{1}{a+h} - \dfrac{1}{a}\right)"
                    r" = \dfrac{1}{h}\cdot\dfrac{a-(a+h)}{a(a+h)}",
                    font_size=24,
                ),
                MathTex(
                    r"= \dfrac{-h}{h\,a(a+h)} = \dfrac{-1}{a(a+h)}"
                    r"\quad\xrightarrow[h \to 0]{}\quad f'(a) = -\dfrac{1}{a^2}",
                    font_size=25,
                ),
            ).arrange(DOWN, buff=0.3),
            box_width=11.6,
        )
        exemple3.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Exemple trois : soit f de x égale un sur x, avec a non "
                "nul. Le taux d'accroissement vaut un sur h, fois la "
                "quantité un sur a plus h, moins un sur a. En mettant au "
                "même dénominateur, on obtient un sur h, fois a moins a "
                "plus h, sur a fois a plus h, ce qui se simplifie en moins "
                "un sur a fois a plus h. Quand h tend vers zéro, cette "
                "expression tend vers moins un sur a carré. Donc f est "
                "dérivable en tout a non nul, et f prime de a vaut moins un "
                "sur a carré."
            )
        ) as tracker:
            self.play(FadeIn(exemple3))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(exemple3))

        # --- À retenir -------------------------------------------------------
        retenir = essentiel_box(
            Text(
                _wrap(
                    "f'(a) est le nombre dérivé de f en a : la limite, "
                    "finie, du taux d'accroissement quand h tend vers 0 "
                    "(ou x tend vers a). S'il n'existe pas de limite "
                    "finie, f n'est pas dérivable en a.",
                    width=58,
                ),
                font_size=23,
            )
        )
        retenir.next_to(titre, DOWN, buff=0.6)

        with self.voiceover(
            text=(
                "À retenir : le nombre dérivé f prime de a est la limite, "
                "quand elle existe et qu'elle est finie, du taux "
                "d'accroissement de f en a. Si cette limite n'existe pas, "
                "ou si elle est infinie, alors f n'est tout simplement pas "
                "dérivable en a — c'est justement ce que nous allons "
                "explorer dans la scène suivante."
            )
        ) as tracker:
            self.play(FadeIn(retenir))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(titre), FadeOut(retenir))
