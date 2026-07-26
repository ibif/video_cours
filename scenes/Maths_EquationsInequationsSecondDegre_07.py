"""
scenes/Maths_EquationsInequationsSecondDegre_07.py — Chapitre 1 (1ereC,
Maths), scène 07.

Définition de l'inéquation du second degré, méthode générale en 4 étapes,
deux exemples résolus (discriminant réduit, puis Δ' < 0), et le piège de
la conclusion en intervalle.
Source : 1ereC/Maths.pdf, chapitre 1, pages 4-13.
"""

from manim import DOWN, LEFT, UP, FadeIn, FadeOut, MathTex, Text, VGroup, Write, YELLOW

from shapes.base_scene import NotionScene
from shapes.boxes import definition_box, example_box, method_box, scene_title, warning_box


class ResolutionInequationsSecondDegre(NotionScene):
    def construct(self):
        titre = scene_title("Résoudre une inéquation du second degré")
        titre.scale(0.6)
        titre.to_edge(UP)
        self.play(Write(titre))

        # --- Énoncé : définition -------------------------------------------------
        definition = VGroup(
            Text("Une inéquation du second degré s'écrit :", font_size=26),
            MathTex(
                r"ax^2+bx+c \gtrless 0 \quad\text{ou}\quad ax^2+bx+c \gtreqless 0,"
                r"\qquad a \neq 0",
                font_size=28,
            ),
        ).arrange(DOWN, buff=0.3)
        def_box = definition_box(definition, box_width=11.8)
        def_box.next_to(titre, DOWN, buff=0.45)

        with self.voiceover(
            text=(
                "Une inéquation du second degré est une inéquation qui "
                "peut se ramener à comparer un trinôme a x carré plus b x "
                "plus c à zéro, avec a différent de zéro, à l'aide d'une "
                "inégalité stricte ou large."
            )
        ) as tracker:
            self.play(FadeIn(def_box))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(def_box))

        # --- Animation du raisonnement : méthode en 4 étapes --------------------
        methode = VGroup(
            Text("1. Calculer Δ (ou Δ′) du trinôme.", font_size=25),
            Text("2. Déterminer le signe de Δ et les racines éventuelles.", font_size=25),
            Text("3. Dresser le tableau de signe du trinôme.", font_size=25),
            Text("4. Lire l'intervalle solution selon le sens de l'inégalité.", font_size=25),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.28)
        methode_box = method_box(methode, box_width=11.8)
        methode_box.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "La méthode générale comporte quatre étapes. Première "
                "étape : calculer le discriminant, delta ou delta prime, "
                "du trinôme. Deuxième étape : déterminer son signe, et "
                "donc les racines éventuelles. Troisième étape : dresser "
                "le tableau de signe complet du trinôme. Quatrième étape : "
                "lire, dans ce tableau, l'intervalle solution qui "
                "correspond au sens de l'inégalité de l'énoncé."
            )
        ) as tracker:
            self.play(FadeIn(methode_box))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(methode_box))

        # --- Exemple traité 11 : discriminant réduit -----------------------------
        ex11_enonce = MathTex(r"-x^2 + 4x + 1 \ge 0", font_size=32)
        ex11_calc = MathTex(
            r"b'=2 \;\Rightarrow\; \Delta' = 2^2-(-1)\times1 = 4+1=5>0",
            font_size=27,
        )
        ex11_racines = MathTex(
            r"x_1=\dfrac{-2-\sqrt5}{-1}=2+\sqrt5 \qquad x_2=\dfrac{-2+\sqrt5}{-1}=2-\sqrt5",
            font_size=25,
        )
        ex11_tableau = MathTex(
            r"""
            \begin{array}{|c|ccccccc|}
            \hline
            x & -\infty & & 2-\sqrt5 & & 2+\sqrt5 & & +\infty \\
            \hline
            -x^2+4x+1 & & - & 0 & + & 0 & - & \\
            \hline
            \end{array}
            """,
            font_size=22,
        )
        ex11_concl = MathTex(
            r"S = \left[\, 2-\sqrt5\, ;\, 2+\sqrt5\, \right]",
            font_size=28,
        )
        ex11 = VGroup(ex11_enonce, ex11_calc, ex11_racines, ex11_tableau, ex11_concl).arrange(
            DOWN, buff=0.25
        )
        ex11_box = example_box(ex11, box_width=12.3)
        ex11_box.scale(0.85)
        ex11_box.next_to(titre, DOWN, buff=0.3)

        with self.voiceover(
            text=(
                "Exemple : moins x carré plus quatre x plus un, supérieur "
                "ou égal à zéro. Comme b vaut quatre, b prime vaut deux, "
                "et delta prime vaut quatre plus un, soit cinq, "
                "strictement positif. Les racines sont deux plus racine de "
                "cinq et deux moins racine de cinq. Comme a est négatif, "
                "le trinôme est positif entre les racines : l'ensemble "
                "solution est l'intervalle fermé, de deux moins racine de "
                "cinq à deux plus racine de cinq."
            )
        ) as tracker:
            self.play(FadeIn(ex11_box))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(ex11_box))

        # --- Exemple traité 12 : Δ' < 0 -------------------------------------------
        ex12_enonce = MathTex(r"-2x^2 + 2x - 1 > 0", font_size=32)
        ex12_calc = MathTex(
            r"b'=1 \;\Rightarrow\; \Delta' = 1^2-(-2)\times(-1) = 1-2=-1<0",
            font_size=27,
        )
        ex12_concl = MathTex(
            r"\Delta'<0 \;\Rightarrow\; -2x^2+2x-1 \text{ du signe de } a=-2"
            r"\;\Rightarrow\; S=\varnothing",
            font_size=26,
        )
        ex12 = VGroup(ex12_enonce, ex12_calc, ex12_concl).arrange(DOWN, buff=0.3)
        ex12_box = example_box(ex12, box_width=11.8)
        ex12_box.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Autre exemple : moins deux x carré plus deux x moins un, "
                "strictement supérieur à zéro. Ici b prime vaut un, et "
                "delta prime vaut un moins deux, soit moins un, "
                "strictement négatif. Le trinôme est donc toujours du "
                "signe de a, qui est négatif : il n'est jamais strictement "
                "positif, l'ensemble des solutions est vide."
            )
        ) as tracker:
            self.play(FadeIn(ex12_box))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(ex12_box))

        # --- Piège à éviter --------------------------------------------------------
        piege = Text(
            "Une inéquation se conclut toujours par un intervalle (ou une\n"
            "union d'intervalles) : bien choisir crochets ouverts ou fermés\n"
            "selon que l'inégalité est stricte ou large.",
            font_size=25,
            color=YELLOW,
        )
        piege_box = warning_box(piege, box_width=12.0)
        piege_box.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Piège fréquent : une inéquation se conclut toujours par "
                "un intervalle, ou une union d'intervalles, jamais par une "
                "simple liste de valeurs. Attention aussi aux crochets : "
                "ouverts pour une inégalité stricte, fermés pour une "
                "inégalité large, en incluant ou non les racines "
                "elles-mêmes."
            )
        ) as tracker:
            self.play(FadeIn(piege_box))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(titre), FadeOut(piege_box))
