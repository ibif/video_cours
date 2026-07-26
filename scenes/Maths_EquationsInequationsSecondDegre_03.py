"""
scenes/Maths_EquationsInequationsSecondDegre_03.py — Chapitre 1 (1ereC,
Maths), scène 03.

Factorisation du trinôme selon le signe de Δ (avec démonstration courte),
un exemple de trinôme factorisable et un non factorisable, puis les
relations entre coefficients et racines (somme et produit), démontrées.
Source : 1ereC/Maths.pdf, chapitre 1, pages 4-13.
"""

from manim import DOWN, UP, FadeIn, FadeOut, MathTex, Text, VGroup, Write

from shapes.base_scene import NotionScene
from shapes.boxes import example_box, scene_title, theorem_box


class FactorisationSommeProduitRacines(NotionScene):
    def construct(self):
        titre = scene_title("Factoriser le trinôme — somme et produit")
        titre.scale(0.6)
        titre.to_edge(UP)
        self.play(Write(titre))

        # --- Énoncé : théorème de factorisation ------------------------------
        theo_fact = MathTex(
            r"""
            \begin{aligned}
            \Delta < 0 &\;\Rightarrow\; ax^2+bx+c \text{ n'est pas factorisable} \\
            \Delta = 0 &\;\Rightarrow\; ax^2+bx+c = a(x-x_0)^2 \\
            \Delta > 0 &\;\Rightarrow\; ax^2+bx+c = a(x-x_1)(x-x_2)
            \end{aligned}
            """,
            font_size=30,
        )
        theo_fact_box = theorem_box(theo_fact, box_width=11.5)
        theo_fact_box.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Grâce à la forme canonique, on peut factoriser le "
                "trinôme selon le signe de delta. Si delta est "
                "strictement négatif, il n'existe pas de factorisation en "
                "produit de facteurs du premier degré. Si delta est nul, "
                "le trinôme est le carré parfait a fois le carré de x "
                "moins x zéro, où x zéro est la racine double. Si delta "
                "est strictement positif, le trinôme se factorise en a "
                "fois x moins x un, fois x moins x deux, où x un et x deux "
                "sont les deux racines : cela découle directement de la "
                "forme canonique, qui est alors une différence de deux "
                "carrés."
            )
        ) as tracker:
            self.play(FadeIn(theo_fact_box))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(theo_fact_box))

        # --- Exemple traité 5 : factorisable / non factorisable --------------
        exA_enonce = MathTex(r"A(x) = x^2 + 2x - 35", font_size=30)
        exA_calc = MathTex(
            r"\Delta = 2^2-4\times1\times(-35)=4+140=144=12^2",
            font_size=26,
        )
        exA_sol = MathTex(
            r"x_1=\dfrac{-2-12}{2}=-7 \quad x_2=\dfrac{-2+12}{2}=5"
            r"\;\Rightarrow\; A(x)=(x+7)(x-5)",
            font_size=26,
        )
        exB_enonce = MathTex(r"B(x) = 2x^2 + 3x + 2", font_size=30)
        exB_calc = MathTex(
            r"\Delta = 3^2-4\times2\times2=9-16=-7<0 "
            r"\;\Rightarrow\; B \text{ n'est pas factorisable}",
            font_size=26,
        )
        ex5 = VGroup(exA_enonce, exA_calc, exA_sol, exB_enonce, exB_calc).arrange(DOWN, buff=0.25)
        ex5_box = example_box(ex5, box_width=12.0)
        ex5_box.scale(0.92)
        ex5_box.next_to(titre, DOWN, buff=0.3)

        with self.voiceover(
            text=(
                "Exemple : A de x égale x carré plus deux x moins "
                "trente-cinq. Delta vaut quatre plus cent quarante, soit "
                "cent quarante-quatre, qui est le carré de douze : les "
                "racines sont moins sept et cinq, donc A de x se factorise "
                "en x plus sept, fois x moins cinq. En revanche, pour B de "
                "x égale deux x carré plus trois x plus deux, delta vaut "
                "neuf moins seize, soit moins sept, strictement négatif : "
                "B n'est pas factorisable."
            )
        ) as tracker:
            self.play(FadeIn(ex5_box))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(ex5_box))

        # --- Animation du raisonnement : relations coefficients-racines -----
        theo_relations = MathTex(
            r"x_1+x_2 = -\dfrac{b}{a} \qquad\qquad x_1 x_2 = \dfrac{c}{a}",
            font_size=32,
        )
        demo_relations = MathTex(
            r"""
            \begin{aligned}
            x_1+x_2 &= \dfrac{-b-\sqrt{\Delta}}{2a}+\dfrac{-b+\sqrt{\Delta}}{2a}
                     = \dfrac{-2b}{2a} = -\dfrac{b}{a} \\[4pt]
            x_1 x_2 &= \dfrac{(-b-\sqrt{\Delta})(-b+\sqrt{\Delta})}{4a^2}
                     = \dfrac{b^2-\Delta}{4a^2} = \dfrac{4ac}{4a^2} = \dfrac{c}{a}
            \end{aligned}
            """,
            font_size=26,
        )
        relations = VGroup(theo_relations, demo_relations).arrange(DOWN, buff=0.4)
        relations_box = theorem_box(relations, box_width=12.0)
        relations_box.scale(0.9)
        relations_box.next_to(titre, DOWN, buff=0.35)

        with self.voiceover(
            text=(
                "Lorsque delta est positif ou nul, les racines x un et x "
                "deux vérifient deux relations très utiles avec les "
                "coefficients a, b et c. Leur somme vaut moins b sur a : "
                "on l'obtient en additionnant les deux expressions de x un "
                "et x deux, les termes en racine de delta s'annulent. Leur "
                "produit vaut c sur a : on reconnaît une identité "
                "remarquable au numérateur, b carré moins delta, qui vaut "
                "exactement quatre a c."
            )
        ) as tracker:
            self.play(FadeIn(relations_box))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(relations_box))

        # --- À retenir ---------------------------------------------------------
        retenir = Text(
            "À retenir : le signe de Δ dicte la factorisation du trinôme,\n"
            "et les racines vérifient toujours x₁+x₂ = −b/a et x₁x₂ = c/a.",
            font_size=26,
        )
        retenir.next_to(titre, DOWN, buff=0.8)

        with self.voiceover(
            text=(
                "À retenir : le signe de delta dicte la factorisation du "
                "trinôme, et dès que le trinôme possède des racines, "
                "celles-ci vérifient toujours les deux relations : leur "
                "somme vaut moins b sur a, et leur produit vaut c sur a."
            )
        ) as tracker:
            self.play(FadeIn(retenir))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(titre), FadeOut(retenir))
