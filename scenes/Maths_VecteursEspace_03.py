"""
scenes/Maths_VecteursEspace_03.py — Chapitre 16 « Vecteurs de l'espace »
(1ereC, Maths), scène 03.

§ Vecteurs colinéaires : définition, théorème de l'alignement de 3 points,
théorème du parallélisme de deux droites, théorème « droite définie par un
point et un vecteur directeur ». Exemple résolu 2 : tétraèdre ABCD, I
milieu [AB], J milieu [AC], démontrer (IJ) ∥ (BC) — théorème des milieux
dans l'espace.
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
from shapes.boxes import corrige_box, definition_box, exercise_box, scene_title, theorem_box


# --- Géométrie en perspective cavalière (2D projeté) : tétraèdre -----------

def _tetra_points(names, side=3.4, back=0.9, height=2.6, origin=None):
    """Sommets d'un tétraèdre en perspective cavalière : names = (base
    gauche, base droite, base arrière/cachée, sommet). Le 3e nom est
    l'unique sommet caché (toutes ses arêtes sont en pointillés)."""
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


class VecteursColineairesAlignementParallelisme(NotionScene):
    def construct(self):
        titre = scene_title("Vecteurs colinéaires : alignement et parallélisme")
        titre.scale(0.5)
        titre.to_edge(UP)
        self.play(Write(titre))

        # --- Énoncé : définition --------------------------------------------------
        definition = definition_box(
            VGroup(
                Text("Vecteurs colinéaires", font_size=24, weight="BOLD"),
                MathTex(
                    r"u, v \ \text{colinéaires} \ \iff\ \exists k \in \mathbb{R}, \ v = k \cdot u \ \ (\text{ou } u = \vec 0)",
                    font_size=25,
                ),
            ).arrange(DOWN, buff=0.22),
        )
        definition.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Deux vecteurs u et v de l'espace sont dits colinéaires "
                "lorsqu'il existe un réel k tel que v soit égal à k fois u, "
                "ou lorsque u est le vecteur nul. C'est la même définition "
                "que dans le plan : rien de nouveau ici, mais elle va nous "
                "servir de brique de base pour caractériser alignement et "
                "parallélisme dans l'espace."
            )
        ) as tracker:
            self.play(FadeIn(definition))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(definition))

        # --- Raisonnement : les 3 théorèmes ---------------------------------------
        theo_align = theorem_box(
            VGroup(
                Text("Alignement de trois points", font_size=22, weight="BOLD"),
                MathTex(
                    r"A, B, C \ \text{alignés} \ \iff\ \overrightarrow{AB} \ \text{et} \ \overrightarrow{AC} \ \text{colinéaires}",
                    font_size=24,
                ),
            ).arrange(DOWN, buff=0.2),
        )
        theo_align.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Premier théorème : trois points A, B et C sont alignés si, "
                "et seulement si, les vecteurs A-B et A-C sont colinéaires. "
                "Notez bien qu'ils partagent le même point de départ, A."
            )
        ) as tracker:
            self.play(FadeIn(theo_align))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(theo_align))

        theo_parallel = theorem_box(
            VGroup(
                Text("Parallélisme de deux droites distinctes", font_size=22, weight="BOLD"),
                MathTex(
                    r"(AB) \parallel (CD) \ \iff\ \overrightarrow{AB} \ \text{et} \ \overrightarrow{CD} \ \text{colinéaires}",
                    font_size=24,
                ),
            ).arrange(DOWN, buff=0.2),
        )
        theo_parallel.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Deuxième théorème : deux droites distinctes A-B et C-D "
                "sont parallèles si, et seulement si, les vecteurs A-B et "
                "C-D sont colinéaires — sans exiger cette fois un point "
                "commun entre les deux vecteurs."
            )
        ) as tracker:
            self.play(FadeIn(theo_parallel))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(theo_parallel))

        theo_droite = theorem_box(
            VGroup(
                Text("Droite définie par un point et un vecteur directeur", font_size=21, weight="BOLD"),
                MathTex(
                    r"(d) \ni A, \ \text{de vecteur directeur } u \neq \vec 0 : \quad M \in (d) \ \iff\ \overrightarrow{AM} \ \text{colinéaire à } u",
                    font_size=21,
                ),
            ).arrange(DOWN, buff=0.2),
        )
        theo_droite.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Troisième théorème : une droite d passant par un point A, "
                "de vecteur directeur u non nul, est l'ensemble des points "
                "M tels que le vecteur A-M soit colinéaire à u. C'est cette "
                "caractérisation qui permettra, plus tard, de décrire une "
                "droite par un système d'équations paramétriques."
            )
        ) as tracker:
            self.play(FadeIn(theo_droite))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(theo_droite))

        # --- Exemple résolu 2 : théorème des milieux dans l'espace --------------
        pts = _tetra_points(("B", "C", "D", "A"))
        tetra = _tetra_group(pts, ("B", "C", "D", "A"))
        figure = VGroup(tetra)
        figure.scale(0.8)
        figure.next_to(titre, DOWN, buff=0.3)

        enonce = exercise_box(
            VGroup(
                Text("Exemple résolu 2", font_size=23, weight="BOLD"),
                MathTex(
                    r"ABCD \ \text{tétraèdre}, \quad I \ \text{milieu de } [AB], \quad J \ \text{milieu de } [AC].",
                    font_size=23,
                ),
                MathTex(r"\text{Démontrer que } (IJ) \parallel (BC).", font_size=24),
            ).arrange(DOWN, buff=0.2),
        )
        enonce.next_to(titre, DOWN, buff=0.35)

        with self.voiceover(
            text=(
                "Exemple résolu. A-B-C-D est un tétraèdre. I est le milieu "
                "du segment A-B, J le milieu du segment A-C. On veut "
                "démontrer que la droite I-J est parallèle à la droite "
                "B-C : c'est le théorème des milieux, déjà connu dans le "
                "plan, qui va s'étendre ici sans aucune modification."
            )
        ) as tracker:
            self.play(FadeIn(enonce))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(enonce))
        self.play(FadeIn(figure))

        I = (pts["A"] + pts["B"]) / 2
        J = (pts["A"] + pts["C"]) / 2
        pt_i = VGroup(Dot(I, radius=0.05, color="#DE7C1F"), MathTex("I", font_size=24, color="#DE7C1F").next_to(I, LEFT, buff=0.1))
        pt_j = VGroup(Dot(J, radius=0.05, color="#DE7C1F"), MathTex("J", font_size=24, color="#DE7C1F").next_to(J, RIGHT, buff=0.1))
        pt_i.scale(0.8, about_point=figure.get_center())
        pt_j.scale(0.8, about_point=figure.get_center())
        seg_ij = Line(I, J, color="#288073", stroke_width=4.5).scale(0.8, about_point=figure.get_center())
        seg_bc = Line(pts["B"], pts["C"], color="#1E5FA8", stroke_width=4.5).scale(0.8, about_point=figure.get_center())

        demo = VGroup(
            MathTex(r"\overrightarrow{IJ} = \overrightarrow{AJ} - \overrightarrow{AI} = \tfrac{1}{2}\overrightarrow{AC} - \tfrac{1}{2}\overrightarrow{AB}", font_size=24),
            MathTex(r"= \tfrac{1}{2}\big(\overrightarrow{AC} - \overrightarrow{AB}\big) = \tfrac{1}{2}\,\overrightarrow{BC}", font_size=24),
            MathTex(r"\Longrightarrow\ \overrightarrow{IJ} \ \text{et} \ \overrightarrow{BC} \ \text{colinéaires} \ \Longrightarrow\ (IJ) \parallel (BC)", font_size=25, color=YELLOW),
        ).arrange(DOWN, buff=0.24)
        demo.next_to(titre, DOWN, buff=0.35)

        with self.voiceover(
            text=(
                "Comme I est le milieu de A-B et J le milieu de A-C, le "
                "vecteur A-I vaut la moitié de A-B et le vecteur A-J vaut "
                "la moitié de A-C. Le vecteur I-J, égal à A-J moins A-I, "
                "vaut donc la moitié de A-C moins A-B, c'est-à-dire la "
                "moitié du vecteur B-C. I-J et B-C étant colinéaires, on "
                "conclut que la droite I-J est parallèle à la droite B-C. "
                "Cette démonstration, purement vectorielle, est identique à "
                "celle du plan : c'est tout l'intérêt de la méthode "
                "vectorielle, elle se généralise sans effort."
            )
        ) as tracker:
            self.play(FadeIn(pt_i), FadeIn(pt_j), FadeIn(seg_ij), FadeIn(seg_bc))
            self.play(Write(demo[0]))
            self.play(Write(demo[1]))
            self.play(Write(demo[2]))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(demo), FadeOut(figure), FadeOut(pt_i), FadeOut(pt_j), FadeOut(seg_ij), FadeOut(seg_bc))

        # --- À retenir -----------------------------------------------------------
        retenir = corrige_box(
            VGroup(
                MathTex(r"(IJ) \parallel (BC) \quad \text{et} \quad IJ = \tfrac{1}{2}BC", font_size=26),
                Text(
                    "Le théorème des milieux du plan s'étend tel quel à l'espace : la\n"
                    "démonstration reste purement vectorielle, sans jamais utiliser de coordonnées.",
                    font_size=20,
                ),
            ).arrange(DOWN, buff=0.22),
        )
        retenir.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Retenons deux choses : le résultat, I-J parallèle à B-C "
                "avec I-J égal à la moitié de B-C, et surtout la méthode. "
                "Les théorèmes vectoriels du plan se transportent dans "
                "l'espace sans aucune adaptation, tant qu'on raisonne avec "
                "Chasles et le produit par un réel, sans jamais avoir "
                "besoin de coordonnées."
            )
        ) as tracker:
            self.play(FadeIn(retenir))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(retenir), FadeOut(titre))
