"""
scenes/Maths_VecteursEspace_08.py — Chapitre 16 « Vecteurs de l'espace »
(1ereC, Maths), scène 08.

§ Milieu d'un segment dans l'espace : théorème de caractérisation
vectorielle (4 propriétés équivalentes, démonstration des implications en
chaîne) et propriété des coordonnées du milieu.
Source : 1ereC/Maths.pdf, pages 189-199.
"""

from manim import (
    DOWN,
    LEFT,
    RIGHT,
    UP,
    YELLOW,
    Dot,
    FadeIn,
    FadeOut,
    Line,
    MathTex,
    Text,
    VGroup,
    Write,
)

from shapes.base_scene import NotionScene
from shapes.boxes import property_box, scene_title, theorem_box


class MilieuSegment(NotionScene):
    def construct(self):
        titre = scene_title("Milieu d'un segment dans l'espace")
        titre.scale(0.55)
        titre.to_edge(UP)
        self.play(Write(titre))

        # --- Énoncé : petite figure A, B, I -----------------------------------------
        A = LEFT * 2.6
        B = RIGHT * 2.6
        I = (A + B) / 2
        seg = Line(A, B, color="#1E5FA8", stroke_width=4)
        pts = VGroup(
            Dot(A, color=YELLOW), MathTex("A", font_size=26, color=YELLOW).next_to(A, DOWN, buff=0.15),
            Dot(B, color=YELLOW), MathTex("B", font_size=26, color=YELLOW).next_to(B, DOWN, buff=0.15),
            Dot(I, color="#DE7C1F"), MathTex("I", font_size=26, color="#DE7C1F").next_to(I, UP, buff=0.15),
        )
        figure = VGroup(seg, pts)
        figure.next_to(titre, DOWN, buff=0.6)

        theo = theorem_box(
            VGroup(
                Text("Caractérisation vectorielle du milieu — quatre propriétés équivalentes", font_size=20, weight="BOLD"),
                MathTex(
                    r"I \ \text{milieu de} \ [AB] \iff (1)\ \overrightarrow{AI}=\overrightarrow{IB} \iff (2)\ \overrightarrow{AI}=\tfrac12\overrightarrow{AB}",
                    font_size=21,
                ),
                MathTex(
                    r"\iff (3)\ \overrightarrow{IA}+\overrightarrow{IB}=\vec 0 \iff (4)\ \forall M, \ \overrightarrow{MA}+\overrightarrow{MB}=2\overrightarrow{MI}",
                    font_size=21,
                ),
            ).arrange(DOWN, buff=0.2),
        )
        theo.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Voici, pour un point I et un segment A-B de l'espace, "
                "quatre façons équivalentes de dire que I est le milieu de "
                "A-B : le vecteur A-I égal I-B ; le vecteur A-I égal la "
                "moitié de A-B ; le vecteur I-A plus I-B égal le vecteur "
                "nul ; et enfin, pour tout point M, le vecteur M-A plus "
                "M-B égal deux fois le vecteur M-I."
            )
        ) as tracker:
            self.play(FadeIn(figure))
            self.play(FadeIn(theo))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(theo), FadeOut(figure))

        # --- Raisonnement : démonstration des implications en chaîne ---------------
        demo1 = VGroup(
            Text("(1) ⟺ (2)", font_size=22, weight="BOLD"),
            MathTex(
                r"\overrightarrow{AI}=\overrightarrow{IB} \iff \overrightarrow{AI} = \overrightarrow{AB}-\overrightarrow{AI} \iff 2\overrightarrow{AI}=\overrightarrow{AB} \iff \overrightarrow{AI}=\tfrac12\overrightarrow{AB}",
                font_size=21,
            ),
        ).arrange(DOWN, buff=0.22)
        demo1.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Montrons d'abord que les propriétés un et deux sont "
                "équivalentes. A-I égal I-B équivaut, en remplaçant I-B par "
                "A-B moins A-I via Chasles, à A-I égal A-B moins A-I, "
                "c'est-à-dire deux fois A-I égal A-B, soit encore A-I égal "
                "la moitié de A-B."
            )
        ) as tracker:
            self.play(Write(demo1[0]))
            self.play(Write(demo1[1]))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(demo1))

        demo2 = VGroup(
            Text("(1) ⟺ (3)", font_size=22, weight="BOLD"),
            MathTex(
                r"\overrightarrow{IA}+\overrightarrow{IB} = -\overrightarrow{AI} + \overrightarrow{IB}",
                font_size=22,
            ),
            MathTex(
                r"\text{Si (1) : } \overrightarrow{IB}=\overrightarrow{AI} \ \Longrightarrow\ \overrightarrow{IA}+\overrightarrow{IB} = -\overrightarrow{AI}+\overrightarrow{AI} = \vec 0.",
                font_size=21,
            ),
            MathTex(
                r"\text{Réciproquement, si (3) : } \overrightarrow{IB} = -\overrightarrow{IA} = \overrightarrow{AI} \ \Longrightarrow\ (1).",
                font_size=21,
            ),
        ).arrange(DOWN, buff=0.2)
        demo2.next_to(titre, DOWN, buff=0.35)

        with self.voiceover(
            text=(
                "Montrons ensuite que un et trois sont équivalentes. Le "
                "vecteur I-A plus I-B s'écrit moins A-I plus I-B. Si la "
                "propriété un est vraie, I-B égale A-I, donc cette somme "
                "vaut moins A-I plus A-I, le vecteur nul : c'est la "
                "propriété trois. Réciproquement, si I-A plus I-B est nul, "
                "alors I-B égale moins I-A, c'est-à-dire A-I, ce qui "
                "redonne la propriété un."
            )
        ) as tracker:
            self.play(Write(demo2[0]))
            self.play(Write(demo2[1]))
            self.play(Write(demo2[2]))
            self.play(Write(demo2[3]))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(demo2))

        demo3 = VGroup(
            Text("(3) ⟺ (4)", font_size=22, weight="BOLD"),
            MathTex(
                r"\forall M, \ \overrightarrow{MA}+\overrightarrow{MB} = (\overrightarrow{MI}+\overrightarrow{IA}) + (\overrightarrow{MI}+\overrightarrow{IB}) = 2\overrightarrow{MI} + (\overrightarrow{IA}+\overrightarrow{IB})",
                font_size=20,
            ),
            MathTex(
                r"\text{Si (3) : } \overrightarrow{IA}+\overrightarrow{IB}=\vec 0 \ \Longrightarrow\ \overrightarrow{MA}+\overrightarrow{MB}=2\overrightarrow{MI} \ \text{: c'est (4).}",
                font_size=20,
            ),
            MathTex(
                r"\text{Réciproquement, (4) avec } M=I \ \text{donne} \ \overrightarrow{IA}+\overrightarrow{IB}=2\overrightarrow{II}=\vec 0 \ \text{: c'est (3).}",
                font_size=20,
            ),
        ).arrange(DOWN, buff=0.2)
        demo3.next_to(titre, DOWN, buff=0.35)

        with self.voiceover(
            text=(
                "Enfin, trois et quatre sont équivalentes. En décomposant "
                "M-A et M-B via I, pour tout point M, M-A plus M-B égale "
                "deux fois M-I, plus I-A plus I-B. Si I-A plus I-B est nul, "
                "on retrouve exactement la propriété quatre. "
                "Réciproquement, en choisissant M égal I dans la propriété "
                "quatre, on retrouve directement I-A plus I-B égal au "
                "vecteur nul, c'est-à-dire la propriété trois. La boucle "
                "d'équivalences est bouclée."
            )
        ) as tracker:
            self.play(Write(demo3[0]))
            self.play(Write(demo3[1]))
            self.play(Write(demo3[2]))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(demo3))

        # --- Exemple / application : coordonnées du milieu ---------------------------
        coord = property_box(
            VGroup(
                Text("Coordonnées du milieu", font_size=22, weight="BOLD"),
                MathTex(
                    r"A(x_A;y_A;z_A), \ B(x_B;y_B;z_B), \ I \ \text{milieu de} \ [AB] :",
                    font_size=21,
                ),
                MathTex(
                    r"I\left(\dfrac{x_A+x_B}{2} \, ; \, \dfrac{y_A+y_B}{2} \, ; \, \dfrac{z_A+z_B}{2}\right)",
                    font_size=25,
                ),
            ).arrange(DOWN, buff=0.22),
        )
        coord.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Appliquons cela aux coordonnées. Si A a pour coordonnées x "
                "A, y A, z A, et B pour coordonnées x B, y B, z B, alors le "
                "milieu I de A-B a pour coordonnées la demi-somme de "
                "chaque composante : x A plus x B, sur deux, y A plus y B, "
                "sur deux, et z A plus z B, sur deux. Cette formule "
                "découle directement de la propriété deux, A-I égal la "
                "moitié de A-B, combinée à la formule des coordonnées d'un "
                "vecteur vue à la scène 6."
            )
        ) as tracker:
            self.play(FadeIn(coord))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(coord))

        # --- À retenir -----------------------------------------------------------
        retenir = property_box(
            VGroup(
                Text("À retenir", font_size=23, weight="BOLD"),
                MathTex(r"\overrightarrow{IA}+\overrightarrow{IB}=\vec 0 \quad \text{est la formulation la plus utile en pratique}", font_size=22),
                Text("(elle se généralise directement au centre de gravité d'un tétraèdre, scène 9).", font_size=19),
            ).arrange(DOWN, buff=0.2),
        )
        retenir.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Parmi ces quatre formulations équivalentes, retenez "
                "surtout la troisième, I-A plus I-B égal le vecteur nul : "
                "c'est elle qui se généralise le plus naturellement, "
                "puisque nous verrons à la scène suivante que le centre de "
                "gravité d'un tétraèdre se définit exactement sur ce même "
                "modèle, avec quatre sommets au lieu de deux."
            )
        ) as tracker:
            self.play(FadeIn(retenir))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(retenir), FadeOut(titre))
