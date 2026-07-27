"""
scenes/Physique_EnergieCinetique_04.py — Chapitre 3 « Énergie cinétique »
(1ereC, Physique), scène 04.

§ Établissement du théorème de l'énergie cinétique à partir de la chute
libre (ΔEc(A→B) = W(poids)), généralisation à toutes les forces, énoncé du
théorème en translation et en rotation, rappels utiles (travail du poids,
travail d'une force constante, force perpendiculaire, frottements).
Source : 1ereC/Physique.pdf, pages 24-33 (chapitre 3, § 4).
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
    Create,
    DashedLine,
    Dot,
    FadeIn,
    FadeOut,
    MathTex,
    Text,
    VGroup,
    Write,
)

from shapes.base_scene import NotionScene
from shapes.boxes import essentiel_box, property_box, scene_title, theorem_box


def _wrap(text: str, width: int = 56) -> str:
    return "\n".join(textwrap.fill(line, width=width) for line in text.split("\n"))


class TheoremeEnergieCinetiqueEtablissement(NotionScene):
    def construct(self):
        titre = scene_title("Théorème de l'énergie cinétique")
        titre.scale(0.55)
        titre.to_edge(UP)

        # --- Énoncé : reprise de la chute libre, A et B --------------------------
        haut = UP * 1.6 + LEFT * 4.0
        bas = DOWN * 1.6 + LEFT * 4.0
        ligne = DashedLine(haut, bas, color=WHITE, stroke_width=2)
        point_a = Dot(haut, color=YELLOW, radius=0.11)
        point_b = Dot(bas, color=YELLOW, radius=0.11)
        label_a = MathTex("A", font_size=26).next_to(point_a, LEFT, buff=0.15)
        label_b = MathTex("B", font_size=26).next_to(point_b, LEFT, buff=0.15)
        poids = Arrow(haut, haut + DOWN * 0.9, color="#B42E41", buff=0)
        poids_label = MathTex(r"\vec{P}", font_size=24, color="#B42E41").next_to(poids, RIGHT, buff=0.1)
        schema = VGroup(ligne, point_a, point_b, label_a, label_b, poids, poids_label)
        schema.move_to(LEFT * 3.4)

        mise_en_situation = Text(
            _wrap(
                "Reprenons la chute libre entre un point A (départ, vitesse "
                "nulle) et un point B (après une chute de hauteur h). Le "
                "poids est la seule force qui travaille.",
                width=42,
            ),
            font_size=21,
        )
        mise_en_situation.next_to(schema, RIGHT, buff=0.6)

        with self.voiceover(
            text=(
                "Reprenons l'expérience de la chute libre, entre un point "
                "A de départ, à vitesse nulle, et un point B atteint après "
                "une chute de hauteur h. Seul le poids travaille pendant "
                "ce trajet."
            )
        ) as tracker:
            self.play(Write(titre))
            self.play(Create(schema))
            self.play(FadeIn(mise_en_situation))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(schema), FadeOut(mise_en_situation))

        # --- Raisonnement : Delta Ec = W(poids) puis généralisation ---------------
        raisonnement = VGroup(
            MathTex(r"E_{cA} = 0, \qquad E_{cB} = \dfrac{1}{2}mv_B^2 = mgh", font_size=27),
            MathTex(r"W_{A\to B}(\vec{P}) = mgh", font_size=27),
            MathTex(r"\Longrightarrow\ E_{cB} - E_{cA} = W_{A\to B}(\vec{P})", font_size=30, color=YELLOW),
        ).arrange(DOWN, buff=0.32)
        raisonnement.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "En A, l'énergie cinétique est nulle. En B, elle vaut un "
                "demi m v B carré, soit m g h d'après la relation établie "
                "précédemment. Or le travail du poids entre A et B vaut "
                "exactement m g h. On remarque donc que la variation "
                "d'énergie cinétique entre A et B est égale au travail du "
                "poids sur ce trajet."
            )
        ) as tracker:
            self.play(Write(raisonnement[0]))
            self.play(Write(raisonnement[1]))
            self.play(Write(raisonnement[2]))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(raisonnement))

        generalisation = Text(
            _wrap(
                "Ce résultat, établi ici pour le seul poids, se généralise : "
                "quelle que soit la nature des forces appliquées, la "
                "variation d'énergie cinétique est égale à la somme des "
                "travaux de TOUTES les forces extérieures.",
                width=56,
            ),
            font_size=22,
        )
        generalisation.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Ce résultat, établi ici pour le seul poids, se généralise "
                "à n'importe quel système soumis à n'importe quelles "
                "forces : la variation d'énergie cinétique est toujours "
                "égale à la somme des travaux de toutes les forces "
                "extérieures appliquées. C'est le théorème de l'énergie "
                "cinétique."
            )
        ) as tracker:
            self.play(FadeIn(generalisation))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(generalisation))

        # --- Énoncé du théorème (translation) --------------------------------------
        theoreme_trans = theorem_box(
            VGroup(
                Text("Théorème de l'énergie cinétique — translation", font_size=22, weight="BOLD"),
                MathTex(r"\Delta E_c = E_{cB} - E_{cA} = \sum W_{A\to B}(\vec{F}_{ext})", font_size=30),
            ).arrange(DOWN, buff=0.3),
            box_width=11.6,
        )
        theoreme_trans.next_to(titre, DOWN, buff=0.45)

        with self.voiceover(
            text=(
                "Énoncé officiel, en translation : dans un référentiel "
                "galiléen, la variation d'énergie cinétique d'un système "
                "entre un état A et un état B est égale à la somme des "
                "travaux de toutes les forces extérieures appliquées au "
                "système entre A et B."
            )
        ) as tracker:
            self.play(FadeIn(theoreme_trans))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(theoreme_trans))

        # --- Énoncé du théorème (rotation) ------------------------------------------
        theoreme_rot = theorem_box(
            VGroup(
                Text("Théorème de l'énergie cinétique — rotation", font_size=22, weight="BOLD"),
                MathTex(r"\Delta E_c = \dfrac{1}{2}J_\Delta\omega_2^2 - \dfrac{1}{2}J_\Delta\omega_1^2 = \sum \mathcal{M}_\Delta(\vec{F}_{ext}) \times \Delta\theta", font_size=25),
            ).arrange(DOWN, buff=0.3),
            box_width=12.6,
        )
        theoreme_rot.next_to(titre, DOWN, buff=0.45)

        with self.voiceover(
            text=(
                "Le même théorème existe en rotation autour d'un axe "
                "fixe : la variation d'énergie cinétique de rotation, un "
                "demi J delta oméga deux carré moins un demi J delta "
                "oméga un carré, est égale à la somme des moments des "
                "forces extérieures par rapport à l'axe delta, "
                "multipliée par la variation de l'angle de rotation."
            )
        ) as tracker:
            self.play(FadeIn(theoreme_rot))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(theoreme_rot))

        # --- Rappels utiles sur le travail -------------------------------------------
        rappels = property_box(
            VGroup(
                Text("Rappels utiles sur le travail d'une force", font_size=22, weight="BOLD"),
                MathTex(r"W(\vec{P}) = \pm mgh \quad \text{(} + \text{si le corps descend, } - \text{s'il monte)}", font_size=21),
                MathTex(r"W(\vec{F}) = \vec{F}\cdot\vec{AB} = F\times AB \times \cos\alpha \quad \text{(force constante)}", font_size=21),
                Text("Une force perpendiculaire au déplacement ne travaille pas (W = 0).", font_size=20),
                Text("Le travail des frottements est toujours résistant (W < 0).", font_size=20),
            ).arrange(DOWN, buff=0.22),
            box_width=12.6,
        )
        rappels.next_to(titre, DOWN, buff=0.35)

        with self.voiceover(
            text=(
                "Quatre rappels utiles pour appliquer ce théorème. Le "
                "travail du poids vaut plus ou moins m g h, positif si le "
                "corps descend, négatif s'il monte. Le travail d'une force "
                "constante vaut F fois A B fois le cosinus de l'angle "
                "entre eux. Une force perpendiculaire au déplacement ne "
                "travaille jamais, son travail est nul. Et le travail des "
                "frottements est toujours résistant, donc toujours "
                "négatif."
            )
        ) as tracker:
            self.play(FadeIn(rappels))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(rappels))

        # --- À retenir -------------------------------------------------------------
        retenir = essentiel_box(
            VGroup(
                Text("À retenir", font_size=24, weight="BOLD"),
                MathTex(r"\Delta E_c = \sum W_{A\to B}(\vec{F}_{ext}) \quad \text{(translation)}", font_size=24),
                MathTex(r"\Delta E_c = \sum \mathcal{M}_\Delta(\vec{F}_{ext}) \times \Delta\theta \quad \text{(rotation)}", font_size=24),
            ).arrange(DOWN, buff=0.25),
            box_width=12.0,
        )
        retenir.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Retenons l'essentiel : la variation d'énergie cinétique "
                "est toujours égale à la somme des travaux des forces "
                "extérieures en translation, ou à la somme des moments "
                "des forces multipliée par la variation d'angle en "
                "rotation. C'est l'outil central de toute la suite du "
                "chapitre."
            )
        ) as tracker:
            self.play(FadeIn(retenir))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(retenir), FadeOut(titre))
