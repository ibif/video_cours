"""
scenes/Maths_VecteursEspace_10.py — Chapitre 16 « Vecteurs de l'espace »
(1ereC, Maths), scène 10.

§ Sections de solides par un plan : rappels utiles (intersection de deux
plans sécants = droite ; plans parallèles coupés par un même plan → droites
parallèles ; un plan qui contient 2 points d'une face contient la droite
entière). Exemple résolu 5 complet : cube ABCDEFGH d'arête a, M/N/P
milieux de [AB]/[AD]/[AE], la section par (MNP) est un triangle équilatéral
de côté a√2/2 (démonstration via théorème des milieux dans chaque face +
parallélisme des plans (MNP) et (BDE)).
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
from shapes.boxes import corrige_box, exercise_box, property_box, scene_title


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


class SectionsDeSolides(NotionScene):
    def construct(self):
        titre = scene_title("Sections de solides par un plan")
        titre.scale(0.55)
        titre.to_edge(UP)
        self.play(Write(titre))

        # --- Énoncé : rappels utiles -------------------------------------------------
        rappels = property_box(
            VGroup(
                Text("Rappels utiles pour construire une section", font_size=21, weight="BOLD"),
                MathTex(r"\bullet \ \ P \cap P' \ \text{sécants} \ \Longrightarrow\ P\cap P' \ \text{est une DROITE}", font_size=20),
                MathTex(r"\bullet \ \ P \parallel P', \ Q \ \text{sécant aux deux} \ \Longrightarrow\ (Q\cap P) \parallel (Q\cap P')", font_size=20),
                Text("• Un plan de coupe qui contient 2 points d'une face contient TOUTE la droite qui les joint", font_size=18),
            ).arrange(DOWN, buff=0.2),
        )
        rappels.next_to(titre, DOWN, buff=0.35)

        with self.voiceover(
            text=(
                "Pour construire la section d'un solide par un plan, trois "
                "rappels suffisent. D'abord, l'intersection de deux plans "
                "sécants est toujours une droite. Ensuite, si deux plans "
                "sont parallèles et qu'un troisième plan les coupe tous les "
                "deux, les deux droites d'intersection obtenues sont "
                "parallèles entre elles. Enfin, si le plan de coupe "
                "contient déjà deux points d'une même face du solide, il "
                "contient automatiquement toute la droite qui les relie."
            )
        ) as tracker:
            self.play(FadeIn(rappels))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(rappels))

        # --- Exemple résolu 5 --------------------------------------------------------
        pts = _cube_points()
        cube = _cube_group(pts)
        M = (pts["A"] + pts["B"]) / 2
        N = (pts["A"] + pts["D"]) / 2
        P = (pts["A"] + pts["E"]) / 2
        figure = VGroup(cube)
        figure.scale(0.82)
        figure.next_to(titre, DOWN, buff=0.3)
        center = figure.get_center()
        raw_center = cube.get_center()

        def to_fig(pt):
            return (pt - raw_center) * 0.82 + center

        M_s, N_s, P_s = to_fig(M), to_fig(N), to_fig(P)

        pt_m = VGroup(Dot(M_s, radius=0.05, color="#DE7C1F"), MathTex("M", font_size=22, color="#DE7C1F").next_to(M_s, DOWN, buff=0.08))
        pt_n = VGroup(Dot(N_s, radius=0.05, color="#DE7C1F"), MathTex("N", font_size=22, color="#DE7C1F").next_to(N_s, LEFT, buff=0.08))
        pt_p = VGroup(Dot(P_s, radius=0.05, color="#DE7C1F"), MathTex("P", font_size=22, color="#DE7C1F").next_to(P_s, LEFT, buff=0.08))

        enonce = exercise_box(
            VGroup(
                Text("Exemple résolu 5", font_size=22, weight="BOLD"),
                MathTex(
                    r"ABCDEFGH \ \text{cube d'arête} \ a. \quad M, N, P \ \text{milieux de} \ [AB], [AD], [AE].",
                    font_size=21,
                ),
                MathTex(r"\text{Déterminer la section du cube par le plan} \ (MNP).", font_size=21),
            ).arrange(DOWN, buff=0.2),
        )
        enonce.next_to(titre, DOWN, buff=0.35)

        with self.voiceover(
            text=(
                "Exemple résolu, le plus complet du chapitre. "
                "A-B-C-D-E-F-G-H est un cube d'arête a. M, N, P sont les "
                "milieux respectifs de A-B, A-D, A-E. On veut déterminer, "
                "et caractériser complètement, la section du cube par le "
                "plan M-N-P."
            )
        ) as tracker:
            self.play(FadeIn(enonce))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(enonce))
        self.play(FadeIn(figure))
        self.play(FadeIn(pt_m), FadeIn(pt_n), FadeIn(pt_p))

        etape1 = VGroup(
            MathTex(r"\text{Face } ABD : \ M,N \ \text{milieux de} \ [AB],[AD] \ \Longrightarrow\ (MN) \ \text{droite des milieux}", font_size=19),
            MathTex(r"\Longrightarrow\ (MN)\parallel(BD), \quad MN = \tfrac12 BD = \tfrac{a\sqrt2}{2}", font_size=20),
        ).arrange(DOWN, buff=0.2)
        etape1.next_to(titre, DOWN, buff=0.35)

        seg_mn = Line(M_s, N_s, color="#288073", stroke_width=4)

        with self.voiceover(
            text=(
                "Traitons d'abord la face A-B-D, c'est-à-dire la base du "
                "cube. M et N sont les milieux de A-B et A-D : la droite "
                "M-N est donc la droite des milieux du triangle A-B-D, "
                "parallèle à B-D, et de longueur la moitié de B-D, "
                "c'est-à-dire a racine de deux, sur deux, puisque B-D est "
                "la diagonale d'une face carrée de côté a."
            )
        ) as tracker:
            self.play(FadeIn(seg_mn))
            self.play(Write(etape1[0]))
            self.play(Write(etape1[1]))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(etape1))

        etape2 = VGroup(
            MathTex(r"\text{Face } ABE : \ M,P \ \text{milieux de} \ [AB],[AE] \ \Longrightarrow\ (MP)\parallel(BE), \ MP=\tfrac{a\sqrt2}{2}", font_size=19),
            MathTex(r"\text{Face } ADE : \ N,P \ \text{milieux de} \ [AD],[AE] \ \Longrightarrow\ (NP)\parallel(DE), \ NP=\tfrac{a\sqrt2}{2}", font_size=19),
        ).arrange(DOWN, buff=0.2)
        etape2.next_to(titre, DOWN, buff=0.35)

        seg_mp = Line(M_s, P_s, color="#1E5FA8", stroke_width=4)
        seg_np = Line(N_s, P_s, color="#B42E41", stroke_width=4)

        with self.voiceover(
            text=(
                "De même, dans la face A-B-E, M et P sont les milieux de "
                "A-B et A-E : M-P est parallèle à B-E, et vaut aussi a "
                "racine de deux sur deux. Et dans la face A-D-E, N et P "
                "sont les milieux de A-D et A-E : N-P est parallèle à D-E, "
                "de même longueur, a racine de deux sur deux."
            )
        ) as tracker:
            self.play(FadeIn(seg_mp), FadeIn(seg_np))
            self.play(Write(etape2[0]))
            self.play(Write(etape2[1]))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(etape2))

        etape3 = VGroup(
            MathTex(r"MN = MP = NP = \tfrac{a\sqrt2}{2} \ \Longrightarrow\ MNP \ \text{TRIANGLE ÉQUILATÉRAL}", font_size=22, color=YELLOW),
            MathTex(r"(MN)\parallel(BD), (MP)\parallel(BE) \ \text{sécantes en } M \ \Longrightarrow\ (MNP)\parallel(BDE) \ \text{(scène 7)}", font_size=19),
            MathTex(r"\Longrightarrow\ (MNP) \ \text{ne recoupe aucune autre face} \ \Longrightarrow\ \text{la section EST le triangle} \ MNP", font_size=19),
        ).arrange(DOWN, buff=0.22)
        etape3.next_to(titre, DOWN, buff=0.35)

        with self.voiceover(
            text=(
                "Les trois côtés M-N, M-P, N-P sont donc égaux : le "
                "triangle M-N-P est équilatéral, de côté a racine de deux "
                "sur deux. De plus, M-N est parallèle à B-D, et M-P est "
                "parallèle à B-E, deux droites sécantes en M, "
                "respectivement parallèles à deux droites sécantes en B du "
                "plan B-D-E : par la conséquence pratique vue à la scène 7, "
                "le plan M-N-P est donc parallèle au plan B-D-E. Cela "
                "confirme que le plan de coupe ne traverse aucune autre "
                "face du cube au-delà de ces trois-là : la section est "
                "exactement le triangle équilatéral M-N-P."
            )
        ) as tracker:
            self.play(Write(etape3[0]))
            self.play(Write(etape3[1]))
            self.play(Write(etape3[2]))
            self.wait(tracker.get_remaining_duration())

        self.play(
            FadeOut(etape3), FadeOut(figure), FadeOut(pt_m), FadeOut(pt_n), FadeOut(pt_p),
            FadeOut(seg_mn), FadeOut(seg_mp), FadeOut(seg_np),
        )

        # --- À retenir -----------------------------------------------------------
        retenir = corrige_box(
            VGroup(
                MathTex(r"\text{Section} = \text{triangle équilatéral} \ MNP, \ \text{de côté} \ \tfrac{a\sqrt2}{2}", font_size=24),
                Text(
                    "Méthode : dans chaque face contenant 2 points du plan de coupe, tracer la\n"
                    "droite des milieux, puis vérifier avec le parallélisme de plans (scène 7)\n"
                    "que la section ne va pas plus loin.",
                    font_size=19,
                ),
            ).arrange(DOWN, buff=0.24),
        )
        retenir.next_to(titre, DOWN, buff=0.35)

        with self.voiceover(
            text=(
                "Retenons la méthode : dans chaque face du solide qui "
                "contient deux points du plan de coupe, on trace la droite "
                "qui les joint — ici, systématiquement une droite des "
                "milieux — puis on vérifie, grâce au parallélisme de plans, "
                "que le polygone obtenu se referme bien sans traverser "
                "d'autres faces."
            )
        ) as tracker:
            self.play(FadeIn(retenir))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(retenir), FadeOut(titre))
