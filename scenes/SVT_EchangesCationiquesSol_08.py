"""
scenes/SVT_EchangesCationiquesSol_08.py — Chapitre 9 (1ereC, SVT), scène 08.

Le pH du sol : définition (échelle 0-14, acide/neutre/basique), pH eau vs
pH KCl, tableau de classification (fortement acide à fortement basique),
et origine de l'acidité des sols (5 causes). Source : 1ereC/SVT.pdf,
pages 102-103.
"""

import textwrap

from manim import (
    DOWN,
    GREEN,
    LEFT,
    ORANGE,
    RED,
    RIGHT,
    UP,
    WHITE,
    YELLOW,
    FadeIn,
    FadeOut,
    Line,
    Text,
    VGroup,
    Write,
)

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


class PHDuSol(NotionScene):
    def construct(self):
        titre = scene_title("9.7 — Le pH du sol")
        titre.scale(0.72)
        titre.to_edge(UP)

        # --- Énoncé : un indicateur simple mais essentiel --------------------
        intro = Text(
            _wrap(
                "Un seul nombre résume l'acidité d'un sol : son pH. Cet "
                "indicateur simple conditionne pourtant presque tout ce "
                "que nous avons vu jusqu'ici.",
                width=56,
            ),
            font_size=26,
            color=WHITE,
        )
        intro.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Un seul nombre résume l'acidité d'un sol : son pH. Cet "
                "indicateur, simple à mesurer, conditionne pourtant "
                "presque tout ce que nous avons vu jusqu'ici : la "
                "saturation du complexe, la disponibilité des éléments "
                "nutritifs, la toxicité de certains ions."
            )
        ) as tracker:
            self.play(Write(titre))
            self.play(FadeIn(intro))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(intro))

        # --- Raisonnement : définition du pH + échelle graduée ---------------
        def_ph = definition_box(
            Text(
                _wrap(
                    "Le pH mesure l'acidité de la solution du sol, "
                    "c'est-à-dire sa concentration en ions H+. Il est "
                    "compris entre 0 et 14 : pH < 7, sol acide ; pH = 7, "
                    "sol neutre ; pH > 7, sol basique (excès d'ions OH-).",
                    width=54,
                ),
                font_size=21,
            ),
            box_width=11.8,
        )
        def_ph.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Le pH, ou potentiel hydrogène, mesure l'acidité de la "
                "solution du sol, c'est-à-dire sa concentration en ions "
                "H+. Il est compris entre zéro et quatorze. En dessous de "
                "sept, le sol est acide, un excès d'ions H+. À sept, il "
                "est neutre. Au-dessus de sept, il est basique, ou "
                "alcalin, un excès d'ions OH-."
            )
        ) as tracker:
            self.play(FadeIn(def_ph))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(def_ph))

        # Échelle graduée simple 0-14
        echelle = Line(LEFT * 5, RIGHT * 5, color=WHITE, stroke_width=4)
        echelle.next_to(titre, DOWN, buff=0.9)
        graduations = VGroup()
        for i in range(0, 15, 2):
            x = echelle.get_start()[0] + (i / 14) * (echelle.get_end()[0] - echelle.get_start()[0])
            tick = Line([x, echelle.get_center()[1] - 0.1, 0], [x, echelle.get_center()[1] + 0.1, 0], color=WHITE)
            label = Text(str(i), font_size=16, color=WHITE).next_to(tick, DOWN, buff=0.1)
            graduations.add(tick, label)
        zone_acide = Text("Acide", font_size=18, color=RED).next_to(echelle, UP, buff=0.15).align_to(echelle, LEFT).shift(RIGHT * 0.8)
        zone_neutre = Text("Neutre", font_size=18, color=YELLOW).next_to(echelle, UP, buff=0.15).move_to([echelle.get_center()[0], 0, 0]).align_to(echelle, UP)
        zone_basique = Text("Basique", font_size=18, color=GREEN).next_to(echelle, UP, buff=0.15).align_to(echelle, RIGHT).shift(LEFT * 0.8)
        zone_neutre.shift(UP * 0.4)
        zone_acide.shift(UP * 0.4)
        zone_basique.shift(UP * 0.4)

        schema_ph = VGroup(echelle, graduations, zone_acide, zone_neutre, zone_basique)

        with self.voiceover(
            text=(
                "En pratique, la plupart des sols ont un pH compris "
                "entre quatre et neuf sur cette échelle. On distingue "
                "aussi deux façons de le mesurer : le pH eau, mesuré sur "
                "une suspension de sol dans l'eau, et le pH KCl, mesuré "
                "dans une solution de chlorure de potassium, qui fait "
                "apparaître l'acidité de réserve portée par le complexe. "
                "On a toujours pH KCl inférieur au pH eau."
            )
        ) as tracker:
            self.play(FadeIn(schema_ph))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(schema_ph))

        # --- Tableau de classification -----------------------------------------
        tab_titre = Text("Classification du sol selon le pH", font_size=23, color=YELLOW, weight="BOLD")
        tab_titre.next_to(titre, DOWN, buff=0.5)

        classes = _bullets(
            [
                "pH < 5,5 : sol fortement acide",
                "5,5 ≤ pH < 6,5 : sol acide",
                "6,5 ≤ pH ≤ 7,3 : sol neutre ou presque neutre",
                "7,3 < pH ≤ 8,5 : sol basique (calcaire)",
                "pH > 8,5 : sol fortement basique",
            ],
            font_size=21,
            width=52,
        )
        classes.next_to(tab_titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Voici la classification détaillée des sols selon leur "
                "pH. En dessous de cinq virgule cinq : sol fortement "
                "acide. Entre cinq virgule cinq et six virgule cinq : sol "
                "acide. Entre six virgule cinq et sept virgule trois : "
                "sol neutre ou presque neutre. Entre sept virgule trois "
                "et huit virgule cinq : sol basique, ou calcaire. "
                "Au-dessus de huit virgule cinq : sol fortement basique."
            )
        ) as tracker:
            self.play(FadeIn(tab_titre))
            self.play(FadeIn(classes))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(tab_titre), FadeOut(classes))

        # --- À retenir : origine de l'acidité des sols --------------------------
        origine_titre = Text("Origine de l'acidité des sols", font_size=25, color=YELLOW, weight="BOLD")
        origine_titre.next_to(titre, DOWN, buff=0.5)

        origine = _bullets(
            [
                "Le lessivage des bases par les eaux de pluie abondantes "
                "(climat ivoirien)",
                "La décomposition de la matière organique (acides "
                "organiques)",
                "La respiration des racines et des micro-organismes "
                "(CO2 → acide)",
                "L'exportation des récoltes (bases non restituées au "
                "sol)",
                "L'usage excessif de certains engrais (sulfate "
                "d'ammonium, urée)",
            ],
            font_size=19,
            width=54,
        )
        origine.next_to(origine_titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "D'où vient l'acidité des sols ? Un sol devient acide "
                "lorsque les ions H+, et l'aluminium, envahissent le "
                "complexe argilo-humique. Cinq causes principales. Le "
                "lessivage des bases par les eaux de pluie abondantes, "
                "typique du climat équatorial et subéquatorial ivoirien. "
                "La décomposition de la matière organique, qui produit "
                "des acides organiques. La respiration des racines et des "
                "micro-organismes, qui dégage du CO2 formant un acide "
                "dans l'eau. L'exportation des récoltes : chaque récolte "
                "emporte des bases qui ne sont pas restituées au sol. Et "
                "enfin l'usage excessif de certains engrais, comme le "
                "sulfate d'ammonium ou l'urée, qui acidifient le sol à "
                "long terme."
            )
        ) as tracker:
            self.play(FadeIn(origine_titre))
            self.play(FadeIn(origine))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(origine_titre), FadeOut(origine))

        # --- Piège à éviter : échelle logarithmique -----------------------------
        piege = warning_box(
            Text(
                _wrap(
                    "Piège à éviter : le pH est une échelle logarithmique. "
                    "Passer de pH 5 à pH 6, c'est diviser par 10 la "
                    "concentration en ions H+, pas la diminuer d'une "
                    "unité quelconque.",
                    width=54,
                ),
                font_size=22,
            ),
            box_width=11.8,
        )
        piege.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Un piège fréquent à éviter : le pH est une échelle "
                "logarithmique. Passer de pH cinq à pH six, ce n'est pas "
                "diminuer l'acidité d'une petite unité : c'est diviser "
                "par dix la concentration en ions H+. Un écart d'une "
                "seule unité de pH correspond donc à un facteur dix sur "
                "l'acidité réelle du sol."
            )
        ) as tracker:
            self.play(FadeIn(piege))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(titre), FadeOut(piege))
