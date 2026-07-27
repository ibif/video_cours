"""
scenes/Maths_VecteursEspace_09.py — Chapitre 16 « Vecteurs de l'espace »
(1ereC, Maths), scène 09.

§ Centre de gravité d'un tétraèdre : définition (isobarycentre, GA+GB+GC+
GD=0), théorème de position (AG = 3/4 AA′, A′ centre de gravité de la face
opposée, avec démonstration), les 4 médianes concourantes en G aux 3/4,
propriété des coordonnées (moyenne des 4 sommets). Illustré sur le
tétraèdre ABCD, A′ (centre de gravité de BCD) et G.
Source : 1ereC/Maths.pdf, pages 189-199.
"""

from manim import (
    DOWN,
    LEFT,
    RIGHT,
    UP,
    WHITE,
    YELLOW,
    DashedLine,
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
from shapes.boxes import definition_box, property_box, scene_title, theorem_box


def _tetra_points(names, side=3.2, back=0.9, height=2.6, origin=None):
    if origin is None:
        origin = DOWN * 1.0
    n0, n1, n2, n3 = names
    p0 = origin + LEFT * side / 2
    p1 = origin + RIGHT * side / 2
    p2 = origin + UP * back + RIGHT * back * 0.7
    p3 = (p0 + p1) / 2 + UP * height + RIGHT * 0.25
    return {n0: p0, n1: p1, n2: p2, n3: p3}


def _tetra_group(pts, names, color=WHITE, label_color=YELLOW, label_font_size=26, label_dirs=None):
    n0, n1, n2, n3 = names
    p = pts
    hidden = [(n0, n2), (n1, n2), (n2, n3)]
    visible = [(n0, n1), (n0, n3), (n1, n3)]
    lines = VGroup()
    for u, v in visible:
        lines.add(Line(p[u], p[v], color=color, stroke_width=2.5))
    for u, v in hidden:
        lines.add(DashedLine(p[u], p[v], color=color, stroke_width=2, dash_length=0.09))
    if label_dirs is None:
        label_dirs = {n0: DOWN + LEFT, n1: DOWN + RIGHT, n2: UP + RIGHT, n3: UP}
    labels = VGroup()
    for name, point in p.items():
        dot = Dot(point, radius=0.045, color=label_color)
        lab = MathTex(name, font_size=label_font_size, color=label_color)
        lab.next_to(dot, label_dirs.get(name, UP), buff=0.08)
        labels.add(dot, lab)
    return VGroup(lines, labels)


class CentreGraviteTetraedre(NotionScene):
    def construct(self):
        titre = scene_title("Centre de gravité d'un tétraèdre")
        titre.scale(0.55)
        titre.to_edge(UP)

        pts = _tetra_points(("B", "C", "D", "A"))
        tetra = _tetra_group(pts, ("B", "C", "D", "A"))
        figure = VGroup(tetra)
        figure.scale(0.8)
        figure.next_to(titre, DOWN, buff=0.35)

        # --- Énoncé : définition ----------------------------------------------------
        definition = definition_box(
            VGroup(
                Text("Centre de gravité (isobarycentre) d'un tétraèdre", font_size=22, weight="BOLD"),
                MathTex(
                    r"G \ \text{centre de gravité de} \ ABCD \ \iff\ \overrightarrow{GA}+\overrightarrow{GB}+\overrightarrow{GC}+\overrightarrow{GD} = \vec 0",
                    font_size=23,
                ),
            ).arrange(DOWN, buff=0.2),
        )
        definition.next_to(titre, DOWN, buff=0.35)

        with self.voiceover(
            text=(
                "Le centre de gravité, ou isobarycentre, d'un tétraèdre "
                "A-B-C-D est l'unique point G tel que la somme des vecteurs "
                "G-A, G-B, G-C, G-D soit le vecteur nul. C'est exactement "
                "la généralisation à quatre points de la caractérisation "
                "du milieu vue à la scène précédente."
            )
        ) as tracker:
            self.play(Write(titre))
            self.play(FadeIn(figure))
            self.play(FadeIn(definition))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(definition))

        # --- Raisonnement : théorème de position + démonstration --------------------
        theo = theorem_box(
            VGroup(
                Text("Position du centre de gravité", font_size=22, weight="BOLD"),
                MathTex(
                    r"A' \ \text{centre de gravité de} \ BCD \ \text{(face opposée à } A \text{)} \ \Longrightarrow\ \overrightarrow{AG} = \tfrac34 \overrightarrow{AA'}",
                    font_size=22,
                ),
            ).arrange(DOWN, buff=0.2),
        )
        theo.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Voici le théorème de position : si A prime est le centre "
                "de gravité du triangle B-C-D, la face opposée à A, alors "
                "le vecteur A-G est égal aux trois quarts du vecteur A-A "
                "prime. Autrement dit, G se trouve sur le segment reliant "
                "A à A prime, appelé médiane, aux trois quarts en partant "
                "de A."
            )
        ) as tracker:
            self.play(FadeOut(figure))
            self.play(FadeIn(theo))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(theo))

        demo = VGroup(
            Text("Démonstration", font_size=21, weight="BOLD"),
            MathTex(r"A' \ \text{centre de gravité de} \ BCD \ : \quad \overrightarrow{A'B}+\overrightarrow{A'C}+\overrightarrow{A'D} = \vec 0", font_size=20),
            MathTex(r"\vec 0 = \overrightarrow{GA}+\overrightarrow{GB}+\overrightarrow{GC}+\overrightarrow{GD} = \overrightarrow{GA} + \sum(\overrightarrow{GA'}+\overrightarrow{A'B}) + \dots", font_size=19),
            MathTex(r"= \overrightarrow{GA} + 3\overrightarrow{GA'} + \underbrace{(\overrightarrow{A'B}+\overrightarrow{A'C}+\overrightarrow{A'D})}_{=\,\vec 0} = \overrightarrow{GA} + 3\overrightarrow{GA'}", font_size=20),
            MathTex(r"\Longrightarrow\ \overrightarrow{GA} = -3\overrightarrow{GA'} = 3\overrightarrow{A'G} \ \Longrightarrow\ \overrightarrow{AG} = 3\overrightarrow{GA'}", font_size=20),
            MathTex(r"\overrightarrow{AA'} = \overrightarrow{AG}+\overrightarrow{GA'} \ \Longrightarrow\ \overrightarrow{AG} = 3(\overrightarrow{AA'}-\overrightarrow{AG}) \ \Longrightarrow\ 4\overrightarrow{AG}=3\overrightarrow{AA'}", font_size=19),
            MathTex(r"\Longrightarrow\ \overrightarrow{AG} = \tfrac34 \overrightarrow{AA'}", font_size=24, color=YELLOW),
        ).arrange(DOWN, buff=0.14)
        demo.next_to(titre, DOWN, buff=0.28)

        with self.voiceover(
            text=(
                "Voici la démonstration. Puisque A prime est le centre de "
                "gravité du triangle B-C-D, on a A-prime-B plus "
                "A-prime-C plus A-prime-D égal au vecteur nul. Repartons de "
                "la définition de G : G-A plus G-B plus G-C plus G-D égal "
                "au vecteur nul. En décomposant G-B, G-C, G-D via A prime, "
                "on obtient G-A plus trois fois G-A prime, plus la somme "
                "A-prime-B plus A-prime-C plus A-prime-D, qui vaut zéro. Il "
                "reste donc G-A plus trois G-A prime égal zéro, "
                "c'est-à-dire A-G égal trois fois G-A prime. En "
                "remplaçant G-A prime par A-A prime moins A-G, via "
                "Chasles, on obtient A-G égal trois A-A prime moins trois "
                "A-G, soit quatre A-G égal trois A-A prime, et finalement "
                "A-G égal les trois quarts de A-A prime."
            )
        ) as tracker:
            self.play(Write(demo[0]))
            self.play(Write(demo[1]))
            self.play(Write(demo[2]))
            self.play(Write(demo[3]))
            self.play(Write(demo[4]))
            self.play(Write(demo[5]))
            self.play(Write(demo[6]))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(demo))

        # --- Exemple / illustration : figure avec A', G -----------------------------
        Aprime = (pts["B"] + pts["C"] + pts["D"]) / 3
        G = pts["A"] + (Aprime - pts["A"]) * 0.75
        figure2 = VGroup(tetra.copy())
        figure2.scale(0.8)
        figure2.next_to(titre, DOWN, buff=0.35)
        scale_factor = 0.8
        center = figure2.get_center()
        Aprime_s = (Aprime - tetra.get_center()) * scale_factor + center
        G_s = (G - tetra.get_center()) * scale_factor + center
        A_s = (pts["A"] - tetra.get_center()) * scale_factor + center

        mediane = Line(A_s, Aprime_s, color="#1E5FA8", stroke_width=4)
        pt_aprime = VGroup(Dot(Aprime_s, radius=0.05, color="#DE7C1F"), MathTex("A'", font_size=24, color="#DE7C1F").next_to(Aprime_s, DOWN, buff=0.1))
        pt_g = VGroup(Dot(G_s, radius=0.06, color=YELLOW), MathTex("G", font_size=26, color=YELLOW).next_to(G_s, RIGHT, buff=0.1))

        with self.voiceover(
            text=(
                "Voici la figure : A prime, le centre de gravité de la "
                "face B-C-D, et G, situé sur la médiane A, A prime, aux "
                "trois quarts en partant de A. Par symétrie du résultat, "
                "les quatre médianes du tétraèdre — reliant chaque sommet "
                "au centre de gravité de la face opposée — sont "
                "concourantes en ce même point G, chacune aux trois quarts "
                "à partir de son sommet."
            )
        ) as tracker:
            self.play(FadeIn(figure2))
            self.play(FadeIn(mediane), FadeIn(pt_aprime), FadeIn(pt_g))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(figure2), FadeOut(mediane), FadeOut(pt_aprime), FadeOut(pt_g))

        # --- À retenir : coordonnées du centre de gravité -----------------------------
        coord = property_box(
            VGroup(
                Text("Coordonnées du centre de gravité", font_size=22, weight="BOLD"),
                MathTex(
                    r"G\left(\dfrac{x_A+x_B+x_C+x_D}{4} \, ; \, \dfrac{y_A+y_B+y_C+y_D}{4} \, ; \, \dfrac{z_A+z_B+z_C+z_D}{4}\right)",
                    font_size=21,
                ),
            ).arrange(DOWN, buff=0.2),
        )
        coord.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Enfin, en coordonnées, le centre de gravité de A-B-C-D est "
                "simplement la moyenne des quatre sommets, composante par "
                "composante : la moyenne des abscisses, la moyenne des "
                "ordonnées, la moyenne des cotes. C'est la généralisation "
                "directe de la formule du milieu vue à la scène "
                "précédente."
            )
        ) as tracker:
            self.play(FadeIn(coord))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(coord), FadeOut(titre))
