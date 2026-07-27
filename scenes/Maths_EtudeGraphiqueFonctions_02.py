"""
scenes/Maths_EtudeGraphiqueFonctions_02.py — Chapitre 11 (1ereC, Maths), scène 02.

Ensemble de définition (règles pratiques) et réduction du domaine d'étude
par parité ou périodicité : définitions fonction paire / impaire /
périodique, exemple résolu de Df pour une fonction rationnelle, exemple de
parité pour (x²-1)/(x²+1).
Source : 1ereC/Maths.pdf, chapitre 11, pages 130-141.
"""

import textwrap

from manim import DOWN, LEFT, RIGHT, UP, WHITE, YELLOW, Axes, DashedLine, Dot, FadeIn, FadeOut, MathTex, Text, VGroup, Write

from shapes.base_scene import NotionScene
from shapes.boxes import definition_box, essentiel_box, example_box, scene_title, warning_box


def _wrap(text: str, width: int = 58) -> str:
    return "\n".join(textwrap.fill(line, width=width) for line in text.split("\n"))


class EnsembleDefinitionReductionDomaine(NotionScene):
    def construct(self):
        titre = scene_title("Ensemble de définition et réduction du domaine")
        titre.scale(0.42)
        titre.to_edge(UP)

        # --- Énoncé ------------------------------------------------------------
        enonce = Text(
            "Étapes 1 et 2 : Df, puis parité et périodicité",
            font_size=26,
            color=YELLOW,
            weight="BOLD",
        )
        enonce.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Revenons en détail sur les deux premières étapes du plan "
                "d'étude : déterminer l'ensemble de définition, puis "
                "chercher une éventuelle parité ou périodicité pour réduire "
                "le domaine réellement étudié."
            )
        ) as tracker:
            self.play(Write(titre))
            self.play(FadeIn(enonce))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(enonce))

        # --- Règles pratiques de Df ---------------------------------------------
        regles = definition_box(
            MathTex(
                r"""
                \begin{array}{ll}
                \dfrac{u(x)}{v(x)} & v(x) \neq 0 \\
                \sqrt{u(x)} & u(x) \geq 0 \\
                \dfrac{1}{\sqrt{u(x)}} & u(x) > 0 \\
                \tan(x) & x \neq \dfrac{\pi}{2}+k\pi,\ k \in \mathbb{Z}
                \end{array}
                """,
                font_size=28,
            ),
            box_width=9.5,
        )
        regles.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Quatre règles pratiques à connaître par cœur. Un quotient "
                "est défini là où le dénominateur est différent de zéro. "
                "Une racine carrée est définie là où l'expression sous la "
                "racine est positive ou nulle. Si cette racine est de plus "
                "au dénominateur, la condition devient stricte : "
                "strictement positive. Et la tangente de x est définie tant "
                "que x est différent de pi sur deux, plus k pi, pour k "
                "entier relatif."
            )
        ) as tracker:
            self.play(FadeIn(regles))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(regles))

        # --- Définitions parité / périodicité -----------------------------------
        def_parite = definition_box(
            Text(
                _wrap(
                    "f est paire si Df est symétrique par rapport à 0 et si "
                    "f(-x) = f(x) pour tout x de Df : Cf est symétrique par "
                    "rapport à l'axe des ordonnées. f est impaire si Df est "
                    "symétrique par rapport à 0 et si f(-x) = -f(x) : Cf est "
                    "symétrique par rapport à l'origine O.",
                    width=58,
                ),
                font_size=22,
            ),
            box_width=11.4,
        )
        def_parite.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Une fonction f est dite paire si son ensemble de "
                "définition est symétrique par rapport à zéro, et si f de "
                "moins x égale f de x pour tout x du domaine : sa courbe "
                "est alors symétrique par rapport à l'axe des ordonnées. "
                "Elle est dite impaire si le domaine est symétrique par "
                "rapport à zéro, et si f de moins x égale moins f de x : sa "
                "courbe est alors symétrique par rapport à l'origine O."
            )
        ) as tracker:
            self.play(FadeIn(def_parite))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(def_parite))

        def_periode = definition_box(
            MathTex(
                r"f \text{ périodique de période } T \Longleftrightarrow "
                r"f(x+T) = f(x) \ \ \forall x \in D_f",
                font_size=28,
            ),
            box_width=10.5,
        )
        def_periode.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Une fonction f est périodique de période T si f de x plus "
                "T est égal à f de x pour tout x du domaine. On peut alors "
                "réduire l'étude à un seul intervalle de longueur T, puis "
                "compléter la courbe par translations successives."
            )
        ) as tracker:
            self.play(FadeIn(def_periode))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(def_periode))

        # --- Exemple traité 1 : Df d'une fonction rationnelle -------------------
        enonce_ex1 = Text(
            "Exemple 1 — ensemble de définition de f(x) = (2x+1)/(x²-4)",
            font_size=24,
            color=YELLOW,
            weight="BOLD",
        )
        enonce_ex1.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Exemple : déterminons l'ensemble de définition de f de x "
                "égale deux x plus un, sur x carré moins quatre."
            )
        ) as tracker:
            self.play(FadeIn(enonce_ex1))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(enonce_ex1))

        calcul_ex1 = example_box(
            MathTex(
                r"""
                \begin{array}{l}
                x^2-4 = 0 \ \Longleftrightarrow \ x^2=4 \ \Longleftrightarrow \ x=-2 \text{ ou } x=2 \\
                D_f = \mathbb{R} \setminus \{-2\,;2\}
                \end{array}
                """,
                font_size=28,
            ),
            box_width=8.5,
        )
        calcul_ex1.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Le dénominateur x carré moins quatre s'annule quand x "
                "carré égale quatre, c'est-à-dire pour x égale moins deux "
                "ou x égale deux. Donc Df est ℝ privé de moins deux et de "
                "deux."
            )
        ) as tracker:
            self.play(FadeIn(calcul_ex1))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(calcul_ex1))

        # --- Exemple traité 2 : parité de (x²-1)/(x²+1) -------------------------
        enonce_ex2 = Text(
            "Exemple 2 — parité de f(x) = (x²-1)/(x²+1)",
            font_size=25,
            color=YELLOW,
            weight="BOLD",
        )
        enonce_ex2.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Deuxième exemple : étudions la parité de f de x égale x "
                "carré moins un, sur x carré plus un."
            )
        ) as tracker:
            self.play(FadeIn(enonce_ex2))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(enonce_ex2))

        calcul_ex2 = example_box(
            MathTex(
                r"""
                \begin{array}{l}
                D_f = \mathbb{R} \text{ (symétrique par rapport à 0)} \\
                f(-x) = \dfrac{(-x)^2-1}{(-x)^2+1} = \dfrac{x^2-1}{x^2+1} = f(x) \\
                \Longrightarrow \ f \text{ est paire}
                \end{array}
                """,
                font_size=26,
            ),
            box_width=9.5,
        )
        calcul_ex2.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "D'abord, Df vaut ℝ tout entier, qui est bien symétrique "
                "par rapport à zéro : la question de la parité a donc un "
                "sens. Ensuite, f de moins x égale moins x au carré moins "
                "un, sur moins x au carré plus un, ce qui se simplifie en x "
                "carré moins un sur x carré plus un, exactement f de x. La "
                "fonction est donc paire."
            )
        ) as tracker:
            self.play(FadeIn(calcul_ex2))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(calcul_ex2))

        # petit schéma illustrant la symétrie d'axe (Oy)
        axes = Axes(
            x_range=[-3, 3, 1], y_range=[-1, 1, 1], x_length=5.5, y_length=2.8,
            axis_config={"color": WHITE, "font_size": 16},
        )
        axes.move_to(titre.get_center() + DOWN * 3.2)
        courbe = axes.plot(lambda x: (x**2 - 1) / (x**2 + 1), x_range=[-3, 3], color="#1E90FF")
        M = Dot(axes.c2p(1.6, (1.6**2 - 1) / (1.6**2 + 1)), color=WHITE)
        Mp = Dot(axes.c2p(-1.6, (1.6**2 - 1) / (1.6**2 + 1)), color=WHITE)
        pointille = DashedLine(M.get_center(), Mp.get_center(), color=WHITE)
        schema = VGroup(axes, courbe, M, Mp, pointille)

        with self.voiceover(
            text=(
                "Sur la courbe, cette parité se traduit par une symétrie "
                "par rapport à l'axe des ordonnées : les points d'abscisses "
                "opposées ont la même image."
            )
        ) as tracker:
            self.play(FadeIn(schema))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(schema))

        # --- À retenir ---------------------------------------------------------
        retenir = essentiel_box(
            Text(
                _wrap(
                    "Toujours calculer Df d'abord. Si Df est symétrique par "
                    "rapport à 0, tester f(-x) : égal à f(x) → paire "
                    "(symétrie /axe Oy), égal à -f(x) → impaire (symétrie "
                    "/origine O). Sinon, réduire l'étude à un demi-domaine.",
                    width=58,
                ),
                font_size=22,
            ),
            box_width=11.4,
        )
        retenir.next_to(titre, DOWN, buff=0.6)

        with self.voiceover(
            text=(
                "À retenir : on calcule toujours Df en premier. Si ce "
                "domaine est symétrique par rapport à zéro, on teste f de "
                "moins x. S'il est égal à f de x, la fonction est paire, "
                "symétrie d'axe Oy. S'il est égal à moins f de x, elle est "
                "impaire, symétrie de centre O. Dans les deux cas, on peut "
                "réduire l'étude à la moitié positive du domaine."
            )
        ) as tracker:
            self.play(FadeIn(retenir))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(retenir))

        # --- Piège à éviter ------------------------------------------------
        piege = warning_box(
            Text(
                _wrap(
                    "Piège : ne jamais tester la parité avant d'avoir "
                    "vérifié que Df est symétrique par rapport à 0. Si Df "
                    "n'est pas symétrique, f n'est ni paire ni impaire, "
                    "point final — inutile de calculer f(-x).",
                    width=58,
                ),
                font_size=22,
            ),
            box_width=11.0,
        )
        piege.next_to(titre, DOWN, buff=0.6)

        with self.voiceover(
            text=(
                "Piège fréquent : ne jamais tester la parité avant d'avoir "
                "vérifié que le domaine est symétrique par rapport à zéro. "
                "Si Df n'est pas symétrique, la fonction n'est ni paire ni "
                "impaire, un point c'est tout — il est inutile, et même "
                "trompeur, de calculer f de moins x dans ce cas."
            )
        ) as tracker:
            self.play(FadeIn(piege))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(titre), FadeOut(piege))
