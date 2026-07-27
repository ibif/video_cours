"""
scenes/Maths_AnglesOrientesTrigonometrie_10.py — Chapitre « Angles orientés
et trigonométrie » (1ereC, Maths), scène 10.

§ Transformation de produits en sommes (3 formules, démonstration par
addition/soustraction des formules d'addition) et de sommes en produits (4
formules, démonstration par changement p=a+b, q=a-b). Exemple résolu 7 :
factoriser A=sin5x+sinx, résoudre sin5x+sinx=0.
Source : 1ereC/Maths.pdf, chapitre 2, pages 14-27.
"""

import textwrap

from manim import DOWN, LEFT, UP, FadeIn, FadeOut, MathTex, Text, VGroup, Write

from shapes.base_scene import NotionScene
from shapes.boxes import example_box, theorem_box, scene_title


def _wrap(text: str, width: int = 56) -> str:
    return "\n".join(textwrap.fill(line, width=width) for line in text.split("\n"))


class TransformationProduitsSommes(NotionScene):
    def construct(self):
        titre = scene_title("Transformation produits ↔ sommes")
        titre.scale(0.6)
        titre.to_edge(UP)

        # --- Énoncé : produits en sommes -----------------------------------
        theoreme1 = theorem_box(
            VGroup(
                Text("Transformation de produits en sommes", font_size=22, weight="BOLD"),
                MathTex(r"\cos a \cos b = \dfrac{1}{2}\big[\cos(a-b) + \cos(a+b)\big]", font_size=22),
                MathTex(r"\sin a \sin b = \dfrac{1}{2}\big[\cos(a-b) - \cos(a+b)\big]", font_size=22),
                MathTex(r"\sin a \cos b = \dfrac{1}{2}\big[\sin(a+b) + \sin(a-b)\big]", font_size=22),
            ).arrange(DOWN, buff=0.25),
            box_width=9.5,
        )
        theoreme1.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "On peut transformer un produit de cosinus ou de sinus en "
                "une somme. Cosinus a cosinus b égale un demi, cosinus de "
                "a moins b plus cosinus de a plus b. Sinus a sinus b égale "
                "un demi, cosinus de a moins b moins cosinus de a plus b. "
                "Et sinus a cosinus b égale un demi, sinus de a plus b "
                "plus sinus de a moins b."
            )
        ) as tracker:
            self.play(Write(titre))
            self.play(FadeIn(theoreme1))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(theoreme1))

        demo1 = VGroup(
            Text("Démonstration", font_size=22, color="#DE7C1F", weight="BOLD"),
            MathTex(r"\cos(a-b) = \cos a \cos b + \sin a \sin b", font_size=21),
            MathTex(r"\cos(a+b) = \cos a \cos b - \sin a \sin b", font_size=21),
            Text("En additionnant ces deux formules d'addition membre à membre :", font_size=19),
            MathTex(r"\cos(a-b) + \cos(a+b) = 2\cos a \cos b", font_size=22),
            Text("d'où la première formule ; les deux autres s'obtiennent en soustrayant, ou en combinant sin(a+b) et sin(a-b).", font_size=18),
        ).arrange(DOWN, buff=0.22, aligned_edge=LEFT)
        demo1.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Ces formules se démontrent en combinant les formules "
                "d'addition. En additionnant membre à membre cosinus de a "
                "moins b et cosinus de a plus b, les termes en sinus a "
                "sinus b s'annulent, et il reste deux cosinus a cosinus b "
                "égale cosinus de a moins b plus cosinus de a plus b, "
                "d'où la première formule. Les deux autres s'obtiennent de "
                "la même manière, en soustrayant ces deux formules, ou en "
                "combinant sinus de a plus b et sinus de a moins b."
            )
        ) as tracker:
            self.play(FadeIn(demo1))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(demo1))

        # --- Sommes en produits ----------------------------------------------------
        theoreme2 = theorem_box(
            VGroup(
                Text("Transformation de sommes en produits", font_size=21, weight="BOLD"),
                MathTex(r"\cos p + \cos q = 2\cos\!\left(\dfrac{p+q}{2}\right)\cos\!\left(\dfrac{p-q}{2}\right)", font_size=20),
                MathTex(r"\cos p - \cos q = -2\sin\!\left(\dfrac{p+q}{2}\right)\sin\!\left(\dfrac{p-q}{2}\right)", font_size=20),
                MathTex(r"\sin p + \sin q = 2\sin\!\left(\dfrac{p+q}{2}\right)\cos\!\left(\dfrac{p-q}{2}\right)", font_size=20),
                MathTex(r"\sin p - \sin q = 2\cos\!\left(\dfrac{p+q}{2}\right)\sin\!\left(\dfrac{p-q}{2}\right)", font_size=20),
            ).arrange(DOWN, buff=0.2),
            box_width=10,
        )
        theoreme2.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Inversement, on peut transformer une somme en produit, "
                "ce qui est très utile pour résoudre des équations. "
                "Cosinus p plus cosinus q égale deux cosinus de p plus q "
                "sur deux, fois cosinus de p moins q sur deux. Cosinus p "
                "moins cosinus q égale moins deux sinus de p plus q sur "
                "deux, fois sinus de p moins q sur deux. Sinus p plus "
                "sinus q égale deux sinus de p plus q sur deux, fois "
                "cosinus de p moins q sur deux. Et sinus p moins sinus q "
                "égale deux cosinus de p plus q sur deux, fois sinus de p "
                "moins q sur deux."
            )
        ) as tracker:
            self.play(FadeIn(theoreme2))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(theoreme2))

        demo2 = VGroup(
            Text("Démonstration (changement p = a+b, q = a-b)", font_size=20, color="#DE7C1F", weight="BOLD"),
            MathTex(
                r"p = a+b,\ q = a-b \ \Longrightarrow\ a = \dfrac{p+q}{2},\ b = \dfrac{p-q}{2}",
                font_size=21,
            ),
            Text("On reporte a et b dans la formule cos a cos b = ½[cos(a-b)+cos(a+b)] :", font_size=18),
            MathTex(
                r"\cos\!\left(\dfrac{p+q}{2}\right)\cos\!\left(\dfrac{p-q}{2}\right) = \dfrac{1}{2}(\cos q + \cos p)",
                font_size=20,
            ),
            Text("d'où cos p + cos q = 2 cos((p+q)/2) cos((p-q)/2). Les trois autres se déduisent de même.", font_size=18),
        ).arrange(DOWN, buff=0.22, aligned_edge=LEFT)
        demo2.next_to(titre, DOWN, buff=0.55)

        with self.voiceover(
            text=(
                "Pour démontrer ces formules, on part des formules de "
                "transformation de produits en sommes vues juste avant, et "
                "on effectue le changement de variables p égale a plus b, "
                "q égale a moins b, d'où a égale p plus q sur deux, et b "
                "égale p moins q sur deux. En reportant ces expressions "
                "dans la formule cosinus a cosinus b, on retrouve "
                "directement cosinus p plus cosinus q égale deux cosinus "
                "de p plus q sur deux fois cosinus de p moins q sur deux. "
                "Les trois autres formules se déduisent de la même "
                "façon."
            )
        ) as tracker:
            self.play(FadeIn(demo2))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(demo2))

        # --- Exemple résolu 7 -----------------------------------------------------
        exemple = example_box(
            VGroup(
                Text("Factoriser A = sin5x + sinx, puis résoudre sin5x + sinx = 0.", font_size=20),
                MathTex(
                    r"A = \sin 5x + \sin x = 2\sin\!\left(\dfrac{5x+x}{2}\right)\cos\!\left(\dfrac{5x-x}{2}\right)"
                    r" = 2\sin(3x)\cos(2x)",
                    font_size=20,
                ),
                MathTex(
                    r"\sin 5x + \sin x = 0 \iff 2\sin 3x \cos 2x = 0 \iff \sin 3x = 0 \ \text{ou} \ \cos 2x = 0",
                    font_size=20,
                ),
            ).arrange(DOWN, buff=0.3),
            box_width=11,
        )
        exemple.next_to(titre, DOWN, buff=0.6)

        with self.voiceover(
            text=(
                "Exemple résolu. Factorisons A égale sinus de cinq x plus "
                "sinus de x. On reconnaît une somme de sinus, avec p égale "
                "cinq x et q égale x. On obtient deux sinus de trois x, "
                "fois cosinus de deux x. Cette factorisation transforme "
                "immédiatement l'équation sinus de cinq x plus sinus de x "
                "égale zéro en un produit nul : deux sinus de trois x "
                "cosinus de deux x égale zéro, équivalent à sinus de trois "
                "x égale zéro, ou cosinus de deux x égale zéro. Nous "
                "résoudrons complètement ces deux équations à la dernière "
                "scène de ce chapitre, une fois les équations "
                "trigonométriques de base étudiées."
            )
        ) as tracker:
            self.play(FadeIn(exemple))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(exemple), FadeOut(titre))
