"""
scenes/Physique_LentillesMinces_02.py — Chapitre 13 « Les lentilles minces »
(1ereC, Physique), scène 02.

§ Centre optique O, axe principal, axes secondaires, foyer principal
image F' (rayons parallèles à l'axe convergent en F' après la lentille :
réel pour une convergente, virtuel pour une divergente), foyer principal
objet F (rayon passant par F émerge parallèle à l'axe), propriété de
symétrie des foyers OF = -OF'.
Source : 1ereC/Physique.pdf, pages 130-140 (chapitre 13, § 2).
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
from shapes.boxes import definition_box, essentiel_box, example_box, property_box, scene_title, warning_box


def _wrap(text: str, width: int = 56) -> str:
    return "\n".join(textwrap.fill(line, width=width) for line in text.split("\n"))


def _lens_symbol(convergente: bool = True, height: float = 2.4, color=WHITE) -> VGroup:
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


def _axis(demi_longueur: float = 4.3, color=WHITE) -> Line:
    return Line(LEFT * demi_longueur, RIGHT * demi_longueur, color=color, stroke_width=1.5)


class CentreOptiqueFoyers(NotionScene):
    def construct(self):
        titre = scene_title("Centre optique, axes et foyers principaux")
        titre.scale(0.42)
        titre.to_edge(UP)
        self.play(Write(titre))

        # --- Énoncé : centre optique et axes --------------------------------------
        definitions = definition_box(
            VGroup(
                Text("Centre optique O", font_size=23, weight="BOLD"),
                Text("Tout rayon lumineux passant par O n'est pas dévié.", font_size=20),
                Text("Axe principal", font_size=23, weight="BOLD"),
                Text("Droite passant par O, perpendiculaire au plan de la", font_size=20),
                Text("lentille.", font_size=20),
                Text("Axe secondaire", font_size=23, weight="BOLD"),
                Text("Toute autre droite passant par O.", font_size=20),
            ).arrange(DOWN, buff=0.15, aligned_edge=LEFT),
            box_width=11.4,
        )
        definitions.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Le centre optique, noté O, est le point de la lentille "
                "tel que tout rayon lumineux qui passe par lui n'est pas "
                "dévié : il continue en ligne droite. L'axe principal est "
                "la droite qui passe par O et qui est perpendiculaire au "
                "plan de la lentille. Toute autre droite passant par O est "
                "appelée un axe secondaire."
            )
        ) as tracker:
            self.play(FadeIn(definitions))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(definitions))

        # --- Raisonnement : foyer image F' (rayons // axe → convergent en F') ----
        axe1 = _axis()
        lentille1 = _lens_symbol(True)
        O1 = Dot(ORIGIN, color=WHITE, radius=0.05)
        label_O1 = MathTex("O", font_size=26).next_to(O1, DOWN, buff=0.15)
        Fp = Dot(RIGHT * 2.2, color=YELLOW, radius=0.06)
        label_Fp = MathTex("F'", font_size=26, color=YELLOW).next_to(Fp, DOWN, buff=0.15)

        rayons_in = VGroup(*[
            Line(LEFT * 4.0 + UP * h, UP * h, color=BLUE, stroke_width=3)
            for h in (0.9, 0.45, -0.45, -0.9)
        ])
        rayons_out = VGroup(*[
            Line(UP * h, RIGHT * 2.2, color=BLUE, stroke_width=3)
            for h in (0.9, 0.45, -0.45, -0.9)
        ])
        rayon_axial = Line(LEFT * 4.0, RIGHT * 4.0, color=BLUE, stroke_width=3)

        groupe1 = VGroup(axe1, lentille1, O1, label_O1, Fp, label_Fp, rayons_in, rayons_out, rayon_axial)
        groupe1.move_to(ORIGIN).next_to(titre, DOWN, buff=0.7)

        legende1 = Text("Lentille convergente : F' réel (rayons se croisent vraiment)", font_size=19)
        legende1.next_to(groupe1, DOWN, buff=0.3)

        with self.voiceover(
            text=(
                "Considérons des rayons incidents parallèles à l'axe "
                "principal. Après avoir traversé une lentille convergente, "
                "ils convergent tous en un même point de l'axe, situé "
                "après la lentille : c'est le foyer principal image, noté "
                "F prime. Pour une convergente, ce foyer est réel, les "
                "rayons s'y croisent vraiment. Pour une lentille "
                "divergente, ces mêmes rayons parallèles divergent après "
                "la lentille : ce sont leurs prolongements, tracés en "
                "arrière, qui se croisent en F prime. Le foyer est alors "
                "virtuel."
            )
        ) as tracker:
            self.play(Create(axe1), Create(lentille1))
            self.play(FadeIn(O1), Write(label_O1))
            self.play(Create(rayons_in))
            self.play(Create(rayons_out), FadeIn(Fp), Write(label_Fp))
            self.play(Write(legende1))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(groupe1), FadeOut(legende1))

        # --- Raisonnement : foyer objet F (rayon par F → émerge // axe) ----------
        axe2 = _axis()
        lentille2 = _lens_symbol(True)
        O2 = Dot(ORIGIN, color=WHITE, radius=0.05)
        label_O2 = MathTex("O", font_size=26).next_to(O2, DOWN, buff=0.15)
        F = Dot(LEFT * 2.2, color=YELLOW, radius=0.06)
        label_F = MathTex("F", font_size=26, color=YELLOW).next_to(F, DOWN, buff=0.15)

        rayons_vers_lentille = VGroup(*[
            Line(LEFT * 2.2, UP * h, color=BLUE, stroke_width=3)
            for h in (0.9, 0.45, -0.45, -0.9)
        ])
        rayons_emergents = VGroup(*[
            Line(UP * h, RIGHT * 4.0 + UP * h, color=BLUE, stroke_width=3)
            for h in (0.9, 0.45, -0.45, -0.9)
        ])

        groupe2 = VGroup(axe2, lentille2, O2, label_O2, F, label_F, rayons_vers_lentille, rayons_emergents)
        groupe2.move_to(ORIGIN).next_to(titre, DOWN, buff=0.7)

        legende2 = Text("Tout rayon passant par F émerge parallèle à l'axe", font_size=19)
        legende2.next_to(groupe2, DOWN, buff=0.3)

        with self.voiceover(
            text=(
                "Le foyer principal objet, noté F, est défini de façon "
                "symétrique : tout rayon incident qui passe par F, avant "
                "d'atteindre la lentille, émerge après elle parallèlement "
                "à l'axe principal."
            )
        ) as tracker:
            self.play(Create(axe2), Create(lentille2))
            self.play(FadeIn(O2), Write(label_O2), FadeIn(F), Write(label_F))
            self.play(Create(rayons_vers_lentille))
            self.play(Create(rayons_emergents))
            self.play(Write(legende2))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(groupe2), FadeOut(legende2))

        # --- Propriété : symétrie des foyers --------------------------------------
        symetrie = property_box(
            VGroup(
                Text("Symétrie des foyers", font_size=23, weight="BOLD"),
                MathTex(r"\overline{OF} = -\overline{OF'}", font_size=30, color=YELLOW),
                Text(
                    "F et F' sont symétriques par rapport au centre optique O",
                    font_size=19,
                ),
                Text("(une lentille mince, dans l'air, a le même milieu", font_size=19),
                Text("des deux côtés).", font_size=19),
            ).arrange(DOWN, buff=0.22),
            box_width=11.0,
        )
        symetrie.next_to(titre, DOWN, buff=0.45)

        with self.voiceover(
            text=(
                "Propriété importante : les foyers F et F prime sont "
                "symétriques par rapport au centre optique O, ce qui "
                "s'écrit O F égale moins O F prime. Cela vient du fait "
                "qu'une lentille mince, plongée dans l'air, a le même "
                "milieu des deux côtés."
            )
        ) as tracker:
            self.play(FadeIn(symetrie))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(symetrie))

        # --- Exemple ------------------------------------------------------------------
        exemple = example_box(
            VGroup(
                Text("Une lentille convergente a son foyer F' à 3 cm de O.", font_size=20),
                Text("Où se trouve son foyer objet F ?", font_size=20),
                MathTex(r"\overline{OF} = -\overline{OF'} = -3\ \text{cm}", font_size=26, color=YELLOW),
                Text("F est donc à 3 cm de O, du côté opposé à F'.", font_size=20),
            ).arrange(DOWN, buff=0.2),
            box_width=11.4,
        )
        exemple.next_to(titre, DOWN, buff=0.45)

        with self.voiceover(
            text=(
                "Exemple : une lentille convergente a son foyer image F "
                "prime situé à 3 centimètres du centre optique O. Où se "
                "trouve son foyer objet F ? Par symétrie, O F égale moins "
                "O F prime égale moins 3 centimètres : F se trouve donc "
                "aussi à 3 centimètres de O, mais du côté opposé à F "
                "prime."
            )
        ) as tracker:
            self.play(FadeIn(exemple))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(exemple))

        # --- À retenir --------------------------------------------------------------
        retenir = essentiel_box(
            VGroup(
                Text("À retenir", font_size=24, weight="BOLD"),
                Text("O : tout rayon qui le traverse n'est pas dévié.", font_size=19),
                Text("F' : point de convergence des rayons // à l'axe.", font_size=19),
                Text("F : point tel qu'un rayon qui y passe ressort // à l'axe.", font_size=19),
                Text("Symétrie : OF = -OF' de part et d'autre de O.", font_size=19),
            ).arrange(DOWN, buff=0.18, aligned_edge=LEFT),
            box_width=12.0,
        )
        retenir.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Retenons l'essentiel : O est le point que tout rayon "
                "traverse sans être dévié. F prime est le point où "
                "convergent les rayons parallèles à l'axe. F est le point "
                "tel qu'un rayon qui y passe ressort parallèle à l'axe. Et "
                "les deux foyers sont symétriques par rapport à O."
            )
        ) as tracker:
            self.play(FadeIn(retenir))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(retenir))

        # --- Piège --------------------------------------------------------------------
        piege = warning_box(
            VGroup(
                Text("• Pour une lentille DIVERGENTE, les positions de F", font_size=19),
                Text("   et F' sont INVERSÉES par rapport à la convergente :", font_size=19),
                Text("   F' (virtuel) est du côté incident (avant la", font_size=19),
                Text("   lentille), F (virtuel) du côté de la sortie", font_size=19),
                Text("   (après la lentille).", font_size=19),
                Text("• Un foyer virtuel se construit avec des prolongements", font_size=19),
                Text("   en pointillés, jamais avec des rayons réels.", font_size=19),
            ).arrange(DOWN, aligned_edge=LEFT, buff=0.12),
            box_width=12.0,
        )
        piege.next_to(titre, DOWN, buff=0.4)

        # petit schéma illustrant le foyer virtuel d'une divergente
        axe3 = _axis(3.2)
        lentille3 = _lens_symbol(False)
        rayons_in3 = VGroup(*[
            Line(LEFT * 2.6 + UP * h, UP * h, color=BLUE, stroke_width=2.5)
            for h in (0.7, -0.7)
        ])
        rayons_out3 = VGroup(*[
            Line(UP * h, RIGHT * 2.6 + UP * (h * 1.9), color=BLUE, stroke_width=2.5)
            for h in (0.7, -0.7)
        ])
        prolongements3 = VGroup(*[
            DashedLine(UP * h, LEFT * 1.4 + UP * (h * 1.9), color=YELLOW, stroke_width=2)
            for h in (0.7, -0.7)
        ])
        Fp3 = Dot(LEFT * 1.4, color=YELLOW, radius=0.05)
        label_Fp3 = MathTex("F'", font_size=22, color=YELLOW).next_to(Fp3, DOWN, buff=0.12)
        mini_schema = VGroup(axe3, lentille3, rayons_in3, rayons_out3, prolongements3, Fp3, label_Fp3)
        mini_schema.scale(0.62)
        mini_schema.next_to(piege, DOWN, buff=0.35)

        with self.voiceover(
            text=(
                "Attention à un piège fréquent : pour une lentille "
                "divergente, les positions de F et F prime sont inversées "
                "par rapport à la convergente. F prime, virtuel, se trouve "
                "du côté incident, avant la lentille ; F, virtuel lui "
                "aussi, se trouve du côté de la sortie, après la lentille. "
                "Et un foyer virtuel se construit toujours avec des "
                "prolongements en pointillés, jamais avec des rayons "
                "réels."
            )
        ) as tracker:
            self.play(FadeIn(piege))
            self.play(Create(mini_schema))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(piege), FadeOut(mini_schema), FadeOut(titre))
