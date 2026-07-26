"""
scenes/Maths_ExtensionNotionLimite_03.py — Chapitre 7 (1ereC, Maths), scène 03.

Limite en +∞/-∞ d'une fonction rationnelle : rappel des 4 formes
indéterminées, théorème du terme de plus haut degré (avec démonstration par
factorisation), conséquence selon les degrés n et p, exemple résolu (3
calculs).
Source : 1ereC/Maths.pdf, chapitre 7, pages 80-90.
"""

import textwrap

from manim import DOWN, UP, FadeIn, FadeOut, MathTex, Text, VGroup, Write, YELLOW

from shapes.base_scene import NotionScene
from shapes.boxes import essentiel_box, example_box, scene_title, theorem_box, warning_box


def _wrap(text: str, width: int = 58) -> str:
    return "\n".join(textwrap.fill(line, width=width) for line in text.split("\n"))


class LimiteInfinieFonctionRationnelle(NotionScene):
    def construct(self):
        titre = scene_title("Limite en ±∞ d'une fonction rationnelle")
        titre.scale(0.5)
        titre.to_edge(UP)

        # --- Énoncé : rappel des 4 formes indéterminées ------------------------
        rappel_fi = example_box(
            VGroup(
                Text("Rappel — les 4 formes indéterminées :", font_size=22, weight="BOLD"),
                MathTex(
                    r"\infty - \infty \qquad 0 \times \infty \qquad "
                    r"\dfrac{\infty}{\infty} \qquad \dfrac{0}{0}",
                    font_size=30,
                ),
            ).arrange(DOWN, buff=0.35),
            box_width=9.5,
        )
        rappel_fi.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Rappelons les quatre formes indéterminées : l'infini moins "
                "l'infini, zéro fois l'infini, l'infini sur l'infini, et "
                "zéro sur zéro. Une fonction rationnelle en plus l'infini "
                "ou moins l'infini se présente presque toujours sous la "
                "forme infini sur infini, une indétermination qu'il faut "
                "lever."
            )
        ) as tracker:
            self.play(Write(titre))
            self.play(FadeIn(rappel_fi))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(rappel_fi))

        # --- Animation du raisonnement : théorème + démonstration -------------
        theoreme = theorem_box(
            VGroup(
                Text(
                    "En +∞ ou en -∞, un polynôme a même limite que son terme "
                    "de plus haut degré :",
                    font_size=21,
                ),
                MathTex(
                    r"a_n x^n + a_{n-1}x^{n-1} + \cdots + a_0"
                    r"\quad \text{a même limite que} \quad a_n x^n",
                    font_size=25,
                ),
                Text(
                    "Une fonction rationnelle a même limite que le quotient "
                    "des termes de plus haut degré du numérateur et du "
                    "dénominateur.",
                    font_size=21,
                ),
            ).arrange(DOWN, buff=0.3),
            box_width=11.4,
        )
        theoreme.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Voici le théorème central de cette scène : en plus l'infini "
                "ou en moins l'infini, un polynôme a la même limite que son "
                "terme de plus haut degré. Et une fonction rationnelle, "
                "c'est-à-dire un quotient de deux polynômes, a la même "
                "limite que le quotient des termes de plus haut degré du "
                "numérateur et du dénominateur."
            )
        ) as tracker:
            self.play(FadeIn(theoreme))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(theoreme))

        demonstration = example_box(
            MathTex(
                r"""
                \begin{array}{l}
                a_nx^n+\cdots+a_0 = a_nx^n
                \left(1+\dfrac{a_{n-1}}{a_n x}+\cdots+\dfrac{a_0}{a_n x^n}\right) \\[0.25cm]
                \text{Or } \dfrac{a_{n-1}}{a_n x}, \ldots, \dfrac{a_0}{a_n x^n}
                \longrightarrow 0 \text{ quand } x \to \pm\infty \\[0.15cm]
                \text{donc le facteur entre parenthèses} \longrightarrow 1
                \end{array}
                """,
                font_size=25,
            ),
            box_width=11.3,
        )
        demonstration.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Voici l'idée de la démonstration : on met le terme de plus "
                "haut degré, a indice n, x puissance n, en facteur dans le "
                "polynôme. Chaque terme restant entre parenthèses contient "
                "alors une puissance négative de x, qui tend vers zéro "
                "quand x tend vers plus ou moins l'infini. Le facteur entre "
                "parenthèses tend donc vers un, et il ne reste que le terme "
                "de plus haut degré."
            )
        ) as tracker:
            self.play(FadeIn(demonstration))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(demonstration))

        consequence = theorem_box(
            MathTex(
                r"""
                \begin{array}{lll}
                n = p & \Longrightarrow &
                \lim\limits_{x\to\pm\infty} \dfrac{P(x)}{Q(x)} = \dfrac{a_n}{b_p} \ \ (\text{finie, non nulle}) \\[0.3cm]
                n < p & \Longrightarrow &
                \lim\limits_{x\to\pm\infty} \dfrac{P(x)}{Q(x)} = 0 \\[0.3cm]
                n > p & \Longrightarrow &
                \lim\limits_{x\to\pm\infty} \dfrac{P(x)}{Q(x)} = \pm\infty
                \end{array}
                """,
                font_size=26,
            ),
            box_width=10.5,
        )
        consequence.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "On en tire trois conséquences pratiques, selon les degrés n "
                "du numérateur et p du dénominateur. Si n égale p, la "
                "limite est le rapport des coefficients dominants, une "
                "valeur finie non nulle. Si n est strictement inférieur à "
                "p, la limite vaut zéro. Et si n est strictement supérieur "
                "à p, la limite est infinie, avec un signe à déterminer."
            )
        ) as tracker:
            self.play(FadeIn(consequence))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(consequence))

        # --- Exemple traité 3 : trois calculs ----------------------------------
        enonce_ex3 = Text(
            "Exemple 3 — calculer trois limites en +∞ ou -∞",
            font_size=25,
            color=YELLOW,
            weight="BOLD",
        )
        enonce_ex3.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Mettons cela en pratique sur trois exemples, un pour "
                "chaque cas de figure."
            )
        ) as tracker:
            self.play(FadeIn(enonce_ex3))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(enonce_ex3))

        cas_np = example_box(
            MathTex(
                r"""
                \lim_{x\to+\infty} \dfrac{3x^2-5x+1}{2x^2+x-7}
                = \lim_{x\to+\infty} \dfrac{3x^2}{2x^2} = \dfrac{3}{2}
                """,
                font_size=27,
            ),
            box_width=10.5,
        )
        cas_np.next_to(titre, DOWN, buff=0.55)

        with self.voiceover(
            text=(
                "Premier cas, n égale p : la limite en plus l'infini de "
                "trois x carré moins cinq x plus un, sur deux x carré plus "
                "x moins sept, a même limite que trois x carré sur deux x "
                "carré, soit trois demis."
            )
        ) as tracker:
            self.play(FadeIn(cas_np))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(cas_np))

        cas_ninfp = example_box(
            MathTex(
                r"""
                \lim_{x\to-\infty} \dfrac{2x+5}{x^2-3}
                = \lim_{x\to-\infty} \dfrac{2x}{x^2}
                = \lim_{x\to-\infty} \dfrac{2}{x} = 0
                """,
                font_size=27,
            ),
            box_width=10.5,
        )
        cas_ninfp.next_to(titre, DOWN, buff=0.55)

        with self.voiceover(
            text=(
                "Deuxième cas, n strictement inférieur à p : la limite en "
                "moins l'infini de deux x plus cinq, sur x carré moins "
                "trois, a même limite que deux x sur x carré, c'est-à-dire "
                "deux sur x, qui tend vers zéro."
            )
        ) as tracker:
            self.play(FadeIn(cas_ninfp))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(cas_ninfp))

        cas_nsupp = example_box(
            MathTex(
                r"""
                \lim_{x\to+\infty} \dfrac{x^3-4x}{x^2+1}
                = \lim_{x\to+\infty} \dfrac{x^3}{x^2}
                = \lim_{x\to+\infty} x = +\infty
                """,
                font_size=27,
            ),
            box_width=10.5,
        )
        cas_nsupp.next_to(titre, DOWN, buff=0.55)

        with self.voiceover(
            text=(
                "Troisième cas, n strictement supérieur à p : la limite en "
                "plus l'infini de x au cube moins quatre x, sur x carré "
                "plus un, a même limite que x cube sur x carré, c'est-à-dire "
                "x lui-même, qui tend vers plus l'infini."
            )
        ) as tracker:
            self.play(FadeIn(cas_nsupp))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(cas_nsupp))

        # --- À retenir -----------------------------------------------------
        retenir = essentiel_box(
            Text(
                _wrap(
                    "En ±∞, un polynôme ~ son terme de plus haut degré ; une "
                    "fraction rationnelle ~ le quotient des termes de plus "
                    "haut degré. Le résultat dépend de la comparaison n / p.",
                    width=58,
                ),
                font_size=23,
            )
        )
        retenir.next_to(titre, DOWN, buff=0.6)

        with self.voiceover(
            text=(
                "À retenir : en plus ou moins l'infini, un polynôme se "
                "comporte comme son terme de plus haut degré, et une "
                "fraction rationnelle comme le quotient des termes de plus "
                "haut degré du numérateur et du dénominateur. Le résultat "
                "final dépend uniquement de la comparaison des degrés n et "
                "p."
            )
        ) as tracker:
            self.play(FadeIn(retenir))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(retenir))

        # --- Piège à éviter --------------------------------------------------
        piege = warning_box(
            Text(
                _wrap(
                    "Piège : cette méthode du terme de plus haut degré ne "
                    "s'applique qu'en +∞ ou -∞. En un point fini x₀, il faut "
                    "une autre méthode (voir scène suivante).",
                    width=58,
                ),
                font_size=24,
            )
        )
        piege.next_to(titre, DOWN, buff=0.6)

        with self.voiceover(
            text=(
                "Attention : cette méthode du terme de plus haut degré ne "
                "fonctionne qu'aux bornes infinies, plus l'infini ou moins "
                "l'infini. En un point fini x zéro, il faudra une méthode "
                "différente, que nous verrons dans la scène suivante."
            )
        ) as tracker:
            self.play(FadeIn(piege))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(titre), FadeOut(piege))
