"""
scenes/Maths_OrthogonaliteEspace_10.py — Chapitre 10 « Orthogonalité dans
l'espace » (1ereC, Maths), scène 10 (dernière scène du chapitre).

§ Applications aux solides usuels : tableau des configurations remarquables
(cube, pavé droit, tétraèdre régulier, pyramide à base carrée, prisme
droit/cylindre). Exemple résolu 5 (pyramide SABCD, base carrée de centre O,
(SO) ⟂ (ABCD), démontrer (BD) ⟂ (SA)). 6 method_box (méthodes du chapitre),
3 warning_box (pièges du chapitre), essentiel_box récapitulatif final.
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
from shapes.boxes import essentiel_box, example_box, method_box, scene_title, warning_box


# --- Géométrie en perspective cavalière (2D projeté) : pyramide S-ABCD -----

def _pyramide_points(side=3.0, depth_x=1.0, depth_y=0.65, height=2.6, origin=None):
    if origin is None:
        origin = DOWN * 0.6
    depth = RIGHT * depth_x + UP * depth_y
    A = origin + LEFT * side / 2 + DOWN * side / 2
    B = A + RIGHT * side
    D = A + depth
    C = B + depth
    O = (A + C) / 2
    S = O + UP * height
    return {"A": A, "B": B, "C": C, "D": D, "O": O, "S": S}


def _pyramide_group(pts, color=WHITE, label_color=YELLOW, label_font_size=26):
    p = pts
    visible = [("A", "B"), ("B", "C"), ("S", "A"), ("S", "B"), ("S", "C")]
    hidden = [("A", "D"), ("D", "C"), ("S", "D"), ("S", "O")]
    lines = VGroup()
    for u, v in visible:
        lines.add(Line(p[u], p[v], color=color, stroke_width=2.5))
    for u, v in hidden:
        lines.add(DashedLine(p[u], p[v], color=color, stroke_width=2, dash_length=0.09))

    label_dirs = {"A": DOWN + LEFT, "B": DOWN + RIGHT, "C": RIGHT, "D": LEFT, "S": UP, "O": DOWN}
    labels = VGroup()
    for name, point in p.items():
        dot = Dot(point, radius=0.045, color=label_color)
        lab = MathTex(name, font_size=label_font_size, color=label_color)
        lab.next_to(dot, label_dirs.get(name, UP), buff=0.08)
        labels.add(dot, lab)
    return VGroup(lines, labels)


class ApplicationsSolidesUsuelsSynthese(NotionScene):
    def construct(self):
        titre = scene_title("Applications aux solides usuels — synthèse")
        titre.scale(0.48)
        titre.to_edge(UP)
        self.play(Write(titre))

        # --- Énoncé : tableau des configurations remarquables --------------------
        lignes = VGroup(
            Text("Cube / pavé droit : chaque arête est orthogonale aux 2 faces qu'elle ne touche pas", font_size=19),
            Text("Tétraèdre régulier : arêtes opposées orthogonales deux à deux", font_size=19),
            Text("Pyramide à base carrée régulière : (sommet–centre) ⟂ plan de base", font_size=19),
            Text("Prisme droit / cylindre : arêtes (ou axe) latérales ⟂ aux 2 bases", font_size=19),
        ).arrange(DOWN, buff=0.28, aligned_edge=LEFT)
        tableau = example_box(lignes)
        tableau.next_to(titre, DOWN, buff=0.35)

        with self.voiceover(
            text=(
                "Récapitulons les configurations d'orthogonalité "
                "remarquables des solides usuels du programme. Dans un "
                "cube ou un pavé droit, chaque arête est orthogonale aux "
                "deux faces qu'elle ne touche pas. Dans un tétraèdre "
                "régulier, les arêtes opposées sont orthogonales deux à "
                "deux, comme nous l'avons démontré à la scène 4. Dans une "
                "pyramide à base carrée régulière, la droite reliant le "
                "sommet au centre de la base est orthogonale au plan de "
                "base. Et dans un prisme droit ou un cylindre, les arêtes "
                "latérales, ou l'axe, sont orthogonales aux deux bases."
            )
        ) as tracker:
            self.play(FadeIn(tableau))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(tableau))

        # --- Raisonnement / exemple traité : pyramide SABCD -----------------------
        pts = _pyramide_points()
        pyramide = _pyramide_group(pts)
        figure = VGroup(pyramide)
        figure.scale(0.72)
        figure.next_to(titre, DOWN, buff=0.3)

        enonce_ex = MathTex(
            r"SABCD \ \text{pyramide, base carrée } ABCD \ \text{de centre } O, \ (SO) \perp \text{plan}(ABCD)."
            r"\ \text{Démontrer } (BD) \perp (SA).",
            font_size=19,
        )
        enonce_ex.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Exemple résolu 5, pour terminer. S-A-B-C-D est une "
                "pyramide dont la base A-B-C-D est un carré de centre O, "
                "et la droite S-O est orthogonale au plan de base. On veut "
                "démontrer que la diagonale B-D est orthogonale à l'arête "
                "S-A."
            )
        ) as tracker:
            self.play(Write(enonce_ex))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(enonce_ex))
        self.play(FadeIn(figure))

        demo_pyramide = example_box(
            VGroup(
                MathTex(r"(BD) \perp (AC) \ \text{(diagonales du carré)}, \quad (BD) \perp (SO) \ \text{(} SO \perp \text{base)}", font_size=19),
                MathTex(r"(AC) \cap (SO) = \{O\} \ \Longrightarrow\ (BD) \perp \text{plan}(SAC)", font_size=21),
                MathTex(r"(SA) \subset \text{plan}(SAC) \ \Longrightarrow\ (BD) \perp (SA)", font_size=22, color=YELLOW),
            ).arrange(DOWN, buff=0.24),
        )
        demo_pyramide.next_to(titre, DOWN, buff=0.35)

        with self.voiceover(
            text=(
                "B-D est orthogonale à A-C, car ce sont les diagonales du "
                "carré de base, et B-D est orthogonale à S-O, puisque S-O "
                "est orthogonale à tout le plan de base. A-C et S-O sont "
                "sécantes en O : donc B-D est orthogonale au plan S-A-C "
                "tout entier. Comme S-A appartient à ce plan, on conclut "
                "que B-D est orthogonale à S-A."
            )
        ) as tracker:
            self.play(FadeIn(demo_pyramide))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(demo_pyramide), FadeOut(figure))

        # --- À retenir : les 6 méthodes du chapitre --------------------------------
        methodes_txt = [
            r"\text{Démontrer } d\perp d' \ : \ \text{trouver un triangle équilatéral/isocèle (médiane=hauteur), ou une droite des milieux}",
            r"\text{Démontrer } d \perp P \ : \ \text{trouver 2 droites SÉCANTES de } P, \ \text{chacune orthogonale à } d",
            r"\text{Démontrer } P \perp Q \ : \ \text{un plan contient une droite} \perp \text{à l'autre, ou orthogonal à leur intersection}",
            r"\text{Calculer } d(A,P) \ : \ \text{identifier le projeté orthogonal } H \ \text{de } A \ \text{sur } P, \ \text{puis } d(A,P)=AH",
            r"\text{Démontrer un parallélisme} \ : \ \text{via l'orthogonalité à un même plan (droites) ou une même droite (plans)}",
            r"\text{Raisonnement par l'absurde} \ : \ \text{supposer le contraire, aboutir à une contradiction (ex. angle} \neq 90°)",
        ]
        for i, txt in enumerate(methodes_txt, start=1):
            meth = method_box(MathTex(txt, font_size=19))
            meth.next_to(titre, DOWN, buff=0.4)
            with self.voiceover(text=f"Méthode {i}. " + self._methode_narration(i)) as tracker:
                self.play(FadeIn(meth))
                self.wait(tracker.get_remaining_duration())
            self.play(FadeOut(meth))

        # --- Pièges à éviter : les 3 pièges du chapitre ----------------------------
        piege1 = warning_box(
            Text(
                "Piège 1 : deux droites PARALLÈLES d'un plan ne suffisent jamais à prouver\n"
                "qu'une droite est orthogonale à ce plan — il faut deux droites SÉCANTES.",
                font_size=20,
            ),
        )
        piege1.next_to(titre, DOWN, buff=0.45)

        with self.voiceover(
            text=(
                "Premier piège à ne jamais oublier : deux droites "
                "parallèles d'un plan ne suffisent jamais à prouver "
                "qu'une droite est orthogonale à ce plan. Il faut "
                "impérativement deux droites sécantes."
            )
        ) as tracker:
            self.play(FadeIn(piege1))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(piege1))

        piege2 = warning_box(
            Text(
                "Piège 2 : ne pas confondre ORTHOGONALES (angle droit, éventuellement gauches)\n"
                "et PERPENDICULAIRES (orthogonales ET coplanaires, donc sécantes).",
                font_size=20,
            ),
        )
        piege2.next_to(titre, DOWN, buff=0.45)

        with self.voiceover(
            text=(
                "Deuxième piège : ne confondez jamais orthogonales et "
                "perpendiculaires. Deux droites orthogonales peuvent être "
                "gauches, sans jamais se couper ; deux droites "
                "perpendiculaires sont orthogonales ET coplanaires, donc "
                "sécantes."
            )
        ) as tracker:
            self.play(FadeIn(piege2))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(piege2))

        piege3 = warning_box(
            VGroup(
                Text(
                    "Piège 3 : deux droites (ou deux plans) orthogonaux à un même TROISIÈME\n"
                    "objet ne sont PAS forcément parallèles entre eux…",
                    font_size=20,
                ),
                MathTex(
                    r"\text{SAUF cas particulier} \ : \ d\perp P, d'\perp P \Rightarrow d\parallel d' "
                    r"\quad \text{et} \quad P\perp d, P'\perp d \Rightarrow P\parallel P'",
                    font_size=17,
                ),
            ).arrange(DOWN, buff=0.18),
        )
        piege3.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Troisième piège, le plus subtil : deux droites, ou deux "
                "plans, orthogonaux à un même troisième objet ne sont pas "
                "forcément parallèles entre eux — sauf dans un cas précis, "
                "vu à la scène 5 : si ce troisième objet est un PLAN pour "
                "deux droites, ou une DROITE pour deux plans, alors le "
                "parallélisme est garanti. Mais si ce troisième objet est "
                "une simple droite pour deux droites, ou un simple plan "
                "pour deux plans, aucune conclusion n'est possible."
            )
        ) as tracker:
            self.play(FadeIn(piege3))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(piege3))

        # --- L'essentiel à retenir --------------------------------------------------
        essentiel = essentiel_box(
            VGroup(
                Text("Orthogonalité dans l'espace — l'essentiel", font_size=22, weight="BOLD"),
                MathTex(r"\text{orthogonales (éventuellement gauches)} \ \supsetneq \ \text{perpendiculaires (coplanaires, sécantes)}", font_size=17),
                MathTex(r"d\perp P \iff d \ \text{orthogonale à 2 droites SÉCANTES de } P", font_size=20),
                MathTex(r"H=\text{projeté de } A \ \text{sur } P \ \Longrightarrow\ d(A,P)=AH \le AM, \ \forall M \in P", font_size=20),
                MathTex(r"P\perp Q \iff P \ \text{contient une droite} \perp Q \iff P \perp (Q\cap R) \ \text{si} \ P\perp Q \ \text{et} \ P\perp R", font_size=17),
            ).arrange(DOWN, buff=0.2),
        )
        essentiel.next_to(titre, DOWN, buff=0.35)

        with self.voiceover(
            text=(
                "Pour conclure ce chapitre, l'essentiel à retenir. "
                "L'orthogonalité, éventuellement entre droites gauches, "
                "est une notion plus large que la perpendicularité, "
                "réservée aux droites coplanaires et sécantes. Une droite "
                "est orthogonale à un plan si, et seulement si, elle est "
                "orthogonale à deux droites sécantes de ce plan. Le "
                "projeté orthogonal H d'un point A sur un plan P donne la "
                "distance de A à P, et c'est toujours la plus courte. "
                "Enfin, deux plans sont perpendiculaires si l'un contient "
                "une droite orthogonale à l'autre, ou, de façon "
                "équivalente, s'ils sont chacun orthogonaux à leur droite "
                "d'intersection avec un troisième plan sécant aux deux. "
                "Toutes ces notions, combinées, permettent de résoudre la "
                "quasi-totalité des exercices de géométrie dans l'espace "
                "au programme."
            )
        ) as tracker:
            self.play(FadeIn(essentiel))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(essentiel), FadeOut(titre))

    @staticmethod
    def _methode_narration(i: int) -> str:
        textes = {
            1: (
                "Pour démontrer que deux droites sont orthogonales, on "
                "cherche souvent un triangle équilatéral ou isocèle où "
                "médiane et hauteur coïncident, ou une droite des milieux "
                "parallèle à une direction connue."
            ),
            2: (
                "Pour démontrer qu'une droite est orthogonale à un plan, "
                "on cherche deux droites sécantes du plan, chacune "
                "orthogonale à la droite étudiée — jamais deux droites "
                "parallèles."
            ),
            3: (
                "Pour démontrer que deux plans sont perpendiculaires, on "
                "montre que l'un contient une droite orthogonale à "
                "l'autre, ou qu'il est orthogonal à leur droite "
                "d'intersection avec un troisième plan sécant aux deux."
            ),
            4: (
                "Pour calculer une distance d'un point à un plan, on "
                "identifie le projeté orthogonal H de ce point sur le "
                "plan, puis on calcule la longueur A-H, souvent via "
                "Pythagore."
            ),
            5: (
                "Pour démontrer un parallélisme, on peut montrer que deux "
                "droites sont orthogonales à un même plan, ou que deux "
                "plans sont orthogonaux à une même droite."
            ),
            6: (
                "Enfin, le raisonnement par l'absurde reste utile : on "
                "suppose que deux objets ne sont pas orthogonaux, on en "
                "déduit une contradiction avec les données de l'énoncé, "
                "ce qui prouve qu'ils le sont bien."
            ),
        }
        return textes[i]
