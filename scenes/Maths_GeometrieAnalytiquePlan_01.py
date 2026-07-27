"""
scenes/Maths_GeometrieAnalytiquePlan_01.py — Chapitre 14 « Géométrie
analytique du plan » (1ereC, Maths), scène 01.

§ Repère du plan (O;i,j), repère orthogonal, repère orthonormé.
Coordonnées d'un point et d'un vecteur. Propriétés valables dans tout
repère : coordonnées de AB⃗ (xB-xA;yB-yA), égalité de deux vecteurs, somme
de deux vecteurs, produit d'un vecteur par un réel, coordonnées du milieu
d'un segment. Exemple résolu : A(2;3), B(5;1), C(-1;7) — calcul de AB⃗, AC⃗
et du milieu de [AB].
Source : 1ereC/Maths.pdf, chapitre 14, pages 165-166.
"""

import textwrap

from manim import (
    DOWN,
    LEFT,
    RIGHT,
    UP,
    WHITE,
    YELLOW,
    Arrow,
    Axes,
    Create,
    Dot,
    FadeIn,
    FadeOut,
    MathTex,
    Text,
    VGroup,
    Write,
)

from shapes.base_scene import NotionScene
from shapes.boxes import definition_box, example_box, property_box, scene_title, warning_box


def _wrap(text: str, width: int = 56) -> str:
    return "\n".join(textwrap.fill(line, width=width) for line in text.split("\n"))


def _dot_label(point, label, color=WHITE, label_dir=UP, font_size=28, dot_color=YELLOW):
    d = Dot(point, color=dot_color, radius=0.07)
    t = MathTex(label, font_size=font_size, color=color)
    t.next_to(d, label_dir, buff=0.12)
    return VGroup(d, t)


class RepereCoordonneesVecteursPoints(NotionScene):
    def construct(self):
        titre = scene_title("Repère du plan — Coordonnées de points et vecteurs")
        titre.scale(0.42)
        titre.to_edge(UP)

        # --- Énoncé : définition du repère --------------------------------------
        axes = Axes(
            x_range=[-1, 4, 1],
            y_range=[-1, 3, 1],
            x_length=4.5,
            y_length=3.2,
            axis_config={"include_tip": True, "color": WHITE},
        )
        axes.move_to(LEFT * 3.3 + DOWN * 0.7)
        i_arrow = Arrow(axes.c2p(0, 0), axes.c2p(1, 0), buff=0, color=YELLOW, stroke_width=4)
        j_arrow = Arrow(axes.c2p(0, 0), axes.c2p(0, 1), buff=0, color="#288073", stroke_width=4)
        i_label = MathTex(r"\vec{i}", font_size=26, color=YELLOW).next_to(i_arrow, DOWN, buff=0.1)
        j_label = MathTex(r"\vec{j}", font_size=26, color="#288073").next_to(j_arrow, LEFT, buff=0.1)
        o_label = MathTex("O", font_size=26).next_to(axes.c2p(0, 0), DOWN + LEFT, buff=0.12)
        schema = VGroup(axes, i_arrow, j_arrow, i_label, j_label, o_label)

        texte_def = Text(
            _wrap(
                "Un repère (O;i,j) est la donnée d'un point O (l'origine) et "
                "de deux vecteurs non colinéaires i et j. Il est orthogonal "
                "si (i,j) sont perpendiculaires, orthonormé si de plus "
                "‖i‖=‖j‖=1.",
                width=42,
            ),
            font_size=22,
        )
        texte_def.next_to(titre, DOWN, buff=0.5).shift(RIGHT * 2.8)

        with self.voiceover(
            text=(
                "Pour repérer un point ou un vecteur dans le plan, on se "
                "donne un repère, noté O, i, j : un point O appelé origine, "
                "et deux vecteurs i et j non colinéaires. Le repère est dit "
                "orthogonal si les vecteurs i et j sont perpendiculaires, et "
                "orthonormé s'il est de plus orthogonal avec des vecteurs de "
                "norme un. C'est dans ce cadre que l'on va définir les "
                "coordonnées d'un point et d'un vecteur."
            )
        ) as tracker:
            self.play(Write(titre))
            self.play(Create(schema))
            self.play(FadeIn(texte_def))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(schema), FadeOut(texte_def))

        # --- Coordonnées d'un point et d'un vecteur -----------------------------
        def_coord = definition_box(
            VGroup(
                Text("Coordonnées dans (O;i,j)", font_size=24, weight="BOLD"),
                MathTex(
                    r"M(x\,;\,y) \iff \overrightarrow{OM} = x\,\vec{i} + y\,\vec{j}",
                    font_size=28,
                ),
                Text(
                    _wrap("x est l'abscisse, y est l'ordonnée de M (ou du vecteur).", width=46),
                    font_size=22,
                ),
            ).arrange(DOWN, buff=0.25),
        )
        def_coord.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Un point M a pour coordonnées x et y dans le repère O, i, "
                "j lorsque le vecteur O-M s'écrit x fois i plus y fois j. Le "
                "nombre x est appelé l'abscisse de M, et y son ordonnée. On "
                "définit de la même façon les coordonnées d'un vecteur "
                "quelconque."
            )
        ) as tracker:
            self.play(FadeIn(def_coord))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(def_coord))

        # --- Raisonnement : propriétés en repère quelconque ---------------------
        proprietes = property_box(
            VGroup(
                MathTex(
                    r"A(x_A;y_A),\ B(x_B;y_B) \ \Rightarrow\ \overrightarrow{AB}(x_B-x_A\,;\,y_B-y_A)",
                    font_size=26,
                ),
                MathTex(
                    r"\vec{u}(x;y) = \vec{u'}(x';y') \iff x=x' \text{ et } y=y'",
                    font_size=26,
                ),
                MathTex(
                    r"\vec{u}(x;y) + \vec{u'}(x';y') = (x+x'\,;\,y+y')"
                    r"\qquad k\,\vec{u}(x;y) = (kx\,;\,ky)",
                    font_size=25,
                ),
                MathTex(
                    r"I \text{ milieu de } [AB] \ \Rightarrow\ "
                    r"I\left(\dfrac{x_A+x_B}{2}\,;\,\dfrac{y_A+y_B}{2}\right)",
                    font_size=26,
                ),
            ).arrange(DOWN, buff=0.28),
            box_width=11.3,
        )
        proprietes.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Ces propriétés sont valables dans TOUT repère, pas "
                "seulement orthonormé. Si A et B ont pour coordonnées "
                "x-A, y-A et x-B, y-B, alors le vecteur A-B a pour "
                "coordonnées x-B moins x-A, et y-B moins y-A. Deux vecteurs "
                "sont égaux si et seulement si ils ont les mêmes "
                "coordonnées. La somme de deux vecteurs s'obtient en "
                "additionnant leurs coordonnées, et le produit d'un vecteur "
                "par un réel k en multipliant chaque coordonnée par k. "
                "Enfin, le milieu I du segment A-B a pour coordonnées la "
                "demi-somme des coordonnées de A et de B."
            )
        ) as tracker:
            self.play(FadeIn(proprietes))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(proprietes))

        # --- Exemple traité -------------------------------------------------------
        axes2 = Axes(
            x_range=[-2, 6, 1],
            y_range=[-1, 8, 1],
            x_length=4.6,
            y_length=4.2,
            axis_config={"include_tip": True, "color": WHITE, "font_size": 16},
        )
        axes2.move_to(RIGHT * 3.3 + DOWN * 0.3)
        pa = _dot_label(axes2.c2p(2, 3), "A")
        pb = _dot_label(axes2.c2p(5, 1), "B", label_dir=DOWN)
        pc = _dot_label(axes2.c2p(-1, 7), "C")
        figure = VGroup(axes2, pa, pb, pc)

        calculs = MathTex(
            r"A(2;3),\ B(5;1),\ C(-1;7)"
            r"\\[6pt]"
            r"\overrightarrow{AB}(5-2\,;\,1-3) = (3\,;\,-2)"
            r"\\[4pt]"
            r"\overrightarrow{AC}(-1-2\,;\,7-3) = (-3\,;\,4)"
            r"\\[4pt]"
            r"I_{[AB]}\left(\dfrac{2+5}{2}\,;\,\dfrac{3+1}{2}\right) = \left(\dfrac{7}{2}\,;\,2\right)",
            font_size=25,
        )
        calculs.to_edge(LEFT, buff=0.6).shift(DOWN * 0.2)
        exemple = example_box(calculs, box_width=6.0)
        exemple.move_to(LEFT * 3.3 + DOWN * 0.3)

        with self.voiceover(
            text=(
                "Prenons un exemple : A de coordonnées 2 et 3, B de "
                "coordonnées 5 et 1, C de coordonnées moins un et 7. Le "
                "vecteur A-B a pour coordonnées 5 moins 2, soit 3, et 1 "
                "moins 3, soit moins 2. Le vecteur A-C a pour coordonnées "
                "moins 3 et 4. Enfin, le milieu du segment A-B a pour "
                "coordonnées sept demis et 2."
            )
        ) as tracker:
            self.play(Create(figure))
            self.play(FadeIn(exemple))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(figure), FadeOut(exemple))

        # --- À retenir --------------------------------------------------------
        retenir = definition_box(
            VGroup(
                MathTex(
                    r"\overrightarrow{AB}(x_B-x_A\,;\,y_B-y_A)",
                    font_size=27,
                ),
                MathTex(
                    r"I_{[AB]}\left(\dfrac{x_A+x_B}{2}\,;\,\dfrac{y_A+y_B}{2}\right)",
                    font_size=27,
                ),
                Text("Ces formules sont valables dans tout repère.", font_size=22),
            ).arrange(DOWN, buff=0.28),
        )
        retenir.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "À retenir : les coordonnées du vecteur A-B s'obtiennent "
                "toujours en soustrayant celles de A à celles de B, et le "
                "milieu d'un segment en faisant la demi-somme des "
                "coordonnées de ses extrémités — et cela, dans tout repère, "
                "sans condition d'orthonormalité."
            )
        ) as tracker:
            self.play(FadeIn(retenir))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(retenir))

        # --- Piège à éviter -----------------------------------------------------
        piege = warning_box(
            Text(
                _wrap(
                    "Ne pas confondre les coordonnées d'un POINT et celles "
                    "d'un VECTEUR : un vecteur AB⃗ garde les mêmes "
                    "coordonnées où qu'on le déplace dans le plan, alors "
                    "qu'un point a une position fixe. Attention aussi à "
                    "l'ordre B moins A, et non A moins B.",
                    width=48,
                ),
                font_size=22,
            ),
        )
        piege.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Piège classique : ne confondez pas les coordonnées d'un "
                "point, qui repèrent une position fixe, et celles d'un "
                "vecteur, qui ne dépendent pas de l'endroit où on le "
                "représente. Et surtout, respectez bien l'ordre de la "
                "soustraction : pour le vecteur A-B, on calcule toujours "
                "les coordonnées de l'arrivée B moins celles du départ A, "
                "jamais l'inverse."
            )
        ) as tracker:
            self.play(FadeIn(piege))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(piege), FadeOut(titre))
