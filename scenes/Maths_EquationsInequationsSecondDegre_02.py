"""
scenes/Maths_EquationsInequationsSecondDegre_02.py — Chapitre 1 (1ereC,
Maths), scène 02.

Résolution de l'équation du second degré selon le signe du discriminant,
avec démonstration, quatre exemples résolus (dont un au discriminant
réduit), et le piège du facteur commun / de l'identité remarquable.
Source : 1ereC/Maths.pdf, chapitre 1, pages 4-13.
"""

from manim import DOWN, UP, FadeIn, FadeOut, MathTex, Text, VGroup, Write, YELLOW

from shapes.base_scene import NotionScene
from shapes.boxes import example_box, scene_title, theorem_box, warning_box


class ResolutionEquationSecondDegre(NotionScene):
    def construct(self):
        titre = scene_title("Résoudre ax² + bx + c = 0")
        titre.scale(0.65)
        titre.to_edge(UP)
        self.play(Write(titre))

        # --- Énoncé : théorème de résolution + démonstration ----------------
        theo = MathTex(
            r"""
            \begin{aligned}
            \Delta < 0 &\;\Rightarrow\; S = \varnothing \\
            \Delta = 0 &\;\Rightarrow\; S = \left\{-\dfrac{b}{2a}\right\} \\
            \Delta > 0 &\;\Rightarrow\; S = \left\{
                \dfrac{-b-\sqrt{\Delta}}{2a}\, ;\, \dfrac{-b+\sqrt{\Delta}}{2a}
              \right\}
            \end{aligned}
            """,
            font_size=30,
        )
        theo_box = theorem_box(theo, box_width=11.5)
        theo_box.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "D'après la forme canonique vue dans la scène précédente, "
                "résoudre a x carré plus b x plus c égale zéro revient à "
                "résoudre le carré de x plus b sur deux a, égal à delta "
                "sur quatre a carré. Trois cas se présentent selon le "
                "signe de delta. Si delta est strictement négatif, un "
                "carré ne peut jamais être négatif : l'équation n'a aucune "
                "solution réelle. Si delta est nul, le carré doit être "
                "nul, ce qui donne une unique solution, moins b sur deux "
                "a, appelée racine double. Si delta est strictement "
                "positif, on peut prendre la racine carrée des deux côtés, "
                "ce qui donne deux solutions distinctes."
            )
        ) as tracker:
            self.play(FadeIn(theo_box))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(theo_box))

        # --- Exemple traité 1 : Δ > 0 ----------------------------------------
        ex1_enonce = MathTex(r"2x^2 - 7x + 3 = 0", font_size=32)
        ex1_calc = MathTex(
            r"\Delta = (-7)^2 - 4\times 2\times 3 = 49-24 = 25 = 5^2",
            font_size=28,
        )
        ex1_sol = MathTex(
            r"x_1=\dfrac{7-5}{4}=\dfrac{1}{2} \qquad x_2=\dfrac{7+5}{4}=3",
            font_size=28,
        )
        ex1 = VGroup(ex1_enonce, ex1_calc, ex1_sol).arrange(DOWN, buff=0.3)
        ex1_box = example_box(ex1, box_width=11.5)
        ex1_box.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Premier exemple : deux x carré moins sept x plus trois "
                "égale zéro. On calcule delta : sept carré moins quatre "
                "fois deux fois trois, soit quarante-neuf moins "
                "vingt-quatre, c'est-à-dire vingt-cinq, qui est le carré "
                "de cinq. Delta est strictement positif : il y a deux "
                "solutions, un demi et trois."
            )
        ) as tracker:
            self.play(FadeIn(ex1_box))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(ex1_box))

        # --- Exemple traité 2 : Δ = 0 -----------------------------------------
        ex2_enonce = MathTex(r"9x^2 - 6x + 1 = 0", font_size=32)
        ex2_calc = MathTex(
            r"\Delta = (-6)^2 - 4\times 9\times 1 = 36-36 = 0",
            font_size=28,
        )
        ex2_ident = MathTex(
            r"9x^2-6x+1=(3x-1)^2 \quad\text{(identité remarquable)}",
            font_size=28,
        )
        ex2_sol = MathTex(r"x_0 = \dfrac{6}{18} = \dfrac{1}{3}", font_size=28)
        ex2 = VGroup(ex2_enonce, ex2_calc, ex2_ident, ex2_sol).arrange(DOWN, buff=0.28)
        ex2_box = example_box(ex2, box_width=11.5)
        ex2_box.next_to(titre, DOWN, buff=0.35)

        with self.voiceover(
            text=(
                "Deuxième exemple : neuf x carré moins six x plus un égale "
                "zéro. Delta vaut trente-six moins trente-six, soit zéro : "
                "il y a une racine double. On reconnaît d'ailleurs "
                "l'identité remarquable : neuf x carré moins six x plus un "
                "est le carré de trois x moins un. La racine double est "
                "moins b sur deux a, soit un tiers."
            )
        ) as tracker:
            self.play(FadeIn(ex2_box))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(ex2_box))

        # --- Exemple traité 3 : Δ < 0 -----------------------------------------
        ex3_enonce = MathTex(r"x^2 + 2x + 5 = 0", font_size=32)
        ex3_calc = MathTex(
            r"\Delta = 2^2 - 4\times 1\times 5 = 4-20 = -16 < 0",
            font_size=28,
        )
        ex3_sol = MathTex(r"S = \varnothing", font_size=30)
        ex3 = VGroup(ex3_enonce, ex3_calc, ex3_sol).arrange(DOWN, buff=0.3)
        ex3_box = example_box(ex3, box_width=11.5)
        ex3_box.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Troisième exemple : x carré plus deux x plus cinq égale "
                "zéro. Delta vaut quatre moins vingt, soit moins seize, "
                "qui est strictement négatif : l'équation n'a aucune "
                "solution réelle, l'ensemble des solutions est vide."
            )
        ) as tracker:
            self.play(FadeIn(ex3_box))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(ex3_box))

        # --- Discriminant réduit -----------------------------------------------
        remarque_reduit = VGroup(
            Text("Si b = 2b′ (b pair ou de la forme 2b′) :", font_size=26),
            MathTex(r"\Delta' = b'^2 - ac \qquad x = \dfrac{-b' \pm \sqrt{\Delta'}}{a}", font_size=30),
        ).arrange(DOWN, buff=0.3)
        remarque_box = warning_box(remarque_reduit, box_width=11.5)
        remarque_box.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Remarque utile : lorsque b s'écrit deux fois b prime, on "
                "peut alléger les calculs avec le discriminant réduit, "
                "delta prime, égal à b prime carré moins a c. Les "
                "solutions s'écrivent alors moins b prime plus ou moins "
                "racine de delta prime, le tout sur a."
            )
        ) as tracker:
            self.play(FadeIn(remarque_box))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(remarque_box))

        # --- Exemple traité 4 : discriminant réduit -----------------------------
        ex4_enonce = MathTex(r"3x^2 - 2\sqrt{2}x - 2 = 0", font_size=32)
        ex4_bprime = MathTex(r"b = -2\sqrt{2} = 2b' \;\Rightarrow\; b' = -\sqrt{2}", font_size=28)
        ex4_calc = MathTex(
            r"\Delta' = (-\sqrt{2})^2 - 3\times(-2) = 2+6 = 8",
            font_size=28,
        )
        ex4_sol = MathTex(
            r"x = \dfrac{\sqrt{2} \pm \sqrt{8}}{3} = \dfrac{\sqrt{2} \pm 2\sqrt{2}}{3}"
            r"\;\Rightarrow\; x_1=-\dfrac{\sqrt{2}}{3},\; x_2=\sqrt{2}",
            font_size=26,
        )
        ex4 = VGroup(ex4_enonce, ex4_bprime, ex4_calc, ex4_sol).arrange(DOWN, buff=0.28)
        ex4_box = example_box(ex4, box_width=12.0)
        ex4_box.next_to(titre, DOWN, buff=0.3)
        ex4_box.scale(0.95)
        ex4_box.next_to(titre, DOWN, buff=0.3)

        with self.voiceover(
            text=(
                "Quatrième exemple : trois x carré moins deux racine de "
                "deux x moins deux égale zéro. Ici b vaut moins deux "
                "racine de deux, donc b prime vaut moins racine de deux. "
                "Delta prime vaut deux plus six, soit huit. Les solutions "
                "sont racine de deux plus ou moins racine de huit, le tout "
                "sur trois, ce qui se simplifie en moins racine de deux "
                "sur trois, et racine de deux."
            )
        ) as tracker:
            self.play(FadeIn(ex4_box))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(ex4_box))

        # --- À retenir / piège --------------------------------------------------
        piege = Text(
            "Avant de calculer Δ : vérifier s'il n'y a pas un facteur commun\n"
            "à mettre en évidence, ou une identité remarquable évidente —\n"
            "cela évite bien des calculs inutiles.",
            font_size=26,
            color=YELLOW,
        )
        piege_box = warning_box(piege, box_width=11.8)
        piege_box.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Piège classique à éviter : avant de se lancer dans le "
                "calcul de delta, il faut toujours vérifier s'il n'y a pas "
                "un facteur commun à mettre en évidence, ou une identité "
                "remarquable évidente, comme dans notre deuxième exemple. "
                "Cela évite bien des calculs inutiles."
            )
        ) as tracker:
            self.play(FadeIn(piege_box))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(titre), FadeOut(piege_box))
