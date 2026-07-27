"""
scenes/Physique_TravailPuissanceRotation_02.py — Chapitre 2 « Travail et
puissance dans le cas d'un mouvement de rotation autour d'un axe fixe »
(1ereC, Physique), scène 02.

§ Moment d'une force par rapport à un axe fixe : mise en évidence
(expérience de la porte) et définition ℳΔ(F⃗) = ± F × d, bras de levier
d = OA × sin(α), cas particuliers (perpendiculaire, droite d'action
passant par l'axe ou parallèle à l'axe).
Source : 1ereC/Physique.pdf, chapitre 2, pages 13-23.
"""

import textwrap

from manim import (
    DOWN,
    LEFT,
    RIGHT,
    UP,
    WHITE,
    YELLOW,
    Arc,
    Create,
    Dot,
    FadeIn,
    FadeOut,
    Line,
    MathTex,
    Text,
    VGroup,
    Vector,
    Write,
)

from shapes.base_scene import NotionScene
from shapes.boxes import definition_box, essentiel_box, example_box, scene_title, warning_box


def _wrap(text: str, width: int = 58) -> str:
    return "\n".join(textwrap.fill(line, width=width) for line in text.split("\n"))


def _dot_label(point, label, color=WHITE, label_dir=UP, font_size=26, dot_color=YELLOW):
    d = Dot(point, color=dot_color, radius=0.07)
    t = MathTex(label, font_size=font_size, color=color)
    t.next_to(d, label_dir, buff=0.15)
    return VGroup(d, t)


class MomentForceMiseEvidenceDefinition(NotionScene):
    def construct(self):
        titre = scene_title("Moment d'une force par rapport à un axe")
        titre.scale(0.5)
        titre.to_edge(UP)

        # --- Énoncé : expérience de la porte -----------------------------------
        enonce = Text(
            _wrap(
                "Pourquoi pousse-t-on une porte loin des gonds, et pourquoi "
                "pousser vers les gonds ne l'ouvre-t-elle jamais ?",
                width=54,
            ),
            font_size=24,
            color=YELLOW,
        )
        enonce.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Poussons une porte : plus on pousse loin des gonds, plus "
                "elle s'ouvre facilement. Mais si l'on pousse vers les "
                "gonds, ou droit vers eux, la porte ne bouge pas du tout. "
                "Cette expérience très simple va nous permettre de définir "
                "le moment d'une force par rapport à un axe."
            )
        ) as tracker:
            self.play(Write(titre))
            self.play(FadeIn(enonce))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(enonce))

        # --- Raisonnement : schéma de la porte vue de dessus -------------------
        gond = LEFT * 4.5 + DOWN * 0.5
        bout = RIGHT * 1.5 + DOWN * 0.5
        porte = Line(gond, bout, color=WHITE, stroke_width=6)
        axe_pt = _dot_label(gond, r"\text{axe }\Delta", label_dir=DOWN, dot_color="#288073")
        a_pt = _dot_label(bout, "A", label_dir=UP)
        f_eff = Vector(UP * 1.3, color="#DE7C1F").shift(bout)
        f_eff_label = MathTex(r"\vec{F}", font_size=26, color="#DE7C1F").next_to(f_eff, RIGHT, buff=0.1)
        schema1 = VGroup(porte, axe_pt, a_pt, f_eff, f_eff_label)
        schema1.scale(0.85).move_to(DOWN * 0.6)

        with self.voiceover(
            text=(
                "Poussée perpendiculairement à la porte, en A, loin de "
                "l'axe des gonds, la force F fait tourner la porte : elle "
                "a un effet de rotation maximal."
            )
        ) as tracker:
            self.play(Create(schema1))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(schema1))

        gond2 = LEFT * 4.5 + DOWN * 0.5
        bout2 = RIGHT * 1.5 + DOWN * 0.5
        porte2 = Line(gond2, bout2, color=WHITE, stroke_width=6)
        axe_pt2 = _dot_label(gond2, r"\text{axe }\Delta", label_dir=DOWN, dot_color="#288073")
        a_pt2 = _dot_label(bout2, "A", label_dir=UP)
        f_nul = Vector(LEFT * 1.3, color="#B42E41").shift(bout2)
        f_nul_label = MathTex(r"\vec{F}", font_size=26, color="#B42E41").next_to(f_nul, UP, buff=0.1)
        schema2 = VGroup(porte2, axe_pt2, a_pt2, f_nul, f_nul_label)
        schema2.scale(0.85).move_to(DOWN * 0.6)

        with self.voiceover(
            text=(
                "Mais si l'on pousse en A dans la direction de la porte "
                "elle-même — c'est-à-dire le long de la droite qui passe "
                "par l'axe — la force n'a plus aucun effet de rotation : "
                "son moment est nul."
            )
        ) as tracker:
            self.play(Create(schema2))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(schema2))

        # --- Définition ---------------------------------------------------------
        defn = definition_box(
            VGroup(
                Text("Moment d'une force par rapport à un axe Δ", font_size=22, weight="BOLD"),
                MathTex(r"\mathcal{M}_\Delta(\vec{F}) = \pm\, F \times d \quad (\text{en N} \cdot \text{m})", font_size=27),
                Text(
                    "d = bras de levier : distance perpendiculaire entre l'axe et la droite d'action de F⃗.",
                    font_size=21,
                ),
                MathTex(r"d = OA \times \sin(\alpha)", font_size=26),
            ).arrange(DOWN, buff=0.25),
            box_width=10.6,
        )
        defn.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Le moment de la force F par rapport à l'axe delta se "
                "note ℳ delta de F vecteur, et vaut plus ou moins F fois "
                "d, en newton-mètre. Le bras de levier d est la distance "
                "perpendiculaire entre l'axe et la droite d'action de la "
                "force. Concrètement, si O est le pied de l'axe et A le "
                "point d'application, avec alpha l'angle entre O A et la "
                "force, on calcule d égale O A fois sinus de alpha."
            )
        ) as tracker:
            self.play(FadeIn(defn))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(defn))

        # --- Schéma du bras de levier (calcul pratique) -------------------------
        o_pt = LEFT * 3.0 + DOWN * 0.4
        a_pt3 = o_pt + RIGHT * 2.6 + UP * 0.4
        droite_action = Line(a_pt3 + LEFT * 0.3 + DOWN * 0.55, a_pt3 + RIGHT * 1.6 + UP * 1.05, color="#DE7C1F", stroke_width=3)
        oa_seg = Line(o_pt, a_pt3, color=WHITE, stroke_width=3)
        force_vec = Vector((a_pt3 + RIGHT * 1.6 + UP * 1.05 - a_pt3), color="#DE7C1F").shift(a_pt3)
        arc_alpha = Arc(radius=0.5, start_angle=oa_seg.get_angle(), angle=droite_action.get_angle() - oa_seg.get_angle(), arc_center=a_pt3, color=YELLOW)
        o_lbl = _dot_label(o_pt, "O", label_dir=DOWN, dot_color="#288073")
        a_lbl = _dot_label(a_pt3, "A", label_dir=UP)
        schema3 = VGroup(oa_seg, droite_action, force_vec, arc_alpha, o_lbl, a_lbl)
        schema3.scale(0.9).move_to(DOWN * 0.7 + LEFT * 1.0)

        cas_part = VGroup(
            Text("Cas particuliers :", font_size=22, weight="BOLD"),
            Text("• F⃗ ⟂ OA : d = OA (moment maximal)", font_size=21),
            Text("• droite d'action passant par l'axe, ou parallèle à Δ : d = 0", font_size=21),
        ).arrange(DOWN, buff=0.2, aligned_edge=LEFT)
        cas_part.next_to(schema3, RIGHT, buff=0.6)

        with self.voiceover(
            text=(
                "En pratique, on trace le segment O A puis la droite "
                "d'action de la force, et on mesure l'angle alpha entre "
                "les deux pour obtenir d égale O A fois sinus alpha. Deux "
                "cas particuliers à connaître : si la force est "
                "perpendiculaire à O A, le bras de levier est maximal et "
                "vaut O A tout entier ; et si la droite d'action passe par "
                "l'axe, ou lui est parallèle, le bras de levier est nul, "
                "donc le moment aussi."
            )
        ) as tracker:
            self.play(Create(schema3))
            self.play(FadeIn(cas_part))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(schema3), FadeOut(cas_part))

        # --- Exemple traité -----------------------------------------------------
        exemple = example_box(
            VGroup(
                Text("Exemple — porte de largeur OA = 0,9 m, poignée poussée à α = 90° :", font_size=20),
                Text("Force F = 15 N, appliquée perpendiculairement à la porte.", font_size=20),
                MathTex(r"d = OA \times \sin(90^\circ) = 0{,}9\ \text{m}", font_size=25),
                MathTex(r"\mathcal{M}_\Delta(\vec{F}) = F \times d = 15 \times 0{,}9 = 13{,}5\ \text{N} \cdot \text{m}", font_size=25),
            ).arrange(DOWN, buff=0.28),
            box_width=11.2,
        )
        exemple.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Exemple : une porte de largeur zéro virgule neuf mètre, "
                "poussée perpendiculairement, avec une force de quinze "
                "newtons appliquée sur la poignée. L'angle alpha vaut "
                "quatre-vingt-dix degrés, donc le bras de levier est égal "
                "à O A tout entier, soit zéro virgule neuf mètre. Le "
                "moment de la force vaut alors F fois d, soit quinze fois "
                "zéro virgule neuf, c'est-à-dire treize virgule cinq "
                "newton-mètre."
            )
        ) as tracker:
            self.play(FadeIn(exemple))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(exemple))

        # --- À retenir ------------------------------------------------------------
        retenir = essentiel_box(
            Text(
                _wrap(
                    "ℳΔ(F⃗) = ±F×d, avec d le bras de levier (distance "
                    "perpendiculaire de l'axe à la droite d'action), "
                    "calculé par d = OA sin(α).",
                    width=58,
                ),
                font_size=22,
            )
        )
        retenir.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "À retenir : le moment d'une force par rapport à un axe "
                "vaut plus ou moins F fois d, où d, le bras de levier, est "
                "la distance perpendiculaire entre l'axe et la droite "
                "d'action de la force, calculée par d égale O A fois "
                "sinus alpha."
            )
        ) as tracker:
            self.play(FadeIn(retenir))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(retenir))

        # --- Piège ------------------------------------------------------------------
        piege = warning_box(
            Text(
                _wrap(
                    "Piège : le moment se mesure en newton-mètre (N·m), "
                    "jamais en joules — même si les unités semblent "
                    "similaires, ce n'est pas un travail ni une énergie."
                ),
                font_size=22,
            )
        )
        piege.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Piège fréquent : le moment d'une force se mesure en "
                "newton-mètre, jamais en joules. Même si les unités "
                "paraissent similaires, un moment n'est ni un travail, ni "
                "une énergie — c'est une grandeur qui caractérise l'effet "
                "de rotation d'une force."
            )
        ) as tracker:
            self.play(FadeIn(piege))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(piege), FadeOut(titre))
