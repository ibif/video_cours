"""
scenes/SVT_EcosystemeAgroIndustriel_05.py — Chapitre 11 (1ereC, SVT), scène 05.

§ 2.3 L'étang : biotope (eau, oxygène, lumière décroissante, vase) et
biocénose organisée en 3 zones (littorale, limnétique, profonde /
benthique), puis piège « ne pas confondre biotope et biocénose ».
Source : 1ereC/SVT.pdf, page 122.
"""

import textwrap

from manim import BLUE_E, DOWN, LEFT, RIGHT, UP, WHITE, YELLOW, FadeIn, FadeOut, Line, Rectangle, Text, VGroup, Write

from shapes.base_scene import NotionScene
from shapes.boxes import property_box, scene_title, warning_box


def _wrap(text: str, width: int = 56) -> str:
    return "\n".join(textwrap.fill(line, width=width) for line in text.split("\n"))


def _bullets(items, font_size=23, color=WHITE, width=52):
    lines = VGroup(
        *[Text(f"• {_wrap(it, width=width)}", font_size=font_size, color=color) for it in items]
    )
    lines.arrange(DOWN, aligned_edge=LEFT, buff=0.22)
    return lines


class LEtang(NotionScene):
    def construct(self):
        titre = scene_title("2.3 — L'étang")
        titre.scale(0.7)
        titre.to_edge(UP)

        # --- Énoncé --------------------------------------------------------
        intro = Text(
            _wrap(
                "Troisième écosystème naturel : l'étang, un écosystème "
                "aquatique d'eau douce, peu profond, facilement "
                "observable — étangs de pisciculture d'Abengourou ou de "
                "Dabou, mares de village.",
                width=56,
            ),
            font_size=24,
            color=WHITE,
        )
        intro.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Troisième écosystème naturel : l'étang, un écosystème "
                "aquatique d'eau douce, peu profond, que l'on peut "
                "observer facilement, comme les étangs de pisciculture de "
                "la région d'Abengourou ou de Dabou, ou les mares de "
                "village."
            )
        ) as tracker:
            self.play(Write(titre))
            self.play(FadeIn(intro))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(intro))

        # --- Raisonnement : biotope de l'étang -------------------------------
        biotope = property_box(
            Text(
                _wrap(
                    "Biotope : l'eau (température, oxygène dissous, "
                    "lumière qui diminue avec la profondeur, sels "
                    "minéraux dissous) et la vase du fond.",
                    width=54,
                ),
                font_size=22,
            ),
            box_width=11.5,
        )
        biotope.next_to(titre, DOWN, buff=0.45)

        with self.voiceover(
            text=(
                "Le biotope de l'étang, c'est d'abord l'eau : sa "
                "température, son taux d'oxygène dissous, sa lumière qui "
                "diminue rapidement avec la profondeur, ses sels minéraux "
                "dissous. C'est aussi la vase qui tapisse le fond."
            )
        ) as tracker:
            self.play(FadeIn(biotope))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(biotope))

        # --- Schéma : coupe de l'étang en 3 zones ----------------------------
        eau = Rectangle(width=9.5, height=3.4, fill_color=BLUE_E, fill_opacity=0.55, stroke_color=WHITE, stroke_width=2)
        surface = Line(eau.get_corner(UP + LEFT), eau.get_corner(UP + RIGHT), color=WHITE, stroke_width=2)

        zone_littorale_g = Rectangle(width=1.6, height=3.4, fill_color=BLUE_E, fill_opacity=0.2, stroke_width=0)
        zone_littorale_g.align_to(eau, LEFT)
        zone_littorale_d = zone_littorale_g.copy().align_to(eau, RIGHT)
        label_littorale_g = Text("Littorale", font_size=15, color=WHITE, weight="BOLD").move_to(zone_littorale_g).shift(UP * 1.3)
        label_littorale_d = Text("Littorale", font_size=15, color=WHITE, weight="BOLD").move_to(zone_littorale_d).shift(UP * 1.3)

        label_limnetique = Text("Zone limnétique\n(eau libre)", font_size=17, color=WHITE, weight="BOLD")
        label_limnetique.move_to(eau.get_center() + UP * 0.7)

        zone_profonde = Rectangle(width=9.5, height=1.0, fill_color="#5D4037", fill_opacity=0.75, stroke_width=0)
        zone_profonde.align_to(eau, DOWN)
        label_profonde = Text("Zone profonde / fond benthique (vase)", font_size=15, color=WHITE, weight="BOLD")
        label_profonde.move_to(zone_profonde.get_center())

        schema = VGroup(eau, zone_profonde, zone_littorale_g, zone_littorale_d, surface, label_littorale_g, label_littorale_d, label_limnetique, label_profonde)
        schema.next_to(titre, DOWN, buff=0.6)

        with self.voiceover(
            text=(
                "La biocénose de l'étang s'organise en trois zones. La "
                "zone littorale, sur les bords : des plantes enracinées, "
                "papyrus, nénuphars, des grenouilles, des insectes. La "
                "zone limnétique, en eau libre : du phytoplancton, algues "
                "microscopiques, du zooplancton, et des poissons, "
                "tilapias, carpes. Et la zone profonde et le fond "
                "benthique : des vers, des larves, des bactéries et des "
                "champignons qui décomposent la matière organique morte."
            )
        ) as tracker:
            self.play(FadeIn(schema))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(schema))

        # --- Exemple traité : espèces par zone --------------------------------
        exemple_titre = Text("Espèces caractéristiques par zone", font_size=24, color=YELLOW, weight="BOLD")
        exemple_titre.next_to(titre, DOWN, buff=0.45)
        exemple = _bullets(
            [
                "Littorale : papyrus, nénuphars, grenouilles, insectes.",
                "Limnétique : phytoplancton, zooplancton, tilapias, carpes.",
                "Profonde / benthique : vers, larves, bactéries, champignons décomposeurs.",
            ],
            font_size=21,
            width=56,
        )
        exemple.next_to(exemple_titre, DOWN, buff=0.35)

        with self.voiceover(
            text=(
                "Un étang de pisciculture ivoirien illustre bien ces trois "
                "zones : les tilapias et les carpes peuplent la zone "
                "limnétique, tandis que les décomposeurs de la vase "
                "recyclent les restes organiques qui tombent au fond."
            )
        ) as tracker:
            self.play(FadeIn(exemple_titre))
            self.play(FadeIn(exemple))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(exemple_titre), FadeOut(exemple))

        # --- Piège à éviter ----------------------------------------------------
        piege = warning_box(
            Text(
                _wrap(
                    "Ne pas confondre « biotope » et « biocénose ». L'eau, "
                    "le sol, la lumière et la température appartiennent au "
                    "biotope ; les êtres vivants (même microscopiques, "
                    "comme le phytoplancton) appartiennent à la "
                    "biocénose.",
                    width=54,
                ),
                font_size=21,
            ),
            box_width=11.8,
        )
        piege.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Piège classique à éviter : ne pas confondre biotope et "
                "biocénose. L'eau, le sol, la lumière et la température "
                "appartiennent au biotope. Les êtres vivants, même "
                "microscopiques, comme le phytoplancton ou le "
                "zooplancton, appartiennent à la biocénose."
            )
        ) as tracker:
            self.play(FadeIn(piege))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(titre), FadeOut(piege))
