"""
scenes/Maths_ComposeesTransformationsPlan_07.py — Chapitre 8 « Composées de
transformations du plan » (1ereC, Maths), scène 07.

§ Composée de deux symétries axiales d'axes parallèles : sΔ'∘sΔ = t(2u⃗)
(translation, u⃗ orthogonal aux axes), démonstration, conséquence
(décomposition d'une translation), exemple résolu 3 (Δ:x=1, Δ':x=4).
Source : 1ereC/Maths.pdf, chapitre 8, pages 98-99.
"""

import textwrap

from manim import (
    DOWN,
    LEFT,
    RIGHT,
    UP,
    WHITE,
    YELLOW,
    Arrow,
    Create,
    DashedLine,
    Dot,
    FadeIn,
    FadeOut,
    MathTex,
    Text,
    VGroup,
    Write,
)

from shapes.base_scene import NotionScene
from shapes.boxes import example_box, scene_title, theorem_box, warning_box


def _wrap(text: str, width: int = 56) -> str:
    return "\n".join(textwrap.fill(line, width=width) for line in text.split("\n"))


def _dot_label(point, label, color=WHITE, label_dir=UP, font_size=28, dot_color=YELLOW):
    d = Dot(point, color=dot_color, radius=0.08)
    t = MathTex(label, font_size=font_size, color=color)
    t.next_to(d, label_dir, buff=0.15)
    return VGroup(d, t)


class ComposeeSymetriesAxialesAxesParalleles(NotionScene):
    def construct(self):
        titre = scene_title("Symétries axiales — axes parallèles")
        titre.scale(0.48)
        titre.to_edge(UP)

        # --- Énoncé : théorème fondamental --------------------------------------
        theoreme = theorem_box(
            VGroup(
                Text("Théorème fondamental (axes parallèles)", font_size=24, weight="BOLD"),
                MathTex(r"s_{\Delta'}\circ s_{\Delta} = t_{2\vec u}", font_size=32),
                Text(
                    _wrap("u⃗ est orthogonal aux deux axes, allant de Δ vers Δ' (vecteur reliant les projetés orthogonaux)."),
                    font_size=22,
                ),
            ).arrange(DOWN, buff=0.25)
        )
        theoreme.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Passons aux symétries axiales, en commençant par le cas "
                "où les deux axes delta et delta prime sont parallèles. La "
                "composée s indice delta prime, rond s indice delta, est "
                "encore une translation, de vecteur 2 fois u, où u est le "
                "vecteur orthogonal aux deux axes qui va de delta vers "
                "delta prime — le vecteur reliant les projetés orthogonaux "
                "d'un même point sur les deux droites."
            )
        ) as tracker:
            self.play(Write(titre))
            self.play(FadeIn(theoreme))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(theoreme))

        # --- Raisonnement : démonstration + figure ------------------------------
        etape1 = MathTex(r"H = \text{projet\'e orthogonal de } M \text{ sur } \Delta \implies H \text{ milieu de } [MM_1]", font_size=22)
        etape2 = MathTex(r"H' = \text{projet\'e orthogonal de } M_1 \text{ sur } \Delta' \implies H' \text{ milieu de } [M_1M']", font_size=22)
        etape3 = MathTex(
            r"\text{Th\'eor\`eme des milieux : } \overrightarrow{MM'} = 2\,\overrightarrow{HH'} = 2\vec u",
            font_size=23,
            color=YELLOW,
        )
        demo = VGroup(etape1, etape2, etape3).arrange(DOWN, buff=0.3)
        demo.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "La démonstration reprend exactement l'idée du théorème "
                "des milieux déjà vu pour les symétries centrales. Notons "
                "H le projeté orthogonal de M sur delta : c'est le milieu "
                "de M M-un. Comme les axes sont parallèles, la même "
                "direction perpendiculaire sert à projeter M-un sur delta "
                "prime, en un point H prime, milieu de M-un M prime. Le "
                "théorème des milieux donne alors le vecteur M M prime "
                "égal à deux fois le vecteur H H prime, c'est-à-dire deux "
                "fois u, un vecteur constant orthogonal aux deux axes."
            )
        ) as tracker:
            self.play(Write(etape1))
            self.play(Write(etape2))
            self.play(Write(etape3))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(demo))

        # figure : deux droites verticales parallèles
        delta = DashedLine(UP * 2 + LEFT * 2, DOWN * 2 + LEFT * 2, color="#1E5FA8")
        delta_p = DashedLine(UP * 2 + RIGHT * 1, DOWN * 2 + RIGHT * 1, color="#74458C")
        label_d = MathTex(r"\Delta", font_size=26).next_to(delta, UP, buff=0.15)
        label_dp = MathTex(r"\Delta'", font_size=26).next_to(delta_p, UP, buff=0.15)
        m_pt = LEFT * 3.2 + DOWN * 0.5
        h_pt = LEFT * 2 + DOWN * 0.5
        m1_pt = 2 * h_pt - m_pt
        hp_pt = RIGHT * 1 + DOWN * 0.5
        m2_pt = 2 * hp_pt - m1_pt
        traj = Arrow(m_pt, m2_pt, color=YELLOW, stroke_width=2, buff=0.1, tip_length=0.15)
        pt_m = _dot_label(m_pt, "M", font_size=24)
        pt_m1 = _dot_label(m1_pt, "M_1", font_size=24)
        pt_m2 = _dot_label(m2_pt, "M'", font_size=24)
        figure = VGroup(delta, delta_p, label_d, label_dp, traj, pt_m, pt_m1, pt_m2)
        figure.scale(0.85)
        figure.move_to(DOWN * 0.7)

        with self.voiceover(
            text=(
                "Sur la figure, on observe M se déplacer vers M-un par "
                "réflexion selon delta, puis vers M prime par réflexion "
                "selon delta prime : le trajet global équivaut bien à une "
                "translation horizontale."
            )
        ) as tracker:
            self.play(Create(figure))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(figure))

        # --- Conséquence ---------------------------------------------------------
        consequence = theorem_box(
            Text(
                _wrap(
                    "Conséquence : toute translation se décompose en 2 symétries "
                    "d'axes parallèles perpendiculaires au vecteur, l'un des deux "
                    "axes pouvant être choisi arbitrairement."
                ),
                font_size=22,
            )
        )
        consequence.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Conséquence pratique : toute translation peut se "
                "décomposer en deux symétries d'axes parallèles, "
                "perpendiculaires au vecteur de translation, le premier "
                "axe étant choisi totalement arbitrairement."
            )
        ) as tracker:
            self.play(FadeIn(consequence))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(consequence))

        # --- Exemple résolu 3 -------------------------------------------------
        enonce = MathTex(r"\Delta: x=1, \quad \Delta': x=4, \quad f = s_{\Delta'}\circ s_{\Delta}", font_size=27)
        calc1 = MathTex(r"s_\Delta: x'=2-x,\ y'=y", font_size=25)
        calc2 = MathTex(r"s_{\Delta'}(x',y') : x''=8-x'=8-(2-x)=x+6,\ y''=y", font_size=24)
        calc3 = MathTex(r"f: x''=x+6,\ y''=y \implies f = t_{(6\,;\,0)}", font_size=26, color=YELLOW)
        verif = MathTex(r"\text{V\'erification : } 2\,|4-1| = 6 \ \checkmark", font_size=25)
        exemple = example_box(VGroup(enonce, calc1, calc2, calc3, verif).arrange(DOWN, buff=0.22))
        exemple.next_to(titre, DOWN, buff=0.35)

        with self.voiceover(
            text=(
                "Traitons un exemple analytique complet. Soit delta "
                "d'équation x égale 1, et delta prime d'équation x égale "
                "4. La symétrie par rapport à delta donne x prime égale 2 "
                "moins x, y prime égale y. En appliquant ensuite la "
                "symétrie par rapport à delta prime, on obtient x seconde "
                "égale 8 moins x prime, soit x plus 6, et y seconde égale "
                "y. La composée est donc la translation de vecteur 6, "
                "0. On retrouve bien ce résultat avec le théorème : deux "
                "fois la distance entre les axes, soit deux fois 4 moins "
                "1, donne exactement 6."
            )
        ) as tracker:
            self.play(FadeIn(exemple))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(exemple))

        # --- À retenir + piège --------------------------------------------------
        retenir = theorem_box(MathTex(r"s_{\Delta'}\circ s_{\Delta} = t_{2\vec u} \quad (\Delta \parallel \Delta')", font_size=28))
        retenir.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "À retenir : deux symétries d'axes parallèles se composent "
                "en une translation, de vecteur deux fois le vecteur "
                "orthogonal reliant les axes."
            )
        ) as tracker:
            self.play(FadeIn(retenir))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(retenir))

        piege = warning_box(
            Text(
                _wrap(
                    "Piège : le vecteur de translation vaut 2 fois la distance "
                    "entre les axes, pas la distance elle-même — et il pointe "
                    "de Δ vers Δ', pas l'inverse."
                ),
                font_size=22,
            )
        )
        piege.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Piège classique : ne pas oublier le facteur 2 entre la "
                "distance des axes et la norme du vecteur de translation, "
                "et bien respecter le sens, de delta vers delta prime, "
                "selon l'ordre de composition."
            )
        ) as tracker:
            self.play(FadeIn(piege))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(piege), FadeOut(titre))
