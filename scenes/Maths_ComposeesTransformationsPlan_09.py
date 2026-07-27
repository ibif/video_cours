"""
scenes/Maths_ComposeesTransformationsPlan_09.py — Chapitre 8 « Composées de
transformations du plan » (1ereC, Maths), scène 09.

§ Complément : composée de deux rotations r'∘r selon α+β≠0[2π] (rotation
d'angle α+β) ou α+β≡0[2π] (translation), démonstration par décomposition
en symétries axiales d'axe commun (OO'), cas particuliers, exemple résolu
5 (carré ABCD, rA=r(A,π/2), rB=r(B,π/2)).
Source : 1ereC/Maths.pdf, chapitre 8, pages 100-101.
"""

import textwrap

from manim import DOWN, LEFT, RIGHT, UP, WHITE, YELLOW, Create, Dot, FadeIn, FadeOut, MathTex, Polygon, Text, VGroup, Write

from shapes.base_scene import NotionScene
from shapes.boxes import example_box, scene_title, theorem_box, warning_box


def _wrap(text: str, width: int = 56) -> str:
    return "\n".join(textwrap.fill(line, width=width) for line in text.split("\n"))


def _dot_label(point, label, color=WHITE, label_dir=UP, font_size=28, dot_color=YELLOW):
    d = Dot(point, color=dot_color, radius=0.08)
    t = MathTex(label, font_size=font_size, color=color)
    t.next_to(d, label_dir, buff=0.15)
    return VGroup(d, t)


class ComposeeDeuxRotations(NotionScene):
    def construct(self):
        titre = scene_title("Complément — composée de deux rotations")
        titre.scale(0.44)
        titre.to_edge(UP)

        # --- Énoncé : théorème --------------------------------------------------
        theoreme = theorem_box(
            VGroup(
                Text("Composée de deux rotations", font_size=24, weight="BOLD"),
                MathTex(r"r=r_{(O,\alpha)}, \quad r'=r_{(O',\beta)}", font_size=26),
                MathTex(r"\alpha+\beta\not\equiv 0\,[2\pi] \implies r'\circ r = r_{(\Omega,\,\alpha+\beta)}", font_size=25),
                MathTex(r"\alpha+\beta\equiv 0\,[2\pi] \implies r'\circ r \text{ est une translation}", font_size=25),
            ).arrange(DOWN, buff=0.22)
        )
        theoreme.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Complétons le panorama avec la composée de deux "
                "rotations, r de centre O et d'angle alpha, puis r prime "
                "de centre O prime et d'angle bêta. Si la somme alpha plus "
                "bêta n'est pas un multiple de 2 pi, la composée est une "
                "rotation d'angle alpha plus bêta, autour d'un centre "
                "Oméga à déterminer. Si au contraire cette somme est un "
                "multiple de 2 pi, la composée dégénère en une "
                "translation."
            )
        ) as tracker:
            self.play(Write(titre))
            self.play(FadeIn(theoreme))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(theoreme))

        # --- Raisonnement : démonstration par décomposition ----------------------
        etape1 = Text(
            _wrap("On décompose r et r' en symétries axiales partageant un même axe : la droite (OO')."),
            font_size=22,
        )
        etape2 = MathTex(
            r"r = s_{\Delta_2}\circ s_{\Delta_1} \ (\text{angle } \Delta_1,\Delta_2 = \alpha/2, \ \Delta_2=(OO'))",
            font_size=23,
        )
        etape3 = MathTex(
            r"r' = s_{\Delta_4}\circ s_{\Delta_3} \ (\text{angle } \Delta_3,\Delta_4 = \beta/2, \ \Delta_3=(OO'))",
            font_size=23,
        )
        etape4 = MathTex(
            r"r'\circ r = s_{\Delta_4}\circ\underbrace{(s_{\Delta_3}\circ s_{\Delta_2})}_{\Delta_2=\Delta_3 \Rightarrow\, \mathrm{id}}\circ s_{\Delta_1} = s_{\Delta_4}\circ s_{\Delta_1}",
            font_size=21,
            color=YELLOW,
        )
        demo = VGroup(etape1, etape2, etape3, etape4).arrange(DOWN, buff=0.28)
        demo.next_to(titre, DOWN, buff=0.35)

        with self.voiceover(
            text=(
                "L'idée de la démonstration est élégante : on décompose "
                "chaque rotation en deux symétries axiales, en choisissant "
                "à chaque fois la droite O O prime comme axe commun. Pour "
                "r, on prend delta 1 et delta 2 égal à la droite O O "
                "prime, formant un angle alpha sur deux. Pour r prime, on "
                "prend delta 3 égal à cette même droite O O prime, et "
                "delta 4, formant un angle bêta sur deux. En composant "
                "tout, delta 3 et delta 2 coïncident : leur composée "
                "s'annule, et il ne reste que s indice delta 4 rond s "
                "indice delta 1, deux symétries d'axes passant "
                "respectivement par O prime et par O. Si ces deux droites "
                "sont sécantes, on retombe sur le théorème précédent : une "
                "rotation d'angle double de l'angle entre elles, soit "
                "exactement alpha plus bêta. Si elles sont parallèles, "
                "c'est-à-dire quand alpha plus bêta est un multiple de 2 "
                "pi, on obtient une translation."
            )
        ) as tracker:
            self.play(FadeIn(etape1))
            self.play(Write(etape2))
            self.play(Write(etape3))
            self.play(Write(etape4))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(demo))

        # --- Cas particuliers ------------------------------------------------
        cas_part = theorem_box(
            VGroup(
                Text("Cas particuliers", font_size=23, weight="BOLD"),
                MathTex(r"O=O' \implies r'\circ r = r_{(O,\,\alpha+\beta)}", font_size=24),
                MathTex(r"\alpha=\beta=\pi/2,\ O\neq O' \implies r'\circ r = s_\Omega \ (\text{sym\'etrie centrale})", font_size=22),
                MathTex(r"\beta=-\alpha \implies r'\circ r \text{ est une translation}", font_size=24),
            ).arrange(DOWN, buff=0.2)
        )
        cas_part.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Trois cas particuliers à retenir. Si les deux rotations "
                "ont le même centre, la composée est simplement la "
                "rotation de ce centre commun, d'angle la somme des "
                "angles. Si l'on compose deux quarts de tour directs de "
                "centres distincts, la somme des angles vaut pi, et l'on "
                "obtient une symétrie centrale. Enfin, si les angles sont "
                "opposés, leur somme est nulle, et la composée est une "
                "translation."
            )
        ) as tracker:
            self.play(FadeIn(cas_part))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(cas_part))

        # --- Exemple résolu 5 : carré ABCD -----------------------------------
        a_pt = LEFT * 1.5 + DOWN * 1.2
        b_pt = RIGHT * 0.5 + DOWN * 1.2
        c_pt = RIGHT * 0.5 + UP * 0.8
        d_pt = LEFT * 1.5 + UP * 0.8
        carre = Polygon(a_pt, b_pt, c_pt, d_pt, color=WHITE, stroke_width=2)
        pt_a = _dot_label(a_pt, "A", label_dir=DOWN)
        pt_b = _dot_label(b_pt, "B", label_dir=DOWN)
        pt_c = _dot_label(c_pt, "C", label_dir=UP)
        pt_d = _dot_label(d_pt, "D", label_dir=UP)
        figure = VGroup(carre, pt_a, pt_b, pt_c, pt_d)
        figure.scale(0.9)
        figure.to_edge(RIGHT, buff=1.2)

        enonce = MathTex(r"ABCD \text{ carr\'e direct}, \quad r_A=r_{(A,\pi/2)}, \quad r_B=r_{(B,\pi/2)}", font_size=24)
        calc1 = MathTex(r"\alpha+\beta = \pi \implies r_B\circ r_A \text{ est une sym\'etrie centrale } s_\Omega", font_size=23)
        calc2 = MathTex(r"r_A(A)=A \implies (r_B\circ r_A)(A) = r_B(A)", font_size=23)
        calc3 = MathTex(r"\Omega = \text{milieu de } [A,\ r_B(A)]", font_size=25, color=YELLOW)
        exemple = example_box(VGroup(enonce, calc1, calc2, calc3).arrange(DOWN, buff=0.22))
        exemple.scale(0.85)
        exemple.next_to(titre, DOWN, buff=0.35)
        exemple.to_edge(LEFT, buff=0.4)

        with self.voiceover(
            text=(
                "Exemple : soit ABCD un carré direct, et considérons les "
                "deux quarts de tour directs r indice A, de centre A, et r "
                "indice B, de centre B. Leur somme d'angles vaut pi, donc "
                "d'après le cas particulier précédent, la composée r "
                "indice B rond r indice A est une symétrie centrale, de "
                "centre Oméga à déterminer. Astuce : comme A est fixe par "
                "r indice A, l'image de A par la composée est simplement r "
                "indice B de A. Or, pour une symétrie centrale, le centre "
                "est le milieu du segment reliant un point à son image : "
                "Oméga est donc le milieu du segment A, r indice B de A."
            )
        ) as tracker:
            self.play(Create(figure))
            self.play(FadeIn(exemple))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(exemple), FadeOut(figure))

        # --- À retenir --------------------------------------------------------
        retenir = theorem_box(
            VGroup(
                MathTex(r"r'\circ r = r_{(\Omega,\,\alpha+\beta)} \quad \text{si } \alpha+\beta\not\equiv 0\,[2\pi]", font_size=25),
                MathTex(r"r'\circ r = \text{translation} \quad \text{si } \alpha+\beta\equiv 0\,[2\pi]", font_size=25),
            ).arrange(DOWN, buff=0.25)
        )
        retenir.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "À retenir : la composée de deux rotations est déterminée "
                "par la somme de leurs angles — rotation si cette somme "
                "est non nulle modulo deux pi, translation sinon — le "
                "centre, lui, devant être calculé dans le cas général."
            )
        ) as tracker:
            self.play(FadeIn(retenir))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(retenir), FadeOut(titre))
