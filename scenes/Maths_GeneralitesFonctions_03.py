"""
scenes/Maths_GeneralitesFonctions_03.py — Chapitre 3 (1ereC, Maths), scène 03.

Exemple d'étude de parité sur quatre fonctions, puis périodicité :
définition, interprétation graphique, exemples fondamentaux (sin, cos,
tan, mantisse) et exemple résolu.
Source : 1ereC/Maths.pdf, chapitre 3, pages 28-40.
"""

import textwrap

import numpy as np
from manim import (
    DOWN,
    LEFT,
    RIGHT,
    UP,
    WHITE,
    YELLOW,
    Arrow,
    Axes,
    FadeIn,
    FadeOut,
    MathTex,
    Text,
    VGroup,
    Write,
)

from shapes.base_scene import NotionScene
from shapes.boxes import definition_box, essentiel_box, example_box, scene_title, theorem_box, warning_box


def _wrap(text: str, width: int = 60) -> str:
    return "\n".join(textwrap.fill(line, width=width) for line in text.split("\n"))


class ExempleParitePeriodicite(NotionScene):
    def construct(self):
        titre = scene_title("Exemple de parité — périodicité")
        titre.scale(0.55)
        titre.to_edge(UP)
        self.play(Write(titre))

        # --- Énoncé : exemple 3, étudier la parité de 4 fonctions ------------
        enonce = Text(
            "Exemple 3 — étudier la parité de :",
            font_size=25,
            color=YELLOW,
            weight="BOLD",
        )
        enonce.next_to(titre, DOWN, buff=0.4)

        fonctions = MathTex(
            r"""
            \begin{array}{ll}
            f(x) = 3x^4-2x^2+1 & g(x) = \dfrac{x}{x^2-1} \\[0.3em]
            h(x) = \dfrac{1}{(x-1)(x+3)} & k(x) = x^2+x
            \end{array}
            """,
            font_size=30,
        )
        fonctions.next_to(enonce, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Exemple : étudions la parité de quatre fonctions. f de x "
                "égale trois x puissance quatre moins deux x carré plus "
                "un ; g de x égale x sur x carré moins un ; h de x égale "
                "un sur x moins un fois x plus trois ; et k de x égale x "
                "carré plus x."
            )
        ) as tracker:
            self.play(FadeIn(enonce))
            self.play(Write(fonctions))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(enonce), FadeOut(fonctions))

        # --- Animation du raisonnement : les 4 cas ---------------------------
        cas_f = example_box(
            MathTex(
                r"D_f = \mathbb{R} \text{ (symétrique)}, \quad "
                r"f(-x)=3x^4-2x^2+1=f(x) \ \Longrightarrow \ f \text{ paire}",
                font_size=24,
            ),
            box_width=11.0,
        )
        cas_f.next_to(titre, DOWN, buff=0.55)

        with self.voiceover(
            text=(
                "f est définie sur ℝ, un ensemble symétrique. On calcule f "
                "de moins x, qui redonne exactement trois x puissance "
                "quatre moins deux x carré plus un, donc f de moins x "
                "égale f de x : f est paire."
            )
        ) as tracker:
            self.play(FadeIn(cas_f))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(cas_f))

        cas_g = example_box(
            MathTex(
                r"D_g = \mathbb{R}\setminus\{-1;1\} \text{ (symétrique)}, \quad "
                r"g(-x)=\dfrac{-x}{x^2-1}=-g(x) \ \Longrightarrow \ g \text{ impaire}",
                font_size=24,
            ),
            box_width=11.2,
        )
        cas_g.next_to(titre, DOWN, buff=0.55)

        with self.voiceover(
            text=(
                "g est définie sur ℝ privé de moins un et de un, un "
                "ensemble symétrique. g de moins x vaut moins x sur x "
                "carré moins un, soit exactement l'opposé de g de x : g "
                "est impaire."
            )
        ) as tracker:
            self.play(FadeIn(cas_g))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(cas_g))

        cas_h = example_box(
            Text(
                _wrap(
                    "Dh = ℝ\\{1 ; −3}. Ce n'est PAS symétrique : −1 ∈ Dh "
                    "mais 1 ∉ Dh. Donc h n'est ni paire ni impaire, sans "
                    "même calculer h(−x).",
                    width=52,
                ),
                font_size=23,
            ),
            box_width=10.3,
        )
        cas_h.next_to(titre, DOWN, buff=0.55)

        with self.voiceover(
            text=(
                "h est définie sur ℝ privé de un et de moins trois. Cet "
                "ensemble n'est pas symétrique : moins un appartient à Dh, "
                "mais un n'y appartient pas. Il est donc inutile de "
                "calculer h de moins x : h n'est ni paire ni impaire."
            )
        ) as tracker:
            self.play(FadeIn(cas_h))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(cas_h))

        cas_k = example_box(
            MathTex(
                r"D_k=\mathbb{R} \text{ (symétrique)}, \quad k(-x)=x^2-x "
                r"\neq k(x) \text{ et } \neq -k(x) \ \Longrightarrow \ "
                r"k \text{ ni paire ni impaire}",
                font_size=22,
            ),
            box_width=11.3,
        )
        cas_k.next_to(titre, DOWN, buff=0.55)

        with self.voiceover(
            text=(
                "k est définie sur ℝ, ensemble symétrique. Mais k de moins "
                "x vaut x carré moins x, qui n'est égal ni à k de x ni à "
                "son opposé : k n'est ni paire ni impaire, bien que son "
                "domaine soit symétrique."
            )
        ) as tracker:
            self.play(FadeIn(cas_k))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(cas_k))

        # --- Périodicité : définition ------------------------------------
        def_periode = definition_box(
            MathTex(
                r"""
                \begin{array}{l}
                f \text{ est périodique de période } T>0 \text{ si :} \\
                \bullet \ \forall x \in D_f,\ x+T \in D_f \\
                \bullet \ \forall x \in D_f,\ f(x+T) = f(x)
                \end{array}
                """,
                font_size=28,
            ),
            box_width=9.2,
        )
        def_periode.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Passons à la périodicité. Une fonction f est périodique "
                "de période T, un réel strictement positif, si, pour tout "
                "x de Df, x plus T appartient encore à Df, et f de x plus "
                "T est égal à f de x."
            )
        ) as tracker:
            self.play(FadeIn(def_periode))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(def_periode))

        # --- Interprétation graphique : translation --------------------------
        axes_periode = Axes(
            x_range=[-1, 7, 1],
            y_range=[-1.5, 1.5, 1],
            x_length=7.5,
            y_length=2.6,
            axis_config={"color": WHITE, "font_size": 16},
        )
        axes_periode.next_to(titre, DOWN, buff=0.6)

        courbe_periode = axes_periode.plot(lambda x: 0.9 * np.sin(x * 2), x_range=[-1, 7], color=YELLOW)
        fleche = Arrow(axes_periode.c2p(0, 1.3), axes_periode.c2p(np.pi, 1.3), color=WHITE, buff=0)
        label_T = MathTex("T", font_size=26).next_to(fleche, UP, buff=0.1)
        schema_periode = VGroup(axes_periode, courbe_periode, fleche, label_T)

        theo_periode = theorem_box(
            Text(
                _wrap(
                    "La courbe de f est invariante par translation de "
                    "vecteur T·i : elle se reproduit identique à "
                    "elle-même tous les T sur l'axe des abscisses.",
                    width=58,
                ),
                font_size=22,
            ),
            box_width=10.3,
        )

        with self.voiceover(
            text=(
                "Interprétation graphique : la courbe de f est invariante "
                "par translation de vecteur T fois le vecteur i. Autrement "
                "dit, elle se reproduit à l'identique tous les T sur l'axe "
                "des abscisses — c'est la démonstration directe de "
                "l'égalité f de x plus T égale f de x."
            )
        ) as tracker:
            self.play(FadeIn(schema_periode))
            self.wait(1)
            theo_periode.next_to(schema_periode, DOWN, buff=0.4)
            self.play(FadeIn(theo_periode))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(schema_periode), FadeOut(theo_periode))

        # --- Exemple traité : exemples fondamentaux + exemple 4 --------------
        exemples_fond = example_box(
            MathTex(
                r"""
                \begin{array}{ll}
                \sin \text{ et } \cos & \text{période } 2\pi \\
                \tan & \text{période } \pi \\
                \text{mantisse } x - \lfloor x \rfloor & \text{période } 1
                \end{array}
                """,
                font_size=27,
            ),
            box_width=8.3,
        )
        exemples_fond.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Exemples fondamentaux à connaître : sinus et cosinus sont "
                "de période deux pi ; tangente est de période pi ; et la "
                "fonction mantisse, x moins sa partie entière, est de "
                "période un."
            )
        ) as tracker:
            self.play(FadeIn(exemples_fond))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(exemples_fond))

        exemple4 = example_box(
            MathTex(
                r"""
                \begin{array}{l}
                f(x) = \cos(2x), \quad f(x+\pi) = \cos(2x+2\pi) = \cos(2x) = f(x) \\
                \Longrightarrow \ f \text{ est périodique de période } \pi
                \end{array}
                """,
                font_size=27,
            ),
            box_width=10.0,
        )
        exemple4.next_to(titre, DOWN, buff=0.6)

        with self.voiceover(
            text=(
                "Exemple 4 : soit f de x égale cosinus de deux x. On a f "
                "de x plus pi égale cosinus de deux x plus deux pi, ce qui "
                "vaut cosinus de deux x par périodicité du cosinus, donc f "
                "de x. La fonction f est donc périodique, de période pi."
            )
        ) as tracker:
            self.play(FadeIn(exemple4))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(exemple4))

        # --- À retenir ---------------------------------------------------
        retenir = essentiel_box(
            Text(
                _wrap(
                    "Toujours vérifier le domaine avant de tester la "
                    "parité. Une fonction périodique de période T a une "
                    "courbe qui se répète tous les T.",
                    width=56,
                ),
                font_size=24,
            ),
            box_width=10.6,
        )
        retenir.next_to(titre, DOWN, buff=0.6)

        with self.voiceover(
            text=(
                "À retenir : toujours vérifier que le domaine est "
                "symétrique avant de tester f de moins x. Et une fonction "
                "périodique de période T a une courbe qui se répète à "
                "l'identique tous les T."
            )
        ) as tracker:
            self.play(FadeIn(retenir))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(retenir))

        # --- Piège à éviter ----------------------------------------------
        piege = warning_box(
            Text(
                _wrap(
                    "Piège : si T est une période de f, alors 2T, 3T, etc. "
                    "en sont aussi. La « période » d'une fonction, sans "
                    "précision, désigne la plus petite période strictement "
                    "positive.",
                    width=56,
                ),
                font_size=23,
            ),
            box_width=10.6,
        )
        piege.next_to(titre, DOWN, buff=0.6)

        with self.voiceover(
            text=(
                "Attention : si T est une période de f, alors deux T, "
                "trois T, et plus généralement tout multiple de T, en "
                "sont aussi. Quand on parle « de la » période d'une "
                "fonction, on désigne en réalité la plus petite période "
                "strictement positive."
            )
        ) as tracker:
            self.play(FadeIn(piege))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(titre), FadeOut(piege))
