"""
scenes/Maths_GeneralitesFonctions_02.py — Chapitre 3 (1ereC, Maths), scène 02.

Parité des fonctions : fonctions paires, fonctions impaires, interprétation
graphique et conséquence pratique.
Source : 1ereC/Maths.pdf, chapitre 3, pages 28-40.
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
    Dot,
    DashedLine,
    FadeIn,
    FadeOut,
    MathTex,
    Text,
    VGroup,
    Write,
)

from shapes.base_scene import NotionScene
from shapes.boxes import definition_box, essentiel_box, property_box, scene_title, theorem_box, warning_box


def _wrap(text: str, width: int = 60) -> str:
    return "\n".join(textwrap.fill(line, width=width) for line in text.split("\n"))


class ParitesFonctions(NotionScene):
    def construct(self):
        titre = scene_title("Parité : fonctions paires, fonctions impaires")
        titre.scale(0.5)
        titre.to_edge(UP)

        # --- Énoncé : ensemble symétrique et fonction paire ------------------
        def_symetrique = definition_box(
            MathTex(
                r"D \text{ est symétrique par rapport à } 0 \ \Longleftrightarrow \ "
                r"\forall x \in D,\ -x \in D",
                font_size=28,
            )
        )
        def_symetrique.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Un ensemble D est symétrique par rapport à zéro lorsque, "
                "pour tout x appartenant à D, l'opposé de x appartient "
                "aussi à D."
            )
        ) as tracker:
            self.play(Write(titre))
            self.play(FadeIn(def_symetrique))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(def_symetrique))

        def_paire = definition_box(
            MathTex(
                r"""
                \begin{array}{l}
                f \text{ est paire sur } D_f \text{ si :} \\
                \bullet \ D_f \text{ est symétrique par rapport à } 0 \\
                \bullet \ \forall x \in D_f,\ f(-x) = f(x)
                \end{array}
                """,
                font_size=28,
            ),
            box_width=9.0,
        )
        def_paire.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Une fonction f est paire lorsque son ensemble de "
                "définition est symétrique par rapport à zéro, et que, "
                "pour tout x de Df, f de moins x est égal à f de x."
            )
        ) as tracker:
            self.play(FadeIn(def_paire))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(def_paire))

        # --- Animation du raisonnement : interprétation graphique paire ------
        axes_paire = Axes(
            x_range=[-3, 3, 1],
            y_range=[-1, 5, 1],
            x_length=5.2,
            y_length=3.2,
            axis_config={"color": WHITE, "font_size": 16},
        )
        axes_paire.next_to(titre, DOWN, buff=0.5).shift(LEFT * 3.0)
        courbe_paire = axes_paire.plot(lambda x: x**2, x_range=[-2.1, 2.1], color=YELLOW)
        M_paire = Dot(axes_paire.c2p(1.3, 1.69), color=WHITE)
        Mp_paire = Dot(axes_paire.c2p(-1.3, 1.69), color=WHITE)
        pointille_paire = DashedLine(M_paire.get_center(), Mp_paire.get_center(), color=WHITE)
        schema_paire = VGroup(axes_paire, courbe_paire, M_paire, Mp_paire, pointille_paire)

        theo_paire = theorem_box(
            Text(
                _wrap(
                    "Si f est paire, sa courbe Cf admet l'axe des "
                    "ordonnées comme axe de symétrie : M(x;f(x)) et "
                    "M'(-x;f(x)) sont symétriques par rapport à cet axe, "
                    "car f(-x) = f(x).",
                    width=42,
                ),
                font_size=21,
            ),
            box_width=6.2,
        )
        theo_paire.next_to(titre, DOWN, buff=0.5).shift(RIGHT * 3.3)

        with self.voiceover(
            text=(
                "Interprétation graphique : si f est paire, sa courbe "
                "admet l'axe des ordonnées comme axe de symétrie. En "
                "effet, le point M de coordonnées x et f de x, et le "
                "point M prime de coordonnées moins x et f de moins x, "
                "ont la même ordonnée puisque f de moins x égale f de x : "
                "ils sont donc symétriques par rapport à l'axe des "
                "ordonnées."
            )
        ) as tracker:
            self.play(FadeIn(schema_paire))
            self.play(FadeIn(theo_paire))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(schema_paire), FadeOut(theo_paire))

        # --- Fonction impaire --------------------------------------------
        def_impaire = definition_box(
            MathTex(
                r"""
                \begin{array}{l}
                f \text{ est impaire sur } D_f \text{ si :} \\
                \bullet \ D_f \text{ est symétrique par rapport à } 0 \\
                \bullet \ \forall x \in D_f,\ f(-x) = -f(x)
                \end{array}
                """,
                font_size=28,
            ),
            box_width=9.0,
        )
        def_impaire.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Une fonction f est impaire lorsque son ensemble de "
                "définition est symétrique par rapport à zéro, et que, "
                "pour tout x de Df, f de moins x est égal à l'opposé de f "
                "de x."
            )
        ) as tracker:
            self.play(FadeIn(def_impaire))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(def_impaire))

        axes_impaire = Axes(
            x_range=[-3, 3, 1],
            y_range=[-3, 3, 1],
            x_length=5.2,
            y_length=3.2,
            axis_config={"color": WHITE, "font_size": 16},
        )
        axes_impaire.next_to(titre, DOWN, buff=0.5).shift(LEFT * 3.0)
        courbe_impaire = axes_impaire.plot(lambda x: x**3 / 3, x_range=[-2.1, 2.1], color=YELLOW)
        M_imp = Dot(axes_impaire.c2p(1.5, 1.125), color=WHITE)
        Mp_imp = Dot(axes_impaire.c2p(-1.5, -1.125), color=WHITE)
        centre = Dot(axes_impaire.c2p(0, 0), color=WHITE, radius=0.05)
        schema_impaire = VGroup(axes_impaire, courbe_impaire, M_imp, Mp_imp, centre)

        theo_impaire = theorem_box(
            Text(
                _wrap(
                    "Si f est impaire, sa courbe Cf admet l'origine du "
                    "repère comme centre de symétrie : M(x;f(x)) et "
                    "M'(-x;-f(x)) sont symétriques par rapport à O, "
                    "car f(-x) = -f(x).",
                    width=42,
                ),
                font_size=21,
            ),
            box_width=6.2,
        )
        theo_impaire.next_to(titre, DOWN, buff=0.5).shift(RIGHT * 3.3)

        with self.voiceover(
            text=(
                "Interprétation graphique : si f est impaire, sa courbe "
                "admet l'origine du repère comme centre de symétrie. Le "
                "point M de coordonnées x et f de x, et le point M prime "
                "de coordonnées moins x et moins f de x, sont symétriques "
                "par rapport à l'origine O, car f de moins x égale moins f "
                "de x."
            )
        ) as tracker:
            self.play(FadeIn(schema_impaire))
            self.play(FadeIn(theo_impaire))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(schema_impaire), FadeOut(theo_impaire))

        # --- Exemple traité : conséquence pratique ---------------------------
        consequence = property_box(
            Text(
                _wrap(
                    "Conséquence pratique : si f est paire ou impaire, il "
                    "suffit de l'étudier sur Df ∩ ℝ+, puis de compléter "
                    "la courbe par la symétrie correspondante (axe des "
                    "ordonnées, ou origine du repère).",
                    width=56,
                ),
                font_size=24,
            ),
            box_width=10.8,
        )
        consequence.next_to(titre, DOWN, buff=0.6)

        with self.voiceover(
            text=(
                "Conséquence pratique très utile : si f est paire ou "
                "impaire, il suffit de l'étudier sur la partie positive de "
                "son ensemble de définition, Df intersecté avec ℝ plus, "
                "puis de compléter la courbe par la symétrie "
                "correspondante — cela divise le travail par deux."
            )
        ) as tracker:
            self.play(FadeIn(consequence))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(consequence))

        # --- À retenir ---------------------------------------------------
        retenir = essentiel_box(
            Text(
                _wrap(
                    "Paire : f(-x) = f(x), symétrie par rapport à l'axe "
                    "des ordonnées. Impaire : f(-x) = -f(x), symétrie par "
                    "rapport à l'origine. Toujours vérifier Df symétrique "
                    "avant de tester f(-x).",
                    width=56,
                ),
                font_size=24,
            ),
            box_width=11.0,
        )
        retenir.next_to(titre, DOWN, buff=0.6)

        with self.voiceover(
            text=(
                "À retenir : pour une fonction paire, f de moins x égale f "
                "de x, symétrie par rapport à l'axe des ordonnées. Pour "
                "une fonction impaire, f de moins x égale moins f de x, "
                "symétrie par rapport à l'origine. Dans les deux cas, on "
                "vérifie toujours en premier que Df est symétrique."
            )
        ) as tracker:
            self.play(FadeIn(retenir))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(retenir))

        # --- Piège à éviter ----------------------------------------------
        piege = warning_box(
            Text(
                _wrap(
                    "Piège : une fonction peut n'être ni paire ni impaire "
                    "— soit parce que Df n'est pas symétrique, soit parce "
                    "que f(-x) ne vaut ni f(x) ni -f(x). Ne pas conclure "
                    "trop vite.",
                    width=56,
                ),
                font_size=24,
            ),
            box_width=11.0,
        )
        piege.next_to(titre, DOWN, buff=0.6)

        with self.voiceover(
            text=(
                "Attention : une fonction peut très bien n'être ni paire "
                "ni impaire, soit parce que son ensemble de définition "
                "n'est pas symétrique, soit parce que f de moins x ne "
                "coïncide ni avec f de x ni avec l'opposé de f de x. La "
                "scène suivante donne des exemples précis de chaque cas."
            )
        ) as tracker:
            self.play(FadeIn(piege))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(titre), FadeOut(piege))
