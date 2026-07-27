"""
scenes/Physique_LentillesMinces_04.py — Chapitre 13 « Les lentilles minces »
(1ereC, Physique), scène 04.

§ Plans focaux objet et image, foyers secondaires (intersection d'un axe
secondaire avec le plan focal), conditions de Gauss (rayons peu écartés et
peu inclinés par rapport à l'axe) → stigmatisme approché, justifiant les
constructions graphiques simples.
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
    GREY,
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
from shapes.boxes import definition_box, essentiel_box, example_box, scene_title, warning_box


def _wrap(text: str, width: int = 56) -> str:
    return "\n".join(textwrap.fill(line, width=width) for line in text.split("\n"))


def _lens_symbol(convergente: bool = True, height: float = 2.6, color=WHITE) -> VGroup:
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


class PlansFocauxConditionsGauss(NotionScene):
    def construct(self):
        titre = scene_title("Plans focaux, foyers secondaires, conditions de Gauss")
        titre.scale(0.38)
        titre.to_edge(UP)
        self.play(Write(titre))

        # --- Énoncé : définitions --------------------------------------------------
        definitions = definition_box(
            VGroup(
                Text("Plans focaux", font_size=22, weight="BOLD"),
                Text("Plans perpendiculaires à l'axe principal, passant", font_size=19),
                Text("par F (plan focal objet) et par F' (plan focal image).", font_size=19),
                Text("Foyer secondaire", font_size=22, weight="BOLD"),
                Text("Intersection d'un axe secondaire avec le plan focal", font_size=19),
                Text("correspondant.", font_size=19),
            ).arrange(DOWN, buff=0.16, aligned_edge=LEFT),
            box_width=11.4,
        )
        definitions.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Les plans focaux sont les plans perpendiculaires à l'axe "
                "principal qui passent par les foyers : le plan focal "
                "objet passe par F, le plan focal image passe par F prime. "
                "Un foyer secondaire est le point d'intersection d'un axe "
                "secondaire, une droite quelconque passant par O, avec le "
                "plan focal correspondant."
            )
        ) as tracker:
            self.play(FadeIn(definitions))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(definitions))

        # --- Raisonnement : construction du foyer secondaire image ----------------
        axe = Line(LEFT * 4.2, RIGHT * 4.2, color=WHITE, stroke_width=1.5)
        lentille = _lens_symbol(True)
        O = Dot(ORIGIN, color=WHITE, radius=0.05)
        label_O = MathTex("O", font_size=24).next_to(O, DOWN, buff=0.12)
        Fp = Dot(RIGHT * 2.4, color=YELLOW, radius=0.06)
        label_Fp = MathTex("F'", font_size=24, color=YELLOW).next_to(Fp, DOWN, buff=0.12)
        plan_focal = DashedLine(RIGHT * 2.4 + UP * 1.7, RIGHT * 2.4 + DOWN * 1.7, color=GREY, stroke_width=2)
        label_plan = Text("plan focal image", font_size=17, color=GREY).next_to(plan_focal, UP, buff=0.1)

        axe_secondaire = Line(LEFT * 2.0 + DOWN * 0.95, RIGHT * 3.0 + UP * 1.42, color=BLUE, stroke_width=2)
        # foyer secondaire = intersection axe secondaire / plan focal (x = 2.4)
        # pente de l'axe secondaire : de (-2.0,-0.95) à (3.0,1.42) → pente = 2.37/5.0
        pente = 2.37 / 5.0
        y_fs = -0.95 + pente * (2.4 - (-2.0))
        Fs = Dot(RIGHT * 2.4 + UP * y_fs, color=YELLOW, radius=0.06)
        label_Fs = MathTex("F'_s", font_size=22, color=YELLOW).next_to(Fs, RIGHT, buff=0.12)

        groupe = VGroup(axe, lentille, O, label_O, Fp, label_Fp, plan_focal, label_plan, axe_secondaire, Fs, label_Fs)
        groupe.move_to(ORIGIN).next_to(titre, DOWN, buff=0.6)

        legende = Text(
            "Un faisceau de rayons // à l'axe secondaire converge en F's",
            font_size=18,
        )
        legende.next_to(groupe, DOWN, buff=0.35)

        with self.voiceover(
            text=(
                "Construisons un foyer secondaire. On trace un axe "
                "secondaire quelconque passant par O, incliné par rapport "
                "à l'axe principal. Son intersection avec le plan focal "
                "image, ici en F prime indice s, est le foyer secondaire "
                "image associé à cette direction. Tout faisceau de rayons "
                "parallèles à cet axe secondaire converge, après la "
                "lentille, en ce même point F prime indice s."
            )
        ) as tracker:
            self.play(Create(axe), Create(lentille))
            self.play(FadeIn(O), Write(label_O))
            self.play(Create(plan_focal), Write(label_plan))
            self.play(Create(axe_secondaire))
            self.play(FadeIn(Fp), Write(label_Fp), FadeIn(Fs), Write(label_Fs))
            self.play(Write(legende))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(groupe), FadeOut(legende))

        # --- Conditions de Gauss ---------------------------------------------------
        conditions = definition_box(
            VGroup(
                Text("Conditions de Gauss", font_size=22, weight="BOLD"),
                Text("Les rayons utilisés sont peu écartés de l'axe", font_size=19),
                Text("principal et peu inclinés par rapport à lui.", font_size=19),
                Text("→ stigmatisme approché : à un point objet", font_size=19, color=YELLOW),
                Text("correspond un point image net et unique.", font_size=19, color=YELLOW),
            ).arrange(DOWN, buff=0.18, aligned_edge=LEFT),
            box_width=11.4,
        )
        conditions.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Toutes nos constructions supposent que les conditions de "
                "Gauss sont respectées : les rayons utilisés doivent être "
                "peu écartés de l'axe principal, et peu inclinés par "
                "rapport à lui. Sous ces conditions, on obtient un "
                "stigmatisme approché : à un point objet correspond un "
                "point image net et unique, ce qui justifie toutes les "
                "constructions géométriques simples que nous ferons."
            )
        ) as tracker:
            self.play(FadeIn(conditions))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(conditions))

        # --- Exemple --------------------------------------------------------------------
        exemple = example_box(
            VGroup(
                Text("Une lentille de diamètre 4 cm et de focale f' = 8 cm", font_size=19),
                Text("respecte les conditions de Gauss pour un faisceau", font_size=19),
                Text("d'ouverture de quelques degrés seulement autour de", font_size=19),
                Text("l'axe : c'est le cas usuel des exercices de ce cours.", font_size=19),
            ).arrange(DOWN, buff=0.18, aligned_edge=LEFT),
            box_width=11.6,
        )
        exemple.next_to(titre, DOWN, buff=0.45)

        with self.voiceover(
            text=(
                "Par exemple, une lentille de 4 centimètres de diamètre et "
                "de distance focale 8 centimètres respecte les conditions "
                "de Gauss pour un faisceau de quelques degrés d'ouverture "
                "autour de l'axe seulement : c'est précisément le cas "
                "usuel de tous les exercices de ce cours."
            )
        ) as tracker:
            self.play(FadeIn(exemple))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(exemple))

        # --- À retenir --------------------------------------------------------------
        retenir = essentiel_box(
            VGroup(
                Text("À retenir", font_size=24, weight="BOLD"),
                Text("Plan focal image : perpendiculaire à l'axe en F'.", font_size=19),
                Text("Foyer secondaire : axe secondaire ∩ plan focal.", font_size=19),
                Text("Conditions de Gauss : rayons peu écartés/inclinés →", font_size=19),
                Text("constructions simples valables (stigmatisme approché).", font_size=19),
            ).arrange(DOWN, buff=0.16, aligned_edge=LEFT),
            box_width=12.0,
        )
        retenir.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Retenons l'essentiel : le plan focal image est le plan "
                "perpendiculaire à l'axe passant par F prime. Un foyer "
                "secondaire est l'intersection d'un axe secondaire avec le "
                "plan focal. Et les conditions de Gauss, rayons peu "
                "écartés et peu inclinés, rendent valables toutes nos "
                "constructions géométriques simples."
            )
        ) as tracker:
            self.play(FadeIn(retenir))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(retenir))

        # --- Piège --------------------------------------------------------------------
        piege = warning_box(
            VGroup(
                Text("• Hors des conditions de Gauss (rayons trop écartés,", font_size=19),
                Text("   trop inclinés), l'image devient floue : ce sont les", font_size=19),
                Text("   aberrations géométriques.", font_size=19),
                Text("• Les constructions de ce chapitre (tracé de rayons)", font_size=19),
                Text("   ne sont donc valables QUE dans ces conditions,", font_size=19),
                Text("   même si on ne le rappelle pas à chaque fois.", font_size=19),
            ).arrange(DOWN, aligned_edge=LEFT, buff=0.14),
            box_width=12.0,
        )
        piege.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Piège à garder en tête : en dehors des conditions de "
                "Gauss, quand les rayons sont trop écartés ou trop "
                "inclinés, l'image devient floue à cause des aberrations "
                "géométriques. Toutes les constructions de tracé de "
                "rayons de ce chapitre ne sont donc valables que dans ces "
                "conditions, même si on ne le rappelle pas à chaque fois."
            )
        ) as tracker:
            self.play(FadeIn(piege))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(piege), FadeOut(titre))
