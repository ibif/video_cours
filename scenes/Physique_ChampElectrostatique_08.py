"""
scenes/Physique_ChampElectrostatique_08.py — Chapitre 6 « Champ
électrostatique » (1ereC, Physique), scène 08.

§ Force subie par une charge placée dans un champ électrostatique :
théorème F⃗=qE⃗ (norme F=|q|·E), caractéristiques selon le signe de q,
conséquences (particule accélérée/déviée dans un champ uniforme, poids
souvent négligeable pour les particules élémentaires). Exemple résolu 5 :
dans le champ E=2×10⁴V/m (exemple précédent), comparaison de la force sur
q=+2nC et sur un électron, comparaison avec le poids de l'électron
(rapport F/P≈3,5×10¹⁴).
Source : 1ereC/Physique.pdf, pages 54-65 (chapitre 6, § 6).
"""

import textwrap

from manim import (
    DOWN,
    LEFT,
    RIGHT,
    UP,
    WHITE,
    YELLOW,
    RED,
    BLUE,
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
from shapes.boxes import definition_box, essentiel_box, example_box, scene_title, theorem_box, warning_box


def _wrap(text: str, width: int = 56) -> str:
    return "\n".join(textwrap.fill(line, width=width) for line in text.split("\n"))


class ForceChargeChampElectrostatique(NotionScene):
    def construct(self):
        titre = scene_title("Force subie par une charge dans un champ")
        titre.scale(0.48)
        titre.to_edge(UP)

        # --- Énoncé : que devient une charge placée dans un champ ? --------------
        mise_en_situation = Text(
            _wrap(
                "On place une charge q en un point M où règne un champ "
                "électrostatique E⃗(M). Quelle force cette charge "
                "subit-elle ?",
                width=52,
            ),
            font_size=23,
        )
        mise_en_situation.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "On place une charge q en un point M où règne un champ "
                "électrostatique E de M. Quelle force cette charge "
                "subit-elle ? La réponse découle directement de la "
                "définition même du vecteur champ, vue précédemment."
            )
        ) as tracker:
            self.play(Write(titre))
            self.play(FadeIn(mise_en_situation))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(mise_en_situation))

        # --- Théorème : F = qE ---------------------------------------------------------
        theoreme = theorem_box(
            VGroup(
                Text("Force électrique subie par une charge q", font_size=22, weight="BOLD"),
                MathTex(r"\vec{F} = q\, \vec{E}(M) \qquad F = |q|\, E", font_size=30),
                Text("(conséquence immédiate de E⃗(M) = F⃗/q)", font_size=18),
            ).arrange(DOWN, buff=0.22),
            box_width=10.8,
        )
        theoreme.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Puisque le champ E de M a justement été défini comme F "
                "sur q, on en déduit directement que la force subie par "
                "une charge q placée en M vaut F égale q fois E de M, de "
                "norme F égale la valeur absolue de q, fois E."
            )
        ) as tracker:
            self.play(FadeIn(theoreme))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(theoreme))

        # --- Caractéristiques selon le signe de q ---------------------------------------
        e_vec = Arrow(LEFT * 3.0, LEFT * 1.0, buff=0.1, color=YELLOW, stroke_width=3)
        e_label = MathTex(r"\vec{E}", font_size=24, color=YELLOW).next_to(e_vec, UP, buff=0.1)
        q_pos_pt = Dot(LEFT * 2.0, color=RED, radius=0.12)
        f_pos = Arrow(q_pos_pt.get_center(), q_pos_pt.get_center() + RIGHT * 1.2, buff=0.15, color=BLUE, stroke_width=3)
        f_pos_label = MathTex(r"\vec{F} = q\vec{E}\ (q>0)", font_size=20, color=BLUE).next_to(f_pos, DOWN, buff=0.35)
        groupe_pos = VGroup(e_vec, e_label, q_pos_pt, f_pos, f_pos_label)
        groupe_pos.move_to(LEFT * 2.5 + UP * 0.3)

        e_vec2 = Arrow(RIGHT * 1.0, RIGHT * 3.0, buff=0.1, color=YELLOW, stroke_width=3)
        e_label2 = MathTex(r"\vec{E}", font_size=24, color=YELLOW).next_to(e_vec2, UP, buff=0.1)
        q_neg_pt = Dot(RIGHT * 2.0, color=BLUE, radius=0.12)
        f_neg = Arrow(q_neg_pt.get_center(), q_neg_pt.get_center() + LEFT * 1.2, buff=0.15, color=RED, stroke_width=3)
        f_neg_label = MathTex(r"\vec{F} = q\vec{E}\ (q<0)", font_size=20, color=RED).next_to(f_neg, DOWN, buff=0.35)
        groupe_neg = VGroup(e_vec2, e_label2, q_neg_pt, f_neg, f_neg_label)
        groupe_neg.move_to(RIGHT * 2.5 + UP * 0.3)

        schema = VGroup(groupe_pos, groupe_neg)
        schema.next_to(titre, DOWN, buff=0.6)

        with self.voiceover(
            text=(
                "Le sens de cette force dépend directement du signe de la "
                "charge. Si q est positive, la force F est dans le même "
                "sens que le champ E. Si q est négative, la force F "
                "pointe en sens opposé au champ E."
            )
        ) as tracker:
            self.play(Create(groupe_pos))
            self.play(Create(groupe_neg))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(schema))

        # --- Conséquences : accélération, déviation, poids négligeable -----------------
        consequences = definition_box(
            VGroup(
                Text("Conséquences", font_size=22, weight="BOLD"),
                Text("• Une particule chargée pénétrant dans un champ", font_size=19),
                Text("   uniforme est accélérée ou déviée par la force qE⃗.", font_size=19),
                Text("• Pour les particules élémentaires (électron, proton…),", font_size=19),
                Text("   le poids est presque toujours négligeable devant", font_size=19),
                Text("   la force électrique.", font_size=19),
            ).arrange(DOWN, aligned_edge=LEFT, buff=0.16),
            box_width=11.6,
        )
        consequences.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Cela a deux conséquences importantes. D'abord, une "
                "particule chargée qui pénètre dans un champ uniforme est "
                "accélérée, ou déviée, sous l'effet de la force q E. "
                "Ensuite, pour les particules élémentaires comme "
                "l'électron ou le proton, le poids est presque toujours "
                "totalement négligeable devant la force électrique, en "
                "raison de leur masse extrêmement faible."
            )
        ) as tracker:
            self.play(FadeIn(consequences))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(consequences))

        # --- Exemple résolu 5 : force sur q et sur un électron -------------------------
        exemple = example_box(
            VGroup(
                Text("Dans le champ E = 2×10⁴ V/m (armatures, exemple précédent) :", font_size=18),
                MathTex(r"q = +2\ \text{nC} : \ F = qE = 4\times 10^{-5}\ \text{N}", font_size=21),
                MathTex(r"\text{électron} : \ F = eE = 1{,}6\times 10^{-19}\times 2\times 10^4 = 3{,}2\times 10^{-15}\ \text{N}", font_size=19),
                MathTex(r"\text{Poids de l'électron : } P = m_e g \approx 8{,}9\times 10^{-30}\ \text{N}", font_size=19),
                MathTex(r"\dfrac{F}{P} \approx 3{,}5\times 10^{14} \ \Rightarrow\ \text{poids totalement négligeable}", font_size=21, color=YELLOW),
            ).arrange(DOWN, buff=0.2),
            box_width=12.6,
        )
        exemple.next_to(titre, DOWN, buff=0.35)

        with self.voiceover(
            text=(
                "Exemple résolu : reprenons le champ de deux fois dix "
                "puissance quatre volts par mètre entre les armatures de "
                "l'exemple précédent. Une charge de plus deux "
                "nanocoulombs y subit une force de quatre fois dix "
                "puissance moins cinq newton. Un électron, de charge moins "
                "e, y subit une force de trois virgule deux fois dix "
                "puissance moins quinze newton. Or le poids de l'électron "
                "vaut seulement huit virgule neuf fois dix puissance "
                "moins trente newton. Le rapport de la force électrique "
                "sur le poids atteint environ trois virgule cinq fois dix "
                "puissance quatorze : le poids de l'électron est donc "
                "totalement négligeable devant la force électrique."
            )
        ) as tracker:
            self.play(FadeIn(exemple))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(exemple))

        # --- À retenir -----------------------------------------------------------------
        retenir = essentiel_box(
            VGroup(
                Text("À retenir", font_size=24, weight="BOLD"),
                MathTex(r"\vec{F} = q\,\vec{E} \qquad F = |q|\,E", font_size=28),
                Text("Sens de F⃗ = sens de E⃗ si q>0, sens opposé si q<0.", font_size=20),
                Text("Poids d'une particule élémentaire : quasi toujours négligeable.", font_size=20),
            ).arrange(DOWN, buff=0.22),
            box_width=12.4,
        )
        retenir.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Retenons l'essentiel : la force subie par une charge q "
                "placée dans un champ E vaut F égale q E, de norme la "
                "valeur absolue de q fois E. Elle est dans le sens du "
                "champ si q est positive, en sens opposé si q est "
                "négative. Et pour une particule élémentaire, le poids "
                "est presque toujours totalement négligeable devant "
                "cette force électrique."
            )
        ) as tracker:
            self.play(FadeIn(retenir))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(retenir), FadeOut(titre))
