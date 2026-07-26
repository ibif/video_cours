"""
scenes/Chimie_Alcanes_14.py — Chapitre 2 « Hydrocarbures saturés — les
alcanes » (1ereC, Chimie), scène 14 (clôture du chapitre).

Méthodes et astuces : les 4 méthodes (nommer un alcane ramifié, trouver
tous les isomères de chaîne, déterminer une formule brute par combustion,
exploiter la densité d'un gaz par rapport à l'air) + les 4 pièges à
éviter, puis L'ESSENTIEL DU CHAPITRE (essentiel_box).
Source : 1ereC/Chimie.pdf, page 24.
"""

import textwrap

from manim import (
    DOWN,
    LEFT,
    RIGHT,
    UP,
    WHITE,
    YELLOW,
    FadeIn,
    FadeOut,
    MathTex,
    Text,
    VGroup,
    Write,
    config,
)

from shapes.base_scene import NotionScene
from shapes.boxes import essentiel_box, method_box, scene_title, warning_box


def _wrap(text: str, width: int = 56) -> str:
    return "\n".join(textwrap.fill(line, width=width) for line in text.split("\n"))


def _bullets(items, font_size=20, color=WHITE, width=54):
    lines = VGroup(
        *[Text(f"• {_wrap(it, width=width)}", font_size=font_size, color=color) for it in items]
    )
    lines.arrange(DOWN, aligned_edge=LEFT, buff=0.2)
    return lines


def _fit(mobject, top_y):
    bas_visible = -config.frame_height / 2 + 0.25
    hauteur_dispo = top_y - bas_visible
    if mobject.height > hauteur_dispo:
        mobject.scale(hauteur_dispo / mobject.height, about_point=mobject.get_top())
    return mobject


class MethodesPiegesEssentiel(NotionScene):
    def construct(self):
        titre = scene_title("Méthodes, pièges et l'essentiel du chapitre")
        titre.scale(0.6)
        titre.to_edge(UP)

        # --- Énoncé : avant de clore le chapitre ----------------------------------
        intro = Text(
            _wrap(
                "Avant de clore ce chapitre, récapitulons les méthodes "
                "clés pour résoudre les exercices, les pièges à éviter, "
                "puis l'essentiel à retenir.",
                width=54,
            ),
            font_size=24,
            color=WHITE,
        )
        intro.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Avant de clore ce chapitre, récapitulons les méthodes "
                "clés pour résoudre les exercices, les pièges à éviter, "
                "puis l'essentiel à retenir."
            )
        ) as tracker:
            self.play(Write(titre))
            self.play(FadeIn(intro))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(intro))

        # --- Raisonnement : méthodes 1 et 2 --------------------------------------
        methode12 = method_box(
            VGroup(
                Text(
                    _wrap(
                        "Nommer un alcane ramifié (4 étapes) : repérer la "
                        "chaîne la plus longue (elle peut « tourner » dans "
                        "le dessin) → numéroter dans le sens des plus "
                        "petits indices → citer les substituants par "
                        "ordre alphabétique → terminer par la chaîne "
                        "principale.",
                        width=50,
                    ),
                    font_size=19,
                ),
                Text(
                    _wrap(
                        "Trouver tous les isomères de chaîne : partir de "
                        "la chaîne linéaire, la raccourcir d'un carbone en "
                        "déplaçant un méthyle (jamais sur une extrémité), "
                        "explorer toutes les positions, puis nommer "
                        "chaque squelette pour éliminer les doublons.",
                        width=50,
                    ),
                    font_size=19,
                ),
            ).arrange(DOWN, buff=0.35),
            box_width=11.8,
        )
        methode12.next_to(titre, DOWN, buff=0.4)
        _fit(methode12, titre.get_bottom()[1] - 0.4)

        with self.voiceover(
            text=(
                "Première méthode : pour nommer un alcane ramifié en "
                "quatre étapes, repérez la chaîne la plus longue, qui "
                "peut très bien tourner dans le dessin ; numérotez-la "
                "dans le sens qui donne les plus petits indices ; citez "
                "les substituants par ordre alphabétique ; puis terminez "
                "par le nom de la chaîne principale. Deuxième méthode : "
                "pour trouver tous les isomères de chaîne, partez de la "
                "chaîne linéaire, raccourcissez-la d'un carbone en "
                "déplaçant un méthyle, jamais sur une extrémité, "
                "explorez toutes les positions possibles, puis nommez "
                "chaque squelette obtenu pour éliminer les doublons."
            )
        ) as tracker:
            self.play(FadeIn(methode12))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(methode12))

        # --- Exemple traité : méthodes 3 et 4 -------------------------------------
        methode34 = method_box(
            VGroup(
                Text(
                    _wrap(
                        "Déterminer une formule brute par combustion : "
                        "écrire l'équation-bilan générale → calculer "
                        "n(CO₂) et n(H₂O) → résoudre n via n(CO₂)/n(alcane) "
                        "ou n(H₂O)/n(CO₂)=(n+1)/n → vérifier avec "
                        "M=14n+2.",
                        width=50,
                    ),
                    font_size=19,
                ),
                MathTex(
                    r"\text{Densité d'un gaz / air : } d = \dfrac{M}{29} \;\Rightarrow\; M = 29d \;\Rightarrow\; 14n+2=M",
                    font_size=19,
                    color=WHITE,
                ),
            ).arrange(DOWN, buff=0.35),
            box_width=11.8,
        )
        methode34.next_to(titre, DOWN, buff=0.4)
        _fit(methode34, titre.get_bottom()[1] - 0.4)

        with self.voiceover(
            text=(
                "Troisième méthode : pour déterminer une formule brute "
                "par combustion, écrivez l'équation-bilan générale, "
                "calculez les quantités de matière de dioxyde de carbone "
                "et d'eau, puis résolvez n grâce au rapport n de C-O-2 "
                "sur n de l'alcane, et vérifiez avec la masse molaire M "
                "égale quatorze n plus deux. Quatrième méthode : pour "
                "exploiter la densité d'un gaz par rapport à l'air, "
                "utilisez d égale M sur vingt-neuf ; connaissant d, on "
                "calcule M égale vingt-neuf d, puis on résout quatorze n "
                "plus deux égale M pour trouver n."
            )
        ) as tracker:
            self.play(FadeIn(methode34))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(methode34))

        # --- Pièges à éviter : les 4 pièges classiques du chapitre --------------
        entete_pieges = Text("Les 4 pièges classiques du chapitre", font_size=22, color=YELLOW, weight="BOLD")
        entete_pieges.next_to(titre, DOWN, buff=0.35)

        pieges = warning_box(
            _bullets(
                [
                    "La chaîne la plus longue n'est pas forcément celle "
                    "écrite à l'horizontale : elle peut monter ou "
                    "descendre dans la formule.",
                    "Le coefficient (3n+1)/2 de la combustion peut être "
                    "fractionnaire : ce n'est pas une erreur.",
                    "Combustion complète (CO₂ + H₂O seulement) et "
                    "incomplète (+ CO et/ou C) ont des produits "
                    "différents : ne pas les mélanger.",
                    "La substitution donne du HCl (pas Cl₂) : il faut "
                    "autant de Cl₂ que d'atomes H remplacés.",
                ],
                font_size=19,
                width=56,
            ),
            box_width=11.8,
        )
        pieges.next_to(entete_pieges, DOWN, buff=0.35)
        _fit(VGroup(entete_pieges, pieges), entete_pieges.get_bottom()[1] - 0.35)

        with self.voiceover(
            text=(
                "Voici les quatre pièges classiques du chapitre. Un : la "
                "chaîne la plus longue n'est pas forcément celle écrite à "
                "l'horizontale, elle peut monter ou descendre dans la "
                "formule. Deux : le coefficient trois n plus un sur deux "
                "de la combustion peut être fractionnaire, ce n'est pas "
                "une erreur. Trois : la combustion complète et la "
                "combustion incomplète n'ont pas les mêmes produits, ne "
                "les mélangez pas. Quatre : la substitution donne du "
                "chlorure d'hydrogène, et non du dichlore, comme "
                "sous-produit, et il faut autant de molécules de "
                "dichlore que d'atomes d'hydrogène remplacés."
            )
        ) as tracker:
            self.play(FadeIn(entete_pieges))
            self.play(FadeIn(pieges))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(entete_pieges), FadeOut(pieges))

        # --- À retenir : L'ESSENTIEL DU CHAPITRE (clôture) -----------------------
        essentiel = essentiel_box(
            _bullets(
                [
                    "Alcane = hydrocarbure saturé, formule CₙH₂ₙ₊₂ "
                    "(n≥1) ; cyclane = CₙH₂ₙ (n≥3), formules distinctes.",
                    "Nomenclature UICPA : chaîne principale la plus "
                    "longue + numérotation aux plus petits indices + "
                    "substituants par ordre alphabétique.",
                    "Isomères de chaîne : même formule brute, "
                    "squelettes différents, propriétés physiques "
                    "différentes.",
                    "État physique et Téb croissent avec n ; à formule "
                    "égale, plus la chaîne est ramifiée, plus Téb est "
                    "bas.",
                    "Alcanes peu réactifs (« paraffines ») : deux "
                    "réactions clés, combustion (complète : CO₂+H₂O ; "
                    "incomplète : + CO/C, danger du CO) et substitution "
                    "radicalaire (initiation / propagation / "
                    "terminaison).",
                    "Usages : combustibles (gaz, essence, gas-oil), "
                    "solvants, matières premières, paraffines/cires.",
                ],
                font_size=18,
                width=56,
            ),
            box_width=12.6,
        )
        essentiel.next_to(titre, DOWN, buff=0.35)

        _bas_visible = -config.frame_height / 2 + 0.3
        _hauteur_dispo = essentiel.get_top()[1] - _bas_visible
        if essentiel.height > _hauteur_dispo:
            essentiel.scale(_hauteur_dispo / essentiel.height, about_point=essentiel.get_top())

        with self.voiceover(
            text=(
                "Voici l'essentiel du chapitre. Un alcane est un "
                "hydrocarbure saturé, de formule C indice n, H indice "
                "deux n plus deux, avec n supérieur ou égal à un ; un "
                "cyclane est C indice n, H indice deux n, avec n "
                "supérieur ou égal à trois — deux formules bien "
                "distinctes. La nomenclature de l'UICPA repose sur la "
                "chaîne principale la plus longue, numérotée pour donner "
                "les plus petits indices, avec les substituants cités par "
                "ordre alphabétique. Les isomères de chaîne partagent la "
                "même formule brute mais ont des squelettes et des "
                "propriétés physiques différents. L'état physique et le "
                "point d'ébullition croissent avec le nombre de carbones "
                "n ; à formule égale, plus la chaîne est ramifiée, plus "
                "le point d'ébullition est bas. Les alcanes sont peu "
                "réactifs, on les appelle des paraffines, et connaissent "
                "deux réactions clés : la combustion, complète ou "
                "incomplète, avec le danger du monoxyde de carbone en cas "
                "de défaut de dioxygène, et la substitution radicalaire, "
                "en trois phases, initiation, propagation, terminaison. "
                "Enfin, les alcanes servent de combustibles, de solvants, "
                "de matières premières et de paraffines. Voilà, vous "
                "maîtrisez maintenant les alcanes, des hydrocarbures "
                "essentiels à l'industrie et à la vie quotidienne "
                "ivoirienne."
            )
        ) as tracker:
            self.play(FadeIn(essentiel))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(titre), FadeOut(essentiel))
