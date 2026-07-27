"""
scenes/Maths_OrthogonaliteEspace_07.py — Chapitre 10 « Orthogonalité dans
l'espace » (1ereC, Maths), scène 07.

§ Plan médiateur d'un segment (théorème + définition, démonstration par
double inclusion), axe d'un cercle circonscrit, sphère circonscrite à un
tétraèdre (avec justification), théorème des trois perpendiculaires (avec
démonstration, réutilisant le théorème fondamental de la scène 4).
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
from shapes.boxes import definition_box, property_box, scene_title, theorem_box, warning_box


def _plan_schema(width=3.4, height=2.0, color="#1E5FA8", opacity=0.25):
    return Polygon(
        LEFT * width / 2 + DOWN * height / 3,
        RIGHT * width / 2 + DOWN * height / 6,
        RIGHT * width / 2 + UP * height / 3,
        LEFT * width / 2 + UP * height / 6,
        color=color, fill_color=color, fill_opacity=opacity, stroke_width=2,
    )


class PlanMediateurSpherePerpendiculaires(NotionScene):
    def construct(self):
        titre = scene_title("Plan médiateur, sphère circonscrite, 3 perpendiculaires")
        titre.scale(0.42)
        titre.to_edge(UP)
        self.play(Write(titre))

        # --- Énoncé : plan médiateur --------------------------------------------
        A_pt, B_pt = LEFT * 2.6, RIGHT * 2.6
        seg_ab = Line(A_pt, B_pt, color="#DE7C1F", stroke_width=4)
        I_pt = (A_pt + B_pt) / 2
        plan_med = _plan_schema(width=2.2, height=3.0).rotate(1.5708).move_to(I_pt)
        labels_ab = VGroup(
            MathTex("A", font_size=26).next_to(A_pt, DOWN, buff=0.15),
            MathTex("B", font_size=26).next_to(B_pt, DOWN, buff=0.15),
            MathTex("I", font_size=24, color=YELLOW).next_to(I_pt, DOWN, buff=0.15),
        )
        schema_med = VGroup(plan_med, seg_ab, labels_ab, Dot(I_pt, radius=0.04, color=YELLOW))
        schema_med.next_to(titre, DOWN, buff=0.4)

        theo_med = theorem_box(
            MathTex(r"\{M \ / \ MA = MB\} = \text{plan passant par } I=\text{milieu}[AB], \ \text{orthogonal à } (AB)", font_size=22),
        )
        theo_med.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Premier résultat : le plan médiateur d'un segment A-B. "
                "L'ensemble des points M équidistants de A et de B est "
                "exactement le plan passant par I, le milieu de A-B, et "
                "orthogonal à la droite A-B. Démontrons cette égalité par "
                "double inclusion."
            )
        ) as tracker:
            self.play(FadeIn(schema_med))
            self.play(FadeIn(theo_med))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(theo_med))

        def_med = definition_box(
            Text(
                "Ce plan s'appelle le plan médiateur du segment [AB].",
                font_size=24,
            ),
        )
        def_med.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text="Ce plan porte un nom : c'est le plan médiateur du segment A-B."
        ) as tracker:
            self.play(FadeIn(def_med))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(def_med))

        # --- Raisonnement : double inclusion -----------------------------------
        preuve_med = VGroup(
            MathTex(r"M \in P \ \Longrightarrow\ (MI) \subset P \ \Longrightarrow\ (MI) \perp (AB)", font_size=22),
            MathTex(r"\Longrightarrow\ MA^2 = MI^2+IA^2 = MI^2+IB^2 = MB^2 \ \Longrightarrow\ MA=MB", font_size=22),
            MathTex(r"\text{Réciproquement, } MA=MB \ \Longrightarrow\ \text{triangle } MAB \ \text{isocèle en } M", font_size=22),
            MathTex(r"\Longrightarrow\ \text{médiane } (MI) = \text{hauteur} \ \Longrightarrow\ (MI)\perp(AB) \ \Longrightarrow\ M \in P", font_size=22, color=YELLOW),
        ).arrange(DOWN, buff=0.24)
        preuve_med.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Sens direct : si M appartient au plan P, alors la droite "
                "M-I est incluse dans P, donc orthogonale à A-B. Par "
                "Pythagore, M-A au carré et M-B au carré valent tous deux "
                "M-I au carré plus I-A au carré, puisque I-A égale I-B : "
                "donc M-A égale M-B. Réciproquement, si M-A égale M-B, le "
                "triangle M-A-B est isocèle en M, donc sa médiane M-I est "
                "aussi sa hauteur, orthogonale à A-B : M appartient bien "
                "au plan P. L'égalité des deux ensembles est démontrée."
            )
        ) as tracker:
            self.play(FadeOut(schema_med))
            self.play(Write(preuve_med[0]))
            self.play(Write(preuve_med[1]))
            self.play(Write(preuve_med[2]))
            self.play(Write(preuve_med[3]))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(preuve_med))

        # --- Exemple traité : axe et sphère circonscrite ------------------------
        prop_axe = property_box(
            VGroup(
                Text("Axe d'un cercle circonscrit", font_size=22, weight="BOLD"),
                Text(
                    "L'axe du cercle circonscrit à un triangle ABC est la droite orthogonale au\n"
                    "plan (ABC) passant par son centre : c'est l'ensemble des points équidistants\n"
                    "de A, B et C (intersection des 3 plans médiateurs des côtés).",
                    font_size=20,
                ),
            ).arrange(DOWN, buff=0.18),
        )
        prop_axe.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "On généralise cette idée à un triangle. L'axe du cercle "
                "circonscrit à un triangle A-B-C est la droite orthogonale "
                "au plan A-B-C, passant par le centre de ce cercle : c'est "
                "l'ensemble des points équidistants de A, B et C, obtenu "
                "en intersectant les trois plans médiateurs des côtés du "
                "triangle."
            )
        ) as tracker:
            self.play(FadeIn(prop_axe))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(prop_axe))

        prop_sphere = property_box(
            VGroup(
                Text("Sphère circonscrite à un tétraèdre", font_size=22, weight="BOLD"),
                Text(
                    "Tout tétraèdre ABCD possède une unique sphère circonscrite passant par\n"
                    "ses 4 sommets : son centre O est l'intersection de l'axe du cercle circonscrit\n"
                    "à (ABC) avec le plan médiateur de [AD] (O équidistant de A, B, C, D).",
                    font_size=20,
                ),
            ).arrange(DOWN, buff=0.18),
        )
        prop_sphere.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "On peut alors justifier l'existence d'une sphère "
                "circonscrite à tout tétraèdre A-B-C-D. L'axe du cercle "
                "circonscrit à la face A-B-C est constitué des points "
                "équidistants de A, B et C. En le coupant avec le plan "
                "médiateur du segment A-D, on obtient un point O, "
                "équidistant à la fois de A, B, C, et de A, D : donc "
                "équidistant des quatre sommets. Ce point O est le centre "
                "de l'unique sphère passant par les quatre sommets du "
                "tétraèdre."
            )
        ) as tracker:
            self.play(FadeIn(prop_sphere))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(prop_sphere))

        # --- À retenir : théorème des trois perpendiculaires --------------------
        P_center = DOWN * 1.3
        plan_p = _plan_schema(width=5.0, height=2.2, color="#288073").move_to(P_center)
        A3 = P_center + UP * 2.4 + LEFT * 0.3
        H3 = P_center + DOWN * 0.15
        d_line = Line(P_center + LEFT * 2.3 + DOWN * 0.55, P_center + RIGHT * 2.1 + UP * 0.55, color="#DE7C1F", stroke_width=4)
        K3 = H3 + (RIGHT * 2.1 + UP * 0.55 - (LEFT * 2.3 + DOWN * 0.55)) * 0.42 + (P_center + LEFT * 2.3 + DOWN * 0.55 - P_center)
        seg_ah = Line(A3, H3, color=WHITE, stroke_width=3)
        seg_hk = DashedLine(H3, K3, color=WHITE, stroke_width=3)
        seg_ak = Line(A3, K3, color=YELLOW, stroke_width=4)
        pts3 = VGroup(
            Dot(A3, radius=0.05), MathTex("A", font_size=24).next_to(A3, UP, buff=0.1),
            Dot(H3, radius=0.05), MathTex("H", font_size=22).next_to(H3, DOWN, buff=0.1),
            Dot(K3, radius=0.05), MathTex("K", font_size=22).next_to(K3, RIGHT, buff=0.1),
        )
        schema3 = VGroup(plan_p, d_line, seg_ah, seg_hk, seg_ak, pts3)
        schema3.scale(0.75).next_to(titre, DOWN, buff=0.35)

        theo_3perp = property_box(
            VGroup(
                Text("Théorème des trois perpendiculaires", font_size=21, weight="BOLD"),
                MathTex(
                    r"(AH)\perp P, \ d \subset P, \ K = \text{projeté de } H \ \text{sur } d "
                    r"\ \Longrightarrow\ (AK) \perp d",
                    font_size=20,
                ),
            ).arrange(DOWN, buff=0.15),
        )
        theo_3perp.next_to(schema3, DOWN, buff=0.25)

        with self.voiceover(
            text=(
                "Terminons avec le théorème des trois perpendiculaires. "
                "Soit A un point, H son projeté orthogonal sur un plan P, "
                "d une droite de P, et K le projeté orthogonal de H sur d, "
                "à l'intérieur du plan P. Alors la droite A-K est "
                "orthogonale à d. La démonstration réutilise directement "
                "le théorème fondamental de la scène 4 : A-H est "
                "orthogonale à d, car A-H est orthogonale à tout le plan "
                "P ; H-K est orthogonale à d par construction. Les droites "
                "A-H et H-K sont sécantes en H et toutes deux orthogonales "
                "à d : donc d est orthogonale au plan A-H-K, et en "
                "particulier à la droite A-K."
            )
        ) as tracker:
            self.play(FadeIn(schema3))
            self.play(FadeIn(theo_3perp))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(schema3), FadeOut(theo_3perp))

        # --- Piège à éviter ------------------------------------------------------
        piege = warning_box(
            Text(
                "Ne pas confondre H (projeté de A sur le plan P tout entier) et K (projeté\n"
                "de H sur la droite d, DANS le plan P) : ce sont deux projections successives,\n"
                "sur deux objets différents — inverser l'ordre rend la démonstration fausse.",
                font_size=21,
            ),
        )
        piege.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Attention à un piège fréquent avec ce théorème : il ne "
                "faut pas confondre H, le projeté de A sur le plan P tout "
                "entier, et K, le projeté de H sur la droite d, à "
                "l'intérieur du plan P. Ce sont deux projections "
                "successives, sur deux objets de nature différente : "
                "intervertir leur ordre rend toute la démonstration fausse."
            )
        ) as tracker:
            self.play(FadeIn(piege))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(piege), FadeOut(titre))
