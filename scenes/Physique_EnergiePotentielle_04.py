"""
scenes/Physique_EnergiePotentielle_04.py — Chapitre 4 « Énergie potentielle »
(1ereC, Physique), scène 04.

Variation de l'énergie potentielle de pesanteur : théorème
ΔEpp = Epp(B) - Epp(A) = -W_{A→B}(poids) = mg(z_B - z_A), démonstration,
lecture physique (montée/descente, emmagasine/restitue), deux exemples
résolus (pierre par rapport à deux références différentes ; grue qui
soulève un sac de ciment).
Source : 1ereC/Physique.pdf, chapitre 4, pages 34-42.
"""

import textwrap

from manim import (
    DOWN,
    LEFT,
    RIGHT,
    UP,
    YELLOW,
    FadeIn,
    FadeOut,
    MathTex,
    Text,
    VGroup,
    Write,
)

from shapes.base_scene import NotionScene
from shapes.boxes import essentiel_box, example_box, scene_title, theorem_box


def _wrap(text: str, width: int = 56) -> str:
    return "\n".join(textwrap.fill(line, width=width) for line in text.split("\n"))


class VariationEpp(NotionScene):
    def construct(self):
        titre = scene_title("Variation de l'énergie potentielle de pesanteur")
        titre.scale(0.48)
        titre.to_edge(UP)

        # --- Énoncé : théorème -------------------------------------------------------
        theoreme = theorem_box(
            MathTex(
                r"\Delta E_{pp} = E_{pp}(B) - E_{pp}(A) = -W_{A \to B}(\vec{P}) = mg\,(z_B - z_A)",
                font_size=27,
            ),
            box_width=11.6,
        )
        theoreme.next_to(titre, DOWN, buff=0.6)

        with self.voiceover(
            text=(
                "Voici le théorème central de cette leçon. Entre deux "
                "points A et B, la variation de l'énergie potentielle de "
                "pesanteur, delta Epp, égale Epp de B moins Epp de A, est "
                "égale à l'opposé du travail du poids entre A et B, "
                "c'est-à-dire m g fois z indice B moins z indice A."
            )
        ) as tracker:
            self.play(FadeIn(theoreme))
            self.wait(tracker.get_remaining_duration())

        self.play(theoreme.animate.scale(0.75).to_corner(UP + RIGHT).shift(DOWN * 0.3))

        # --- Raisonnement : démonstration ---------------------------------------------
        demo1 = MathTex(
            r"E_{pp}(A) = mgz_A + \text{Cte}, \quad E_{pp}(B) = mgz_B + \text{Cte}",
            font_size=26,
        )
        demo2 = MathTex(
            r"E_{pp}(B) - E_{pp}(A) = mgz_B - mgz_A = mg\,(z_B - z_A)",
            font_size=26,
        )
        demo3 = MathTex(
            r"\text{Or } W_{A \to B}(\vec{P}) = mg\,(z_A - z_B) \; \Rightarrow \; E_{pp}(B) - E_{pp}(A) = -W_{A \to B}(\vec{P})",
            font_size=24,
        )
        demo = VGroup(demo1, demo2, demo3).arrange(DOWN, buff=0.4, aligned_edge=LEFT)
        demo.next_to(titre, DOWN, buff=0.9).to_edge(LEFT, buff=0.6)

        with self.voiceover(
            text=(
                "Démontrons cette relation. Par définition, Epp de A vaut m "
                "g z indice A plus une constante, et Epp de B vaut m g z "
                "indice B plus la même constante. En soustrayant, la "
                "constante disparaît : Epp de B moins Epp de A égale m g "
                "fois z indice B moins z indice A. Or, nous avons vu dans "
                "la scène précédente que le travail du poids de A vers B "
                "vaut m g fois z indice A moins z indice B. On reconnaît "
                "immédiatement l'opposé : Epp de B moins Epp de A est donc "
                "bien égal à moins le travail du poids de A vers B."
            )
        ) as tracker:
            self.play(Write(demo1))
            self.play(Write(demo2))
            self.play(Write(demo3))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(demo))

        # --- Lecture physique ---------------------------------------------------------
        lecture = VGroup(
            Text("Le système monte (zB > zA) :", font_size=23, color=YELLOW),
            MathTex(r"\Delta E_{pp} > 0 \quad \text{et} \quad W(\vec{P}) < 0", font_size=26),
            Text("→ le système emmagasine de l'énergie.", font_size=22),
            Text("Le système descend (zB < zA) :", font_size=23, color=YELLOW),
            MathTex(r"\Delta E_{pp} < 0 \quad \text{et} \quad W(\vec{P}) > 0", font_size=26),
            Text("→ le système restitue de l'énergie.", font_size=22),
        ).arrange(DOWN, buff=0.25)
        lecture.next_to(titre, DOWN, buff=0.9)

        with self.voiceover(
            text=(
                "Interprétons physiquement ce résultat. Quand le système "
                "monte, z indice B est supérieur à z indice A : delta Epp "
                "est positif, et le travail du poids est négatif — le "
                "système emmagasine de l'énergie potentielle. Quand le "
                "système descend, au contraire, delta Epp est négatif, et "
                "le travail du poids est positif — le système restitue de "
                "l'énergie potentielle, qui se retrouve sous forme "
                "d'énergie cinétique."
            )
        ) as tracker:
            self.play(FadeIn(lecture))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(lecture), FadeOut(theoreme))

        # --- Exemple résolu 1 : la pierre, deux références ---------------------------
        enonce1 = Text(
            _wrap(
                "Exemple 1 : une pierre de masse m=70 g est à 10 m "
                "au-dessus du sol, au bord d'un puits de 15 m de "
                "profondeur. Calculer Epp par rapport au sol, puis par "
                "rapport au fond du puits.",
                width=54,
            ),
            font_size=22,
        )
        enonce1.next_to(titre, DOWN, buff=0.6)

        with self.voiceover(
            text=(
                "Premier exemple. Une pierre de masse 70 grammes se trouve "
                "à 10 mètres au-dessus du sol, juste au bord d'un puits "
                "profond de 15 mètres. On prend g égal à 10 newtons par "
                "kilogramme. Calculons son énergie potentielle de "
                "pesanteur, d'abord par rapport au sol, puis par rapport au "
                "fond du puits."
            )
        ) as tracker:
            self.play(Write(enonce1))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(enonce1))

        calcul1 = example_box(
            VGroup(
                Text("Référence : le sol (z=0 au sol)", font_size=21),
                MathTex(r"E_{pp} = mgz = 0{,}070 \times 10 \times 10 = 7\ \text{J}", font_size=25),
                Text("Référence : le fond du puits (z=0 au fond)", font_size=21),
                MathTex(
                    r"z = 10+15 = 25\ \text{m} \; \Rightarrow \; E_{pp} = 0{,}070 \times 10 \times 25 = 17{,}5\ \text{J}",
                    font_size=24,
                ),
            ).arrange(DOWN, buff=0.3),
            box_width=11.4,
        )
        calcul1.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Par rapport au sol, l'altitude de la pierre est de 10 "
                "mètres, donc Epp vaut 0 virgule 070 fois 10 fois 10, soit "
                "7 joules. Par rapport au fond du puits, l'altitude de la "
                "pierre devient 10 plus 15, soit 25 mètres, ce qui donne "
                "Epp égale 0 virgule 070 fois 10 fois 25, soit 17 virgule 5 "
                "joules. La valeur numérique change bel et bien avec la "
                "référence choisie."
            )
        ) as tracker:
            self.play(FadeIn(calcul1))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(calcul1))

        conclusion1 = example_box(
            VGroup(
                Text("Variation de Epp entre le sol et la pierre M :", font_size=21),
                MathTex(r"\text{Référence sol : } \Delta E_{pp} = 7 - 0 = 7\ \text{J}", font_size=23),
                MathTex(r"\text{Référence puits : } \Delta E_{pp} = 17{,}5 - 10{,}5 = 7\ \text{J}", font_size=23),
                Text("La variation ne dépend pas de la référence choisie !", font_size=22, color=YELLOW),
            ).arrange(DOWN, buff=0.28),
            box_width=11.6,
        )
        conclusion1.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Regardons maintenant la variation d'énergie potentielle "
                "entre le sol et la position M de la pierre. Avec la "
                "référence au sol, cette variation vaut 7 moins 0, soit 7 "
                "joules. Avec la référence au fond du puits, l'énergie "
                "potentielle du sol vaut cette fois 10 virgule 5 joules, et "
                "la variation vaut 17 virgule 5 moins 10 virgule 5, soit "
                "encore 7 joules. On retrouve exactement la même valeur : "
                "la variation d'énergie potentielle ne dépend jamais de la "
                "référence choisie, contrairement à sa valeur brute."
            )
        ) as tracker:
            self.play(FadeIn(conclusion1))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(conclusion1))

        # --- Exemple résolu 2 : la grue à Abidjan --------------------------------------
        enonce2 = Text(
            _wrap(
                "Exemple 2 : à Abidjan, une grue soulève un sac de ciment "
                "de 50 kg d'une hauteur de 12 m. Calculer ΔEpp puis le "
                "travail du poids.",
                width=54,
            ),
            font_size=22,
        )
        enonce2.next_to(titre, DOWN, buff=0.7)

        with self.voiceover(
            text=(
                "Second exemple, sur un chantier à Abidjan. Une grue "
                "soulève un sac de ciment de 50 kilogrammes sur une hauteur "
                "de 12 mètres. Calculons la variation d'énergie potentielle "
                "de pesanteur, puis le travail du poids correspondant."
            )
        ) as tracker:
            self.play(Write(enonce2))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(enonce2))

        calcul2 = example_box(
            VGroup(
                MathTex(
                    r"\Delta E_{pp} = mg\,(z_B - z_A) = 50 \times 10 \times 12 = 6000\ \text{J}",
                    font_size=27,
                ),
                MathTex(
                    r"W_{A \to B}(\vec{P}) = -\Delta E_{pp} = -6000\ \text{J}",
                    font_size=27,
                ),
                Text(
                    "Le poids résiste à la montée : travail résistant.",
                    font_size=21,
                ),
            ).arrange(DOWN, buff=0.3),
            box_width=11.2,
        )
        calcul2.next_to(titre, DOWN, buff=0.6)

        with self.voiceover(
            text=(
                "La variation d'énergie potentielle vaut m g fois z indice "
                "B moins z indice A, soit 50 fois 10 fois 12, c'est-à-dire "
                "6000 joules : le sac emmagasine de l'énergie potentielle "
                "en montant. Le travail du poids, opposé de cette "
                "variation, vaut donc moins 6000 joules : le poids exerce "
                "un travail résistant, puisqu'il s'oppose à la montée du "
                "sac de ciment."
            )
        ) as tracker:
            self.play(FadeIn(calcul2))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(calcul2))

        # --- À retenir -------------------------------------------------------------------
        retenir = essentiel_box(
            Text(
                _wrap(
                    "ΔEpp = mg(zB−zA) = −W(poids). Montée : ΔEpp>0, "
                    "W(poids)<0, énergie emmagasinée. Descente : ΔEpp<0, "
                    "W(poids)>0, énergie restituée. La variation ne dépend "
                    "jamais de la référence, contrairement à Epp elle-même.",
                    width=56,
                ),
                font_size=21,
            )
        )
        retenir.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "À retenir : delta Epp égale m g fois z indice B moins z "
                "indice A, ce qui vaut aussi moins le travail du poids. À "
                "la montée, delta Epp est positif et le poids fournit un "
                "travail résistant : le système emmagasine de l'énergie. À "
                "la descente, c'est l'inverse : le système restitue de "
                "l'énergie. Et surtout, cette variation ne dépend jamais de "
                "la référence choisie, contrairement à la valeur de Epp "
                "elle-même."
            )
        ) as tracker:
            self.play(FadeIn(retenir))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(titre), FadeOut(retenir))
