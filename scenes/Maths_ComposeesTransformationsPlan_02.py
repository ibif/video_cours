"""
scenes/Maths_ComposeesTransformationsPlan_02.py — Chapitre 8 « Composées de
transformations du plan » (1ereC, Maths), scène 02.

§ Rappels sur les transformations usuelles (2/2) : symétrie centrale
(expression analytique, propriétés), rotation (expression analytique,
quart de tour), homothétie (expression analytique, propriété vectorielle
et réciproque, effets sur distances/aires).
Source : 1ereC/Maths.pdf, chapitre 8, pages 93-95.
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
from shapes.boxes import definition_box, scene_title, theorem_box


def _wrap(text: str, width: int = 56) -> str:
    return "\n".join(textwrap.fill(line, width=width) for line in text.split("\n"))


def _dot_label(point, label, color=WHITE, label_dir=UP, font_size=28, dot_color=YELLOW):
    d = Dot(point, color=dot_color, radius=0.08)
    t = MathTex(label, font_size=font_size, color=color)
    t.next_to(d, label_dir, buff=0.15)
    return VGroup(d, t)


class RappelsTransformationsUsuelles2(NotionScene):
    def construct(self):
        titre = scene_title("Rappels — Transformations usuelles (2/2)")
        titre.scale(0.48)
        titre.to_edge(UP)
        self.play(Write(titre))

        # --- Énoncé : symétrie centrale ------------------------------------
        def_sym_centrale = definition_box(
            VGroup(
                Text("Symétrie centrale de centre Ω", font_size=25, weight="BOLD"),
                MathTex(r"M' = s_{\Omega}(M) \iff \Omega \text{ milieu de } [MM']", font_size=27),
                MathTex(r"\Omega(a\,;\,b): \quad x'=2a-x, \quad y'=2b-y", font_size=27),
                Text(_wrap("Déplacement, involutive : sΩ∘sΩ = id."), font_size=22),
            ).arrange(DOWN, buff=0.25)
        )
        def_sym_centrale.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "La symétrie centrale de centre Oméga associe à M le "
                "point M prime tel que Oméga soit le milieu du segment M "
                "M prime. Si Oméga a pour coordonnées a et b, l'expression "
                "analytique est x prime égale 2a moins x, y prime égale 2b "
                "moins y. Contrairement à la symétrie axiale, c'est un "
                "déplacement, qui conserve les angles orientés. Elle reste "
                "involutive."
            )
        ) as tracker:
            self.play(FadeIn(def_sym_centrale))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(def_sym_centrale))

        # --- Raisonnement : rotation ------------------------------------------
        def_rotation = definition_box(
            VGroup(
                Text("Rotation de centre O, angle θ", font_size=25, weight="BOLD"),
                MathTex(
                    r"\begin{cases} x' = x\cos\theta - y\sin\theta \\ y' = x\sin\theta + y\cos\theta \end{cases}"
                    r"\quad (\text{centre } O(0\,;0))",
                    font_size=26,
                ),
                Text(_wrap("Le quart de tour correspond à θ = π/2 (sens direct)."), font_size=22),
            ).arrange(DOWN, buff=0.25)
        )
        def_rotation.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "La rotation de centre O et d'angle thêta conserve la "
                "distance au centre et fait tourner tous les points du "
                "même angle orienté. Lorsque le centre est l'origine, son "
                "expression analytique fait intervenir cosinus et sinus de "
                "thêta, comme indiqué ici. Le quart de tour est le cas "
                "particulier où thêta vaut pi sur deux, dans le sens "
                "direct."
            )
        ) as tracker:
            self.play(FadeIn(def_rotation))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(def_rotation))

        # --- Exemple traité : homothétie + propriété vectorielle --------------
        def_homothetie = definition_box(
            VGroup(
                Text("Homothétie de centre Ω, rapport k", font_size=24, weight="BOLD"),
                MathTex(r"M' = h_{(\Omega,k)}(M) \iff \overrightarrow{\Omega M'} = k\,\overrightarrow{\Omega M}", font_size=27),
                MathTex(r"\Omega(a\,;\,b): \quad x'-a = k(x-a), \quad y'-b=k(y-b)", font_size=25),
            ).arrange(DOWN, buff=0.25)
        )
        def_homothetie.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "L'homothétie de centre Oméga et de rapport k, un réel non "
                "nul, associe à M le point M prime tel que le vecteur "
                "Oméga-M prime soit égal à k fois le vecteur Oméga-M. Son "
                "expression analytique se déduit directement de cette "
                "définition."
            )
        ) as tracker:
            self.play(FadeIn(def_homothetie))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(def_homothetie))

        prop_vect = theorem_box(
            VGroup(
                Text("Propriété caractéristique", font_size=24, weight="BOLD"),
                MathTex(r"f = h_{(\Omega,k)} \implies \overrightarrow{A'B'} = k\,\overrightarrow{AB} \ \ \forall A,B", font_size=27),
                MathTex(
                    r"\text{R\'eciproquement, si } \overrightarrow{A'B'}=k\,\overrightarrow{AB} \text{ pour tous } A,B,"
                    r"\text{ alors } f \text{ est une homoth\'etie de rapport } k",
                    font_size=22,
                ),
                Text(_wrap("Effets : distances multipliées par |k|, aires multipliées par k²."), font_size=22),
            ).arrange(DOWN, buff=0.25)
        )
        prop_vect.next_to(titre, DOWN, buff=0.35)

        with self.voiceover(
            text=(
                "Voici la propriété vectorielle fondamentale des "
                "homothéties : si f est l'homothétie de centre Oméga et de "
                "rapport k, alors pour tous points A et B, le vecteur A "
                "prime B prime est égal à k fois le vecteur AB. Cette "
                "propriété admet une réciproque très utile : si une "
                "transformation multiplie ainsi tous les vecteurs par un "
                "même réel k constant, alors c'est nécessairement une "
                "homothétie de rapport k. Conséquence directe : les "
                "distances sont multipliées par la valeur absolue de k, et "
                "les aires par k au carré."
            )
        ) as tracker:
            self.play(FadeIn(prop_vect))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(prop_vect))

        # --- Illustration rapide -------------------------------------------
        omega = _dot_label(LEFT * 3, "\\Omega", dot_color="#288073", label_dir=DOWN)
        pt_a = _dot_label(RIGHT * 0.5 + UP * 0.8, "A")
        pt_b = _dot_label(RIGHT * 1.5 + DOWN * 0.6, "B")
        seg_ab = Line(pt_a[0].get_center(), pt_b[0].get_center(), color=WHITE)
        # k = 2 : A', B' obtenus en doublant les vecteurs depuis Ω
        o_pt = omega[0].get_center()
        a_pt = pt_a[0].get_center()
        b_pt = pt_b[0].get_center()
        a_prime_pt = o_pt + 2 * (a_pt - o_pt)
        b_prime_pt = o_pt + 2 * (b_pt - o_pt)
        pt_a1 = _dot_label(a_prime_pt, "A'", color=YELLOW)
        pt_b1 = _dot_label(b_prime_pt, "B'", color=YELLOW)
        seg_a1b1 = Line(a_prime_pt, b_prime_pt, color=YELLOW)
        lignes_centre = VGroup(
            Line(o_pt, a_prime_pt, color="#595959", stroke_width=1.5),
            Line(o_pt, b_prime_pt, color="#595959", stroke_width=1.5),
        )
        figure_homothetie = VGroup(lignes_centre, omega, pt_a, pt_b, seg_ab, pt_a1, pt_b1, seg_a1b1)
        figure_homothetie.move_to(DOWN * 0.5)

        with self.voiceover(
            text=(
                "Sur cette figure, l'homothétie de centre Oméga et de "
                "rapport 2 envoie A et B sur A prime et B prime, alignés "
                "avec Oméga, à une distance double : le segment A prime B "
                "prime est bien deux fois plus long que le segment AB, et "
                "parallèle à celui-ci."
            )
        ) as tracker:
            self.play(Create(figure_homothetie))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(figure_homothetie))

        # --- À retenir --------------------------------------------------------
        retenir = definition_box(
            VGroup(
                MathTex(r"s_\Omega:\ x'=2a-x,\ y'=2b-y \quad (\text{d\'eplacement, involutive})", font_size=24),
                MathTex(r"r_{(O,\theta)}:\ \cos\theta,\ \sin\theta \quad (\text{d\'eplacement})", font_size=24),
                MathTex(r"h_{(\Omega,k)}:\ \overrightarrow{A'B'}=k\,\overrightarrow{AB} \quad (\text{distances} \times |k|,\ \text{aires}\times k^2)", font_size=24),
            ).arrange(DOWN, buff=0.3)
        )
        retenir.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "À retenir : symétrie centrale et rotation sont des "
                "déplacements caractérisés respectivement par leur centre, "
                "et par leur centre et leur angle. L'homothétie, elle, est "
                "entièrement caractérisée par la propriété vectorielle A "
                "prime B prime égale k fois AB, valable pour tous les "
                "points du plan."
            )
        ) as tracker:
            self.play(FadeIn(retenir))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(retenir), FadeOut(titre))
