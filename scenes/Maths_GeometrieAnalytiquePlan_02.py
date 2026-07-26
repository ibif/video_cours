"""
scenes/Maths_GeometrieAnalytiquePlan_02.py — Chapitre 14 « Géométrie
analytique du plan » (1ereC, Maths), scène 02.

§ Norme d'un vecteur et distance entre deux points, EN REPÈRE ORTHONORMÉ
uniquement : ‖u‖=√(x²+y²), AB=√((xB-xA)²+(yB-yA)²), démonstration par le
théorème de Pythagore. Reprise de l'exemple A(2;3), B(5;1) : AB=√13.
Source : 1ereC/Maths.pdf, chapitre 14, page 166.
"""

import textwrap

from manim import (
    DOWN,
    LEFT,
    RIGHT,
    UP,
    WHITE,
    YELLOW,
    Create,
    Dot,
    FadeIn,
    FadeOut,
    Line,
    MathTex,
    Polygon,
    Text,
    VGroup,
    Write,
)

from shapes.base_scene import NotionScene
from shapes.boxes import definition_box, example_box, scene_title, theorem_box, warning_box


def _wrap(text: str, width: int = 56) -> str:
    return "\n".join(textwrap.fill(line, width=width) for line in text.split("\n"))


class NormeDistanceRepereOrthonorme(NotionScene):
    def construct(self):
        titre = scene_title("Norme d'un vecteur et distance — repère orthonormé")
        titre.scale(0.42)
        titre.to_edge(UP)

        # --- Énoncé -------------------------------------------------------------
        enonce = Text(
            _wrap(
                "À partir de maintenant, le repère (O;i,j) est supposé "
                "ORTHONORMÉ : c'est la condition indispensable pour parler "
                "de longueur, de distance et de norme.",
                width=54,
            ),
            font_size=25,
        )
        enonce.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Jusqu'ici, nos formules étaient valables dans un repère "
                "quelconque. Mais pour parler de longueur ou de distance, "
                "il faut désormais se placer dans un repère orthonormé : "
                "c'est la condition indispensable, que nous garderons pour "
                "tout le reste du chapitre sauf mention contraire."
            )
        ) as tracker:
            self.play(Write(titre))
            self.play(FadeIn(enonce))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(enonce))

        # --- Raisonnement : théorème + démonstration -----------------------------
        theoreme = theorem_box(
            VGroup(
                MathTex(r"\vec{u}(x;y) \ \Rightarrow\ \|\vec{u}\| = \sqrt{x^2+y^2}", font_size=28),
                MathTex(
                    r"AB = \|\overrightarrow{AB}\| = \sqrt{(x_B-x_A)^2+(y_B-y_A)^2}",
                    font_size=28,
                ),
            ).arrange(DOWN, buff=0.3),
        )
        theoreme.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Voici le théorème : dans un repère orthonormé, la norme "
                "d'un vecteur u de coordonnées x et y vaut la racine carrée "
                "de x carré plus y carré. Et la distance A-B entre deux "
                "points est la norme du vecteur A-B, soit la racine carrée "
                "de x-B moins x-A, au carré, plus y-B moins y-A, au carré. "
                "Démontrons cette formule avec le théorème de Pythagore."
            )
        ) as tracker:
            self.play(FadeIn(theoreme))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(theoreme))

        o_pt = LEFT * 3 + DOWN * 1.5
        h_pt = o_pt + RIGHT * 3
        m_pt = o_pt + RIGHT * 3 + UP * 2
        triangle = Polygon(o_pt, h_pt, m_pt, color=WHITE, stroke_width=2)
        droit_marker = Polygon(
            h_pt + LEFT * 0.18, h_pt + LEFT * 0.18 + UP * 0.18, h_pt + UP * 0.18,
            color=WHITE, stroke_width=1.5, fill_opacity=0,
        )
        label_o = MathTex("O", font_size=26).next_to(o_pt, DOWN + LEFT, buff=0.1)
        label_h = MathTex("H(x;0)", font_size=22).next_to(h_pt, DOWN, buff=0.15)
        label_m = MathTex("M(x;y)", font_size=22).next_to(m_pt, UP, buff=0.15)
        schema = VGroup(triangle, droit_marker, label_o, label_h, label_m)
        schema.move_to(LEFT * 3.3 + DOWN * 0.4)

        demo = VGroup(
            Text("Triangle OHM rectangle en H", font_size=22, color=YELLOW),
            MathTex(r"OH = |x| \qquad HM = |y|", font_size=25),
            MathTex(
                r"OM^2 = OH^2 + HM^2 = x^2 + y^2 \ \text{(Pythagore)}",
                font_size=25,
            ),
            MathTex(r"\Rightarrow\ \|\vec{u}\| = OM = \sqrt{x^2+y^2}", font_size=27, color=YELLOW),
        ).arrange(DOWN, buff=0.3)
        demo.move_to(RIGHT * 3.0 + DOWN * 0.3)

        with self.voiceover(
            text=(
                "Plaçons le vecteur u d'origine O et d'extrémité M, de "
                "coordonnées x et y. Notons H le projeté de M sur l'axe des "
                "abscisses : le triangle O-H-M est rectangle en H, car le "
                "repère est orthonormé. On a alors O-H égal valeur absolue "
                "de x, et H-M égal valeur absolue de y. Le théorème de "
                "Pythagore donne O-M au carré égale O-H au carré plus H-M "
                "au carré, c'est-à-dire x carré plus y carré. En prenant la "
                "racine carrée, on retrouve exactement la norme du vecteur "
                "u : c'est la longueur O-M."
            )
        ) as tracker:
            self.play(Create(schema))
            self.play(Write(demo))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(schema), FadeOut(demo))

        # --- Exemple traité : reprise de l'exemple 1 ------------------------------
        a_pt = LEFT * 2.5 + DOWN * 0.3
        b_pt = RIGHT * 2.5 + UP * 1.0
        segment = Line(a_pt, b_pt, color=WHITE)
        pa = VGroup(Dot(a_pt, color=YELLOW), MathTex("A", font_size=26).next_to(a_pt, DOWN, buff=0.12))
        pb = VGroup(Dot(b_pt, color=YELLOW), MathTex("B", font_size=26).next_to(b_pt, UP, buff=0.12))
        figure = VGroup(segment, pa, pb)
        figure.move_to(LEFT * 3.3 + DOWN * 0.3)

        calcul = example_box(
            MathTex(
                r"A(2;3),\ B(5;1)"
                r"\\[6pt]"
                r"AB = \sqrt{(5-2)^2+(1-3)^2}"
                r"\\[4pt]"
                r"AB = \sqrt{9+4} = \sqrt{13}",
                font_size=27,
            ),
            box_width=6.0,
        )
        calcul.move_to(RIGHT * 3.3 + DOWN * 0.3)

        with self.voiceover(
            text=(
                "Reprenons notre exemple du début : A de coordonnées 2 et "
                "3, B de coordonnées 5 et 1. La distance A-B vaut la racine "
                "carrée de 5 moins 2, au carré, plus 1 moins 3, au carré, "
                "c'est-à-dire la racine carrée de 9 plus 4, soit racine de "
                "13."
            )
        ) as tracker:
            self.play(Create(figure))
            self.play(FadeIn(calcul))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(figure), FadeOut(calcul))

        # --- À retenir --------------------------------------------------------
        retenir = definition_box(
            MathTex(
                r"AB = \sqrt{(x_B-x_A)^2+(y_B-y_A)^2} \quad \text{(repère orthonormé)}",
                font_size=27,
            ),
        )
        retenir.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "À retenir : la distance entre deux points s'obtient en "
                "prenant la racine carrée de la somme des carrés des "
                "différences de coordonnées — à condition impérative que le "
                "repère soit orthonormé."
            )
        ) as tracker:
            self.play(FadeIn(retenir))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(retenir))

        # --- Piège à éviter -----------------------------------------------------
        piege = warning_box(
            Text(
                _wrap(
                    "Cette formule de distance est FAUSSE dans un repère "
                    "quelconque (non orthonormé) : la démonstration utilise "
                    "le théorème de Pythagore, qui exige un angle droit "
                    "entre les axes et des unités identiques sur i et j.",
                    width=48,
                ),
                font_size=22,
            ),
        )
        piege.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Piège fréquent : cette formule de distance est fausse dans "
                "un repère quelconque. La démonstration s'appuie sur le "
                "théorème de Pythagore, qui exige un angle droit entre les "
                "axes et des unités identiques sur i et j : sans repère "
                "orthonormé, aucune conclusion sur les longueurs n'est "
                "possible."
            )
        ) as tracker:
            self.play(FadeIn(piege))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(piege), FadeOut(titre))
