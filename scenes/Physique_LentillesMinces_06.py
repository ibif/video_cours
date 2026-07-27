"""
scenes/Physique_LentillesMinces_06.py — Chapitre 13 « Les lentilles minces »
(1ereC, Physique), scène 06.

§ Exemple de construction complète : lentille convergente, objet réel AB
situé à 2f' (image réelle, renversée, de même taille, à 2f' après la
lentille). Cas de la lentille divergente pour le même objet (image
toujours virtuelle, droite, plus petite, entre O et F', prolongements en
pointillés).
Source : 1ereC/Physique.pdf, pages 130-140 (chapitre 13, § 3).
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
    BLUE,
    GREEN,
    RED,
    Arrow,
    Create,
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
from shapes.boxes import essentiel_box, example_box, scene_title, warning_box


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


class ExempleConstructionImages(NotionScene):
    def construct(self):
        titre = scene_title("Construire une image : deux exemples complets")
        titre.scale(0.4)
        titre.to_edge(UP)
        self.play(Write(titre))

        # --- Énoncé -----------------------------------------------------------------
        enonce = Text(
            _wrap(
                "Construisons l'image d'un objet AB par une lentille "
                "convergente, avec l'objet placé à une distance 2f' de la "
                "lentille, puis observons ce que devient cette même "
                "construction avec une lentille divergente.",
                width=52,
            ),
            font_size=21,
        )
        enonce.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Construisons l'image d'un objet A B par une lentille "
                "convergente, l'objet étant placé à une distance 2f' de la "
                "lentille. Nous observerons ensuite ce que devient cette "
                "même construction avec une lentille divergente."
            )
        ) as tracker:
            self.play(FadeIn(enonce))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(enonce))

        # --- Raisonnement : construction, lentille convergente, objet à 2f' ------
        f = 1.6
        axe = Line(LEFT * 4.4, RIGHT * 4.4, color=WHITE, stroke_width=1.5)
        lentille = _lens_symbol(True, height=2.6)
        O = Dot(ORIGIN, color=WHITE, radius=0.05)
        F = Dot(LEFT * f, color=YELLOW, radius=0.05)
        label_F = MathTex("F", font_size=22, color=YELLOW).next_to(F, DOWN, buff=0.1)
        Fp = Dot(RIGHT * f, color=YELLOW, radius=0.05)
        label_Fp = MathTex("F'", font_size=22, color=YELLOW).next_to(Fp, DOWN, buff=0.1)
        F2 = Dot(LEFT * 2 * f, color=BLUE, radius=0.04)
        label_F2 = MathTex("2F", font_size=18, color=BLUE).next_to(F2, DOWN, buff=0.1)
        F2p = Dot(RIGHT * 2 * f, color=BLUE, radius=0.04)
        label_F2p = MathTex("2F'", font_size=18, color=BLUE).next_to(F2p, DOWN, buff=0.1)

        A = LEFT * 2 * f
        B = LEFT * 2 * f + UP * 0.9
        objet = Arrow(A, B, buff=0, color=WHITE, stroke_width=3)
        label_B = Text("B", font_size=18).next_to(B, UP, buff=0.06)

        # rayon (1) // axe → F'
        r1a = Line(B, UP * 0.9, color=GREEN, stroke_width=2.5)
        r1b = Line(UP * 0.9, RIGHT * 2 * f + DOWN * 0.9, color=GREEN, stroke_width=2.5)
        # rayon (2) par O → non dévié (symétrique, va jusqu'à 2F')
        r2 = Line(B, RIGHT * 2 * f + DOWN * 0.9, color=RED, stroke_width=2.5)

        Bp = RIGHT * 2 * f + DOWN * 0.9
        Ap = RIGHT * 2 * f
        image = Arrow(Ap, Bp, buff=0, color=YELLOW, stroke_width=3)
        label_Bp = MathTex("B'", font_size=18, color=YELLOW).next_to(Bp, DOWN, buff=0.08)

        groupe_conv = VGroup(
            axe, lentille, O, F, label_F, Fp, label_Fp, F2, label_F2, F2p, label_F2p,
            objet, label_B, r1a, r1b, r2, image, label_Bp,
        )
        groupe_conv.move_to(ORIGIN).next_to(titre, DOWN, buff=0.55)

        legende_conv = Text(
            "Objet à 2f' → image réelle, renversée, même taille, à 2f'",
            font_size=18,
        )
        legende_conv.next_to(groupe_conv, DOWN, buff=0.3)

        with self.voiceover(
            text=(
                "L'objet A B est placé à une distance 2 f prime de la "
                "lentille convergente. On trace le rayon parallèle à "
                "l'axe, qui émerge par F prime, et le rayon qui passe par "
                "O, non dévié. Leur intersection donne l'image B prime. "
                "On observe que l'image se forme aussi à 2 f prime, de "
                "l'autre côté : elle est réelle, renversée, et de la même "
                "taille que l'objet."
            )
        ) as tracker:
            self.play(Create(axe), Create(lentille))
            self.play(FadeIn(O), FadeIn(F), Write(label_F), FadeIn(Fp), Write(label_Fp))
            self.play(FadeIn(F2), Write(label_F2), FadeIn(F2p), Write(label_F2p))
            self.play(Create(objet), Write(label_B))
            self.play(Create(r1a), Create(r1b))
            self.play(Create(r2))
            self.play(Create(image), Write(label_Bp))
            self.play(Write(legende_conv))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(groupe_conv), FadeOut(legende_conv))

        # --- Raisonnement : même objet, lentille divergente -----------------------
        axe2 = Line(LEFT * 4.4, RIGHT * 4.4, color=WHITE, stroke_width=1.5)
        lentille2 = _lens_symbol(False, height=2.4)
        O2 = Dot(ORIGIN, color=WHITE, radius=0.05)
        Fp2 = Dot(LEFT * f, color=YELLOW, radius=0.05)  # F' virtuel côté incident (divergente)
        label_Fp2 = MathTex("F'", font_size=22, color=YELLOW).next_to(Fp2, DOWN, buff=0.1)

        A2 = LEFT * 2.6
        B2 = LEFT * 2.6 + UP * 0.9
        objet2 = Arrow(A2, B2, buff=0, color=WHITE, stroke_width=3)
        label_B2 = Text("B", font_size=18).next_to(B2, UP, buff=0.06)

        # rayon (1) // axe → diverge comme s'il venait de F' (virtuel, à gauche)
        r1a_2 = Line(B2, UP * 0.9, color=GREEN, stroke_width=2.5)
        # pente réelle : direction issue de F' passant par (0, 0.9)
        pente_1 = (0.9 - 0) / (0 - (-f))
        sortie_1 = UP * 0.9 + RIGHT * 2.6 * 1 + UP * (pente_1 * 2.6)
        r1b_2 = Line(UP * 0.9, sortie_1, color=GREEN, stroke_width=2.5)
        prol_1 = DashedLine(UP * 0.9, Fp2.get_center(), color=GREEN, stroke_width=1.5)

        # rayon (2) par O → non dévié (droite B2-O prolongée au-delà de O)
        pente_2 = (0 - 0.9) / (0 - (-2.6))
        sortie_2 = RIGHT * 2.6 + UP * (pente_2 * 2.6)
        r2_2 = Line(B2, sortie_2, color=RED, stroke_width=2.5)

        # Intersection des DEUX rayons émergents divergents (prolongés en arrière) → B' virtuelle
        # r1 émergent : passe par (0,0.9) avec pente pente_1 ; r2 émergent : passe par O avec pente pente_2
        # r1: y = 0.9 + pente_1 * x ;  r2: y = pente_2 * x
        x_bp = 0.9 / (pente_2 - pente_1)
        y_bp = pente_2 * x_bp
        Bp2 = RIGHT * x_bp + UP * y_bp
        prol_r1_arriere = DashedLine(UP * 0.9, Bp2, color=GREEN, stroke_width=1.5)
        prol_r2_arriere = DashedLine(ORIGIN, Bp2, color=RED, stroke_width=1.5)

        image2 = Arrow(RIGHT * x_bp, Bp2, buff=0, color=YELLOW, stroke_width=3)
        label_Bp2 = MathTex("B'", font_size=18, color=YELLOW).next_to(Bp2, UP, buff=0.08)

        groupe_div = VGroup(
            axe2, lentille2, O2, Fp2, label_Fp2, objet2, label_B2,
            r1a_2, r1b_2, r2_2, prol_1, prol_r1_arriere, prol_r2_arriere, image2, label_Bp2,
        )
        groupe_div.move_to(ORIGIN).next_to(titre, DOWN, buff=0.55)

        legende_div = Text(
            "Divergente : image toujours virtuelle, droite, plus petite",
            font_size=18,
        )
        legende_div.next_to(groupe_div, DOWN, buff=0.3)

        with self.voiceover(
            text=(
                "Reprenons le même objet A B, mais avec une lentille "
                "divergente. Le rayon parallèle à l'axe ressort comme "
                "s'il venait du foyer F prime virtuel, situé du côté "
                "incident. Le rayon qui passe par O n'est pas dévié. Ces "
                "deux rayons émergents divergent : ce sont leurs "
                "prolongements en pointillés, vers l'arrière, qui se "
                "croisent pour donner l'image B prime. Cette image est "
                "toujours virtuelle, droite, et plus petite que l'objet, "
                "située entre O et F'."
            )
        ) as tracker:
            self.play(Create(axe2), Create(lentille2))
            self.play(FadeIn(O2), FadeIn(Fp2), Write(label_Fp2))
            self.play(Create(objet2), Write(label_B2))
            self.play(Create(r1a_2), Create(r1b_2), Create(prol_1))
            self.play(Create(r2_2))
            self.play(Create(prol_r1_arriere), Create(prol_r2_arriere))
            self.play(Create(image2), Write(label_Bp2))
            self.play(Write(legende_div))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(groupe_div), FadeOut(legende_div))

        # --- Exemple --------------------------------------------------------------------
        exemple = example_box(
            VGroup(
                Text("Lentille convergente, f' = 1,6 cm, objet à 2f' = 3,2 cm.", font_size=19),
                Text("Construction → image réelle, renversée, même taille,", font_size=19),
                Text("formée à 3,2 cm de l'autre côté de la lentille.", font_size=19),
            ).arrange(DOWN, buff=0.16, aligned_edge=LEFT),
            box_width=11.4,
        )
        exemple.next_to(titre, DOWN, buff=0.45)

        with self.voiceover(
            text=(
                "Exemple : pour une lentille convergente de distance "
                "focale 1,6 centimètre, un objet placé à 2 f prime, soit "
                "3,2 centimètres, donne par construction une image "
                "réelle, renversée, de même taille, formée à 3,2 "
                "centimètres de l'autre côté de la lentille."
            )
        ) as tracker:
            self.play(FadeIn(exemple))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(exemple))

        # --- À retenir --------------------------------------------------------------
        retenir = essentiel_box(
            VGroup(
                Text("À retenir", font_size=23, weight="BOLD"),
                Text("Convergente, objet à 2F : image réelle, renversée,", font_size=18),
                Text("même taille, à 2F' (cas particulier remarquable).", font_size=18),
                Text("Divergente : l'image d'un objet réel est TOUJOURS", font_size=18),
                Text("virtuelle, droite et plus petite, entre O et F'.", font_size=18),
            ).arrange(DOWN, buff=0.14, aligned_edge=LEFT),
            box_width=11.8,
        )
        retenir.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Retenons l'essentiel : pour une lentille convergente, un "
                "objet placé en 2F donne une image réelle, renversée, de "
                "même taille, en 2F prime — c'est un cas particulier "
                "remarquable. Pour une lentille divergente, l'image d'un "
                "objet réel est toujours virtuelle, droite et plus "
                "petite, située entre O et F prime."
            )
        ) as tracker:
            self.play(FadeIn(retenir))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(retenir))

        # --- Piège --------------------------------------------------------------------
        piege = warning_box(
            VGroup(
                Text("• Une image virtuelle se construit avec les", font_size=19),
                Text("   PROLONGEMENTS en pointillés des rayons émergents,", font_size=19),
                Text("   jamais avec les rayons émergents réels eux-mêmes.", font_size=19),
                Text("• Une lentille divergente ne donne JAMAIS d'image", font_size=19),
                Text("   réelle pour un objet réel, quelle que soit sa", font_size=19),
                Text("   position : ne pas chercher une image réelle !", font_size=19),
            ).arrange(DOWN, aligned_edge=LEFT, buff=0.12),
            box_width=12.0,
        )
        piege.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Piège à éviter : une image virtuelle se construit "
                "toujours avec les prolongements en pointillés des rayons "
                "émergents, jamais avec les rayons émergents réels "
                "eux-mêmes. Et une lentille divergente ne donne jamais "
                "d'image réelle pour un objet réel, quelle que soit sa "
                "position : il est inutile de chercher une image réelle "
                "dans ce cas."
            )
        ) as tracker:
            self.play(FadeIn(piege))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(piege), FadeOut(titre))
