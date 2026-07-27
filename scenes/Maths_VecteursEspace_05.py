"""
scenes/Maths_VecteursEspace_05.py — Chapitre 16 « Vecteurs de l'espace »
(1ereC, Maths), scène 05.

§ Base de l'espace (triplet non coplanaire) et théorème de décomposition
d'un vecteur sur une base (existence + unicité, démonstration complète :
existence géométrique via le plan (OAB) et la parallèle à (OC), unicité via
la non-coplanarité). Illustré sur le tétraèdre OABC (figure 2 du PDF).
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


def _tetra_points(names, side=3.0, back=0.85, height=2.4, origin=None):
    if origin is None:
        origin = DOWN * 0.9
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


class BaseDecomposition(NotionScene):
    def construct(self):
        titre = scene_title("Base de l'espace et décomposition d'un vecteur")
        titre.scale(0.5)
        titre.to_edge(UP)

        pts = _tetra_points(("A", "B", "C", "O"))
        tetra = _tetra_group(pts, ("A", "B", "C", "O"))
        figure = VGroup(tetra)
        figure.scale(0.82)
        figure.next_to(titre, DOWN, buff=0.35)

        # --- Énoncé : définition ----------------------------------------------------
        definition = definition_box(
            VGroup(
                Text("Base de l'espace", font_size=24, weight="BOLD"),
                MathTex(
                    r"(i,j,k) \ \text{est une base de l'espace} \ \iff\ i,j,k \ \text{non coplanaires}",
                    font_size=24,
                ),
                Text("(le tétraèdre OABC ci-dessus, avec i=OA, j=OB, k=OC, illustre une base.)", font_size=19),
            ).arrange(DOWN, buff=0.22),
        )
        definition.next_to(titre, DOWN, buff=0.35)

        with self.voiceover(
            text=(
                "Un triplet de vecteurs i, j, k est une base de l'espace "
                "lorsque ces trois vecteurs ne sont pas coplanaires. En "
                "posant i égal O-A, j égal O-B, k égal O-C, ce tétraèdre "
                "O-A-B-C que voici illustre exactement une telle base."
            )
        ) as tracker:
            self.play(Write(titre))
            self.play(FadeIn(figure))
            self.play(FadeIn(definition))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(definition))

        # --- Raisonnement : théorème de décomposition -------------------------------
        theo = theorem_box(
            VGroup(
                Text("Théorème de décomposition sur une base", font_size=22, weight="BOLD"),
                MathTex(
                    r"(i,j,k) \ \text{base} \ \Longrightarrow\ \forall w, \ \exists ! \, (x,y,z)\in\mathbb R^3, \ w = x\,i + y\,j + z\,k",
                    font_size=22,
                ),
            ).arrange(DOWN, buff=0.2),
        )
        theo.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Voici le théorème fondamental de cette scène. Si i, j, k "
                "est une base de l'espace, alors tout vecteur w se "
                "décompose de façon unique : il existe un unique triplet de "
                "réels x, y, z tel que w soit égal à x fois i, plus y fois "
                "j, plus z fois k."
            )
        ) as tracker:
            self.play(FadeOut(figure))
            self.play(FadeIn(theo))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(theo))

        # --- Démonstration : existence -----------------------------------------------
        demo_exist = VGroup(
            Text("Démonstration — existence", font_size=22, weight="BOLD"),
            Text("Soit M tel que w = OM. La droite par M parallèle à (OC) coupe le", font_size=19),
            Text("plan (OAB) en un point M′ (sinon (OC) serait parallèle à (OAB), donc", font_size=19),
            Text("coplanaire à i,j — contradiction avec (i,j,k) base).", font_size=19),
            MathTex(r"\overrightarrow{M'M} \ \text{colinéaire à } k \ \Longrightarrow\ \overrightarrow{M'M} = z\,k, \ z \in \mathbb R", font_size=21),
            MathTex(r"M' \in (OAB), \ (i,j) \ \text{non colinéaires} \ \Longrightarrow\ \overrightarrow{OM'} = x\,i + y\,j", font_size=21),
            MathTex(r"w = \overrightarrow{OM} = \overrightarrow{OM'} + \overrightarrow{M'M} = x\,i + y\,j + z\,k", font_size=23, color=YELLOW),
        ).arrange(DOWN, buff=0.16)
        demo_exist.next_to(titre, DOWN, buff=0.25)

        with self.voiceover(
            text=(
                "Démontrons d'abord l'existence. Soit M le point tel que w "
                "égale O-M. La droite passant par M et parallèle à O-C "
                "coupe le plan O-A-B en un point M prime — cette droite "
                "n'est pas parallèle au plan, sinon O-C serait coplanaire à "
                "i et j, ce qui contredirait le fait que i, j, k forment "
                "une base. Le vecteur M prime M est alors colinéaire à k, "
                "donc égal à z fois k pour un certain réel z. Et comme M "
                "prime appartient au plan O-A-B, avec i, j non colinéaires, "
                "le théorème de décomposition plane donne O-M prime égal x "
                "fois i plus y fois j. En sommant, w égale O-M égale O-M "
                "prime plus M prime M, c'est-à-dire x i plus y j plus z k. "
                "L'existence est démontrée."
            )
        ) as tracker:
            self.play(Write(demo_exist[0]))
            self.play(Write(demo_exist[1]), Write(demo_exist[2]), Write(demo_exist[3]))
            self.play(Write(demo_exist[4]))
            self.play(Write(demo_exist[5]))
            self.play(Write(demo_exist[6]))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(demo_exist))

        # --- Démonstration : unicité ---------------------------------------------------
        demo_unique = VGroup(
            Text("Démonstration — unicité", font_size=22, weight="BOLD"),
            MathTex(r"\text{Si } xi+yj+zk = x'i+y'j+z'k, \ \text{alors} \ (x-x')i+(y-y')j+(z-z')k = \vec 0.", font_size=19),
            MathTex(r"\text{Si } z \neq z' \ : \ k = \tfrac{x'-x}{z-z'}\,i + \tfrac{y'-y}{z-z'}\,j \ \Longrightarrow\ k \ \text{coplanaire à } i,j.", font_size=19),
            Text("Contradiction avec (i,j,k) base non coplanaire ⟹ z = z′.", font_size=19),
            MathTex(r"\text{Alors } (x-x')i + (y-y')j = \vec 0, \ \text{et} \ i,j \ \text{non colinéaires} \ \Longrightarrow\ x=x', \ y=y'.", font_size=19),
        ).arrange(DOWN, buff=0.2)
        demo_unique.next_to(titre, DOWN, buff=0.3)

        with self.voiceover(
            text=(
                "Passons à l'unicité. Supposons que w admette deux "
                "décompositions, avec des coefficients x, y, z et x prime, "
                "y prime, z prime. En soustrayant, on obtient x moins x "
                "prime, fois i, plus y moins y prime, fois j, plus z moins "
                "z prime, fois k, égal au vecteur nul. Si z était différent "
                "de z prime, on pourrait isoler k comme combinaison "
                "linéaire de i et j, ce qui rendrait k coplanaire à i et j "
                "— contradiction, puisque i, j, k forment une base. Donc z "
                "égale z prime. Il reste alors x moins x prime, fois i, "
                "plus y moins y prime, fois j, égal au vecteur nul ; comme "
                "i et j ne sont pas colinéaires, cela impose x égale x "
                "prime et y égale y prime. L'unicité est démontrée."
            )
        ) as tracker:
            self.play(Write(demo_unique[0]))
            self.play(Write(demo_unique[1]))
            self.play(Write(demo_unique[2]))
            self.play(Write(demo_unique[3]))
            self.play(Write(demo_unique[4]))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(demo_unique))

        # --- À retenir -----------------------------------------------------------
        retenir = property_box(
            VGroup(
                Text("À retenir", font_size=23, weight="BOLD"),
                MathTex(r"(i,j,k) \ \text{non coplanaires} \ \Longrightarrow\ \text{tout } w \ \text{a un UNIQUE triplet } (x,y,z)", font_size=22),
                Text("(x, y, z) sont les COMPOSANTES de w dans la base (i,j,k).", font_size=20),
            ).arrange(DOWN, buff=0.22),
        )
        retenir.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Retenons l'essentiel : dès que i, j, k forment une base de "
                "l'espace, c'est-à-dire dès qu'ils ne sont pas coplanaires, "
                "tout vecteur w admet un unique triplet de réels x, y, z, "
                "appelés ses composantes dans cette base. Ce théorème est "
                "la clé de voûte de toute la suite : il va nous permettre, "
                "à la scène suivante, d'attacher des coordonnées à chaque "
                "point de l'espace."
            )
        ) as tracker:
            self.play(FadeIn(retenir))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(retenir), FadeOut(titre))
