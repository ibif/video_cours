"""
scenes/Physique_EnergiePotentielleElectrostatique_05.py — Chapitre « Énergie
potentielle électrostatique » (1ereC, Physique), scène 05.

Sens du champ électrostatique (orienté dans le sens des potentiels
décroissants, démonstration courte) et surfaces équipotentielles :
définition, travail nul entre deux points d'une même équipotentielle,
équipotentielles perpendiculaires aux lignes de champ (démonstration
courte), équipotentielles planes et parallèles aux armatures dans un champ
uniforme.
Source : 1ereC/Physique.pdf, pages 66-75.
"""

import textwrap

from manim import (
    BLUE,
    DOWN,
    LEFT,
    RED,
    RIGHT,
    UP,
    WHITE,
    YELLOW,
    Arrow,
    DashedLine,
    FadeIn,
    FadeOut,
    MathTex,
    Rectangle,
    Text,
    VGroup,
    Write,
)

from shapes.base_scene import NotionScene
from shapes.boxes import definition_box, essentiel_box, property_box, scene_title


def _wrap(text: str, width: int = 56) -> str:
    return "\n".join(textwrap.fill(line, width=width) for line in text.split("\n"))


def _plaques_equipotentielles(sep: float = 4.6, hauteur: float = 2.6, n_lignes: int = 4):
    plaque_pos = Rectangle(width=0.14, height=hauteur, color=RED, fill_color=RED, fill_opacity=1.0)
    plaque_neg = Rectangle(width=0.14, height=hauteur, color=BLUE, fill_color=BLUE, fill_opacity=1.0)
    plaque_pos.move_to(LEFT * sep / 2)
    plaque_neg.move_to(RIGHT * sep / 2)
    label_pos = Text("+", font_size=26, color=RED).next_to(plaque_pos, UP, buff=0.1)
    label_neg = Text("−", font_size=26, color=BLUE).next_to(plaque_neg, UP, buff=0.1)
    champ = Arrow(
        plaque_pos.get_right() + UP * 0.9 + RIGHT * 0.1,
        plaque_neg.get_left() + UP * 0.9 + LEFT * 0.1,
        color=YELLOW,
        buff=0,
        stroke_width=3,
    )
    label_e = MathTex(r"\vec{E}", font_size=22, color=YELLOW).next_to(champ, UP, buff=0.1)
    lignes = VGroup()
    xs = [plaque_pos.get_right()[0] + i * (sep / (n_lignes + 1)) for i in range(1, n_lignes + 1)]
    for x in xs:
        ligne = DashedLine([x, -hauteur / 2 + 0.1, 0], [x, hauteur / 2 - 0.1, 0], color=WHITE, stroke_width=1.5)
        lignes.add(ligne)
    return VGroup(plaque_pos, plaque_neg, label_pos, label_neg, champ, label_e, lignes)


class SensChampEquipotentielles(NotionScene):
    def construct(self):
        titre = scene_title("Sens du champ et surfaces équipotentielles")
        titre.scale(0.5)
        titre.to_edge(UP)

        # --- Énoncé : dans quel sens pointe E⃗ ? -----------------------------------
        question = Text(
            _wrap(
                "Nous savons que U_AB=V_A-V_B=E⃗·AB⃗. Dans quel sens le "
                "champ E⃗ pointe-t-il, par rapport aux potentiels ?",
                width=54,
            ),
            font_size=23,
        )
        question.next_to(titre, DOWN, buff=0.7)

        with self.voiceover(
            text=(
                "Nous avons établi que U A B égale V A moins V B, égale E "
                "fois AB. Une question naturelle se pose : dans quel sens "
                "le champ électrostatique pointe-t-il, par rapport aux "
                "valeurs du potentiel ?"
            )
        ) as tracker:
            self.play(Write(question))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(question))

        # --- Raisonnement : démonstration courte ------------------------------------------
        demo = VGroup(
            MathTex(
                r"\text{Si A et B sont sur une ligne de champ, avec } \vec{AB} \parallel \vec{E} :",
                font_size=22,
            ),
            MathTex(r"V_A - V_B = \vec{E}\cdot\vec{AB} = E \times AB > 0", font_size=26),
            MathTex(r"\Rightarrow \; V_A > V_B", font_size=28, color=YELLOW),
        ).arrange(DOWN, buff=0.35)
        demo.next_to(titre, DOWN, buff=0.8)

        with self.voiceover(
            text=(
                "Considérons deux points A et B sur une même ligne de "
                "champ, avec le vecteur AB orienté exactement dans le sens "
                "du champ E. Le produit scalaire E fois AB est alors "
                "positif, puisque les deux vecteurs sont colinéaires et de "
                "même sens. Donc V A moins V B est positif, ce qui signifie "
                "que V A est supérieur à V B."
            )
        ) as tracker:
            self.play(Write(demo[0]))
            self.play(Write(demo[1]))
            self.play(Write(demo[2]))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(demo))

        propriete_sens = property_box(
            Text(
                _wrap(
                    "Le champ électrostatique E⃗ est orienté dans le sens "
                    "des potentiels décroissants : E⃗ pointe toujours du "
                    "point de plus haut potentiel vers celui de plus bas "
                    "potentiel.",
                    width=52,
                ),
                font_size=22,
            ),
            box_width=10.8,
        )
        propriete_sens.next_to(titre, DOWN, buff=0.7)

        with self.voiceover(
            text=(
                "Autrement dit, A, situé « avant » sur la ligne de champ, "
                "est au potentiel le plus élevé. Le champ électrostatique "
                "est donc toujours orienté dans le sens des potentiels "
                "décroissants : il pointe du point de plus haut potentiel "
                "vers celui de plus bas potentiel."
            )
        ) as tracker:
            self.play(FadeIn(propriete_sens))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(propriete_sens))

        # --- Définition : surface équipotentielle -------------------------------------
        definition = definition_box(
            Text(
                _wrap(
                    "Une surface équipotentielle est l'ensemble des points "
                    "M de l'espace ayant le même potentiel électrique : "
                    "pour tous M et N sur la surface, V_M=V_N.",
                    width=52,
                ),
                font_size=23,
            ),
            box_width=10.8,
        )
        definition.next_to(titre, DOWN, buff=0.7)

        with self.voiceover(
            text=(
                "Introduisons maintenant la notion de surface "
                "équipotentielle. Une surface équipotentielle est "
                "l'ensemble des points M de l'espace qui ont exactement le "
                "même potentiel électrique : pour deux points M et N "
                "quelconques de cette surface, V M est égal à V N."
            )
        ) as tracker:
            self.play(FadeIn(definition))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(definition))

        # --- Propriétés des équipotentielles ------------------------------------------
        prop1 = MathTex(
            r"V_M = V_N \; \Rightarrow \; U_{MN} = 0 \; \Rightarrow \; W_{M \to N}(\vec{F}) = qU_{MN} = 0",
            font_size=24,
        )
        prop2 = Text(
            "Les équipotentielles sont perpendiculaires aux lignes de champ.",
            font_size=21,
        )
        proprietes = VGroup(prop1, prop2).arrange(DOWN, buff=0.4)
        proprietes.next_to(titre, DOWN, buff=0.7)

        with self.voiceover(
            text=(
                "Deux propriétés en découlent. D'abord, le travail de la "
                "force électrostatique entre deux points d'une même "
                "équipotentielle est nul, puisque la tension entre ces "
                "deux points est nulle. Ensuite, les surfaces "
                "équipotentielles sont toujours perpendiculaires aux "
                "lignes de champ."
            )
        ) as tracker:
            self.play(Write(prop1))
            self.play(Write(prop2))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(proprietes))

        demo_perp = MathTex(
            r"\text{Si } \vec{MN} \text{ est tangent à la surface : } U_{MN}=\vec{E}\cdot\vec{MN}=0",
            font_size=22,
        )
        demo_perp2 = MathTex(
            r"\text{Avec } \vec{MN}\neq\vec{0} \; \Rightarrow \; \vec{E}\perp\vec{MN}",
            font_size=24,
            color=YELLOW,
        )
        demo_perp_grp = VGroup(demo_perp, demo_perp2).arrange(DOWN, buff=0.3)
        demo_perp_grp.next_to(titre, DOWN, buff=0.8)

        with self.voiceover(
            text=(
                "En effet, si M et N sont deux points infiniment proches "
                "de la même équipotentielle, le vecteur MN est tangent à "
                "la surface, et la tension U M N, égale à E fois MN, est "
                "nulle. Comme MN n'est pas le vecteur nul, c'est donc E qui "
                "est perpendiculaire à MN, et donc à la surface "
                "équipotentielle tout entière."
            )
        ) as tracker:
            self.play(Write(demo_perp))
            self.play(Write(demo_perp2))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(demo_perp_grp))

        # --- Exemple : champ uniforme, plans parallèles --------------------------------
        schema = _plaques_equipotentielles()
        schema.next_to(titre, DOWN, buff=0.6)

        with self.voiceover(
            text=(
                "Dans le cas particulier d'un champ uniforme, entre deux "
                "plaques planes et parallèles, les surfaces "
                "équipotentielles sont donc des plans, parallèles entre "
                "eux et parallèles aux armatures, perpendiculaires aux "
                "lignes de champ qui vont d'une plaque à l'autre."
            )
        ) as tracker:
            self.play(FadeIn(schema))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(schema))

        # --- À retenir ------------------------------------------------------------------
        retenir = essentiel_box(
            Text(
                _wrap(
                    "E⃗ pointe vers les potentiels décroissants. "
                    "Équipotentielle : V constant, W=0 entre deux de ses "
                    "points, toujours perpendiculaire aux lignes de champ "
                    "(plans parallèles aux armatures en champ uniforme).",
                    width=56,
                ),
                font_size=21,
            )
        )
        retenir.next_to(titre, DOWN, buff=0.6)

        with self.voiceover(
            text=(
                "À retenir : le champ électrostatique pointe toujours vers "
                "les potentiels décroissants. Une surface équipotentielle "
                "regroupe les points de même potentiel ; le travail y est "
                "nul entre deux quelconques de ses points, et elle est "
                "toujours perpendiculaire aux lignes de champ — des plans "
                "parallèles aux armatures, dans le cas d'un champ "
                "uniforme."
            )
        ) as tracker:
            self.play(FadeIn(retenir))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(titre), FadeOut(retenir))
