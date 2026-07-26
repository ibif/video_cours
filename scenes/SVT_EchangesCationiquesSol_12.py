"""
scenes/SVT_EchangesCationiquesSol_12.py — Chapitre 9 (1ereC, SVT), scène 12.

Application : les sols agricoles en Côte d'Ivoire — la fatigue des sols
(définition, 5 facteurs contributifs en contexte ivoirien) et la jachère
(définition, mécanisme de restauration, limite des jachères de plus en
plus courtes). Source : 1ereC/SVT.pdf, page 105.
"""

import textwrap

from manim import DOWN, LEFT, RIGHT, UP, WHITE, YELLOW, FadeIn, FadeOut, Text, VGroup, Write

from shapes.base_scene import NotionScene
from shapes.boxes import definition_box, scene_title, warning_box


def _wrap(text: str, width: int = 56) -> str:
    return "\n".join(textwrap.fill(line, width=width) for line in text.split("\n"))


def _bullets(items, font_size=24, color=WHITE, width=54):
    lines = VGroup(
        *[Text(f"• {_wrap(it, width=width)}", font_size=font_size, color=color) for it in items]
    )
    lines.arrange(DOWN, aligned_edge=LEFT, buff=0.22)
    return lines


class SolsAgricolesCotedIvoire(NotionScene):
    def construct(self):
        titre = scene_title("9.11 — Les sols agricoles en Côte d'Ivoire")
        titre.scale(0.6)
        titre.to_edge(UP)

        # --- Énoncé : le constat de la fatigue des sols ----------------------
        intro = Text(
            _wrap(
                "Sur de nombreuses vieilles plantations ivoiriennes de "
                "cacao ou de café, les rendements baissent d'année en "
                "année, malgré un entretien régulier : c'est la fatigue "
                "des sols.",
                width=56,
            ),
            font_size=24,
            color=WHITE,
        )
        intro.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Sur de nombreuses vieilles plantations ivoiriennes de "
                "cacao ou de café, les rendements baissent d'année en "
                "année, malgré un entretien régulier. C'est ce qu'on "
                "appelle la fatigue des sols, un phénomène concret que "
                "tout notre chapitre permet enfin d'expliquer."
            )
        ) as tracker:
            self.play(Write(titre))
            self.play(FadeIn(intro))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(intro))

        # --- Raisonnement : définition + 5 facteurs de la fatigue des sols --
        def_fatigue = definition_box(
            Text(
                _wrap(
                    "La fatigue des sols est la dégradation progressive "
                    "de la fertilité d'un sol cultivé de façon continue "
                    "et intensive, sans restitution suffisante des "
                    "éléments exportés. Elle se traduit par la baisse "
                    "des rendements.",
                    width=54,
                ),
                font_size=21,
            ),
            box_width=11.8,
        )
        def_fatigue.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "La fatigue des sols est la dégradation progressive de "
                "la fertilité d'un sol cultivé de façon continue et "
                "intensive, sans restitution suffisante des éléments "
                "exportés. Elle se traduit très concrètement par la "
                "baisse des rendements."
            )
        ) as tracker:
            self.play(FadeIn(def_fatigue))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(def_fatigue))

        facteurs_titre = Text("5 facteurs, en contexte ivoirien", font_size=24, color=YELLOW, weight="BOLD")
        facteurs_titre.next_to(titre, DOWN, buff=0.4)

        facteurs = _bullets(
            [
                "Le lessivage intense sous les fortes pluies des zones "
                "forestières (Sud et Centre-Ouest : cacao, café, hévéa)",
                "Les exportations par les récoltes, non compensées par "
                "des apports d'engrais suffisants",
                "La déforestation et la culture continue, qui détruisent "
                "l'humus, donc la CEC",
                "Les feux de brousse, qui brûlent la matière organique",
                "L'acidification progressive (chute du pH, toxicité "
                "aluminique), qui bloque le phosphore",
            ],
            font_size=19,
            width=54,
        )
        facteurs.next_to(facteurs_titre, DOWN, buff=0.35)

        with self.voiceover(
            text=(
                "En Côte d'Ivoire, la fatigue des sols résulte de la "
                "combinaison de cinq facteurs. Le lessivage intense sous "
                "les fortes pluies des zones forestières, au Sud et au "
                "Centre-Ouest, zones du cacao, du café, de l'hévéa. Les "
                "exportations par les récoltes, non compensées par des "
                "apports d'engrais suffisants. La déforestation et la "
                "culture continue, qui détruisent l'humus, et donc la "
                "CEC. Les feux de brousse, qui brûlent la matière "
                "organique. Et enfin l'acidification progressive, avec la "
                "chute du pH et la toxicité aluminique, qui bloque le "
                "phosphore."
            )
        ) as tracker:
            self.play(FadeIn(facteurs_titre))
            self.play(FadeIn(facteurs))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(facteurs_titre), FadeOut(facteurs))

        # --- Exemple traité : la jachère, une solution traditionnelle -------
        def_jachere = definition_box(
            Text(
                _wrap(
                    "La jachère est la mise en repos temporaire d'une "
                    "terre cultivée : on abandonne la culture pendant "
                    "plusieurs années afin que la végétation naturelle "
                    "repousse et que le sol reconstitue sa fertilité.",
                    width=54,
                ),
                font_size=21,
            ),
            box_width=11.8,
        )
        def_jachere.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Face à cette fatigue, les paysans ivoiriens pratiquent "
                "traditionnellement la jachère : la mise en repos "
                "temporaire d'une terre cultivée. On abandonne la culture "
                "pendant plusieurs années, afin que la végétation "
                "naturelle repousse et que le sol reconstitue sa "
                "fertilité."
            )
        ) as tracker:
            self.play(FadeIn(def_jachere))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(def_jachere))

        mecanisme_titre = Text("Mécanisme de restauration pendant la jachère", font_size=21, color=YELLOW, weight="BOLD")
        mecanisme_titre.next_to(titre, DOWN, buff=0.4)

        mecanisme = _bullets(
            [
                "La végétation spontanée puise les éléments minéraux en "
                "profondeur et les restitue en surface par la chute des "
                "feuilles",
                "La matière organique s'accumule : l'humus se reforme, "
                "la CEC augmente",
                "Le complexe se resature en bases, et le pH remonte "
                "légèrement",
                "La vie du sol (micro-organismes, lombrics) se "
                "rétablit",
            ],
            font_size=19,
            width=54,
        )
        mecanisme.next_to(mecanisme_titre, DOWN, buff=0.35)

        with self.voiceover(
            text=(
                "Voici comment la jachère restaure la fertilité, en "
                "quatre points. La végétation spontanée puise les "
                "éléments minéraux en profondeur, et les restitue en "
                "surface par la chute de ses feuilles. La matière "
                "organique s'accumule : l'humus se reforme, la CEC "
                "augmente. Le complexe se resature en bases, et le pH "
                "remonte légèrement. Et la vie du sol, micro-organismes "
                "et lombrics, se rétablit."
            )
        ) as tracker:
            self.play(FadeIn(mecanisme_titre))
            self.play(FadeIn(mecanisme))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(mecanisme_titre), FadeOut(mecanisme))

        # --- À retenir / piège : jachères de plus en plus courtes -----------
        limite = warning_box(
            Text(
                _wrap(
                    "Limite : avec la pression démographique et le "
                    "manque de terres, les jachères sont de plus en plus "
                    "courtes (2-3 ans au lieu de 10-15 ans) et ne "
                    "suffisent plus à régénérer le sol. D'où l'importance "
                    "des engrais organiques et minéraux, du chaulage des "
                    "sols acides, et des techniques de conservation "
                    "(couverture végétale, agroforesterie, association "
                    "avec les légumineuses fixatrices d'azote).",
                    width=54,
                ),
                font_size=19,
            ),
            box_width=12.0,
        )
        limite.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Mais attention, une limite sérieuse : avec la pression "
                "démographique et le manque de terres, les jachères sont "
                "de plus en plus courtes, deux à trois ans, au lieu de "
                "dix à quinze ans autrefois, et ne suffisent plus à "
                "régénérer le sol. D'où l'importance croissante des "
                "engrais organiques et minéraux, du chaulage des sols "
                "acides, et des techniques de conservation, couverture "
                "végétale, agroforesterie, association avec des "
                "légumineuses fixatrices d'azote, pour compenser le "
                "recul de la jachère traditionnelle."
            )
        ) as tracker:
            self.play(FadeIn(limite))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(titre), FadeOut(limite))
