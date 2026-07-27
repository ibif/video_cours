"""
scenes/Physique_LentillesMinces_10.py — Chapitre 13 « Les lentilles minces »
(1ereC, Physique), scène 10.

§ Formule de conjugaison de Newton FA·F'A' = -f'² et γ = f'/FA = -F'A'/f',
AVEC démonstration (triangles semblables FAB/FOI et F'A'B'/F'OJ).
Vérification sur l'exemple résolu de la scène précédente. Théorème (admis)
d'association de lentilles accolées C = C1 + C2. Exemple résolu 3 :
L1 C1 = +8 δ, L2 f'2 = +50 cm → C2 = +2 δ, C = +10 δ, f' = +10 cm.
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
from shapes.boxes import essentiel_box, example_box, scene_title, theorem_box, warning_box


def _wrap(text: str, width: int = 56) -> str:
    return "\n".join(textwrap.fill(line, width=width) for line in text.split("\n"))


def _lens_symbol(convergente: bool = True, height: float = 2.8, color=WHITE) -> VGroup:
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


class FormuleNewtonVergences(NotionScene):
    def construct(self):
        titre = scene_title("Formule de Newton et théorème des vergences")
        titre.scale(0.4)
        titre.to_edge(UP)
        self.play(Write(titre))

        # --- Énoncé / raisonnement : démonstration de la formule de Newton -----------
        f = 1.4
        axe = Line(LEFT * 4.6, RIGHT * 4.6, color=WHITE, stroke_width=1.5)
        lentille = _lens_symbol(True, height=2.6)
        O = Dot(ORIGIN, color=WHITE, radius=0.045)
        label_O = MathTex("O", font_size=18).next_to(O, DOWN, buff=0.06)
        F = Dot(LEFT * f, color=YELLOW, radius=0.05)
        label_F = MathTex("F", font_size=18, color=YELLOW).next_to(F, DOWN, buff=0.06)
        Fp = Dot(RIGHT * f, color=YELLOW, radius=0.05)
        label_Fp = MathTex("F'", font_size=18, color=YELLOW).next_to(Fp, DOWN, buff=0.06)

        A = LEFT * 3.0
        B = LEFT * 3.0 + UP * 1.0
        objet = Arrow(A, B, buff=0, color=WHITE, stroke_width=2.2)
        label_B = Text("B", font_size=15).next_to(B, UP, buff=0.05)

        # rayon par O non dévié (I, mentionné dans la démonstration, est le
        # point de ce rayon à la hauteur de B, donc B lui-même ici)
        r_O = Line(B, B + (ORIGIN - B) * 2.4, color=RED, stroke_width=2)
        # rayon // axe -> J, puis J -> F'
        J_point = UP * 1.0
        J = Dot(J_point, color=GREEN, radius=0.03)
        label_J = MathTex("J", font_size=16, color=GREEN).next_to(J, UP, buff=0.05)
        r_par1 = Line(B, J_point, color=GREEN, stroke_width=2)
        dir_JFp = Fp.get_center() - J_point
        r_par2 = Line(J_point, Fp.get_center() + dir_JFp * 1.8, color=GREEN, stroke_width=2)

        pente_par = dir_JFp[1] / dir_JFp[0]
        pente_O = (0 - B[1]) / (0 - B[0])
        x_bp = 1.0 / (pente_O - pente_par)
        y_bp = pente_O * x_bp
        Bp = RIGHT * x_bp + UP * y_bp
        image = Arrow(RIGHT * x_bp, Bp, buff=0, color=YELLOW, stroke_width=2.2)
        label_Bp = MathTex("B'", font_size=15, color=YELLOW).next_to(Bp, DOWN, buff=0.05)

        groupe = VGroup(
            axe, lentille, O, label_O, F, label_F, Fp, label_Fp,
            objet, label_B, r_O, r_par1, r_par2, J, label_J, image, label_Bp,
        )
        groupe.scale(0.85).move_to(ORIGIN).next_to(titre, DOWN, buff=0.5)

        demo = VGroup(
            Text("Triangles semblables FAB et FOI (I sur le rayon par O,", font_size=16),
            Text("à la hauteur de B) :", font_size=16),
            MathTex(r"\dfrac{\overline{FA}}{\overline{FO}} = \dfrac{\overline{AB}}{\overline{OI}}", font_size=18),
            Text("Triangles semblables F'A'B' et F'OJ (OJ = AB) :", font_size=16),
            MathTex(r"\dfrac{\overline{F'A'}}{\overline{F'O}} = \dfrac{\overline{A'B'}}{\overline{OJ}}", font_size=18),
            Text("En combinant (OI = -AB par construction) :", font_size=16),
            MathTex(r"\overline{FA}\cdot\overline{F'A'} = -f'^2", font_size=22, color=YELLOW),
        ).arrange(DOWN, buff=0.1)
        demo.next_to(groupe, DOWN, buff=0.25)

        with self.voiceover(
            text=(
                "Démontrons la formule de Newton. Les triangles F A B et "
                "F O I, où I est un point du rayon passant par O à la "
                "même hauteur que B, sont semblables. Les triangles F "
                "prime A prime B prime et F prime O J, où J est le point "
                "du rayon parallèle à l'axe dans le plan de la lentille, "
                "sont eux aussi semblables. En combinant ces deux "
                "relations de similitude, on obtient la formule de "
                "Newton : F A fois F prime A prime égale moins f prime "
                "au carré."
            )
        ) as tracker:
            self.play(Create(axe), Create(lentille))
            self.play(FadeIn(O), Write(label_O), FadeIn(F), Write(label_F), FadeIn(Fp), Write(label_Fp))
            self.play(Create(objet), Write(label_B))
            self.play(Create(r_O))
            self.play(Create(r_par1), FadeIn(J), Write(label_J), Create(r_par2))
            self.play(Create(image), Write(label_Bp))
            self.play(Write(demo))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(groupe), FadeOut(demo))

        # --- Théorème -----------------------------------------------------------------
        newton = theorem_box(
            VGroup(
                Text("Formule de Newton et grandissement", font_size=21, weight="BOLD"),
                MathTex(r"\overline{FA}\cdot\overline{F'A'} = -f'^2", font_size=27, color=YELLOW),
                MathTex(r"\gamma = \dfrac{f'}{\overline{FA}} = -\dfrac{\overline{F'A'}}{f'}", font_size=27, color=YELLOW),
                Text("(distances mesurées depuis F et F', pas depuis O)", font_size=17),
            ).arrange(DOWN, buff=0.22),
            box_width=10.8,
        )
        newton.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Retenons la formule de Newton : F A fois F prime A "
                "prime égale moins f prime au carré. Le grandissement "
                "s'exprime alors aussi par gamma égale f prime sur F A, "
                "égale moins F prime A prime sur f prime. Attention : ici "
                "les distances sont mesurées depuis F et F prime, pas "
                "depuis O."
            )
        ) as tracker:
            self.play(FadeIn(newton))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(newton))

        # --- Exemple : vérification + association de lentilles -----------------------
        verif = example_box(
            VGroup(
                Text("Vérification (exemple précédent : f' = 5 cm, OA = -15 cm) :", font_size=18),
                MathTex(r"\overline{FA} = \overline{OA}-\overline{OF} = -15-(-5) = -10\ \text{cm}", font_size=20),
                MathTex(r"\overline{F'A'} = \overline{OA'}-\overline{OF'} = 7{,}5-5 = 2{,}5\ \text{cm}", font_size=20),
                MathTex(r"\overline{FA}\cdot\overline{F'A'} = -10 \times 2{,}5 = -25 = -f'^2\ \checkmark", font_size=20, color=YELLOW),
            ).arrange(DOWN, buff=0.16),
            box_width=11.4,
        )
        verif.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Vérifions sur l'exemple précédent, où f prime valait 5 "
                "centimètres et O A valait moins 15 centimètres. F A "
                "égale O A moins O F, soit moins 15 moins moins 5, donc "
                "moins 10 centimètres. F prime A prime égale O A prime "
                "moins O F prime, soit 7,5 moins 5, donc 2,5 centimètres. "
                "Le produit F A fois F prime A prime vaut moins 10 fois "
                "2,5, soit moins 25, ce qui correspond bien à moins f "
                "prime au carré, puisque f prime au carré vaut 25."
            )
        ) as tracker:
            self.play(FadeIn(verif))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(verif))

        # --- Théorème (admis) : association de lentilles accolées --------------------
        association = theorem_box(
            VGroup(
                Text("Association de deux lentilles minces accolées", font_size=20, weight="BOLD"),
                Text("(admis)", font_size=15),
                MathTex(r"C = C_1 + C_2", font_size=28, color=YELLOW),
            ).arrange(DOWN, buff=0.2),
            box_width=9.0,
        )
        association.next_to(titre, DOWN, buff=0.5)

        exemple3 = example_box(
            VGroup(
                Text("L1 : C1 = +8 δ.   L2 : f'2 = +50 cm = 0,5 m → C2 = +2 δ.", font_size=18),
                MathTex(r"C = C_1+C_2 = 8+2 = +10\ \delta \quad\Rightarrow\quad f' = \dfrac{1}{C} = +0{,}10\ \text{m} = +10\ \text{cm}", font_size=20, color=YELLOW),
            ).arrange(DOWN, buff=0.18),
            box_width=11.6,
        )
        exemple3.next_to(association, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Dernier résultat, admis sans démonstration : pour deux "
                "lentilles minces accolées, la vergence de l'ensemble est "
                "la somme des vergences, C égale C1 plus C2. Exemple "
                "résolu : la lentille L1 a une vergence C1 de plus 8 "
                "dioptries. La lentille L2 a une distance focale f prime "
                "2 de plus 50 centimètres, soit une vergence C2 de plus 2 "
                "dioptries. La vergence totale vaut donc C1 plus C2, soit "
                "10 dioptries, ce qui correspond à une distance focale "
                "totale de plus 10 centimètres."
            )
        ) as tracker:
            self.play(FadeIn(association))
            self.play(FadeIn(exemple3))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(association), FadeOut(exemple3))

        # --- À retenir --------------------------------------------------------------
        retenir = essentiel_box(
            VGroup(
                Text("À retenir", font_size=22, weight="BOLD"),
                MathTex(r"\overline{FA}\cdot\overline{F'A'} = -f'^2 \qquad \gamma = \dfrac{f'}{\overline{FA}}", font_size=24),
                MathTex(r"C_{\text{accolées}} = C_1 + C_2", font_size=24, color=YELLOW),
            ).arrange(DOWN, buff=0.2),
            box_width=10.6,
        )
        retenir.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Retenons l'essentiel : la formule de Newton, F A fois F "
                "prime A prime égale moins f prime au carré, avec gamma "
                "égale f prime sur F A. Et pour des lentilles accolées, "
                "les vergences s'additionnent."
            )
        ) as tracker:
            self.play(FadeIn(retenir))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(retenir))

        # --- Piège --------------------------------------------------------------------
        piege = warning_box(
            VGroup(
                Text("• Dans la formule de Newton, les distances FA et F'A'", font_size=18),
                Text("   sont mesurées depuis F et F', PAS depuis O : ne pas", font_size=18),
                Text("   les confondre avec OA et OA' de Descartes.", font_size=18),
                Text("• Le produit FA·F'A' est TOUJOURS négatif (= -f'²),", font_size=18),
                Text("   même pour une lentille divergente (f'² reste > 0).", font_size=18),
                Text("• L'addition des vergences ne vaut que pour des", font_size=18),
                Text("   lentilles ACCOLÉES (distance nulle entre elles).", font_size=18),
            ).arrange(DOWN, aligned_edge=LEFT, buff=0.1),
            box_width=12.0,
        )
        piege.next_to(titre, DOWN, buff=0.35)

        with self.voiceover(
            text=(
                "Pièges à éviter : dans la formule de Newton, les "
                "distances F A et F prime A prime sont mesurées depuis F "
                "et F prime, pas depuis O — il ne faut pas les confondre "
                "avec O A et O A prime de la formule de Descartes. Le "
                "produit F A fois F prime A prime est toujours négatif, "
                "même pour une lentille divergente, puisque f prime au "
                "carré reste positif. Enfin, l'addition des vergences ne "
                "vaut que pour des lentilles accolées, c'est-à-dire "
                "séparées d'une distance nulle."
            )
        ) as tracker:
            self.play(FadeIn(piege))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(piege), FadeOut(titre))
