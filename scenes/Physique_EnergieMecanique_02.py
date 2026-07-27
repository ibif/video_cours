"""
scenes/Physique_EnergieMecanique_02.py — Chapitre 5 « Énergie mécanique »
(1ereC, Physique), scène 02.

Mise en évidence : cas de la chute libre. Système/bilan des forces (poids
seul), application du théorème de l'énergie cinétique entre A et B,
regroupement Ec(B)+mgzB=Ec(A)+mgzA, et constat que la quantité Ec+Ep se
conserve — introduction du nom « énergie mécanique ».
Source : 1ereC/Physique.pdf, chapitre 5, pages 43-53.
"""

import textwrap

from manim import (
    DOWN,
    LEFT,
    RIGHT,
    UP,
    WHITE,
    YELLOW,
    DashedLine,
    Dot,
    FadeIn,
    FadeOut,
    MathTex,
    Text,
    VGroup,
    Vector,
    Write,
)

from shapes.base_scene import NotionScene
from shapes.boxes import definition_box, essentiel_box, scene_title, theorem_box, warning_box

POIDS_COLOR = "#1E5FA8"


def _wrap(text: str, width: int = 56) -> str:
    return "\n".join(textwrap.fill(line, width=width) for line in text.split("\n"))


class MiseEnEvidenceChuteLibre(NotionScene):
    def construct(self):
        titre = scene_title("Mise en évidence : la chute libre")
        titre.scale(0.5)
        titre.to_edge(UP)

        # --- Énoncé : bille en chute libre, système et bilan des forces -----------
        haut = UP * 1.6 + LEFT * 3.5
        bas = DOWN * 1.6 + LEFT * 3.5
        chute_ligne = DashedLine(haut, bas, color=WHITE, stroke_width=2)
        bille_a = Dot(haut, color=YELLOW, radius=0.14)
        bille_b = Dot(bas, color=YELLOW, radius=0.14)
        label_a = MathTex("A", font_size=26).next_to(bille_a, LEFT, buff=0.15)
        label_b = MathTex("B", font_size=26).next_to(bille_b, LEFT, buff=0.15)
        poids_vec = Vector(DOWN * 0.7, color=POIDS_COLOR).next_to(bille_a, RIGHT, buff=0.15)
        label_poids = MathTex(r"\vec{P}", font_size=24, color=POIDS_COLOR).next_to(poids_vec, RIGHT, buff=0.1)
        sol = DashedLine(bas + LEFT * 0.6, bas + RIGHT * 1.6, color=WHITE, stroke_width=2)
        schema = VGroup(chute_ligne, bille_a, bille_b, label_a, label_b, poids_vec, label_poids, sol)
        schema.move_to(LEFT * 2.5)

        systeme = definition_box(
            VGroup(
                Text("Système : la bille", font_size=21, weight="BOLD"),
                Text("Bilan des forces : le poids P⃗ SEUL", font_size=20),
                Text("(chute libre : air négligé)", font_size=19),
            ).arrange(DOWN, buff=0.18, aligned_edge=LEFT),
            box_width=6.0,
        )
        systeme.next_to(schema, RIGHT, buff=0.6)

        with self.voiceover(
            text=(
                "Reprenons la situation de la chute libre. Une bille est "
                "lâchée sans vitesse initiale au point A, et arrive au "
                "point B avec une certaine vitesse. Le système étudié est "
                "la bille, et le bilan des forces se réduit à une seule "
                "force : le poids, puisque la résistance de l'air est "
                "négligée."
            )
        ) as tracker:
            self.play(Write(titre))
            self.play(FadeIn(schema), FadeIn(systeme))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(schema), FadeOut(systeme))

        # --- Raisonnement : théorème de l'énergie cinétique --------------------------
        etape1 = MathTex(
            r"E_c(B) - E_c(A) = W_{AB}(\vec{P}) = mg\,(z_A - z_B)",
            font_size=28,
        )
        etape1.next_to(titre, DOWN, buff=0.6)

        with self.voiceover(
            text=(
                "Appliquons le théorème de l'énergie cinétique entre A et "
                "B : E c de B moins E c de A est égal au travail du poids, "
                "soit m g fois z de A moins z de B."
            )
        ) as tracker:
            self.play(Write(etape1))
            self.wait(tracker.get_remaining_duration())

        etape2 = MathTex(
            r"E_c(B) - E_c(A) = mgz_A - mgz_B",
            font_size=28,
        )
        etape2.next_to(etape1, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "En développant le membre de droite, on obtient E c de B "
                "moins E c de A égale m g z de A moins m g z de B."
            )
        ) as tracker:
            self.play(Write(etape2))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(etape1), FadeOut(etape2))

        etape3 = MathTex(
            r"E_c(B) + mgz_B = E_c(A) + mgz_A",
            font_size=30,
            color=YELLOW,
        )
        etape3.next_to(titre, DOWN, buff=0.7)

        with self.voiceover(
            text=(
                "Regroupons maintenant les termes relatifs à B d'un côté, "
                "et ceux relatifs à A de l'autre : E c de B plus m g z de "
                "B égale E c de A plus m g z de A."
            )
        ) as tracker:
            self.play(Write(etape3))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(etape3))

        # --- Constat : la quantité Ec+Ep se conserve ---------------------------------
        constat = theorem_box(
            VGroup(
                Text("La quantité Ec + Ep a la MÊME valeur en A et en B :", font_size=21),
                MathTex(r"E_c(A) + E_{pp}(A) = E_c(B) + E_{pp}(B)", font_size=27),
                Text("Elle se conserve tout au long de la chute.", font_size=21),
            ).arrange(DOWN, buff=0.25),
            box_width=10.8,
        )
        constat.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Autrement dit, la quantité énergie cinétique plus énergie "
                "potentielle de pesanteur a exactement la même valeur au "
                "point A et au point B. Elle ne dépend pas de l'instant "
                "choisi : elle se conserve tout au long de la chute. Cette "
                "quantité, somme de l'énergie cinétique et de l'énergie "
                "potentielle, mérite un nom : on l'appelle l'énergie "
                "mécanique du système."
            )
        ) as tracker:
            self.play(FadeIn(constat))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(constat))

        # --- À retenir -----------------------------------------------------------------
        retenir = essentiel_box(
            Text(
                _wrap(
                    "En chute libre, la somme Ec+Ep ne varie pas entre deux "
                    "instants quelconques. Cette quantité conservée porte "
                    "un nom : l'énergie mécanique, que nous allons "
                    "définir précisément.",
                    width=54,
                ),
                font_size=22,
            ),
            box_width=11.0,
        )
        retenir.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "À retenir : en chute libre, la somme de l'énergie "
                "cinétique et de l'énergie potentielle ne varie pas entre "
                "deux instants quelconques. Cette quantité conservée porte "
                "un nom, l'énergie mécanique, que nous allons maintenant "
                "définir précisément."
            )
        ) as tracker:
            self.play(FadeIn(retenir))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(retenir))

        # --- Piège à éviter ------------------------------------------------------------
        piege = warning_box(
            Text(
                _wrap(
                    "Cette conservation n'a été démontrée ici QUE pour la "
                    "chute libre (poids seul). Elle ne sera pas toujours "
                    "vraie : la scène suivante précisera à quelles "
                    "conditions elle s'applique.",
                    width=54,
                ),
                font_size=22,
            ),
            box_width=11.2,
        )
        piege.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Attention cependant : cette conservation n'a été démontrée "
                "ici que dans le cas particulier de la chute libre, où le "
                "poids est la seule force à s'exercer. Elle ne sera pas "
                "toujours vraie : nous préciserons bientôt, avec rigueur, "
                "à quelles conditions exactement l'énergie mécanique se "
                "conserve."
            )
        ) as tracker:
            self.play(FadeIn(piege))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(piege), FadeOut(titre))
