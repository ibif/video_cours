"""
scenes/SVT_GametogeneseMammiferes_03.py — Chapitre 3 (1ereC, SVT), scène 03.

La spermatogenèse : bilan quantitatif (1 spermatocyte I → 4 spermatides
→ 4 spermatozoïdes) et continuité / rendement (débute à la puberté,
continue jusqu'à la vieillesse, cycle de 70-75 jours, centaines de
millions de spermatozoïdes par jour).
Source : 1ereC/SVT.pdf, page 25.
"""

import textwrap

from manim import (
    DOWN,
    LEFT,
    ORANGE,
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
from shapes.boxes import example_box, property_box, scene_title, warning_box


def _wrap(text: str, width: int = 56) -> str:
    return "\n".join(textwrap.fill(line, width=width) for line in text.split("\n"))


def _bullets(items, font_size=22, color=WHITE, width=52):
    lines = VGroup(
        *[Text(f"• {_wrap(it, width=width)}", font_size=font_size, color=color) for it in items]
    )
    lines.arrange(DOWN, aligned_edge=LEFT, buff=0.22)
    return lines


class SpermatogeneseBilanEtRendement(NotionScene):
    def construct(self):
        titre = scene_title("3.2 — Spermatogenèse : bilan et rendement")
        titre.scale(0.68)
        titre.to_edge(UP)

        # --- Énoncé : bilan quantitatif ------------------------------------------
        entete_bilan = Text("Bilan quantitatif d'une méiose", font_size=26, color=YELLOW, weight="BOLD")
        entete_bilan.next_to(titre, DOWN, buff=0.5)

        bilan = MathTex(
            r"1\ \text{spermatocyte I} \xrightarrow{\text{méiose}} 4\ \text{spermatides} "
            r"\xrightarrow{\text{spermiogenèse}} 4\ \text{spermatozoïdes}",
            font_size=26,
            color=YELLOW,
        )
        bilan.set(width=min(bilan.width, 11.3))
        bilan.next_to(entete_bilan, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Faisons le bilan quantitatif d'une spermatogenèse : un "
                "spermatocyte de premier ordre, par méiose, donne quatre "
                "spermatides ; puis, par spermiogenèse, ces quatre "
                "spermatides donnent quatre spermatozoïdes. Un seul "
                "spermatocyte de premier ordre produit donc quatre gamètes "
                "mâles fonctionnels."
            )
        ) as tracker:
            self.play(Write(titre))
            self.play(FadeIn(entete_bilan))
            self.play(Write(bilan))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(entete_bilan), FadeOut(bilan))

        # --- Animation du raisonnement : schéma des 4 cellules égales -----------
        entete_schema = Text("Quatre cellules filles égales et viables", font_size=24, color=YELLOW, weight="BOLD")
        entete_schema.next_to(titre, DOWN, buff=0.45)

        cellules = VGroup(*[Circle(radius=0.35, color=ORANGE, fill_color=ORANGE, fill_opacity=0.8) for _ in range(4)])
        cellules.arrange(RIGHT, buff=0.6)
        cellules.next_to(entete_schema, DOWN, buff=0.6)

        egal_label = Text("Même taille, mêmes ressources → 4 spermatozoïdes viables", font_size=18, color=WHITE)
        egal_label.next_to(cellules, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Contrairement à ce qui se passe chez la femelle, les "
                "divisions cytoplasmiques de la spermatogenèse sont "
                "équitables : les quatre cellules issues de la méiose "
                "reçoivent chacune la même quantité de cytoplasme. Toutes "
                "les quatre sont donc viables et se différencient chacune "
                "en un spermatozoïde fonctionnel."
            )
        ) as tracker:
            self.play(FadeIn(entete_schema))
            self.play(FadeIn(cellules))
            self.play(FadeIn(egal_label))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(entete_schema), FadeOut(cellules), FadeOut(egal_label))

        # --- Exemple traité : continuité et rendement chiffré --------------------
        exemple = example_box(
            Text(
                _wrap(
                    "Un éjaculat de 3 mL contient en moyenne 100 millions "
                    "de spermatozoïdes par mL, soit environ 300 millions "
                    "de spermatozoïdes. Sur une vie active de 12 à 75 ans "
                    "(63 ans), en production continue, un homme fabrique "
                    "plusieurs milliers de milliards de spermatozoïdes : "
                    "un rendement considérable, sans commune mesure avec "
                    "l'ovogenèse.",
                    width=54,
                ),
                font_size=22,
            ),
            box_width=12.2,
        )
        exemple.next_to(titre, DOWN, buff=0.45)

        with self.voiceover(
            text=(
                "Prenons un exemple chiffré. Un éjaculat de trois "
                "millilitres contient en moyenne cent millions de "
                "spermatozoïdes par millilitre, soit environ trois cents "
                "millions de spermatozoïdes en tout. Comme la production "
                "est continue, de la puberté, vers douze à quatorze ans, "
                "jusqu'à un âge avancé, un homme fabrique, au cours de sa "
                "vie, plusieurs milliers de milliards de spermatozoïdes : "
                "un rendement considérable, sans commune mesure avec celui "
                "de l'ovogenèse."
            )
        ) as tracker:
            self.play(FadeIn(exemple))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(exemple))

        # --- À retenir : continuité et rythme -------------------------------------
        retenir = property_box(
            _bullets(
                [
                    "Débute à la puberté (~12-14 ans) sous l'action de la "
                    "testostérone, de la FSH et de la LH.",
                    "Se poursuit ensuite de façon CONTINUE jusqu'à la "
                    "vieillesse (jamais totalement arrêtée).",
                    "Cycle complet : environ 70 à 75 jours.",
                    "Production : plusieurs centaines de millions de "
                    "spermatozoïdes par jour ; 40 à 500 millions par "
                    "éjaculat (2 à 5 mL).",
                ],
                font_size=20,
                width=50,
            ),
            box_width=12.2,
        )
        retenir.next_to(titre, DOWN, buff=0.45)

        with self.voiceover(
            text=(
                "Retenons les caractéristiques de la spermatogenèse. Elle "
                "débute à la puberté, vers douze à quatorze ans, sous "
                "l'action de la testostérone et des hormones "
                "hypophysaires, FSH et LH, puis se poursuit de façon "
                "continue jusqu'à la vieillesse. Le cycle complet dure "
                "environ soixante-dix à soixante-quinze jours chez "
                "l'Homme. La production est considérable : plusieurs "
                "centaines de millions de spermatozoïdes chaque jour, et "
                "chaque éjaculat, de deux à cinq millilitres, en contient "
                "normalement entre quarante et cinq cents millions."
            )
        ) as tracker:
            self.play(FadeIn(retenir))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(retenir))

        # --- Piège à éviter ---------------------------------------------------
        piege = warning_box(
            Text(
                _wrap(
                    "Ne dis pas que la spermatogenèse s'arrête avec l'âge : "
                    "le vieillissement diminue la QUALITÉ des "
                    "spermatozoïdes (mobilité, morphologie), mais "
                    "n'interrompt jamais totalement leur production, "
                    "contrairement à l'ovogenèse qui, elle, s'arrête "
                    "définitivement à la ménopause.",
                    width=54,
                ),
                font_size=22,
            ),
            box_width=12.2,
        )
        piege.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Piège fréquent : ne dis pas que la spermatogenèse "
                "s'arrête avec l'âge. Le vieillissement diminue la "
                "qualité des spermatozoïdes, leur mobilité et leur "
                "morphologie, mais n'interrompt jamais totalement leur "
                "production, contrairement à l'ovogenèse qui, elle, "
                "s'arrête définitivement à la ménopause."
            )
        ) as tracker:
            self.play(FadeIn(piege))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(titre), FadeOut(piege))
