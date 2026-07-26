"""
scenes/Chimie_ClassificationQuantitativeRedox_04.py — Chapitre 11
« Classification quantitative des couples oxydant/réducteur » (1ereC,
Chimie), scène 04.

§ 4. L'électrode normale à hydrogène (ENH). Problème de la référence : un
potentiel d'électrode isolée ne se mesure pas dans l'absolu, seule une
différence de potentiel (une tension) est mesurable → il faut choisir une
électrode de référence commune. `definition_box` de l'ENH (fil ou lame de
platine platiné, plongeant dans une solution où [H₃O⁺] = 1 mol/L,
balayée par du dihydrogène gazeux sous p = 1 bar, à 25°C), demi-équation
de l'ENH (2H₃O⁺ + 2e⁻ ⇌ H₂ + 2H₂O). `definition_box` de la convention
fondamentale E°(H₃O⁺/H₂) = 0,00 V à toute température.
Source : 1ereC/Chimie.pdf, chapitre 11, pages 105-106.
"""

import textwrap

from manim import (
    DOWN,
    GRAY,
    LEFT,
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
from shapes.boxes import definition_box, scene_title, warning_box


def _wrap(text: str, width: int = 56) -> str:
    return "\n".join(textwrap.fill(line, width=width) for line in text.split("\n"))


def _fit(mobject, top_y):
    bas_visible = -config.frame_height / 2 + 0.25
    hauteur_dispo = top_y - bas_visible
    if mobject.height > hauteur_dispo:
        mobject.scale(hauteur_dispo / mobject.height, about_point=mobject.get_top())
    return mobject


def _schema_enh():
    """Schéma simplifié de l'électrode normale à hydrogène : bécher
    contenant une solution à [H3O+] = 1 mol/L, lame de platine platiné,
    bullage de H2 sous 1 bar — primitives Manim de base uniquement."""
    becher = Rectangle(width=2.4, height=2.6, color=GRAY, stroke_width=3)
    becher.move_to([0, -0.4, 0])

    solution = Rectangle(width=2.3, height=2.2, fill_color=WHITE, fill_opacity=0.06, stroke_width=0)
    solution.move_to(becher.get_bottom() + UP * 1.1)
    label_solution = Text("[H₃O⁺] = 1 mol/L", font_size=15, color=WHITE)
    label_solution.move_to(becher.get_bottom() + UP * 0.4)

    lame_pt = Rectangle(width=0.3, height=1.8, fill_color="#B7B7B7", fill_opacity=0.9, stroke_width=1)
    lame_pt.move_to(becher.get_center() + UP * 0.3)
    label_pt = Text("Pt platiné", font_size=15, color="#B7B7B7", weight="BOLD")
    label_pt.next_to(lame_pt, UP, buff=0.15)

    tube_gaz = Line(lame_pt.get_top() + UP * 0.3, lame_pt.get_top() + UP * 1.4, color=YELLOW, stroke_width=6)
    bulles = VGroup(*[
        Circle(radius=0.06, color=YELLOW, stroke_width=1, fill_color=YELLOW, fill_opacity=0.6).move_to(
            lame_pt.get_bottom() + UP * (0.3 + 0.35 * i) + RIGHT * 0.12 * (-1) ** i
        )
        for i in range(4)
    ])
    label_gaz = Text("H₂ (g), p = 1 bar", font_size=15, color=YELLOW)
    label_gaz.next_to(tube_gaz, UP, buff=0.1)

    label_temp = Text("25 °C", font_size=15, color=WHITE)
    label_temp.next_to(becher, RIGHT, buff=0.4)

    return VGroup(
        becher, solution, label_solution,
        lame_pt, label_pt, tube_gaz, bulles, label_gaz, label_temp,
    )


class ElectrodeNormaleHydrogene(NotionScene):
    def construct(self):
        titre = scene_title("11.4 L'électrode normale à hydrogène (ENH)")
        titre.scale(0.48)
        titre.to_edge(UP)

        # --- Énoncé : le problème de la référence -----------------------------------
        intro = Text(
            _wrap(
                "La pile Daniell fournit une f.é.m., c'est-à-dire une "
                "DIFFÉRENCE de potentiel entre deux électrodes. Mais "
                "peut-on mesurer le potentiel d'UNE SEULE électrode, "
                "isolément ? ",
                width=56,
            ),
            font_size=23,
            color=WHITE,
        )
        intro.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "La pile Daniell nous a donné une force électromotrice, "
                "c'est-à-dire une différence de potentiel entre deux "
                "électrodes. Mais peut-on mesurer le potentiel d'une "
                "seule électrode, isolément, dans l'absolu ? La réponse "
                "est non : comme pour l'altitude, qui se mesure toujours "
                "par rapport à un niveau de référence, un potentiel "
                "d'électrode ne peut être mesuré que par rapport à une "
                "référence commune, choisie par convention internationale."
            )
        ) as tracker:
            self.play(Write(titre))
            self.play(FadeIn(intro))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(intro))

        # --- Raisonnement : définition de l'ENH + schéma ----------------------------
        def_enh = definition_box(
            Text(
                _wrap(
                    "L'électrode normale à hydrogène (ENH) est une lame de "
                    "platine platiné plongeant dans une solution où "
                    "[H₃O⁺] = 1 mol/L, balayée par un courant de "
                    "dihydrogène gazeux sous une pression p = 1 bar, à "
                    "25 °C. Par convention, son potentiel sert de "
                    "référence à tous les autres.",
                    width=48,
                ),
                font_size=21,
            ),
            box_width=12.2,
        )
        def_enh.next_to(titre, DOWN, buff=0.35)

        with self.voiceover(
            text=(
                "Cette référence universelle s'appelle l'électrode "
                "normale à hydrogène, abrégée E-N-H. C'est une lame de "
                "platine platiné, c'est-à-dire recouverte de noir de "
                "platine pour catalyser la réaction, plongeant dans une "
                "solution où la concentration en ions oxonium vaut un "
                "mole par litre, balayée par un courant de dihydrogène "
                "gazeux sous une pression d'un bar, le tout à vingt-cinq "
                "degrés Celsius."
            )
        ) as tracker:
            self.play(FadeIn(def_enh))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(def_enh))

        schema = _schema_enh()
        schema.scale(1.0)
        schema.next_to(titre, DOWN, buff=0.5)
        eq_enh = MathTex(
            r"2\,H_3O^{+} + 2\,e^{-} \rightleftharpoons H_2 + 2\,H_2O",
            font_size=28,
            color=WHITE,
        )
        eq_enh.next_to(schema, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Voici son schéma, et la demi-équation associée au couple "
                "ion oxonium sur dihydrogène : deux H-3-O-plus, plus deux "
                "électrons, sont en équilibre avec H-2 plus deux H-2-O. "
                "Cette double flèche signale un équilibre, dans un sens "
                "ou dans l'autre selon l'électrode à laquelle on associe "
                "l'E-N-H."
            )
        ) as tracker:
            self.play(FadeIn(schema))
            self.play(Write(eq_enh))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(schema), FadeOut(eq_enh))

        # --- À retenir : convention fondamentale -------------------------------------
        def_convention = definition_box(
            VGroup(
                Text(
                    "Convention fondamentale (à toute température) :",
                    font_size=22,
                    weight="BOLD",
                ),
                MathTex(r"E^{\circ}(H_3O^{+}/H_2) = 0{,}00\ V", font_size=32, color="#1A1A1A"),
            ).arrange(DOWN, buff=0.35),
        )
        def_convention.next_to(titre, DOWN, buff=0.55)

        with self.voiceover(
            text=(
                "On pose alors une convention fondamentale, valable à "
                "toute température : le potentiel standard du couple ion "
                "oxonium sur dihydrogène est fixé arbitrairement à zéro "
                "virgule zéro zéro volt. C'est ce zéro de référence qui "
                "va nous permettre de définir, et donc de mesurer, le "
                "potentiel standard de tous les autres couples."
            )
        ) as tracker:
            self.play(FadeIn(def_convention))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(def_convention))

        # --- Piège à éviter --------------------------------------------------------------
        piege = warning_box(
            Text(
                _wrap(
                    "E°(H₃O⁺/H₂) = 0,00 V n'est PAS une valeur mesurée : "
                    "c'est une convention, un choix arbitraire d'origine, "
                    "exactement comme le niveau de la mer pour les "
                    "altitudes.",
                    width=48,
                ),
                font_size=21,
            ),
        )
        piege.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Attention à ne pas se tromper sur la nature de ce zéro : "
                "ce n'est pas une valeur mesurée expérimentalement, c'est "
                "une convention, un choix arbitraire d'origine, "
                "exactement comme le niveau de la mer choisi comme "
                "origine des altitudes."
            )
        ) as tracker:
            self.play(FadeIn(piege))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(piege), FadeOut(titre))
