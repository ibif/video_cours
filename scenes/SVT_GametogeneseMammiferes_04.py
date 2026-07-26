"""
scenes/SVT_GametogeneseMammiferes_04.py — Chapitre 3 (1ereC, SVT), scène 04.

L'ovogenèse : localisation (follicules ovariques) ; phase 1, la
multiplication en vie fœtale, limitée dans le temps ; phase 2, la
croissance et le premier blocage en prophase I (follicule primordial,
stock de 1 à 2 millions d'ovocytes I à la naissance).
Source : 1ereC/SVT.pdf, pages 26-27.
"""

import textwrap

import numpy as np
from manim import (
    DOWN,
    LEFT,
    PURPLE,
    RIGHT,
    UP,
    WHITE,
    YELLOW,
    Circle,
    FadeIn,
    FadeOut,
    Text,
    VGroup,
    Write,
)

from shapes.base_scene import NotionScene
from shapes.boxes import definition_box, property_box, scene_title, warning_box


def _wrap(text: str, width: int = 56) -> str:
    return "\n".join(textwrap.fill(line, width=width) for line in text.split("\n"))


def _bullets(items, font_size=22, color=WHITE, width=52):
    lines = VGroup(
        *[Text(f"• {_wrap(it, width=width)}", font_size=font_size, color=color) for it in items]
    )
    lines.arrange(DOWN, aligned_edge=LEFT, buff=0.22)
    return lines


class OvogeneseLocalisationEtPremieresPhases(NotionScene):
    def construct(self):
        titre = scene_title("3.3 — L'ovogenèse : localisation et débuts")
        titre.scale(0.68)
        titre.to_edge(UP)

        # --- Énoncé : définition et localisation ---------------------------------
        definition = definition_box(
            Text(
                _wrap(
                    "L'ovogenèse se déroule dans les ovaires, au sein des "
                    "follicules ovariques : chaque follicule associe une "
                    "cellule germinale (ovogonie puis ovocyte) et des "
                    "cellules folliculaires nourricières. Contrairement à "
                    "la spermatogenèse, elle commence avant la naissance, "
                    "puis s'interrompt à deux reprises.",
                    width=54,
                ),
                font_size=22,
            ),
            box_width=12.2,
        )
        definition.next_to(titre, DOWN, buff=0.45)

        with self.voiceover(
            text=(
                "L'ovogenèse se déroule dans les ovaires, au sein des "
                "follicules ovariques. Chaque follicule associe une "
                "cellule germinale, ovogonie puis ovocyte, à des cellules "
                "folliculaires nourricières qui l'entourent. Contrairement "
                "à la spermatogenèse, l'ovogenèse commence avant la "
                "naissance, pendant la vie fœtale, puis s'interrompt à "
                "deux reprises avant de s'achever, éventuellement, au "
                "moment de la fécondation."
            )
        ) as tracker:
            self.play(Write(titre))
            self.play(FadeIn(definition))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(definition))

        # --- Animation du raisonnement : phase 1, multiplication fœtale --------
        entete_p1 = Text("Phase 1 — Multiplication (vie fœtale)", font_size=24, color=YELLOW, weight="BOLD")
        entete_p1.next_to(titre, DOWN, buff=0.45)

        p1 = _bullets(
            [
                "Pendant la vie embryonnaire, les ovogonies (2n) se "
                "multiplient par mitoses dans les ovaires du fœtus.",
                "Multiplication LIMITÉE DANS LE TEMPS : elle cesse avant "
                "la naissance — contrairement aux spermatogonies, jamais "
                "renouvelée ensuite.",
            ],
            font_size=21,
            width=50,
        )
        p1.next_to(entete_p1, DOWN, buff=0.35)

        with self.voiceover(
            text=(
                "Phase un : la multiplication, pendant la vie fœtale. Dans "
                "les ovaires du fœtus, les ovogonies, diploïdes, se "
                "multiplient par mitoses. Mais cette multiplication est "
                "limitée dans le temps : elle cesse avant la naissance. "
                "C'est une différence majeure avec la spermatogenèse : "
                "chez la femelle, il n'y aura plus jamais de production "
                "de nouvelles ovogonies après la naissance."
            )
        ) as tracker:
            self.play(FadeIn(entete_p1))
            self.play(FadeIn(p1))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(entete_p1), FadeOut(p1))

        # --- Exemple traité : phase 2, croissance, follicule primordial --------
        entete_p2 = Text("Phase 2 — Croissance et 1er blocage", font_size=24, color=YELLOW, weight="BOLD")
        entete_p2.next_to(titre, DOWN, buff=0.4)

        p2 = _bullets(
            [
                "Les ovogonies grossissent : ovocytes I (2n, chromosomes "
                "à 2 chromatides).",
                "Ils entrent en méiose I, qui se bloque en PROPHASE I "
                "(stade diplotène), dès la vie fœtale.",
                "Ovocyte bloqué + cellules folliculaires = follicule "
                "primordial.",
            ],
            font_size=19,
            width=46,
        )
        p2.next_to(entete_p2, DOWN, buff=0.3).to_edge(LEFT, buff=1.0)

        # Petit schéma : follicule primordial (ovocyte central entouré de
        # cellules folliculaires aplaties).
        ovocyte = Circle(radius=0.45, color=PURPLE, fill_color=PURPLE, fill_opacity=0.85)
        follicule = VGroup(ovocyte)
        for k in range(10):
            angle = k * (2 * np.pi / 10)
            cell = Circle(radius=0.14, color=YELLOW, fill_color=YELLOW, fill_opacity=0.7)
            cell.move_to(ovocyte.get_center() + 0.62 * np.array([np.cos(angle), np.sin(angle), 0]))
            follicule.add(cell)
        follicule.next_to(p2, RIGHT, buff=1.0).align_to(p2, UP).shift(DOWN * 0.4)
        label_foll = Text("Follicule\nprimordial", font_size=15, color=WHITE)
        label_foll.next_to(follicule, DOWN, buff=0.25)

        with self.voiceover(
            text=(
                "Phase deux : la croissance et le premier blocage. Les "
                "ovogonies entrent en croissance et deviennent des "
                "ovocytes de premier ordre, toujours diploïdes, mais avec "
                "des chromosomes désormais formés de deux chromatides. Ils "
                "s'engagent dans la méiose un, mais celle-ci se bloque en "
                "prophase de méiose un, dès la vie fœtale. Chaque ovocyte "
                "ainsi bloqué, entouré de cellules folliculaires, "
                "constitue un follicule primordial. Ce blocage peut durer "
                "de la vie fœtale jusqu'à la puberté, parfois pendant "
                "quarante à cinquante ans."
            )
        ) as tracker:
            self.play(FadeIn(entete_p2))
            self.play(FadeIn(p2))
            self.play(FadeIn(follicule), FadeIn(label_foll))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(entete_p2), FadeOut(p2), FadeOut(follicule), FadeOut(label_foll))

        # --- À retenir : effondrement du stock ------------------------------------
        retenir = property_box(
            _bullets(
                [
                    "5e mois fœtal : 6 à 7 millions d'ovocytes I.",
                    "À la naissance : 1 à 2 millions d'ovocytes I (déjà "
                    "TOUT le stock, jamais renouvelé).",
                    "À la puberté : environ 300 000 à 400 000 follicules.",
                    "Au cours de la vie génitale : seulement 400 à 500 "
                    "follicules arriveront à maturité.",
                ],
                font_size=20,
                width=50,
            ),
            box_width=12.2,
        )
        retenir.next_to(titre, DOWN, buff=0.45)

        with self.voiceover(
            text=(
                "Retenons l'effondrement de ce stock au fil du temps. Vers "
                "le cinquième mois de la vie fœtale, l'ovaire contient six "
                "à sept millions d'ovocytes de premier ordre. À la "
                "naissance, il n'en reste plus qu'un à deux millions : une "
                "petite fille possède alors déjà tout son stock de "
                "cellules germinales, il n'y en aura plus jamais "
                "d'autres. À la puberté, ce stock s'est encore réduit à "
                "environ trois cent mille à quatre cent mille follicules, "
                "et seulement quatre cents à cinq cents d'entre eux "
                "arriveront à maturité au cours de toute la vie génitale."
            )
        ) as tracker:
            self.play(FadeIn(retenir))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(retenir))

        # --- Piège à éviter ---------------------------------------------------
        piege = warning_box(
            Text(
                _wrap(
                    "Ne dis pas que l'ovogenèse « commence » à la puberté : "
                    "la multiplication des ovogonies et le premier "
                    "blocage en prophase I ont lieu AVANT la naissance. La "
                    "puberté marque seulement la REPRISE cyclique de la "
                    "méiose, pas son commencement.",
                    width=54,
                ),
                font_size=22,
            ),
            box_width=12.2,
        )
        piege.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Piège classique de devoir de niveau : ne dis jamais que "
                "l'ovogenèse commence à la puberté. La multiplication des "
                "ovogonies et le premier blocage en prophase de méiose un "
                "ont lieu avant la naissance, pendant la vie fœtale. La "
                "puberté marque seulement la reprise cyclique de la "
                "méiose, pas son commencement."
            )
        ) as tracker:
            self.play(FadeIn(piege))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(titre), FadeOut(piege))
