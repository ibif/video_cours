"""
scenes/Physique_EnergieMecanique_06.py — Chapitre 5 « Énergie mécanique »
(1ereC, Physique), scène 06.

Non-conservation de l'énergie mécanique : démonstration (solide glissant
avec frottements sur plan incliné) Em(B)-Em(A)=W(frottement)=-fℓ<0.
Théorème de la loi de non-conservation ΔEm=ΣW(forces non conservatives).
Tableau récapitulatif (sans frottements→conservatif ; avec frottements→
dissipatif ΔEm=W(f)<0 ; avec moteur/traction→non conservatif ΔEm=
W(F_motrice)>0 ; système complet→énergie totale conservée). Exemple résolu
3 : luge 40 kg arrive à 10 m/s, s'arrête après 25 m sur zone rugueuse →
f=80 N.
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
    FadeIn,
    FadeOut,
    MathTex,
    Polygon,
    Square,
    Text,
    VGroup,
    Vector,
    Write,
)

from shapes.base_scene import NotionScene
from shapes.boxes import corrige_box, essentiel_box, exercise_box, scene_title, theorem_box, warning_box

FROTTEMENT_COLOR = "#B42E41"


def _wrap(text: str, width: int = 56) -> str:
    return "\n".join(textwrap.fill(line, width=width) for line in text.split("\n"))


def _plan_incline_rugueux():
    return Polygon(
        LEFT * 2.0 + DOWN * 1.2,
        RIGHT * 2.0 + DOWN * 1.2,
        RIGHT * 2.0 + UP * 1.0,
        color=WHITE,
        fill_color="#4A3A2A",
        fill_opacity=0.6,
    )


class NonConservationEnergieMecanique(NotionScene):
    def construct(self):
        titre = scene_title("Non-conservation de l'énergie mécanique")
        titre.scale(0.48)
        titre.to_edge(UP)

        # --- Énoncé : que se passe-t-il avec des frottements ? ------------------------
        plan = _plan_incline_rugueux().scale(0.75)
        point_a = plan.get_vertices()[2] + LEFT * 0.3 + DOWN * 0.1
        point_b = plan.get_vertices()[0] + RIGHT * 0.3 + UP * 0.1
        solide_a = Square(side_length=0.28, color=YELLOW, fill_color=YELLOW, fill_opacity=0.9).move_to(point_a)
        solide_b = Square(side_length=0.28, color=YELLOW, fill_color=YELLOW, fill_opacity=0.4).move_to(point_b)
        frott_vec = Vector(RIGHT * 0.4 + UP * 0.15, color=FROTTEMENT_COLOR).next_to(solide_a, LEFT, buff=0.05)
        label_f = MathTex(r"\vec{f}", font_size=20, color=FROTTEMENT_COLOR).next_to(frott_vec, LEFT, buff=0.08)
        label_a = MathTex("A", font_size=22).next_to(solide_a, DOWN, buff=0.12)
        label_b = MathTex("B", font_size=22).next_to(solide_b, UP, buff=0.12)
        schema = VGroup(plan, solide_a, solide_b, frott_vec, label_f, label_a, label_b)
        schema.scale(0.85).move_to(LEFT * 3.2)

        intro = Text(
            _wrap(
                "Que se passe-t-il si, cette fois, le plan incliné est "
                "rugueux, et qu'une force de frottement s'exerce sur le "
                "solide en mouvement ?",
                width=42,
            ),
            font_size=22,
        )
        intro.next_to(schema, RIGHT, buff=0.4)

        with self.voiceover(
            text=(
                "Que se passe-t-il, cette fois, si le plan incliné est "
                "rugueux, et qu'une force de frottement, non conservative, "
                "s'exerce sur le solide glissant de A vers B ?"
            )
        ) as tracker:
            self.play(Write(titre))
            self.play(FadeIn(schema), FadeIn(intro))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(schema), FadeOut(intro))

        # --- Raisonnement : démonstration ------------------------------------------------
        demo1 = MathTex(
            r"E_c(B) - E_c(A) = W_{AB}(\vec{P}) + W_{AB}(\vec{R}) + W_{AB}(\vec{f})",
            font_size=25,
        )
        demo2 = MathTex(
            r"W_{AB}(\vec{P}) = E_{pp}(A) - E_{pp}(B), \quad W_{AB}(\vec{R}) = 0",
            font_size=25,
        )
        demo3 = MathTex(
            r"E_m(B) - E_m(A) = W_{AB}(\vec{f}) = -f\ell < 0",
            font_size=28,
            color=YELLOW,
        )
        demo = VGroup(demo1, demo2, demo3).arrange(DOWN, buff=0.32)
        demo.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Le théorème de l'énergie cinétique s'écrit maintenant avec "
                "trois travaux : celui du poids, celui de la réaction, "
                "toujours nul, et celui de la force de frottement. En "
                "reprenant le même regroupement que précédemment, on "
                "obtient cette fois : l'énergie mécanique en B, moins "
                "l'énergie mécanique en A, est égale au travail de la force "
                "de frottement, soit moins f fois ℓ, la longueur du trajet "
                "— une quantité négative."
            )
        ) as tracker:
            self.play(Write(demo1))
            self.play(Write(demo2))
            self.play(Write(demo3))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(demo))

        theoreme = theorem_box(
            VGroup(
                Text("Loi de non-conservation de l'énergie mécanique", font_size=20, weight="BOLD"),
                MathTex(r"\Delta E_m = E_m(B) - E_m(A) = \sum W_{AB}(\vec{F}_{\text{non conservatives}})", font_size=25),
            ).arrange(DOWN, buff=0.25),
            box_width=11.0,
        )
        theoreme.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "On généralise ce résultat en un théorème : la variation de "
                "l'énergie mécanique d'un système est égale à la somme des "
                "travaux des forces non conservatives qui s'exercent sur "
                "lui — frottements, ou force motrice éventuelle."
            )
        ) as tracker:
            self.play(FadeIn(theoreme))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(theoreme))

        # --- Tableau récapitulatif -------------------------------------------------------
        tableau = VGroup(
            Text("Sans frottement → système conservatif : Em = constante", font_size=19),
            Text("Avec frottements → dissipatif : ΔEm = W(f) < 0", font_size=19),
            Text("Avec force motrice → non conservatif : ΔEm = W(F) > 0", font_size=19),
            Text("Système complet (+ source d'énergie) → énergie TOTALE conservée", font_size=19),
        ).arrange(DOWN, buff=0.2, aligned_edge=LEFT)
        tableau_box = theorem_box(tableau, box_width=11.6)
        tableau_box.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Récapitulons quatre situations. Sans frottement, le "
                "système est conservatif : l'énergie mécanique reste "
                "constante. Avec des frottements, le système est "
                "dissipatif : la variation d'énergie mécanique est égale au "
                "travail des frottements, négatif. Avec une force motrice, "
                "comme une traction, le système est non conservatif, mais "
                "cette fois la variation est positive. Enfin, si l'on "
                "considère le système complet, y compris la source "
                "d'énergie, c'est l'énergie totale qui reste conservée : "
                "rien ne se perd, l'énergie mécanique « perdue » est "
                "simplement transférée sous une autre forme, la chaleur."
            )
        ) as tracker:
            self.play(FadeIn(tableau_box))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(tableau_box))

        # --- Exemple traité : luge sur zone rugueuse --------------------------------------
        enonce = exercise_box(
            Text(
                _wrap(
                    "Une luge de masse 40 kg arrive à 10 m/s sur une zone "
                    "horizontale rugueuse et s'arrête après avoir parcouru "
                    "25 m. Calculer l'intensité f de la force de "
                    "frottement (supposée constante).",
                    width=52,
                ),
                font_size=21,
            ),
            box_width=11.0,
        )
        enonce.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Exemple résolu. Une luge de masse quarante kilogrammes "
                "arrive à dix mètres par seconde sur une zone horizontale "
                "rugueuse, et s'arrête après avoir parcouru vingt-cinq "
                "mètres. Calculons l'intensité f de la force de frottement, "
                "supposée constante."
            )
        ) as tracker:
            self.play(FadeIn(enonce))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(enonce))

        calc1 = MathTex(
            r"\text{Terrain horizontal} \Rightarrow E_{pp}(A)=E_{pp}(B) \Rightarrow \Delta E_m = \Delta E_c",
            font_size=23,
        )
        calc2 = MathTex(
            r"\Delta E_c = E_c(B) - E_c(A) = 0 - \tfrac{1}{2}\times 40\times 10^2 = -2000\ \text{J}",
            font_size=24,
        )
        calc3 = MathTex(
            r"\Delta E_m = W(\vec{f}) = -f\ell \ \Longrightarrow\ f = \dfrac{2000}{25} = 80\ \text{N}",
            font_size=26,
            color=YELLOW,
        )
        calc = VGroup(calc1, calc2, calc3).arrange(DOWN, buff=0.3)
        calc.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Le terrain étant horizontal, l'énergie potentielle de "
                "pesanteur ne varie pas, donc la variation d'énergie "
                "mécanique se réduit à la variation d'énergie cinétique. "
                "Celle-ci vaut zéro moins un demi fois quarante fois dix au "
                "carré, soit moins deux mille joules. Cette variation est "
                "égale au travail du frottement, moins f fois ℓ. On en "
                "déduit f égale deux mille divisé par vingt-cinq, soit "
                "quatre-vingts newtons."
            )
        ) as tracker:
            self.play(Write(calc1))
            self.play(Write(calc2))
            self.play(Write(calc3))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(calc))

        # --- À retenir ---------------------------------------------------------------------
        retenir = essentiel_box(
            MathTex(
                r"\Delta E_m = \sum W(\vec{F}_{\text{non conservatives}}) \quad (<0 \text{ si frottements})",
                font_size=25,
            ),
            box_width=10.6,
        )
        retenir.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Retenons l'essentiel : la variation d'énergie mécanique "
                "est égale à la somme des travaux des forces non "
                "conservatives. Elle est négative en présence de "
                "frottements seuls, positive s'il existe une force motrice."
            )
        ) as tracker:
            self.play(FadeIn(retenir))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(retenir))

        # --- Piège à éviter ------------------------------------------------------------------
        piege = warning_box(
            Text(
                _wrap(
                    "Piège : W(f) = -fℓ où ℓ est la LONGUEUR DU TRAJET "
                    "parcouru, pas la distance entre A et B « à vol "
                    "d'oiseau ». Sur un trajet courbe ou un aller-retour, "
                    "ne pas les confondre.",
                    width=52,
                ),
                font_size=21,
            ),
            box_width=11.0,
        )
        piege.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Piège fréquent, à retenir dès maintenant : le travail du "
                "frottement vaut moins f fois ℓ, où ℓ est la longueur du "
                "trajet réellement parcouru, et non la distance directe "
                "entre le point de départ et le point d'arrivée. Sur un "
                "trajet courbe, ou lors d'un aller-retour, il ne faut "
                "surtout pas les confondre."
            )
        ) as tracker:
            self.play(FadeIn(piege))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(piege), FadeOut(titre))
