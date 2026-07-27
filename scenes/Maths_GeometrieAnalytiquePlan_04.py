"""
scenes/Maths_GeometrieAnalytiquePlan_04.py — Chapitre 14 « Géométrie
analytique du plan » (1ereC, Maths), scène 04.

§ Applications du déterminant : alignement de trois points
(det(AB⃗,AC⃗)=0), parallélisme de deux droites, aire du triangle =
½|det(AB⃗,AC⃗)| (repère ORTHONORMÉ). Exemple résolu : A(2;3), B(5;1),
C(-1;7), det=6≠0 (non alignés), aire=3.
Source : 1ereC/Maths.pdf, chapitre 14, page 168.
"""

import textwrap

from manim import DOWN, LEFT, RIGHT, UP, WHITE, YELLOW, Create, Dot, FadeIn, FadeOut, MathTex, Polygon, Text, VGroup, Write

from shapes.base_scene import NotionScene
from shapes.boxes import example_box, property_box, scene_title, warning_box


def _wrap(text: str, width: int = 56) -> str:
    return "\n".join(textwrap.fill(line, width=width) for line in text.split("\n"))


def _dot_label(point, label, color=WHITE, label_dir=UP, font_size=28, dot_color=YELLOW):
    d = Dot(point, color=dot_color, radius=0.07)
    t = MathTex(label, font_size=font_size, color=color)
    t.next_to(d, label_dir, buff=0.12)
    return VGroup(d, t)


class ApplicationsDeterminant(NotionScene):
    def construct(self):
        titre = scene_title("Applications du déterminant : alignement, parallélisme, aire")
        titre.scale(0.38)
        titre.to_edge(UP)

        # --- Énoncé -------------------------------------------------------------
        enonce = Text(
            _wrap(
                "Le déterminant, en plus de tester la colinéarité de deux "
                "vecteurs, permet de répondre à trois questions "
                "géométriques : trois points sont-ils alignés ? Deux "
                "droites sont-elles parallèles ? Quelle est l'aire d'un "
                "triangle ?",
                width=54,
            ),
            font_size=24,
        )
        enonce.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Le déterminant de deux vecteurs ne sert pas qu'à tester la "
                "colinéarité abstraite : il répond directement à trois "
                "questions géométriques très fréquentes. Trois points "
                "sont-ils alignés ? Deux droites sont-elles parallèles ? Et "
                "quelle est l'aire d'un triangle ?"
            )
        ) as tracker:
            self.play(Write(titre))
            self.play(FadeIn(enonce))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(enonce))

        # --- Raisonnement : alignement et parallélisme ----------------------------
        alignement = property_box(
            VGroup(
                Text("Alignement de trois points", font_size=23, weight="BOLD"),
                MathTex(
                    r"A,B,C \text{ alignés} \iff \det(\overrightarrow{AB},\overrightarrow{AC}) = 0",
                    font_size=27,
                ),
            ).arrange(DOWN, buff=0.25),
            box_width=10.0,
        )
        alignement.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Premier résultat : trois points A, B et C sont alignés si "
                "et seulement si les vecteurs A-B et A-C sont colinéaires, "
                "c'est-à-dire si leur déterminant est nul. C'est une simple "
                "application directe du critère vu précédemment, avec deux "
                "vecteurs partant du même point A."
            )
        ) as tracker:
            self.play(FadeIn(alignement))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(alignement))

        parallelisme = property_box(
            VGroup(
                Text("Parallélisme de deux droites", font_size=23, weight="BOLD"),
                MathTex(
                    r"(D) \parallel (D') \iff \vec{u}_D \text{ et } \vec{u}_{D'} "
                    r"\text{ colinéaires} \iff \det(\vec{u}_D,\vec{u}_{D'}) = 0",
                    font_size=25,
                ),
            ).arrange(DOWN, buff=0.25),
            box_width=11.2,
        )
        parallelisme.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Deuxième résultat : deux droites sont parallèles si et "
                "seulement si leurs vecteurs directeurs respectifs sont "
                "colinéaires, donc si le déterminant de ces deux vecteurs "
                "directeurs est nul. On retrouve encore le même critère."
            )
        ) as tracker:
            self.play(FadeIn(parallelisme))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(parallelisme))

        aire = property_box(
            VGroup(
                Text("Aire d'un triangle (repère orthonormé)", font_size=23, weight="BOLD"),
                MathTex(
                    r"\mathcal{A}_{ABC} = \dfrac{1}{2}\big|\det(\overrightarrow{AB},\overrightarrow{AC})\big|",
                    font_size=28,
                ),
            ).arrange(DOWN, buff=0.25),
            box_width=9.0,
        )
        aire.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Troisième résultat, uniquement valable en repère "
                "orthonormé cette fois : l'aire du triangle A-B-C est égale "
                "à la moitié de la valeur absolue du déterminant des "
                "vecteurs A-B et A-C. La valeur absolue est indispensable "
                "car une aire est toujours positive, alors que le "
                "déterminant peut être négatif."
            )
        ) as tracker:
            self.play(FadeIn(aire))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(aire))

        # --- Exemple traité ---------------------------------------------------
        pa = _dot_label(LEFT * 2.2 + DOWN * 1.0, "A")
        pb = _dot_label(RIGHT * 2.2 + DOWN * 1.0, "B", label_dir=DOWN)
        pc = _dot_label(LEFT * 1.0 + UP * 1.8, "C")
        triangle = Polygon(pa[0].get_center(), pb[0].get_center(), pc[0].get_center(), color="#DE7C1F", fill_color="#DE7C1F", fill_opacity=0.25)
        figure = VGroup(triangle, pa, pb, pc)
        figure.scale(0.9).move_to(LEFT * 3.3 + DOWN * 0.2)

        calcul = example_box(
            MathTex(
                r"A(2;3),\ B(5;1),\ C(-1;7)"
                r"\\[6pt]"
                r"\overrightarrow{AB}(3;-2),\ \overrightarrow{AC}(-3;4)"
                r"\\[4pt]"
                r"\det(\overrightarrow{AB},\overrightarrow{AC}) = 3\times4-(-3)\times(-2) = 12-6=6 \neq 0"
                r"\\[4pt]"
                r"\Rightarrow\ A,B,C \text{ non alignés}"
                r"\\[4pt]"
                r"\mathcal{A}_{ABC} = \dfrac{1}{2}|6| = 3",
                font_size=23,
            ),
            box_width=6.4,
        )
        calcul.move_to(RIGHT * 3.2 + DOWN * 0.2)

        with self.voiceover(
            text=(
                "Reprenons nos points A de coordonnées 2 et 3, B de "
                "coordonnées 5 et 1, C de coordonnées moins un et 7. Les "
                "vecteurs A-B et A-C ont pour coordonnées 3, moins 2, et "
                "moins 3, 4. Le déterminant vaut 3 fois 4, moins moins 3 "
                "fois moins 2, soit 12 moins 6, donc 6, qui est non nul : "
                "les trois points ne sont pas alignés. L'aire du triangle "
                "A-B-C vaut alors un demi de la valeur absolue de 6, soit "
                "3 unités d'aire."
            )
        ) as tracker:
            self.play(Create(figure))
            self.play(FadeIn(calcul))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(figure), FadeOut(calcul))

        # --- À retenir --------------------------------------------------------
        retenir = property_box(
            VGroup(
                MathTex(r"A,B,C \text{ alignés} \iff \det(\overrightarrow{AB},\overrightarrow{AC})=0", font_size=25),
                MathTex(r"\mathcal{A}_{ABC} = \dfrac{1}{2}\big|\det(\overrightarrow{AB},\overrightarrow{AC})\big|", font_size=25),
            ).arrange(DOWN, buff=0.3),
            box_width=10.5,
        )
        retenir.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "À retenir : le déterminant de A-B et A-C nul signifie "
                "l'alignement des trois points, et sa valeur absolue divisée "
                "par deux donne directement l'aire du triangle A-B-C."
            )
        ) as tracker:
            self.play(FadeIn(retenir))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(retenir))

        # --- Piège à éviter -----------------------------------------------------
        piege = warning_box(
            Text(
                _wrap(
                    "L'alignement et le parallélisme se testent dans TOUT "
                    "repère (le déterminant s'en moque), mais la formule "
                    "d'aire n'est valable qu'en repère ORTHONORMÉ — comme "
                    "toute formule qui exprime une longueur ou une aire.",
                    width=48,
                ),
                font_size=22,
            ),
        )
        piege.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Attention à bien distinguer les deux régimes : le test "
                "d'alignement et le test de parallélisme fonctionnent dans "
                "n'importe quel repère, puisqu'ils reposent uniquement sur "
                "la nullité du déterminant. Mais dès qu'on veut calculer "
                "une aire, donc une grandeur métrique, le repère doit être "
                "orthonormé, exactement comme pour les distances."
            )
        ) as tracker:
            self.play(FadeIn(piege))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(piege), FadeOut(titre))
