"""
scenes/Maths_SuitesNumeriques_09.py — Chapitre 15 « Suites numériques »
(1ereC, Maths), scène 09.

Somme de termes consécutifs d'une suite géométrique : théorème,
démonstration par télescopage (S - qS), cas particulier 1+q+...+qⁿ, cas
q = 1. Exemple résolu 9.
Source : 1ereC/Maths.pdf, chapitre 15, pages 176-188.
"""

import textwrap

from manim import DOWN, UP, FadeIn, FadeOut, MathTex, Text, VGroup, Write, YELLOW

from shapes.base_scene import NotionScene
from shapes.boxes import essentiel_box, example_box, scene_title, theorem_box, warning_box


def _wrap(text: str, width: int = 58) -> str:
    return "\n".join(textwrap.fill(line, width=width) for line in text.split("\n"))


class SommeSuiteGeometrique(NotionScene):
    def construct(self):
        titre = scene_title("Somme de termes consécutifs — suite géométrique")
        titre.scale(0.44)
        titre.to_edge(UP)
        self.play(Write(titre))

        # --- Énoncé : théorème -------------------------------------------------
        theo = theorem_box(
            VGroup(
                Text(
                    "Pour q ≠ 1, la somme S de termes consécutifs d'une suite\n"
                    "géométrique de raison q se calcule ainsi :",
                    font_size=21,
                ),
                MathTex(
                    r"S = \text{premier terme}\times\dfrac{1-q^{\,\text{nb de termes}}}{1-q}",
                    font_size=26,
                ),
                MathTex(
                    r"\text{Cas particulier : } 1+q+q^2+\cdots+q^n = \dfrac{1-q^{\,n+1}}{1-q}",
                    font_size=25,
                ),
            ).arrange(DOWN, buff=0.3),
            box_width=11.6,
        )
        theo.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Théorème, valable dès que q est différent de un : la "
                "somme S de plusieurs termes consécutifs d'une suite "
                "géométrique de raison q vaut le premier terme, multiplié "
                "par un moins q puissance le nombre de termes, le tout "
                "divisé par un moins q. Cas particulier utile : un plus q "
                "plus q carré, et ainsi de suite jusqu'à q puissance n, "
                "vaut un moins q puissance n plus un, sur un moins q."
            )
        ) as tracker:
            self.play(FadeIn(theo))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(theo))

        # --- Démonstration : télescopage --------------------------------------
        demo_titre = Text(
            "Démonstration — méthode du télescopage (S - qS) :",
            font_size=22,
            color=YELLOW,
            weight="BOLD",
        )
        demo_titre.next_to(titre, DOWN, buff=0.4)
        demo = VGroup(
            MathTex(r"S = u_0+u_0q+u_0q^2+\cdots+u_0q^{n}", font_size=23),
            MathTex(r"qS = u_0q+u_0q^2+\cdots+u_0q^{n}+u_0q^{n+1}", font_size=23),
            Text(
                "En soustrayant, tous les termes intermédiaires s'annulent :",
                font_size=20,
            ),
            MathTex(
                r"S-qS = u_0-u_0q^{n+1} \Longrightarrow S(1-q)=u_0(1-q^{n+1})",
                font_size=24,
            ),
            MathTex(
                r"\Longrightarrow S = u_0\times\dfrac{1-q^{n+1}}{1-q} \quad (q\neq 1)",
                font_size=25,
            ),
        ).arrange(DOWN, buff=0.2)
        demo.next_to(demo_titre, DOWN, buff=0.3)

        with self.voiceover(
            text=(
                "Démonstration par télescopage : on écrit S, la somme des "
                "n plus un premiers termes, puis q fois S, qui décale tous "
                "les termes d'un cran. En soustrayant ces deux lignes, "
                "tous les termes intermédiaires s'annulent deux à deux, et "
                "il ne reste que le tout premier terme, moins le tout "
                "dernier terme multiplié par q. On obtient S fois un moins "
                "q égale u zéro fois un moins q puissance n plus un, d'où "
                "la formule, valable dès que q est différent de un."
            )
        ) as tracker:
            self.play(FadeIn(demo_titre))
            self.play(FadeIn(demo))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(demo_titre), FadeOut(demo))

        # --- Cas q = 1 -----------------------------------------------------------
        cas_q1 = MathTex(
            r"\text{Si } q=1 : \ (u_n) \text{ est constante, } S = (\text{nombre de termes})\times u_0",
            font_size=25,
        )
        cas_q1.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Cas particulier, si q vaut un : la suite est en réalité "
                "constante, et la formule précédente ne s'applique plus, "
                "car on diviserait par zéro. La somme est alors simplement "
                "le nombre de termes, multiplié par la valeur constante u "
                "zéro."
            )
        ) as tracker:
            self.play(FadeIn(cas_q1))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(cas_q1))

        # --- Exemple résolu 9 ----------------------------------------------------
        ex9_titre = Text(
            "Exemple 9 — S = 2 + 6 + 18 + ... + 1458 :",
            font_size=24,
            color=YELLOW,
            weight="BOLD",
        )
        ex9_titre.next_to(titre, DOWN, buff=0.4)
        ex9_calc = example_box(
            VGroup(
                MathTex(
                    r"q=3, \quad 1458=2\times 3^{n-1} \Longrightarrow 3^{n-1}=729=3^6 \Longrightarrow n=7 \text{ termes}",
                    font_size=21,
                ),
                MathTex(
                    r"S = 2\times\dfrac{1-3^{7}}{1-3} = 2\times\dfrac{-2186}{-2} = 2186",
                    font_size=26,
                ),
            ).arrange(DOWN, buff=0.3),
            box_width=11.6,
        )
        ex9_calc.next_to(ex9_titre, DOWN, buff=0.3)

        with self.voiceover(
            text=(
                "Exemple : calculons S égale deux plus six plus dix-huit, "
                "et ainsi de suite, jusqu'à mille quatre cent "
                "cinquante-huit. La raison vaut trois. On détermine le "
                "nombre de termes : mille quatre cent cinquante-huit égale "
                "deux fois trois puissance n moins un, ce qui donne trois "
                "puissance six, donc sept termes au total. La somme vaut "
                "alors deux fois un moins trois puissance sept, sur un "
                "moins trois, soit deux mille cent quatre-vingt-six."
            )
        ) as tracker:
            self.play(FadeIn(ex9_titre))
            self.play(FadeIn(ex9_calc))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(ex9_titre), FadeOut(ex9_calc))

        # --- À retenir -----------------------------------------------------------
        retenir = essentiel_box(
            Text(
                _wrap(
                    "Somme géométrique (q ≠ 1) = premier terme × (1 - "
                    "q^(nombre de termes)) / (1 - q). Si q = 1 : somme = "
                    "nombre de termes × valeur constante.",
                    width=58,
                ),
                font_size=22,
            ),
            box_width=11.3,
        )
        retenir.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "À retenir : la somme géométrique se calcule avec le "
                "premier terme, la raison et le nombre de termes — jamais "
                "avec q égal à un dans cette formule, un cas à traiter à "
                "part."
            )
        ) as tracker:
            self.play(FadeIn(retenir))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(retenir))

        # --- Piège à éviter ----------------------------------------------------
        piege = warning_box(
            Text(
                _wrap(
                    "Piège : dans qⁿ de la formule, l'exposant est le "
                    "NOMBRE DE TERMES de la somme, pas le dernier indice "
                    "n. Et la formule ne s'applique jamais telle quelle si "
                    "q = 1 (division par zéro).",
                    width=56,
                ),
                font_size=21,
            ),
            box_width=11.2,
        )
        piege.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Double piège à éviter : l'exposant qui apparaît dans la "
                "formule est le nombre de termes additionnés, et non le "
                "dernier indice de la suite — les deux coïncident "
                "rarement. Et surtout, cette formule ne s'applique jamais "
                "telle quelle si q vaut un, sous peine de diviser par "
                "zéro."
            )
        ) as tracker:
            self.play(FadeIn(piege))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(piege), FadeOut(titre))
