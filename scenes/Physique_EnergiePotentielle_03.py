"""
scenes/Physique_EnergiePotentielle_03.py — Chapitre 4 « Énergie potentielle »
(1ereC, Physique), scène 03.

Définition et expression de l'énergie potentielle de pesanteur :
Epp = mgz + Cte, convention de référence (z₀ où Epp=0, simplification
Epp=mgz si l'origine est prise au niveau de référence), remarques (signe
selon la position par rapport à la référence, grandeur scalaire en joules,
choix arbitraire de la référence).
Source : 1ereC/Physique.pdf, chapitre 4, pages 34-42.
"""

import textwrap

from manim import (
    DOWN,
    GREEN,
    LEFT,
    PI,
    RED,
    RIGHT,
    UP,
    WHITE,
    YELLOW,
    Dot,
    DashedLine,
    FadeIn,
    FadeOut,
    MathTex,
    NumberLine,
    Text,
    VGroup,
    Write,
)

from shapes.base_scene import NotionScene
from shapes.boxes import definition_box, essentiel_box, scene_title, warning_box


def _wrap(text: str, width: int = 56) -> str:
    return "\n".join(textwrap.fill(line, width=width) for line in text.split("\n"))


class DefinitionExpressionEpp(NotionScene):
    def construct(self):
        titre = scene_title("Définition et expression de Epp")
        titre.scale(0.55)
        titre.to_edge(UP)

        # --- Définition ------------------------------------------------------------
        definition = definition_box(
            VGroup(
                Text(
                    "Pour un système de masse m, à l'altitude z sur un axe "
                    "vertical ascendant :",
                    font_size=23,
                ),
                MathTex(r"E_{pp} = mgz + \text{Cte}", font_size=34),
            ).arrange(DOWN, buff=0.3),
            box_width=10.8,
        )
        definition.next_to(titre, DOWN, buff=0.6)

        with self.voiceover(
            text=(
                "Voici la définition générale de l'énergie potentielle de "
                "pesanteur. Pour un système de masse m situé à l'altitude z "
                "sur un axe vertical orienté vers le haut, l'énergie "
                "potentielle de pesanteur Epp vaut m g z, plus une "
                "constante."
            )
        ) as tracker:
            self.play(FadeIn(definition))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(definition))

        # --- Raisonnement : convention de référence ---------------------------------
        axe = NumberLine(x_range=[0, 6, 1], length=4.4, include_numbers=False, color=WHITE)
        axe.rotate(PI / 2)
        axe.move_to(LEFT * 3.4)
        label_z = MathTex("z", font_size=30).next_to(axe, UP, buff=0.15)

        niveau_ref = axe.n2p(1.2)
        ligne_ref = DashedLine(niveau_ref + LEFT * 0.6, niveau_ref + RIGHT * 2.2, color=YELLOW)
        label_ref = MathTex(r"z_0 \; (E_{pp}=0)", font_size=24, color=YELLOW)
        label_ref.next_to(ligne_ref, RIGHT, buff=0.15)

        schema = VGroup(axe, label_z, ligne_ref, label_ref)
        schema.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Comme toute énergie potentielle, Epp est définie à une "
                "constante près. On choisit donc un niveau de référence, "
                "d'altitude z indice zéro, pour lequel on décide que "
                "l'énergie potentielle de pesanteur est nulle."
            )
        ) as tracker:
            self.play(Write(axe), Write(label_z))
            self.play(Write(ligne_ref), Write(label_ref))
            self.wait(tracker.get_remaining_duration())

        simplification = MathTex(
            r"\text{Si } z_0 = 0 \; : \quad E_{pp} = mgz",
            font_size=30,
        )
        simplification.next_to(schema, RIGHT, buff=0.8)

        with self.voiceover(
            text=(
                "En pratique, on prend très souvent l'origine de l'axe "
                "exactement au niveau de cette référence : z indice zéro "
                "vaut alors zéro, et l'expression se simplifie : l'énergie "
                "potentielle de pesanteur devient simplement m g z, sans "
                "constante additionnelle."
            )
        ) as tracker:
            self.play(Write(simplification))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(schema), FadeOut(simplification))

        # --- Remarques : signe et choix de la référence --------------------------
        point_haut = Dot(color=GREEN)
        point_bas = Dot(color=RED)

        axe2 = NumberLine(x_range=[0, 6, 1], length=4.0, include_numbers=False, color=WHITE)
        axe2.rotate(PI / 2)
        axe2.move_to(LEFT * 4.0 + DOWN * 0.3)
        niveau_ref2 = axe2.n2p(2.5)
        ligne_ref2 = DashedLine(niveau_ref2 + LEFT * 0.5, niveau_ref2 + RIGHT * 2.4, color=YELLOW)

        point_haut.move_to(axe2.n2p(4.3))
        point_bas.move_to(axe2.n2p(0.8))
        label_haut = MathTex(r"E_{pp} > 0", font_size=24, color=GREEN).next_to(point_haut, RIGHT, buff=0.2)
        label_bas = MathTex(r"E_{pp} < 0", font_size=24, color=RED).next_to(point_bas, RIGHT, buff=0.2)

        schema2 = VGroup(axe2, ligne_ref2, point_haut, point_bas, label_haut, label_bas)
        schema2.next_to(titre, DOWN, buff=0.5).shift(LEFT * 0.3)

        remarque = warning_box(
            Text(
                _wrap(
                    "Au-dessus de la référence, Epp > 0 ; en-dessous, "
                    "Epp < 0 : ce n'est pas une erreur, seule la position "
                    "par rapport à la référence choisie compte. Epp est "
                    "une grandeur scalaire, exprimée en joules (J).",
                    width=42,
                ),
                font_size=21,
            ),
            box_width=6.6,
        )
        remarque.next_to(schema2, RIGHT, buff=0.5)

        with self.voiceover(
            text=(
                "Une conséquence importante : au-dessus du niveau de "
                "référence, l'énergie potentielle de pesanteur est "
                "positive. En-dessous, elle est négative. Ce n'est "
                "absolument pas une erreur de calcul : c'est seulement la "
                "position par rapport à la référence choisie qui compte. "
                "Epp est une grandeur scalaire, comme toute énergie, et "
                "s'exprime en joules."
            )
        ) as tracker:
            self.play(FadeIn(schema2))
            self.play(FadeIn(remarque))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(schema2), FadeOut(remarque))

        # --- Choix de la référence ---------------------------------------------------
        choix = Text(
            _wrap(
                "Le choix de la référence est arbitraire : on le fait "
                "toujours pour simplifier les calculs (ex : le sol, la "
                "table, le point de départ...).",
                width=52,
            ),
            font_size=25,
        )
        choix.next_to(titre, DOWN, buff=0.8)

        with self.voiceover(
            text=(
                "Le choix de la référence est arbitraire : rien ne l'impose "
                "physiquement. On le fait toujours dans le but de "
                "simplifier les calculs. On prendra par exemple le sol, la "
                "surface d'une table, ou encore le point de départ du "
                "mouvement étudié."
            )
        ) as tracker:
            self.play(Write(choix))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(choix))

        # --- À retenir -----------------------------------------------------------------
        retenir = essentiel_box(
            Text(
                _wrap(
                    "Epp = mgz + Cte, ou Epp = mgz si l'origine est au "
                    "niveau de référence choisi (Epp=0). Grandeur scalaire "
                    "en joules, positive au-dessus, négative en-dessous de "
                    "la référence. Référence choisie librement.",
                    width=56,
                ),
                font_size=22,
            )
        )
        retenir.next_to(titre, DOWN, buff=0.6)

        with self.voiceover(
            text=(
                "À retenir : Epp égale m g z plus une constante, ou "
                "simplement m g z si l'origine de l'axe coïncide avec le "
                "niveau de référence choisi. C'est une grandeur scalaire, "
                "exprimée en joules, positive au-dessus et négative "
                "en-dessous de la référence, laquelle est choisie "
                "librement pour simplifier les calculs."
            )
        ) as tracker:
            self.play(FadeIn(retenir))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(titre), FadeOut(retenir))
