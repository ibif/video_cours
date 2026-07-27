"""
scenes/Physique_AmplificateurOperationnel_07.py — Chapitre « L'amplificateur
opérationnel » (1ereC, Physique), scène 07.

§ 7. Le montage amplificateur non inverseur : Ue directement sur E+, R1
de E- à la masse, R2 de S à E-. Démonstration complète du gain :
V- = V+ = Ue, I1 = I2 (car i- = 0), Ue = R1·I1, Us = Ue + R2·I2 →
Av = 1 + R2/R1 (toujours ≥ 1, pas d'inversion). Exemple résolu 3 :
R1 = 1 kΩ, R2 = 9 kΩ, Ue = 0,8 V → Av = 10, Us = 8 V. Mention du montage
sommateur inverseur : Us = -R3(U1/R1 + U2/R2), application mélangeur
audio.
Source : 1ereC/Physique.pdf, pages 99-107 (§ 7).
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
    centre = (gauche + droite) / 2
    largeur = abs((droite - gauche)[0]) or abs((droite - gauche)[1])
    corps = Rectangle(width=min(max(largeur * 0.5, 0.5), 0.9), height=0.35, color=color, stroke_width=2.5)
    corps.move_to(centre)
    fil_g = Line(gauche, corps.get_left(), stroke_width=2.5, color=color)
    fil_d = Line(corps.get_right(), droite, stroke_width=2.5, color=color)
    etiquette = Text(label, font_size=17, color=color).next_to(corps, UP, buff=0.08)
    return VGroup(fil_g, corps, fil_d, etiquette)


def _resistor_vertical(haut, bas, label, color=WHITE):
    centre = (haut + bas) / 2
    corps = Rectangle(width=0.35, height=0.7, color=color, stroke_width=2.5)
    corps.move_to(centre)
    fil_h = Line(haut, corps.get_top(), stroke_width=2.5, color=color)
    fil_b = Line(corps.get_bottom(), bas, stroke_width=2.5, color=color)
    etiquette = Text(label, font_size=17, color=color).next_to(corps, RIGHT, buff=0.1)
    return VGroup(fil_h, corps, fil_b, etiquette)


def _masse(point):
    stub = Line(point, point + DOWN * 0.25, stroke_width=2, color=WHITE)
    b1 = Line(LEFT * 0.22, RIGHT * 0.22, stroke_width=2, color=WHITE).move_to(point + DOWN * 0.25)
    b2 = Line(LEFT * 0.14, RIGHT * 0.14, stroke_width=2, color=WHITE).move_to(point + DOWN * 0.38)
    b3 = Line(LEFT * 0.06, RIGHT * 0.06, stroke_width=2, color=WHITE).move_to(point + DOWN * 0.5)
    return VGroup(stub, b1, b2, b3)


def _schema_non_inverseur():
    symbole, haut, bas, pointe = _ao_symbole()

    # Ue directement sur E+
    ue_pt = haut + LEFT * 1.6
    fil_e_plus = Line(ue_pt, haut, stroke_width=2.5, color=YELLOW)
    label_ue = Text("Ue", font_size=18, color=YELLOW).next_to(ue_pt, LEFT, buff=0.1)

    # Nœud A sur E- : R1 vers la masse (en bas), R2 vers la sortie (en haut)
    noeud_a = bas + LEFT * 0.9
    fil_a_e_moins = Line(noeud_a, bas, stroke_width=2.5, color=WHITE)
    point_a = Circle(radius=0.05, color=ORANGE, fill_color=ORANGE, fill_opacity=1).move_to(noeud_a)

    masse_pt = noeud_a + DOWN * 1.1
    r1 = _resistor_vertical(noeud_a, masse_pt, "R1", color=WHITE)
    masse = _masse(masse_pt)

    s_pt = pointe + RIGHT * 1.8
    fil_s = Line(pointe, s_pt, stroke_width=2.5, color=WHITE)
    point_d = Circle(radius=0.05, color=ORANGE, fill_color=ORANGE, fill_opacity=1).move_to(pointe + RIGHT * 0.9)
    label_us = Text("Us", font_size=18, color=ORANGE).next_to(s_pt, RIGHT, buff=0.1)

    haut_a = noeud_a + UP * 1.6
    haut_d = point_d.get_center() + UP * 1.6
    fil_a_haut = Line(noeud_a, haut_a, stroke_width=2.5, color=ORANGE)
    r2 = _resistor(haut_a, haut_d, "R2", color=ORANGE)
    fil_d_haut = Line(haut_d, point_d.get_center(), stroke_width=2.5, color=ORANGE)

    return VGroup(
        symbole, fil_e_plus, label_ue, fil_a_e_moins, point_a, r1, masse,
        fil_s, point_d, label_us, fil_a_haut, r2, fil_d_haut,
    )


class MontageAmplificateurNonInverseur(NotionScene):
    def construct(self):
        titre = scene_title("Le montage amplificateur non inverseur")
        titre.scale(0.38)
        titre.to_edge(UP)

        # --- Énoncé -------------------------------------------------------
        mise_en_situation = Text(
            _wrap(
                "Et s'il fallait amplifier un signal SANS inverser son "
                "signe ? Un léger changement de branchement suffit à "
                "obtenir ce résultat.",
                width=58,
            ),
            font_size=22,
        )
        mise_en_situation.next_to(titre, DOWN, buff=0.35)

        with self.voiceover(
            text=(
                "Et s'il fallait amplifier un signal sans inverser son "
                "signe ? Un léger changement de branchement suffit à "
                "obtenir ce résultat : c'est le montage amplificateur non "
                "inverseur."
            )
        ) as tracker:
            self.play(Write(titre))
            self.play(FadeIn(mise_en_situation))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(mise_en_situation))

        # --- Raisonnement : schéma --------------------------------------------
        schema = _schema_non_inverseur()
        schema.scale(0.9)
        schema.next_to(titre, DOWN, buff=0.55).shift(LEFT * 0.6)

        with self.voiceover(
            text=(
                "Cette fois, Ue est appliquée directement sur l'entrée E "
                "plus. La résistance R1 relie l'entrée E moins à la masse, "
                "et la résistance R2 relie la sortie à cette même entrée E "
                "moins : c'est toujours la réaction négative."
            )
        ) as tracker:
            self.play(FadeIn(schema))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(schema))

        # --- Raisonnement : démonstration complète du gain --------------------
        demonstration = theorem_box(
            VGroup(
                Text("ε = 0  →  V− = V+ = Ue", font_size=19),
                Text("i− = 0  →  loi des nœuds au point A : I1 = I2", font_size=19),
                MathTex(r"U_e = R_1 I_1 \quad ; \quad U_s = U_e + R_2 I_2", font_size=24),
                MathTex(r"A_v = \dfrac{U_s}{U_e} = 1 + \dfrac{R_2}{R_1}", font_size=28, color=YELLOW),
            ).arrange(DOWN, buff=0.18),
            box_width=11.2,
        )
        demonstration.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Démonstration. Epsilon est nul, donc V moins égale V "
                "plus, qui vaut Ue directement. Puisque i moins est nul, "
                "la loi des nœuds au point A impose I1 égal I2 dans R1 et "
                "R2. La loi d'Ohm donne Ue égale R1 fois I1, et Us égale "
                "Ue plus R2 fois I2 cette fois-ci, sans signe moins. On en "
                "déduit que le gain Av égale 1 plus R2 sur R1 : il est "
                "toujours supérieur ou égal à 1, et il n'y a jamais "
                "d'inversion de signe."
            )
        ) as tracker:
            self.play(FadeIn(demonstration))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(demonstration))

        # --- Exemple résolu 3 ---------------------------------------------------
        enonce_ex = example_box(
            VGroup(
                Text("R1 = 1 kΩ, R2 = 9 kΩ, Ue = 0,8 V.", font_size=20),
                Text("Calculer Av puis Us.", font_size=20),
            ).arrange(DOWN, aligned_edge=LEFT, buff=0.2),
            box_width=8.4,
        )
        enonce_ex.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Exemple résolu. R1 vaut 1 kilo-ohm, R2 vaut 9 "
                "kilo-ohms, et Ue vaut 0,8 volt. Calculons Av puis Us."
            )
        ) as tracker:
            self.play(FadeIn(enonce_ex))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(enonce_ex))

        corrige = corrige_box(
            VGroup(
                MathTex(r"A_v = 1 + \dfrac{R_2}{R_1} = 1 + \dfrac{9}{1} = 10", font_size=26),
                MathTex(r"U_s = A_v \cdot U_e = 10 \times 0{,}8 = 8\ \text{V}", font_size=26, color=YELLOW),
            ).arrange(DOWN, buff=0.25),
            box_width=9.6,
        )
        corrige.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Corrigé. Av vaut 1 plus R2 sur R1, soit 1 plus 9 sur 1, "
                "c'est-à-dire 10. Us vaut Av fois Ue, soit 10 fois 0,8 "
                "volt, c'est-à-dire 8 volts."
            )
        ) as tracker:
            self.play(FadeIn(corrige))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(corrige))

        # --- À retenir (+ mention du sommateur inverseur) ----------------------
        retenir = essentiel_box(
            VGroup(
                Text("À retenir", font_size=24, weight="BOLD"),
                MathTex(r"A_v = \dfrac{U_s}{U_e} = 1 + \dfrac{R_2}{R_1} \ \geq 1", font_size=27),
                Text("Variante : sommateur inverseur (plusieurs entrées),", font_size=19),
                MathTex(r"U_s = -R_3\left(\dfrac{U_1}{R_1} + \dfrac{U_2}{R_2}\right)", font_size=24),
                Text("Application : table de mixage / mélangeur audio.", font_size=19),
            ).arrange(DOWN, buff=0.18),
            box_width=12.0,
        )
        retenir.next_to(titre, DOWN, buff=0.35)

        with self.voiceover(
            text=(
                "Retenons l'essentiel. Le gain du montage non inverseur "
                "vaut 1 plus R2 sur R1, toujours supérieur ou égal à 1. "
                "Une variante importante est le montage sommateur "
                "inverseur, à plusieurs entrées, où Us égale moins R3 fois "
                "la somme de U1 sur R1 et de U2 sur R2 : c'est le principe "
                "d'une table de mixage, qui mélange plusieurs signaux "
                "audio."
            )
        ) as tracker:
            self.play(FadeIn(retenir))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(retenir))

        # --- Pièges à éviter --------------------------------------------------
        pieges = warning_box(
            VGroup(
                Text("• Ne pas oublier le « +1 » dans Av = 1 + R2/R1 : le", font_size=19),
                Text("   gain n'est jamais nul, même si R2 = 0.", font_size=19),
                Text("• Ne pas confondre avec l'inverseur : ici Ue est SUR", font_size=19),
                Text("   E+ directement, pas via R1.", font_size=19),
            ).arrange(DOWN, aligned_edge=LEFT, buff=0.15),
            box_width=12.0,
        )
        pieges.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Deux pièges à éviter. N'oubliez pas le plus 1 dans la "
                "formule Av égale 1 plus R2 sur R1 : le gain n'est jamais "
                "nul, même si R2 est nulle. Et ne confondez pas ce montage "
                "avec l'inverseur : ici, Ue est appliquée directement sur "
                "E plus, pas à travers R1."
            )
        ) as tracker:
            self.play(FadeIn(pieges))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(pieges), FadeOut(titre))
