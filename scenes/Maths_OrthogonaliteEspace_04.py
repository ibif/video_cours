"""
scenes/Maths_OrthogonaliteEspace_04.py — Chapitre 10 « Orthogonalité dans
l'espace » (1ereC, Maths), scène 04.

§ Théorème fondamental (droite orthogonale à un plan ⟹ orthogonale à toute
droite du plan) avec démonstration complète (point I milieu de [BC],
Pythagore dans deux triangles rectangles, théorème de la médiane, réciproque
de Pythagore). Méthode pratique (réciproque d'usage). Exemple résolu 2 :
tétraèdre régulier ABCD, (AB) ⟂ (CD) via médianes-hauteurs du triangle
équilatéral.
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
from shapes.boxes import example_box, method_box, scene_title, theorem_box


# --- Géométrie en perspective cavalière (2D projeté) ------------------------

def _tetrahedron_points(scale=2.6, origin=None):
    """Sommets d'un tétraèdre ABCD en perspective : face avant ABC visible
    (solide), sommet D « derrière », en pointillés (arêtes DA, DB, DC)."""
    if origin is None:
        origin = DOWN * 0.2
    A = origin + UP * scale * 0.85
    B = origin + LEFT * scale * 0.7 + DOWN * scale * 0.55
    C = origin + RIGHT * scale * 0.7 + DOWN * scale * 0.55
    D = origin + DOWN * scale * 0.05 + RIGHT * scale * 0.05
    return {"A": A, "B": B, "C": C, "D": D}


def _tetrahedron_group(pts, color=WHITE, label_color=YELLOW, label_font_size=26):
    p = pts
    visible = [("A", "B"), ("A", "C"), ("B", "C")]
    hidden = [("A", "D"), ("B", "D"), ("C", "D")]
    lines = VGroup()
    for u, v in visible:
        lines.add(Line(p[u], p[v], color=color, stroke_width=2.5))
    for u, v in hidden:
        lines.add(DashedLine(p[u], p[v], color=color, stroke_width=2, dash_length=0.09))

    label_dirs = {"A": UP, "B": DOWN + LEFT, "C": DOWN + RIGHT, "D": DOWN * 0.3 + RIGHT * 0.5}
    labels = VGroup()
    for name, point in p.items():
        dot = Dot(point, radius=0.05, color=label_color)
        lab = MathTex(name, font_size=label_font_size, color=label_color)
        lab.next_to(dot, label_dirs.get(name, UP), buff=0.1)
        labels.add(dot, lab)
    return VGroup(lines, labels)


class TheoremeFondamentalOrthogonalite(NotionScene):
    def construct(self):
        titre = scene_title("Théorème fondamental de l'orthogonalité")
        titre.scale(0.55)
        titre.to_edge(UP)

        # --- Énoncé : le théorème ----------------------------------------------
        theoreme = theorem_box(
            VGroup(
                Text(
                    "Si une droite d est orthogonale à deux droites sécantes d'un plan P,\n"
                    "alors elle est orthogonale à TOUTE droite de P (donc au plan P).",
                    font_size=23,
                ),
                MathTex(
                    r"d \perp r, \ d \perp s, \ r \cap s = \{A\}, \ r,s \subset P"
                    r"\ \Longrightarrow\ \forall \Delta \subset P,\ d \perp \Delta",
                    font_size=24,
                ),
            ).arrange(DOWN, buff=0.22),
        )
        theoreme.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Voici le théorème fondamental de ce chapitre. Si une "
                "droite d est orthogonale à deux droites sécantes r et s "
                "d'un plan P, alors elle est orthogonale à toute droite du "
                "plan P, quelle que soit sa direction. C'est ce résultat "
                "qui justifie la définition vue précédemment. Démontrons-le."
            )
        ) as tracker:
            self.play(Write(titre))
            self.play(FadeIn(theoreme))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(theoreme))

        # --- Raisonnement : démonstration complète -----------------------------
        etape1 = MathTex(
            r"\text{Soit } \Delta \subset P \text{ une droite quelconque. On choisit } "
            r"B \in r, \ C \in s \ \text{tels que } I = \text{milieu}[BC] \in \Delta.",
            font_size=21,
        )
        etape2 = MathTex(
            r"\text{Soit } M \in d, \ M \neq A. \ \text{Triangles } MAB \ \text{et} \ MAC \ \text{rectangles en } A \ (d\perp r, d\perp s) :",
            font_size=21,
        )
        etape3 = MathTex(
            r"MB^2 = MA^2 + AB^2 \qquad \text{et} \qquad MC^2 = MA^2 + AC^2 \quad \text{(Pythagore)}",
            font_size=24,
        )
        etape4 = MathTex(
            r"MB^2+MC^2 = 2MA^2 + AB^2+AC^2",
            font_size=24,
        )
        demo1 = VGroup(etape1, etape2, etape3, etape4).arrange(DOWN, buff=0.28)
        demo1.next_to(titre, DOWN, buff=0.35)

        with self.voiceover(
            text=(
                "Prenons une droite delta quelconque du plan P. Comme r et "
                "s sont sécantes en A et engendrent le plan, on peut "
                "toujours choisir un point B sur r et un point C sur s "
                "tels que I, le milieu du segment B-C, soit un point de "
                "delta. Prenons ensuite un point M sur la droite d, "
                "différent de A. Les triangles M-A-B et M-A-C sont "
                "rectangles en A, puisque d est orthogonale à r et à s. Le "
                "théorème de Pythagore donne alors : M-B au carré égale "
                "M-A au carré plus A-B au carré, et de même pour M-C. En "
                "additionnant, M-B au carré plus M-C au carré égale deux "
                "fois M-A au carré, plus A-B au carré plus A-C au carré."
            )
        ) as tracker:
            self.play(Write(etape1))
            self.play(Write(etape2))
            self.play(Write(etape3))
            self.play(Write(etape4))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(demo1))

        etape5 = MathTex(
            r"\text{Théorème de la médiane (}I=\text{milieu}[BC]\text{) dans } MBC \ \text{et } ABC \ :",
            font_size=22,
        )
        etape6 = MathTex(
            r"MB^2+MC^2 = 2MI^2 + \dfrac{BC^2}{2} \qquad \text{et} \qquad AB^2+AC^2 = 2AI^2 + \dfrac{BC^2}{2}",
            font_size=23,
        )
        etape7 = MathTex(
            r"2MI^2 + \dfrac{BC^2}{2} = 2MA^2 + 2AI^2 + \dfrac{BC^2}{2} \ \Longrightarrow\ MI^2 = MA^2 + AI^2",
            font_size=24,
        )
        etape8 = MathTex(
            r"\text{Réciproque de Pythagore} \ \Longrightarrow\ MAI \ \text{rectangle en } A "
            r"\ \Longrightarrow\ (MA) \perp (AI), \ \text{c'est-à-dire } d \perp \Delta.",
            font_size=22,
            color=YELLOW,
        )
        demo2 = VGroup(etape5, etape6, etape7, etape8).arrange(DOWN, buff=0.3)
        demo2.next_to(titre, DOWN, buff=0.35)

        with self.voiceover(
            text=(
                "On applique maintenant le théorème de la médiane, qui "
                "relie la somme des carrés de deux côtés d'un triangle à "
                "la médiane issue du troisième sommet, dans le triangle "
                "M-B-C et dans le triangle A-B-C, tous deux munis du même "
                "milieu I. En combinant cette relation avec l'égalité "
                "précédente, le terme B-C au carré disparaît, et il reste : "
                "M-I au carré égale M-A au carré plus A-I au carré. Par la "
                "réciproque du théorème de Pythagore, le triangle M-A-I "
                "est donc rectangle en A : la droite M-A, c'est-à-dire d, "
                "est orthogonale à la droite A-I, qui n'est autre que "
                "delta, puisque A et I sont deux points de delta. Le "
                "théorème est démontré."
            )
        ) as tracker:
            self.play(Write(etape5))
            self.play(Write(etape6))
            self.play(Write(etape7))
            self.play(Write(etape8))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(demo2))

        # --- Méthode pratique --------------------------------------------------
        methode = method_box(
            VGroup(
                Text("Pour démontrer qu'une droite d est orthogonale à un plan P :", font_size=23, weight="BOLD"),
                Text(
                    "il suffit de trouver DEUX droites SÉCANTES de P, chacune orthogonale à d\n"
                    "(inutile — et impossible — de tester toutes les droites de P une à une).",
                    font_size=21,
                ),
            ).arrange(DOWN, buff=0.2),
        )
        methode.next_to(titre, DOWN, buff=0.45)

        with self.voiceover(
            text=(
                "Ce théorème donne, en pratique, une méthode redoutablement "
                "efficace : pour démontrer qu'une droite d est orthogonale "
                "à un plan P, il suffit de trouver deux droites sécantes de "
                "P, chacune orthogonale à d. Inutile, et de toute façon "
                "impossible, de tester une à une toutes les droites du "
                "plan."
            )
        ) as tracker:
            self.play(FadeIn(methode))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(methode))

        # --- Exemple traité : tétraèdre régulier --------------------------------
        pts = _tetrahedron_points()
        tetra = _tetrahedron_group(pts)
        I = (pts["C"] + pts["D"]) / 2
        pt_i = VGroup(Dot(I, radius=0.05, color="#DE7C1F"), MathTex("I", font_size=24, color="#DE7C1F").next_to(I, RIGHT, buff=0.1))
        seg_ai = Line(pts["A"], I, color="#288073", stroke_width=4)
        seg_bi = Line(pts["B"], I, color="#1E5FA8", stroke_width=4)
        figure = VGroup(tetra, pt_i, seg_ai, seg_bi)
        figure.scale(0.72)
        figure.next_to(titre, DOWN, buff=0.35)

        enonce_ex = MathTex(
            r"ABCD \ \text{tétraèdre RÉGULIER}, \ I = \text{milieu}[CD]. \ \text{Démontrer } (AB) \perp (CD).",
            font_size=23,
        )
        enonce_ex.next_to(titre, DOWN, buff=0.35)

        with self.voiceover(
            text=(
                "Appliquons cette méthode. Soit A-B-C-D un tétraèdre "
                "régulier : ses quatre faces sont des triangles "
                "équilatéraux identiques. Notons I le milieu de l'arête "
                "C-D. On veut démontrer que A-B est orthogonale à C-D."
            )
        ) as tracker:
            self.play(Write(enonce_ex))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(enonce_ex))
        self.play(FadeIn(tetra))

        demo_ex = example_box(
            VGroup(
                MathTex(r"ACD \ \text{équilatéral} \ \Longrightarrow\ (AI) \ \text{médiane} = \text{hauteur} \ \Longrightarrow\ (AI)\perp(CD)", font_size=21),
                MathTex(r"BCD \ \text{équilatéral} \ \Longrightarrow\ (BI) \ \text{médiane} = \text{hauteur} \ \Longrightarrow\ (BI)\perp(CD)", font_size=21),
                MathTex(r"(AI) \cap (BI) = \{I\} \ \Longrightarrow\ (CD) \perp \text{plan}(ABI) \ \Longrightarrow\ (CD) \perp (AB)", font_size=22, color=YELLOW),
            ).arrange(DOWN, buff=0.24),
        )
        demo_ex.next_to(titre, DOWN, buff=0.35)

        with self.voiceover(
            text=(
                "Dans la face A-C-D, équilatérale, la médiane A-I issue de "
                "A est aussi une hauteur : elle est donc orthogonale à "
                "C-D. De même, dans la face B-C-D, la médiane B-I est "
                "aussi une hauteur, orthogonale à C-D. Les droites A-I et "
                "B-I sont sécantes en I : ce sont exactement les deux "
                "droites sécantes qu'il nous fallait. D'après notre "
                "méthode, C-D est donc orthogonale au plan A-B-I tout "
                "entier, et en particulier à la droite A-B, qui appartient "
                "à ce plan. On a bien démontré que A-B est orthogonale à "
                "C-D."
            )
        ) as tracker:
            self.play(FadeIn(pt_i))
            self.play(FadeIn(seg_ai), FadeIn(seg_bi))
            self.play(FadeIn(demo_ex))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(figure), FadeOut(demo_ex), FadeOut(titre))
