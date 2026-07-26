"""
scenes/SVT_GametogeneseMammiferes_05.py — Chapitre 3 (1ereC, SVT), scène 05.

L'ovogenèse : phase 3, reprise cyclique de la méiose I à la puberté
(follicule de Graaf, division inégale : ovocyte II + 1er globule
polaire) ; phase 4, deuxième blocage en métaphase II, achèvement
seulement si fécondation (2e globule polaire) ; bilan quantitatif.
Source : 1ereC/SVT.pdf, pages 27-28.
"""

import textwrap

from manim import (
    DOWN,
    LEFT,
    ORANGE,
    RED,
    RIGHT,
    UP,
    WHITE,
    YELLOW,
    Circle,
    FadeIn,
    FadeOut,
    MathTex,
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


class OvogenesePhasesTardivesEtBilan(NotionScene):
    def construct(self):
        titre = scene_title("3.4 — Ovogenèse : reprise, blocages, bilan")
        titre.scale(0.65)
        titre.to_edge(UP)

        # --- Énoncé : phase 3, reprise cyclique de la méiose I -----------------
        entete_p3 = Text("Phase 3 — Reprise cyclique (puberté→ménopause)", font_size=21, color=YELLOW, weight="BOLD")
        entete_p3.next_to(titre, DOWN, buff=0.45)

        p3 = _bullets(
            [
                "À partir de la puberté, à chaque cycle (~28 jours), un "
                "groupe de follicules reprend son évolution (FSH). Un "
                "seul devient follicule de Graaf (mûr), les autres "
                "régressent (atrésie folliculaire).",
                "Juste avant l'ovulation, sous l'action du pic de LH, "
                "l'ovocyte I achève la méiose I : division INÉGALE.",
            ],
            font_size=19,
            width=48,
        )
        p3.next_to(entete_p3, DOWN, buff=0.3)

        # Schéma : division inégale de la méiose I
        gros = Circle(radius=0.55, color=ORANGE, fill_color=ORANGE, fill_opacity=0.85)
        petit = Circle(radius=0.17, color=RED, fill_color=RED, fill_opacity=0.85)
        petit.next_to(gros, RIGHT, buff=0.15).align_to(gros, UP)
        division = VGroup(gros, petit)
        division.next_to(p3, DOWN, buff=0.4)
        label_div = Text(
            "Ovocyte II (gros, garde le cytoplasme) + 1er globule polaire (petit, dégénère)",
            font_size=15,
            color=WHITE,
        )
        label_div.next_to(division, DOWN, buff=0.2)

        with self.voiceover(
            text=(
                "Phase trois : la reprise cyclique de la méiose un, de la "
                "puberté à la ménopause. À partir de la puberté, à chaque "
                "cycle ovarien, environ vingt-huit jours, un petit groupe "
                "de follicules reprend son évolution sous l'action de la "
                "FSH. En principe, un seul follicule par cycle parvient au "
                "stade de follicule de Graaf, le follicule mûr ; les "
                "autres régressent, c'est l'atrésie folliculaire. Juste "
                "avant l'ovulation, sous l'action du pic de LH, l'ovocyte "
                "de premier ordre du follicule dominant achève enfin la "
                "méiose un : il produit deux cellules inégales. Un gros "
                "ovocyte de second ordre, qui garde presque tout le "
                "cytoplasme et les réserves, et un minuscule premier "
                "globule polaire, cellule avortée, dépourvue de "
                "cytoplasme, qui dégénère."
            )
        ) as tracker:
            self.play(Write(titre))
            self.play(FadeIn(entete_p3))
            self.play(FadeIn(p3))
            self.play(FadeIn(division), FadeIn(label_div))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(entete_p3), FadeOut(p3), FadeOut(division), FadeOut(label_div))

        # --- Animation du raisonnement : définition globule polaire ------------
        definition = definition_box(
            Text(
                _wrap(
                    "Un globule polaire est une petite cellule haploïde, "
                    "pratiquement dépourvue de cytoplasme, issue des "
                    "divisions inégales de l'ovogenèse. Il ne participe "
                    "pas à la reproduction et dégénère : sa formation "
                    "permet à l'ovocyte de conserver la quasi-totalité du "
                    "cytoplasme et des réserves nutritives.",
                    width=54,
                ),
                font_size=22,
            ),
            box_width=12.2,
        )
        definition.next_to(titre, DOWN, buff=0.45)

        with self.voiceover(
            text=(
                "Précisons cette notion de globule polaire. Les globules "
                "polaires sont de petites cellules haploïdes, pratiquement "
                "dépourvues de cytoplasme, issues des divisions inégales "
                "de l'ovogenèse. Ils ne participent pas à la reproduction "
                "et dégénèrent. Leur formation permet à l'ovocyte de "
                "conserver la quasi-totalité du cytoplasme et des réserves "
                "nutritives : c'est une stratégie qui concentre toutes les "
                "ressources dans une seule cellule."
            )
        ) as tracker:
            self.play(FadeIn(definition))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(definition))

        # --- Exemple traité : phase 4, deuxième blocage, bilan -------------------
        entete_p4 = Text("Phase 4 — Deuxième blocage et achèvement", font_size=22, color=YELLOW, weight="BOLD")
        entete_p4.next_to(titre, DOWN, buff=0.45)

        p4 = _bullets(
            [
                "L'ovocyte II entre en méiose II, qui se bloque à "
                "nouveau, en MÉTAPHASE II — c'est sous cette forme qu'il "
                "est expulsé à l'ovulation et capté par la trompe.",
                "La méiose II ne s'achève QUE si fécondation : entrée du "
                "spermatozoïde → 2e globule polaire + ovotide (ovule "
                "définitif, n).",
            ],
            font_size=19,
            width=48,
        )
        p4.next_to(entete_p4, DOWN, buff=0.3)

        bilan = MathTex(
            r"1\ \text{ovocyte I} \xrightarrow{\text{méiose I}} "
            r"1\ \text{ovocyte II} + 1\ \text{GP1} "
            r"\xrightarrow[\text{si fécondation}]{\text{méiose II}} "
            r"1\ \text{ovotide} + 1\ \text{GP2}",
            font_size=20,
            color=YELLOW,
        )
        bilan.set(width=min(bilan.width, 11.5))
        bilan.next_to(p4, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Phase quatre : le deuxième blocage et l'achèvement "
                "éventuel de l'ovogenèse. L'ovocyte de second ordre entre "
                "aussitôt en méiose deux, mais celle-ci se bloque de "
                "nouveau, en métaphase deux. C'est sous cette forme, "
                "ovocyte de second ordre bloqué en métaphase deux, que "
                "l'ovule est expulsé lors de l'ovulation et capté par la "
                "trompe de Fallope. La méiose deux ne s'achève que si une "
                "fécondation a lieu : l'entrée du spermatozoïde déclenche "
                "la fin de la métaphase deux, avec émission d'un deuxième "
                "globule polaire et formation de l'ovotide, l'ovule "
                "définitif, dont le noyau devient le pronoyau femelle. "
                "Faisons le bilan : un ovocyte de premier ordre, par "
                "méiose un, donne un ovocyte de second ordre plus un "
                "premier globule polaire ; puis, seulement s'il y a "
                "fécondation, la méiose deux donne un ovotide plus un "
                "deuxième globule polaire."
            )
        ) as tracker:
            self.play(FadeIn(entete_p4))
            self.play(FadeIn(p4))
            self.play(Write(bilan))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(entete_p4), FadeOut(p4), FadeOut(bilan))

        # --- À retenir : un seul gamète viable -------------------------------------
        retenir = property_box(
            Text(
                _wrap(
                    "L'ovogenèse ne produit en principe qu'un seul ovule "
                    "viable par cycle (et non quatre comme la "
                    "spermatogenèse), car les divisions cytoplasmiques "
                    "sont inégales : les globules polaires ne sont pas "
                    "fonctionnels.",
                    width=54,
                ),
                font_size=23,
            ),
            box_width=12.2,
        )
        retenir.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Retenons cette propriété essentielle : l'ovogenèse ne "
                "produit en principe qu'un seul ovule viable par cycle, et "
                "non quatre comme la spermatogenèse, parce que les "
                "divisions cytoplasmiques sont inégales : les globules "
                "polaires ne sont pas fonctionnels."
            )
        ) as tracker:
            self.play(FadeIn(retenir))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(retenir))

        # --- Piège à éviter : ovocyte ≠ ovule -------------------------------------
        piege = warning_box(
            Text(
                _wrap(
                    "La cellule expulsée à l'ovulation est un ovocyte II "
                    "bloqué en métaphase II, pas un ovule terminé. "
                    "L'ovogenèse n'est totalement achevée que si la "
                    "fécondation a lieu. « La femme produit un ovule par "
                    "cycle » est un abus de langage toléré à l'oral ; en "
                    "rédaction, préciser « ovocyte II ».",
                    width=54,
                ),
                font_size=21,
            ),
            box_width=12.2,
        )
        piege.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Piège fréquent : la cellule expulsée à l'ovulation est un "
                "ovocyte de second ordre, bloqué en métaphase deux, pas un "
                "ovule terminé. L'ovogenèse n'est totalement achevée que "
                "si la fécondation a lieu. Dire que la femme produit un "
                "ovule par cycle est un abus de langage toléré à l'oral, "
                "mais en rédaction, il faut préciser ovocyte de second "
                "ordre."
            )
        ) as tracker:
            self.play(FadeIn(piege))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(titre), FadeOut(piege))
