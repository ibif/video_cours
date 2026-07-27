"""
scenes/Maths_SuitesNumeriques_07.py — Chapitre 15 « Suites numériques »
(1ereC, Maths), scène 07.

Somme de termes consécutifs d'une suite arithmétique : théorème,
démonstration par la « méthode du petit Gauss », cas particulier de la
somme des n premiers entiers. Exemple résolu 7.
Source : 1ereC/Maths.pdf, chapitre 15, pages 176-188.
"""

import textwrap

from manim import DOWN, UP, FadeIn, FadeOut, MathTex, Text, VGroup, Write, YELLOW

from shapes.base_scene import NotionScene
from shapes.boxes import essentiel_box, example_box, scene_title, theorem_box, warning_box


def _wrap(text: str, width: int = 58) -> str:
    return "\n".join(textwrap.fill(line, width=width) for line in text.split("\n"))


class SommeSuiteArithmetique(NotionScene):
    def construct(self):
        titre = scene_title("Somme de termes consécutifs — suite arithmétique")
        titre.scale(0.44)
        titre.to_edge(UP)
        self.play(Write(titre))

        # --- Énoncé : théorème -------------------------------------------------
        theo = theorem_box(
            VGroup(
                Text(
                    "La somme S de termes consécutifs d'une suite arithmétique\n"
                    "se calcule ainsi :",
                    font_size=22,
                ),
                MathTex(
                    r"S = (\text{nombre de termes}) \times \dfrac{\text{premier terme}+\text{dernier terme}}{2}",
                    font_size=25,
                ),
                MathTex(
                    r"\text{Cas particulier : } 1+2+\cdots+n = \dfrac{n(n+1)}{2}",
                    font_size=27,
                ),
            ).arrange(DOWN, buff=0.3),
            box_width=11.6,
        )
        theo.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Théorème : la somme S de plusieurs termes consécutifs "
                "d'une suite arithmétique est toujours égale au nombre de "
                "termes additionnés, multiplié par la demi-somme du "
                "premier et du dernier terme. Cas particulier très utile : "
                "la somme des n premiers entiers naturels non nuls vaut n "
                "fois n plus un, le tout divisé par deux."
            )
        ) as tracker:
            self.play(FadeIn(theo))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(theo))

        # --- Démonstration : méthode du petit Gauss --------------------------------
        demo_titre = Text(
            "Démonstration — méthode du petit Gauss :",
            font_size=23,
            color=YELLOW,
            weight="BOLD",
        )
        demo_titre.next_to(titre, DOWN, buff=0.4)
        demo = VGroup(
            MathTex(r"S = u_0 + u_1 + \cdots + u_n", font_size=25),
            MathTex(r"S = u_n + u_{n-1} + \cdots + u_0 \ \text{(à l'envers)}", font_size=25),
            Text(
                "En additionnant les deux lignes terme à terme, chaque\n"
                "colonne vaut u0 + un (les termes équidistants des bords) :",
                font_size=21,
            ),
            MathTex(
                r"2S = (n+1)\times(u_0+u_n) \Longrightarrow S = (n+1)\times\dfrac{u_0+u_n}{2}",
                font_size=25,
            ),
        ).arrange(DOWN, buff=0.25)
        demo.next_to(demo_titre, DOWN, buff=0.3)

        with self.voiceover(
            text=(
                "Petite astuce attribuée au jeune Gauss : on écrit la somme "
                "S une première fois dans l'ordre, puis une seconde fois à "
                "l'envers. En additionnant ces deux écritures colonne par "
                "colonne, chaque paire de termes vaut exactement u zéro "
                "plus u indice n, et il y a n plus un colonnes. On obtient "
                "donc deux S égale n plus un fois u zéro plus u indice n, "
                "d'où la formule de la somme."
            )
        ) as tracker:
            self.play(FadeIn(demo_titre))
            self.play(FadeIn(demo))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(demo_titre), FadeOut(demo))

        # --- Exemple résolu 7 ----------------------------------------------------
        ex7_titre = Text(
            "Exemple 7 — S = 5 + 8 + 11 + ... + 62 :",
            font_size=24,
            color=YELLOW,
            weight="BOLD",
        )
        ex7_titre.next_to(titre, DOWN, buff=0.4)
        ex7_calc = example_box(
            VGroup(
                MathTex(
                    r"r=3, \quad 62 = 5+(n-1)\times 3 \Longrightarrow n=20 \text{ termes}",
                    font_size=25,
                ),
                MathTex(
                    r"S = 20\times\dfrac{5+62}{2} = 20\times\dfrac{67}{2} = 670",
                    font_size=27,
                ),
            ).arrange(DOWN, buff=0.3),
            box_width=10.4,
        )
        ex7_calc.next_to(ex7_titre, DOWN, buff=0.3)

        with self.voiceover(
            text=(
                "Exemple : calculons S égale cinq plus huit plus onze, et "
                "ainsi de suite, jusqu'à soixante-deux. La raison vaut "
                "trois. On détermine le nombre de termes : soixante-deux "
                "égale cinq plus, n moins un, fois trois, ce qui donne "
                "vingt termes. La somme vaut donc vingt fois la demi-somme "
                "de cinq et soixante-deux, soit vingt fois trente-trois "
                "virgule cinq, égale six cent soixante-dix."
            )
        ) as tracker:
            self.play(FadeIn(ex7_titre))
            self.play(FadeIn(ex7_calc))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(ex7_titre), FadeOut(ex7_calc))

        # --- À retenir -----------------------------------------------------------
        retenir = essentiel_box(
            Text(
                _wrap(
                    "Somme arithmétique = (nombre de termes) × (premier + "
                    "dernier) / 2. Toujours compter précisément le nombre "
                    "de termes avant d'appliquer la formule.",
                    width=56,
                ),
                font_size=22,
            ),
            box_width=10.8,
        )
        retenir.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "À retenir : la somme de termes consécutifs d'une suite "
                "arithmétique s'obtient toujours par le nombre de termes, "
                "multiplié par la demi-somme du premier et du dernier "
                "terme. L'étape la plus délicate est souvent de bien "
                "compter le nombre de termes additionnés."
            )
        ) as tracker:
            self.play(FadeIn(retenir))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(retenir))

        # --- Piège à éviter ----------------------------------------------------
        piege = warning_box(
            Text(
                _wrap(
                    "Piège classique : le nombre de termes de u_p à u_n "
                    "est (n - p + 1), pas (n - p). Un oubli du « +1 » est "
                    "l'erreur la plus fréquente dans le calcul d'une somme.",
                    width=56,
                ),
                font_size=22,
            ),
            box_width=11.2,
        )
        piege.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Piège à éviter, très fréquent : le nombre de termes entre "
                "u indice p et u indice n, bornes incluses, vaut n moins p "
                "plus un, et non pas n moins p. Oublier ce plus un fausse "
                "systématiquement le résultat de la somme."
            )
        ) as tracker:
            self.play(FadeIn(piege))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(piege), FadeOut(titre))
