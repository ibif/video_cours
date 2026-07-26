"""
scenes/Chimie_EsterificationHydrolyse_08.py — Chapitre 8 « Estérification et
hydrolyse d'un ester » (1ereC, Chimie), scène 08.

§ Comment augmenter le rendement ? Excès d'un réactif. theorem_box loi de
déplacement d'équilibre qualitative. Tableau résultats expérimentaux
(1mol acide+1mol alcool→67% ; +2mol alcool→85% ; +5mol alcool→94%).
method_box choix économique (excès du réactif le moins coûteux).
Source : 1ereC/Chimie.pdf, chapitre 8, pages 80-81.
"""

import textwrap

from manim import (
    DOWN,
    UP,
    WHITE,
    YELLOW,
    FadeIn,
    FadeOut,
    Table,
    Text,
    VGroup,
    Write,
    config,
)

from shapes.base_scene import NotionScene
from shapes.boxes import method_box, scene_title, theorem_box


def _wrap(text: str, width: int = 56) -> str:
    return "\n".join(textwrap.fill(line, width=width) for line in text.split("\n"))


def _fit(mobject, top_y):
    bas_visible = -config.frame_height / 2 + 0.25
    hauteur_dispo = top_y - bas_visible
    if mobject.height > hauteur_dispo:
        mobject.scale(hauteur_dispo / mobject.height, about_point=mobject.get_top())
    return mobject


class AugmenterRendementExcesReactif(NotionScene):
    def construct(self):
        titre = scene_title("8. Augmenter le rendement : l'excès d'un réactif")
        titre.scale(0.46)
        titre.to_edge(UP)

        # --- Énoncé -----------------------------------------------------------
        enonce = Text(
            _wrap(
                "Un rendement de 67 % ne satisfait pas toujours "
                "l'industriel ou le chimiste : peut-on faire mieux, sans "
                "toucher à la nature de l'acide ni de l'alcool utilisés ?",
                width=54,
            ),
            font_size=24,
            color=WHITE,
        )
        enonce.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Un rendement de soixante-sept pour cent ne satisfait pas "
                "toujours l'industriel ou le chimiste. Peut-on faire "
                "mieux, sans toucher à la nature de l'acide ni de "
                "l'alcool utilisés ? Il existe en réalité deux leviers, "
                "que nous découvrons dans cette scène et la suivante."
            )
        ) as tracker:
            self.play(Write(titre))
            self.play(FadeIn(enonce))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(enonce))

        # --- Raisonnement : theorem_box loi de déplacement d'équilibre --------------
        theoreme = theorem_box(
            Text(
                _wrap(
                    "Loi de déplacement d'équilibre (qualitative) : si l'on "
                    "augmente la quantité d'un des réactifs, l'équilibre se "
                    "déplace dans le sens qui en consomme une partie — ici "
                    "le sens direct — ce qui augmente la quantité d'ester "
                    "formé.",
                    width=48,
                ),
                font_size=22,
            ),
        )
        theoreme.next_to(titre, DOWN, buff=0.4)
        _fit(theoreme, titre.get_bottom()[1] - 0.4)

        with self.voiceover(
            text=(
                "Le premier levier repose sur une loi qualitative de "
                "déplacement d'équilibre : si l'on augmente la quantité "
                "d'un des réactifs, l'équilibre se déplace dans le sens "
                "qui consomme une partie de cet excès — ici, le sens "
                "direct, celui de l'estérification. Le taux d'avancement "
                "du réactif limitant augmente alors."
            )
        ) as tracker:
            self.play(FadeIn(theoreme))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(theoreme))

        # --- Exemple traité : tableau de résultats expérimentaux --------------------
        entete_tab = Text("Résultats expérimentaux (excès d'alcool)", font_size=22, color=YELLOW, weight="BOLD")
        entete_tab.next_to(titre, DOWN, buff=0.35)

        rows = [
            ["1 mol acide + 1 mol alcool", "67 %"],
            ["1 mol acide + 2 mol alcool", "85 %"],
            ["1 mol acide + 5 mol alcool", "94 %"],
        ]
        table = Table(
            rows,
            col_labels=[Text(c, font_size=18, weight="BOLD") for c in ["quantités initiales", "τ (rendement en ester)"]],
            element_to_mobject=Text,
            element_to_mobject_config={"font_size": 18},
            line_config={"color": WHITE, "stroke_width": 1},
            include_outer_lines=True,
            v_buff=0.25,
            h_buff=0.35,
        )
        table.get_entries().set_color(WHITE)
        table.get_col_labels().set_color(YELLOW)
        for line in table.get_horizontal_lines():
            line.set_color(WHITE)
        for line in table.get_vertical_lines():
            line.set_color(WHITE)
        table.next_to(entete_tab, DOWN, buff=0.3)

        groupe = VGroup(entete_tab, table)
        _fit(groupe, titre.get_bottom()[1] - 0.35)

        with self.voiceover(
            text=(
                "Voici des résultats expérimentaux typiques, en gardant "
                "toujours une mole d'acide et en faisant varier la "
                "quantité d'alcool introduite. Avec une mole d'alcool, "
                "un mélange équimolaire, le rendement vaut soixante-sept "
                "pour cent. Avec deux moles d'alcool, il grimpe à "
                "quatre-vingt-cinq pour cent. Et avec cinq moles "
                "d'alcool, il atteint quatre-vingt-quatorze pour cent : "
                "plus l'excès est grand, plus le rendement en acide "
                "s'améliore, mais avec un effet de moins en moins "
                "marginal."
            )
        ) as tracker:
            self.play(FadeIn(entete_tab))
            self.play(FadeIn(table))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(groupe))

        # --- À retenir : method_box choix économique ---------------------------------
        methode = method_box(
            Text(
                _wrap(
                    "En pratique, on choisit d'introduire en excès le "
                    "réactif le MOINS COÛTEUX (souvent l'alcool), et l'on "
                    "récupère le produit à partir du réactif le plus "
                    "précieux (souvent l'acide) : c'est un compromis "
                    "économique, pas seulement chimique.",
                    width=48,
                ),
                font_size=22,
            ),
        )
        methode.next_to(titre, DOWN, buff=0.4)
        _fit(methode, titre.get_bottom()[1] - 0.4)

        with self.voiceover(
            text=(
                "Retenons cette méthode : en pratique industrielle, on "
                "choisit d'introduire en excès le réactif le moins "
                "coûteux, souvent l'alcool, et l'on calcule le rendement "
                "par rapport au réactif le plus précieux, souvent "
                "l'acide. C'est donc un compromis économique autant que "
                "chimique, qui guide le choix du réactif mis en excès."
            )
        ) as tracker:
            self.play(FadeIn(methode))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(methode), FadeOut(titre))
