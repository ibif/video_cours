"""
scenes/Maths_OrthogonaliteEspace_01.py — Chapitre 10 « Orthogonalité dans
l'espace » (1ereC, Maths), scène 01.

§ Droites orthogonales et droites perpendiculaires : introduction (cube
ABCDEFGH, droites (AE) et (FG) non coplanaires), définitions, remarques
(perpendiculaire ⟹ orthogonale mais pas la réciproque), propriétés de
transitivité par parallélisme, piège (deux droites orthogonales à une même
troisième pas forcément parallèles entre elles).
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
from shapes.boxes import definition_box, property_box, scene_title, warning_box


# --- Géométrie en perspective cavalière (2D projeté) ------------------------

def _cube_points(side=3.0, depth_x=1.05, depth_y=0.7, origin=None):
    """Sommets d'un cube ABCDEFGH en perspective cavalière.
    Base ABCD (bas), face EFGH (haut) directement au-dessus (A-E, B-F,
    C-G, D-H arêtes verticales). D (et H, au-dessus) sont les seuls
    sommets cachés : arêtes AD, DC, DH en pointillés.
    """
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


def _cube_group(pts, color=WHITE, label_color=YELLOW, label_font_size=26):
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
        dot = Dot(point, radius=0.045, color=label_color)
        lab = MathTex(name, font_size=label_font_size, color=label_color)
        lab.next_to(dot, label_dirs.get(name, UP), buff=0.08)
        labels.add(dot, lab)
    return VGroup(lines, labels)


class DroitesOrthogonalesPerpendiculaires(NotionScene):
    def construct(self):
        titre = scene_title("Droites orthogonales et perpendiculaires")
        titre.scale(0.55)
        titre.to_edge(UP)

        # --- Énoncé : mise en situation dans le cube ------------------------
        pts = _cube_points()
        cube = _cube_group(pts)
        cube.scale(0.85)
        cube.next_to(titre, DOWN, buff=0.5)

        droite_ae = Line(pts["A"], pts["E"], color="#DE7C1F", stroke_width=5)
        droite_fg = Line(pts["F"], pts["G"], color="#288073", stroke_width=5)
        droite_ae.scale(0.85, about_point=cube.get_center())
        droite_fg.scale(0.85, about_point=cube.get_center())

        with self.voiceover(
            text=(
                "Dans le plan, deux droites perpendiculaires forment un "
                "angle droit et se coupent forcément. Mais dans l'espace, "
                "deux droites peuvent très bien ne pas être coplanaires : "
                "on dit qu'elles sont gauches, comme ici, la droite A-E et "
                "la droite F-G dans ce cube A-B-C-D-E-F-G-H. Peut-on quand "
                "même parler d'angle droit entre elles ? C'est tout "
                "l'objet de ce chapitre."
            )
        ) as tracker:
            self.play(Write(titre))
            self.play(FadeIn(cube))
            self.play(FadeIn(droite_ae))
            self.play(FadeIn(droite_fg))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(cube), FadeOut(droite_ae), FadeOut(droite_fg))

        # --- Raisonnement : les deux définitions -----------------------------
        def_orth = definition_box(
            VGroup(
                Text("Droites orthogonales", font_size=25, weight="BOLD"),
                Text(
                    "Deux droites de l'espace sont orthogonales quand les "
                    "parallèles à chacune d'elles menées par un même point\n"
                    "quelconque sont perpendiculaires (coplanaires et à angle droit).",
                    font_size=22,
                ),
                MathTex(r"d \perp d' \iff \vec{u}_d \cdot \vec{u}_{d'} = 0", font_size=27),
            ).arrange(DOWN, buff=0.22),
        )
        def_orth.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Première définition : deux droites de l'espace sont dites "
                "orthogonales lorsque les parallèles menées à chacune "
                "d'elles par un même point quelconque sont perpendiculaires. "
                "Autrement dit, leurs vecteurs directeurs ont un produit "
                "scalaire nul, que les droites soient coplanaires ou non."
            )
        ) as tracker:
            self.play(FadeIn(def_orth))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(def_orth))

        def_perp = definition_box(
            VGroup(
                Text("Droites perpendiculaires", font_size=25, weight="BOLD"),
                Text(
                    "Deux droites sont perpendiculaires quand elles sont à la fois\n"
                    "orthogonales ET coplanaires (donc sécantes, à angle droit).",
                    font_size=22,
                ),
            ).arrange(DOWN, buff=0.22),
        )
        def_perp.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Deuxième définition : deux droites sont perpendiculaires "
                "lorsqu'elles sont à la fois orthogonales et coplanaires, "
                "c'est-à-dire sécantes et formant un angle droit. La "
                "perpendicularité est donc un cas particulier de "
                "l'orthogonalité, celui où les droites se rencontrent "
                "réellement."
            )
        ) as tracker:
            self.play(FadeIn(def_perp))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(def_perp))

        remarque = warning_box(
            Text(
                "Perpendiculaires ⟹ orthogonales, mais la réciproque est fausse :\n"
                "deux droites orthogonales et non coplanaires (gauches) ne se coupent\n"
                "jamais, donc ne sont jamais perpendiculaires.",
                font_size=23,
            ),
        )
        remarque.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Remarque essentielle : deux droites perpendiculaires sont "
                "toujours orthogonales, mais la réciproque est fausse. Deux "
                "droites orthogonales et non coplanaires, comme A-E et F-G "
                "dans notre cube, ne se coupent jamais : elles ne sont donc "
                "jamais perpendiculaires, seulement orthogonales."
            )
        ) as tracker:
            self.play(FadeIn(remarque))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(remarque))

        # --- Exemple traité : les deux propriétés de transitivité -----------
        prop1 = property_box(
            VGroup(
                Text("Transitivité par parallélisme (1)", font_size=23, weight="BOLD"),
                MathTex(r"d \perp d' \ \text{et} \ d' \parallel d'' \ \Longrightarrow\ d \perp d''", font_size=27),
            ).arrange(DOWN, buff=0.22),
        )
        prop1.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Voyons deux propriétés très utiles en pratique. Première "
                "propriété : si une droite d est orthogonale à une droite "
                "d prime, et que d prime est parallèle à une droite d "
                "seconde, alors d est orthogonale à d seconde. On dit que "
                "l'orthogonalité se transporte par parallélisme."
            )
        ) as tracker:
            self.play(FadeIn(prop1))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(prop1))

        prop2 = property_box(
            VGroup(
                Text("Transitivité par parallélisme (2)", font_size=23, weight="BOLD"),
                MathTex(r"d \parallel d' \ \text{et} \ d \perp \Delta \ \Longrightarrow\ d' \perp \Delta", font_size=27),
            ).arrange(DOWN, buff=0.22),
        )
        prop2.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Deuxième propriété, la réciproque logique : si d est "
                "parallèle à d prime, et que d est orthogonale à une "
                "droite delta, alors d prime est aussi orthogonale à "
                "delta. Ces deux propriétés permettent de démontrer une "
                "orthogonalité sans jamais calculer un produit scalaire, "
                "simplement en remplaçant une droite par une droite "
                "parallèle plus commode."
            )
        ) as tracker:
            self.play(FadeIn(prop2))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(prop2))

        # --- Piège à éviter ---------------------------------------------------
        piege = warning_box(
            VGroup(
                Text(
                    "Deux droites orthogonales à une même troisième droite ne sont\n"
                    "PAS forcément parallèles entre elles !",
                    font_size=23,
                ),
                MathTex(
                    r"d \perp \Delta \ \text{et} \ d' \perp \Delta \ \not\Longrightarrow\ d \parallel d'",
                    font_size=26,
                ),
                Text(
                    "(dans un plan orthogonal à Δ, une infinité de directions conviennent)",
                    font_size=20,
                ),
            ).arrange(DOWN, buff=0.2),
        )
        piege.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Attention à un piège classique : si d et d prime sont "
                "toutes deux orthogonales à une même troisième droite "
                "delta, elles ne sont pas forcément parallèles entre "
                "elles. Contrairement au plan, il existe dans l'espace une "
                "infinité de directions orthogonales à une droite donnée : "
                "toutes les droites d'un même plan orthogonal à delta "
                "conviennent, sans être parallèles les unes aux autres."
            )
        ) as tracker:
            self.play(FadeIn(piege))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(piege), FadeOut(titre))
