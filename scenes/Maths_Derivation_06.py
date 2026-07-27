"""
scenes/Maths_Derivation_06.py — Chapitre 9 (1ereC, Maths), scène 06.

Approximation affine : f(a+h) ≈ f(a) + h f'(a), exemple résolu 6 (valeur
approchée de √4,02 sans calculatrice).
Source : 1ereC/Maths.pdf, chapitre 9, pages 105-117.
"""

import textwrap

from manim import DOWN, UP, FadeIn, FadeOut, MathTex, Text, VGroup, Write, YELLOW

from shapes.base_scene import NotionScene
from shapes.boxes import essentiel_box, example_box, property_box, scene_title


def _wrap(text: str, width: int = 58) -> str:
    return "\n".join(textwrap.fill(line, width=width) for line in text.split("\n"))


class ApproximationAffine(NotionScene):
    def construct(self):
        titre = scene_title("Approximation affine")
        titre.scale(0.6)
        titre.to_edge(UP)

        # --- Énoncé ---------------------------------------------------------------
        enonce = Text(
            _wrap(
                "Près du point A, la courbe de f ressemble beaucoup à sa "
                "tangente. Peut-on utiliser cette tangente pour obtenir "
                "une valeur approchée de f, sans calculatrice ?",
                width=56,
            ),
            font_size=24,
            color=YELLOW,
        )
        enonce.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Au voisinage du point A, la courbe de f se confond "
                "presque avec sa tangente. Cette observation, très "
                "concrète, permet d'obtenir facilement une valeur "
                "approchée de f de a plus h, pour h petit, sans avoir "
                "besoin de calculatrice."
            )
        ) as tracker:
            self.play(Write(titre))
            self.play(FadeIn(enonce))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(enonce))

        # --- Propriété --------------------------------------------------------------
        propriete = property_box(
            VGroup(
                Text(
                    "Pour h proche de 0, on approche f(a+h) par la valeur\n"
                    "de la tangente en a :",
                    font_size=22,
                ),
                MathTex(r"f(a+h) \approx f(a) + h \, f'(a)", font_size=32),
            ).arrange(DOWN, buff=0.3),
            box_width=9.6,
        )
        propriete.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Voici la propriété d'approximation affine : pour h proche "
                "de zéro, f de a plus h est approximativement égal à f de "
                "a, plus h fois f prime de a. C'est simplement l'équation "
                "de la tangente, utilisée pour évaluer f, au lieu de tracer "
                "une droite."
            )
        ) as tracker:
            self.play(FadeIn(propriete))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(propriete))

        # --- Exemple résolu 6 : valeur approchée de √4,02 ---------------------------
        exemple = example_box(
            VGroup(
                Text("Exemple 6 — valeur approchée de √4,02 sans calculatrice :", font_size=21),
                Text("On pose f(x) = √x, a = 4, h = 0,02 (car 4,02 = 4 + 0,02).", font_size=20),
                MathTex(
                    r"f(4) = \sqrt{4} = 2 \qquad "
                    r"f'(x) = \dfrac{1}{2\sqrt{x}} \ \Longrightarrow\ f'(4) = \dfrac{1}{4}",
                    font_size=23,
                ),
                MathTex(
                    r"\sqrt{4{,}02} \approx f(4) + 0{,}02 \times f'(4)"
                    r" = 2 + 0{,}02 \times 0{,}25 = 2{,}005",
                    font_size=25,
                ),
            ).arrange(DOWN, buff=0.28),
            box_width=11.6,
        )
        exemple.next_to(titre, DOWN, buff=0.45)

        with self.voiceover(
            text=(
                "Exemple : cherchons une valeur approchée de racine de "
                "quatre virgule zéro deux, sans calculatrice. On pose f de "
                "x égale racine de x, a égale quatre, et h égale zéro "
                "virgule zéro deux, puisque quatre virgule zéro deux est "
                "égal à quatre plus zéro virgule zéro deux. On a f de "
                "quatre qui vaut deux, et f prime de x qui vaut un sur deux "
                "racine de x, donc f prime de quatre vaut un quart, "
                "c'est-à-dire zéro virgule vingt-cinq. L'approximation "
                "affine donne alors : racine de quatre virgule zéro deux "
                "est approximativement égale à deux, plus zéro virgule "
                "zéro deux fois zéro virgule vingt-cinq, ce qui donne deux "
                "virgule zéro zéro cinq — une excellente approximation, "
                "obtenue en quelques lignes de calcul mental."
            )
        ) as tracker:
            self.play(FadeIn(exemple))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(exemple))

        # --- À retenir ----------------------------------------------------------------
        retenir = essentiel_box(
            Text(
                _wrap(
                    "f(a+h) ≈ f(a) + h f'(a) pour h proche de 0. Cette "
                    "approximation affine est d'autant plus précise que h "
                    "est petit : c'est un outil de calcul rapide, utile "
                    "quand on connaît f(a) et f'(a).",
                    width=58,
                ),
                font_size=22,
            )
        )
        retenir.next_to(titre, DOWN, buff=0.6)

        with self.voiceover(
            text=(
                "À retenir : l'approximation affine f de a plus h "
                "approximativement égal à f de a plus h fois f prime de a "
                "est d'autant plus précise que h est petit. C'est un outil "
                "de calcul rapide, très utile dès que l'on connaît la "
                "valeur et le nombre dérivé de f en un point voisin."
            )
        ) as tracker:
            self.play(FadeIn(retenir))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(titre), FadeOut(retenir))
