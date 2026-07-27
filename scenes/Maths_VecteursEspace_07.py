"""
scenes/Maths_VecteursEspace_07.py — Chapitre 16 « Vecteurs de l'espace »
(1ereC, Maths), scène 07.

§ Parallélisme de droites et de plans dans l'espace : couple de vecteurs
directeurs d'un plan, théorème du parallélisme droite/plan, théorème du
parallélisme de deux plans, conséquence pratique (droites sécantes
respectivement parallèles). Piège : deux droites non sécantes ne sont pas
nécessairement parallèles (elles peuvent être gauches) — illustré sur un
tétraèdre (arêtes opposées non coplanaires).
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
from shapes.boxes import definition_box, property_box, scene_title, theorem_box, warning_box


def _tetra_points(names, side=3.2, back=0.9, height=2.6, origin=None):
    if origin is None:
        origin = DOWN * 1.0
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


class ParallelismeDroitesPlans(NotionScene):
    def construct(self):
        titre = scene_title("Parallélisme de droites et de plans")
        titre.scale(0.55)
        titre.to_edge(UP)
        self.play(Write(titre))

        # --- Énoncé : couple de vecteurs directeurs d'un plan -----------------------
        definition = definition_box(
            VGroup(
                Text("Couple de vecteurs directeurs d'un plan", font_size=22, weight="BOLD"),
                MathTex(
                    r"(u,v) \ \text{non colinéaires dirige le plan} \ P \ni A \ \iff\ M \in P \iff \overrightarrow{AM} \ \text{coplanaire à } u,v",
                    font_size=20,
                ),
            ).arrange(DOWN, buff=0.2),
        )
        definition.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Un couple de vecteurs u, v non colinéaires dirige un plan "
                "P passant par un point A lorsque, pour tout point M, M "
                "appartient à P si, et seulement si, le vecteur A-M est "
                "coplanaire à u et v. C'est l'analogue, pour un plan, du "
                "vecteur directeur d'une droite."
            )
        ) as tracker:
            self.play(FadeIn(definition))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(definition))

        # --- Raisonnement : les deux théorèmes de parallélisme ----------------------
        theo_droite_plan = theorem_box(
            VGroup(
                Text("Parallélisme droite / plan", font_size=22, weight="BOLD"),
                MathTex(
                    r"(d) \ \text{de vecteur directeur} \ w, \quad P \ \text{dirigé par} \ (u,v) \, :",
                    font_size=21,
                ),
                MathTex(
                    r"(d) \parallel P \ \text{ou} \ (d) \subset P \ \iff\ u,v,w \ \text{coplanaires}",
                    font_size=23,
                ),
            ).arrange(DOWN, buff=0.18),
        )
        theo_droite_plan.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Premier théorème : une droite d, de vecteur directeur w, "
                "est parallèle à un plan P dirigé par le couple u, v — ou "
                "bien incluse dans P — si, et seulement si, u, v et w sont "
                "coplanaires. Pour conclure qu'elle est strictement "
                "parallèle, disjointe du plan, il suffit ensuite de "
                "vérifier qu'un seul point de d n'appartient pas à P."
            )
        ) as tracker:
            self.play(FadeIn(theo_droite_plan))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(theo_droite_plan))

        theo_plans = theorem_box(
            VGroup(
                Text("Parallélisme de deux plans", font_size=22, weight="BOLD"),
                MathTex(
                    r"P \ \text{dirigé par} \ (u,v), \quad P' \ \text{dirigé par} \ (u',v')",
                    font_size=21,
                ),
                MathTex(
                    r"P \parallel P' \ \iff\ u,v \ \text{coplanaires à} \ u',v' \quad (\text{chacun combinaison linéaire de } u',v')",
                    font_size=20,
                ),
            ).arrange(DOWN, buff=0.18),
        )
        theo_plans.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Deuxième théorème : deux plans P et P prime, dirigés "
                "respectivement par u, v et u prime, v prime, sont "
                "parallèles si, et seulement si, u et v sont chacun "
                "combinaison linéaire de u prime et v prime — autrement "
                "dit, si les deux couples de vecteurs directeurs dirigent "
                "le même plan vectoriel."
            )
        ) as tracker:
            self.play(FadeIn(theo_plans))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(theo_plans))

        # --- Conséquence pratique ----------------------------------------------------
        consequence = property_box(
            VGroup(
                Text("Conséquence pratique, très utilisée", font_size=22, weight="BOLD"),
                Text(
                    "Si P contient deux droites sécantes respectivement parallèles à\n"
                    "deux droites sécantes de P′, alors P ∥ P′.",
                    font_size=21,
                ),
            ).arrange(DOWN, buff=0.2),
        )
        consequence.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "En pratique, on utilise surtout cette conséquence : si un "
                "plan P contient deux droites sécantes, respectivement "
                "parallèles à deux droites sécantes d'un autre plan P "
                "prime, alors P et P prime sont parallèles. C'est le "
                "critère le plus rapide pour démontrer un parallélisme de "
                "plans en pratique — nous le retrouverons à la scène 10 sur "
                "les sections de solides."
            )
        ) as tracker:
            self.play(FadeIn(consequence))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(consequence))

        # --- Piège : droites non sécantes pas forcément parallèles ------------------
        pts = _tetra_points(("A", "B", "C", "D"))
        tetra = _tetra_group(pts, ("A", "B", "C", "D"))
        figure = VGroup(tetra)
        figure.scale(0.85)
        figure.next_to(titre, DOWN, buff=0.35)

        droite_ab = Line(pts["A"], pts["B"], color="#DE7C1F", stroke_width=5)
        droite_cd = DashedLine(pts["C"], pts["D"], color="#288073", stroke_width=5, dash_length=0.09)
        droite_ab.scale(0.85, about_point=figure.get_center())
        droite_cd.scale(0.85, about_point=figure.get_center())

        piege = warning_box(
            VGroup(
                Text(
                    "Deux droites qui ne se coupent pas ne sont PAS forcément\n"
                    "parallèles : elles peuvent être GAUCHES (non coplanaires) !",
                    font_size=21,
                ),
                MathTex(
                    r"\text{Ex. : dans un tétraèdre } ABCD, \ (AB) \ \text{et} \ (CD) \ \text{(arêtes opposées) sont gauches.}",
                    font_size=19,
                ),
            ).arrange(DOWN, buff=0.2),
        )
        piege.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Attention à un piège fondamental de la géométrie dans "
                "l'espace : deux droites qui ne se coupent pas ne sont pas "
                "forcément parallèles. Contrairement au plan, où deux "
                "droites non sécantes sont automatiquement parallèles, dans "
                "l'espace elles peuvent être gauches, c'est-à-dire non "
                "coplanaires. C'est le cas ici, dans le tétraèdre A-B-C-D, "
                "des deux arêtes opposées A-B, en orange, et C-D, en vert "
                "pointillé : elles ne se coupent jamais, et pourtant elles "
                "ne sont pas parallèles non plus."
            )
        ) as tracker:
            self.play(FadeIn(figure))
            self.play(FadeIn(droite_ab), FadeIn(droite_cd))
            self.play(FadeIn(piege))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(piege), FadeOut(figure), FadeOut(droite_ab), FadeOut(droite_cd))

        # --- À retenir -----------------------------------------------------------
        retenir = property_box(
            VGroup(
                Text("À retenir : trois positions relatives possibles pour deux droites", font_size=21, weight="BOLD"),
                MathTex(r"\text{sécantes} \quad \text{ou} \quad \text{strictement parallèles} \quad \text{ou} \quad \text{gauches (non coplanaires)}", font_size=22),
                Text("Seules les deux premières se déduisent d'une colinéarité de vecteurs.", font_size=19),
            ).arrange(DOWN, buff=0.2),
        )
        retenir.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Résumons : dans l'espace, deux droites peuvent être dans "
                "trois positions relatives, et non plus deux comme dans le "
                "plan — sécantes, strictement parallèles, ou gauches. Seule "
                "l'absence de colinéarité entre deux vecteurs directeurs "
                "prouve qu'elles ne sont pas parallèles ; pour savoir si "
                "elles sont sécantes ou gauches, il faut une étude "
                "complémentaire, que nous verrons dans un chapitre "
                "ultérieur."
            )
        ) as tracker:
            self.play(FadeIn(retenir))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(retenir), FadeOut(titre))
