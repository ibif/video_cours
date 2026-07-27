"""
scenes/Physique_PuissanceEnergieElectriques_03.py — Chapitre 8 « Puissance
et énergie électriques » (1ereC, Physique), scène 03.

§ 3. Effet Joule (échauffement d'un conducteur traversé par un courant :
utile, néfaste ou protecteur selon le contexte) et loi d'Ohm U=RI pour un
résistor (ohm Ω), conductance G=1/R (siemens). Loi de Joule, établie à
partir de W=UIt et U=RI : W_J=RI²t, puissance P_J=RI²=U²/R=UI — piège :
cette dernière écriture n'est valable QUE pour un conducteur ohmique.
Exemple résolu : R=20 Ω, I=2 A pendant 10 min → U=40 V, P_J=80 W,
W_J=48 000 J.
Source : 1ereC/Physique.pdf, pages 76-87 (chapitre 8, § 3).
"""

import textwrap

from manim import (
    DOWN,
    LEFT,
    ORANGE,
    RIGHT,
    UP,
    WHITE,
    YELLOW,
    FadeIn,
    FadeOut,
    Line,
    MathTex,
    Rectangle,
    Text,
    VGroup,
    Write,
)

from shapes.base_scene import NotionScene
from shapes.boxes import definition_box, essentiel_box, example_box, scene_title, theorem_box, warning_box


def _wrap(text: str, width: int = 56) -> str:
    return "\n".join(textwrap.fill(line, width=width) for line in text.split("\n"))


def _resistor_schema():
    """Résistor (rectangle) traversé par un courant, avec des petites
    lignes ondulées de chaleur au-dessus pour figurer l'effet Joule."""
    corps = Rectangle(width=2.2, height=0.7, color=WHITE, stroke_width=3)
    label = Text("R", font_size=26, color=WHITE).move_to(corps.get_center())
    fil_g = Line(corps.get_left() + LEFT * 1.2, corps.get_left(), stroke_width=3, color=WHITE)
    fil_d = Line(corps.get_right(), corps.get_right() + RIGHT * 1.2, stroke_width=3, color=WHITE)

    chaleur = VGroup()
    for dx in (-0.6, 0.0, 0.6):
        onde = VGroup(
            Line(corps.get_top() + RIGHT * dx + UP * 0.05, corps.get_top() + RIGHT * (dx - 0.12) + UP * 0.3, stroke_width=2, color=ORANGE),
            Line(corps.get_top() + RIGHT * (dx - 0.12) + UP * 0.3, corps.get_top() + RIGHT * (dx + 0.12) + UP * 0.55, stroke_width=2, color=ORANGE),
        )
        chaleur.add(onde)

    return VGroup(fil_g, corps, label, fil_d, chaleur)


class EffetJouleLoiOhm(NotionScene):
    def construct(self):
        titre = scene_title("Effet Joule et loi d'Ohm")
        titre.scale(0.5)
        titre.to_edge(UP)

        # --- Énoncé -----------------------------------------------------------
        mise_en_situation = Text(
            _wrap(
                "Un fil de résistor chauffe quand un courant le traverse. "
                "Ce fer à repasser transforme utilement cet échauffement, "
                "alors qu'un fil électrique qui chauffe trop est un danger. "
                "D'où vient cette énergie thermique, et comment la "
                "calculer ?",
                width=56,
            ),
            font_size=22,
        )
        mise_en_situation.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Un fil résistif chauffe dès qu'un courant électrique le "
                "traverse. Dans un fer à repasser, cet échauffement est "
                "utile ; dans un fil électrique trop fin, il devient un "
                "danger. D'où vient cette énergie thermique, et comment la "
                "calculer précisément ?"
            )
        ) as tracker:
            self.play(Write(titre))
            self.play(FadeIn(mise_en_situation))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(mise_en_situation))

        # --- Effet Joule + loi d'Ohm --------------------------------------------
        schema = _resistor_schema()
        schema.next_to(titre, DOWN, buff=0.6)

        definition_joule = definition_box(
            VGroup(
                Text("Effet Joule : échauffement d'un conducteur traversé", font_size=21),
                Text("par un courant électrique — utile (fer à repasser),", font_size=21),
                Text("néfaste (pertes en ligne) ou protecteur (fusible).", font_size=21),
            ).arrange(DOWN, aligned_edge=LEFT, buff=0.16),
            box_width=11.0,
        )
        definition_joule.next_to(schema, DOWN, buff=0.3)

        with self.voiceover(
            text=(
                "On appelle effet Joule l'échauffement d'un conducteur "
                "traversé par un courant électrique. Selon le contexte, cet "
                "effet peut être utile, comme dans un fer à repasser ou une "
                "bouilloire ; néfaste, comme les pertes d'énergie dans les "
                "lignes électriques ; ou protecteur, comme dans un fusible "
                "qui fond volontairement en cas de surintensité."
            )
        ) as tracker:
            self.play(FadeIn(schema))
            self.play(FadeIn(definition_joule))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(schema), FadeOut(definition_joule))

        loi_ohm = theorem_box(
            VGroup(
                Text("Loi d'Ohm (conducteur ohmique)", font_size=23, weight="BOLD"),
                MathTex(r"U = R \, I", font_size=32),
                Text("R en ohms (Ω) : résistance du résistor.", font_size=20),
                MathTex(r"G = \dfrac{1}{R}\ \ (\text{conductance, en siemens S})", font_size=24),
            ).arrange(DOWN, buff=0.2),
            box_width=11.4,
        )
        loi_ohm.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Pour un résistor, encore appelé conducteur ohmique, la loi "
                "d'Ohm relie la tension à ses bornes et l'intensité qui le "
                "traverse : U égale R I, où R, la résistance, s'exprime en "
                "ohms. On définit aussi la conductance G, inverse de la "
                "résistance, G égale un sur R, qui s'exprime en siemens."
            )
        ) as tracker:
            self.play(FadeIn(loi_ohm))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(loi_ohm))

        # --- Loi de Joule : démonstration -----------------------------------------
        demonstration = VGroup(
            Text("Partons de l'énergie électrique d'un dipôle :", font_size=21),
            MathTex(r"W = U \, I \, t", font_size=28),
            Text("Pour un résistor, U = RI, donc :", font_size=21),
            MathTex(r"W_J = (R I) \times I \times t = R \, I^2 \, t", font_size=28, color=YELLOW),
            Text("En divisant par t, la puissance dissipée par effet Joule :", font_size=21),
            MathTex(r"P_J = R I^2 = \dfrac{U^2}{R} = U I", font_size=28, color=YELLOW),
        ).arrange(DOWN, buff=0.2)
        demonstration.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Établissons la loi de Joule. On part de l'énergie "
                "électrique générale d'un dipôle, W égale U I t. Pour un "
                "résistor, la loi d'Ohm donne U égale R I, donc l'énergie "
                "dissipée par effet Joule vaut W J égale R I au carré, "
                "fois t. En divisant par la durée, la puissance dissipée "
                "s'écrit P J égale R I carré, ce qui équivaut aussi à U "
                "carré sur R, ou encore à U I."
            )
        ) as tracker:
            self.play(FadeIn(demonstration))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(demonstration))

        # --- Exemple résolu 2 -------------------------------------------------------
        exemple = example_box(
            VGroup(
                Text("Un résistor R = 20 Ω est traversé par I = 2 A pendant t = 10 min.", font_size=20),
                MathTex(r"U = R \, I = 20 \times 2 = 40\ \text{V}", font_size=27),
                MathTex(r"P_J = R \, I^2 = 20 \times 2^2 = 80\ \text{W}", font_size=27),
                MathTex(r"t = 600\ \text{s} \Rightarrow W_J = P_J \, t = 80 \times 600 = 48\,000\ \text{J}", font_size=25),
            ).arrange(DOWN, buff=0.25),
            box_width=12.2,
        )
        exemple.next_to(titre, DOWN, buff=0.35)

        with self.voiceover(
            text=(
                "Exemple résolu : un résistor de vingt ohms est traversé "
                "par un courant de deux ampères pendant dix minutes. La "
                "tension à ses bornes vaut R I, soit vingt fois deux, "
                "quarante volts. La puissance Joule vaut R I carré, soit "
                "vingt fois quatre, quatre-vingts watts. En convertissant "
                "dix minutes en six cents secondes, l'énergie dissipée par "
                "effet Joule vaut quarante-huit mille joules."
            )
        ) as tracker:
            self.play(FadeIn(exemple))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(exemple))

        # --- À retenir -------------------------------------------------------------
        retenir = essentiel_box(
            VGroup(
                Text("À retenir", font_size=24, weight="BOLD"),
                MathTex(r"U = R I, \qquad P_J = R I^2 = \dfrac{U^2}{R} = U I", font_size=26),
                Text("Ces trois écritures de P_J supposent un conducteur ohmique.", font_size=19),
            ).arrange(DOWN, buff=0.24),
            box_width=11.8,
        )
        retenir.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Retenons l'essentiel : la loi d'Ohm s'écrit U égale R I, "
                "et la puissance dissipée par effet Joule s'écrit R I "
                "carré, égale aussi U carré sur R, égale aussi U I — trois "
                "écritures équivalentes, mais valables seulement pour un "
                "conducteur ohmique."
            )
        ) as tracker:
            self.play(FadeIn(retenir))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(retenir))

        # --- Pièges à éviter --------------------------------------------------------
        pieges = warning_box(
            VGroup(
                Text("⚠ P = UI est valable pour TOUT dipôle. Mais les écritures", font_size=20),
                Text("   P_J = RI² et P_J = U²/R ne sont valables QUE pour un", font_size=20),
                Text("   conducteur ohmique (résistor) — jamais pour un moteur", font_size=20),
                Text("   ou un générateur, où U ≠ RI en général.", font_size=20),
            ).arrange(DOWN, aligned_edge=LEFT, buff=0.16),
            box_width=12.2,
        )
        pieges.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Attention à ce piège classique : la formule P égale U I "
                "est valable pour tout dipôle, sans exception. Mais les "
                "écritures P J égale R I carré et P J égale U carré sur R "
                "ne sont valables que pour un conducteur ohmique, un "
                "résistor. Elles ne s'appliquent jamais directement à un "
                "moteur ou à un générateur, où la tension n'est pas "
                "proportionnelle au courant."
            )
        ) as tracker:
            self.play(FadeIn(pieges))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(pieges), FadeOut(titre))
