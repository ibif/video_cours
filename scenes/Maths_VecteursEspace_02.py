"""
scenes/Maths_VecteursEspace_02.py — Chapitre 16 « Vecteurs de l'espace »
(1ereC, Maths), scène 02.

§ Produit d'un vecteur par un réel : définition (direction, sens, norme),
propriétés admises (distributivité, associativité). Exemple résolu 1 :
cube ABCDEFGH, i = AB, j = AD, k = AE, exprimer BE et CF en fonction de
i, j, k.
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
from shapes.boxes import corrige_box, definition_box, exercise_box, property_box, scene_title, warning_box


# --- Géométrie en perspective cavalière (2D projeté) : cube -----------------

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


class ProduitVecteurParReel(NotionScene):
    def construct(self):
        titre = scene_title("Produit d'un vecteur par un réel")
        titre.scale(0.55)
        titre.to_edge(UP)
        self.play(Write(titre))

        # --- Énoncé : définition -------------------------------------------------
        definition = definition_box(
            VGroup(
                Text("Produit d'un vecteur par un réel", font_size=24, weight="BOLD"),
                Text(
                    "Pour un vecteur u ≠ 0 et un réel k ≠ 0, le vecteur k·u est le vecteur :",
                    font_size=21,
                ),
                Text(
                    "— de même direction que u  ·  de même sens que u si k>0, sens opposé si k<0\n"
                    "— de norme |k|·‖u‖",
                    font_size=21,
                ),
                MathTex(r"\text{Si } k = 0 \ \text{ou} \ u = \vec 0, \ \text{alors} \ k \cdot u = \vec 0.", font_size=21),
            ).arrange(DOWN, buff=0.2),
        )
        definition.next_to(titre, DOWN, buff=0.35)

        with self.voiceover(
            text=(
                "Comme dans le plan, on peut multiplier un vecteur de "
                "l'espace par un réel. Pour un vecteur u non nul et un réel "
                "k non nul, le vecteur k fois u a la même direction que u, "
                "le même sens si k est positif, le sens opposé si k est "
                "négatif, et une norme égale à la valeur absolue de k fois "
                "la norme de u. Si k est nul ou si u est le vecteur nul, "
                "alors k fois u est le vecteur nul."
            )
        ) as tracker:
            self.play(FadeIn(definition))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(definition))

        # --- Raisonnement : propriétés admises -----------------------------------
        proprietes = property_box(
            VGroup(
                Text("Propriétés (admises), pour tous vecteurs u, v et réels k, k' :", font_size=21, weight="BOLD"),
                MathTex(r"k(u+v) = ku + kv \qquad (k+k')u = ku + k'u", font_size=23),
                MathTex(r"k(k'u) = (kk')u \qquad 1 \cdot u = u \qquad (-1)\cdot u = -u", font_size=23),
            ).arrange(DOWN, buff=0.22),
        )
        proprietes.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Ces propriétés, déjà connues dans le plan, restent admises "
                "telles quelles dans l'espace : distributivité par rapport "
                "à la somme de vecteurs, distributivité par rapport à la "
                "somme de réels, associativité du produit par deux réels "
                "successifs, et les deux cas particuliers un fois u égale "
                "u, et moins un fois u égale l'opposé de u."
            )
        ) as tracker:
            self.play(FadeIn(proprietes))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(proprietes))

        # --- Exemple résolu 1 ------------------------------------------------------
        pts = _cube_points()
        cube = _cube_group(pts)
        figure = VGroup(cube)
        figure.scale(0.78)
        figure.next_to(titre, DOWN, buff=0.3)

        enonce = exercise_box(
            VGroup(
                Text("Exemple résolu 1", font_size=23, weight="BOLD"),
                MathTex(
                    r"ABCDEFGH \ \text{cube}, \quad i = \overrightarrow{AB}, \ j = \overrightarrow{AD}, \ k = \overrightarrow{AE}.",
                    font_size=23,
                ),
                MathTex(
                    r"\text{Exprimer } \overrightarrow{BE} \ \text{et} \ \overrightarrow{CF} \ \text{en fonction de } i, j, k.",
                    font_size=23,
                ),
            ).arrange(DOWN, buff=0.2),
        )
        enonce.next_to(titre, DOWN, buff=0.35)

        with self.voiceover(
            text=(
                "Exemple résolu. A-B-C-D-E-F-G-H est un cube. On pose i "
                "égal au vecteur A-B, j égal au vecteur A-D, et k égal au "
                "vecteur A-E : ces trois vecteurs, portés par les trois "
                "arêtes issues de A, forment une base naturelle du cube. On "
                "veut exprimer les vecteurs B-E et C-F en fonction de i, j "
                "et k."
            )
        ) as tracker:
            self.play(FadeIn(enonce))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(enonce))
        self.play(FadeIn(figure))

        i_vec = Line(pts["A"], pts["B"], color="#DE7C1F", stroke_width=5).scale(0.78, about_point=figure.get_center())
        j_vec = Line(pts["A"], pts["D"], color="#288073", stroke_width=5).scale(0.78, about_point=figure.get_center())
        k_vec = Line(pts["A"], pts["E"], color="#1E5FA8", stroke_width=5).scale(0.78, about_point=figure.get_center())
        be_vec = Line(pts["B"], pts["E"], color="#B42E41", stroke_width=5).scale(0.78, about_point=figure.get_center())
        cf_vec = DashedLine(pts["C"], pts["F"], color="#A42A5A", stroke_width=5, dash_length=0.09).scale(0.78, about_point=figure.get_center())

        with self.voiceover(
            text=(
                "Repérons d'abord les trois vecteurs de base i, j, k en "
                "orange, vert et bleu, puis les deux vecteurs à exprimer, "
                "B-E en rouge et C-F en magenta."
            )
        ) as tracker:
            self.play(FadeIn(i_vec), FadeIn(j_vec), FadeIn(k_vec))
            self.play(FadeIn(be_vec), FadeIn(cf_vec))
            self.wait(tracker.get_remaining_duration())

        etape_be = VGroup(
            MathTex(r"\overrightarrow{BE} = \overrightarrow{BA} + \overrightarrow{AE} \quad \text{(Chasles)}", font_size=24),
            MathTex(r"\overrightarrow{BA} = -\overrightarrow{AB} = -i, \qquad \overrightarrow{AE} = k", font_size=24),
            MathTex(r"\Longrightarrow\ \overrightarrow{BE} = -i + k", font_size=27, color=YELLOW),
        ).arrange(DOWN, buff=0.24)
        etape_be.next_to(titre, DOWN, buff=0.35)

        with self.voiceover(
            text=(
                "Pour B-E, on passe par Chasles via le point A : B-E égale "
                "B-A plus A-E. Or B-A est l'opposé de A-B, donc moins i, et "
                "A-E vaut k. On obtient donc B-E égale moins i plus k."
            )
        ) as tracker:
            self.play(Write(etape_be[0]))
            self.play(Write(etape_be[1]))
            self.play(Write(etape_be[2]))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(etape_be))

        etape_cf = VGroup(
            MathTex(r"\overrightarrow{CF} = \overrightarrow{CB} + \overrightarrow{BF} \quad \text{(Chasles)}", font_size=24),
            MathTex(r"\overrightarrow{CB} = -\overrightarrow{BC} = -\overrightarrow{AD} = -j \quad \text{(} BC = AD, \ ABCD \ \text{carré)}", font_size=22),
            MathTex(r"\overrightarrow{BF} = \overrightarrow{AE} = k \quad \text{(translation verticale identique)}", font_size=22),
            MathTex(r"\Longrightarrow\ \overrightarrow{CF} = -j + k", font_size=27, color=YELLOW),
        ).arrange(DOWN, buff=0.22)
        etape_cf.next_to(titre, DOWN, buff=0.35)

        with self.voiceover(
            text=(
                "Pour C-F, on passe par B : C-F égale C-B plus B-F. C-B est "
                "l'opposé de B-C, qui est égal à A-D puisque A-B-C-D est un "
                "carré, donc C-B égale moins j. Et B-F est la même "
                "translation verticale que A-E, donc B-F égale k. On "
                "obtient donc C-F égale moins j plus k."
            )
        ) as tracker:
            self.play(Write(etape_cf[0]))
            self.play(Write(etape_cf[1]))
            self.play(Write(etape_cf[2]))
            self.play(Write(etape_cf[3]))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(etape_cf), FadeOut(figure), FadeOut(i_vec), FadeOut(j_vec), FadeOut(k_vec), FadeOut(be_vec), FadeOut(cf_vec))

        # --- À retenir -----------------------------------------------------------
        retenir = corrige_box(
            MathTex(
                r"\overrightarrow{BE} = -i + k \qquad \overrightarrow{CF} = -j + k",
                font_size=27,
            ),
        )
        retenir.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Résultat à retenir : B-E égale moins i plus k, et C-F "
                "égale moins j plus k. La méthode générale, elle, est "
                "encore plus importante que le résultat : passer "
                "systématiquement par Chasles via un sommet du cube où l'on "
                "connaît déjà les vecteurs, ici A."
            )
        ) as tracker:
            self.play(FadeIn(retenir))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(retenir))

        # --- Piège à éviter --------------------------------------------------------
        piege = warning_box(
            Text(
                "Le produit k·u ne change JAMAIS la direction de u : k·u et u sont\n"
                "toujours colinéaires, quel que soit le réel k (nul ou non).",
                font_size=22,
            ),
        )
        piege.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Attention à un piège fréquent : multiplier un vecteur par "
                "un réel ne change jamais sa direction. Le vecteur k fois u "
                "reste toujours colinéaire à u, que k soit positif, négatif "
                "ou nul. C'est cette propriété qui va nous servir de base "
                "pour définir la colinéarité, dès la scène suivante."
            )
        ) as tracker:
            self.play(FadeIn(piege))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(piege), FadeOut(titre))
