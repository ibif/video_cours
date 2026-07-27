"""
scenes/Physique_EnergiePotentielle_02.py — Chapitre 4 « Énergie potentielle »
(1ereC, Physique), scène 02.

Mise en évidence de l'énergie potentielle de pesanteur : reprise du
théorème de l'énergie cinétique pour une bille en chute libre entre A et B,
ΔEc = W(poids) = mg(z_A - z_B), regroupement Ec(B)+mgz_B = Ec(A)+mgz_A,
apparition de l'expression mgz comme énergie « en réserve » liée à la
position.
Source : 1ereC/Physique.pdf, chapitre 4, pages 34-42.
"""

import textwrap

from manim import (
    BLUE,
    DOWN,
    LEFT,
    PI,
    RIGHT,
    UP,
    WHITE,
    YELLOW,
    Arrow,
    Dot,
    FadeIn,
    FadeOut,
    MathTex,
    NumberLine,
    Text,
    VGroup,
    Write,
)

from shapes.base_scene import NotionScene
from shapes.boxes import essentiel_box, scene_title


def _wrap(text: str, width: int = 56) -> str:
    return "\n".join(textwrap.fill(line, width=width) for line in text.split("\n"))


class MiseEnEvidenceEppPesanteur(NotionScene):
    def construct(self):
        titre = scene_title("Énergie potentielle de pesanteur : mise en évidence")
        titre.scale(0.48)
        titre.to_edge(UP)

        # --- Énoncé : rappel du théorème de l'énergie cinétique -----------------
        rappel = Text(
            _wrap(
                "Rappel : une bille de masse m est lâchée sans vitesse "
                "initiale en A, et tombe en chute libre jusqu'en B, plus "
                "bas. Que dit le théorème de l'énergie cinétique entre A "
                "et B ?",
                width=52,
            ),
            font_size=25,
        )
        rappel.next_to(titre, DOWN, buff=0.6)

        with self.voiceover(
            text=(
                "Reprenons le théorème de l'énergie cinétique sur un "
                "exemple simple. Une bille de masse m est lâchée sans "
                "vitesse initiale au point A, et tombe en chute libre "
                "jusqu'au point B, situé plus bas. Que nous dit le théorème "
                "de l'énergie cinétique entre A et B ?"
            )
        ) as tracker:
            self.play(Write(rappel))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(rappel))

        # --- Schéma : axe vertical, points A et B, bille, poids ------------------
        axe = NumberLine(x_range=[0, 6, 1], length=4.2, include_numbers=False, color=WHITE)
        axe.rotate(PI / 2)
        axe.move_to(LEFT * 3.6)
        label_z = MathTex("z", font_size=30).next_to(axe, UP, buff=0.15)

        point_a = axe.n2p(4.5)
        point_b = axe.n2p(1.0)

        bille = Dot(point_a, color=YELLOW, radius=0.14)
        label_a = MathTex("A", font_size=30).next_to(point_a, RIGHT, buff=0.2)
        label_b = MathTex("B", font_size=30).next_to(point_b, RIGHT, buff=0.2)
        label_za = MathTex("z_A", font_size=26).next_to(point_a, LEFT, buff=0.6)
        label_zb = MathTex("z_B", font_size=26).next_to(point_b, LEFT, buff=0.6)

        poids = Arrow(point_a, point_a + DOWN * 0.9, color=BLUE, buff=0)
        label_poids = MathTex(r"\vec{P}", font_size=26, color=BLUE).next_to(poids, RIGHT, buff=0.1)

        schema = VGroup(axe, label_z, bille, label_a, label_b, label_za, label_zb, poids, label_poids)
        schema.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Traçons un axe vertical Oz, orienté vers le haut. La bille "
                "part du point A, d'altitude z indice A, soumise à son "
                "poids, dirigé vers le bas. Elle tombe librement jusqu'au "
                "point B, d'altitude z indice B, avec z indice B inférieur "
                "à z indice A."
            )
        ) as tracker:
            self.play(Write(axe), Write(label_z))
            self.play(FadeIn(bille), Write(label_a), Write(label_za))
            self.play(FadeIn(poids), Write(label_poids))
            self.wait(tracker.get_remaining_duration())

        with self.voiceover(
            text=(
                "La bille chute, entraînée par son poids, du point A "
                "jusqu'au point B."
            )
        ) as tracker:
            self.play(bille.animate.move_to(point_b), run_time=1.5)
            self.play(Write(label_b), Write(label_zb))
            self.wait(tracker.get_remaining_duration())

        # --- Raisonnement : théorème de l'énergie cinétique -----------------------
        tec = MathTex(
            r"\Delta E_c = E_c(B) - E_c(A) = W_{A \to B}(\vec{P})",
            font_size=30,
        )
        tec.next_to(schema, RIGHT, buff=0.8).align_to(schema, UP)

        travail_poids = MathTex(
            r"W_{A \to B}(\vec{P}) = mg\,(z_A - z_B)",
            font_size=30,
        )
        travail_poids.next_to(tec, DOWN, buff=0.4, aligned_edge=LEFT)

        with self.voiceover(
            text=(
                "Le théorème de l'énergie cinétique donne : la variation "
                "d'énergie cinétique entre A et B est égale au travail du "
                "poids entre A et B. Or, le travail du poids, seule force "
                "agissant ici, vaut m g fois z indice A moins z indice B."
            )
        ) as tracker:
            self.play(Write(tec))
            self.play(Write(travail_poids))
            self.wait(tracker.get_remaining_duration())

        combinaison = MathTex(
            r"E_c(B) - E_c(A) = mg\,z_A - mg\,z_B",
            font_size=30,
        )
        combinaison.next_to(travail_poids, DOWN, buff=0.4, aligned_edge=LEFT)

        regroupement = MathTex(
            r"E_c(B) + mg\,z_B = E_c(A) + mg\,z_A",
            font_size=32,
            color=YELLOW,
        )
        regroupement.next_to(combinaison, DOWN, buff=0.5, aligned_edge=LEFT)

        with self.voiceover(
            text=(
                "En combinant les deux égalités, puis en regroupant les "
                "termes en A d'un côté et les termes en B de l'autre, on "
                "obtient une relation remarquable : l'énergie cinétique en "
                "B, plus m g z indice B, est égale à l'énergie cinétique en "
                "A, plus m g z indice A. Autrement dit, la quantité énergie "
                "cinétique plus m g z se conserve entre A et B."
            )
        ) as tracker:
            self.play(Write(combinaison))
            self.play(Write(regroupement))
            self.wait(tracker.get_remaining_duration())

        self.play(
            FadeOut(schema),
            FadeOut(tec),
            FadeOut(travail_poids),
            FadeOut(combinaison),
        )
        self.play(regroupement.animate.next_to(titre, DOWN, buff=0.7))

        # --- Interprétation : mgz = énergie « en réserve » ------------------------
        interpretation = Text(
            _wrap(
                "Le terme mgz, associé à la position, se comporte comme "
                "une énergie « en réserve » : c'est l'énergie potentielle "
                "de pesanteur, notée Epp.",
                width=52,
            ),
            font_size=25,
        )
        interpretation.next_to(regroupement, DOWN, buff=0.7)

        with self.voiceover(
            text=(
                "Le terme m g z, qui apparaît ici associé à la position de "
                "la bille sur l'axe vertical, se comporte exactement comme "
                "une énergie mise en réserve : quand la bille descend, ce "
                "terme diminue et l'énergie cinétique augmente d'autant. "
                "C'est précisément cette grandeur que l'on baptise énergie "
                "potentielle de pesanteur, notée Epp."
            )
        ) as tracker:
            self.play(Write(interpretation))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(interpretation), FadeOut(regroupement))

        # --- À retenir -------------------------------------------------------------
        retenir = essentiel_box(
            Text(
                _wrap(
                    "Pour une bille en chute libre : Ec(B)+mgzB = "
                    "Ec(A)+mgzA. Le terme mgz, lié à l'altitude, se "
                    "comporte comme une énergie en réserve : c'est "
                    "l'énergie potentielle de pesanteur Epp.",
                    width=56,
                ),
                font_size=23,
            )
        )
        retenir.next_to(titre, DOWN, buff=0.6)

        with self.voiceover(
            text=(
                "À retenir : pour une bille en chute libre, la somme "
                "énergie cinétique plus m g z se conserve entre deux "
                "instants. Le terme m g z, lié à l'altitude, se comporte "
                "comme une énergie en réserve : c'est l'énergie "
                "potentielle de pesanteur, Epp. Dans la scène suivante, "
                "nous allons en donner la définition précise et son "
                "expression."
            )
        ) as tracker:
            self.play(FadeIn(retenir))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(titre), FadeOut(retenir))
