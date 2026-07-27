"""
scenes/Maths_OrthogonaliteEspace_09.py — Chapitre 10 « Orthogonalité dans
l'espace » (1ereC, Maths), scène 09.

§ Propriétés des plans perpendiculaires : plan parallèle à un plan
perpendiculaire (avec démonstration), théorème plan perpendiculaire à deux
plans sécants ssi orthogonal à leur intersection (avec démonstration),
récapitulatif « à retenir » des 3 procédés pour démontrer une
perpendicularité de plans. Exemple résolu 4 complet (prisme droit ABCDEF à
base triangulaire, 3 démonstrations de perpendicularité de plans).
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
from shapes.boxes import example_box, property_box, scene_title, theorem_box, warning_box


# --- Géométrie en perspective cavalière (2D projeté) : prisme droit ---------

def _prism_points(scale=2.4, height=3.0, origin=None):
    """Sommets d'un prisme droit ABCDEF, base triangulaire ABC (bas),
    DEF (haut), arêtes verticales A-D, B-E, C-F. C est le sommet caché de
    la base (arêtes BC, CA en pointillés, ainsi que l'arête verticale CF)."""
    if origin is None:
        origin = DOWN * 0.5
    A = origin + LEFT * scale * 0.75 + DOWN * height / 2
    B = origin + RIGHT * scale * 0.75 + DOWN * height / 2
    C = origin + UP * scale * 0.35 + RIGHT * scale * 0.2 + DOWN * height / 2
    D = A + UP * height
    E = B + UP * height
    F = C + UP * height
    return {"A": A, "B": B, "C": C, "D": D, "E": E, "F": F}


def _prism_group(pts, color=WHITE, label_color=YELLOW, label_font_size=26):
    p = pts
    visible = [("A", "B"), ("A", "D"), ("B", "E"), ("D", "E"), ("E", "F"), ("F", "D")]
    hidden = [("B", "C"), ("C", "A"), ("C", "F")]
    lines = VGroup()
    for u, v in visible:
        lines.add(Line(p[u], p[v], color=color, stroke_width=2.5))
    for u, v in hidden:
        lines.add(DashedLine(p[u], p[v], color=color, stroke_width=2, dash_length=0.09))

    label_dirs = {"A": DOWN + LEFT, "B": DOWN + RIGHT, "C": RIGHT, "D": UP + LEFT, "E": UP + RIGHT, "F": UP}
    labels = VGroup()
    for name, point in p.items():
        dot = Dot(point, radius=0.05, color=label_color)
        lab = MathTex(name, font_size=label_font_size, color=label_color)
        lab.next_to(dot, label_dirs.get(name, UP), buff=0.1)
        labels.add(dot, lab)
    return VGroup(lines, labels)


class ProprietesPlansPerpendiculaires(NotionScene):
    def construct(self):
        titre = scene_title("Propriétés des plans perpendiculaires")
        titre.scale(0.5)
        titre.to_edge(UP)
        self.play(Write(titre))

        # --- Énoncé : propriété 1 (avec démonstration) --------------------------
        prop1 = property_box(
            MathTex(r"P' \parallel P \ \text{et} \ P \perp Q \ \Longrightarrow\ P' \perp Q", font_size=27),
        )
        prop1.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Première propriété : si un plan P prime est parallèle à "
                "un plan P, et que P est perpendiculaire à un plan Q, "
                "alors P prime est aussi perpendiculaire à Q."
            )
        ) as tracker:
            self.play(FadeIn(prop1))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(prop1))

        preuve1 = VGroup(
            MathTex(r"P \perp Q \ \Longrightarrow\ \exists\, d \subset P, \ d \perp Q", font_size=24),
            MathTex(r"P' \parallel P \ \Longrightarrow\ \exists\, d' \subset P', \ d' \parallel d \ \Longrightarrow\ d' \perp Q \ \text{(scène 1)}", font_size=23),
            MathTex(r"d' \subset P' \ \text{et} \ d' \perp Q \ \Longrightarrow\ P' \perp Q", font_size=24, color=YELLOW),
        ).arrange(DOWN, buff=0.28)
        preuve1.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Démonstration : P perpendiculaire à Q signifie qu'il "
                "existe une droite d de P orthogonale à Q. Comme P prime "
                "est parallèle à P, il existe dans P prime une droite d "
                "prime parallèle à d ; par transitivité de l'orthogonalité "
                "par parallélisme, vue à la scène 1, d prime est aussi "
                "orthogonale à Q. Or d prime est incluse dans P prime : "
                "par définition, P prime est donc perpendiculaire à Q."
            )
        ) as tracker:
            self.play(Write(preuve1[0]))
            self.play(Write(preuve1[1]))
            self.play(Write(preuve1[2]))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(preuve1))

        # --- Raisonnement : théorème intersection de 2 plans sécants ------------
        theo2 = theorem_box(
            VGroup(
                Text("Plan perpendiculaire à deux plans sécants", font_size=21, weight="BOLD"),
                MathTex(
                    r"Q \cap R = \Delta \ (\text{sécants}) \ : \quad P \perp Q \ \text{et} \ P \perp R \ \iff\ P \perp \Delta",
                    font_size=22,
                ),
            ).arrange(DOWN, buff=0.2),
        )
        theo2.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Deuxième résultat, très important en pratique. Soient Q "
                "et R deux plans sécants suivant une droite delta. Un plan "
                "P est perpendiculaire à la fois à Q et à R si, et "
                "seulement si, P est orthogonal à leur droite "
                "d'intersection delta."
            )
        ) as tracker:
            self.play(FadeIn(theo2))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(theo2))

        preuve2 = VGroup(
            MathTex(r"(\Leftarrow) \ P \perp \Delta, \ \Delta \subset Q \ \Longrightarrow\ P \perp Q \ ; \ \ \Delta \subset R \ \Longrightarrow\ P \perp R", font_size=22),
            MathTex(r"(\Rightarrow) \ P\perp Q \ \Longrightarrow\ \exists d\subset P, d\perp Q \ \Longrightarrow\ d\perp \Delta \ (\Delta\subset Q)", font_size=21),
            MathTex(r"\text{De même avec } R \ : \ \exists d'' \subset P, \ d'' \perp \Delta \ \Longrightarrow\ P \ \text{contient 2 sécantes} \perp \Delta \ \Longrightarrow\ P \perp \Delta", font_size=19, color=YELLOW),
        ).arrange(DOWN, buff=0.26)
        preuve2.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Le sens facile d'abord : si P est orthogonal à delta, "
                "comme delta est incluse dans Q, P est orthogonal à une "
                "droite de Q, donc P est perpendiculaire à Q ; de même "
                "pour R. Réciproquement, si P est perpendiculaire à Q, il "
                "existe une droite d de P orthogonale à Q, donc orthogonale "
                "en particulier à delta, incluse dans Q. Le même "
                "raisonnement avec R fournit une autre droite de P, "
                "orthogonale à delta. En combinant, P contient deux droites "
                "sécantes orthogonales à delta, donc P est orthogonal à "
                "delta tout entière, d'après le théorème fondamental de la "
                "scène 4."
            )
        ) as tracker:
            self.play(Write(preuve2[0]))
            self.play(Write(preuve2[1]))
            self.play(Write(preuve2[2]))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(preuve2))

        # --- Exemple traité : prisme droit à base triangulaire -------------------
        pts = _prism_points()
        prisme = _prism_group(pts)
        figure = VGroup(prisme)
        figure.scale(0.75)
        figure.next_to(titre, DOWN, buff=0.3)

        enonce_ex = MathTex(
            r"ABCDEF \ \text{prisme DROIT, base triangulaire } ABC \ (\text{sommets } D,E,F \ \text{au-dessus de } A,B,C).",
            font_size=20,
        )
        enonce_ex.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Exemple résolu. A-B-C-D-E-F est un prisme droit, de base "
                "triangulaire A-B-C, les sommets D, E, F étant "
                "respectivement au-dessus de A, B, C. Voyons trois "
                "démonstrations de perpendicularité de plans dans ce "
                "solide."
            )
        ) as tracker:
            self.play(Write(enonce_ex))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(enonce_ex))
        self.play(FadeIn(figure))

        demo_prisme1 = example_box(
            MathTex(
                r"(AD) \perp \text{plan}(ABC) \ (\text{prisme DROIT}) \ \Longrightarrow\ \text{plan}(ADEB) \perp \text{plan}(ABC)",
                font_size=20,
            ),
        )
        demo_prisme1.next_to(titre, DOWN, buff=0.35)

        with self.voiceover(
            text=(
                "Premièrement, le prisme étant droit, l'arête latérale A-D "
                "est orthogonale au plan de base A-B-C. Comme A-D est "
                "incluse dans la face latérale A-D-E-B, cette face est "
                "perpendiculaire au plan de base."
            )
        ) as tracker:
            self.play(FadeIn(demo_prisme1))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(demo_prisme1))

        demo_prisme2 = example_box(
            MathTex(
                r"\text{plan}(ADEB) \cap \text{plan}(ABC) = (AB), \quad \text{plan}(DEF) \parallel \text{plan}(ABC)"
                r"\ \Longrightarrow\ \text{plan}(ADEB) \perp \text{plan}(DEF)",
                font_size=18,
            ),
        )
        demo_prisme2.next_to(titre, DOWN, buff=0.35)

        with self.voiceover(
            text=(
                "Deuxièmement, comme le plan D-E-F, celui de la face "
                "supérieure, est parallèle au plan de base A-B-C, et que "
                "ce dernier est perpendiculaire à la face A-D-E-B, notre "
                "première propriété du jour donne directement : la face "
                "A-D-E-B est aussi perpendiculaire à la face supérieure "
                "D-E-F."
            )
        ) as tracker:
            self.play(FadeIn(demo_prisme2))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(demo_prisme2))

        demo_prisme3 = example_box(
            VGroup(
                MathTex(r"\text{Si } (AB) \perp (AC) : \ (AB) \perp \text{plan}(ACFD) \ \Longrightarrow\ \text{plan}(ADEB) \perp \text{plan}(ACFD)", font_size=18),
            ),
        )
        demo_prisme3.next_to(titre, DOWN, buff=0.35)

        with self.voiceover(
            text=(
                "Troisièmement, si le triangle de base est rectangle en A, "
                "c'est-à-dire si A-B est orthogonale à A-C, alors A-B est "
                "orthogonale à deux droites sécantes du plan A-C-F-D, à "
                "savoir A-C et l'arête verticale A-D, donc A-B est "
                "orthogonale à ce plan tout entier. Comme A-B est incluse "
                "dans la face A-D-E-B, cette face est perpendiculaire à la "
                "face A-C-F-D."
            )
        ) as tracker:
            self.play(FadeIn(demo_prisme3))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(demo_prisme3), FadeOut(figure))

        # --- À retenir : les 3 procédés -------------------------------------------
        retenir = warning_box(
            VGroup(
                Text("À retenir : 3 procédés pour démontrer que 2 plans sont perpendiculaires", font_size=20, weight="BOLD"),
                MathTex(r"\text{1) Montrer qu'un des plans contient une droite orthogonale à l'autre}", font_size=18),
                MathTex(r"\text{2) Montrer que le plan est orthogonal à l'intersection de deux plans sécants}", font_size=18),
                MathTex(r"\text{3) Utiliser un plan parallèle déjà connu comme perpendiculaire (propriété 1)}", font_size=18),
            ).arrange(DOWN, buff=0.2),
        )
        retenir.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Pour conclure, retenons les trois procédés disponibles "
                "pour démontrer que deux plans sont perpendiculaires : "
                "montrer que l'un contient une droite orthogonale à "
                "l'autre, c'est la définition ; montrer que le plan est "
                "orthogonal à l'intersection de deux plans sécants, "
                "c'est notre théorème du jour ; ou bien passer par un plan "
                "parallèle déjà connu comme perpendiculaire."
            )
        ) as tracker:
            self.play(FadeIn(retenir))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(retenir), FadeOut(titre))
