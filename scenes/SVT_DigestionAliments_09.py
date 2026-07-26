"""
scenes/SVT_DigestionAliments_09.py — Chapitre 12 (1ereD, SVT), scène 09.

§ 12.6 Le devenir des nutriments : l'absorption intestinale. Définition,
siège (intestin grêle, villosités, surface immense), schéma d'une
villosité, devenir de chaque nutriment (glucose/acides aminés → sang →
veine porte → foie ; acides gras/glycérol → lymphe). Piège : l'absorption
n'a pas lieu dans l'estomac.
Source : 1ereD/SVT.pdf, pages 163-165.
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
    Ellipse,
    FadeIn,
    FadeOut,
    Line,
    Text,
    VGroup,
    Write,
)

from shapes.base_scene import NotionScene
from shapes.boxes import definition_box, example_box, scene_title, warning_box


def _wrap(text: str, width: int = 56) -> str:
    return "\n".join(textwrap.fill(line, width=width) for line in text.split("\n"))


def _bullets(items, font_size=21, color=WHITE, width=54):
    lines = VGroup(
        *[Text(f"• {_wrap(it, width=width)}", font_size=font_size, color=color) for it in items]
    )
    lines.arrange(DOWN, aligned_edge=LEFT, buff=0.22)
    return lines


class LAbsorptionIntestinale(NotionScene):
    def construct(self):
        titre = scene_title("12.6 — L'absorption intestinale")
        titre.scale(0.62)
        titre.to_edge(UP)

        # --- Énoncé : définition de l'absorption -------------------------------
        definition = definition_box(
            Text(
                _wrap(
                    "L'absorption intestinale est le passage des "
                    "nutriments et de l'eau de la cavité de l'intestin "
                    "grêle vers le sang et la lymphe, à travers la paroi "
                    "des villosités intestinales.",
                    width=54,
                ),
                font_size=23,
            ),
            box_width=11.9,
        )
        definition.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "L'absorption intestinale est le passage des nutriments "
                "et de l'eau de la cavité de l'intestin grêle vers le "
                "sang et la lymphe, à travers la paroi des villosités "
                "intestinales."
            )
        ) as tracker:
            self.play(Write(titre))
            self.play(FadeIn(definition))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(definition))

        # --- Animation du raisonnement : une surface d'échange immense ---------
        entete_surface = Text("Une surface d'échange immense", font_size=24, color=YELLOW, weight="BOLD")
        entete_surface.next_to(titre, DOWN, buff=0.45)

        surface_bullets = _bullets(
            [
                "Le tube mesure environ 6 m de long.",
                "Sa paroi forme des plis, hérissés de 4 à 5 millions de villosités (≈1 mm).",
                "Chaque cellule d'une villosité porte elle-même des microvillosités.",
                "Surface totale : environ 200 à 300 m² — un terrain de tennis dans l'abdomen !",
            ],
            font_size=20,
            width=54,
        )
        surface_bullets.next_to(entete_surface, DOWN, buff=0.35)

        with self.voiceover(
            text=(
                "Le siège presque exclusif de l'absorption des nutriments "
                "est l'intestin grêle. Son organisation interne réalise "
                "une surface d'échange immense : le tube mesure environ "
                "six mètres de long ; sa paroi interne forme des plis, "
                "hérissés d'environ quatre à cinq millions de villosités, "
                "petits reliefs d'environ un millimètre ; et chaque "
                "cellule de la surface d'une villosité porte elle-même des "
                "microvillosités. Au total, la surface d'échange atteint "
                "environ deux cents à trois cents mètres carrés, soit la "
                "surface d'un terrain de tennis, logée dans un tube qui "
                "tient dans l'abdomen !"
            )
        ) as tracker:
            self.play(FadeIn(entete_surface))
            self.play(FadeIn(surface_bullets))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(entete_surface), FadeOut(surface_bullets))

        # --- Schéma d'une villosité intestinale --------------------------------
        entete_schema = Text("Schéma d'une villosité intestinale", font_size=23, color=YELLOW, weight="BOLD")
        entete_schema.next_to(titre, DOWN, buff=0.4)

        villosite = Ellipse(width=1.6, height=3.2, color=WHITE, fill_color="#E8D9B5", fill_opacity=0.35)
        capillaire = Line(villosite.get_bottom() + UP * 0.3, villosite.get_top() + DOWN * 0.5, color=RED, stroke_width=6)
        capillaire.shift(LEFT * 0.25)
        chylifere = Line(villosite.get_bottom() + UP * 0.3, villosite.get_top() + DOWN * 0.5, color=YELLOW, stroke_width=6)
        chylifere.shift(RIGHT * 0.25)
        villo_group = VGroup(villosite, capillaire, chylifere)
        villo_group.next_to(entete_schema, DOWN, buff=0.4).shift(LEFT * 2.8)

        label_capillaire = Text("Capillaires sanguins :\nglucose, acides aminés", font_size=17, color=RED)
        label_capillaire.next_to(villo_group, RIGHT, buff=1.1).shift(UP * 0.9)
        arrow_capillaire = Arrow(label_capillaire.get_left(), capillaire.get_center(), buff=0.1, color=RED)

        label_chylifere = Text("Vaisseau chylifère (lymphe) :\nacides gras, glycérol", font_size=17, color=YELLOW)
        label_chylifere.next_to(villo_group, RIGHT, buff=1.1).shift(DOWN * 0.9)
        arrow_chylifere = Arrow(label_chylifere.get_left(), chylifere.get_center(), buff=0.1, color=YELLOW)

        schema = VGroup(villo_group, label_capillaire, arrow_capillaire, label_chylifere, arrow_chylifere)

        with self.voiceover(
            text=(
                "Chaque villosité contient un réseau de capillaires "
                "sanguins et un vaisseau chylifère, un vaisseau "
                "lymphatique, séparés de la lumière intestinale par une "
                "paroi très fine. Le glucose et les acides aminés passent "
                "dans les capillaires sanguins ; les acides gras et le "
                "glycérol passent dans le vaisseau chylifère."
            )
        ) as tracker:
            self.play(FadeIn(entete_schema))
            self.play(FadeIn(villo_group))
            self.play(FadeIn(label_capillaire), FadeIn(arrow_capillaire))
            self.play(FadeIn(label_chylifere), FadeIn(arrow_chylifere))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(entete_schema), FadeOut(schema))

        # --- Exemple traité : le devenir du glucose de l'attiéké d'Awa -----------
        exemple = example_box(
            Text(
                _wrap(
                    "Le glucose issu de l'attiéké d'Awa passe dans les "
                    "capillaires d'une villosité de son intestin grêle, "
                    "rejoint la veine porte hépatique, traverse le foie "
                    "puis gagne la circulation générale. Distribué aux "
                    "cellules — par exemple des muscles — il est utilisé "
                    "par la respiration cellulaire pour produire de "
                    "l'énergie.",
                    width=54,
                ),
                font_size=20,
            ),
            box_width=12.0,
        )
        exemple.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Exemple traité : le glucose et les acides aminés "
                "traversent la paroi de la villosité et entrent dans les "
                "capillaires sanguins. Les vaisseaux de toutes les "
                "villosités se réunissent dans la veine porte hépatique, "
                "qui conduit le sang riche en nutriments au foie. Celui-ci "
                "contrôle, stocke une partie du glucose sous forme de "
                "glycogène, et répartit le reste ; le sang rejoint ensuite "
                "la circulation générale qui alimente toutes les "
                "cellules. Ainsi, le glucose issu de l'attiéké d'Awa "
                "passe dans les capillaires d'une villosité, rejoint la "
                "veine porte hépatique, traverse le foie, puis gagne la "
                "circulation générale : distribué aux cellules des "
                "muscles, par exemple, il sera utilisé par la respiration "
                "cellulaire pour produire l'énergie nécessaire aux "
                "activités quotidiennes. Les acides gras et le glycérol, "
                "eux, entrent dans le vaisseau chylifère, gagnent la "
                "lymphe, qui se jette finalement dans le sang au niveau "
                "des gros vaisseaux du cou. Les vitamines, les sels "
                "minéraux et l'eau passent directement dans le sang, sans "
                "avoir subi de digestion."
            )
        ) as tracker:
            self.play(FadeIn(exemple))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(exemple))

        # --- À retenir : le gros intestin ----------------------------------------
        a_retenir = Text(
            _wrap(
                "À retenir : dans le gros intestin, une grande partie de "
                "l'eau restante et des sels minéraux est encore absorbée. "
                "La flore intestinale y fermente les fibres et fabrique "
                "certaines vitamines. Les résidus définitivement "
                "inutilisables forment les fèces.",
                width=54,
            ),
            font_size=22,
            color=WHITE,
        )
        a_retenir.next_to(titre, DOWN, buff=0.55)

        with self.voiceover(
            text=(
                "À retenir : dans le gros intestin, une grande partie de "
                "l'eau restante et des sels minéraux est encore absorbée. "
                "La flore intestinale, ou microbiote, y fermente les "
                "fibres et fabrique certaines vitamines. Les résidus "
                "définitivement inutilisables forment les fèces."
            )
        ) as tracker:
            self.play(FadeIn(a_retenir))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(a_retenir))

        # --- Piège à éviter -----------------------------------------------------------
        piege = warning_box(
            Text(
                _wrap(
                    "Ne place pas l'absorption dans l'estomac : l'estomac "
                    "absorbe très peu de choses (un peu d'eau, l'alcool, "
                    "certains médicaments). C'est l'intestin grêle qui "
                    "absorbe l'immense majorité des nutriments. Le gros "
                    "intestin, lui, absorbe surtout de l'eau et des sels "
                    "minéraux.",
                    width=54,
                ),
                font_size=21,
            ),
            box_width=12.0,
        )
        piege.next_to(titre, DOWN, buff=0.55)

        with self.voiceover(
            text=(
                "Ne place pas l'absorption dans l'estomac : l'estomac "
                "absorbe très peu de choses, un peu d'eau, de l'alcool, "
                "certains médicaments. C'est l'intestin grêle qui absorbe "
                "l'immense majorité des nutriments. Le gros intestin, lui, "
                "absorbe surtout de l'eau et des sels minéraux."
            )
        ) as tracker:
            self.play(FadeIn(piege))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(titre), FadeOut(piege))
