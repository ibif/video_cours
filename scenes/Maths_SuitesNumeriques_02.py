"""
scenes/Maths_SuitesNumeriques_02.py — Chapitre 15 « Suites numériques »
(1ereC, Maths), scène 02.

Modes de génération d'une suite : formule explicite (un = f(n)) et relation
de récurrence (u0 donné, u(n+1) = f(un)). Exemples résolus 1 et 2.
Source : 1ereC/Maths.pdf, chapitre 15, pages 176-188.
"""

import textwrap

from manim import DOWN, UP, FadeIn, FadeOut, MathTex, Text, VGroup, Write, YELLOW

from shapes.base_scene import NotionScene
from shapes.boxes import definition_box, essentiel_box, example_box, scene_title, warning_box


def _wrap(text: str, width: int = 58) -> str:
    return "\n".join(textwrap.fill(line, width=width) for line in text.split("\n"))


class ModesGenerationSuite(NotionScene):
    def construct(self):
        titre = scene_title("Modes de génération : explicite et récurrence")
        titre.scale(0.48)
        titre.to_edge(UP)
        self.play(Write(titre))

        # --- Énoncé : suite explicite --------------------------------------------
        def_explicite = definition_box(
            VGroup(
                Text(
                    "Une suite est définie de façon explicite quand un\n"
                    "s'exprime directement en fonction de n :",
                    font_size=23,
                ),
                MathTex(r"u_n = f(n)", font_size=32),
            ).arrange(DOWN, buff=0.3),
            box_width=9.6,
        )
        def_explicite.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Premier mode de génération : la formule explicite. Une "
                "suite est définie de façon explicite lorsque son terme "
                "général u indice n s'exprime directement en fonction de n, "
                "sous la forme u indice n égale f de n. On calcule alors "
                "n'importe quel terme directement, sans passer par les "
                "précédents."
            )
        ) as tracker:
            self.play(FadeIn(def_explicite))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(def_explicite))

        # --- Exemple résolu 1 -----------------------------------------------------
        ex1_titre = Text(
            "Exemple 1 — un = n² - 3n + 1 :",
            font_size=24,
            color=YELLOW,
            weight="BOLD",
        )
        ex1_titre.next_to(titre, DOWN, buff=0.4)
        ex1_calc = example_box(
            MathTex(
                r"""
                u_0 = 1, \quad u_1 = -1, \quad u_2 = -1, \quad
                u_{10} = 100-30+1 = 71
                """,
                font_size=25,
            ),
            box_width=11.0,
        )
        ex1_calc.next_to(ex1_titre, DOWN, buff=0.3)

        with self.voiceover(
            text=(
                "Exemple : soit u indice n égale n carré moins trois n plus "
                "un. On calcule directement u zéro égale un, u un égale "
                "moins un, u deux égale moins un également, et même u dix, "
                "en remplaçant n par dix : cent moins trente plus un, soit "
                "soixante et onze. Chaque terme se calcule indépendamment "
                "des autres."
            )
        ) as tracker:
            self.play(FadeIn(ex1_titre))
            self.play(FadeIn(ex1_calc))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(ex1_titre), FadeOut(ex1_calc))

        # --- Énoncé : suite récurrente ---------------------------------------------
        def_recurrence = definition_box(
            VGroup(
                Text(
                    "Une suite est définie par récurrence quand on donne\n"
                    "son premier terme, et une relation liant deux termes\n"
                    "consécutifs :",
                    font_size=22,
                ),
                MathTex(r"u_0 \text{ donné}, \qquad u_{n+1} = f(u_n)", font_size=30),
            ).arrange(DOWN, buff=0.3),
            box_width=10.8,
        )
        def_recurrence.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Deuxième mode de génération : la relation de récurrence. "
                "On donne le premier terme u zéro, ainsi qu'une relation "
                "qui permet de calculer chaque terme à partir du "
                "précédent : u indice n plus un égale f de u indice n. Pour "
                "obtenir un terme, il faut donc calculer tous les termes "
                "qui le précèdent, un par un."
            )
        ) as tracker:
            self.play(FadeIn(def_recurrence))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(def_recurrence))

        # --- Exemple résolu 2 -----------------------------------------------------
        ex2_titre = Text(
            "Exemple 2 — v0 = 1, v(n+1) = 2vn + 3 :",
            font_size=24,
            color=YELLOW,
            weight="BOLD",
        )
        ex2_titre.next_to(titre, DOWN, buff=0.4)
        ex2_calc = example_box(
            MathTex(
                r"""
                v_1 = 2(1)+3 = 5, \quad
                v_2 = 2(5)+3 = 13, \quad
                v_3 = 2(13)+3 = 29
                """,
                font_size=25,
            ),
            box_width=11.2,
        )
        ex2_calc.next_to(ex2_titre, DOWN, buff=0.3)

        with self.voiceover(
            text=(
                "Exemple : soit v zéro égale un, et v indice n plus un "
                "égale deux fois v indice n, plus trois. On calcule v un en "
                "utilisant v zéro : deux fois un plus trois, soit cinq. "
                "Puis v deux, en utilisant v un : deux fois cinq plus "
                "trois, soit treize. Puis v trois : deux fois treize plus "
                "trois, soit vingt-neuf. Chaque terme dépend du précédent."
            )
        ) as tracker:
            self.play(FadeIn(ex2_titre))
            self.play(FadeIn(ex2_calc))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(ex2_titre), FadeOut(ex2_calc))

        # --- À retenir ---------------------------------------------------------
        retenir = essentiel_box(
            Text(
                _wrap(
                    "Deux modes de génération : explicite (un = f(n), "
                    "calcul direct de n'importe quel terme) et récurrence "
                    "(u0 donné, un+1 = f(un), calcul terme par terme à "
                    "partir du précédent).",
                    width=58,
                ),
                font_size=22,
            ),
            box_width=11.3,
        )
        retenir.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "À retenir : il existe deux façons de générer une suite. "
                "La formule explicite, qui donne accès directement à "
                "n'importe quel terme. Et la relation de récurrence, qui "
                "impose de calculer les termes les uns après les autres, "
                "à partir du terme initial."
            )
        ) as tracker:
            self.play(FadeIn(retenir))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(retenir))

        # --- Piège à éviter ----------------------------------------------------
        piege = warning_box(
            Text(
                _wrap(
                    "Pour une suite récurrente, impossible de calculer u10 "
                    "directement sans passer par u1, u2, ..., u9 : il n'y a "
                    "pas de raccourci, sauf à trouver ensuite une formule "
                    "explicite équivalente.",
                    width=56,
                ),
                font_size=22,
            ),
            box_width=11.2,
        )
        piege.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Piège à éviter : pour une suite définie par récurrence, il "
                "est impossible de calculer directement, par exemple, le "
                "dixième terme sans être passé par tous les termes "
                "précédents. Il n'y a aucun raccourci, à moins de réussir "
                "à établir ensuite une formule explicite équivalente."
            )
        ) as tracker:
            self.play(FadeIn(piege))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(piege), FadeOut(titre))
