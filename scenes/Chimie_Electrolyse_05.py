"""
scenes/Chimie_Electrolyse_05.py — Chapitre 14 « Électrolyse » (1ereC,
Chimie), scène 05.

§ 5. Électrolyse à électrodes inertes : solution d'acide sulfurique.
Expérience (électrodes de platine ou graphite, solution H₂SO₄ diluée) et
observations (dégagement gazeux aux deux électrodes, volume à la cathode
double de celui à l'anode). Demi-équations : anode = oxydation de l'eau
(2H₂O → O₂ + 4H⁺ + 4e⁻), cathode = réduction de H⁺ (2H⁺ + 2e⁻ → H₂).
Équation-bilan 2H₂O → 2H₂ + O₂. Conclusion : c'est en réalité l'eau qui
est électrolysée, l'acide sulfurique ne servant qu'à rendre l'eau
suffisamment conductrice. Exemple résolu 1 : 30 mL de O₂ recueillis à
l'anode → 60 mL de H₂ à la cathode (rapport stœchiométrique 2:1).
Source : 1ereC/Chimie.pdf, chapitre 14, pages 138-139.
"""

import textwrap

from manim import (
    BLUE,
    DOWN,
    LEFT,
    LIGHT_GRAY,
    RED,
    RIGHT,
    UP,
    WHITE,
    YELLOW,
    Circle,
    FadeIn,
    FadeOut,
    Line,
    MathTex,
    Rectangle,
    Text,
    VGroup,
    Write,
    config,
)

from shapes.base_scene import NotionScene
from shapes.boxes import example_box, scene_title


def _wrap(text: str, width: int = 56) -> str:
    return "\n".join(textwrap.fill(line, width=width) for line in text.split("\n"))


def _bullets(items, font_size=21, color=WHITE, width=54):
    lines = VGroup(
        *[Text(f"• {_wrap(it, width=width)}", font_size=font_size, color=color) for it in items]
    )
    lines.arrange(DOWN, aligned_edge=LEFT, buff=0.22)
    return lines


def _fit(mobject, top_y):
    bas_visible = -config.frame_height / 2 + 0.25
    hauteur_dispo = top_y - bas_visible
    if mobject.height > hauteur_dispo:
        mobject.scale(hauteur_dispo / mobject.height, about_point=mobject.get_top())
    return mobject


def _schema_h2so4():
    """Cuve à électrolyse d'une solution d'acide sulfurique, avec des tubes
    à essais renversés collectant les gaz : volume O2 (anode) deux fois
    plus petit que le volume H2 (cathode)."""
    largeur, hauteur = 3.2, 1.7
    cuve = Rectangle(width=largeur, height=hauteur, color=LIGHT_GRAY, stroke_width=3)
    cuve.move_to([0, -1.1, 0])

    solution = Rectangle(width=largeur - 0.1, height=hauteur - 0.2, fill_color=BLUE, fill_opacity=0.10, stroke_width=0)
    solution.move_to(cuve.get_center())
    label_sol = Text("H₂SO₄ dilué", font_size=14, color=WHITE)
    label_sol.move_to(cuve.get_bottom() + UP * 0.25)

    electrode_a = Line(cuve.get_center() + RIGHT * 1.0 + DOWN * 0.7, cuve.get_center() + RIGHT * 1.0 + UP * 0.7, color=RED, stroke_width=4)
    electrode_c = Line(cuve.get_center() + LEFT * 1.0 + DOWN * 0.7, cuve.get_center() + LEFT * 1.0 + UP * 0.7, color=BLUE, stroke_width=4)

    # Tubes à essai renversés au-dessus de chaque électrode, hauteur du gaz
    # proportionnelle au volume recueilli (cathode = 2x anode).
    tube_a = Rectangle(width=0.35, height=0.7, color=LIGHT_GRAY, stroke_width=1.5)
    tube_a.move_to(electrode_a.get_top() + UP * 0.55)
    gaz_a = Rectangle(width=0.3, height=0.3, fill_color=YELLOW, fill_opacity=0.5, stroke_width=0)
    gaz_a.move_to(tube_a.get_top() + DOWN * 0.15)
    label_a = Text("O₂ (V)", font_size=14, color=RED, weight="BOLD")
    label_a.next_to(tube_a, UP, buff=0.1)

    tube_c = Rectangle(width=0.35, height=0.9, color=LIGHT_GRAY, stroke_width=1.5)
    tube_c.move_to(electrode_c.get_top() + UP * 0.65)
    gaz_c = Rectangle(width=0.3, height=0.6, fill_color=YELLOW, fill_opacity=0.5, stroke_width=0)
    gaz_c.move_to(tube_c.get_top() + DOWN * 0.3)
    label_c = Text("H₂ (2V)", font_size=14, color=BLUE, weight="BOLD")
    label_c.next_to(tube_c, UP, buff=0.1)

    label_anode = Text("anode (+)", font_size=13, color=RED)
    label_anode.next_to(electrode_a, DOWN, buff=0.55)
    label_cathode = Text("cathode (−)", font_size=13, color=BLUE)
    label_cathode.next_to(electrode_c, DOWN, buff=0.55)

    return VGroup(
        cuve, solution, label_sol,
        electrode_a, electrode_c, label_anode, label_cathode,
        tube_a, gaz_a, label_a, tube_c, gaz_c, label_c,
    )


class ElectrolyseAcideSulfurique(NotionScene):
    def construct(self):
        titre = scene_title("14.5 Électrolyse d'une solution d'acide sulfurique")
        titre.scale(0.42)
        titre.to_edge(UP)

        # --- Énoncé : le montage ---------------------------------------------------
        intro = Text(
            _wrap(
                "Réalisons l'électrolyse, à électrodes inertes (platine ou "
                "graphite), d'une solution diluée d'acide sulfurique.",
                width=58,
            ),
            font_size=22,
            color=WHITE,
        )
        intro.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Réalisons notre première électrolyse à électrodes "
                "inertes, en platine ou en graphite : celle d'une "
                "solution diluée d'acide sulfurique."
            )
        ) as tracker:
            self.play(Write(titre))
            self.play(FadeIn(intro))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(intro))

        # --- Raisonnement : observations + schéma ----------------------------------
        entete_obs = Text("Observations expérimentales", font_size=21, color=YELLOW, weight="BOLD")
        entete_obs.next_to(titre, DOWN, buff=0.3)

        schema = _schema_h2so4()
        schema.next_to(entete_obs, DOWN, buff=0.35).shift(LEFT * 2.6)

        observations = _bullets(
            [
                "un gaz se dégage aux DEUX électrodes ;",
                "le volume de gaz recueilli à la CATHODE est le double du "
                "volume recueilli à l'ANODE.",
            ],
            width=32,
        )
        observations.next_to(schema, RIGHT, buff=0.6)

        with self.voiceover(
            text=(
                "On observe un dégagement gazeux aux deux électrodes. En "
                "recueillant les gaz par déplacement d'eau dans des tubes "
                "renversés, on constate que le volume de gaz obtenu à la "
                "cathode est exactement le double du volume obtenu à "
                "l'anode."
            )
        ) as tracker:
            self.play(FadeIn(entete_obs))
            self.play(FadeIn(schema))
            self.play(FadeIn(observations))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(entete_obs), FadeOut(schema), FadeOut(observations))

        # --- Exemple traité : demi-équations et bilan --------------------------------
        entete_eq = Text("Interprétation par demi-équations", font_size=21, color=YELLOW, weight="BOLD")
        entete_eq.next_to(titre, DOWN, buff=0.3)

        anode_eq = VGroup(
            Text("Anode (oxydation de l'eau) :", font_size=18, color=RED, weight="BOLD"),
            MathTex(r"2\,H_2O \longrightarrow O_2 + 4\,H^+ + 4\,e^-", font_size=28, color=WHITE),
        ).arrange(DOWN, buff=0.2)

        cathode_eq = VGroup(
            Text("Cathode (réduction de H⁺) :", font_size=18, color=BLUE, weight="BOLD"),
            MathTex(r"2\,H^+ + 2\,e^- \longrightarrow H_2", font_size=28, color=WHITE),
        ).arrange(DOWN, buff=0.2)

        bilan = VGroup(
            Text("Équation-bilan (cathode × 2 pour équilibrer les e⁻) :", font_size=18, color=YELLOW, weight="BOLD"),
            MathTex(r"2\,H_2O \longrightarrow 2\,H_2 + O_2", font_size=30, color=WHITE),
        ).arrange(DOWN, buff=0.2)

        groupe_eq = VGroup(anode_eq, cathode_eq, bilan).arrange(DOWN, buff=0.35)
        groupe_eq.next_to(entete_eq, DOWN, buff=0.35)

        with self.voiceover(
            text=(
                "Ici, il n'y a ni ion métallique réductible, ni ion "
                "chlorure, bromure ou iodure : c'est donc l'eau qui réagit "
                "aux deux électrodes. À l'anode, l'eau est oxydée : deux "
                "molécules d'eau donnent une molécule de dioxygène, "
                "quatre ions H plus, et quatre électrons. À la cathode, "
                "les ions H plus, apportés par l'acide sulfurique, sont "
                "réduits : deux ions H plus, plus deux électrons, donnent "
                "une molécule de dihydrogène. En multipliant la demi-"
                "équation de la cathode par deux, pour égaliser le nombre "
                "d'électrons, puis en additionnant, on obtient "
                "l'équation-bilan : deux molécules d'eau donnent deux "
                "molécules de dihydrogène et une molécule de dioxygène. "
                "Ce rapport de deux pour un explique exactement le rapport "
                "des volumes de gaz observé."
            )
        ) as tracker:
            self.play(FadeIn(entete_eq))
            self.play(Write(anode_eq))
            self.play(Write(cathode_eq))
            self.play(Write(bilan))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(entete_eq), FadeOut(groupe_eq))

        # --- À retenir : conclusion --------------------------------------------------
        conclusion = _bullets(
            [
                "cette électrolyse est en réalité une ÉLECTROLYSE DE "
                "L'EAU : l'acide sulfurique ne fait que rendre l'eau "
                "suffisamment conductrice, il n'est pas consommé ;",
                "à retenir : V(H₂) à la cathode = 2 × V(O₂) à l'anode, "
                "dans les mêmes conditions de température et de pression.",
            ],
            font_size=19,
            width=56,
        )
        entete_concl = Text("Conclusion", font_size=21, color="#288073", weight="BOLD")
        entete_concl.next_to(titre, DOWN, buff=0.35)
        conclusion.next_to(entete_concl, DOWN, buff=0.3)
        _fit(VGroup(entete_concl, conclusion), entete_concl.get_bottom()[1] - 0.3)

        with self.voiceover(
            text=(
                "En conclusion, cette électrolyse est en réalité une "
                "électrolyse de l'eau : l'acide sulfurique ne sert qu'à "
                "rendre l'eau suffisamment conductrice pour permettre le "
                "passage du courant, mais il n'est lui-même pas consommé. "
                "Retenons ce rapport de volumes : le volume de "
                "dihydrogène recueilli à la cathode est toujours le "
                "double du volume de dioxygène recueilli à l'anode, dans "
                "les mêmes conditions de température et de pression."
            )
        ) as tracker:
            self.play(FadeIn(entete_concl))
            self.play(FadeIn(conclusion))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(entete_concl), FadeOut(conclusion))

        # --- Exemple résolu 1 --------------------------------------------------------
        exemple1 = example_box(
            VGroup(
                Text("Exemple résolu 1", font_size=20, weight="BOLD"),
                Text(
                    "On recueille 30 mL de O₂ à l'anode. Quel volume de "
                    "H₂ recueille-t-on à la cathode ?",
                    font_size=18,
                ),
                MathTex(r"V(H_2) = 2 \times V(O_2) = 2 \times 30 = 60\ mL", font_size=24, color="#1A1A1A"),
            ).arrange(DOWN, buff=0.25, aligned_edge=LEFT),
            box_width=11.0,
        )
        exemple1.next_to(titre, DOWN, buff=0.45)

        with self.voiceover(
            text=(
                "Appliquons ce résultat. On recueille trente millilitres "
                "de dioxygène à l'anode. D'après l'équation-bilan, le "
                "volume de dihydrogène à la cathode est le double : deux "
                "fois trente, soit soixante millilitres de dihydrogène."
            )
        ) as tracker:
            self.play(FadeIn(exemple1))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(exemple1), FadeOut(titre))
