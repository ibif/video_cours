"""
scenes/Maths_LimitesContinuite_11.py — Chapitre 5 « Limites et continuité »
(1ereC, Maths), scène 11.

Continuité sur un intervalle, prolongement par continuité. Exemples
résolus 15 ((x²-1)/(x-1) prolongée en 1) et 16 (sin x / x prolongée en 0).
Piège : limite infinie ou limites latérales différentes empêchent le
prolongement.
Source : 1ereC/Maths.pdf, chapitre 5, pages 52-65.
"""

from manim import DOWN, UP, FadeIn, FadeOut, MathTex, Text, VGroup, Write, YELLOW

from shapes.base_scene import NotionScene
from shapes.boxes import definition_box, example_box, scene_title, warning_box


class ContinuiteSurIntervalleEtProlongement(NotionScene):
    def construct(self):
        titre = scene_title("Continuité sur un intervalle — prolongement")
        titre.scale(0.5)
        titre.to_edge(UP)
        self.play(Write(titre))

        # --- Énoncé : continuité sur un intervalle -------------------------------
        def_intervalle = definition_box(
            Text(
                "f est continue sur un intervalle I si f est continue en tout point de I.",
                font_size=24,
            ),
            box_width=10.5,
        )
        def_intervalle.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Une fonction f est dite continue sur un intervalle I si "
                "elle est continue en chacun des points de cet intervalle "
                "— autrement dit, si sa courbe se trace sur I sans lever le "
                "crayon."
            )
        ) as tracker:
            self.play(FadeIn(def_intervalle))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(def_intervalle))

        # --- Énoncé : prolongement par continuité --------------------------------
        def_prolongement = definition_box(
            VGroup(
                Text(
                    "Si f n'est pas définie en x0 mais admet une limite finie ℓ en x0,",
                    font_size=22,
                ),
                Text(
                    "on peut prolonger f par continuité en posant :",
                    font_size=22,
                ),
                MathTex(
                    r"""
                    \tilde{f}(x) = \left\{
                    \begin{array}{ll}
                    f(x) & \text{si } x\neq x_0\\
                    \ell & \text{si } x=x_0
                    \end{array}
                    \right.
                    """,
                    font_size=27,
                ),
            ).arrange(DOWN, buff=0.2),
            box_width=10.5,
        )
        def_prolongement.next_to(titre, DOWN, buff=0.35)

        with self.voiceover(
            text=(
                "Le prolongement par continuité : si f n'est pas définie en "
                "x zéro, mais admet malgré tout une limite finie ℓ en x "
                "zéro, on peut construire une nouvelle fonction, notée f "
                "tilde, égale à f partout ailleurs, et à laquelle on donne "
                "la valeur ℓ en x zéro. Cette nouvelle fonction f tilde est "
                "alors continue en x zéro."
            )
        ) as tracker:
            self.play(FadeIn(def_prolongement))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(def_prolongement))

        # --- Exemple résolu 15 : (x²-1)/(x-1) prolongée en 1 ----------------------
        ex15_titre = Text(
            "Exemple 15 — f(x) = (x²-1)/(x-1) prolongée en x0 = 1 :",
            font_size=20,
            color=YELLOW,
            weight="BOLD",
        )
        ex15_titre.next_to(titre, DOWN, buff=0.35)
        ex15_calc = MathTex(
            r"""
            \begin{array}{l}
            D_f = \mathbb{R}\setminus\{1\}, \qquad
            \dfrac{x^2-1}{x-1} = \dfrac{(x-1)(x+1)}{x-1} = x+1 \quad (x\neq 1)\\
            \lim_{x\to 1} f(x) = 1+1 = 2 \ \text{(finie)}\\
            \Longrightarrow\ \tilde{f}(x) = x+1 \text{ pour tout } x \in \mathbb{R}
            \ \text{(prolongement continu, } \tilde f(1)=2\text{)}
            \end{array}
            """,
            font_size=21,
        )
        ex15_calc.next_to(ex15_titre, DOWN, buff=0.3)
        ex15_box = example_box(ex15_calc, box_width=11.2)
        ex15_box.next_to(ex15_titre, DOWN, buff=0.25)

        with self.voiceover(
            text=(
                "Exemple : f de x égale x carré moins un, sur x moins un, "
                "définie sur ℝ privé de un. En factorisant, f de x égale x "
                "plus un, pour x différent de un. La limite en un vaut "
                "donc deux, une limite finie : on peut prolonger f par "
                "continuité en posant f tilde de un égale deux — la "
                "fonction prolongée coïncide alors avec x plus un sur ℝ "
                "tout entier."
            )
        ) as tracker:
            self.play(FadeIn(ex15_titre))
            self.play(FadeIn(ex15_box))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(ex15_titre), FadeOut(ex15_box))

        # --- Exemple résolu 16 : sin(x)/x prolongée en 0 -------------------------
        ex16_titre = Text(
            "Exemple 16 — f(x) = sin(x)/x prolongée en x0 = 0 :",
            font_size=21,
            color=YELLOW,
            weight="BOLD",
        )
        ex16_titre.next_to(titre, DOWN, buff=0.35)
        ex16_calc = MathTex(
            r"""
            \begin{array}{l}
            D_f = \mathbb{R}^{*}, \qquad \lim_{x\to 0} \dfrac{\sin x}{x} = 1 \ \text{(limite de référence, finie)}\\
            \Longrightarrow\ \tilde f(x) = \left\{
            \begin{array}{ll}
            \sin(x)/x & \text{si } x\neq 0\\
            1 & \text{si } x=0
            \end{array}
            \right. \ \text{est continue sur } \mathbb{R}
            \end{array}
            """,
            font_size=21,
        )
        ex16_calc.next_to(ex16_titre, DOWN, buff=0.3)
        ex16_box = example_box(ex16_calc, box_width=11.5)
        ex16_box.next_to(ex16_titre, DOWN, buff=0.25)

        with self.voiceover(
            text=(
                "Deuxième exemple : f de x égale sinus de x sur x, définie "
                "sur ℝ étoile. On sait, grâce à la limite trigonométrique "
                "de référence, que la limite en zéro vaut un, une limite "
                "finie. On peut donc prolonger f par continuité en posant "
                "f tilde de zéro égale un : la fonction ainsi prolongée est "
                "continue sur ℝ tout entier."
            )
        ) as tracker:
            self.play(FadeIn(ex16_titre))
            self.play(FadeIn(ex16_box))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(ex16_titre), FadeOut(ex16_box))

        # --- Piège à éviter -------------------------------------------------
        piege = warning_box(
            Text(
                "Pas de prolongement possible si la limite en x0 est infinie, "
                "ou si les limites à gauche et à droite en x0 diffèrent "
                "(exemples : 1/x en 0, ou |x-1|/(x-1) en 1).",
                font_size=22,
            ),
            box_width=11.5,
        )
        piege.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Attention, piège classique : le prolongement par "
                "continuité n'est possible que si la limite en x zéro "
                "existe et est finie. Si la limite est infinie, comme pour "
                "un sur x en zéro, ou si les limites à gauche et à droite "
                "diffèrent, comme pour la valeur absolue de x moins un sur "
                "x moins un, en un, aucun prolongement continu n'existe."
            )
        ) as tracker:
            self.play(FadeIn(piege))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(piege), FadeOut(titre))
