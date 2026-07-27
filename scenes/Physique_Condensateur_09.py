"""
scenes/Physique_Condensateur_09.py — Chapitre 9 « Le condensateur »
(1ereC, Physique), scène 09.

§ 6a. Charge et décharge à travers un résistor : allures des courbes.
Montage (générateur E, interrupteur à deux positions, résistor R,
condensateur C). Allures qualitatives : à la charge, u_C croît de 0 vers
E en s'approchant d'une asymptote, i décroît de E/R vers 0 ; à la
décharge, u_C décroît de U0 vers 0, i change de sens par rapport à la
charge.
Source : 1ereC/Physique.pdf, pages 88-98 (chapitre 9, § 6a).
"""

import textwrap

import numpy as np

from manim import (
    DOWN,
    LEFT,
    RIGHT,
    UP,
    WHITE,
    YELLOW,
    Axes,
    Create,
    DashedLine,
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


def _montage_rc():
    """Générateur E, interrupteur à deux positions, résistor R,
    condensateur C — construit uniquement avec Line/Rectangle."""
    tl = UP * 1.0 + LEFT * 2.8
    tr = UP * 1.0 + RIGHT * 2.8
    bl = DOWN * 1.0 + LEFT * 2.8
    br = DOWN * 1.0 + RIGHT * 2.8

    fil_bas = Line(bl, br, stroke_width=3, color=WHITE)

    # Générateur E à gauche
    gen = VGroup(
        Line(UP * 0.3 + LEFT * 2.8 + LEFT * 0.25, UP * 0.3 + LEFT * 2.8 + RIGHT * 0.25, stroke_width=5, color=WHITE),
        Line(DOWN * 0.3 + LEFT * 2.8 + LEFT * 0.12, DOWN * 0.3 + LEFT * 2.8 + RIGHT * 0.12, stroke_width=2, color=WHITE),
    )
    fil_g_haut = Line(tl, LEFT * 2.8 + UP * 0.3, stroke_width=3, color=WHITE)
    fil_g_bas = Line(LEFT * 2.8 + DOWN * 0.3, bl, stroke_width=3, color=WHITE)
    label_E = Text("E", font_size=20, color=YELLOW).next_to(gen, LEFT, buff=0.15)

    # Interrupteur à 2 positions (charge / décharge) au milieu du fil du haut
    interr_pivot = UP * 1.0 + LEFT * 0.5
    interr_charge = LEFT * 0.5 + UP * 0.5 + RIGHT * 0.6
    tige = Line(interr_pivot, interr_pivot + RIGHT * 0.7 + UP * 0.25, stroke_width=3, color=YELLOW)
    fil_tl_interr = Line(tl, interr_pivot, stroke_width=3, color=WHITE)
    point_charge = Line(interr_pivot + RIGHT * 0.7, interr_pivot + RIGHT * 0.9, stroke_width=3, color=WHITE)
    label_interr = Text("K", font_size=18, color=YELLOW).next_to(tige, UP, buff=0.1)

    # Résistor R
    r_center = RIGHT * 0.8 + UP * 1.0
    resistor = Rectangle(width=0.9, height=0.35, color=WHITE, stroke_width=3)
    resistor.move_to(r_center)
    label_R = Text("R", font_size=20, color=WHITE).next_to(resistor, UP, buff=0.1)
    fil_interr_r = Line(interr_pivot + RIGHT * 0.9, resistor.get_left(), stroke_width=3, color=WHITE)
    fil_r_tr = Line(resistor.get_right(), tr, stroke_width=3, color=WHITE)

    # Condensateur C à droite
    c_center = RIGHT * 2.8
    p1 = Line(UP * 0.35, DOWN * 0.35, stroke_width=6, color=WHITE).shift(c_center + UP * 0.35)
    p2 = Line(UP * 0.35, DOWN * 0.35, stroke_width=6, color=WHITE).shift(c_center + DOWN * 0.35)
    fil_tr_c = Line(tr, c_center + UP * 0.35 + UP * 0.35, stroke_width=3, color=WHITE)
    fil_c_br = Line(c_center + DOWN * 0.35 + DOWN * 0.35, br, stroke_width=3, color=WHITE)
    label_C = Text("C", font_size=20, color=WHITE).next_to(VGroup(p1, p2), RIGHT, buff=0.15)

    return VGroup(
        fil_bas, gen, fil_g_haut, fil_g_bas, label_E,
        fil_tl_interr, tige, point_charge, label_interr,
        resistor, label_R, fil_interr_r, fil_r_tr,
        p1, p2, fil_tr_c, fil_c_br, label_C,
    )


class ChargeDechargeResistorAllures(NotionScene):
    def construct(self):
        titre = scene_title("Charge/décharge à travers un résistor")
        titre.scale(0.46)
        titre.to_edge(UP)

        # --- Énoncé -------------------------------------------------------
        mise_en_situation = Text(
            _wrap(
                "Jusqu'ici, on chargeait le condensateur avec un courant "
                "constant, ce qui donnait une droite. Mais si l'on charge "
                "(ou décharge) le condensateur à travers un résistor, "
                "quelle allure prennent alors u_C(t) et i(t) ?",
                width=56,
            ),
            font_size=23,
        )
        mise_en_situation.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Jusqu'ici, on chargeait le condensateur avec un courant "
                "constant, ce qui donnait une tension en droite. Mais si "
                "l'on charge, ou décharge, le condensateur à travers un "
                "résistor, quelle allure prennent alors la tension u C de t "
                "et le courant i de t ?"
            )
        ) as tracker:
            self.play(Write(titre))
            self.play(FadeIn(mise_en_situation))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(mise_en_situation))

        # --- Raisonnement : montage ---------------------------------------------
        montage = _montage_rc()
        montage.scale(0.9)
        montage.next_to(titre, DOWN, buff=0.55)

        with self.voiceover(
            text=(
                "Voici le montage : un générateur de force électromotrice "
                "E, un interrupteur K à deux positions, un résistor R et un "
                "condensateur C. En position charge, le condensateur se "
                "charge à travers R sous l'effet du générateur ; en "
                "position décharge, il se décharge à travers R seul."
            )
        ) as tracker:
            self.play(FadeIn(montage))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(montage))

        # --- Allure de la charge -------------------------------------------------
        axes_ch = Axes(
            x_range=[0, 5, 1],
            y_range=[0, 6, 1],
            x_length=5.6,
            y_length=3.4,
            axis_config={"include_tip": True, "stroke_width": 2, "color": WHITE},
        )
        axes_ch.next_to(titre, DOWN, buff=0.55).shift(LEFT * 2.6)
        E_val = 5
        courbe_uc = axes_ch.plot(lambda t: E_val * (1 - np.exp(-t)), x_range=[0, 5], color=YELLOW)
        courbe_i = axes_ch.plot(lambda t: E_val * np.exp(-t), x_range=[0, 5], color="#4FA8FF")
        asymptote = DashedLine(axes_ch.c2p(0, E_val), axes_ch.c2p(5, E_val), color=WHITE, stroke_width=1.5)

        legende_ch = VGroup(
            Text("u_C : croît de 0 vers E", font_size=18, color=YELLOW),
            Text("i : décroît de E/R vers 0", font_size=18, color="#4FA8FF"),
        ).arrange(DOWN, buff=0.2, aligned_edge=LEFT)
        legende_ch.next_to(axes_ch, RIGHT, buff=0.4)

        graphe_ch = VGroup(axes_ch, courbe_uc, courbe_i, asymptote)

        with self.voiceover(
            text=(
                "Pendant la CHARGE, la tension u C part de zéro et croît "
                "progressivement vers E, sans jamais tout à fait "
                "l'atteindre : c'est une courbe qui s'aplatit, avec E comme "
                "asymptote horizontale. L'intensité i, elle, part de sa "
                "valeur maximale E sur R et décroît progressivement vers "
                "zéro."
            )
        ) as tracker:
            self.play(Create(axes_ch))
            self.play(Create(courbe_uc), FadeIn(asymptote))
            self.play(Create(courbe_i))
            self.play(FadeIn(legende_ch))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(graphe_ch), FadeOut(legende_ch))

        # --- Allure de la décharge -------------------------------------------------
        axes_dc = Axes(
            x_range=[0, 5, 1],
            y_range=[-6, 6, 2],
            x_length=5.6,
            y_length=3.4,
            axis_config={"include_tip": True, "stroke_width": 2, "color": WHITE},
        )
        axes_dc.next_to(titre, DOWN, buff=0.55).shift(LEFT * 2.6)
        courbe_uc_d = axes_dc.plot(lambda t: E_val * np.exp(-t), x_range=[0, 5], color=YELLOW)
        courbe_i_d = axes_dc.plot(lambda t: -E_val * np.exp(-t), x_range=[0, 5], color="#4FA8FF")

        legende_dc = VGroup(
            Text("u_C : décroît de U0 vers 0", font_size=18, color=YELLOW),
            Text("i : change de SENS (négatif)", font_size=18, color="#4FA8FF"),
        ).arrange(DOWN, buff=0.2, aligned_edge=LEFT)
        legende_dc.next_to(axes_dc, RIGHT, buff=0.4)

        graphe_dc = VGroup(axes_dc, courbe_uc_d, courbe_i_d)

        with self.voiceover(
            text=(
                "Pendant la DÉCHARGE, c'est l'inverse : la tension u C part "
                "de sa valeur initiale U zéro et décroît progressivement "
                "vers zéro. Et surtout, l'intensité i CHANGE DE SENS par "
                "rapport à la charge : le courant traverse désormais le "
                "résistor dans l'autre direction, puisque c'est le "
                "condensateur qui alimente maintenant le circuit."
            )
        ) as tracker:
            self.play(Create(axes_dc))
            self.play(Create(courbe_uc_d))
            self.play(Create(courbe_i_d))
            self.play(FadeIn(legende_dc))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(graphe_dc), FadeOut(legende_dc))

        # --- Exemple : identifier charge ou décharge ---------------------------
        exemple = example_box(
            VGroup(
                Text("On observe une tension u_C qui décroît progressivement", font_size=20),
                Text("de 12 V vers 0 V, sans jamais devenir négative.", font_size=20),
                Text("→ Il s'agit d'une DÉCHARGE (U0 = 12 V ici).", font_size=20, color=YELLOW),
            ).arrange(DOWN, aligned_edge=LEFT, buff=0.2),
            box_width=11.6,
        )
        exemple.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Exemple : on observe une tension u C qui décroît "
                "progressivement de douze volts vers zéro, sans jamais "
                "devenir négative. Cette allure décroissante, qui part "
                "d'une valeur non nulle vers zéro, est caractéristique "
                "d'une décharge, avec ici une tension initiale U zéro de "
                "douze volts."
            )
        ) as tracker:
            self.play(FadeIn(exemple))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(exemple))

        # --- À retenir -------------------------------------------------------------
        retenir = essentiel_box(
            VGroup(
                Text("À retenir", font_size=24, weight="BOLD"),
                Text("Charge : u_C croît de 0 à E (asymptote), i décroît de E/R à 0.", font_size=20),
                Text("Décharge : u_C décroît de U0 à 0, i change de sens.", font_size=20),
            ).arrange(DOWN, buff=0.22),
            box_width=12.0,
        )
        retenir.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Retenons l'essentiel : à la charge, u C croît de zéro vers "
                "E en s'approchant d'une asymptote, tandis que i décroît de "
                "E sur R vers zéro. À la décharge, u C décroît de U zéro "
                "vers zéro, et i change de sens par rapport à la charge."
            )
        ) as tracker:
            self.play(FadeIn(retenir))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(retenir))

        # --- Pièges à éviter --------------------------------------------------------
        pieges = warning_box(
            VGroup(
                Text("• Ces courbes sont EXPONENTIELLES, pas des droites : ne pas", font_size=20),
                Text("   les confondre avec le cas du courant constant (scène 3).", font_size=20),
                Text("• u_C ne devient JAMAIS strictement égale à E ni à 0 : elle", font_size=20),
                Text("   s'en approche seulement (asymptote), en théorie sans fin.", font_size=20),
            ).arrange(DOWN, aligned_edge=LEFT, buff=0.16),
            box_width=12.2,
        )
        pieges.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Deux pièges à éviter. Ces courbes sont exponentielles, pas "
                "des droites : il ne faut surtout pas les confondre avec le "
                "cas du courant constant vu précédemment. Et, en théorie, u "
                "C ne devient jamais strictement égale à E ni à zéro : elle "
                "s'en approche seulement, indéfiniment, comme une "
                "asymptote."
            )
        ) as tracker:
            self.play(FadeIn(pieges))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(pieges), FadeOut(titre))
