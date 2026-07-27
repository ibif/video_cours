"""
scenes/Maths_VecteursEspace_04.py — Chapitre 16 « Vecteurs de l'espace »
(1ereC, Maths), scène 04.

§ Vecteurs coplanaires : définition, remarques (2 vecteurs toujours
coplanaires ; OA,OB,OC non coplanaires ⟺ tétraèdre ; colinéaires ⟹
coplanaires avec tout autre vecteur), théorème de caractérisation
fondamentale w = xu+yv (avec démonstration complète), théorème avec 3
coefficients. Exemple résolu 3 : p=u+v, q=v+w, r=u+2v+w, montrer p,q,r
coplanaires.
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
from shapes.boxes import corrige_box, definition_box, exercise_box, scene_title, theorem_box, warning_box


def _tetra_points(names, side=2.6, back=0.8, height=2.2, origin=None):
    if origin is None:
        origin = DOWN * 0.8
    n0, n1, n2, n3 = names
    p0 = origin + LEFT * side / 2
    p1 = origin + RIGHT * side / 2
    p2 = origin + UP * back + RIGHT * back * 0.7
    p3 = (p0 + p1) / 2 + UP * height + RIGHT * 0.25
    return {n0: p0, n1: p1, n2: p2, n3: p3}


def _tetra_group(pts, names, color=WHITE, label_color=YELLOW, label_font_size=24, label_dirs=None):
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
        dot = Dot(point, radius=0.04, color=label_color)
        lab = MathTex(name, font_size=label_font_size, color=label_color)
        lab.next_to(dot, label_dirs.get(name, UP), buff=0.08)
        labels.add(dot, lab)
    return VGroup(lines, labels)


class VecteursCoplanaires(NotionScene):
    def construct(self):
        titre = scene_title("Vecteurs coplanaires")
        titre.scale(0.55)
        titre.to_edge(UP)
        self.play(Write(titre))

        # --- Énoncé : définition ---------------------------------------------------
        definition = definition_box(
            VGroup(
                Text("Vecteurs coplanaires", font_size=23, weight="BOLD"),
                Text(
                    "Les points O, A₁, …, Aₙ sont coplanaires s'il existe un plan qui les\n"
                    "contient tous. Les vecteurs OA₁, …, OAₙ sont alors dits coplanaires\n"
                    "(la propriété ne dépend pas du choix du point O commun).",
                    font_size=20,
                ),
            ).arrange(DOWN, buff=0.22),
        )
        definition.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Voici la grande notion nouvelle de ce chapitre, celle qui "
                "n'existe pas dans le plan : la coplanarité. Des points O, "
                "A un, jusqu'à A n, sont coplanaires s'il existe un plan qui "
                "les contient tous. On dit alors que les vecteurs O-A un "
                "jusqu'à O-A n, tous issus d'un même point O, sont "
                "coplanaires — et cette propriété ne dépend pas du choix de "
                "ce point O."
            )
        ) as tracker:
            self.play(FadeIn(definition))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(definition))

        # --- Remarques --------------------------------------------------------------
        remarques = warning_box(
            VGroup(
                Text("Remarques", font_size=22, weight="BOLD"),
                MathTex(r"\bullet \ \ \text{Deux vecteurs sont TOUJOURS coplanaires.}", font_size=21),
                MathTex(r"\bullet \ \ \overrightarrow{OA}, \overrightarrow{OB}, \overrightarrow{OC} \ \text{non coplanaires} \iff O,A,B,C \ \text{forment un tétraèdre}", font_size=21),
                MathTex(r"\bullet \ \ u, v \ \text{colinéaires} \ \Longrightarrow\ u, v, w \ \text{coplanaires, quel que soit } w", font_size=21),
            ).arrange(DOWN, buff=0.2),
        )
        remarques.next_to(titre, DOWN, buff=0.35)

        with self.voiceover(
            text=(
                "Trois remarques essentielles. D'abord, deux vecteurs sont "
                "toujours coplanaires : on peut toujours trouver un plan "
                "qui les contient tous les deux. Ensuite, trois vecteurs "
                "O-A, O-B, O-C sont non coplanaires si, et seulement si, O, "
                "A, B, C forment un véritable tétraèdre, non aplati. Enfin, "
                "si deux vecteurs u et v sont colinéaires, alors u, v et "
                "n'importe quel troisième vecteur w sont automatiquement "
                "coplanaires."
            )
        ) as tracker:
            self.play(FadeIn(remarques))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(remarques))

        # --- Raisonnement : théorème de caractérisation + démonstration -----------
        theo_carac = theorem_box(
            VGroup(
                Text("Caractérisation fondamentale", font_size=22, weight="BOLD"),
                MathTex(
                    r"u, v \ \text{non colinéaires} \ : \quad w \ \text{coplanaire à} \ u,v \ \iff\ \exists (x,y)\in\mathbb R^2, \ w = x\,u + y\,v",
                    font_size=22,
                ),
            ).arrange(DOWN, buff=0.2),
        )
        theo_carac.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Voici le théorème central de cette scène. Si u et v sont "
                "deux vecteurs non colinéaires, alors un vecteur w est "
                "coplanaire à u et v si, et seulement si, il existe deux "
                "réels x et y tels que w soit égal à x fois u plus y fois "
                "v : autrement dit, w est une combinaison linéaire de u et "
                "v."
            )
        ) as tracker:
            self.play(FadeIn(theo_carac))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(theo_carac))

        demo = VGroup(
            Text("Démonstration", font_size=22, weight="BOLD"),
            Text("Soit O un point, u = OA, v = OB (A,B,O non alignés car u,v non colinéaires).", font_size=19),
            MathTex(r"(\Leftarrow) \ \ \text{Si } w = xu+yv, \ \text{soit } C \ \text{tel que} \ w = \overrightarrow{OC}.", font_size=20),
            MathTex(r"\text{Alors } C \ \text{se construit dans le plan } (OAB) \ \Longrightarrow\ O,A,B,C \ \text{coplanaires.}", font_size=20),
            MathTex(r"(\Rightarrow) \ \ \text{Si } w = \overrightarrow{OC} \ \text{coplanaire à } u,v, \ \text{alors } C \in \text{plan}(OAB).", font_size=20),
            MathTex(r"\text{Dans ce plan, } (u,v) \ \text{non colinéaires forment une base} \ \Longrightarrow\ \exists!(x,y), \ \overrightarrow{OC}=xu+yv.", font_size=19),
        ).arrange(DOWN, buff=0.18)
        demo.next_to(titre, DOWN, buff=0.3)

        with self.voiceover(
            text=(
                "Démontrons ce théorème. Plaçons-nous en un point O, avec u "
                "égal O-A et v égal O-B ; comme u et v ne sont pas "
                "colinéaires, O, A, B ne sont pas alignés. Dans le sens "
                "facile : si w s'écrit x fois u plus y fois v, on construit "
                "le point C tel que w soit O-C directement dans le plan "
                "O-A-B, par la règle du parallélogramme ; donc O, A, B, C "
                "sont coplanaires. Réciproquement, si w égal O-C est "
                "coplanaire à u et v, alors C appartient au plan O-A-B ; "
                "dans ce plan, u et v, non colinéaires, forment une base du "
                "plan, donc le théorème de décomposition plane, déjà connu, "
                "garantit l'existence et l'unicité du couple x, y tel que "
                "O-C égale x fois u plus y fois v."
            )
        ) as tracker:
            self.play(Write(demo[0]))
            self.play(Write(demo[1]))
            self.play(Write(demo[2]))
            self.play(Write(demo[3]))
            self.play(Write(demo[4]))
            self.play(Write(demo[5]))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(demo))

        theo_coeffs = theorem_box(
            VGroup(
                Text("Condition avec trois coefficients", font_size=22, weight="BOLD"),
                MathTex(
                    r"u,v,w \ \text{coplanaires} \ \iff\ \exists (\alpha,\beta,\gamma) \neq (0,0,0), \ \alpha u + \beta v + \gamma w = \vec 0",
                    font_size=23,
                ),
            ).arrange(DOWN, buff=0.2),
        )
        theo_coeffs.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Ce théorème se reformule d'une façon plus robuste, qui "
                "englobe aussi les cas où deux des trois vecteurs seraient "
                "colinéaires : u, v, w sont coplanaires si, et seulement "
                "si, il existe trois réels alpha, bêta, gamma, non tous "
                "nuls, tels que alpha fois u plus bêta fois v plus gamma "
                "fois w soit le vecteur nul."
            )
        ) as tracker:
            self.play(FadeIn(theo_coeffs))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(theo_coeffs))

        # --- Petite illustration : tétraèdre = non coplanaires ---------------------
        pts = _tetra_points(("A", "B", "C", "O"))
        tetra = _tetra_group(pts, ("A", "B", "C", "O"))
        tetra.scale(0.85)
        tetra.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Petit rappel visuel : lorsque O, A, B, C ne sont pas "
                "coplanaires, ils forment exactement ce solide à quatre "
                "faces triangulaires, le tétraèdre — la figure de référence "
                "de tout ce chapitre."
            )
        ) as tracker:
            self.play(FadeIn(tetra))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(tetra))

        # --- Exemple résolu 3 --------------------------------------------------------
        enonce = exercise_box(
            VGroup(
                Text("Exemple résolu 3", font_size=23, weight="BOLD"),
                MathTex(r"p = u+v, \quad q = v+w, \quad r = u+2v+w.", font_size=24),
                MathTex(r"\text{Montrer que } p, q, r \ \text{sont coplanaires.}", font_size=24),
            ).arrange(DOWN, buff=0.2),
        )
        enonce.next_to(titre, DOWN, buff=0.35)

        with self.voiceover(
            text=(
                "Exemple résolu. On pose p égal u plus v, q égal v plus w, "
                "et r égal u plus deux v plus w. On veut montrer que p, q "
                "et r sont coplanaires."
            )
        ) as tracker:
            self.play(FadeIn(enonce))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(enonce))

        resolution = VGroup(
            MathTex(r"p + q = (u+v) + (v+w) = u + 2v + w", font_size=25),
            MathTex(r"\Longrightarrow\ p + q = r, \quad \text{soit} \quad r = 1\cdot p + 1 \cdot q", font_size=25),
            MathTex(r"\Longrightarrow\ r \ \text{combinaison linéaire de } p, q \ \Longrightarrow\ p,q,r \ \text{coplanaires}", font_size=25, color=YELLOW),
        ).arrange(DOWN, buff=0.28)
        resolution.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Calculons p plus q : u plus v, plus v plus w, cela donne u "
                "plus deux v plus w — exactement l'expression de r. Donc r "
                "est égal à p plus q, c'est-à-dire une combinaison linéaire "
                "de p et de q. Par le théorème de caractérisation, p, q et "
                "r sont donc coplanaires."
            )
        ) as tracker:
            self.play(Write(resolution[0]))
            self.play(Write(resolution[1]))
            self.play(Write(resolution[2]))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(resolution))

        # --- À retenir -----------------------------------------------------------
        retenir = corrige_box(
            VGroup(
                Text("À retenir", font_size=23, weight="BOLD"),
                MathTex(r"w = xu+yv \ (u,v \ \text{non colinéaires}) \quad \text{ou} \quad \alpha u+\beta v+\gamma w=\vec 0, \ (\alpha,\beta,\gamma)\neq(0,0,0)", font_size=19),
                Text(
                    "Pour prouver une coplanarité : faire apparaître une combinaison\n"
                    "linéaire entre les vecteurs (comme p+q=r ci-dessus).",
                    font_size=20,
                ),
            ).arrange(DOWN, buff=0.2),
        )
        retenir.next_to(titre, DOWN, buff=0.35)

        with self.voiceover(
            text=(
                "Retenons la méthode : pour prouver que des vecteurs sont "
                "coplanaires, on cherche à écrire l'un comme combinaison "
                "linéaire des deux autres, ou à trouver une relation entre "
                "les trois avec des coefficients non tous nuls. C'est "
                "exactement ce que nous venons de faire avec p plus q égale "
                "r."
            )
        ) as tracker:
            self.play(FadeIn(retenir))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(retenir), FadeOut(titre))
