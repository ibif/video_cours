"""
scenes/Maths_EquationsInequationsSecondDegre_04.py — Chapitre 1 (1ereC,
Maths), scène 04.

Méthode de la racine évidente, exemple résolu, puis le théorème « deux
nombres de somme S et produit P sont solutions de X² − SX + P = 0 » avec
démonstration et deux exemples (numérique, puis problème de rectangle).
Source : 1ereC/Maths.pdf, chapitre 1, pages 4-13.
"""

from manim import DOWN, UP, FadeIn, FadeOut, MathTex, Text, VGroup, Write

from shapes.base_scene import NotionScene
from shapes.boxes import example_box, method_box, scene_title, theorem_box


class RacineEvidenteSommeProduit(NotionScene):
    def construct(self):
        titre = scene_title("Racine évidente — somme et produit")
        titre.scale(0.65)
        titre.to_edge(UP)
        self.play(Write(titre))

        # --- Énoncé : méthode de la racine évidente ---------------------------
        methode = VGroup(
            Text("Avant de calculer Δ, tester les valeurs simples :", font_size=26),
            MathTex(r"x=0,\; x=1,\; x=-1,\; x=2,\; x=-2", font_size=28),
            MathTex(
                r"\text{Si } a+b+c=0 \;\Rightarrow\; 1 \text{ est racine, }"
                r"\; x_2=\dfrac{c}{a}",
                font_size=26,
            ),
            MathTex(
                r"\text{Si } a-b+c=0 \;\Rightarrow\; -1 \text{ est racine, }"
                r"\; x_2=-\dfrac{c}{a}",
                font_size=26,
            ),
        ).arrange(DOWN, buff=0.3)
        methode_box = method_box(methode, box_width=11.8)
        methode_box.next_to(titre, DOWN, buff=0.35)

        with self.voiceover(
            text=(
                "Avant de se lancer dans le calcul de delta, il est "
                "souvent efficace de tester quelques valeurs simples : "
                "zéro, un, moins un, deux, moins deux. Un cas particulier "
                "à connaître par cœur : si la somme des coefficients a "
                "plus b plus c est nulle, alors un est racine évidente de "
                "l'équation, et l'autre racine vaut c sur a, d'après la "
                "relation sur le produit des racines. De même, si a moins "
                "b plus c est nul, alors moins un est racine évidente."
            )
        ) as tracker:
            self.play(FadeIn(methode_box))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(methode_box))

        # --- Exemple traité 6 --------------------------------------------------
        ex6_enonce = MathTex(r"15x^2 - 11x - 4 = 0", font_size=32)
        ex6_test = MathTex(
            r"a+b+c = 15-11-4 = 0 \;\Rightarrow\; x_1=1 \text{ est racine}",
            font_size=28,
        )
        ex6_autre = MathTex(
            r"x_1 x_2 = \dfrac{c}{a} = -\dfrac{4}{15} \;\Rightarrow\; "
            r"x_2 = -\dfrac{4}{15}",
            font_size=28,
        )
        ex6 = VGroup(ex6_enonce, ex6_test, ex6_autre).arrange(DOWN, buff=0.3)
        ex6_box = example_box(ex6, box_width=11.8)
        ex6_box.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Exemple : quinze x carré moins onze x moins quatre égale "
                "zéro. On remarque que a plus b plus c vaut quinze moins "
                "onze moins quatre, soit zéro : un est donc racine "
                "évidente. Le produit des racines vaut c sur a, soit moins "
                "quatre quinzièmes, donc la seconde racine vaut moins "
                "quatre quinzièmes."
            )
        ) as tracker:
            self.play(FadeIn(ex6_box))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(ex6_box))

        # --- Animation du raisonnement : théorème somme/produit ---------------
        theo_enonce = MathTex(
            r"\text{Si } x_1+x_2=S \text{ et } x_1 x_2=P, \text{ alors } x_1, x_2"
            r" \text{ sont solutions de } X^2-SX+P=0",
            font_size=27,
        )
        demo = MathTex(
            r"(X-x_1)(X-x_2) = X^2-(x_1+x_2)X+x_1x_2 = X^2-SX+P",
            font_size=27,
        )
        theo = VGroup(theo_enonce, demo).arrange(DOWN, buff=0.35)
        theo_box = theorem_box(theo, box_width=12.0)
        theo_box.scale(0.92)
        theo_box.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Voici un résultat très utile : si deux nombres x un et x "
                "deux ont pour somme S et pour produit P, alors ils sont "
                "solutions de l'équation X carré moins S X plus P égale "
                "zéro. La démonstration est immédiate : il suffit de "
                "développer le produit X moins x un, fois X moins x deux, "
                "pour retrouver exactement cette équation."
            )
        ) as tracker:
            self.play(FadeIn(theo_box))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(theo_box))

        # --- Exemple traité 7 : numérique --------------------------------------
        ex7_enonce = MathTex(r"S = 7 \qquad P = -30", font_size=32)
        ex7_eq = MathTex(r"X^2 - 7X - 30 = 0", font_size=30)
        ex7_calc = MathTex(r"\Delta = 49+120=169=13^2", font_size=28)
        ex7_sol = MathTex(
            r"X_1=\dfrac{7-13}{2}=-3 \qquad X_2=\dfrac{7+13}{2}=10",
            font_size=28,
        )
        ex7 = VGroup(ex7_enonce, ex7_eq, ex7_calc, ex7_sol).arrange(DOWN, buff=0.28)
        ex7_box = example_box(ex7, box_width=11.5)
        ex7_box.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Exemple : trouvons deux nombres de somme sept et de "
                "produit moins trente. Ils sont solutions de X carré moins "
                "sept X moins trente égale zéro. Delta vaut cent "
                "soixante-neuf, qui est le carré de treize. Les deux "
                "nombres cherchés sont donc moins trois et dix."
            )
        ) as tracker:
            self.play(FadeIn(ex7_box))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(ex7_box))

        # --- Exemple traité 8 : problème du rectangle ---------------------------
        ex8_enonce = Text(
            "Un rectangle a un périmètre de 64 m et une aire de 240 m².\n"
            "Trouver ses dimensions L et ℓ.",
            font_size=25,
        )
        ex8_mise_eq = MathTex(
            r"L+\ell = 32 \qquad L\times\ell = 240",
            font_size=28,
        )
        ex8_eq = MathTex(r"X^2-32X+240=0 \qquad \Delta = 1024-960=64=8^2", font_size=26)
        ex8_sol = MathTex(
            r"X_1=\dfrac{32-8}{2}=12 \qquad X_2=\dfrac{32+8}{2}=20"
            r"\;\Rightarrow\; L=20\text{ m},\; \ell=12\text{ m}",
            font_size=26,
        )
        ex8 = VGroup(ex8_enonce, ex8_mise_eq, ex8_eq, ex8_sol).arrange(DOWN, buff=0.28)
        ex8_box = example_box(ex8, box_width=12.2)
        ex8_box.scale(0.9)
        ex8_box.next_to(titre, DOWN, buff=0.3)

        with self.voiceover(
            text=(
                "Dernier exemple : un rectangle a un périmètre de "
                "soixante-quatre mètres et une aire de deux cent quarante "
                "mètres carrés ; on cherche ses dimensions L et petit l. "
                "Le périmètre donne L plus l égale trente-deux, l'aire "
                "donne L fois l égale deux cent quarante : L et l sont "
                "donc les deux racines de X carré moins trente-deux X plus "
                "deux cent quarante égale zéro. Delta vaut soixante-quatre, "
                "le carré de huit, et l'on trouve douze et vingt : le "
                "rectangle mesure vingt mètres sur douze mètres."
            )
        ) as tracker:
            self.play(FadeIn(ex8_box))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(titre), FadeOut(ex8_box))
