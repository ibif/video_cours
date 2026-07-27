"""
scenes/Maths_ComposeesTransformationsPlan_03.py — Chapitre 8 « Composées de
transformations du plan » (1ereC, Maths), scène 03.

§ Déplacements / antidéplacements, tableau de classification des
transformations usuelles, règle de composition (parité), tableau
récapitulatif des images de figures usuelles.
Source : 1ereC/Maths.pdf, chapitre 8, pages 95-96.
"""

import textwrap

from manim import DOWN, UP, WHITE, FadeIn, FadeOut, MathTex, Text, VGroup, Write

from shapes.base_scene import NotionScene
from shapes.boxes import definition_box, scene_title, theorem_box


def _wrap(text: str, width: int = 58) -> str:
    return "\n".join(textwrap.fill(line, width=width) for line in text.split("\n"))


def _cell(text_str: str, font_size: int = 22, bold: bool = False):
    return Text(text_str, font_size=font_size, weight="BOLD" if bold else "NORMAL", color=WHITE)


class DeplacementsAntideplacementsTableau(NotionScene):
    def construct(self):
        titre = scene_title("Déplacements, antidéplacements — tableau")
        titre.scale(0.46)
        titre.to_edge(UP)
        self.play(Write(titre))

        # --- Énoncé : définitions ---------------------------------------------
        def_dep = definition_box(
            VGroup(
                Text("Déplacement / antidéplacement", font_size=24, weight="BOLD"),
                Text(
                    _wrap("Un déplacement est une isométrie qui conserve les angles orientés (isométrie directe)."),
                    font_size=22,
                ),
                Text(
                    _wrap("Un antidéplacement est une isométrie qui inverse les angles orientés (isométrie indirecte)."),
                    font_size=22,
                ),
            ).arrange(DOWN, buff=0.25)
        )
        def_dep.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Toutes les transformations usuelles conservent les "
                "distances : ce sont des isométries. Mais on les classe en "
                "deux familles. Un déplacement, ou isométrie directe, "
                "conserve les angles orientés. Un antidéplacement, ou "
                "isométrie indirecte, les inverse. Cette distinction va "
                "être essentielle pour prévoir la nature d'une composée."
            )
        ) as tracker:
            self.play(FadeIn(def_dep))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(def_dep))

        # --- Raisonnement : tableau de classification --------------------------
        headers1 = [_cell("Transformation", bold=True), _cell("Type", bold=True)]
        rows1 = [
            ("Translation", "Déplacement"),
            ("Symétrie centrale", "Déplacement"),
            ("Rotation", "Déplacement"),
            ("Symétrie axiale", "Antidéplacement"),
            ("Identité", "Déplacement"),
        ]
        cells1 = list(headers1)
        for name, kind in rows1:
            cells1.append(_cell(name, font_size=21))
            cells1.append(_cell(kind, font_size=21))
        tableau1 = VGroup(*cells1).arrange_in_grid(rows=6, cols=2, buff=(0.6, 0.22), col_alignments="lc")
        tableau1.scale(0.85)
        tableau1.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Récapitulons la classification des transformations "
                "usuelles. Translation, symétrie centrale, rotation et "
                "identité sont des déplacements. La symétrie axiale, "
                "seule, est un antidéplacement."
            )
        ) as tracker:
            self.play(FadeIn(tableau1))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(tableau1))

        regle = theorem_box(
            VGroup(
                Text("Règle de composition (parité)", font_size=24, weight="BOLD"),
                MathTex(r"\text{d\'eplacement} \circ \text{d\'eplacement} = \text{d\'eplacement}", font_size=25),
                MathTex(r"\text{antid\'eplacement} \circ \text{antid\'eplacement} = \text{d\'eplacement}", font_size=25),
                MathTex(r"\text{d\'eplacement} \circ \text{antid\'eplacement} = \text{antid\'eplacement}", font_size=25),
            ).arrange(DOWN, buff=0.25)
        )
        regle.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "La composition suit une règle de parité, exactement comme "
                "le signe d'un produit : composer deux déplacements donne "
                "un déplacement ; composer deux antidéplacements donne "
                "aussi un déplacement, car les deux inversions d'angles se "
                "compensent ; et composer un déplacement avec un "
                "antidéplacement, dans un sens ou dans l'autre, donne un "
                "antidéplacement. Cette règle nous servira dans tout le "
                "chapitre pour anticiper la nature d'une composée avant "
                "même de calculer."
            )
        ) as tracker:
            self.play(FadeIn(regle))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(regle))

        # --- Exemple : tableau des images de figures usuelles -------------------
        headers2 = [_cell("Figure", bold=True), _cell("Isométrie", bold=True), _cell("Homothétie (k)", bold=True)]
        rows2 = [
            ("Droite", "Droite", "Droite parallèle"),
            ("Segment [AB]", "Longueur AB", "Longueur |k|·AB"),
            ("Cercle (r)", "Rayon r", "Rayon |k|·r"),
            ("Angle", "Même mesure*", "Même mesure"),
            ("Aire", "Conservée", "Aire × k²"),
        ]
        cells2 = list(headers2)
        for a, b, c in rows2:
            cells2.append(_cell(a, font_size=19))
            cells2.append(_cell(b, font_size=19))
            cells2.append(_cell(c, font_size=19))
        tableau2 = VGroup(*cells2).arrange_in_grid(rows=6, cols=3, buff=(0.5, 0.2), col_alignments="lcc")
        tableau2.scale(0.75)
        tableau2.next_to(titre, DOWN, buff=0.35)
        note = Text(
            _wrap("* mesure conservée par un déplacement, opposée par un antidéplacement.", width=60),
            font_size=18,
        )
        note.next_to(tableau2, DOWN, buff=0.3)

        with self.voiceover(
            text=(
                "Voici le tableau récapitulatif à connaître : par une "
                "isométrie, une droite reste une droite, un segment garde "
                "sa longueur, un cercle son rayon, un angle sa mesure — "
                "sauf pour un antidéplacement où la mesure orientée "
                "s'inverse — et une aire est conservée. Par une "
                "homothétie de rapport k, les longueurs sont multipliées "
                "par la valeur absolue de k, et les aires par k au carré, "
                "tandis que les angles restent identiques."
            )
        ) as tracker:
            self.play(FadeIn(tableau2), FadeIn(note))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(tableau2), FadeOut(note))

        # --- À retenir --------------------------------------------------------
        retenir = definition_box(
            VGroup(
                Text("À retenir", font_size=24, weight="BOLD"),
                Text(
                    _wrap("Isométries directes (déplacements) : translation, symétrie centrale, rotation."),
                    font_size=22,
                ),
                Text(_wrap("Isométrie indirecte (antidéplacement) : symétrie axiale."), font_size=22),
                Text(_wrap("La règle de parité de la composition anticipe la nature du résultat."), font_size=22),
            ).arrange(DOWN, buff=0.22)
        )
        retenir.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Retenons l'essentiel : translation, symétrie centrale et "
                "rotation sont des déplacements, la symétrie axiale est le "
                "seul antidéplacement parmi les transformations usuelles, "
                "et la règle de parité permet d'anticiper la nature de "
                "n'importe quelle composée."
            )
        ) as tracker:
            self.play(FadeIn(retenir))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(retenir), FadeOut(titre))
