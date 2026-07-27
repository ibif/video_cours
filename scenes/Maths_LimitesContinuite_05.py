"""
scenes/Maths_LimitesContinuite_05.py — Chapitre 5 « Limites et continuité »
(1ereC, Maths), scène 05.

Méthode 1 : factorisation par le terme dominant (polynôme et fraction
rationnelle en l'infini) et factorisation en un point pour lever une F.I.
0/0. Exemples résolus 2, 3, 4.
Source : 1ereC/Maths.pdf, chapitre 5, pages 52-65.
"""

from manim import DOWN, UP, FadeIn, FadeOut, MathTex, Text, VGroup, Write, YELLOW

from shapes.base_scene import NotionScene
from shapes.boxes import essentiel_box, example_box, method_box, scene_title


class MethodeFactorisationTermeDominant(NotionScene):
    def construct(self):
        titre = scene_title("Méthode 1 — factoriser par le terme dominant")
        titre.scale(0.5)
        titre.to_edge(UP)
        self.play(Write(titre))

        # --- Énoncé de la méthode -------------------------------------------
        methode = method_box(
            MathTex(
                r"""
                \begin{array}{l}
                \text{En } \pm\infty,\ \text{un polynôme a même limite que son terme de plus haut degré :} \\
                a_n x^n + \dots + a_0 \ \sim \ a_n x^n \\[6pt]
                \text{Une fraction rationnelle a même limite que le quotient des} \\
                \text{termes de plus haut degré du numérateur et du dénominateur.}
                \end{array}
                """,
                font_size=25,
            ),
            box_width=11.5,
        )
        methode.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Première méthode, la plus utile : en plus ou moins "
                "l'infini, un polynôme a toujours la même limite que son "
                "terme de plus haut degré, car c'est lui qui écrase tous "
                "les autres. De même, une fraction rationnelle a la même "
                "limite que le quotient des termes de plus haut degré du "
                "numérateur et du dénominateur."
            )
        ) as tracker:
            self.play(FadeIn(methode))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(methode))

        # --- Exemple 2 : polynôme en +∞ -----------------------------------------
        ex2_titre = Text("Exemple 2 — lim (2x³ - 5x + 1) en +∞ :", font_size=24, color=YELLOW, weight="BOLD")
        ex2_titre.next_to(titre, DOWN, buff=0.35)
        ex2_calc = MathTex(
            r"""
            \begin{array}{l}
            2x^3-5x+1 = x^3\left(2-\dfrac{5}{x^2}+\dfrac{1}{x^3}\right)\\
            \lim_{x\to+\infty} \left(2-\dfrac{5}{x^2}+\dfrac{1}{x^3}\right) = 2,\quad \lim_{x\to+\infty} x^3 = +\infty\\
            \Longrightarrow\ \lim_{x\to+\infty} (2x^3-5x+1) = +\infty
            \end{array}
            """,
            font_size=25,
        )
        ex2_calc.next_to(ex2_titre, DOWN, buff=0.35)

        with self.voiceover(
            text=(
                "Exemple : calculons la limite de deux x cube moins cinq x "
                "plus un, en plus l'infini. On factorise par x cube, le "
                "terme de plus haut degré : la parenthèse tend vers deux, "
                "et x cube tend vers plus l'infini. Par produit, la limite "
                "vaut donc plus l'infini."
            )
        ) as tracker:
            self.play(FadeIn(ex2_titre))
            self.play(Write(ex2_calc))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(ex2_titre), FadeOut(ex2_calc))

        # --- Exemple 3 : fraction rationnelle en -∞ -----------------------------
        ex3_titre = Text(
            "Exemple 3 — lim (3x²+x-5)/(x²-2x+1) en -∞ :", font_size=22, color=YELLOW, weight="BOLD"
        )
        ex3_titre.next_to(titre, DOWN, buff=0.35)
        ex3_calc = MathTex(
            r"""
            \dfrac{3x^2+x-5}{x^2-2x+1} \ \underset{-\infty}{\sim}\ \dfrac{3x^2}{x^2} = 3
            \ \Longrightarrow\ \lim_{x\to-\infty} \dfrac{3x^2+x-5}{x^2-2x+1} = 3
            """,
            font_size=27,
        )
        ex3_calc.next_to(ex3_titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Exemple : pour trois x carré plus x moins cinq, sur x "
                "carré moins deux x plus un, en moins l'infini, on ne garde "
                "que les termes de plus haut degré du numérateur et du "
                "dénominateur : trois x carré sur x carré, qui se simplifie "
                "en trois. La limite vaut donc trois."
            )
        ) as tracker:
            self.play(FadeIn(ex3_titre))
            self.play(Write(ex3_calc))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(ex3_titre), FadeOut(ex3_calc))

        # --- Exemple 4 : F.I. 0/0 en un point, factorisation par (x-2) ---------
        ex4_titre = Text(
            "Exemple 4 — lim (x²+x-6)/(x²-4) en x0 = 2 :", font_size=22, color=YELLOW, weight="BOLD"
        )
        ex4_titre.next_to(titre, DOWN, buff=0.35)
        ex4_calc = MathTex(
            r"""
            \begin{array}{l}
            \text{En } x=2 : \text{numérateur} \to 0,\ \text{dénominateur} \to 0 \ \text{(F.I. } 0/0\text{)}\\
            x^2+x-6=(x-2)(x+3), \qquad x^2-4=(x-2)(x+2)\\
            \dfrac{x^2+x-6}{x^2-4} = \dfrac{(x-2)(x+3)}{(x-2)(x+2)} = \dfrac{x+3}{x+2} \quad (x\neq 2)\\
            \Longrightarrow\ \lim_{x\to 2} \dfrac{x^2+x-6}{x^2-4} = \dfrac{5}{4}
            \end{array}
            """,
            font_size=22,
        )
        ex4_calc.next_to(ex4_titre, DOWN, buff=0.35)
        ex4_box = example_box(ex4_calc, box_width=11.5)
        ex4_box.next_to(ex4_titre, DOWN, buff=0.3)

        with self.voiceover(
            text=(
                "Dernier exemple, plus délicat : x carré plus x moins six, "
                "sur x carré moins quatre, en x égale deux. En remplaçant "
                "directement, numérateur et dénominateur s'annulent tous "
                "les deux : c'est une forme indéterminée zéro sur zéro. On "
                "factorise alors chacun par x moins deux, la racine "
                "commune : le numérateur devient x moins deux fois x plus "
                "trois, le dénominateur x moins deux fois x plus deux. Après "
                "simplification par x moins deux, il reste x plus trois sur "
                "x plus deux, dont la limite en deux vaut cinq quarts."
            )
        ) as tracker:
            self.play(FadeIn(ex4_titre))
            self.play(FadeIn(ex4_box))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(ex4_titre), FadeOut(ex4_box))

        # --- À retenir -----------------------------------------------------------
        retenir = essentiel_box(
            MathTex(
                r"""
                \begin{array}{l}
                \text{En } \pm\infty : \text{on garde le(s) terme(s) de plus haut degré.}\\
                \text{En } x_0, \text{F.I. } 0/0 : \text{on factorise par } (x-x_0) \text{ au numérateur et au dénominateur.}
                \end{array}
                """,
                font_size=24,
            ),
            box_width=11.5,
        )
        retenir.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "À retenir : en plus ou moins l'infini, on factorise "
                "toujours par le terme de plus haut degré. Face à une forme "
                "zéro sur zéro en un point x zéro, on factorise numérateur "
                "et dénominateur par x moins x zéro, la racine commune, "
                "puis on simplifie avant de passer à la limite."
            )
        ) as tracker:
            self.play(FadeIn(retenir))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(retenir), FadeOut(titre))
