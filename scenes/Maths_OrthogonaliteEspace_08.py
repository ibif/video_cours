"""
scenes/Maths_OrthogonaliteEspace_08.py — Chapitre 10 « Orthogonalité dans
l'espace » (1ereC, Maths), scène 08.

§ Plans perpendiculaires : mise en situation (fil à plomb du maçon),
définition, remarques (symétrie de la définition, plans perpendiculaires
nécessairement sécants), exemples dans le cube, piège (droite parallèle à
un plan perpendiculaire à un autre pas forcément orthogonale à cet autre).
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
    Polygon,
    Text,
    VGroup,
    Write,
)

from shapes.base_scene import NotionScene
from shapes.boxes import definition_box, scene_title, warning_box


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


class PlansPerpendiculaires(NotionScene):
    def construct(self):
        titre = scene_title("Plans perpendiculaires")
        titre.scale(0.55)
        titre.to_edge(UP)

        # --- Énoncé : mise en situation (fil à plomb) ---------------------------
        sol = Line(LEFT * 2.8, RIGHT * 2.8, color="#288073", stroke_width=4)
        mur = Line(LEFT * 1.0 + DOWN * 0.05, LEFT * 1.0 + UP * 2.6, color="#1E5FA8", stroke_width=4)
        fil = Line(LEFT * 1.0 + UP * 2.6, LEFT * 1.0 + DOWN * 0.05, color=WHITE, stroke_width=2)
        plomb = Dot(LEFT * 1.0 + DOWN * 0.05, radius=0.08, color=YELLOW)
        schema_maçon = VGroup(sol, mur, fil, plomb)
        schema_maçon.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Sur un chantier, le maçon vérifie qu'un mur est bien "
                "vertical à l'aide d'un fil à plomb : un fil tendu par un "
                "poids indique toujours la direction verticale, "
                "orthogonale au sol. Si ce fil reste bien collé au mur sur "
                "toute sa hauteur, le mur est vertical, c'est-à-dire "
                "orthogonal au plan du sol. On dit alors que le plan du "
                "mur et le plan du sol sont perpendiculaires."
            )
        ) as tracker:
            self.play(Write(titre))
            self.play(FadeIn(schema_maçon))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(schema_maçon))

        # --- Raisonnement : définition -------------------------------------------
        definition = definition_box(
            VGroup(
                Text("Plans perpendiculaires", font_size=25, weight="BOLD"),
                Text(
                    "Deux plans P et Q sont perpendiculaires quand l'un des deux contient\n"
                    "une droite orthogonale à l'autre.",
                    font_size=22,
                ),
                MathTex(r"P \perp Q \iff \exists\, d \subset P \ \text{tel que } d \perp Q", font_size=25),
            ).arrange(DOWN, buff=0.22),
        )
        definition.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Voici la définition rigoureuse. Deux plans P et Q sont "
                "perpendiculaires lorsque l'un des deux, disons P, contient "
                "une droite d orthogonale à l'autre plan, Q. Dans notre "
                "exemple du maçon, le mur contient bien une droite, le fil "
                "à plomb, orthogonale au plan du sol."
            )
        ) as tracker:
            self.play(FadeIn(definition))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(definition))

        remarque1 = warning_box(
            VGroup(
                Text(
                    "La définition est SYMÉTRIQUE : si P contient une droite ⟂ Q,\n"
                    "alors Q contient aussi une droite ⟂ P (admis ici, démontré scène 9).",
                    font_size=21,
                ),
                Text(
                    "Deux plans perpendiculaires sont toujours SÉCANTS (jamais parallèles) :\n"
                    "des plans parallèles ne peuvent jamais être perpendiculaires entre eux.",
                    font_size=21,
                ),
            ).arrange(DOWN, buff=0.22),
        )
        remarque1.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Deux remarques importantes. D'abord, cette définition est "
                "en réalité symétrique : si P contient une droite "
                "orthogonale à Q, alors Q contient aussi une droite "
                "orthogonale à P. Nous l'admettons pour l'instant ; elle "
                "sera démontrée à la scène suivante. Ensuite, deux plans "
                "perpendiculaires sont toujours sécants : deux plans "
                "parallèles ne peuvent jamais être perpendiculaires entre "
                "eux."
            )
        ) as tracker:
            self.play(FadeIn(remarque1))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(remarque1))

        # --- Exemple traité : dans le cube ----------------------------------------
        pts = _cube_points()
        cube = _cube_group(pts)
        face_base = Polygon(pts["A"], pts["B"], pts["C"], pts["D"], color="#288073",
                             fill_color="#288073", fill_opacity=0.28, stroke_width=2)
        face_avant = Polygon(pts["A"], pts["B"], pts["F"], pts["E"], color="#1E5FA8",
                              fill_color="#1E5FA8", fill_opacity=0.28, stroke_width=2)
        figure = VGroup(cube, face_base, face_avant)
        figure.scale(0.8)
        figure.next_to(titre, DOWN, buff=0.35)

        exemple_txt = MathTex(
            r"(BF) \subset (ABFE), \ (BF) \perp (ABCD) \quad \Longrightarrow\quad (ABFE) \perp (ABCD)",
            font_size=24,
        )
        exemple_txt.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Illustrons cela dans le cube. La face avant A-B-F-E "
                "contient l'arête verticale B-F, qui est orthogonale au "
                "plan de base A-B-C-D. La face avant est donc "
                "perpendiculaire à la base : on retrouve deux faces "
                "adjacentes d'un cube, toujours perpendiculaires entre "
                "elles."
            )
        ) as tracker:
            self.play(FadeIn(figure))
            self.wait(1)
            self.play(FadeOut(figure))
            self.play(Write(exemple_txt))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(exemple_txt))

        # --- Piège à éviter ---------------------------------------------------------
        piege = warning_box(
            VGroup(
                Text(
                    "Si P ⟂ Q et qu'une droite d est PARALLÈLE à P, on ne peut PAS en\n"
                    "déduire que d est orthogonale à Q !",
                    font_size=22,
                ),
                MathTex(r"P \perp Q, \ d \parallel P \ \not\Longrightarrow\ d \perp Q", font_size=25),
                Text("(d peut très bien être elle-même parallèle à Q, ou sécante sans être orthogonale)", font_size=18),
            ).arrange(DOWN, buff=0.2),
        )
        piege.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Attention à un piège très répandu : si le plan P est "
                "perpendiculaire au plan Q, et qu'une droite d est "
                "parallèle à P, on ne peut absolument pas en déduire que d "
                "est orthogonale à Q. La perpendicularité de deux plans ne "
                "se transmet pas ainsi à une droite simplement parallèle à "
                "l'un d'eux : cette droite peut très bien être parallèle à "
                "Q elle aussi, ou sécante à Q sans lui être orthogonale."
            )
        ) as tracker:
            self.play(FadeIn(piege))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(piege), FadeOut(titre))
