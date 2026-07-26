"""
scenes/Maths_EquationsInequationsSecondDegre_09.py — Chapitre 1 (1ereC,
Maths), scène 09.

Équations avec valeurs absolues se ramenant au second degré (changement
X = |x| ou disjonction de cas), puis équations et inéquations
irrationnelles (√A = B ⟺ A = B² et B ≥ 0), avec un exemple pour chaque cas.
Source : 1ereC/Maths.pdf, chapitre 1, pages 4-13.
"""

from manim import DOWN, UP, FadeIn, FadeOut, MathTex, Text, VGroup, Write

from shapes.base_scene import NotionScene
from shapes.boxes import definition_box, example_box, method_box, property_box, scene_title


class ValeursAbsoluesEtIrrationnelles(NotionScene):
    def construct(self):
        titre = scene_title("Valeurs absolues et équations irrationnelles")
        titre.scale(0.55)
        titre.to_edge(UP)
        self.play(Write(titre))

        # --- Énoncé : méthode pour les valeurs absolues -----------------------
        methode_va = VGroup(
            Text("Deux techniques pour une équation en x et |x| :", font_size=25),
            MathTex(
                r"\text{1) Changement d'inconnue } X=|x|\;(X\ge0), "
                r"\text{ car } x^2=|x|^2",
                font_size=26,
            ),
            MathTex(
                r"\text{2) Disjonction de cas : } x\ge0 \Rightarrow |x|=x"
                r"\ ;\quad x<0 \Rightarrow |x|=-x",
                font_size=26,
            ),
        ).arrange(DOWN, buff=0.3)
        methode_va_box = method_box(methode_va, box_width=12.2)
        methode_va_box.scale(0.92)
        methode_va_box.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Pour une équation faisant intervenir x et sa valeur "
                "absolue, deux techniques sont possibles. La première : "
                "quand seul x carré et la valeur absolue de x "
                "interviennent, on pose X égale la valeur absolue de x, "
                "positive ou nulle, car x carré est égal au carré de la "
                "valeur absolue de x. La seconde : on distingue deux cas, "
                "x positif ou nul, où la valeur absolue de x vaut x, et x "
                "strictement négatif, où elle vaut moins x."
            )
        ) as tracker:
            self.play(FadeIn(methode_va_box))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(methode_va_box))

        # --- Exemple traité 15 --------------------------------------------------
        ex15_enonce = MathTex(r"x^2 - 3|x| - 4 = 0", font_size=32)
        ex15_pose = MathTex(r"X=|x| \;\Rightarrow\; X^2-3X-4=0", font_size=28)
        ex15_calc = MathTex(r"\Delta=9+16=25=5^2", font_size=27)
        ex15_racines = MathTex(
            r"X_1=\dfrac{3-5}{2}=-1 \qquad X_2=\dfrac{3+5}{2}=4",
            font_size=27,
        )
        ex15_concl = MathTex(
            r"X_1=-1 \text{ rejetée} \qquad X_2=4 \;\Rightarrow\; |x|=4"
            r"\;\Rightarrow\; S=\{-4\, ;\, 4\}",
            font_size=26,
        )
        ex15 = VGroup(ex15_enonce, ex15_pose, ex15_calc, ex15_racines, ex15_concl).arrange(
            DOWN, buff=0.25
        )
        ex15_box = example_box(ex15, box_width=12.0)
        ex15_box.scale(0.92)
        ex15_box.next_to(titre, DOWN, buff=0.3)

        with self.voiceover(
            text=(
                "Exemple : x carré moins trois fois la valeur absolue de "
                "x, moins quatre égale zéro. En posant X égale la valeur "
                "absolue de x, on obtient X carré moins trois X moins "
                "quatre égale zéro, de discriminant vingt-cinq. On trouve "
                "X égale moins un, rejetée car négative, et X égale "
                "quatre, qui donne la valeur absolue de x égale quatre, "
                "donc x égale quatre ou x égale moins quatre."
            )
        ) as tracker:
            self.play(FadeIn(ex15_box))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(ex15_box))

        # --- Animation du raisonnement : équations irrationnelles ----------------
        def_irr = VGroup(
            Text("Une équation irrationnelle contient l'inconnue", font_size=25),
            Text("sous un radical (une racine carrée).", font_size=25),
        ).arrange(DOWN, buff=0.15)
        def_irr_box = definition_box(def_irr, box_width=10.5)
        def_irr_box.next_to(titre, DOWN, buff=0.4)

        propriete = MathTex(
            r"\sqrt{A} = B \;\Longleftrightarrow\; \left(A=B^2 \ \text{et}\ B\ge0\right)",
            font_size=32,
        )
        propriete_box = property_box(propriete, box_width=10.5)
        propriete_box.next_to(def_irr_box, DOWN, buff=0.35)

        with self.voiceover(
            text=(
                "On appelle équation irrationnelle une équation où "
                "l'inconnue apparaît sous un radical, une racine carrée. "
                "La propriété fondamentale est la suivante : racine de A "
                "égale B, si et seulement si A égale B carré, et B "
                "supérieur ou égal à zéro. C'est cette équivalence, et non "
                "une simple implication, qui garantit de ne pas ajouter de "
                "solution parasite."
            )
        ) as tracker:
            self.play(FadeIn(def_irr_box))
            self.play(FadeIn(propriete_box))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(def_irr_box), FadeOut(propriete_box))

        # --- méthode deux démarches ------------------------------------------------
        demarches = VGroup(
            MathTex(
                r"\text{a) Par implication : } \sqrt{A}=B \Rightarrow A=B^2,"
                r"\ \text{puis } \textit{vérifier } B\ge0",
                font_size=25,
            ),
            MathTex(
                r"\text{b) Par équivalence : résoudre le système } "
                r"A=B^2 \ \text{et}\ B\ge0",
                font_size=25,
            ),
        ).arrange(DOWN, buff=0.3)
        demarches_box = method_box(demarches, box_width=12.0)
        demarches_box.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Deux démarches sont possibles pour résoudre racine de A "
                "égale B. Première démarche, par implication : on élève "
                "au carré, on résout A égale B carré, puis on vérifie a "
                "posteriori que chaque solution trouvée rend B positif ou "
                "nul, en éliminant les solutions parasites. Deuxième "
                "démarche, par équivalence directe : on résout le système "
                "A égale B carré, et B supérieur ou égal à zéro, sans "
                "vérification finale."
            )
        ) as tracker:
            self.play(FadeIn(demarches_box))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(demarches_box))

        # --- Exemple traité 16 --------------------------------------------------
        ex16_enonce = MathTex(r"\sqrt{2-x} = x+10", font_size=32)
        ex16_cond = MathTex(
            r"\Longleftrightarrow\; \left(2-x=(x+10)^2 \ \text{et}\ x+10\ge0\right)",
            font_size=27,
        )
        ex16_dev = MathTex(
            r"2-x=x^2+20x+100 \;\Longleftrightarrow\; x^2+21x+98=0",
            font_size=27,
        )
        ex16_calc = MathTex(r"\Delta=441-392=49=7^2", font_size=26)
        ex16_racines = MathTex(
            r"x=\dfrac{-21-7}{2}=-14 \qquad x=\dfrac{-21+7}{2}=-7",
            font_size=26,
        )
        ex16_verif = MathTex(
            r"x+10\ge0 \;\Longleftrightarrow\; x\ge-10 : \quad -14 \text{ rejetée},"
            r"\ -7 \text{ conservée}",
            font_size=25,
        )
        ex16_concl = MathTex(r"S = \{-7\}", font_size=28)
        ex16 = VGroup(
            ex16_enonce, ex16_cond, ex16_dev, ex16_calc, ex16_racines, ex16_verif, ex16_concl
        ).arrange(DOWN, buff=0.2)
        ex16_box = example_box(ex16, box_width=12.4)
        ex16_box.scale(0.75)
        ex16_box.next_to(titre, DOWN, buff=0.2)

        with self.voiceover(
            text=(
                "Exemple : racine de deux moins x égale x plus dix. Par "
                "équivalence, cela équivaut à deux moins x égale x plus "
                "dix au carré, et x plus dix supérieur ou égal à zéro. En "
                "développant, on obtient x carré plus vingt-et-un x plus "
                "quatre-vingt-dix-huit égale zéro, de discriminant "
                "quarante-neuf. On trouve x égale moins quatorze et x "
                "égale moins sept. La condition x plus dix supérieur ou "
                "égal à zéro, c'est-à-dire x supérieur ou égal à moins "
                "dix, élimine moins quatorze et conserve moins sept. "
                "L'unique solution est donc moins sept."
            )
        ) as tracker:
            self.play(FadeIn(ex16_box))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(ex16_box))

        # --- Exemple traité 17 : inéquation irrationnelle -------------------------
        ex17_enonce = MathTex(r"\sqrt{x-1} \ge 3-x \qquad (\text{domaine } x\ge1)", font_size=30)
        ex17_cas1 = MathTex(
            r"\text{Cas } 3-x<0\ (x>3) : \text{ vrai automatiquement (racine} \ge 0)",
            font_size=24,
        )
        ex17_cas2 = MathTex(
            r"\text{Cas } 3-x\ge0\ (1\le x\le3) : x-1\ge(3-x)^2 "
            r"\Longleftrightarrow x^2-7x+10\le0",
            font_size=24,
        )
        ex17_calc = MathTex(
            r"\Delta=49-40=9=3^2 \;\Rightarrow\; x\in[2\, ;\, 5]"
            r"\;\Rightarrow\; \text{ici } x\in[2\, ;\, 3]",
            font_size=24,
        )
        ex17_concl = MathTex(
            r"S = [2\, ;\, 3] \cup\, ]3\, ;\, +\infty[ \;=\; [2\, ;\, +\infty[",
            font_size=27,
        )
        ex17 = VGroup(ex17_enonce, ex17_cas1, ex17_cas2, ex17_calc, ex17_concl).arrange(
            DOWN, buff=0.22
        )
        ex17_box = example_box(ex17, box_width=12.4)
        ex17_box.scale(0.85)
        ex17_box.next_to(titre, DOWN, buff=0.25)

        with self.voiceover(
            text=(
                "Dernier exemple, une inéquation irrationnelle : racine de "
                "x moins un, supérieur ou égal à trois moins x, sur le "
                "domaine x supérieur ou égal à un. On distingue deux cas "
                "selon le signe de trois moins x. Si x est strictement "
                "supérieur à trois, l'inégalité est automatiquement vraie, "
                "puisqu'une racine carrée est toujours positive ou nulle. "
                "Si x est compris entre un et trois, les deux membres sont "
                "positifs : on peut élever au carré, ce qui donne x carré "
                "moins sept x plus dix inférieur ou égal à zéro, vrai "
                "entre deux et cinq, donc ici entre deux et trois. En "
                "réunissant les deux cas, l'ensemble solution final est "
                "l'intervalle deux, plus l'infini."
            )
        ) as tracker:
            self.play(FadeIn(ex17_box))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(titre), FadeOut(ex17_box))
