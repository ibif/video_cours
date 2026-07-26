"""
scenes/SVT_EchangesCationiquesSol_01.py — Chapitre 9 (1ereC, SVT), scène 01.

Introduction du chapitre « Les échanges d'ions au niveau du sol » : qu'est-
ce qu'un ion (cation / anion, exemples), origine des ions du sol,
définition de la solution du sol, et objectifs du chapitre. Source :
1ereC/SVT.pdf, pages 95-97.
"""

import textwrap

from manim import DOWN, LEFT, RIGHT, UP, WHITE, YELLOW, FadeIn, FadeOut, Text, VGroup, Write

from shapes.base_scene import NotionScene
from shapes.boxes import definition_box, essentiel_box, method_box, scene_title


def _wrap(text: str, width: int = 56) -> str:
    return "\n".join(textwrap.fill(line, width=width) for line in text.split("\n"))


def _bullets(items, font_size=24, color=WHITE, width=54):
    lines = VGroup(
        *[Text(f"• {_wrap(it, width=width)}", font_size=font_size, color=color) for it in items]
    )
    lines.arrange(DOWN, aligned_edge=LEFT, buff=0.22)
    return lines


class IntroductionEchangesCationiquesSol(NotionScene):
    def construct(self):
        titre = scene_title("Chapitre 9 — Les échanges d'ions au niveau du sol")
        titre.scale(0.58)
        titre.to_edge(UP)

        # --- Énoncé : d'où viennent les éléments minéraux de la plante ? --
        intro = Text(
            _wrap(
                "Une plante puise dans le sol l'azote, le potassium, le "
                "calcium dont elle a besoin. Mais sous quelle forme "
                "exacte ces éléments existent-ils dans le sol, et comment "
                "la racine peut-elle les capter ?",
                width=56,
            ),
            font_size=26,
            color=WHITE,
        )
        intro.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Une plante puise dans le sol l'azote, le potassium, le "
                "calcium dont elle a besoin pour grandir. Mais sous quelle "
                "forme exacte ces éléments existent-ils dans le sol, et "
                "comment la racine peut-elle les capter ? C'est ce que "
                "nous allons comprendre dans ce chapitre sur les échanges "
                "d'ions au niveau du sol."
            )
        ) as tracker:
            self.play(Write(titre))
            self.play(FadeIn(intro))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(intro))

        # --- Raisonnement : qu'est-ce qu'un ion ? (cation / anion) --------
        def_ion = definition_box(
            Text(
                _wrap(
                    "Un ion est un atome (ou un groupe d'atomes) qui porte "
                    "une charge électrique par gain ou perte d'électrons. "
                    "Un cation est chargé positivement (perte "
                    "d'électrons). Un anion est chargé négativement (gain "
                    "d'électrons).",
                    width=54,
                ),
                font_size=22,
            ),
            box_width=11.8,
        )
        def_ion.next_to(titre, DOWN, buff=0.45)

        with self.voiceover(
            text=(
                "La matière est faite d'atomes. Un atome qui gagne ou "
                "perd un ou plusieurs électrons devient une particule "
                "chargée électriquement : un ion. Un cation est un ion "
                "chargé positivement, par perte d'électrons. Un anion est "
                "un ion chargé négativement, par gain d'électrons."
            )
        ) as tracker:
            self.play(FadeIn(def_ion))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(def_ion))

        exemples_titre = Text("Exemples d'ions du sol", font_size=27, color=YELLOW, weight="BOLD")
        exemples_titre.next_to(titre, DOWN, buff=0.5)

        cations_titre = Text("Cations (+)", font_size=23, color=YELLOW, weight="BOLD")
        cations = _bullets(
            [
                "Ca2+, Mg2+, K+, Na+",
                "H+, NH4+, Al3+",
            ],
            font_size=22,
            width=24,
        )
        colonne_cations = VGroup(cations_titre, cations).arrange(DOWN, aligned_edge=LEFT, buff=0.3)

        anions_titre = Text("Anions (-)", font_size=23, color=YELLOW, weight="BOLD")
        anions = _bullets(
            [
                "Cl-, NO3-",
                "SO4(2-), PO4(3-)",
            ],
            font_size=22,
            width=24,
        )
        colonne_anions = VGroup(anions_titre, anions).arrange(DOWN, aligned_edge=LEFT, buff=0.3)

        deux_colonnes = VGroup(colonne_cations, colonne_anions).arrange(RIGHT, buff=1.4, aligned_edge=UP)
        deux_colonnes.next_to(exemples_titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Le sol contient de nombreux exemples de ces deux "
                "familles. Côté cations, chargés positivement : calcium "
                "deux plus, magnésium deux plus, potassium plus, sodium "
                "plus, hydrogène plus, ammonium plus, aluminium trois "
                "plus. Côté anions, chargés négativement : chlorure, "
                "nitrate, sulfate, phosphate."
            )
        ) as tracker:
            self.play(FadeIn(exemples_titre))
            self.play(FadeIn(deux_colonnes))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(exemples_titre), FadeOut(deux_colonnes))

        # --- Origine des ions du sol + solution du sol ---------------------
        origine_titre = Text("D'où viennent ces ions ?", font_size=27, color=YELLOW, weight="BOLD")
        origine_titre.next_to(titre, DOWN, buff=0.5)

        origine = _bullets(
            [
                "L'altération des roches (libère Ca2+, Mg2+, K+, Na+...)",
                "La décomposition de la matière organique par les "
                "micro-organismes (libère NH4+, NO3-, PO4(3-)...)",
                "Les pluies, les engrais et les amendements apportés par "
                "l'agriculteur",
            ],
            font_size=22,
            width=52,
        )
        origine.next_to(origine_titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "L'eau du sol n'est jamais pure : elle forme une solution, "
                "appelée solution du sol, qui contient de nombreux ions "
                "dissous. Ces ions proviennent de trois sources "
                "principales. D'abord l'altération des roches, qui "
                "libère calcium, magnésium, potassium, sodium. Ensuite la "
                "décomposition de la matière organique par les "
                "micro-organismes, qui libère ammonium, nitrate, "
                "phosphate. Enfin les pluies, les engrais et les "
                "amendements apportés par l'agriculteur."
            )
        ) as tracker:
            self.play(FadeIn(origine_titre))
            self.play(FadeIn(origine))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(origine_titre), FadeOut(origine))

        methode = method_box(
            Text(
                _wrap(
                    "Point clé : les éléments nutritifs minéraux "
                    "indispensables aux plantes (azote, phosphore, "
                    "potassium, calcium, magnésium...) ne sont absorbés "
                    "par les racines que sous forme d'ions dissous dans "
                    "la solution du sol.",
                    width=54,
                ),
                font_size=22,
            ),
            box_width=11.8,
        )
        methode.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Retenez ce point clé : les éléments nutritifs minéraux "
                "indispensables aux plantes, azote, phosphore, potassium, "
                "calcium, magnésium, ne sont absorbés par les racines que "
                "sous forme d'ions dissous dans la solution du sol. C'est "
                "le fil conducteur de tout ce chapitre."
            )
        ) as tracker:
            self.play(FadeIn(methode))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(methode))

        # --- À retenir : objectifs du chapitre ------------------------------
        objectifs = essentiel_box(
            _bullets(
                [
                    "Décrire le complexe argilo-humique et l'origine de "
                    "ses charges négatives.",
                    "Expliquer l'adsorption et la désorption des ions "
                    "(échanges cationiques).",
                    "Calculer la CEC, la somme des bases échangeables et "
                    "le taux de saturation d'un sol.",
                    "Interpréter le pH d'un sol et ses effets sur la "
                    "disponibilité des éléments nutritifs.",
                    "Expliquer le lessivage et proposer des solutions "
                    "(engrais, chaulage, jachère) adaptées à la Côte "
                    "d'Ivoire.",
                ],
                font_size=20,
                width=54,
            ),
            box_width=12.4,
        )
        objectifs.next_to(titre, DOWN, buff=0.45)

        with self.voiceover(
            text=(
                "Voici les objectifs de ce chapitre. Décrire le complexe "
                "argilo-humique et expliquer l'origine de ses charges "
                "négatives. Expliquer l'adsorption et la désorption des "
                "ions, c'est-à-dire les échanges cationiques. Calculer la "
                "capacité d'échange cationique, la somme des bases "
                "échangeables et le taux de saturation d'un sol. "
                "Interpréter le pH d'un sol et ses effets sur la "
                "disponibilité des éléments nutritifs. Et enfin, "
                "expliquer le phénomène de lessivage et proposer des "
                "solutions, engrais, chaulage, jachère, adaptées aux "
                "problèmes de fatigue des sols en Côte d'Ivoire."
            )
        ) as tracker:
            self.play(FadeIn(objectifs))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(titre), FadeOut(objectifs))
