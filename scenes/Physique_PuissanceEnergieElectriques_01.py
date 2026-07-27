"""
scenes/Physique_PuissanceEnergieElectriques_01.py — Chapitre 8 « Puissance et
énergie électriques » (1ereC, Physique), scène 01.

§ 1. Rappels : courant électrique (mouvement ordonné de porteurs de
charge), intensité I=Q/Δt (ampère, ampèremètre en série), tension
U_AB=V_A-V_B (volt, voltmètre en dérivation), dipôles actifs (générateurs)
et passifs (résistors, lampes), conventions récepteur (flèches I et U
opposées) et générateur (flèches de même sens).
Source : 1ereC/Physique.pdf, pages 76-87 (chapitre 8, § 1).
"""

import textwrap

from manim import (
    DOWN,
    LEFT,
    RED,
    RIGHT,
    UP,
    WHITE,
    YELLOW,
    Arrow,
    Circle,
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
from shapes.boxes import definition_box, essentiel_box, example_box, scene_title, warning_box


def _wrap(text: str, width: int = 56) -> str:
    return "\n".join(textwrap.fill(line, width=width) for line in text.split("\n"))


def _circuit_ampere():
    """Boucle simple générateur + lampe, avec un ampèremètre inséré EN
    SÉRIE dans le fil (construit uniquement avec Line/Rectangle/Circle)."""
    tl = UP * 1.0 + LEFT * 2.6
    tr = UP * 1.0 + RIGHT * 2.6
    bl = DOWN * 1.0 + LEFT * 2.6
    br = DOWN * 1.0 + RIGHT * 2.6

    fil_gauche = Line(tl, bl, stroke_width=3, color=WHITE)
    fil_bas = Line(bl, br, stroke_width=3, color=WHITE)

    # Générateur (pile) sur le côté droit
    gen_h = 0.6
    gen_mid = (tr + br) / 2
    gen = VGroup(
        Line(gen_mid + UP * gen_h / 2 + LEFT * 0.25, gen_mid + UP * gen_h / 2 + RIGHT * 0.25, stroke_width=5, color=WHITE),
        Line(gen_mid + DOWN * gen_h / 2 + LEFT * 0.12, gen_mid + DOWN * gen_h / 2 + RIGHT * 0.12, stroke_width=2, color=WHITE),
    )
    fil_droit_haut = Line(tr, gen_mid + UP * gen_h / 2, stroke_width=3, color=WHITE)
    fil_droit_bas = Line(gen_mid + DOWN * gen_h / 2, br, stroke_width=3, color=WHITE)

    # Ampèremètre inséré en série sur le fil du haut
    amp_center = (tl + tr) / 2
    amp = Circle(radius=0.32, color=YELLOW, stroke_width=3)
    amp.move_to(amp_center)
    amp_label = Text("A", font_size=22, color=YELLOW, weight="BOLD")
    amp_label.move_to(amp_center)
    fil_haut_gauche = Line(tl, amp_center + LEFT * 0.32, stroke_width=3, color=WHITE)
    fil_haut_droit = Line(amp_center + RIGHT * 0.32, tr, stroke_width=3, color=WHITE)

    fleche_I = Arrow(
        amp_center + LEFT * 0.9 + UP * 0.35,
        amp_center + LEFT * 0.2 + UP * 0.35,
        buff=0, stroke_width=2, color=YELLOW, max_tip_length_to_length_ratio=0.35,
    )
    label_I = Text("I", font_size=20, color=YELLOW).next_to(fleche_I, UP, buff=0.08)

    return VGroup(
        fil_gauche, fil_bas, fil_droit_haut, fil_droit_bas, gen,
        fil_haut_gauche, fil_haut_droit, amp, amp_label, fleche_I, label_I,
    )


def _circuit_volt():
    """Même boucle, mais avec un voltmètre branché EN DÉRIVATION aux
    bornes de la lampe (ici une simple résistance)."""
    tl = UP * 1.0 + LEFT * 2.6
    tr = UP * 1.0 + RIGHT * 2.6
    bl = DOWN * 1.0 + LEFT * 2.6
    br = DOWN * 1.0 + RIGHT * 2.6

    fil_haut = Line(tl, tr, stroke_width=3, color=WHITE)
    fil_bas = Line(bl, br, stroke_width=3, color=WHITE)

    lampe = Rectangle(width=0.9, height=0.5, color=WHITE, stroke_width=3)
    lampe.move_to(LEFT * 2.6)
    lampe_label = Text("D", font_size=20, color=WHITE).move_to(lampe.get_center())
    fil_g_haut = Line(tl, lampe.get_top(), stroke_width=3, color=WHITE)
    fil_g_bas = Line(lampe.get_bottom(), bl, stroke_width=3, color=WHITE)

    gen = VGroup(
        Line(RIGHT * 2.6 + UP * 0.3 + LEFT * 0.25, RIGHT * 2.6 + UP * 0.3 + RIGHT * 0.25, stroke_width=5, color=WHITE),
        Line(RIGHT * 2.6 + DOWN * 0.3 + LEFT * 0.12, RIGHT * 2.6 + DOWN * 0.3 + RIGHT * 0.12, stroke_width=2, color=WHITE),
    )
    fil_d_haut = Line(tr, RIGHT * 2.6 + UP * 0.3, stroke_width=3, color=WHITE)
    fil_d_bas = Line(RIGHT * 2.6 + DOWN * 0.3, br, stroke_width=3, color=WHITE)

    volt = Circle(radius=0.34, color=RED, stroke_width=3)
    volt.move_to(lampe.get_center() + DOWN * 1.5)
    volt_label = Text("V", font_size=22, color=RED, weight="BOLD").move_to(volt.get_center())
    branche_a2 = Line(lampe.get_left() + UP * 0.3, volt.get_top(), stroke_width=2, color=RED)
    branche_b2 = Line(volt.get_bottom(), lampe.get_left() + DOWN * 0.3, stroke_width=2, color=RED)

    return VGroup(
        fil_haut, fil_bas, lampe, lampe_label, fil_g_haut, fil_g_bas,
        gen, fil_d_haut, fil_d_bas, volt, volt_label, branche_a2, branche_b2,
    )


class RappelsCourantTensionDipoles(NotionScene):
    def construct(self):
        titre = scene_title("Rappels : courant, tension, dipôles")
        titre.scale(0.5)
        titre.to_edge(UP)

        # --- Énoncé -----------------------------------------------------------
        mise_en_situation = Text(
            _wrap(
                "Avant d'étudier la puissance et l'énergie électriques, "
                "reprenons les bases : qu'est-ce que le courant électrique, "
                "comment mesure-t-on l'intensité et la tension, et comment "
                "reconnaît-on un dipôle actif d'un dipôle passif ?",
                width=56,
            ),
            font_size=23,
        )
        mise_en_situation.next_to(titre, DOWN, buff=0.35)

        with self.voiceover(
            text=(
                "Avant d'étudier la puissance et l'énergie électriques, "
                "reprenons les bases. Qu'est-ce que le courant électrique ? "
                "Comment mesure-t-on l'intensité et la tension dans un "
                "circuit ? Et comment reconnaît-on un dipôle actif d'un "
                "dipôle passif ?"
            )
        ) as tracker:
            self.play(Write(titre))
            self.play(FadeIn(mise_en_situation))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(mise_en_situation))

        # --- Raisonnement : intensité I = Q/Δt, ampèremètre en série ----------
        circuit_a = _circuit_ampere()
        circuit_a.scale(0.85)
        circuit_a.next_to(titre, DOWN, buff=0.5)

        definition_I = definition_box(
            VGroup(
                Text("Le courant électrique est un mouvement ordonné de", font_size=20),
                Text("porteurs de charge dans un conducteur.", font_size=20),
                MathTex(r"I = \dfrac{Q}{\Delta t}", font_size=30),
                Text("Q en coulombs (C), Δt en secondes (s), I en ampères (A).", font_size=19),
                Text("L'ampèremètre se branche TOUJOURS en série.", font_size=19),
            ).arrange(DOWN, buff=0.18),
            box_width=10.8,
        )
        definition_I.next_to(circuit_a, DOWN, buff=0.3)

        with self.voiceover(
            text=(
                "Le courant électrique est un mouvement ordonné de porteurs "
                "de charge à l'intérieur d'un conducteur. L'intensité I de "
                "ce courant est le quotient de la charge Q ayant traversé "
                "une section du circuit par la durée Δt de ce passage : I "
                "égale Q sur Δt. La charge s'exprime en coulombs, la durée "
                "en secondes, et l'intensité en ampères. Pour la mesurer, "
                "on insère un ampèremètre EN SÉRIE dans le circuit, comme "
                "sur ce schéma."
            )
        ) as tracker:
            self.play(FadeIn(circuit_a))
            self.play(FadeIn(definition_I))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(circuit_a), FadeOut(definition_I))

        # --- Raisonnement : tension U_AB, voltmètre en dérivation -------------
        circuit_v = _circuit_volt()
        circuit_v.scale(0.85)
        circuit_v.next_to(titre, DOWN, buff=0.5)

        definition_U = definition_box(
            VGroup(
                Text("La tension entre deux points A et B est la différence", font_size=20),
                Text("de leurs potentiels électriques.", font_size=20),
                MathTex(r"U_{AB} = V_A - V_B", font_size=30),
                Text("U en volts (V). Le voltmètre se branche TOUJOURS en", font_size=19),
                Text("dérivation (en parallèle) aux bornes du dipôle.", font_size=19),
            ).arrange(DOWN, buff=0.18),
            box_width=10.8,
        )
        definition_U.next_to(circuit_v, DOWN, buff=0.3)

        with self.voiceover(
            text=(
                "La tension électrique U A B entre deux points A et B est "
                "la différence de leurs potentiels : U A B égale V A moins "
                "V B. Elle s'exprime en volts. Pour la mesurer, on branche "
                "un voltmètre EN DÉRIVATION, c'est-à-dire en parallèle, aux "
                "bornes du dipôle étudié, sans jamais l'insérer dans le fil "
                "principal."
            )
        ) as tracker:
            self.play(FadeIn(circuit_v))
            self.play(FadeIn(definition_U))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(circuit_v), FadeOut(definition_U))

        # --- Raisonnement : dipôles actifs / passifs + conventions ------------
        dipoles = definition_box(
            VGroup(
                Text("Dipôle ACTIF (générateur) : pile, batterie, alternateur —", font_size=20),
                Text("il fournit de l'énergie électrique au circuit.", font_size=20),
                Text("Dipôle PASSIF (récepteur) : résistor, lampe, moteur —", font_size=20),
                Text("il reçoit de l'énergie électrique du circuit.", font_size=20),
            ).arrange(DOWN, aligned_edge=LEFT, buff=0.18),
            box_width=11.2,
        )
        dipoles.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "On distingue deux familles de dipôles. Les dipôles actifs, "
                "comme une pile, une batterie ou un alternateur, fournissent "
                "de l'énergie électrique au circuit : ce sont les "
                "générateurs. Les dipôles passifs, comme un résistor, une "
                "lampe ou un moteur, reçoivent au contraire de l'énergie "
                "électrique du circuit : ce sont les récepteurs."
            )
        ) as tracker:
            self.play(FadeIn(dipoles))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(dipoles))

        conventions = definition_box(
            VGroup(
                Text("Convention récepteur : les flèches I et U sont de sens", font_size=20),
                Text("OPPOSÉS aux bornes du dipôle.", font_size=20),
                Text("Convention générateur : les flèches I et U sont de", font_size=20),
                Text("MÊME SENS aux bornes du dipôle.", font_size=20),
            ).arrange(DOWN, aligned_edge=LEFT, buff=0.18),
            box_width=11.4,
        )
        conventions.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Pour orienter un schéma, on utilise deux conventions. En "
                "convention récepteur, la flèche du courant I et la flèche "
                "de la tension U sont de sens opposés aux bornes du dipôle. "
                "En convention générateur, au contraire, ces deux flèches "
                "sont de même sens. Le choix de la convention détermine le "
                "signe des formules d'énergie que nous verrons juste après."
            )
        ) as tracker:
            self.play(FadeIn(conventions))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(conventions))

        # --- Exemple résolu -----------------------------------------------------
        exemple = example_box(
            VGroup(
                Text("Un résistor branché aux bornes d'une pile : le courant", font_size=20),
                Text("entre par la borne + du résistor (là où U est comptée", font_size=20),
                Text("positive) : les flèches I et U sont opposées.", font_size=20),
                Text("→ Le résistor est étudié en convention RÉCEPTEUR.", font_size=20, color=YELLOW),
            ).arrange(DOWN, aligned_edge=LEFT, buff=0.18),
            box_width=11.6,
        )
        exemple.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Exemple : un résistor est branché aux bornes d'une pile. "
                "Le courant entre dans le résistor par la borne où la "
                "tension est comptée positive : les flèches I et U sont "
                "donc opposées. Ce résistor est étudié en convention "
                "récepteur, comme la quasi-totalité des dipôles passifs "
                "d'un circuit."
            )
        ) as tracker:
            self.play(FadeIn(exemple))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(exemple))

        # --- À retenir ------------------------------------------------------------
        retenir = essentiel_box(
            VGroup(
                Text("À retenir", font_size=24, weight="BOLD"),
                MathTex(r"I = \dfrac{Q}{\Delta t} \ (\text{A}), \quad U_{AB} = V_A - V_B \ (\text{V})", font_size=25),
                Text("Ampèremètre en SÉRIE, voltmètre en DÉRIVATION.", font_size=20),
                Text("Actif = générateur (fournit) ; passif = récepteur (reçoit).", font_size=20),
            ).arrange(DOWN, buff=0.22),
            box_width=12.0,
        )
        retenir.next_to(titre, DOWN, buff=0.35)

        with self.voiceover(
            text=(
                "Retenons l'essentiel : l'intensité I vaut Q sur Δt, en "
                "ampères, et la tension U A B vaut V A moins V B, en volts. "
                "L'ampèremètre se branche toujours en série, le voltmètre "
                "toujours en dérivation. Un dipôle actif, comme un "
                "générateur, fournit de l'énergie ; un dipôle passif, comme "
                "un récepteur, en reçoit."
            )
        ) as tracker:
            self.play(FadeIn(retenir))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(retenir))

        # --- Pièges à éviter --------------------------------------------------------
        pieges = warning_box(
            VGroup(
                Text("• Ne jamais insérer un voltmètre en série : il a une", font_size=20),
                Text("   résistance quasi infinie et bloquerait le courant.", font_size=20),
                Text("• Ne jamais brancher un ampèremètre en dérivation :", font_size=20),
                Text("   il a une résistance quasi nulle et court-circuiterait", font_size=20),
                Text("   le dipôle (risque de destruction de l'appareil).", font_size=20),
            ).arrange(DOWN, aligned_edge=LEFT, buff=0.16),
            box_width=12.0,
        )
        pieges.next_to(titre, DOWN, buff=0.35)

        with self.voiceover(
            text=(
                "Deux pièges classiques à éviter absolument. Il ne faut "
                "jamais insérer un voltmètre en série : sa résistance "
                "quasiment infinie bloquerait totalement le courant. Et il "
                "ne faut jamais brancher un ampèremètre en dérivation : sa "
                "résistance quasiment nulle court-circuiterait le dipôle, "
                "avec un risque réel de détruire l'appareil de mesure."
            )
        ) as tracker:
            self.play(FadeIn(pieges))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(pieges), FadeOut(titre))
