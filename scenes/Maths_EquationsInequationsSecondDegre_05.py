"""
scenes/Maths_EquationsInequationsSecondDegre_05.py — Chapitre 1 (1ereC,
Maths), scène 05.

Signe du trinôme du second degré selon les trois cas du discriminant, avec
démonstration (forme canonique pour Δ ≤ 0, forme factorisée pour Δ > 0),
tableaux récapitulatifs, et deux exemples résolus.
Source : 1ereC/Maths.pdf, chapitre 1, pages 4-13.
"""

from manim import DOWN, UP, FadeIn, FadeOut, MathTex, Text, VGroup, Write

from shapes.base_scene import NotionScene
from shapes.boxes import example_box, scene_title, theorem_box


class SigneDuTrinome(NotionScene):
    def construct(self):
        titre = scene_title("Le signe du trinôme ax² + bx + c")
        titre.scale(0.65)
        titre.to_edge(UP)
        self.play(Write(titre))

        # --- Énoncé : théorème du signe + démonstration -------------------------
        theo = MathTex(
            r"""
            \begin{aligned}
            \Delta < 0 &\;\Rightarrow\; ax^2+bx+c \text{ du signe de } a \text{ pour tout } x\\
            \Delta = 0 &\;\Rightarrow\; ax^2+bx+c \text{ du signe de } a,\ \text{sauf en } x_0 \text{ (nul)}\\
            \Delta > 0 &\;\Rightarrow\; ax^2+bx+c \text{ du signe de } a \text{ à l'extérieur des racines,}\\
            &\quad\;\; \text{du signe de } {-a} \text{ entre les racines}
            \end{aligned}
            """,
            font_size=26,
        )
        theo_box = theorem_box(theo, box_width=12.0)
        theo_box.scale(0.92)
        theo_box.next_to(titre, DOWN, buff=0.35)

        with self.voiceover(
            text=(
                "Étudier le signe du trinôme a x carré plus b x plus c "
                "dépend, encore une fois, du signe de delta. Si delta est "
                "strictement négatif, la forme canonique montre que le "
                "trinôme est toujours du signe de a, pour tout x réel. Si "
                "delta est nul, c'est encore le cas, sauf en la racine "
                "double où le trinôme s'annule. Si delta est strictement "
                "positif, la forme factorisée montre que le trinôme est du "
                "signe de a à l'extérieur des racines, et du signe "
                "contraire de a, entre les racines."
            )
        ) as tracker:
            self.play(FadeIn(theo_box))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(theo_box))

        # --- Animation du raisonnement : démonstration + tableaux --------------
        demo = MathTex(
            r"""
            \begin{aligned}
            \Delta \le 0 &: ax^2+bx+c = a\left[\left(x+\frac{b}{2a}\right)^2-\frac{\Delta}{4a^2}\right]\\
            &\quad\text{le crochet est} \ge 0,\ \text{donc le signe est celui de } a\\[6pt]
            \Delta > 0 &: ax^2+bx+c = a(x-x_1)(x-x_2)\\
            &\quad\text{produit de deux facteurs changeant de signe en } x_1,\ x_2
            \end{aligned}
            """,
            font_size=25,
        )
        demo_box = theorem_box(demo, box_width=12.0)
        demo_box.scale(0.9)
        demo_box.next_to(titre, DOWN, buff=0.35)

        tableau = MathTex(
            r"""
            \begin{array}{|c|ccccccc|}
            \hline
            x & -\infty & & x_1 & & x_2 & & +\infty \\
            \hline
            ax^2+bx+c & & \text{signe } a & 0 & \text{signe } {-a} & 0 & \text{signe } a & \\
            \hline
            \end{array}
            """,
            font_size=24,
        )
        tableau.next_to(demo_box, DOWN, buff=0.3)

        with self.voiceover(
            text=(
                "Pour delta négatif ou nul, on repart de la forme "
                "canonique : le crochet est toujours positif ou nul, donc "
                "le signe global est celui de a. Pour delta strictement "
                "positif, on repart de la forme factorisée : c'est un "
                "produit de deux facteurs affines, chacun changeant de "
                "signe en sa racine, ce qui donne le tableau de signe "
                "classique en trois zones : signe de a, puis signe de "
                "moins a entre les racines, puis de nouveau signe de a."
            )
        ) as tracker:
            self.play(FadeIn(demo_box))
            self.wait(1)
            self.play(FadeIn(tableau))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(demo_box), FadeOut(tableau))

        # --- Exemple traité 9 : Δ < 0 -------------------------------------------
        ex9_enonce = MathTex(r"P(x) = -2x^2 + x - 1", font_size=32)
        ex9_calc = MathTex(r"\Delta = 1^2-4\times(-2)\times(-1) = 1-8 = -7 < 0", font_size=27)
        ex9_concl = MathTex(
            r"\Delta<0 \;\Rightarrow\; P(x) \text{ du signe de } a=-2"
            r"\;\Rightarrow\; P(x)<0 \ \text{pour tout } x",
            font_size=27,
        )
        ex9 = VGroup(ex9_enonce, ex9_calc, ex9_concl).arrange(DOWN, buff=0.3)
        ex9_box = example_box(ex9, box_width=11.8)
        ex9_box.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Exemple : P de x égale moins deux x carré plus x moins "
                "un. Delta vaut un moins huit, soit moins sept, "
                "strictement négatif. P de x est donc toujours du signe de "
                "a, qui vaut moins deux : P de x est strictement négatif "
                "pour tout x réel."
            )
        ) as tracker:
            self.play(FadeIn(ex9_box))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(ex9_box))

        # --- Exemple traité 10 : Δ > 0, tableau complet -------------------------
        ex10_enonce = MathTex(r"Q(x) = -2x^2 + 3x + 2", font_size=32)
        ex10_calc = MathTex(
            r"\Delta = 9+16=25=5^2 \;\Rightarrow\; "
            r"x_1=\dfrac{-3-5}{-4}=2,\ x_2=\dfrac{-3+5}{-4}=-\dfrac{1}{2}",
            font_size=25,
        )
        ex10_tableau = MathTex(
            r"""
            \begin{array}{|c|ccccccc|}
            \hline
            x & -\infty & & -\frac12 & & 2 & & +\infty \\
            \hline
            Q(x) & & - & 0 & + & 0 & - & \\
            \hline
            \end{array}
            """,
            font_size=24,
        )
        ex10 = VGroup(ex10_enonce, ex10_calc, ex10_tableau).arrange(DOWN, buff=0.3)
        ex10_box = example_box(ex10, box_width=12.2)
        ex10_box.scale(0.92)
        ex10_box.next_to(titre, DOWN, buff=0.3)

        with self.voiceover(
            text=(
                "Exemple : Q de x égale moins deux x carré plus trois x "
                "plus deux. Delta vaut vingt-cinq, le carré de cinq, donc "
                "les racines sont moins un demi et deux. Comme a est "
                "négatif, Q de x est négatif à l'extérieur des racines, et "
                "positif entre elles : négatif avant moins un demi, "
                "positif entre moins un demi et deux, puis de nouveau "
                "négatif après deux."
            )
        ) as tracker:
            self.play(FadeIn(ex10_box))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(titre), FadeOut(ex10_box))
