"""
scenes/Physique_EnergiePotentielleElectrostatique_04.py — Chapitre « Énergie
potentielle électrostatique » (1ereC, Physique), scène 04.

Relation U_AB=V_A-V_B=E⃗·AB⃗ (admise), cas particulier d'une même ligne de
champ : E=U/d. Exemple résolu : d=4 cm, U=600 V → E=1,5×10⁴ V/m ; potentiel
d'un point à 1 cm de la plaque positive → V_M=450 V.
Source : 1ereC/Physique.pdf, pages 66-75.
"""

import textwrap

from manim import (
    BLUE,
    DOWN,
    LEFT,
    RED,
    RIGHT,
    UP,
    WHITE,
    YELLOW,
    Arrow,
    Dot,
    FadeIn,
    FadeOut,
    MathTex,
    Rectangle,
    Text,
    VGroup,
    Write,
)

from shapes.base_scene import NotionScene
from shapes.boxes import essentiel_box, example_box, scene_title, theorem_box


def _wrap(text: str, width: int = 56) -> str:
    return "\n".join(textwrap.fill(line, width=width) for line in text.split("\n"))


def _plaques_avec_point(sep: float = 4.6, hauteur: float = 2.6, x_m: float = -1.6):
    plaque_pos = Rectangle(width=0.14, height=hauteur, color=RED, fill_color=RED, fill_opacity=1.0)
    plaque_neg = Rectangle(width=0.14, height=hauteur, color=BLUE, fill_color=BLUE, fill_opacity=1.0)
    plaque_pos.move_to(LEFT * sep / 2)
    plaque_neg.move_to(RIGHT * sep / 2)
    label_pos = Text("+", font_size=28, color=RED).next_to(plaque_pos, UP, buff=0.1)
    label_neg = Text("−", font_size=28, color=BLUE).next_to(plaque_neg, UP, buff=0.1)
    champ = Arrow(
        plaque_pos.get_right() + RIGHT * 0.1,
        plaque_neg.get_left() + LEFT * 0.1,
        color=YELLOW,
        buff=0,
        stroke_width=3,
    )
    label_e = MathTex(r"\vec{E}", font_size=24, color=YELLOW).next_to(champ, UP, buff=0.15)
    point_m = Dot([x_m, 0, 0], color=WHITE, radius=0.07)
    label_m = MathTex("M", font_size=24).next_to(point_m, DOWN, buff=0.15)
    return VGroup(plaque_pos, plaque_neg, label_pos, label_neg, champ, label_e, point_m, label_m)


class RelationChampTensionUniforme(NotionScene):
    def construct(self):
        titre = scene_title("Relation entre champ et tension : E = U / d")
        titre.scale(0.5)
        titre.to_edge(UP)

        # --- Énoncé : théorème général -------------------------------------------------
        theoreme_general = theorem_box(
            MathTex(r"U_{AB} = V_A - V_B = \vec{E} \cdot \vec{AB}", font_size=30),
            box_width=8.4,
        )
        theoreme_general.next_to(titre, DOWN, buff=0.6)

        with self.voiceover(
            text=(
                "Voici une relation fondamentale, admise, qui relie "
                "directement le champ électrostatique et la tension entre "
                "deux points : U A B, égale à V A moins V B, est égal au "
                "produit scalaire de E par AB."
            )
        ) as tracker:
            self.play(FadeIn(theoreme_general))
            self.wait(tracker.get_remaining_duration())

        self.play(theoreme_general.animate.scale(0.7).to_corner(UP + RIGHT).shift(DOWN * 0.2))

        # --- Raisonnement : cas particulier, même ligne de champ ------------------------
        schema = _plaques_avec_point(x_m=-1.4)
        schema.next_to(titre, DOWN, buff=1.0).to_edge(LEFT, buff=0.8)

        explication = Text(
            _wrap(
                "Cas particulier très utile : lorsque A et B sont sur une "
                "même ligne de champ (par exemple sur les deux plaques "
                "d'un condensateur), E⃗ et AB⃗ sont colinéaires.",
                width=46,
            ),
            font_size=20,
        )
        explication.next_to(schema, RIGHT, buff=0.6).align_to(schema, UP)

        with self.voiceover(
            text=(
                "Plaçons-nous dans le cas particulier, très fréquent, où A "
                "et B sont situés sur une même ligne de champ — par "
                "exemple sur les deux plaques d'un condensateur plan. Dans "
                "ce cas, le vecteur champ E et le vecteur déplacement AB "
                "sont colinéaires, exactement de même direction."
            )
        ) as tracker:
            self.play(FadeIn(schema))
            self.play(Write(explication))
            self.wait(tracker.get_remaining_duration())

        theoreme_e_u_d = MathTex(r"E = \dfrac{U}{d}", font_size=34, color=YELLOW)
        legende_e_u_d = Text(
            "d = distance AB le long de la ligne de champ, U = U_AB > 0",
            font_size=18,
        )
        bloc_e_u_d = VGroup(theoreme_e_u_d, legende_e_u_d).arrange(DOWN, buff=0.25)
        bloc_e_u_d.next_to(schema, DOWN, buff=0.6)

        with self.voiceover(
            text=(
                "Le produit scalaire se simplifie alors en un simple "
                "produit de normes, puisque les vecteurs sont colinéaires "
                "et de même sens : on obtient le théorème E égale U sur d, "
                "où d est la distance AB mesurée le long de la ligne de "
                "champ, et U la tension U A B, prise positive dans ce "
                "sens."
            )
        ) as tracker:
            self.play(Write(theoreme_e_u_d))
            self.play(Write(legende_e_u_d))
            self.wait(tracker.get_remaining_duration())

        self.play(
            FadeOut(schema),
            FadeOut(explication),
            FadeOut(bloc_e_u_d),
            FadeOut(theoreme_general),
        )

        # --- Exemple résolu 3 ------------------------------------------------------------
        enonce = Text(
            _wrap(
                "Exemple : les plaques d'un condensateur sont distantes de "
                "d=4 cm, sous une tension U=600 V. Calculer E, puis le "
                "potentiel d'un point M situé à 1 cm de la plaque "
                "positive.",
                width=54,
            ),
            font_size=21,
        )
        enonce.next_to(titre, DOWN, buff=0.7)

        with self.voiceover(
            text=(
                "Exemple d'application. Les plaques d'un condensateur sont "
                "distantes de 4 centimètres, et soumises à une tension de "
                "600 volts. Calculons d'abord le champ E, puis le "
                "potentiel d'un point M situé à 1 centimètre de la plaque "
                "positive."
            )
        ) as tracker:
            self.play(Write(enonce))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(enonce))

        calcul_e = example_box(
            MathTex(
                r"E = \dfrac{U}{d} = \dfrac{600}{0{,}04} = 1{,}5\times10^{4}\ \text{V/m}",
                font_size=27,
            ),
            box_width=8.8,
        )
        calcul_e.next_to(titre, DOWN, buff=0.6)

        with self.voiceover(
            text=(
                "Le champ vaut U sur d, soit 600 divisé par 0 virgule 04, "
                "ce qui donne 1 virgule 5 fois 10 puissance 4 volts par "
                "mètre."
            )
        ) as tracker:
            self.play(FadeIn(calcul_e))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(calcul_e))

        calcul_v = example_box(
            VGroup(
                Text(
                    "En prenant V(plaque −)=0, le potentiel décroît linéairement :",
                    font_size=19,
                ),
                MathTex(
                    r"V_+ = U = 600\ \text{V}, \quad V_M = V_+ - E\times x_M",
                    font_size=24,
                ),
                MathTex(
                    r"V_M = 600 - 1{,}5\times10^{4}\times 0{,}01 = 450\ \text{V}",
                    font_size=26,
                    color=YELLOW,
                ),
            ).arrange(DOWN, buff=0.28),
            box_width=10.6,
        )
        calcul_v.next_to(titre, DOWN, buff=0.6)

        with self.voiceover(
            text=(
                "Prenons la plaque négative comme référence de potentiel "
                "nul. La plaque positive est alors au potentiel 600 volts, "
                "et le potentiel décroît linéairement à mesure qu'on "
                "s'éloigne de cette plaque. Le point M, situé à 1 "
                "centimètre de la plaque positive, est donc au potentiel "
                "600 moins 1 virgule 5 fois 10 puissance 4 fois 0 virgule "
                "01, soit 450 volts."
            )
        ) as tracker:
            self.play(FadeIn(calcul_v))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(calcul_v))

        # --- À retenir --------------------------------------------------------------------
        retenir = essentiel_box(
            Text(
                _wrap(
                    "U_AB=E⃗·AB⃗ en général. Sur une même ligne de champ : "
                    "E=U/d, avec d la distance AB et U=U_AB>0. Le potentiel "
                    "décroît linéairement le long d'une ligne de champ.",
                    width=56,
                ),
                font_size=21,
            )
        )
        retenir.next_to(titre, DOWN, buff=0.6)

        with self.voiceover(
            text=(
                "À retenir : la relation générale U A B égale E fois AB, "
                "et son cas particulier E égale U sur d, valable seulement "
                "sur une même ligne de champ, avec d la distance AB et U la "
                "tension U A B positive. Le potentiel décroît linéairement "
                "le long d'une ligne de champ."
            )
        ) as tracker:
            self.play(FadeIn(retenir))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(titre), FadeOut(retenir))
