"""
scenes/SVT_DigestionAliments_03.py — Chapitre 12 (1ereD, SVT), scène 03.

§ 12.2.1 Organisation générale du système digestif : définition (tube
digestif d'environ 9 m + glandes annexes), puis les 7 organes du tube
digestif dans l'ordre du trajet d'une bouchée, avec schéma simplifié.
Source : 1ereD/SVT.pdf, page 157.
"""

import textwrap

from manim import (
    DOWN,
    LEFT,
    RIGHT,
    UP,
    WHITE,
    YELLOW,
    Arrow,
    FadeIn,
    FadeOut,
    Rectangle,
    Text,
    VGroup,
    Write,
)

from shapes.base_scene import NotionScene
from shapes.boxes import definition_box, scene_title


def _wrap(text: str, width: int = 56) -> str:
    return "\n".join(textwrap.fill(line, width=width) for line in text.split("\n"))


def _organe(nom: str, couleur=WHITE, w=1.9, h=0.75, font_size=16):
    box = Rectangle(width=w, height=h, color=couleur, fill_color=couleur, fill_opacity=0.25)
    label = Text(nom, font_size=font_size, color=WHITE)
    label.set(width=min(label.width, w - 0.15))
    label.move_to(box.get_center())
    return VGroup(box, label)


class LeSystemeDigestifOrganisationGenerale(NotionScene):
    def construct(self):
        titre = scene_title("12.2 — Le système digestif")
        titre.scale(0.66)
        titre.to_edge(UP)

        # --- Énoncé : définition du système digestif ------------------------
        definition = definition_box(
            Text(
                _wrap(
                    "Le système digestif comprend le tube digestif, un "
                    "conduit long d'environ 9 mètres qui s'étend de la "
                    "bouche à l'anus, et les glandes digestives (ou "
                    "glandes annexes) qui fabriquent et déversent les "
                    "sucs digestifs.",
                    width=54,
                ),
                font_size=23,
            ),
            box_width=11.9,
        )
        definition.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Le système digestif comprend le tube digestif, un "
                "conduit long d'environ neuf mètres qui s'étend de la "
                "bouche à l'anus, et les glandes digestives, ou glandes "
                "annexes, qui fabriquent et déversent les sucs digestifs : "
                "les glandes salivaires, le foie et le pancréas. Les "
                "parois de l'estomac et de l'intestin grêle contiennent en "
                "outre de très nombreuses petites glandes."
            )
        ) as tracker:
            self.play(Write(titre))
            self.play(FadeIn(definition))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(definition))

        # --- Animation du raisonnement : les 7 organes, dans l'ordre --------
        entete = Text(
            "Le trajet d'une bouchée : 7 organes, dans l'ordre",
            font_size=25, color=YELLOW, weight="BOLD",
        )
        entete.next_to(titre, DOWN, buff=0.45)

        noms = [
            "1. Bouche", "2. Pharynx", "3. Œsophage", "4. Estomac",
            "5. Intestin grêle", "6. Gros intestin", "7. Rectum / anus",
        ]
        rangee1 = VGroup(*[_organe(n) for n in noms[:4]]).arrange(RIGHT, buff=0.55)
        rangee2 = VGroup(*[_organe(n) for n in noms[4:]]).arrange(RIGHT, buff=0.55)
        rangee2.next_to(rangee1, DOWN, buff=1.0).align_to(rangee1, LEFT)

        fleches1 = VGroup(
            *[
                Arrow(rangee1[i].get_right(), rangee1[i + 1].get_left(), buff=0.05, color=YELLOW, stroke_width=4)
                for i in range(len(rangee1) - 1)
            ]
        )
        fleche_liaison = Arrow(rangee1[3].get_bottom(), rangee2[0].get_top(), buff=0.08, color=YELLOW, stroke_width=4)
        fleches2 = VGroup(
            *[
                Arrow(rangee2[i].get_right(), rangee2[i + 1].get_left(), buff=0.05, color=YELLOW, stroke_width=4)
                for i in range(len(rangee2) - 1)
            ]
        )

        schema = VGroup(rangee1, rangee2, fleches1, fleche_liaison, fleches2)
        schema.next_to(entete, DOWN, buff=0.55)

        with self.voiceover(
            text=(
                "En suivant le trajet d'une bouchée de nourriture, on "
                "rencontre dans l'ordre : la bouche, où les aliments "
                "entrent ; le pharynx, carrefour des voies digestives et "
                "respiratoires ; l'œsophage, tube musculeux d'environ "
                "vingt-cinq centimètres qui traverse le thorax ; puis "
                "l'estomac, poche dilatable d'une capacité d'environ un "
                "litre et demi."
            )
        ) as tracker:
            self.play(FadeIn(entete))
            self.play(FadeIn(rangee1[0]))
            self.play(FadeIn(fleches1[0]), FadeIn(rangee1[1]))
            self.play(FadeIn(fleches1[1]), FadeIn(rangee1[2]))
            self.play(FadeIn(fleches1[2]), FadeIn(rangee1[3]))
            self.wait(tracker.get_remaining_duration())

        with self.voiceover(
            text=(
                "Puis l'intestin grêle, tube long d'environ six mètres, "
                "formé du duodénum, du jéjunum et de l'iléon ; le gros "
                "intestin, ou côlon, long d'environ un mètre et demi, qui "
                "encadre l'intestin grêle ; et enfin le rectum et l'anus, "
                "par où les résidus non digérés sont évacués."
            )
        ) as tracker:
            self.play(FadeIn(fleche_liaison), FadeIn(rangee2[0]))
            self.play(FadeIn(fleches2[0]), FadeIn(rangee2[1]))
            self.play(FadeIn(fleches2[1]), FadeIn(rangee2[2]))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(entete), FadeOut(schema))

        # --- Exemple traité : mesurer le tube digestif d'Awa ----------------
        exemple = Text(
            _wrap(
                "Exemple : mis bout à bout, l'œsophage (0,25 m) + "
                "l'estomac (organe court) + l'intestin grêle (6 m) + le "
                "gros intestin (1,5 m) confirment un tube digestif "
                "d'environ 9 m, roulé dans l'abdomen d'Awa.",
                width=54,
            ),
            font_size=22,
            color=WHITE,
        )
        exemple.next_to(titre, DOWN, buff=0.6)

        with self.voiceover(
            text=(
                "Exemple : mis bout à bout, l'œsophage d'environ "
                "vingt-cinq centimètres, l'estomac, court mais dilatable, "
                "l'intestin grêle d'environ six mètres et le gros "
                "intestin d'environ un mètre et demi confirment bien un "
                "tube digestif d'environ neuf mètres — entièrement roulé "
                "dans l'abdomen d'Awa."
            )
        ) as tracker:
            self.play(FadeIn(exemple))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(exemple))

        # --- À retenir --------------------------------------------------------
        a_retenir = Text(
            _wrap(
                "À retenir : un seul tube continu, de la bouche à l'anus, "
                "traversé successivement par les aliments — et des "
                "glandes annexes qui y déversent leurs sucs sans en faire "
                "partie.",
                width=54,
            ),
            font_size=23,
            color=WHITE,
        )
        a_retenir.next_to(titre, DOWN, buff=0.6)

        with self.voiceover(
            text=(
                "À retenir : le tube digestif est un seul conduit "
                "continu, de la bouche à l'anus, traversé successivement "
                "par les aliments. Les glandes annexes, elles, déversent "
                "leurs sucs dans ce tube, sans en faire partie — nous les "
                "détaillerons dans la scène suivante."
            )
        ) as tracker:
            self.play(FadeIn(a_retenir))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(titre), FadeOut(a_retenir))
