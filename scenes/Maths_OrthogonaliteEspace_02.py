"""
scenes/Maths_OrthogonaliteEspace_02.py — Chapitre 10 « Orthogonalité dans
l'espace » (1ereC, Maths), scène 02.

§ Exemple résolu 1 : cube ABCDEFGH, I milieu de [AF], J milieu de [CF].
Démontrer (CI) ⟂ (DG) via le triangle équilatéral ACF et le parallélisme,
puis (IJ) ⟂ (BD) via la droite des milieux et les diagonales du carré de
base.
Source : 1ereC/Maths.pdf, chapitre 10, pages 118-129.
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
from shapes.boxes import corrige_box, exercise_box, scene_title, warning_box


# --- Géométrie en perspective cavalière (2D projeté) ------------------------

def _cube_points(side=3.0, depth_x=1.05, depth_y=0.7, origin=None):
    if origin is None:
        origin = DOWN * 0.3
    depth = RIGHT * depth_x + UP * depth_y
    A = origin + LEFT * side / 2 + DOWN * side / 2
    B = A + RIGHT * side
    D = A + depth
    C = B + depth
    E = A + UP * side
    F = B + UP * side
    H = D + UP * side
    G = C + UP * side
    return {"A": A, "B": B, "C": C, "D": D, "E": E, "F": F, "G": G, "H": H}


def _cube_group(pts, color=WHITE, label_color=YELLOW, label_font_size=24):
    p = pts
    visible = [("A", "B"), ("B", "C"), ("A", "E"), ("B", "F"), ("C", "G"),
               ("E", "F"), ("F", "G"), ("G", "H"), ("E", "H")]
    hidden = [("A", "D"), ("D", "C"), ("D", "H")]
    lines = VGroup()
    for u, v in visible:
        lines.add(Line(p[u], p[v], color=color, stroke_width=2.5))
    for u, v in hidden:
        lines.add(DashedLine(p[u], p[v], color=color, stroke_width=2, dash_length=0.09))

    label_dirs = {"A": DOWN + LEFT, "B": DOWN + RIGHT, "C": RIGHT, "D": LEFT,
                  "E": UP + LEFT, "F": UP + RIGHT, "G": UP + RIGHT, "H": UP}
    labels = VGroup()
    for name, point in p.items():
        dot = Dot(point, radius=0.04, color=label_color)
        lab = MathTex(name, font_size=label_font_size, color=label_color)
        lab.next_to(dot, label_dirs.get(name, UP), buff=0.08)
        labels.add(dot, lab)
    return VGroup(lines, labels)


class ExempleDroitesOrthogonalesCube(NotionScene):
    def construct(self):
        titre = scene_title("Exemple résolu — droites orthogonales dans un cube")
        titre.scale(0.48)
        titre.to_edge(UP)

        pts = _cube_points()
        cube = _cube_group(pts)
        I = (pts["A"] + pts["F"]) / 2
        J = (pts["C"] + pts["F"]) / 2

        pt_i = VGroup(Dot(I, radius=0.05, color="#DE7C1F"), MathTex("I", font_size=24, color="#DE7C1F").next_to(I, LEFT, buff=0.1))
        pt_j = VGroup(Dot(J, radius=0.05, color="#DE7C1F"), MathTex("J", font_size=24, color="#DE7C1F").next_to(J, RIGHT, buff=0.1))
        figure = VGroup(cube, pt_i, pt_j)
        figure.scale(0.8)
        figure.next_to(titre, DOWN, buff=0.3)

        # --- Énoncé -----------------------------------------------------------
        enonce = exercise_box(
            VGroup(
                Text("ABCDEFGH un cube. I milieu de [AF], J milieu de [CF].", font_size=23),
                MathTex(r"\text{Démontrer que } (CI) \perp (DG) \ \text{ et } \ (IJ) \perp (BD).", font_size=25),
            ).arrange(DOWN, buff=0.2),
        )
        enonce.next_to(titre, DOWN, buff=0.35)

        with self.voiceover(
            text=(
                "Voici un exemple résolu. On considère un cube "
                "A-B-C-D-E-F-G-H. I est le milieu du segment A-F, et J le "
                "milieu du segment C-F. On veut démontrer que la droite "
                "C-I est orthogonale à la droite D-G, puis que la droite "
                "I-J est orthogonale à la droite B-D."
            )
        ) as tracker:
            self.play(Write(titre))
            self.play(FadeIn(enonce))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(enonce))
        self.play(FadeIn(figure))
        self.wait(0.5)

        # --- Raisonnement 1 : (CI) ⟂ (DG) ------------------------------------
        triangle_acf = VGroup(
            Line(pts["A"], pts["C"], color="#DE7C1F", stroke_width=4),
            Line(pts["C"], pts["F"], color="#DE7C1F", stroke_width=4),
            Line(pts["F"], pts["A"], color="#DE7C1F", stroke_width=4),
        )
        triangle_acf.scale(0.8, about_point=figure.get_center())

        etape1 = VGroup(
            MathTex(r"AC = CF = FA = a\sqrt{2} \quad \Longrightarrow\quad ACF \ \text{équilatéral}", font_size=25),
            MathTex(r"\Longrightarrow\ (CI) \ \text{médiane issue de } C = \text{hauteur} \ \Longrightarrow\ (CI) \perp (AF)", font_size=25),
            MathTex(r"(DG) \parallel (AF) \quad \big(\text{diagonales de deux faces opposées, translatées l'une de l'autre}\big)", font_size=20),
            MathTex(r"\Longrightarrow\ (CI) \perp (DG)", font_size=27, color=YELLOW),
        ).arrange(DOWN, buff=0.28)
        etape1.next_to(titre, DOWN, buff=0.35)

        with self.voiceover(
            text=(
                "Les trois faces du cube étant des carrés de côté a, les "
                "diagonales A-C, C-F et F-A sont toutes trois de longueur "
                "a racine de deux : le triangle A-C-F est donc équilatéral. "
                "Dans ce triangle, I est le milieu de A-F, donc la droite "
                "C-I est à la fois médiane et hauteur : elle est "
                "orthogonale à A-F. Or D-G est parallèle à A-F, car ce "
                "sont les diagonales de deux faces opposées du cube, "
                "translatées l'une de l'autre. Par transitivité de "
                "l'orthogonalité par parallélisme, on conclut que C-I est "
                "orthogonale à D-G."
            )
        ) as tracker:
            self.play(FadeIn(triangle_acf))
            self.play(Write(etape1[0]))
            self.play(Write(etape1[1]))
            self.play(Write(etape1[2]))
            self.play(Write(etape1[3]))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(etape1), FadeOut(triangle_acf))

        # --- Exemple traité : (IJ) ⟂ (BD) ------------------------------------
        seg_ij = Line(I, J, color="#288073", stroke_width=4).scale(0.8, about_point=figure.get_center())
        seg_bd = DashedLine(pts["B"], pts["D"], color="#1E5FA8", stroke_width=4).scale(0.8, about_point=figure.get_center())

        etape2 = VGroup(
            MathTex(r"I \text{ milieu de } [AF], \ J \text{ milieu de } [CF] \ \Longrightarrow\ (IJ) \ \text{droite des milieux de } ACF", font_size=22),
            MathTex(r"\Longrightarrow\ (IJ) \parallel (AC)", font_size=26),
            MathTex(r"ABCD \ \text{carré} \ \Longrightarrow\ (AC) \perp (BD) \quad \text{(diagonales d'un carré)}", font_size=24),
            MathTex(r"\Longrightarrow\ (IJ) \perp (BD)", font_size=27, color=YELLOW),
        ).arrange(DOWN, buff=0.26)
        etape2.next_to(titre, DOWN, buff=0.35)

        with self.voiceover(
            text=(
                "Passons à la deuxième orthogonalité. I est le milieu de "
                "A-F et J le milieu de C-F : la droite I-J est donc la "
                "droite des milieux du triangle A-C-F, ce qui la rend "
                "parallèle au troisième côté, A-C. Or A-B-C-D est un "
                "carré, et les diagonales d'un carré sont perpendiculaires : "
                "A-C est orthogonale à B-D. Comme I-J est parallèle à A-C, "
                "elle hérite de cette orthogonalité : I-J est orthogonale "
                "à B-D."
            )
        ) as tracker:
            self.play(FadeIn(seg_ij), FadeIn(seg_bd))
            self.play(Write(etape2[0]))
            self.play(Write(etape2[1]))
            self.play(Write(etape2[2]))
            self.play(Write(etape2[3]))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(etape2), FadeOut(seg_ij), FadeOut(seg_bd), FadeOut(figure))

        # --- À retenir ---------------------------------------------------------
        retenir = corrige_box(
            VGroup(
                MathTex(r"(CI) \perp (DG) \quad \text{et} \quad (IJ) \perp (BD)", font_size=27),
                Text(
                    "Méthode : repérer un triangle équilatéral (médiane = hauteur), une droite des\n"
                    "milieux, ou les diagonales d'un carré, puis transporter l'orthogonalité par parallélisme.",
                    font_size=21,
                ),
            ).arrange(DOWN, buff=0.25),
        )
        retenir.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "En résumé, nous avons démontré les deux orthogonalités "
                "demandées en combinant trois idées clés : reconnaître un "
                "triangle équilatéral où médiane et hauteur coïncident, "
                "utiliser une droite des milieux pour obtenir un "
                "parallélisme, et exploiter les diagonales perpendiculaires "
                "d'un carré. C'est la démarche à retenir pour ce type "
                "d'exercice."
            )
        ) as tracker:
            self.play(FadeIn(retenir))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(retenir))

        # --- Piège à éviter ----------------------------------------------------
        piege = warning_box(
            Text(
                "« Médiane = hauteur » n'est vrai QUE dans un triangle équilatéral (ou isocèle,\n"
                "pour la médiane issue du sommet principal) — jamais dans un triangle quelconque !",
                font_size=22,
            ),
        )
        piege.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Attention au piège : l'égalité entre médiane et hauteur "
                "n'est valable que dans un triangle équilatéral, ou pour la "
                "médiane issue du sommet principal d'un triangle isocèle. "
                "Dans un triangle quelconque, la médiane et la hauteur "
                "issues d'un même sommet sont deux droites distinctes : "
                "vérifiez toujours la nature du triangle avant d'utiliser "
                "cet argument."
            )
        ) as tracker:
            self.play(FadeIn(piege))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(piege), FadeOut(titre))
