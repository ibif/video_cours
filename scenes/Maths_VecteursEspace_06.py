"""
scenes/Maths_VecteursEspace_06.py — Chapitre 16 « Vecteurs de l'espace »
(1ereC, Maths), scène 06.

§ Repère de l'espace (O;i,j,k), coordonnées d'un point (abscisse, ordonnée,
cote), axes de coordonnées. Propriété des coordonnées d'un vecteur AB (avec
démonstration). Exemple résolu 4 : tétraèdre ABCD, repère (A;AB,AC,AD),
calcul des coordonnées de I (milieu [BC]), J (milieu [AD]) et du vecteur IJ.
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
from shapes.boxes import corrige_box, definition_box, exercise_box, property_box, scene_title


def _tetra_points(names, side=2.8, back=0.85, height=2.3, origin=None):
    if origin is None:
        origin = DOWN * 0.85
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


class RepereCoordonnees(NotionScene):
    def construct(self):
        titre = scene_title("Repère de l'espace, coordonnées")
        titre.scale(0.55)
        titre.to_edge(UP)
        self.play(Write(titre))

        # --- Énoncé : définitions ----------------------------------------------------
        def_repere = definition_box(
            VGroup(
                Text("Repère de l'espace", font_size=23, weight="BOLD"),
                Text(
                    "(O;i,j,k) : un point O (l'origine) et une base (i,j,k). Pour tout point M,\n"
                    "l'unique triplet (x;y;z) tel que OM = x·i + y·j + z·k sont les coordonnées\n"
                    "de M : x l'abscisse, y l'ordonnée, z la cote.",
                    font_size=19,
                ),
                Text("Les axes (Ox), (Oy), (Oz) sont les droites définies par O et chaque vecteur de base.", font_size=18),
            ).arrange(DOWN, buff=0.2),
        )
        def_repere.next_to(titre, DOWN, buff=0.35)

        with self.voiceover(
            text=(
                "Un repère de l'espace, noté O, i, j, k, est la donnée d'un "
                "point O, l'origine, et d'une base i, j, k. Pour tout point "
                "M, le théorème de la scène précédente garantit l'existence "
                "d'un unique triplet x, y, z tel que O-M soit égal à x fois "
                "i plus y fois j plus z fois k. Ce triplet donne les "
                "coordonnées de M : x l'abscisse, y l'ordonnée, z la cote. "
                "Les axes O-x, O-y, O-z sont les droites définies par O et "
                "chacun des trois vecteurs de base."
            )
        ) as tracker:
            self.play(FadeIn(def_repere))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(def_repere))

        # --- Raisonnement : propriété des coordonnées d'un vecteur ------------------
        prop = property_box(
            VGroup(
                Text("Coordonnées du vecteur AB", font_size=22, weight="BOLD"),
                MathTex(
                    r"A(x_A;y_A;z_A), \ B(x_B;y_B;z_B) \ \Longrightarrow\ \overrightarrow{AB}\,(x_B-x_A \, ; \, y_B-y_A \, ; \, z_B - z_A)",
                    font_size=23,
                ),
            ).arrange(DOWN, buff=0.2),
        )
        prop.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Voici une propriété très utilisée en pratique : si A a "
                "pour coordonnées x A, y A, z A, et B pour coordonnées x B, "
                "y B, z B, alors le vecteur A-B a pour coordonnées x B "
                "moins x A, y B moins y A, z B moins z A."
            )
        ) as tracker:
            self.play(FadeIn(prop))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(prop))

        demo = VGroup(
            Text("Démonstration", font_size=21, weight="BOLD"),
            MathTex(
                r"\overrightarrow{AB} = \overrightarrow{AO} + \overrightarrow{OB} = \overrightarrow{OB} - \overrightarrow{OA}",
                font_size=23,
            ),
            MathTex(
                r"= (x_B i + y_B j + z_B k) - (x_A i + y_A j + z_A k)",
                font_size=22,
            ),
            MathTex(
                r"= (x_B - x_A)\,i + (y_B-y_A)\,j + (z_B-z_A)\,k",
                font_size=23,
                color=YELLOW,
            ),
            Text("Par unicité de la décomposition (scène 5), ce sont bien les coordonnées de AB.", font_size=19),
        ).arrange(DOWN, buff=0.2)
        demo.next_to(titre, DOWN, buff=0.35)

        with self.voiceover(
            text=(
                "La démonstration tient en une ligne de calcul : A-B égale "
                "A-O plus O-B, par Chasles, c'est-à-dire O-B moins O-A. En "
                "remplaçant chaque vecteur par sa décomposition dans la "
                "base i, j, k, on regroupe terme à terme et on obtient "
                "exactement x B moins x A, fois i, plus y B moins y A, fois "
                "j, plus z B moins z A, fois k. Par unicité de la "
                "décomposition, vue à la scène précédente, ce sont bien là "
                "les coordonnées du vecteur A-B."
            )
        ) as tracker:
            self.play(Write(demo[0]))
            self.play(Write(demo[1]))
            self.play(Write(demo[2]))
            self.play(Write(demo[3]))
            self.play(Write(demo[4]))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(demo))

        # --- Exemple résolu 4 -----------------------------------------------------
        pts = _tetra_points(("B", "C", "D", "A"))
        tetra = _tetra_group(pts, ("B", "C", "D", "A"))
        figure = VGroup(tetra)
        figure.scale(0.78)
        figure.next_to(titre, DOWN, buff=0.3)

        enonce = exercise_box(
            VGroup(
                Text("Exemple résolu 4", font_size=22, weight="BOLD"),
                MathTex(
                    r"ABCD \ \text{tétraèdre, repère } (A; \overrightarrow{AB},\overrightarrow{AC},\overrightarrow{AD}) : \ A(0;0;0), B(1;0;0), C(0;1;0), D(0;0;1).",
                    font_size=18,
                ),
                MathTex(
                    r"I \ \text{milieu de } [BC], \ J \ \text{milieu de } [AD]. \ \text{Calculer les coordonnées de } I, J \ \text{et de } \overrightarrow{IJ}.",
                    font_size=18,
                ),
            ).arrange(DOWN, buff=0.2),
        )
        enonce.next_to(titre, DOWN, buff=0.35)

        with self.voiceover(
            text=(
                "Exemple résolu. A-B-C-D est un tétraèdre, muni du repère "
                "naturel A, A-B, A-C, A-D : dans ce repère, A a pour "
                "coordonnées zéro, zéro, zéro, B un, zéro, zéro, C zéro, "
                "un, zéro, et D zéro, zéro, un. I est le milieu de B-C, J "
                "le milieu de A-D. On veut les coordonnées de I, de J, et "
                "du vecteur I-J."
            )
        ) as tracker:
            self.play(FadeIn(enonce))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(enonce))
        self.play(FadeIn(figure))

        I = (pts["B"] + pts["C"]) / 2
        J = (pts["A"] + pts["D"]) / 2
        pt_i = VGroup(Dot(I, radius=0.05, color="#DE7C1F"), MathTex("I", font_size=24, color="#DE7C1F").next_to(I, RIGHT, buff=0.1))
        pt_j = VGroup(Dot(J, radius=0.05, color="#DE7C1F"), MathTex("J", font_size=24, color="#DE7C1F").next_to(J, LEFT, buff=0.1))
        pt_i.scale(0.78, about_point=figure.get_center())
        pt_j.scale(0.78, about_point=figure.get_center())
        seg_ij = Line(I, J, color="#288073", stroke_width=4.5).scale(0.78, about_point=figure.get_center())

        with self.voiceover(text="Plaçons I et J sur la figure, ainsi que le segment I-J.") as tracker:
            self.play(FadeIn(pt_i), FadeIn(pt_j), FadeIn(seg_ij))
            self.wait(tracker.get_remaining_duration())

        calc = VGroup(
            MathTex(r"\overrightarrow{AI} = \tfrac{1}{2}\big(\overrightarrow{AB}+\overrightarrow{AC}\big) \ \Longrightarrow\ I\big(\tfrac12; \tfrac12; 0\big)", font_size=23),
            MathTex(r"\overrightarrow{AJ} = \tfrac{1}{2}\overrightarrow{AD} \ \Longrightarrow\ J\big(0; 0; \tfrac12\big)", font_size=23),
            MathTex(r"\overrightarrow{IJ}\,(x_J - x_I \, ; \, y_J-y_I \, ; \, z_J-z_I) = \big({-\tfrac12} \, ; \, {-\tfrac12} \, ; \, \tfrac12\big)", font_size=22, color=YELLOW),
        ).arrange(DOWN, buff=0.26)
        calc.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Le vecteur A-I vaut la moyenne de A-B et A-C, ce qui donne "
                "I de coordonnées un demi, un demi, zéro. Le vecteur A-J "
                "vaut la moitié de A-D, ce qui donne J de coordonnées zéro, "
                "zéro, un demi. En appliquant la propriété des coordonnées "
                "d'un vecteur, I-J a pour coordonnées x de J moins x de I, "
                "y de J moins y de I, z de J moins z de I, c'est-à-dire "
                "moins un demi, moins un demi, un demi."
            )
        ) as tracker:
            self.play(FadeOut(figure), FadeOut(pt_i), FadeOut(pt_j), FadeOut(seg_ij))
            self.play(Write(calc[0]))
            self.play(Write(calc[1]))
            self.play(Write(calc[2]))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(calc))

        # --- À retenir -----------------------------------------------------------
        retenir = corrige_box(
            VGroup(
                MathTex(r"I\big(\tfrac12;\tfrac12;0\big), \ J\big(0;0;\tfrac12\big), \ \overrightarrow{IJ}\big({-\tfrac12};{-\tfrac12};\tfrac12\big)", font_size=23),
                Text(
                    "Méthode : calculer d'abord les coordonnées des points via les vecteurs\n"
                    "position dans le repère, puis appliquer la formule des coordonnées de AB.",
                    font_size=19,
                ),
            ).arrange(DOWN, buff=0.22),
        )
        retenir.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Retenons la méthode générale : dans un repère naturel d'un "
                "solide, comme ici A, A-B, A-C, A-D pour un tétraèdre, on "
                "calcule d'abord les coordonnées des points par des "
                "combinaisons de vecteurs, puis on applique systématiquement "
                "la formule des coordonnées d'un vecteur A-B pour obtenir "
                "les coordonnées de n'importe quel segment."
            )
        ) as tracker:
            self.play(FadeIn(retenir))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(retenir), FadeOut(titre))
