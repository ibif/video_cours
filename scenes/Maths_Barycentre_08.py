"""
scenes/Maths_Barycentre_08.py — Chapitre 4 « Barycentre » (1ereC, Maths),
scène 08.

§ Centre de gravité d'un triangle (isobarycentre) : AG⃗=1/3 AB⃗+1/3 AC⃗,
GA⃗+GB⃗+GC⃗=0⃗, G aux 2/3 de chaque médiane, avec démonstration utilisant le
milieu A' de [BC] et l'associativité.
Source : 1ereC/Maths.pdf, chapitre 4, page 46.
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
    Text,
    VGroup,
    Write,
)

from shapes.base_scene import NotionScene
from shapes.boxes import property_box, scene_title, warning_box


def _wrap(text: str, width: int = 54) -> str:
    return "\n".join(textwrap.fill(line, width=width) for line in text.split("\n"))


def _dot_label(point, label, color=WHITE, label_dir=UP, font_size=28, dot_color=YELLOW):
    d = Dot(point, color=dot_color, radius=0.07)
    t = MathTex(label, font_size=font_size, color=color)
    t.next_to(d, label_dir, buff=0.12)
    return VGroup(d, t)


class CentreDeGraviteTriangle(NotionScene):
    def construct(self):
        titre = scene_title("Barycentre — Centre de gravité d'un triangle")
        titre.scale(0.48)
        titre.to_edge(UP)

        a_pt = LEFT * 2.8 + UP * 1.6
        b_pt = LEFT * 2.8 + DOWN * 1.6
        c_pt = RIGHT * 2.2 + DOWN * 0.2

        # --- Énoncé ---------------------------------------------------------
        pa = _dot_label(a_pt, "A")
        pb = _dot_label(b_pt, "B", label_dir=DOWN)
        pc = _dot_label(c_pt, "C", label_dir=RIGHT)
        triangle_abc = VGroup(Line(a_pt, b_pt), Line(b_pt, c_pt), Line(c_pt, a_pt), pa, pb, pc)
        triangle_abc.scale(0.9).move_to(DOWN * 0.7)

        question = Text(
            _wrap(
                "L'isobarycentre G d'un triangle ABC est le centre de "
                "gravité vu en physique. Où se trouve-t-il exactement ?",
                width=52,
            ),
            font_size=25,
        )
        question.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "L'isobarycentre G d'un triangle A-B-C, c'est-à-dire le "
                "barycentre des trois points affectés de coefficients "
                "égaux, est aussi appelé le centre de gravité du "
                "triangle, celui que l'on retrouve en physique. Où se "
                "trouve-t-il exactement, et quelles relations vérifie-t-il ?"
            )
        ) as tracker:
            self.play(Write(titre))
            self.play(FadeIn(question))
            self.play(Create(triangle_abc))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(question), FadeOut(triangle_abc))

        # --- Raisonnement : propriété + démonstration -------------------------
        enonce = VGroup(
            MathTex(r"\overrightarrow{AG} = \dfrac{1}{3}\,\overrightarrow{AB}+\dfrac{1}{3}\,\overrightarrow{AC}", font_size=25),
            MathTex(r"\overrightarrow{GA}+\overrightarrow{GB}+\overrightarrow{GC} = \vec{0}", font_size=25),
            Text("G est situé aux 2/3 de chaque médiane, à partir du sommet.", font_size=22),
        ).arrange(DOWN, buff=0.3)
        propriete = property_box(enonce)
        propriete.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Voici les trois propriétés du centre de gravité. "
                "Premièrement, le vecteur A-G est égal à un tiers du "
                "vecteur A-B, plus un tiers du vecteur A-C. Deuxièmement, "
                "la somme des trois vecteurs G-A, G-B et G-C est le "
                "vecteur nul, ce qui découle directement de la définition "
                "de l'isobarycentre. Troisièmement, G est situé aux deux "
                "tiers de chaque médiane, en partant du sommet. Une "
                "médiane relie un sommet au milieu du côté opposé."
            )
        ) as tracker:
            self.play(FadeIn(propriete))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(propriete))

        etape1 = MathTex(r"A' = \text{milieu de } [BC] = \mathrm{bar}\{(B,1)\,;\,(C,1)\}", font_size=24)
        etape2 = MathTex(
            r"G = \mathrm{bar}\{(A,1)\,;\,(B,1)\,;\,(C,1)\} = \mathrm{bar}\{(A,1)\,;\,(A',2)\}"
            r"\quad (\text{associativité})",
            font_size=22,
        )
        etape3 = MathTex(r"\overrightarrow{AG} = \dfrac{2}{1+2}\,\overrightarrow{AA'} = \dfrac{2}{3}\,\overrightarrow{AA'}", font_size=25, color=YELLOW)
        etape4 = MathTex(
            r"\overrightarrow{AA'} = \dfrac{1}{2}\big(\overrightarrow{AB}+\overrightarrow{AC}\big)"
            r"\ \Rightarrow\ \overrightarrow{AG} = \dfrac{2}{3}\times\dfrac{1}{2}\big(\overrightarrow{AB}+\overrightarrow{AC}\big) "
            r"= \dfrac{1}{3}\,\overrightarrow{AB}+\dfrac{1}{3}\,\overrightarrow{AC}",
            font_size=21,
        )
        demo = VGroup(etape1, etape2, etape3, etape4).arrange(DOWN, buff=0.3)
        demo.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Démontrons ces résultats en utilisant le milieu A-prime "
                "du côté B-C, c'est-à-dire le barycentre de B-un et C-un. "
                "Par associativité, G, isobarycentre de A, B et C, est "
                "aussi le barycentre de A-un et de A-prime, affecté du "
                "coefficient deux, la somme de un et un. On en déduit que "
                "le vecteur A-G est égal à deux tiers du vecteur A-A-"
                "prime : G est donc sur la médiane issue de A, aux deux "
                "tiers en partant de A. Comme A-prime est le milieu de "
                "B-C, le vecteur A-A-prime est la demi-somme de A-B et "
                "A-C, ce qui redonne exactement la première formule : "
                "A-G égale un tiers A-B plus un tiers A-C."
            )
        ) as tracker:
            self.play(Write(demo))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(demo))

        # --- Exemple traité : figure complète -------------------------------------
        a_prime = (b_pt + c_pt) / 2
        g_pt = a_pt + (2 / 3) * (a_prime - a_pt)

        pa2 = _dot_label(a_pt, "A")
        pb2 = _dot_label(b_pt, "B", label_dir=DOWN)
        pc2 = _dot_label(c_pt, "C", label_dir=RIGHT)
        pa_prime = _dot_label(a_prime, "A'", dot_color="#A42A5A", label_dir=DOWN)
        pg = _dot_label(g_pt, "G", dot_color="#288073", label_dir=LEFT)

        triangle = VGroup(Line(a_pt, b_pt), Line(b_pt, c_pt), Line(c_pt, a_pt))
        mediane_a = Line(a_pt, a_prime, color="#A42A5A")
        mediane_b = Line(b_pt, (a_pt + c_pt) / 2, color="#A42A5A")
        mediane_c = Line(c_pt, (a_pt + b_pt) / 2, color="#A42A5A")
        figure = VGroup(triangle, mediane_a, mediane_b, mediane_c, pa2, pb2, pc2, pa_prime, pg)
        figure.scale(0.9).move_to(DOWN * 0.4)

        legende = Text("G se trouve à l'intersection des trois médianes.", font_size=22, color=YELLOW)
        legende.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Voici le triangle A-B-C avec ses trois médianes tracées. "
                "Le raisonnement précédent, mené à partir du sommet A, "
                "s'applique de façon identique à partir de B et de C : G "
                "se trouve donc aux deux tiers de chacune des trois "
                "médianes, ce qui prouve au passage qu'elles sont "
                "concourantes en ce même point G, le centre de gravité du "
                "triangle."
            )
        ) as tracker:
            self.play(FadeIn(legende))
            self.play(Create(figure))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(legende), FadeOut(figure))

        # --- À retenir -----------------------------------------------------------
        retenir = property_box(
            VGroup(
                MathTex(r"\overrightarrow{AG} = \dfrac{1}{3}\overrightarrow{AB}+\dfrac{1}{3}\overrightarrow{AC}", font_size=24),
                MathTex(r"\overrightarrow{GA}+\overrightarrow{GB}+\overrightarrow{GC} = \vec{0}", font_size=24),
                Text("G aux 2/3 de chaque médiane, à partir du sommet.", font_size=21),
            ).arrange(DOWN, buff=0.25),
        )
        retenir.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "À retenir : le centre de gravité d'un triangle vérifie "
                "ces trois relations vectorielles, et se situe toujours "
                "aux deux tiers de chaque médiane, en partant du sommet."
            )
        ) as tracker:
            self.play(FadeIn(retenir))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(retenir))

        # --- Piège à éviter ------------------------------------------------------
        piege = warning_box(
            Text(
                _wrap(
                    "« Aux deux tiers de la médiane » se compte à partir "
                    "du SOMMET, pas à partir du milieu du côté opposé "
                    "(qui donnerait un tiers, pas deux tiers).",
                    width=48,
                ),
                font_size=23,
            ),
        )
        piege.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Piège fréquent : « aux deux tiers de la médiane » se "
                "compte à partir du sommet, et non à partir du milieu du "
                "côté opposé. Compté depuis ce milieu, ce serait un "
                "tiers, pas deux tiers."
            )
        ) as tracker:
            self.play(FadeIn(piege))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(piege), FadeOut(titre))
