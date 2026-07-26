"""
scenes/Maths_SuitesNumeriques_13.py — Chapitre 15 « Suites numériques »
(1ereC, Maths), scène 13.

Résolution de problèmes contextualisés (partie 2) : exemple résolu 14
complet (amortissement, coopérative de transport, capital restant dû
arithmétique). Synthèse des méthodes et récapitulatif des pièges du
chapitre.
Source : 1ereC/Maths.pdf, chapitre 15, pages 176-188.
"""

import textwrap

from manim import DOWN, UP, FadeIn, FadeOut, MathTex, Text, VGroup, Write, YELLOW

from shapes.base_scene import NotionScene
from shapes.boxes import essentiel_box, example_box, scene_title, warning_box


def _wrap(text: str, width: int = 58) -> str:
    return "\n".join(textwrap.fill(line, width=width) for line in text.split("\n"))


class ProblemesContextualisesPartie2Synthese(NotionScene):
    def construct(self):
        titre = scene_title("Problèmes contextualisés (suite) et synthèse")
        titre.scale(0.46)
        titre.to_edge(UP)
        self.play(Write(titre))

        # --- Énoncé : exemple résolu 14 ------------------------------------------
        ex14_titre = Text(
            "Exemple 14 — Amortissement d'un prêt (coopérative de transport) :",
            font_size=19,
            color=YELLOW,
            weight="BOLD",
        )
        ex14_titre.next_to(titre, DOWN, buff=0.35)
        ex14_enonce = Text(
            _wrap(
                "Une coopérative emprunte 600 000 F, remboursés en 12 "
                "mensualités égales de capital (50 000 F chacune). Chaque "
                "mois, elle paie en plus un intérêt de 1% sur le capital "
                "encore dû en début de mois.",
                width=62,
            ),
            font_size=19,
        )
        ex14_enonce.next_to(ex14_titre, DOWN, buff=0.25)

        with self.voiceover(
            text=(
                "Exemple complet : une coopérative de transport emprunte "
                "six cent mille francs, remboursés en douze mensualités "
                "égales de capital, chacune de cinquante mille francs. "
                "Chaque mois, elle paie en plus un intérêt d'un pourcent, "
                "calculé sur le capital encore dû en début de mois."
            )
        ) as tracker:
            self.play(FadeIn(ex14_titre))
            self.play(FadeIn(ex14_enonce))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(ex14_titre), FadeOut(ex14_enonce))

        # --- Raisonnement : capital restant dû, suite arithmétique ------------------
        ex14_c1_titre = Text(
            "Capital restant dû Cn, suite arithmétique :",
            font_size=21,
            color=YELLOW,
            weight="BOLD",
        )
        ex14_c1_titre.next_to(titre, DOWN, buff=0.35)
        ex14_c1 = example_box(
            VGroup(
                MathTex(
                    r"C_0 = 600\,000, \quad r=-50\,000 \Longrightarrow C_n = 600\,000-50\,000\,n",
                    font_size=22,
                ),
                MathTex(
                    r"C_{11} = 600\,000-550\,000 = 50\,000, \qquad C_{12}=0 \ (\text{prêt soldé})",
                    font_size=22,
                ),
            ).arrange(DOWN, buff=0.25),
            box_width=11.6,
        )
        ex14_c1.next_to(ex14_c1_titre, DOWN, buff=0.25)

        with self.voiceover(
            text=(
                "Le capital restant dû, noté C indice n, diminue de "
                "cinquante mille francs à chaque mensualité : c'est une "
                "suite arithmétique, de premier terme six cent mille et de "
                "raison moins cinquante mille. On a C indice n égale six "
                "cent mille moins cinquante mille n. Au douzième mois, le "
                "capital restant est nul : le prêt est intégralement "
                "soldé."
            )
        ) as tracker:
            self.play(FadeIn(ex14_c1_titre))
            self.play(FadeIn(ex14_c1))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(ex14_c1_titre), FadeOut(ex14_c1))

        # --- Coût total des intérêts (somme arithmétique) --------------------------
        ex14_c2_titre = Text(
            "Coût total des intérêts, somme des 12 premiers termes de (Cn) :",
            font_size=19,
            color=YELLOW,
            weight="BOLD",
        )
        ex14_c2_titre.next_to(titre, DOWN, buff=0.35)
        ex14_c2 = example_box(
            VGroup(
                MathTex(
                    r"S = C_0+C_1+\cdots+C_{11} = 12\times\dfrac{600\,000+50\,000}{2} = 3\,900\,000",
                    font_size=21,
                ),
                MathTex(
                    r"\text{Intérêts} = 1\%\times S = 0{,}01\times 3\,900\,000 = 39\,000 \text{ F}",
                    font_size=23,
                ),
            ).arrange(DOWN, buff=0.25),
            box_width=11.8,
        )
        ex14_c2.next_to(ex14_c2_titre, DOWN, buff=0.25)

        with self.voiceover(
            text=(
                "Le coût total des intérêts est la somme des intérêts "
                "payés chaque mois, c'est-à-dire un pourcent du capital "
                "restant dû au début de chacun des douze mois, du rang "
                "zéro au rang onze. On calcule d'abord la somme de ces "
                "douze termes, avec la formule de la somme arithmétique : "
                "douze fois la demi-somme du premier et du douzième terme, "
                "ce qui donne trois millions neuf cent mille francs. Le "
                "coût total des intérêts vaut un pourcent de cette somme, "
                "soit trente-neuf mille francs."
            )
        ) as tracker:
            self.play(FadeIn(ex14_c2_titre))
            self.play(FadeIn(ex14_c2))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(ex14_c2_titre), FadeOut(ex14_c2))

        # --- Synthèse des méthodes du chapitre ---------------------------------------
        synthese = essentiel_box(
            VGroup(
                Text("Synthèse des méthodes du chapitre :", font_size=22, weight="BOLD"),
                Text("• Montrer qu'une suite est arithmétique / géométrique : différence ou quotient constant.", font_size=18),
                Text("• Reconnaître le bon modèle : ajout constant / facteur constant / les deux.", font_size=18),
                Text("• Calculer une somme : formule dédiée, bien compter le nombre de termes.", font_size=18),
                Text("• Étudier le sens de variation : différence, quotient (positifs), ou fonction associée.", font_size=18),
                Text("• Déterminer une limite : limites de référence, factorisation par le terme dominant.", font_size=18),
            ).arrange(DOWN, buff=0.15),
            box_width=11.8,
        )
        synthese.next_to(titre, DOWN, buff=0.3)

        with self.voiceover(
            text=(
                "Synthèse des méthodes de ce chapitre : pour montrer "
                "qu'une suite est arithmétique ou géométrique, calculer la "
                "différence ou le quotient de deux termes consécutifs. "
                "Pour reconnaître le bon modèle dans un problème, repérer "
                "s'il y a un ajout constant, une multiplication par un "
                "facteur constant, ou les deux à la fois. Pour calculer "
                "une somme, utiliser la formule dédiée, en comptant "
                "précisément le nombre de termes. Pour le sens de "
                "variation, choisir entre la différence, le quotient si "
                "les termes sont positifs, ou la fonction associée. Et "
                "pour une limite, s'appuyer sur les limites de référence, "
                "en factorisant par le terme dominant en cas de forme "
                "indéterminée."
            )
        ) as tracker:
            self.play(FadeIn(synthese))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(synthese))

        # --- Pièges à éviter : récapitulatif du chapitre -------------------------
        pieges = warning_box(
            VGroup(
                Text("Récapitulatif des pièges du chapitre :", font_size=21, weight="BOLD"),
                Text("• Le quotient un+1/un ne conclut que si TOUS les termes sont strictement positifs.", font_size=17),
                Text("• Dans la somme géométrique, l'exposant est le NOMBRE de termes, pas le dernier indice ;\n  la formule ne s'applique pas si q = 1.", font_size=17),
                Text("• u(n+1) ≠ un + 1 : ne jamais confondre l'indice et la valeur du terme.", font_size=17),
                Text("• Une suite arithmético-géométrique n'est ni arithmétique ni géométrique :\n  toujours passer par la suite auxiliaire (vn).", font_size=17),
            ).arrange(DOWN, buff=0.18),
            box_width=11.8,
        )
        pieges.next_to(titre, DOWN, buff=0.3)

        with self.voiceover(
            text=(
                "Récapitulons les pièges de ce chapitre. La méthode du "
                "quotient ne permet de conclure sur le sens de variation "
                "que si tous les termes de la suite sont strictement "
                "positifs. Dans la formule de la somme géométrique, "
                "l'exposant est toujours le nombre de termes additionnés, "
                "pas le dernier indice, et cette formule ne s'applique "
                "jamais si q vaut un. Il ne faut jamais confondre le terme "
                "d'indice n plus un avec le terme d'indice n, auquel on "
                "ajouterait un. Et une suite arithmético-géométrique n'est "
                "ni arithmétique ni géométrique : il faut toujours passer "
                "par la suite auxiliaire v indice n pour l'étudier "
                "complètement."
            )
        ) as tracker:
            self.play(FadeIn(pieges))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(pieges), FadeOut(titre))
