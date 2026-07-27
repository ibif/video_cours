"""
scenes/Maths_OrthogonaliteEspace_03.py — Chapitre 10 « Orthogonalité dans
l'espace » (1ereC, Maths), scène 03.

§ Droite et plan orthogonaux — définition : introduction (contre-exemple
(AC) et plan (BCG) — piège « deux droites parallèles ne suffisent pas »),
définition (orthogonale à deux droites SÉCANTES du plan), remarques.
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


class DroitePlanOrthogonauxDefinition(NotionScene):
    def construct(self):
        titre = scene_title("Droite et plan orthogonaux")
        titre.scale(0.55)
        titre.to_edge(UP)

        pts = _cube_points()
        cube = _cube_group(pts)
        plan_bcgf = Polygon(pts["B"], pts["C"], pts["G"], pts["F"],
                             color="#1E5FA8", fill_color="#1E5FA8", fill_opacity=0.25, stroke_width=2)
        diag_ac = Line(pts["A"], pts["C"], color="#DE7C1F", stroke_width=5)
        figure = VGroup(plan_bcgf, cube, diag_ac)
        figure.scale(0.8)
        figure.next_to(titre, DOWN, buff=0.4)

        # --- Énoncé : contre-exemple / mise en garde -------------------------
        with self.voiceover(
            text=(
                "Dans un cube A-B-C-D-E-F-G-H, considérons la diagonale "
                "A-C de la base, et le plan B-C-G, qui n'est autre que la "
                "face latérale B-C-G-F. Peut-on dire que la droite A-C est "
                "orthogonale à ce plan ? On pourrait être tenté de "
                "répondre oui un peu vite : voyons pourquoi c'est une "
                "erreur classique."
            )
        ) as tracker:
            self.play(Write(titre))
            self.play(FadeIn(cube))
            self.play(FadeIn(plan_bcgf))
            self.play(FadeIn(diag_ac))
            self.wait(tracker.get_remaining_duration())

        verticales = VGroup(
            Line(pts["B"], pts["F"], color="#288073", stroke_width=5),
            Line(pts["C"], pts["G"], color="#288073", stroke_width=5),
        ).scale(0.8, about_point=figure.get_center())

        piege_texte = warning_box(
            VGroup(
                MathTex(r"(AC) \perp (BF) \quad \text{et} \quad (AC) \perp (CG)", font_size=26),
                Text(
                    "Pourtant (BF) ∥ (CG) : ce sont DEUX droites PARALLÈLES du plan, pas deux\n"
                    "droites sécantes — cela ne suffit PAS à conclure que (AC) ⟂ plan (BCGF) !",
                    font_size=21,
                ),
                MathTex(r"\text{En fait } (AC) \ \text{n'est même pas orthogonale à } (BC) \ : \ (AC) \not\perp \text{plan } (BCGF)", font_size=21),
            ).arrange(DOWN, buff=0.22),
        )
        piege_texte.next_to(titre, DOWN, buff=0.35)

        with self.voiceover(
            text=(
                "On vérifie que A-C est bien orthogonale aux deux arêtes "
                "verticales B-F et C-G du plan. Mais attention : B-F et "
                "C-G sont deux droites parallèles entre elles, pas deux "
                "droites sécantes. Or A-C n'est pas orthogonale à la "
                "troisième direction du plan, la droite B-C : leur angle "
                "vaut quarante-cinq degrés, l'angle d'une diagonale de "
                "carré. Donc A-C n'est en réalité pas orthogonale au plan "
                "B-C-G-F, malgré les deux orthogonalités constatées. Le "
                "piège est là : vérifier l'orthogonalité à deux droites "
                "parallèles ne renseigne que sur UNE seule direction du "
                "plan, jamais sur le plan entier."
            )
        ) as tracker:
            self.play(FadeOut(figure))
            self.play(FadeIn(cube), FadeIn(plan_bcgf), FadeIn(diag_ac), FadeIn(verticales))
            self.play(FadeIn(piege_texte))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(piege_texte), FadeOut(cube), FadeOut(plan_bcgf), FadeOut(diag_ac), FadeOut(verticales))

        # --- Raisonnement : la bonne définition --------------------------------
        definition = definition_box(
            VGroup(
                Text("Droite orthogonale à un plan", font_size=25, weight="BOLD"),
                Text(
                    "Une droite d est orthogonale à un plan P quand elle est orthogonale\n"
                    "à DEUX DROITES SÉCANTES de P (donc à toute droite de P).",
                    font_size=22,
                ),
                MathTex(
                    r"d \perp r, \ d \perp s, \ r \cap s = \{I\}, \ r,s \subset P \ \Longrightarrow\ d \perp P",
                    font_size=25,
                ),
            ).arrange(DOWN, buff=0.22),
        )
        definition.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Voici donc la bonne définition. Une droite d est "
                "orthogonale à un plan P lorsqu'elle est orthogonale à "
                "deux droites SÉCANTES de ce plan, c'est-à-dire deux "
                "droites de P qui se coupent en un point I. C'est cette "
                "condition de sécance, et non de simple présence dans le "
                "plan, qui garantit que d est orthogonale à toutes les "
                "droites du plan, dans toutes les directions possibles."
            )
        ) as tracker:
            self.play(FadeIn(definition))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(definition))

        # --- Exemple traité : bon exemple dans le cube --------------------------
        pts2 = _cube_points()
        cube2 = _cube_group(pts2)
        bf2 = Line(pts2["B"], pts2["F"], color="#288073", stroke_width=5)
        bc2 = Line(pts2["A"], pts2["B"], color="#288073", stroke_width=5)
        figure2 = VGroup(cube2, bf2, bc2)
        figure2.scale(0.8)
        figure2.next_to(titre, DOWN, buff=0.4)

        bon_exemple = MathTex(
            r"(BF) \perp (AB) \ \text{et} \ (BF) \perp (BC), \ (AB) \cap (BC) = \{B\} \ \Longrightarrow\ (BF) \perp \text{plan } (ABCD)",
            font_size=23,
        )
        bon_exemple.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Reprenons le cube avec la bonne méthode. L'arête verticale "
                "B-F est orthogonale à A-B et orthogonale à B-C, deux "
                "arêtes du plan de base A-B-C-D qui se coupent bien en B. "
                "Cette fois, les deux droites sont sécantes : on peut donc "
                "conclure, en toute rigueur, que B-F est orthogonale au "
                "plan A-B-C-D tout entier."
            )
        ) as tracker:
            self.play(FadeIn(figure2))
            self.wait(1)
            self.play(FadeOut(figure2))
            self.play(Write(bon_exemple))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(bon_exemple))

        # --- À retenir / remarque --------------------------------------------
        remarque = warning_box(
            VGroup(
                Text(
                    "À retenir : pour prouver qu'une droite est orthogonale à un plan,\n"
                    "il FAUT deux droites SÉCANTES du plan (pas seulement deux droites\n"
                    "quelconques, et surtout pas deux droites parallèles entre elles).",
                    font_size=23,
                ),
            ),
        )
        remarque.next_to(titre, DOWN, buff=0.45)

        with self.voiceover(
            text=(
                "Retenez bien cette règle avant de continuer : pour "
                "démontrer qu'une droite est orthogonale à un plan, il "
                "faut impérativement exhiber deux droites sécantes de ce "
                "plan, chacune orthogonale à la droite étudiée. Deux "
                "droites parallèles entre elles, aussi nombreuses soient "
                "les vérifications, ne suffiront jamais : c'est le piège "
                "que nous venons de voir avec A-C et le plan B-C-G-F."
            )
        ) as tracker:
            self.play(FadeIn(remarque))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(remarque), FadeOut(titre))
