"""
scenes/Maths_AnglesOrientesTrigonometrie_09.py — Chapitre « Angles orientés
et trigonométrie » (1ereC, Maths), scène 09.

§ Formules de duplication (cos 2a sous 3 écritures, sin 2a, tan 2a) avec
démonstration courte, exemple résolu 6 (cos a=1/3, calculer cos 2a),
formules de linéarisation de cos²a et sin²a avec démonstration.
Source : 1ereC/Maths.pdf, chapitre 2, pages 14-27.
"""

import textwrap

from manim import DOWN, LEFT, UP, FadeIn, FadeOut, MathTex, Text, VGroup, Write

from shapes.base_scene import NotionScene
from shapes.boxes import example_box, theorem_box, scene_title


def _wrap(text: str, width: int = 56) -> str:
    return "\n".join(textwrap.fill(line, width=width) for line in text.split("\n"))


class DuplicationLinearisation(NotionScene):
    def construct(self):
        titre = scene_title("Duplication et linéarisation")
        titre.scale(0.65)
        titre.to_edge(UP)

        # --- Énoncé : formules de duplication -----------------------------
        theoreme = theorem_box(
            VGroup(
                Text("Formules de duplication", font_size=24, weight="BOLD"),
                MathTex(
                    r"\cos 2a = \cos^2 a - \sin^2 a = 2\cos^2 a - 1 = 1 - 2\sin^2 a",
                    font_size=24,
                ),
                MathTex(r"\sin 2a = 2 \sin a \cos a", font_size=25),
                MathTex(r"\tan 2a = \dfrac{2\tan a}{1 - \tan^2 a}", font_size=25),
            ).arrange(DOWN, buff=0.28),
            box_width=9.5,
        )
        theoreme.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Lorsque a égale b dans les formules d'addition, on "
                "obtient les formules de duplication. Cosinus de deux a "
                "s'écrit de trois façons équivalentes : cosinus carré a "
                "moins sinus carré a, ou deux cosinus carré a moins un, ou "
                "encore un moins deux sinus carré a. Sinus de deux a égale "
                "deux sinus a cosinus a. Et tangente de deux a égale deux "
                "tangente a, divisé par un moins tangente carrée a."
            )
        ) as tracker:
            self.play(Write(titre))
            self.play(FadeIn(theoreme))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(theoreme))

        # --- Raisonnement : démonstration courte -------------------------------
        demo = VGroup(
            Text("Démonstration", font_size=23, color="#DE7C1F", weight="BOLD"),
            MathTex(
                r"\cos 2a = \cos(a+a) = \cos a \cos a - \sin a \sin a = \cos^2 a - \sin^2 a",
                font_size=24,
            ),
            Text("Avec cos²a + sin²a = 1, on remplace sin²a = 1-cos²a ou cos²a = 1-sin²a :", font_size=20),
            MathTex(
                r"\cos^2 a - \sin^2 a = \cos^2 a - (1-\cos^2 a) = 2\cos^2 a - 1",
                font_size=21,
            ),
            MathTex(
                r"\sin 2a = \sin(a+a) = \sin a \cos a + \cos a \sin a = 2\sin a \cos a",
                font_size=24,
            ),
            Text("La formule pour tan 2a s'obtient de même à partir de tan(a+a).", font_size=20),
        ).arrange(DOWN, buff=0.28, aligned_edge=LEFT)
        demo.next_to(titre, DOWN, buff=0.55)

        with self.voiceover(
            text=(
                "Ces formules se démontrent très simplement à partir des "
                "formules d'addition, en posant b égale a. Cosinus de deux "
                "a s'écrit cosinus de a plus a, donc cosinus a cosinus a "
                "moins sinus a sinus a, soit cosinus carré a moins sinus "
                "carré a. En utilisant la relation cosinus carré plus "
                "sinus carré égale un, on remplace sinus carré a par un "
                "moins cosinus carré a, ce qui donne deux cosinus carré a "
                "moins un ; ou l'inverse pour obtenir un moins deux sinus "
                "carré a. De même, sinus de deux a s'écrit sinus de a plus "
                "a, donc sinus a cosinus a plus cosinus a sinus a, soit "
                "deux sinus a cosinus a. La formule de la tangente "
                "s'obtient de la même façon à partir de tangente de a plus "
                "a."
            )
        ) as tracker:
            self.play(FadeIn(demo))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(demo))

        # --- Exemple résolu 6 ---------------------------------------------------
        exemple = example_box(
            VGroup(
                Text("Sachant que cos a = 1/3, calculer cos 2a.", font_size=22),
                MathTex(
                    r"\cos 2a = 2\cos^2 a - 1 = 2 \times \left(\dfrac{1}{3}\right)^2 - 1"
                    r" = \dfrac{2}{9} - 1 = -\dfrac{7}{9}",
                    font_size=25,
                ),
            ).arrange(DOWN, buff=0.35),
            box_width=9,
        )
        exemple.next_to(titre, DOWN, buff=0.6)

        with self.voiceover(
            text=(
                "Exemple résolu. Sachant que cosinus a vaut un tiers, "
                "calculons cosinus de deux a. On utilise la formule la "
                "plus adaptée ici, celle qui ne fait intervenir que le "
                "cosinus : deux cosinus carré a moins un. On obtient deux "
                "fois un tiers au carré, moins un, soit deux neuvièmes "
                "moins un, c'est-à-dire moins sept neuvièmes."
            )
        ) as tracker:
            self.play(FadeIn(exemple))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(exemple))

        # --- Linéarisation --------------------------------------------------------
        lineraisation = theorem_box(
            VGroup(
                Text("Formules de linéarisation", font_size=24, weight="BOLD"),
                MathTex(r"\cos^2 a = \dfrac{1 + \cos 2a}{2}", font_size=27),
                MathTex(r"\sin^2 a = \dfrac{1 - \cos 2a}{2}", font_size=27),
                Text(
                    _wrap(
                        "Démonstration : il suffit d'isoler cos²a et "
                        "sin²a dans les deux dernières écritures de "
                        "cos 2a vues plus haut.",
                        width=46,
                    ),
                    font_size=19,
                ),
            ).arrange(DOWN, buff=0.28),
            box_width=8.6,
        )
        lineraisation.next_to(titre, DOWN, buff=0.55)

        with self.voiceover(
            text=(
                "Pour finir, les formules de duplication se retournent en "
                "formules de linéarisation, très utiles pour transformer "
                "un carré de cosinus ou de sinus en une expression sans "
                "carré. Cosinus carré a égale un plus cosinus de deux a, "
                "le tout divisé par deux. Sinus carré a égale un moins "
                "cosinus de deux a, le tout divisé par deux. Ces deux "
                "formules se démontrent en isolant simplement cosinus "
                "carré a et sinus carré a dans les écritures deux cosinus "
                "carré a moins un, et un moins deux sinus carré a de "
                "cosinus de deux a, vues juste avant."
            )
        ) as tracker:
            self.play(FadeIn(lineraisation))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(lineraisation), FadeOut(titre))
