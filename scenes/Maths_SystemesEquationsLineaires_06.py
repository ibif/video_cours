"""
scenes/Maths_SystemesEquationsLineaires_06.py — Chapitre 13 « Systèmes
d'équations linéaires dans ℝ² et ℝ³ » (1ereC, Maths), scène 06.

§ Systèmes 3×3 particuliers : infinité de solutions (exemple résolu 6,
paramétrage par λ) et aucune solution (exemple résolu 7, incompatibilité
0=1). Remarque : un système 3×3 admet toujours 0, 1 ou une infinité de
solutions (jamais exactement 2 ou 3).
Source : 1ereC/Maths.pdf, chapitre 13, pages 154-164.
"""

import textwrap

from manim import DOWN, LEFT, UP, FadeIn, FadeOut, MathTex, Text, VGroup, Write, YELLOW, RED

from shapes.base_scene import NotionScene
from shapes.boxes import definition_box, example_box, scene_title, warning_box


def _wrap(text: str, width: int = 56) -> str:
    return "\n".join(textwrap.fill(line, width=width) for line in text.split("\n"))


class SystemesInfiniteAucuneSolution(NotionScene):
    def construct(self):
        titre = scene_title("Systèmes 3×3 — Infinité ou aucune solution")
        titre.scale(0.5)
        titre.to_edge(UP)

        # --- Énoncé : mise en situation -----------------------------------------
        mise_en_situation = Text(
            _wrap(
                "Jusqu'ici, nos systèmes 3×3 avaient toujours une solution "
                "unique. Mais comme pour les systèmes 2×2, deux autres "
                "cas peuvent se produire : une infinité de solutions, ou "
                "bien aucune. Deux exemples très proches vont permettre de "
                "les distinguer.",
                width=58,
            ),
            font_size=24,
        )
        mise_en_situation.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Jusqu'ici, nos systèmes de trois équations avaient "
                "toujours une solution unique. Mais, comme pour les "
                "systèmes de deux équations, deux autres situations "
                "peuvent se produire : une infinité de solutions, ou bien "
                "aucune solution du tout. Deux exemples très proches, ne "
                "différant que par un seul nombre, vont nous permettre de "
                "bien les distinguer."
            )
        ) as tracker:
            self.play(Write(titre))
            self.play(FadeIn(mise_en_situation))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(mise_en_situation))

        # --- Exemple résolu 6 : infinité de solutions ------------------------------
        ex6_L = MathTex(
            r"""
            \begin{cases}
            x - z = 8 \\
            y + 3z = -2 \\
            x + y + 2z = 6
            \end{cases}
            """,
            font_size=26,
        )
        ex6_combinaison = MathTex(
            r"L_3 - L_1 - L_2 : \quad 0x+0y+0z = 6-8-(-2) = 0 \quad (\text{toujours vrai})",
            font_size=21,
        )
        ex6_dependance = Text(
            "La 3e équation est une conséquence des deux premières :\nelle n'apporte aucune information nouvelle.",
            font_size=21,
        )
        ex6_param = MathTex(
            r"\text{On pose } z=\lambda \ (\lambda\in\mathbb{R}) : \quad x=8+\lambda, \quad y=-2-3\lambda",
            font_size=23,
        )
        ex6_concl = MathTex(
            r"\mathcal{S} = \big\{\, (8+\lambda\,;\,-2-3\lambda\,;\,\lambda) \ ,\ \lambda \in \mathbb{R} \,\big\}",
            font_size=25,
            color=YELLOW,
        )
        ex6 = VGroup(ex6_L, ex6_combinaison, ex6_dependance, ex6_param, ex6_concl).arrange(
            DOWN, buff=0.24
        )
        ex6_box = example_box(ex6, box_width=12.2)
        ex6_box.scale(0.8)
        ex6_box.next_to(titre, DOWN, buff=0.3)

        with self.voiceover(
            text=(
                "Premier exemple : x moins z égale huit, y plus trois z "
                "égale moins deux, x plus y plus deux z égale six. En "
                "calculant L3 moins L1 moins L2, tous les termes en x, y et "
                "z s'annulent, et il reste zéro égale six moins huit, "
                "moins moins deux, c'est-à-dire zéro égale zéro, ce qui est "
                "toujours vrai. La troisième équation est donc une "
                "conséquence des deux premières : elle n'apporte aucune "
                "information nouvelle. Il ne reste que deux équations "
                "indépendantes pour trois inconnues : on pose alors z égale "
                "lambda, un réel quelconque, et on exprime x et y en "
                "fonction de lambda grâce aux deux premières équations : x "
                "égale huit plus lambda, y égale moins deux moins trois "
                "lambda. L'ensemble des solutions est une infinité de "
                "triplets, un pour chaque valeur de lambda."
            )
        ) as tracker:
            self.play(FadeIn(ex6_box))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(ex6_box))

        # --- Exemple résolu 7 : aucune solution ------------------------------------
        ex7_L = MathTex(
            r"""
            \begin{cases}
            x - z = 8 \\
            y + 3z = -2 \\
            x + y + 2z = 7
            \end{cases}
            """,
            font_size=26,
        )
        ex7_note = Text(
            "(le même système, mais avec 7 au lieu de 6 dans la 3e équation)",
            font_size=20,
        )
        ex7_combinaison = MathTex(
            r"L_3 - L_1 - L_2 : \quad 0x+0y+0z = 7-8-(-2) = 1",
            font_size=22,
        )
        ex7_absurde = MathTex(r"0 = 1 \quad \text{(FAUX, quels que soient } x,y,z)", font_size=26, color=RED)
        ex7_concl = MathTex(r"\mathcal{S} = \varnothing", font_size=28, color=YELLOW)
        ex7 = VGroup(ex7_L, ex7_note, ex7_combinaison, ex7_absurde, ex7_concl).arrange(DOWN, buff=0.26)
        ex7_box = example_box(ex7, box_width=12.0)
        ex7_box.scale(0.85)
        ex7_box.next_to(titre, DOWN, buff=0.3)

        with self.voiceover(
            text=(
                "Second exemple, presque identique : seul le second membre "
                "de la troisième équation change, sept au lieu de six. On "
                "refait le même calcul, L3 moins L1 moins L2 : il reste "
                "cette fois zéro égale sept moins huit, moins moins deux, "
                "soit zéro égale un. Or zéro n'est jamais égal à un, quels "
                "que soient x, y et z : les trois équations sont "
                "incompatibles entre elles. L'ensemble des solutions est "
                "donc l'ensemble vide : ce système n'a aucune solution."
            )
        ) as tracker:
            self.play(FadeIn(ex7_box))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(ex7_box))

        # --- À retenir -------------------------------------------------------------
        retenir = definition_box(
            VGroup(
                Text("À retenir", font_size=23, weight="BOLD"),
                Text(
                    _wrap(
                        "Une combinaison des équations qui donne 0 = 0 → "
                        "infinité de solutions (paramétrer avec λ). Une "
                        "combinaison qui donne 0 = k, k ≠ 0 → aucune "
                        "solution.",
                        width=48,
                    ),
                    font_size=21,
                ),
            ).arrange(DOWN, buff=0.24),
            box_width=11.8,
        )
        retenir.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "À retenir : si une combinaison des équations conduit à "
                "zéro égale zéro, une identité toujours vraie, le système a "
                "une infinité de solutions, que l'on décrit avec un "
                "paramètre lambda. Si elle conduit à zéro égale un nombre "
                "non nul, une absurdité, le système n'a aucune solution."
            )
        ) as tracker:
            self.play(FadeIn(retenir))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(retenir))

        # --- Remarque / piège --------------------------------------------------------
        remarque = warning_box(
            Text(
                "Un système linéaire 3×3 admet toujours 0, 1 ou une infinité de\n"
                "solutions — JAMAIS exactement 2 ou 3 solutions. Si un calcul\n"
                "semble en donner 2 ou 3, il contient une erreur.",
                font_size=22,
            ),
            box_width=12.0,
        )
        remarque.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Remarque essentielle, valable pour tout système linéaire à "
                "trois inconnues : il admet toujours zéro solution, une "
                "seule solution, ou une infinité de solutions, mais jamais "
                "exactement deux ou trois solutions. Si un calcul semble en "
                "donner deux ou trois, c'est le signe certain d'une erreur "
                "quelque part."
            )
        ) as tracker:
            self.play(FadeIn(remarque))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(remarque), FadeOut(titre))
