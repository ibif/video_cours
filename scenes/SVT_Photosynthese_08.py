"""
scenes/SVT_Photosynthese_08.py — Chapitre 10 (1ereC, SVT), scène 08.

§ 10.4.1-10.4.2 (étape 1) La phase biochimique (phase sombre) — le cycle
de Calvin : conditions et lieu (pas besoin direct de lumière mais dépend
des produits de la phase claire, stroma, enzyme Rubisco) + Étape 1 :
fixation du CO2 (RuBP+CO2 --Rubisco--> 2 PGA, MathTex, schéma).
Source : 1ereC/SVT.pdf, pages 109-110.
"""

import textwrap

from manim import (
    DOWN,
    LEFT,
    RIGHT,
    UP,
    WHITE,
    YELLOW,
    Arrow,
    FadeIn,
    FadeOut,
    MathTex,
    RoundedRectangle,
    Text,
    VGroup,
    Write,
)

from shapes.base_scene import NotionScene
from shapes.boxes import definition_box, scene_title, warning_box


def _wrap(text: str, width: int = 56) -> str:
    return "\n".join(textwrap.fill(line, width=width) for line in text.split("\n"))


def _bullets(items, font_size=22, color=WHITE, width=52):
    lines = VGroup(
        *[Text(f"• {_wrap(it, width=width)}", font_size=font_size, color=color) for it in items]
    )
    lines.arrange(DOWN, aligned_edge=LEFT, buff=0.22)
    return lines


def _schema_fixation():
    """Schéma : RuBP (5C) + CO2 (1C), via Rubisco, donne 2 PGA (3C)."""
    rubp = RoundedRectangle(width=1.6, height=0.8, corner_radius=0.1, fill_color="#2E5B3A", fill_opacity=0.8, stroke_color="#3FCB63", stroke_width=1.5)
    label_rubp = Text("RuBP (5C)", font_size=15, color=WHITE).move_to(rubp.get_center())
    rubp_grp = VGroup(rubp, label_rubp)

    plus = Text("+", font_size=22, color=WHITE)

    co2 = RoundedRectangle(width=1.1, height=0.7, corner_radius=0.1, fill_color="#5AA9E6", fill_opacity=0.8, stroke_color="#2E6DA4", stroke_width=1.5)
    label_co2 = Text("CO2 (1C)", font_size=14, color=WHITE).move_to(co2.get_center())
    co2_grp = VGroup(co2, label_co2)

    gauche = VGroup(rubp_grp, plus, co2_grp).arrange(RIGHT, buff=0.35)

    fleche = Arrow(LEFT * 0.6, RIGHT * 0.6, color=YELLOW, buff=0)
    label_fleche = Text("Rubisco", font_size=15, color=YELLOW, weight="BOLD").next_to(fleche, UP, buff=0.1)
    fleche_grp = VGroup(fleche, label_fleche)

    pga1 = RoundedRectangle(width=1.3, height=0.7, corner_radius=0.1, fill_color="#DE7C1F", fill_opacity=0.8, stroke_color="#A65A12", stroke_width=1.5)
    label_pga1 = Text("PGA (3C)", font_size=14, color=WHITE).move_to(pga1.get_center())
    pga2 = pga1.copy()
    label_pga2 = Text("PGA (3C)", font_size=14, color=WHITE).move_to(pga2.get_center())
    droite = VGroup(VGroup(pga1, label_pga1), VGroup(pga2, label_pga2)).arrange(DOWN, buff=0.15)

    ligne = VGroup(gauche, fleche_grp, droite).arrange(RIGHT, buff=0.45)
    return ligne


class CycleDeCalvinFixationCO2(NotionScene):
    def construct(self):
        titre = scene_title("10.4.1-10.4.2 — Le cycle de Calvin : fixation du CO2")
        titre.scale(0.44)
        titre.to_edge(UP)

        # --- Énoncé : conditions et lieu de la phase biochimique -------------
        conditions = definition_box(
            _bullets(
                [
                    "N'exige pas directement la lumière (d'où le nom "
                    "de « phase sombre »), mais dépend des produits de "
                    "la phase claire (ATP, NADPH,H+).",
                    "Se déroule donc surtout le jour, en même temps que "
                    "la phase claire.",
                    "Se déroule dans le stroma du chloroplaste.",
                    "Est catalysée par des enzymes, dont la Rubisco, "
                    "l'enzyme la plus abondante du monde vivant.",
                ],
                font_size=19,
                width=52,
            ),
            box_width=12.2,
        )
        conditions.next_to(titre, DOWN, buff=0.45)

        with self.voiceover(
            text=(
                "Passons maintenant à la seconde grande phase de la "
                "photosynthèse : la phase biochimique, ou phase sombre. "
                "Elle n'exige pas directement la lumière, d'où son nom, "
                "mais elle dépend étroitement des produits de la phase "
                "claire, l'ATP et le NADPH,H plus. Elle se déroule donc "
                "surtout le jour, en même temps que la phase claire. "
                "Elle a lieu dans le stroma du chloroplaste, et elle est "
                "catalysée par des enzymes, dont la Rubisco, l'enzyme la "
                "plus abondante du monde vivant. L'ensemble de ces "
                "réactions forme une chaîne fermée : le cycle de Calvin."
            )
        ) as tracker:
            self.play(Write(titre))
            self.play(FadeIn(conditions))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(conditions))

        # --- Animation du raisonnement : étape 1, fixation du CO2 -------------
        etape1_texte = Text(
            _wrap(
                "Étape 1 — Fixation du CO2 : le CO2 de l'air est fixé "
                "par un composé à 5 atomes de carbone, le RuBP "
                "(ribulose-1,5-bisphosphate), sous l'action de l'enzyme "
                "Rubisco. Il se forme un composé instable à 6 atomes de "
                "carbone qui se scinde aussitôt en 2 molécules de PGA "
                "(acide 3-phosphoglycérique), à 3 atomes de carbone "
                "chacune.",
                width=56,
            ),
            font_size=20,
            color=WHITE,
        )
        etape1_texte.next_to(titre, DOWN, buff=0.45)

        with self.voiceover(
            text=(
                "Première étape du cycle : la fixation du CO2. Le "
                "dioxyde de carbone de l'air est fixé par un composé à "
                "cinq atomes de carbone, le RuBP, ou ribulose un cinq "
                "bisphosphate, sous l'action de l'enzyme Rubisco. Il se "
                "forme alors un composé instable à six atomes de "
                "carbone, qui se scinde aussitôt en deux molécules de "
                "PGA, l'acide trois phosphoglycérique, chacune à trois "
                "atomes de carbone."
            )
        ) as tracker:
            self.play(FadeIn(etape1_texte))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(etape1_texte))

        # --- Exemple traité : équation + schéma de la fixation ----------------
        equation = MathTex(
            r"RuBP\,(5C) + CO_2\,(1C) \xrightarrow{\;\text{Rubisco}\;} 2\,PGA\,(3C)",
            font_size=28,
            color=WHITE,
        )
        equation.next_to(titre, DOWN, buff=0.6)

        schema = _schema_fixation()
        schema.scale(0.95)
        schema.next_to(equation, DOWN, buff=0.7)

        with self.voiceover(
            text=(
                "Cela s'écrit ainsi : RuBP, cinq carbones, plus CO2, un "
                "carbone, sous l'action de la Rubisco, donnent deux PGA, "
                "trois carbones chacun. Vérifions les atomes de carbone "
                "au passage : cinq plus un font six ; trois plus trois "
                "font aussi six. Le compte est bon : c'est cette "
                "logique de conservation du carbone qui gouverne tout "
                "le cycle de Calvin."
            )
        ) as tracker:
            self.play(Write(equation))
            self.play(FadeIn(schema))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(equation), FadeOut(schema))

        # --- À retenir -----------------------------------------------------------
        essentiel = definition_box(
            Text(
                _wrap(
                    "À retenir : l'étape 1 du cycle de Calvin fixe le "
                    "carbone minéral (CO2) sur un accepteur organique "
                    "(RuBP), grâce à la Rubisco, et produit du PGA : "
                    "c'est la véritable porte d'entrée du carbone dans "
                    "la matière vivante.",
                    width=54,
                ),
                font_size=20,
            ),
            box_width=12.0,
        )
        essentiel.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Retenons l'essentiel : l'étape un du cycle de Calvin "
                "fixe le carbone minéral du CO2 sur un accepteur "
                "organique, le RuBP, grâce à l'enzyme Rubisco, et "
                "produit du PGA. C'est la véritable porte d'entrée du "
                "carbone minéral dans la matière vivante."
            )
        ) as tracker:
            self.play(FadeIn(essentiel))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(essentiel))

        # --- Piège à éviter : la Rubisco fixe le CO2, pas l'eau ----------------
        piege = warning_box(
            Text(
                _wrap(
                    "Piège à éviter : ne pas confondre la fixation du "
                    "CO2 (étape 1, dans le stroma, catalysée par la "
                    "Rubisco) avec la photolyse de l'eau (dans les "
                    "thylakoïdes, catalysée par la lumière). Ce sont "
                    "deux réactions différentes, dans deux "
                    "compartiments différents.",
                    width=54,
                ),
                font_size=20,
            ),
            box_width=12.0,
        )
        piege.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Attention à ne pas confondre la fixation du CO2, "
                "première étape du cycle de Calvin, qui se déroule dans "
                "le stroma et qui est catalysée par la Rubisco, avec la "
                "photolyse de l'eau, qui se déroule dans les "
                "thylakoïdes et qui dépend directement de la lumière. "
                "Ce sont deux réactions bien différentes, situées dans "
                "deux compartiments différents du chloroplaste."
            )
        ) as tracker:
            self.play(FadeIn(piege))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(titre), FadeOut(piege))
