"""
scenes/Physique_AmplificateurOperationnel_06.py — Chapitre « L'amplificateur
opérationnel » (1ereC, Physique), scène 06.

§ 6. Le montage amplificateur inverseur : Ue appliquée via R1 sur E-, R2
en réaction entre S et E-, E+ relié à la masse. Démonstration complète du
gain : loi des nœuds I1 = I2 (car i- = 0), masse virtuelle V- = V+ = 0,
loi d'Ohm Ue = R1·I1, Us = -R2·I2 → Av = Us/Ue = -R2/R1.
Exemple résolu 2 : R1 = 2 kΩ, R2 = 10 kΩ, Ue = 0,5 V → Av = -5,
Us = -2,5 V.
Source : 1ereC/Physique.pdf, pages 99-107 (§ 6).
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
    Circle,
    FadeIn,
    FadeOut,
    Line,
    MathTex,
    Polygon,
    Rectangle,
    Text,
    VGroup,
    Write,
)

from shapes.base_scene import NotionScene
from shapes.boxes import corrige_box, essentiel_box, example_box, scene_title, theorem_box, warning_box


def _wrap(text: str, width: int = 56) -> str:
    return "\n".join(textwrap.fill(line, width=width) for line in text.split("\n"))


def _ao_symbole(width=2.0, height=1.4):
    haut = UP * height / 2 + LEFT * width / 2
    bas = DOWN * height / 2 + LEFT * width / 2
    pointe = RIGHT * width / 2
    triangle = Polygon(haut, bas, pointe, color=WHITE, stroke_width=3)
    plus = Text("+", font_size=20, color=WHITE).move_to(haut + RIGHT * 0.3 + DOWN * 0.05)
    moins = Text("−", font_size=20, color=WHITE).move_to(bas + RIGHT * 0.3 + UP * 0.05)
    return VGroup(triangle, plus, moins), haut, bas, pointe


def _resistor(gauche, droite, label, color=WHITE):
    """Résistor rectangulaire entre deux points alignés horizontalement,
    avec ses fils de connexion et son étiquette."""
    centre = (gauche + droite) / 2
    largeur = abs((droite - gauche)[0])
    corps = Rectangle(width=min(largeur * 0.5, 0.9), height=0.35, color=color, stroke_width=2.5)
    corps.move_to(centre)
    fil_g = Line(gauche, corps.get_left(), stroke_width=2.5, color=color)
    fil_d = Line(corps.get_right(), droite, stroke_width=2.5, color=color)
    etiquette = Text(label, font_size=17, color=color).next_to(corps, UP, buff=0.08)
    return VGroup(fil_g, corps, fil_d, etiquette)


def _masse(point):
    """Symbole de masse (3 barres horizontales décroissantes)."""
    stub = Line(point, point + DOWN * 0.25, stroke_width=2, color=WHITE)
    b1 = Line(LEFT * 0.22, RIGHT * 0.22, stroke_width=2, color=WHITE).move_to(point + DOWN * 0.25)
    b2 = Line(LEFT * 0.14, RIGHT * 0.14, stroke_width=2, color=WHITE).move_to(point + DOWN * 0.38)
    b3 = Line(LEFT * 0.06, RIGHT * 0.06, stroke_width=2, color=WHITE).move_to(point + DOWN * 0.5)
    return VGroup(stub, b1, b2, b3)


def _schema_inverseur():
    symbole, haut, bas, pointe = _ao_symbole()

    # E+ (haut) relié à la masse
    e_plus_pt = haut + LEFT * 0.9
    fil_e_plus = Line(haut, e_plus_pt, stroke_width=2.5, color=WHITE)
    masse = _masse(e_plus_pt)

    # Nœud A (sommation) sur le fil vers E-, à gauche de bas
    noeud_a = bas + LEFT * 0.9
    fil_a_e_moins = Line(noeud_a, bas, stroke_width=2.5, color=WHITE)
    point_a = Circle(radius=0.05, color=YELLOW, fill_color=YELLOW, fill_opacity=1).move_to(noeud_a)

    # R1 : de Ue (entrée) au nœud A
    ue_pt = noeud_a + LEFT * 1.8
    r1 = _resistor(ue_pt, noeud_a, "R1", color=YELLOW)
    label_ue = Text("Ue", font_size=18, color=YELLOW).next_to(ue_pt, LEFT, buff=0.1)

    # Sortie S
    s_pt = pointe + RIGHT * 1.8
    fil_s = Line(pointe, s_pt, stroke_width=2.5, color=WHITE)
    point_d = Circle(radius=0.05, color=ORANGE, fill_color=ORANGE, fill_opacity=1).move_to(pointe + RIGHT * 0.9)
    label_us = Text("Us", font_size=18, color=ORANGE).next_to(s_pt, RIGHT, buff=0.1)

    # R2 : réaction, du nœud A vers la sortie, en passant au-dessus de l'AO
    haut_a = noeud_a + UP * 1.6
    haut_d = point_d.get_center() + UP * 1.6
    fil_a_haut = Line(noeud_a, haut_a, stroke_width=2.5, color=ORANGE)
    r2 = _resistor(haut_a, haut_d, "R2", color=ORANGE)
    fil_d_haut = Line(haut_d, point_d.get_center(), stroke_width=2.5, color=ORANGE)

    return VGroup(
        symbole, fil_e_plus, masse, fil_a_e_moins, point_a, r1, label_ue,
        fil_s, point_d, label_us, fil_a_haut, r2, fil_d_haut,
    )


class MontageAmplificateurInverseur(NotionScene):
    def construct(self):
        titre = scene_title("Le montage amplificateur inverseur")
        titre.scale(0.4)
        titre.to_edge(UP)

        # --- Énoncé -------------------------------------------------------
        mise_en_situation = Text(
            _wrap(
                "Comment amplifier un signal tout en inversant son signe, "
                "et comment le gain de ce montage dépend-il uniquement de "
                "deux résistances ?",
                width=58,
            ),
            font_size=22,
        )
        mise_en_situation.next_to(titre, DOWN, buff=0.35)

        with self.voiceover(
            text=(
                "Comment amplifier un signal tout en inversant son signe, "
                "et comment le gain de ce montage dépend-il uniquement de "
                "deux résistances ? C'est le montage amplificateur "
                "inverseur."
            )
        ) as tracker:
            self.play(Write(titre))
            self.play(FadeIn(mise_en_situation))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(mise_en_situation))

        # --- Raisonnement : schéma --------------------------------------------
        schema = _schema_inverseur()
        schema.scale(0.95)
        schema.next_to(titre, DOWN, buff=0.55).shift(LEFT * 1.0)

        with self.voiceover(
            text=(
                "Ue est appliquée à travers la résistance R1 sur l'entrée "
                "E moins. La résistance R2 relie la sortie à cette même "
                "entrée E moins : c'est la réaction négative. L'entrée E "
                "plus, elle, est reliée directement à la masse."
            )
        ) as tracker:
            self.play(FadeIn(schema))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(schema))

        # --- Raisonnement : démonstration complète du gain --------------------
        demonstration = theorem_box(
            VGroup(
                Text("E+ à la masse et ε = 0  →  V− = V+ = 0 (masse virtuelle)", font_size=18),
                Text("i− = 0  →  loi des nœuds au point A : I1 = I2", font_size=18),
                MathTex(r"U_e = R_1 I_1 \quad ; \quad U_s = -R_2 I_2", font_size=24),
                MathTex(r"A_v = \dfrac{U_s}{U_e} = -\dfrac{R_2}{R_1}", font_size=28, color=YELLOW),
            ).arrange(DOWN, buff=0.18),
            box_width=11.2,
        )
        demonstration.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Démonstration. Puisque E plus est à la masse et que "
                "epsilon est nul, V moins vaut aussi zéro : on parle de "
                "masse virtuelle au point A. Puisque i moins est nul, la "
                "loi des nœuds au point A impose que le courant I1 dans R1 "
                "soit égal au courant I2 dans R2. La loi d'Ohm donne alors "
                "Ue égale R1 fois I1, et Us égale moins R2 fois I2, le "
                "signe moins venant du sens choisi pour I2. En combinant "
                "ces relations, le gain Av égale Us sur Ue vaut moins R2 "
                "sur R1."
            )
        ) as tracker:
            self.play(FadeIn(demonstration))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(demonstration))

        # --- Exemple résolu 2 ---------------------------------------------------
        enonce_ex = example_box(
            VGroup(
                Text("R1 = 2 kΩ, R2 = 10 kΩ, Ue = 0,5 V.", font_size=20),
                Text("Calculer Av puis Us.", font_size=20),
            ).arrange(DOWN, aligned_edge=LEFT, buff=0.2),
            box_width=8.4,
        )
        enonce_ex.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Exemple résolu. R1 vaut 2 kilo-ohms, R2 vaut 10 "
                "kilo-ohms, et Ue vaut 0,5 volt. Calculons Av puis Us."
            )
        ) as tracker:
            self.play(FadeIn(enonce_ex))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(enonce_ex))

        corrige = corrige_box(
            VGroup(
                MathTex(r"A_v = -\dfrac{R_2}{R_1} = -\dfrac{10}{2} = -5", font_size=26),
                MathTex(r"U_s = A_v \cdot U_e = -5 \times 0{,}5 = -2{,}5\ \text{V}", font_size=26, color=YELLOW),
            ).arrange(DOWN, buff=0.25),
            box_width=9.6,
        )
        corrige.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Corrigé. Av vaut moins R2 sur R1, soit moins 10 sur 2, "
                "c'est-à-dire moins 5. Us vaut Av fois Ue, soit moins 5 "
                "fois 0,5 volt, c'est-à-dire moins 2,5 volts."
            )
        ) as tracker:
            self.play(FadeIn(corrige))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(corrige))

        # --- À retenir --------------------------------------------------------
        retenir = essentiel_box(
            VGroup(
                Text("À retenir", font_size=24, weight="BOLD"),
                MathTex(r"A_v = \dfrac{U_s}{U_e} = -\dfrac{R_2}{R_1}", font_size=28),
                Text("E+ à la masse → masse virtuelle en E− (V− = 0).", font_size=20),
            ).arrange(DOWN, buff=0.22),
            box_width=11.6,
        )
        retenir.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Retenons l'essentiel. Le gain de l'amplificateur "
                "inverseur vaut moins R2 sur R1. Le fait que E plus soit à "
                "la masse crée une masse virtuelle en E moins, avec V "
                "moins nul."
            )
        ) as tracker:
            self.play(FadeIn(retenir))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(retenir))

        # --- Pièges à éviter --------------------------------------------------
        pieges = warning_box(
            VGroup(
                Text("• Piège classique : inverser R1 et R2 dans la formule.", font_size=19),
                Text("   R2 est TOUJOURS le résistor de réaction (celui qui", font_size=19),
                Text("   relie la sortie à E−), jamais celui côté Ue.", font_size=19),
                Text("• Ne pas oublier le signe moins du gain : la sortie", font_size=19),
                Text("   est toujours de signe opposé à l'entrée.", font_size=19),
            ).arrange(DOWN, aligned_edge=LEFT, buff=0.15),
            box_width=12.0,
        )
        pieges.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Deux pièges à éviter. Le piège classique est d'inverser "
                "R1 et R2 dans la formule : R2 est toujours le résistor de "
                "réaction, celui qui relie la sortie à E moins, jamais "
                "celui du côté de Ue. Et n'oubliez jamais le signe moins "
                "du gain : la sortie est toujours de signe opposé à "
                "l'entrée."
            )
        ) as tracker:
            self.play(FadeIn(pieges))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(pieges), FadeOut(titre))
