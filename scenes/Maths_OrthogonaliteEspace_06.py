"""
scenes/Maths_OrthogonaliteEspace_06.py — Chapitre 10 « Orthogonalité dans
l'espace » (1ereC, Maths), scène 06.

§ Projeté orthogonal et distance d'un point à un plan / à une droite :
définition du projeté orthogonal sur un plan, théorème + définition de la
distance point-plan (AH ≤ AM, démonstration par Pythagore), projeté
orthogonal sur une droite et distance point-droite. Exemple résolu 3 complet
(cube d'arête a : projeté de G sur (ABC), distance AG = a√3, démonstration
(AC) ⟂ (DBF) et distance de A à ce plan).
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
from shapes.boxes import definition_box, example_box, scene_title, theorem_box


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


class ProjeteOrthogonalDistance(NotionScene):
    def construct(self):
        titre = scene_title("Projeté orthogonal et distances")
        titre.scale(0.55)
        titre.to_edge(UP)
        self.play(Write(titre))

        # --- Énoncé : définition du projeté orthogonal sur un plan -------------
        def_proj_plan = definition_box(
            VGroup(
                Text("Projeté orthogonal sur un plan", font_size=24, weight="BOLD"),
                Text(
                    "Le projeté orthogonal d'un point M sur un plan P est le point H,\n"
                    "intersection de P avec la droite passant par M et orthogonale à P.",
                    font_size=22,
                ),
            ).arrange(DOWN, buff=0.2),
        )
        def_proj_plan.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Commençons par une définition clé. Le projeté orthogonal "
                "d'un point M sur un plan P est le point H obtenu en "
                "traçant, par M, la droite orthogonale à P : cette droite "
                "coupe P en un unique point, H, garanti par la propriété "
                "d'existence et d'unicité vue précédemment."
            )
        ) as tracker:
            self.play(FadeIn(def_proj_plan))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(def_proj_plan))

        # --- Raisonnement : théorème + définition distance point-plan ----------
        theo_dist = theorem_box(
            VGroup(
                Text("H, projeté orthogonal de A sur P : le point de P le plus proche de A", font_size=21, weight="BOLD"),
                MathTex(r"\forall M \in P, \ AH \le AM \quad \text{(égalité } \iff M = H\text{)}", font_size=25),
            ).arrange(DOWN, buff=0.2),
        )
        theo_dist.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Voici pourquoi ce point H est particulier : c'est le "
                "point de P le plus proche de A. Si H est le projeté "
                "orthogonal de A sur P, alors pour tout point M de P, la "
                "distance A-H est inférieure ou égale à A-M, avec égalité "
                "uniquement lorsque M est confondu avec H."
            )
        ) as tracker:
            self.play(FadeIn(theo_dist))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(theo_dist))

        def_dist_plan = definition_box(
            MathTex(r"\text{Distance du point } A \ \text{au plan } P \ : \quad d(A,P) = AH", font_size=27),
        )
        def_dist_plan.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "On définit ainsi la distance du point A au plan P comme "
                "étant précisément cette longueur A-H."
            )
        ) as tracker:
            self.play(FadeIn(def_dist_plan))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(def_dist_plan))

        preuve = MathTex(
            r"(AH) \perp P \ \Longrightarrow\ (AH) \perp (HM) \ \Longrightarrow\ AM^2 = AH^2 + HM^2 \ge AH^2 \quad \text{(Pythagore)}",
            font_size=23,
        )
        preuve.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "La démonstration est immédiate grâce à Pythagore. Comme "
                "A-H est orthogonale au plan P, elle est en particulier "
                "orthogonale à la droite H-M, incluse dans P. Le triangle "
                "A-H-M est donc rectangle en H, et le théorème de "
                "Pythagore donne A-M au carré égale A-H au carré plus H-M "
                "au carré, qui est toujours supérieur ou égal à A-H au "
                "carré, avec égalité seulement si H-M est nul, "
                "c'est-à-dire si M égale H."
            )
        ) as tracker:
            self.play(Write(preuve))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(preuve))

        def_proj_droite = definition_box(
            VGroup(
                Text("Projeté orthogonal sur une droite / distance point-droite", font_size=21, weight="BOLD"),
                Text(
                    "Le projeté orthogonal de A sur une droite d est le point H′, intersection\n"
                    "de d avec le plan passant par A et orthogonal à d. On pose d(A,d) = AH′.",
                    font_size=21,
                ),
            ).arrange(DOWN, buff=0.2),
        )
        def_proj_droite.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "On procède de façon symétrique pour une droite. Le "
                "projeté orthogonal d'un point A sur une droite d est le "
                "point H prime, intersection de d avec le plan passant par "
                "A et orthogonal à d. La distance de A à la droite d est "
                "alors, de la même manière, la longueur A-H prime."
            )
        ) as tracker:
            self.play(FadeIn(def_proj_droite))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(def_proj_droite))

        # --- Exemple traité : cube d'arête a ------------------------------------
        pts = _cube_points()
        cube = _cube_group(pts)
        figure = VGroup(cube)
        figure.scale(0.78)
        figure.next_to(titre, DOWN, buff=0.35)

        enonce_ex = MathTex(
            r"\text{Cube } ABCDEFGH \ \text{d'arête } a. \ \text{1) Projeté de } G \ \text{sur } (ABC) \ ? \ \text{Calculer } AG.",
            font_size=22,
        )
        enonce_ex.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Exemple résolu. Soit A-B-C-D-E-F-G-H un cube d'arête a. "
                "Premièrement, quel est le projeté orthogonal de G sur le "
                "plan de base A-B-C, et que vaut la distance A-G ?"
            )
        ) as tracker:
            self.play(Write(enonce_ex))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(enonce_ex))
        self.play(FadeIn(figure))

        cg_seg = Line(pts["C"], pts["G"], color="#DE7C1F", stroke_width=5).scale(0.78, about_point=figure.get_center())
        ag_seg = Line(pts["A"], pts["G"], color="#288073", stroke_width=5).scale(0.78, about_point=figure.get_center())
        ac_seg = Line(pts["A"], pts["C"], color="#1E5FA8", stroke_width=5).scale(0.78, about_point=figure.get_center())

        resolution1 = example_box(
            VGroup(
                MathTex(r"(CG) \perp \text{plan}(ABC) \ \Longrightarrow\ \text{projeté de } G \ \text{sur } (ABC) \ \text{est } C", font_size=21),
                MathTex(r"AC = a\sqrt{2} \ \text{(diagonale du carré } ABCD\text{)}, \ CG = a \ \text{(arête)}", font_size=21),
                MathTex(r"ACG \ \text{rectangle en } C \ \Longrightarrow\ AG^2 = AC^2+CG^2 = 2a^2+a^2 = 3a^2 \ \Longrightarrow\ AG = a\sqrt{3}", font_size=21, color=YELLOW),
            ).arrange(DOWN, buff=0.22),
        )
        resolution1.next_to(titre, DOWN, buff=0.35)

        with self.voiceover(
            text=(
                "L'arête verticale C-G est orthogonale au plan de base, "
                "donc le projeté orthogonal de G sur A-B-C est simplement "
                "C. La droite A-G traverse alors le triangle rectangle "
                "A-C-G, rectangle en C, où A-C, la diagonale du carré de "
                "base, mesure a racine de deux, et C-G, une arête, mesure "
                "a. Le théorème de Pythagore donne A-G au carré égale deux "
                "a carré plus a carré, soit trois a carré : A-G vaut donc "
                "a racine de trois, la diagonale du cube tout entier."
            )
        ) as tracker:
            self.play(FadeIn(cg_seg))
            self.play(FadeIn(ac_seg), FadeIn(ag_seg))
            self.play(FadeIn(resolution1))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(resolution1), FadeOut(cg_seg), FadeOut(ac_seg), FadeOut(ag_seg))

        enonce_ex2 = MathTex(
            r"\text{2) Démontrer } (AC) \perp \text{plan}(DBF) \ \text{et calculer } d(A, (DBF)).",
            font_size=23,
        )
        enonce_ex2.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Deuxième question : démontrons que la diagonale A-C est "
                "orthogonale au plan D-B-F, et calculons la distance de A "
                "à ce plan."
            )
        ) as tracker:
            self.play(Write(enonce_ex2))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(enonce_ex2))

        bd_seg = DashedLine(pts["B"], pts["D"], color="#1E5FA8", stroke_width=5).scale(0.78, about_point=figure.get_center())
        bf_seg = Line(pts["B"], pts["F"], color="#288073", stroke_width=5).scale(0.78, about_point=figure.get_center())
        ac_seg2 = Line(pts["A"], pts["C"], color="#DE7C1F", stroke_width=5).scale(0.78, about_point=figure.get_center())
        O = (pts["A"] + pts["C"]) / 2
        pt_o = VGroup(Dot(O, radius=0.05, color=YELLOW), MathTex("O", font_size=24, color=YELLOW).next_to(O, DOWN, buff=0.08)).scale(0.78).move_to(O * 0.78 + figure.get_center() * 0.22)

        resolution2 = example_box(
            VGroup(
                MathTex(r"(AC) \perp (BD) \ \text{(diagonales du carré } ABCD\text{)}, \quad (AC) \perp (BF) \ \text{(} BF \perp \text{base)}", font_size=21),
                MathTex(r"(BD) \cap (BF) = \{B\} \ \Longrightarrow\ (AC) \perp \text{plan}(DBF)", font_size=22, color=YELLOW),
                MathTex(r"O = (AC) \cap (BD) = \text{centre du carré} \ \Longrightarrow\ \text{projeté de } A \ \text{sur } (DBF) \ \text{est } O", font_size=20),
                MathTex(r"d(A,(DBF)) = AO = \dfrac{AC}{2} = \dfrac{a\sqrt{2}}{2}", font_size=23, color=YELLOW),
            ).arrange(DOWN, buff=0.2),
        )
        resolution2.next_to(titre, DOWN, buff=0.35)

        with self.voiceover(
            text=(
                "A-C est orthogonale à B-D, car ce sont les diagonales du "
                "carré de base, et A-C est orthogonale à B-F, car B-F est "
                "verticale, donc orthogonale à toute droite du plan de "
                "base auquel A-C appartient. Les droites B-D et B-F sont "
                "sécantes en B : A-C est donc orthogonale au plan D-B-F "
                "tout entier. Or le point O, intersection des diagonales A-C "
                "et B-D, appartient justement à ce plan, puisqu'il est sur "
                "la droite B-D. C'est donc lui, le projeté orthogonal de A "
                "sur le plan D-B-F, et la distance cherchée est A-O, la "
                "moitié de la diagonale A-C, soit a racine de deux sur "
                "deux."
            )
        ) as tracker:
            self.play(FadeIn(bd_seg), FadeIn(bf_seg), FadeIn(ac_seg2))
            self.play(FadeIn(pt_o))
            self.play(FadeIn(resolution2))
            self.wait(tracker.get_remaining_duration())

        self.play(
            FadeOut(resolution2), FadeOut(bd_seg), FadeOut(bf_seg),
            FadeOut(ac_seg2), FadeOut(pt_o), FadeOut(figure), FadeOut(titre),
        )
