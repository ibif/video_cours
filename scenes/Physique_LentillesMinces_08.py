"""
scenes/Physique_LentillesMinces_08.py — Chapitre 13 « Les lentilles minces »
(1ereC, Physique), scène 08.

§ Conventions de signes (sens positif = sens de propagation de la
lumière, objet réel : OA < 0, image réelle : OA' > 0, image virtuelle :
OA' < 0) et formule de conjugaison de Descartes, AVEC démonstration
complète (triangles semblables OAB/OA'B' et F'A'B'/F'OJ, relation de
Chasles F'A' = F'O + OA').
Piège : ne jamais injecter une distance positive à la place d'une mesure
algébrique.
Source : 1ereC/Physique.pdf, pages 130-140 (chapitre 13, § 4).
"""

import textwrap

from manim import (
    DOWN,
    LEFT,
    ORIGIN,
    RIGHT,
    UP,
    WHITE,
    YELLOW,
    GREEN,
    RED,
    Arrow,
    Create,
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
from shapes.boxes import definition_box, essentiel_box, scene_title, theorem_box, warning_box


def _wrap(text: str, width: int = 56) -> str:
    return "\n".join(textwrap.fill(line, width=width) for line in text.split("\n"))


def _lens_symbol(convergente: bool = True, height: float = 3.0, color=WHITE) -> VGroup:
    half = height / 2
    if convergente:
        haut = Arrow(ORIGIN, UP * half, buff=0, stroke_width=4, color=color)
        bas = Arrow(ORIGIN, DOWN * half, buff=0, stroke_width=4, color=color)
        return VGroup(haut, bas)
    inner = half * 0.5
    axe = Line(UP * inner, DOWN * inner, color=color, stroke_width=4)
    haut = Arrow(UP * half, UP * inner, buff=0, stroke_width=4, color=color)
    bas = Arrow(DOWN * half, DOWN * inner, buff=0, stroke_width=4, color=color)
    return VGroup(axe, haut, bas)


class ConventionsSignesFormuleDescartes(NotionScene):
    def construct(self):
        titre = scene_title("Conventions de signes et formule de Descartes")
        titre.scale(0.4)
        titre.to_edge(UP)
        self.play(Write(titre))

        # --- Énoncé : conventions de signes ------------------------------------------
        conventions = definition_box(
            VGroup(
                Text("Conventions de signes", font_size=22, weight="BOLD"),
                Text("Sens positif = sens de propagation de la lumière", font_size=19),
                Text("(convention : de gauche à droite).", font_size=19),
                MathTex(r"\text{objet réel : } \overline{OA} < 0", font_size=23),
                MathTex(r"\text{image réelle : } \overline{OA'} > 0", font_size=23),
                MathTex(r"\text{image virtuelle : } \overline{OA'} < 0", font_size=23),
            ).arrange(DOWN, buff=0.16),
            box_width=10.4,
        )
        conventions.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Avant d'écrire la formule de conjugaison, fixons les "
                "conventions de signes. Le sens positif est le sens de "
                "propagation de la lumière, de gauche à droite. Un objet "
                "réel a une mesure algébrique O A négative. Une image "
                "réelle a une mesure algébrique O A prime positive. Une "
                "image virtuelle a une mesure algébrique O A prime "
                "négative."
            )
        ) as tracker:
            self.play(FadeIn(conventions))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(conventions))

        # --- Raisonnement : démonstration de la formule de Descartes -----------------
        f = 1.5
        axe = Line(LEFT * 4.6, RIGHT * 4.6, color=WHITE, stroke_width=1.5)
        lentille = _lens_symbol(True, height=2.6)
        O = Dot(ORIGIN, color=WHITE, radius=0.05)
        label_O = MathTex("O", font_size=20).next_to(O, DOWN, buff=0.08)
        Fp = Dot(RIGHT * f, color=YELLOW, radius=0.05)
        label_Fp = MathTex("F'", font_size=20, color=YELLOW).next_to(Fp, DOWN, buff=0.08)

        A = LEFT * 3.0
        B = LEFT * 3.0 + UP * 1.1
        objet = Arrow(A, B, buff=0, color=WHITE, stroke_width=2.5)
        label_B = Text("B", font_size=16).next_to(B, UP, buff=0.05)

        r1a = Line(B, UP * 1.1, color=GREEN, stroke_width=2.2)
        # J = point d'intersection du rayon (1) avec le plan de la lentille = (0, 1.1)
        J_point = UP * 1.1
        J = Dot(J_point, color=GREEN, radius=0.035)
        label_J = MathTex("J", font_size=18, color=GREEN).next_to(J, UP, buff=0.05)
        r1b_dir = Fp.get_center() - J_point  # direction J → F' → au-delà (rayon émergent réel)
        r1b = Line(J_point, Fp.get_center() + r1b_dir * 1.6, color=GREEN, stroke_width=2.2)

        r2 = Line(B, B + (ORIGIN - B) * 2.3, color=RED, stroke_width=2.2)

        # Intersection r1b/r2 = image B'
        pente_r1 = r1b_dir[1] / r1b_dir[0]
        pente_r2 = (0 - B[1]) / (0 - B[0])
        x_bp = 1.1 / (pente_r2 - pente_r1)
        y_bp = pente_r2 * x_bp
        Bp = RIGHT * x_bp + UP * y_bp
        Ap = RIGHT * x_bp
        image = Arrow(Ap, Bp, buff=0, color=YELLOW, stroke_width=2.5)
        label_Bp = MathTex("B'", font_size=16, color=YELLOW).next_to(Bp, DOWN, buff=0.05)

        groupe = VGroup(
            axe, lentille, O, label_O, Fp, label_Fp, objet, label_B,
            r1a, r1b, r2, J, label_J, image, label_Bp,
        )
        groupe.scale(0.95).move_to(ORIGIN).next_to(titre, DOWN, buff=0.5)

        demonstration = VGroup(
            Text("Triangles semblables OAB et OA'B' :", font_size=17),
            MathTex(r"\dfrac{\overline{OA'}}{\overline{OA}} = \dfrac{\overline{A'B'}}{\overline{AB}}", font_size=22),
            Text("Triangles semblables F'A'B' et F'OJ (avec OJ = AB) :", font_size=17),
            MathTex(r"\dfrac{\overline{F'A'}}{\overline{F'O}} = \dfrac{\overline{A'B'}}{\overline{OJ}} = \dfrac{\overline{A'B'}}{\overline{AB}}", font_size=22),
            Text("Donc, avec Chasles F'A' = F'O + OA' :", font_size=17),
            MathTex(r"\dfrac{\overline{OA'}}{\overline{OA}} = \dfrac{\overline{F'O}+\overline{OA'}}{\overline{F'O}}", font_size=22),
        ).arrange(DOWN, buff=0.14)
        demonstration.next_to(groupe, DOWN, buff=0.3)

        with self.voiceover(
            text=(
                "Démontrons la formule de conjugaison. Les triangles O A "
                "B et O A prime B prime sont semblables : le rapport O A "
                "prime sur O A égale le rapport A prime B prime sur A B. "
                "D'autre part, les triangles F prime A prime B prime et F "
                "prime O J, où J est le point du rayon parallèle situé "
                "dans le plan de la lentille, avec O J égale A B, sont "
                "également semblables : le rapport F prime A prime sur F "
                "prime O égale ce même rapport A prime B prime sur A B. "
                "En combinant ces deux égalités, puis en utilisant la "
                "relation de Chasles F prime A prime égale F prime O plus "
                "O A prime, on obtient O A prime sur O A égale F prime O "
                "plus O A prime, le tout divisé par F prime O."
            )
        ) as tracker:
            self.play(Create(axe), Create(lentille))
            self.play(FadeIn(O), Write(label_O), FadeIn(Fp), Write(label_Fp))
            self.play(Create(objet), Write(label_B))
            self.play(Create(r1a), FadeIn(J), Write(label_J))
            self.play(Create(r1b))
            self.play(Create(r2))
            self.play(Create(image), Write(label_Bp))
            self.play(Write(demonstration))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(groupe), FadeOut(demonstration))

        # --- Théorème : formule de Descartes ------------------------------------------
        descartes = theorem_box(
            VGroup(
                Text("Formule de conjugaison de Descartes", font_size=22, weight="BOLD"),
                MathTex(
                    r"\dfrac{1}{\overline{OA'}} - \dfrac{1}{\overline{OA}} = \dfrac{1}{\overline{OF'}} = \dfrac{1}{f'} = C",
                    font_size=30,
                    color=YELLOW,
                ),
                Text("(origine des distances : le centre optique O)", font_size=18),
            ).arrange(DOWN, buff=0.25),
            box_width=11.0,
        )
        descartes.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "En développant cette relation, on aboutit à la formule "
                "de conjugaison de Descartes : un sur O A prime, moins un "
                "sur O A, égale un sur O F prime, égale un sur f prime, "
                "égale la vergence C. Toutes les distances sont mesurées "
                "à partir du centre optique O, avec les conventions de "
                "signes vues précédemment."
            )
        ) as tracker:
            self.play(FadeIn(descartes))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(descartes))

        # --- À retenir --------------------------------------------------------------
        retenir = essentiel_box(
            VGroup(
                Text("À retenir", font_size=23, weight="BOLD"),
                MathTex(r"\dfrac{1}{\overline{OA'}} - \dfrac{1}{\overline{OA}} = \dfrac{1}{f'} = C", font_size=26),
                Text("Origine des distances : le centre optique O.", font_size=18),
                Text("Objet réel : OA < 0. Image réelle : OA' > 0.", font_size=18),
            ).arrange(DOWN, buff=0.2),
            box_width=10.8,
        )
        retenir.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Retenons l'essentiel : la formule de Descartes s'écrit "
                "un sur O A prime moins un sur O A égale un sur f prime "
                "égale C. L'origine des distances est toujours le centre "
                "optique O. Un objet réel a OA négatif, une image réelle "
                "a OA prime positif."
            )
        ) as tracker:
            self.play(FadeIn(retenir))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(retenir))

        # --- Piège --------------------------------------------------------------------
        piege = warning_box(
            VGroup(
                Text("• Ne JAMAIS injecter une distance mesurée « en", font_size=19),
                Text("   valeur absolue » (positive) à la place de la", font_size=19),
                Text("   mesure algébrique OA : pour un objet réel,", font_size=19),
                Text("   OA est TOUJOURS négatif dans la formule.", font_size=19, color=YELLOW),
                Text("• Toutes les distances (OA, OA', OF') partagent la", font_size=19),
                Text("   même origine O : ne pas mélanger des distances", font_size=19),
                Text("   mesurées depuis d'autres points.", font_size=19),
            ).arrange(DOWN, aligned_edge=LEFT, buff=0.12),
            box_width=12.0,
        )
        piege.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Piège majeur de ce chapitre : il ne faut jamais injecter "
                "une distance mesurée en valeur absolue, donc positive, à "
                "la place de la mesure algébrique O A. Pour un objet "
                "réel, O A est toujours négatif dans la formule de "
                "Descartes. Et toutes les distances, O A, O A prime, O F "
                "prime, doivent partager la même origine O : il ne faut "
                "jamais mélanger des distances mesurées depuis d'autres "
                "points."
            )
        ) as tracker:
            self.play(FadeIn(piege))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(piege), FadeOut(titre))
