"""
scenes/Maths_Derivation_09.py — Chapitre 9 (1ereC, Maths), scène 09.

Dérivée de g(x) = f(ax+b) → g'(x) = a·f'(ax+b), avec idée de démonstration.
Exemple résolu 11 (trois calculs). Dérivée de √u(x) = u'(x)/(2√u(x)),
condition u > 0. Exemple résolu 12.
Source : 1ereC/Maths.pdf, chapitre 9, pages 105-117.
"""

import textwrap

from manim import DOWN, UP, FadeIn, FadeOut, MathTex, Text, VGroup, Write, YELLOW

from shapes.base_scene import NotionScene
from shapes.boxes import example_box, essentiel_box, scene_title, theorem_box


def _wrap(text: str, width: int = 58) -> str:
    return "\n".join(textwrap.fill(line, width=width) for line in text.split("\n"))


class DeriveeCompositionAffineEtRacine(NotionScene):
    def construct(self):
        titre = scene_title("Dérivée de f(ax+b) et de √u(x)")
        titre.scale(0.5)
        titre.to_edge(UP)

        # --- Énoncé --------------------------------------------------------------
        enonce = Text(
            _wrap(
                "Comment dériver une fonction de la forme g(x) = f(ax+b), "
                "sans repasser par la définition ?",
                width=56,
            ),
            font_size=25,
            color=YELLOW,
        )
        enonce.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Il arrive très souvent de devoir dériver une fonction "
                "composée d'une fonction affine, de la forme g de x égale f "
                "de a x plus b, comme x carré appliqué à trois x moins "
                "deux. Comment procéder sans revenir à la définition "
                "complète du nombre dérivé ?"
            )
        ) as tracker:
            self.play(Write(titre))
            self.play(FadeIn(enonce))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(enonce))

        # --- Théorème : dérivée de f(ax+b) -------------------------------------------
        theoreme1 = theorem_box(
            VGroup(
                Text("Si f est dérivable, et g(x) = f(ax+b), alors g est dérivable et :", font_size=20),
                MathTex(r"g'(x) = a \times f'(ax+b)", font_size=32),
            ).arrange(DOWN, buff=0.3),
            box_width=9.6,
        )
        theoreme1.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Voici le théorème : si f est dérivable, et si g de x égale "
                "f de a x plus b, alors g est dérivable, et sa dérivée "
                "vaut a fois f prime de a x plus b. Autrement dit, on "
                "dérive f normalement, on l'évalue en a x plus b, puis on "
                "multiplie par a, le coefficient devant x."
            )
        ) as tracker:
            self.play(FadeIn(theoreme1))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(theoreme1))

        idee_demo = theorem_box(
            Text(
                _wrap(
                    "Idée de démonstration : le taux d'accroissement de g "
                    "en a₀ fait apparaître le taux d'accroissement de f "
                    "entre a·a₀+b et a·(a₀+h)+b, multiplié par a — d'où "
                    "le facteur a devant f'.",
                    width=54,
                ),
                font_size=20,
            ),
            box_width=10.8,
        )
        idee_demo.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "L'idée de la démonstration : en écrivant le taux "
                "d'accroissement de g en un point a zéro, et en posant k "
                "égale a fois h, on fait réapparaître exactement le taux "
                "d'accroissement de f, entre a fois a zéro plus b et a fois "
                "a zéro plus h plus b, multiplié par le facteur a. C'est ce "
                "changement de variable qui explique le a devant f prime."
            )
        ) as tracker:
            self.play(FadeIn(idee_demo))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(idee_demo))

        # --- Exemple résolu 11 : trois calculs -----------------------------------------
        exemple11 = example_box(
            VGroup(
                Text("Exemple 11 — trois applications :", font_size=21),
                MathTex(
                    r"g(x)=(3x-2)^5 \ \Longrightarrow\ g'(x) = 3 \times 5(3x-2)^4 = 15(3x-2)^4",
                    font_size=22,
                ),
                MathTex(
                    r"g(x)=\sqrt{2x+5} \ \Longrightarrow\ "
                    r"g'(x) = 2 \times \dfrac{1}{2\sqrt{2x+5}} = \dfrac{1}{\sqrt{2x+5}}",
                    font_size=22,
                ),
                MathTex(
                    r"g(x)=\dfrac{1}{4x-1} \ \Longrightarrow\ "
                    r"g'(x) = 4 \times \left(-\dfrac{1}{(4x-1)^2}\right) = \dfrac{-4}{(4x-1)^2}",
                    font_size=22,
                ),
            ).arrange(DOWN, buff=0.25),
            box_width=11.8,
        )
        exemple11.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Exemple onze, trois applications directes. Pour g de x "
                "égale trois x moins deux, à la puissance cinq, on utilise "
                "la formule de la puissance combinée à celle-ci : g prime "
                "de x égale trois, fois cinq, fois trois x moins deux, à la "
                "puissance quatre, soit quinze fois trois x moins deux, "
                "puissance quatre. Pour g de x égale racine de deux x plus "
                "cinq, on obtient g prime de x égale deux, fois un sur deux "
                "racine de deux x plus cinq, soit un sur racine de deux x "
                "plus cinq. Et pour g de x égale un sur quatre x moins un, "
                "on obtient g prime de x égale quatre, fois moins un sur "
                "quatre x moins un au carré, soit moins quatre sur quatre x "
                "moins un au carré."
            )
        ) as tracker:
            self.play(FadeIn(exemple11))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(exemple11))

        # --- Théorème : dérivée de √u(x) ----------------------------------------------
        theoreme2 = theorem_box(
            VGroup(
                Text("Si u est dérivable et u > 0 sur I, alors √u est dérivable sur I :", font_size=20),
                MathTex(r"\left(\sqrt{u}\right)'(x) = \dfrac{u'(x)}{2\sqrt{u(x)}}", font_size=30),
            ).arrange(DOWN, buff=0.3),
            box_width=10.0,
        )
        theoreme2.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Un autre cas très fréquent : la dérivée de racine de u de "
                "x. Si u est dérivable et strictement positive sur un "
                "intervalle I, alors racine de u est dérivable sur I, et sa "
                "dérivée vaut u prime de x, sur deux racine de u de x. "
                "C'est une généralisation directe de la dérivée de racine "
                "de x, avec u à la place de x, et un facteur u prime en "
                "plus au numérateur."
            )
        ) as tracker:
            self.play(FadeIn(theoreme2))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(theoreme2))

        # --- Exemple résolu 12 -----------------------------------------------------------
        exemple12 = example_box(
            VGroup(
                Text("Exemple 12 — g(x) = √(x²+3) :", font_size=22),
                MathTex(
                    r"u(x) = x^2+3 > 0 \ \text{sur } \mathbb{R}, \quad u'(x) = 2x",
                    font_size=25,
                ),
                MathTex(
                    r"g'(x) = \dfrac{2x}{2\sqrt{x^2+3}} = \dfrac{x}{\sqrt{x^2+3}}",
                    font_size=28,
                ),
            ).arrange(DOWN, buff=0.3),
            box_width=10.6,
        )
        exemple12.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Exemple douze : soit g de x égale racine de x carré plus "
                "trois. On pose u de x égale x carré plus trois, qui est "
                "strictement positif sur l'ensemble des réels, de dérivée "
                "deux x. La formule donne alors : g prime de x égale deux x "
                "sur deux racine de x carré plus trois, soit finalement x "
                "sur racine de x carré plus trois."
            )
        ) as tracker:
            self.play(FadeIn(exemple12))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(exemple12))

        # --- À retenir ------------------------------------------------------------------
        retenir = essentiel_box(
            Text(
                _wrap(
                    "g(x) = f(ax+b) ⟹ g'(x) = a·f'(ax+b). "
                    "(√u)' = u'/(2√u), valable seulement si u > 0. "
                    "Vérifier systématiquement le signe de u avant "
                    "d'appliquer cette dernière formule.",
                    width=58,
                ),
                font_size=22,
            )
        )
        retenir.next_to(titre, DOWN, buff=0.6)

        with self.voiceover(
            text=(
                "À retenir : pour g de x égale f de a x plus b, la dérivée "
                "est a fois f prime de a x plus b. Pour racine de u de x, "
                "la dérivée est u prime sur deux racine de u, mais "
                "uniquement là où u est strictement positive — un point à "
                "vérifier systématiquement avant tout calcul."
            )
        ) as tracker:
            self.play(FadeIn(retenir))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(titre), FadeOut(retenir))
