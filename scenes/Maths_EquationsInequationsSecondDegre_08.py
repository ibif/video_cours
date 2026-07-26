"""
scenes/Maths_EquationsInequationsSecondDegre_08.py — Chapitre 1 (1ereC,
Maths), scène 08.

Équations et inéquations bicarrées : définition, méthode du changement
d'inconnue X = x², deux exemples résolus (équation, puis inéquation).
Source : 1ereC/Maths.pdf, chapitre 1, pages 4-13.
"""

from manim import DOWN, UP, FadeIn, FadeOut, MathTex, Text, VGroup, Write

from shapes.base_scene import NotionScene
from shapes.boxes import definition_box, example_box, method_box, scene_title


class EquationsInequationsBicarrees(NotionScene):
    def construct(self):
        titre = scene_title("Équations et inéquations bicarrées")
        titre.scale(0.65)
        titre.to_edge(UP)
        self.play(Write(titre))

        # --- Énoncé : définition ---------------------------------------------
        definition = VGroup(
            Text("Une équation bicarrée s'écrit :", font_size=27),
            MathTex(r"ax^4 + bx^2 + c = 0, \qquad a \neq 0", font_size=32),
        ).arrange(DOWN, buff=0.3)
        def_box = definition_box(definition, box_width=11.5)
        def_box.next_to(titre, DOWN, buff=0.45)

        with self.voiceover(
            text=(
                "On appelle équation bicarrée une équation de la forme a x "
                "puissance quatre plus b x carré plus c égale zéro, avec a "
                "différent de zéro : seules les puissances paires de x "
                "interviennent."
            )
        ) as tracker:
            self.play(FadeIn(def_box))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(def_box))

        # --- Animation du raisonnement : méthode du changement d'inconnue ------
        methode = VGroup(
            MathTex(r"\text{On pose } X = x^2 \;(X \ge 0)", font_size=30),
            MathTex(r"ax^4+bx^2+c=0 \;\Longleftrightarrow\; aX^2+bX+c=0", font_size=30),
            Text("On résout en X, puis pour chaque racine X trouvée :", font_size=25),
            MathTex(
                r"X<0 \Rightarrow \text{aucune solution} \quad\;"
                r"X=0 \Rightarrow x=0 \quad\;"
                r"X>0 \Rightarrow x=\pm\sqrt{X}",
                font_size=25,
            ),
        ).arrange(DOWN, buff=0.3)
        methode_box = method_box(methode, box_width=12.0)
        methode_box.scale(0.9)
        methode_box.next_to(titre, DOWN, buff=0.35)

        with self.voiceover(
            text=(
                "Pour résoudre une équation bicarrée, on pose X égale x "
                "carré, avec X positif ou nul. L'équation devient alors "
                "une équation du second degré ordinaire en X : a X carré "
                "plus b X plus c égale zéro. On la résout normalement, "
                "puis on revient à x pour chaque racine X trouvée. Si X "
                "est négatif, cette racine ne donne aucune solution en x, "
                "puisqu'un carré ne peut pas être négatif. Si X est nul, "
                "on obtient x égale zéro. Si X est strictement positif, on "
                "obtient deux solutions, plus ou moins racine de X."
            )
        ) as tracker:
            self.play(FadeIn(methode_box))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(methode_box))

        # --- Exemple traité 13 : équation ----------------------------------------
        ex13_enonce = MathTex(r"x^4 + x^2 - 12 = 0", font_size=32)
        ex13_pose = MathTex(r"X = x^2 \;\Rightarrow\; X^2+X-12=0", font_size=28)
        ex13_calc = MathTex(r"\Delta = 1+48=49=7^2", font_size=27)
        ex13_racines = MathTex(
            r"X_1=\dfrac{-1-7}{2}=-4 \qquad X_2=\dfrac{-1+7}{2}=3",
            font_size=27,
        )
        ex13_concl = MathTex(
            r"X_1=-4 \text{ rejetée} \qquad X_2=3 \;\Rightarrow\; x=\pm\sqrt3"
            r"\;\Rightarrow\; S=\{-\sqrt3\, ;\, \sqrt3\}",
            font_size=26,
        )
        ex13 = VGroup(ex13_enonce, ex13_pose, ex13_calc, ex13_racines, ex13_concl).arrange(
            DOWN, buff=0.25
        )
        ex13_box = example_box(ex13, box_width=12.0)
        ex13_box.scale(0.9)
        ex13_box.next_to(titre, DOWN, buff=0.3)

        with self.voiceover(
            text=(
                "Exemple : x puissance quatre plus x carré moins douze "
                "égale zéro. En posant X égale x carré, on obtient X carré "
                "plus X moins douze égale zéro, de discriminant "
                "quarante-neuf, le carré de sept. On trouve X égale moins "
                "quatre, rejetée car négative, et X égale trois, qui donne "
                "x égale plus ou moins racine de trois. L'ensemble des "
                "solutions est donc moins racine de trois, racine de "
                "trois."
            )
        ) as tracker:
            self.play(FadeIn(ex13_box))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(ex13_box))

        # --- Exemple traité 14 : inéquation ---------------------------------------
        ex14_enonce = MathTex(r"x^4 - x^2 - 12 \ge 0", font_size=32)
        ex14_pose = MathTex(r"X=x^2 \;\Rightarrow\; X^2-X-12 \ge 0", font_size=28)
        ex14_calc = MathTex(
            r"\Delta=1+48=49=7^2 \;\Rightarrow\; X_1=-3,\ X_2=4",
            font_size=27,
        )
        ex14_signe = MathTex(
            r"X^2-X-12\ge0 \;\Longleftrightarrow\; X\le-3 \ \text{ou}\ X\ge4",
            font_size=27,
        )
        ex14_retour = MathTex(
            r"X=x^2\ge0 \;\Rightarrow\; X\le-3 \text{ impossible},"
            r"\ \text{reste } X\ge4",
            font_size=26,
        )
        ex14_concl = MathTex(
            r"x^2\ge4 \;\Longleftrightarrow\; x\le-2 \ \text{ou}\ x\ge2"
            r"\;\Rightarrow\; S=\;]-\infty;-2] \cup [2;+\infty[",
            font_size=26,
        )
        ex14 = VGroup(
            ex14_enonce, ex14_pose, ex14_calc, ex14_signe, ex14_retour, ex14_concl
        ).arrange(DOWN, buff=0.22)
        ex14_box = example_box(ex14, box_width=12.4)
        ex14_box.scale(0.8)
        ex14_box.next_to(titre, DOWN, buff=0.25)

        with self.voiceover(
            text=(
                "Dernier exemple, une inéquation bicarrée : x puissance "
                "quatre moins x carré moins douze, supérieur ou égal à "
                "zéro. En posant X égale x carré, on obtient X carré moins "
                "X moins douze, supérieur ou égal à zéro, dont les racines "
                "sont moins trois et quatre. Le trinôme en X est positif à "
                "l'extérieur des racines : X inférieur ou égal à moins "
                "trois, ou X supérieur ou égal à quatre. Or X égale x "
                "carré est toujours positif ou nul, donc la condition X "
                "inférieur ou égal à moins trois est impossible : il ne "
                "reste que X supérieur ou égal à quatre, c'est-à-dire x "
                "carré supérieur ou égal à quatre, ce qui donne x "
                "inférieur ou égal à moins deux, ou x supérieur ou égal à "
                "deux."
            )
        ) as tracker:
            self.play(FadeIn(ex14_box))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(titre), FadeOut(ex14_box))
