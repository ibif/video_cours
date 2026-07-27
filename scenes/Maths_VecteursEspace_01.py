"""
scenes/Maths_VecteursEspace_01.py — Chapitre 16 « Vecteurs de l'espace »
(1ereC, Maths), scène 01.

§ Vecteur de l'espace, égalité de deux vecteurs (ABDC parallélogramme),
somme de deux vecteurs (relation de Chasles), règle du parallélogramme et
règle du parallélépipède (AG = AB + AD + AE, avec démonstration), illustrées
sur un parallélépipède ABCDEFGH en perspective cavalière.
Source : 1ereC/Maths.pdf, pages 189-199.
"""

from manim import (
    DOWN,
    LEFT,
    RIGHT,
    UP,
    WHITE,
    YELLOW,
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


# --- Géométrie en perspective cavalière (2D projeté) : parallélépipède -----

def _pave_points(width=3.6, elev=2.1, depth_x=0.95, depth_y=0.6, origin=None):
    """Sommets d'un parallélépipède ABCDEFGH (pas un cube, arêtes de
    longueurs différentes) en perspective cavalière. Base ABCD (bas), face
    EFGH (haut) obtenue par translation verticale. D (et H) sont les seuls
    sommets cachés : arêtes AD, DC, DH en pointillés.
    """
    if origin is None:
        origin = DOWN * 0.4
    depth = RIGHT * depth_x + UP * depth_y
    A = origin + LEFT * width / 2 + DOWN * elev / 2
    B = A + RIGHT * width
    D = A + depth
    C = B + depth
    E = A + UP * elev
    F = B + UP * elev
    H = D + UP * elev
    G = C + UP * elev
    return {"A": A, "B": B, "C": C, "D": D, "E": E, "F": F, "G": G, "H": H}


def _pave_group(pts, color=WHITE, label_color=YELLOW, label_font_size=26):
    from manim import DashedLine

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


class VecteurEgaliteSommeChasles(NotionScene):
    def construct(self):
        titre = scene_title("Vecteur de l'espace, égalité, somme")
        titre.scale(0.55)
        titre.to_edge(UP)

        pts = _pave_points()
        pave = _pave_group(pts)
        pave.scale(0.85)
        pave.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Dans le plan, un vecteur A-B est associé à la translation "
                "qui envoie A sur B, et sa norme est la distance A-B. Cette "
                "notion s'étend telle quelle à l'espace : rien ne change "
                "dans la définition, seule la figure devient "
                "tridimensionnelle. Voici un parallélépipède "
                "A-B-C-D-E-F-G-H, qui va nous servir de fil conducteur pour "
                "toute cette scène."
            )
        ) as tracker:
            self.play(Write(titre))
            self.play(FadeIn(pave))
            self.wait(tracker.get_remaining_duration())

        # --- Énoncé : définition du vecteur et de son égalité ------------------
        def_vecteur = definition_box(
            VGroup(
                Text("Vecteur de l'espace", font_size=24, weight="BOLD"),
                MathTex(
                    r"\overrightarrow{AB} \ \text{: vecteur associé à la translation qui envoie } A \ \text{sur } B, \quad \|\overrightarrow{AB}\| = AB",
                    font_size=23,
                ),
                Text("Égalité de deux vecteurs :", font_size=22),
                MathTex(
                    r"\overrightarrow{AB} = \overrightarrow{CD} \ \iff\ ABDC \ \text{parallélogramme (éventuellement aplati)}",
                    font_size=23,
                ),
            ).arrange(DOWN, buff=0.22),
        )
        def_vecteur.next_to(titre, DOWN, buff=0.35)

        with self.voiceover(
            text=(
                "Premier rappel : le vecteur A-B est associé à la "
                "translation qui envoie A sur B, et sa norme vaut la "
                "distance A-B. Deux vecteurs A-B et C-D sont égaux si, et "
                "seulement si, A-B-D-C, dans cet ordre, forme un "
                "parallélogramme, éventuellement aplati si les quatre "
                "points sont alignés."
            )
        ) as tracker:
            self.play(FadeOut(pave))
            self.play(FadeIn(def_vecteur))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(def_vecteur))

        # --- Raisonnement : somme de deux vecteurs, relation de Chasles --------
        def_somme = definition_box(
            VGroup(
                Text("Somme de deux vecteurs — relation de Chasles", font_size=24, weight="BOLD"),
                MathTex(
                    r"\text{Quels que soient les points } A, B, C \ \text{de l'espace :} \quad \overrightarrow{AB} + \overrightarrow{BC} = \overrightarrow{AC}",
                    font_size=25,
                ),
                Text(
                    "Comme dans le plan, cette relation reste valable dans l'espace,\n"
                    "quels que soient les points choisis.",
                    font_size=20,
                ),
            ).arrange(DOWN, buff=0.22),
        )
        def_somme.next_to(titre, DOWN, buff=0.35)

        with self.voiceover(
            text=(
                "La somme de deux vecteurs se définit exactement comme dans "
                "le plan, via la relation de Chasles : quels que soient les "
                "points A, B et C de l'espace, le vecteur A-B plus le "
                "vecteur B-C est égal au vecteur A-C. Ce théorème, admis "
                "depuis le plan, reste vrai sans aucune restriction dans "
                "l'espace."
            )
        ) as tracker:
            self.play(FadeIn(def_somme))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(def_somme))

        # --- Règle du parallélogramme -------------------------------------------
        regle_paral = property_box(
            MathTex(
                r"ABCD \ \text{parallélogramme} \ \Longrightarrow\ \overrightarrow{AB} + \overrightarrow{AD} = \overrightarrow{AC}",
                font_size=27,
            ),
        )
        regle_paral.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Conséquence directe : la règle du parallélogramme. Si "
                "A-B-C-D est un parallélogramme, alors le vecteur A-B plus "
                "le vecteur A-D est égal au vecteur A-C, la grande "
                "diagonale."
            )
        ) as tracker:
            self.play(FadeIn(regle_paral))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(regle_paral))

        # --- Règle du parallélépipède, avec démonstration -----------------------
        regle_pave = theorem_box(
            VGroup(
                Text("Règle du parallélépipède", font_size=24, weight="BOLD"),
                MathTex(
                    r"ABCDEFGH \ \text{parallélépipède} \ \Longrightarrow\ \overrightarrow{AG} = \overrightarrow{AB} + \overrightarrow{AD} + \overrightarrow{AE}",
                    font_size=25,
                ),
            ).arrange(DOWN, buff=0.22),
        )
        regle_pave.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Généralisons à trois dimensions : dans un parallélépipède "
                "A-B-C-D-E-F-G-H, le vecteur A-G, c'est-à-dire la grande "
                "diagonale reliant deux sommets opposés, est égal à la "
                "somme des trois vecteurs A-B, A-D et A-E, portés par les "
                "trois arêtes issues de A. C'est la règle du "
                "parallélépipède."
            )
        ) as tracker:
            self.play(FadeIn(regle_pave))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(regle_pave))
        self.play(FadeIn(pave))

        diag_ag = Line(pts["A"], pts["G"], color="#B42E41", stroke_width=5)
        diag_ag.scale(0.85, about_point=pave.get_center())
        arete_ab = Line(pts["A"], pts["B"], color="#DE7C1F", stroke_width=5)
        arete_ad = Line(pts["A"], pts["D"], color="#288073", stroke_width=5)
        arete_ae = Line(pts["A"], pts["E"], color="#1E5FA8", stroke_width=5)
        for l in (arete_ab, arete_ad, arete_ae):
            l.scale(0.85, about_point=pave.get_center())

        demo = VGroup(
            MathTex(r"\overrightarrow{AG} = \overrightarrow{AC} + \overrightarrow{CG} \quad \text{(Chasles)}", font_size=23),
            MathTex(r"\overrightarrow{AC} = \overrightarrow{AB} + \overrightarrow{BC} \quad \text{(Chasles dans la base } ABCD \text{)}", font_size=23),
            MathTex(r"\overrightarrow{BC} = \overrightarrow{AD} \quad \text{(} ABCD \ \text{parallélogramme)}, \qquad \overrightarrow{CG} = \overrightarrow{AE} \quad \text{(translation verticale)}", font_size=20),
            MathTex(r"\Longrightarrow\ \overrightarrow{AG} = \overrightarrow{AB} + \overrightarrow{AD} + \overrightarrow{AE}", font_size=27, color=YELLOW),
        ).arrange(DOWN, buff=0.22)
        demo.next_to(titre, DOWN, buff=0.35)

        with self.voiceover(
            text=(
                "Voici la démonstration. Par la relation de Chasles, "
                "A-G est égal à A-C plus C-G. Toujours par Chasles, dans la "
                "base A-B-C-D, A-C est égal à A-B plus B-C. Or B-C est égal "
                "à A-D, car A-B-C-D est un parallélogramme ; et C-G est "
                "égal à A-E, car c'est une translation verticale identique "
                "à celle qui envoie A sur E. En combinant tout cela, on "
                "obtient bien A-G égal A-B plus A-D plus A-E."
            )
        ) as tracker:
            self.play(FadeOut(pave), FadeIn(VGroup(diag_ag, arete_ab, arete_ad, arete_ae)))
            self.play(Write(demo[0]))
            self.play(Write(demo[1]))
            self.play(Write(demo[2]))
            self.play(Write(demo[3]))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(demo), FadeOut(diag_ag), FadeOut(arete_ab), FadeOut(arete_ad), FadeOut(arete_ae))

        # --- À retenir -----------------------------------------------------------
        retenir = property_box(
            VGroup(
                Text("À retenir", font_size=24, weight="BOLD"),
                MathTex(r"\overrightarrow{AB} = \overrightarrow{CD} \iff ABDC \ \text{parallélogramme}", font_size=23),
                MathTex(r"\overrightarrow{AB} + \overrightarrow{BC} = \overrightarrow{AC} \quad \text{(Chasles, toujours valable)}", font_size=23),
                MathTex(r"\overrightarrow{AG} = \overrightarrow{AB} + \overrightarrow{AD} + \overrightarrow{AE} \quad \text{(parallélépipède)}", font_size=23),
            ).arrange(DOWN, buff=0.2),
        )
        retenir.next_to(titre, DOWN, buff=0.35)

        with self.voiceover(
            text=(
                "Retenons l'essentiel : l'égalité de deux vecteurs se lit "
                "sur un parallélogramme, la relation de Chasles reste "
                "valable sans restriction, et la règle du parallélépipède "
                "permet d'exprimer la grande diagonale comme somme des "
                "trois arêtes issues d'un même sommet — un outil que nous "
                "réutiliserons très souvent dans ce chapitre."
            )
        ) as tracker:
            self.play(FadeIn(retenir))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(retenir), FadeOut(titre))
