"""
scenes/SVT_EchangesCationiquesSol_02.py — Chapitre 9 (1ereC, SVT), scène 02.

Les colloïdes du sol : définition (particule fine < 2µm, grande surface,
charges négatives), les deux familles (colloïdes minéraux = argiles,
colloïdes organiques = humus) avec tableau origine/caractéristiques, et
remarque sur l'origine des charges négatives (défauts de structure
cristalline vs groupements -COOH / -OH). Source : 1ereC/SVT.pdf, page 97.
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


class ColloidesDuSol(NotionScene):
    def construct(self):
        titre = scene_title("9.1 — Les colloïdes du sol")
        titre.scale(0.68)
        titre.to_edge(UP)

        # --- Énoncé : le sol contient des particules très fines -----------
        intro = Text(
            _wrap(
                "Le sol est fait de sable, de limon, d'argile, de matière "
                "organique, d'eau, d'air et d'êtres vivants. Parmi ces "
                "constituants, les particules les plus fines jouent un "
                "rôle chimique capital : ce sont les colloïdes.",
                width=56,
            ),
            font_size=25,
            color=WHITE,
        )
        intro.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Le sol est constitué de particules minérales, sable, "
                "limon, argile, de matière organique, d'eau, d'air et "
                "d'êtres vivants. Parmi tous ces constituants, les "
                "particules les plus fines jouent un rôle chimique "
                "capital : ce sont les colloïdes."
            )
        ) as tracker:
            self.play(Write(titre))
            self.play(FadeIn(intro))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(intro))

        # --- Raisonnement : définition du colloïde --------------------------
        def_colloide = definition_box(
            Text(
                _wrap(
                    "Un colloïde est une particule extrêmement fine "
                    "(dimension inférieure à 2µm), qui possède une très "
                    "grande surface de contact par rapport à son volume, "
                    "et qui porte des charges électriques à sa surface, "
                    "le plus souvent négatives.",
                    width=54,
                ),
                font_size=22,
            ),
            box_width=11.8,
        )
        def_colloide.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Un colloïde est une particule extrêmement fine, de "
                "dimension inférieure à deux micromètres, qui possède une "
                "très grande surface de contact par rapport à son volume, "
                "et qui porte des charges électriques à sa surface, le "
                "plus souvent négatives. Plus une particule est petite, "
                "plus sa surface est grande par rapport à sa masse : "
                "c'est cette immense surface chargée qui va jouer le rôle "
                "principal dans la rétention des ions."
            )
        ) as tracker:
            self.play(FadeIn(def_colloide))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(def_colloide))

        # --- Tableau : deux familles de colloïdes --------------------------
        tab_titre = Text("Deux familles de colloïdes du sol", font_size=25, color=YELLOW, weight="BOLD")
        tab_titre.next_to(titre, DOWN, buff=0.45)

        col_min_titre = Text("Colloïdes minéraux", font_size=21, color=YELLOW, weight="BOLD")
        col_min = _bullets(
            [
                "Origine : altération des roches",
                "Ce sont les argiles (kaolinite, illite, "
                "montmorillonite...)",
                "Charges négatives en surface",
            ],
            font_size=18,
            width=28,
        )
        colonne_min = VGroup(col_min_titre, col_min).arrange(DOWN, aligned_edge=LEFT, buff=0.3)

        col_org_titre = Text("Colloïdes organiques", font_size=21, color=YELLOW, weight="BOLD")
        col_org = _bullets(
            [
                "Origine : décomposition des végétaux et animaux morts",
                "C'est l'humus",
                "Charges négatives, en plus grand nombre que les "
                "argiles",
            ],
            font_size=18,
            width=28,
        )
        colonne_org = VGroup(col_org_titre, col_org).arrange(DOWN, aligned_edge=LEFT, buff=0.3)

        tableau = VGroup(colonne_min, colonne_org).arrange(RIGHT, buff=1.0, aligned_edge=UP)
        tableau.next_to(tab_titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Le sol contient deux grandes familles de colloïdes. "
                "Les colloïdes minéraux proviennent de l'altération des "
                "roches : ce sont les argiles, comme la kaolinite, "
                "l'illite ou la montmorillonite. Leur surface porte des "
                "charges négatives. Les colloïdes organiques proviennent "
                "de la décomposition des végétaux et des animaux morts : "
                "c'est l'humus. Il porte lui aussi des charges négatives, "
                "et même en plus grand nombre que les argiles."
            )
        ) as tracker:
            self.play(FadeIn(tab_titre))
            self.play(FadeIn(tableau))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(tab_titre), FadeOut(tableau))

        # --- À retenir / remarque : origine des charges négatives ----------
        remarque = warning_box(
            Text(
                _wrap(
                    "Les charges négatives des argiles proviennent de "
                    "défauts dans leur structure cristalline "
                    "(substitution d'atomes). Celles de l'humus "
                    "proviennent de groupements chimiques acides "
                    "(-COOH et -OH) qui perdent un ion H+.",
                    width=54,
                ),
                font_size=22,
            ),
            box_width=11.8,
        )
        remarque.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Remarque importante : ces charges négatives n'ont pas "
                "toutes la même origine. Celles des argiles proviennent "
                "de défauts dans leur structure cristalline, c'est-à-dire "
                "de substitutions d'atomes à l'intérieur du minéral. "
                "Celles de l'humus proviennent de groupements chimiques "
                "acides, notés moins C-O-O-H et moins O-H, qui perdent "
                "chacun un ion hydrogène. Deux origines différentes, un "
                "même résultat : une surface chargée négativement, prête "
                "à attirer les cations."
            )
        ) as tracker:
            self.play(FadeIn(remarque))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(titre), FadeOut(remarque))
