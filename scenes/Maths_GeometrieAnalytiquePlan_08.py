"""
scenes/Maths_GeometrieAnalytiquePlan_08.py — Chapitre 14 « Géométrie
analytique du plan » (1ereC, Maths), scène 08.

§ Distance d'un point à une droite (repère orthonormé) : définition
(projeté orthogonal, distance minimale), théorème
d(A,(D))=|axA+byA+c|/√(a²+b²) avec démonstration complète (vecteur normal,
produit scalaire). Exemple résolu : A(4;-1), (D):3x+4y-10=0 → d=2/5.
Source : 1ereC/Maths.pdf, chapitre 14, page 171.
"""

import textwrap

from manim import DOWN, LEFT, RIGHT, UP, WHITE, YELLOW, Axes, Create, Dot, DashedLine, FadeIn, FadeOut, MathTex, Text, VGroup, Write

from shapes.base_scene import NotionScene
from shapes.boxes import definition_box, example_box, scene_title, theorem_box, warning_box


def _wrap(text: str, width: int = 56) -> str:
    return "\n".join(textwrap.fill(line, width=width) for line in text.split("\n"))


class DistancePointDroite(NotionScene):
    def construct(self):
        titre = scene_title("Distance d'un point à une droite")
        titre.scale(0.45)
        titre.to_edge(UP)

        # --- Énoncé : définition (projeté orthogonal) -----------------------------
        axes = Axes(
            x_range=[-1, 4, 1], y_range=[-1, 3, 1], x_length=4.4, y_length=3.4,
            axis_config={"include_tip": False, "color": WHITE},
        ).move_to(LEFT * 3.3 + DOWN * 0.4)
        droite = axes.plot(lambda x: -0.4 * x + 1.5, x_range=[-1, 4], color=WHITE)
        pt_a = axes.c2p(3, 2.2)
        pt_h = axes.c2p(2.1, 0.66)
        dot_a = Dot(pt_a, color="#DE7C1F")
        dot_h = Dot(pt_h, color="#288073")
        seg_ah = DashedLine(pt_a, pt_h, color=YELLOW)
        label_a = MathTex("A", font_size=26).next_to(dot_a, UP, buff=0.1)
        label_h = MathTex("H", font_size=24).next_to(dot_h, DOWN, buff=0.1)
        label_d = MathTex("(D)", font_size=24).next_to(droite.get_start(), LEFT, buff=0.1)
        schema = VGroup(axes, droite, dot_a, dot_h, seg_ah, label_a, label_h, label_d)

        definition = definition_box(
            VGroup(
                Text("Distance d'un point à une droite", font_size=22, weight="BOLD"),
                Text(
                    _wrap(
                        "d(A,(D)) est la plus petite distance entre A et un "
                        "point de (D) : elle est atteinte au projeté "
                        "orthogonal H de A sur (D). d(A,(D)) = AH.",
                        width=40,
                    ),
                    font_size=20,
                ),
            ).arrange(DOWN, buff=0.25),
            box_width=6.6,
        )
        definition.move_to(RIGHT * 3.4 + DOWN * 0.4)

        with self.voiceover(
            text=(
                "La distance d'un point A à une droite (D) est la plus "
                "petite distance entre A et un point quelconque de (D). "
                "Cette distance minimale est atteinte exactement au "
                "projeté orthogonal H de A sur (D) : la distance de A à "
                "(D) est donc la longueur A-H."
            )
        ) as tracker:
            self.play(Write(titre))
            self.play(Create(schema))
            self.play(FadeIn(definition))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(schema), FadeOut(definition))

        # --- Raisonnement : théorème + démonstration -----------------------------
        theoreme = theorem_box(
            MathTex(
                r"(D):ax+by+c=0,\ A(x_0;y_0) \ \Rightarrow\ "
                r"d(A,(D)) = \dfrac{|ax_0+by_0+c|}{\sqrt{a^2+b^2}}",
                font_size=28,
            ),
        )
        theoreme.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Voici la formule à connaître : la distance de A, de "
                "coordonnées x-zéro, y-zéro, à la droite (D) d'équation a x "
                "plus b y plus c égale zéro, vaut la valeur absolue de a "
                "x-zéro, plus b y-zéro, plus c, le tout divisé par la "
                "racine carrée de a carré plus b carré. Démontrons-la."
            )
        ) as tracker:
            self.play(FadeIn(theoreme))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(theoreme))

        demo1 = VGroup(
            MathTex(
                r"\vec{n}(a;b) \text{ normal à } (D) \ \Rightarrow\ "
                r"\overrightarrow{AH} \text{ colinéaire à } \vec{n} \ (\text{car } AH\perp(D))",
                font_size=24,
            ),
            MathTex(
                r"|\overrightarrow{AH}\cdot\vec{n}| = AH \times \|\vec{n}\| \ "
                r"(\text{colinéaires}) \ \Rightarrow\ AH = \dfrac{|\overrightarrow{AH}\cdot\vec{n}|}{\|\vec{n}\|}",
                font_size=24,
            ),
        ).arrange(DOWN, buff=0.32)
        demo1.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Le vecteur n de coordonnées a, b est normal à (D), et le "
                "segment A-H est perpendiculaire à (D) puisque H est le "
                "projeté orthogonal de A : le vecteur A-H est donc "
                "colinéaire à n. Pour deux vecteurs colinéaires, la valeur "
                "absolue de leur produit scalaire est égale au produit de "
                "leurs normes, ce qui donne A-H égale valeur absolue du "
                "produit scalaire de A-H et n, divisée par la norme de n."
            )
        ) as tracker:
            self.play(Write(demo1))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(demo1))

        demo2 = VGroup(
            MathTex(
                r"H \in (D) \ \Rightarrow\ ax_H+by_H+c=0 \ \Rightarrow\ c = -ax_H-by_H",
                font_size=24,
            ),
            MathTex(
                r"\overrightarrow{AH}\cdot\vec{n} = a(x_H-x_0)+b(y_H-y_0) = (ax_H+by_H)-(ax_0+by_0)",
                font_size=23,
            ),
            MathTex(
                r"= -c - (ax_0+by_0) = -(ax_0+by_0+c)",
                font_size=24,
            ),
            MathTex(
                r"\Rightarrow\ AH = \dfrac{|ax_0+by_0+c|}{\sqrt{a^2+b^2}}",
                font_size=27,
                color=YELLOW,
            ),
        ).arrange(DOWN, buff=0.25)
        demo2.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Comme H appartient à (D), ses coordonnées vérifient "
                "l'équation, ce qui permet d'exprimer c. On calcule ensuite "
                "le produit scalaire de A-H et n en fonction des "
                "coordonnées de A et de H, et tout se simplifie pour faire "
                "apparaître exactement a x-zéro, plus b y-zéro, plus c, au "
                "signe près. Comme la norme de n vaut racine de a carré "
                "plus b carré, on retrouve bien la formule annoncée."
            )
        ) as tracker:
            self.play(Write(demo2))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(demo2))

        # --- Exemple traité ---------------------------------------------------
        exemple = example_box(
            MathTex(
                r"A(4;-1),\ (D): 3x+4y-10=0"
                r"\\[6pt]"
                r"d(A,(D)) = \dfrac{|3\times4+4\times(-1)-10|}{\sqrt{3^2+4^2}}"
                r"\\[6pt]"
                r"= \dfrac{|12-4-10|}{\sqrt{25}} = \dfrac{|-2|}{5} = \dfrac{2}{5}",
                font_size=26,
            ),
        )
        exemple.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Exemple : calculons la distance du point A, de "
                "coordonnées 4 et moins 1, à la droite (D) d'équation 3x "
                "plus 4y moins 10 égale zéro. On remplace : valeur absolue "
                "de 3 fois 4, plus 4 fois moins 1, moins 10, divisée par "
                "racine de 3 carré plus 4 carré. Cela donne valeur absolue "
                "de 12 moins 4 moins 10, sur racine de 25, soit valeur "
                "absolue de moins 2, sur 5, donc deux cinquièmes."
            )
        ) as tracker:
            self.play(FadeIn(exemple))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(exemple))

        # --- À retenir --------------------------------------------------------
        retenir = definition_box(
            MathTex(
                r"d(A,(D)) = \dfrac{|ax_0+by_0+c|}{\sqrt{a^2+b^2}} \quad \text{(repère orthonormé)}",
                font_size=27,
            ),
        )
        retenir.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "À retenir : pour calculer la distance d'un point à une "
                "droite, on remplace les coordonnées du point dans "
                "l'équation, on prend la valeur absolue, et on divise par "
                "la racine carrée de la somme des carrés de a et b."
            )
        ) as tracker:
            self.play(FadeIn(retenir))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(retenir))

        # --- Piège à éviter -----------------------------------------------------
        piege = warning_box(
            Text(
                _wrap(
                    "Deux oublis fréquents : la valeur absolue au numérateur "
                    "(une distance est toujours positive), et la racine "
                    "carrée au dénominateur (on ne divise PAS par a²+b², "
                    "mais par sa racine). Repère orthonormé indispensable.",
                    width=48,
                ),
                font_size=21,
            ),
        )
        piege.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Deux oublis très fréquents à éviter. D'abord, la valeur "
                "absolue au numérateur : une distance est toujours "
                "positive ou nulle, jamais négative. Ensuite, la racine "
                "carrée au dénominateur : on ne divise pas par a carré plus "
                "b carré, mais bien par sa racine carrée. Et bien sûr, le "
                "repère doit être orthonormé."
            )
        ) as tracker:
            self.play(FadeIn(piege))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(piege), FadeOut(titre))
