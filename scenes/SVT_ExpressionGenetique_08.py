"""
scenes/SVT_ExpressionGenetique_08.py — Chapitre 5 (1ereC, SVT), scène 08.

IV.C. Propriétés du code génétique (6 propriétés : triplets, dégénéré,
codon d'initiation AUG, codons stop, lecture sans chevauchement, code
quasi universel) + Exemple résolu 4 (traduire l'ARNm
5'-AUGGGCUUUACCUAA-3').
Source : 1ereC/SVT.pdf, page 49.
"""

import textwrap

from manim import DOWN, LEFT, UP, WHITE, YELLOW, FadeIn, FadeOut, MathTex, Text, VGroup, Write

from shapes.base_scene import NotionScene
from shapes.boxes import example_box, property_box, scene_title


def _wrap(text: str, width: int = 56) -> str:
    return "\n".join(textwrap.fill(line, width=width) for line in text.split("\n"))


def _bullets(items, font_size=20, color=WHITE, width=52):
    lines = VGroup(
        *[Text(f"{i}. {_wrap(it, width=width)}", font_size=font_size, color=color) for i, it in enumerate(items, start=1)]
    )
    lines.arrange(DOWN, aligned_edge=LEFT, buff=0.2)
    return lines


class ProprietesDuCodeGenetique(NotionScene):
    def construct(self):
        titre = scene_title("IV.C — Propriétés du code génétique")
        titre.scale(0.6)
        titre.to_edge(UP)

        with self.voiceover(
            text=(
                "La table du code génétique obéit à six propriétés "
                "importantes, qu'il faut connaître par cœur pour éviter "
                "toute erreur de traduction."
            )
        ) as tracker:
            self.play(Write(titre))
            self.wait(tracker.get_remaining_duration())

        # --- Énoncé + raisonnement : les 6 propriétés ---------------------------
        proprietes = _bullets(
            [
                "Code à triplets : 1 codon = 3 nucléotides = 1 acide aminé.",
                "Code dégénéré : plusieurs codons peuvent coder le même "
                "acide aminé (ex : UUU et UUC codent Phé). Seuls Met (AUG) "
                "et Trp (UGG) n'ont qu'un seul codon.",
                "Codon d'initiation : AUG (Met) marque le début de la "
                "traduction — toute protéine commence par une méthionine.",
                "Codons stop : UAA, UAG, UGA ne codent aucun acide aminé, "
                "ils signalent la fin de la traduction.",
                "Lecture sans chevauchement ni ponctuation : un décalage du "
                "cadre de lecture change toute la protéine.",
                "Code (quasi) universel : le même codon désigne le même "
                "acide aminé chez presque tous les êtres vivants.",
            ],
            font_size=18,
            width=56,
        )
        proprietes.next_to(titre, DOWN, buff=0.45)

        with self.voiceover(
            text=(
                "Un : c'est un code à triplets, un codon égale trois "
                "nucléotides égale un acide aminé. Deux : c'est un code "
                "dégénéré, plusieurs codons peuvent coder le même acide "
                "aminé — par exemple UUU et UUC codent tous deux la "
                "phénylalanine. Seuls la méthionine, codon AUG, et le "
                "tryptophane, codon UGG, ne possèdent qu'un seul codon. "
                "Trois : AUG est le codon d'initiation, il marque le début "
                "de la traduction, si bien que toute protéine commence, au "
                "moment de sa synthèse, par une méthionine. Quatre : les "
                "codons UAA, UAG et UGA sont des codons stop, ils ne codent "
                "aucun acide aminé, ils signalent la fin de la traduction. "
                "Cinq : la lecture se fait sans ponctuation ni "
                "chevauchement — un décalage du cadre de lecture change "
                "toute la protéine, nous y reviendrons avec les mutations. "
                "Six : le code est quasi universel, le même codon désigne "
                "le même acide aminé chez presque tous les êtres vivants, de "
                "la bactérie à l'Homme — c'est une preuve de la parenté de "
                "tous les êtres vivants, et c'est ce qui rend possible le "
                "génie génétique, par exemple faire produire l'insuline "
                "humaine par une bactérie."
            )
        ) as tracker:
            self.play(FadeIn(proprietes))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(proprietes))

        # --- Exemple résolu 4 : traduire un ARNm ---------------------------------
        enonce = MathTex(r"5'\text{-AUGGGCUUUACCUAA-}3'", font_size=28, color=WHITE)
        decoupage = MathTex(r"\text{AUG} \mid \text{GGC} \mid \text{UUU} \mid \text{ACC} \mid \text{UAA}", font_size=26, color=YELLOW)
        traduction = Text("Met — Gly — Phé — Thr — Stop", font_size=24, color="#4FC3F7", weight="BOLD")
        note = Text("La protéine comporte 4 acides aminés ; UAA n'est pas traduit.", font_size=18, color=WHITE)
        calcul = VGroup(enonce, decoupage, traduction, note).arrange(DOWN, buff=0.3)

        exemple = example_box(calcul, box_width=11.5)
        exemple.next_to(titre, DOWN, buff=0.55)

        with self.voiceover(
            text=(
                "Exemple résolu. On donne l'ARN messager : cinq prime, A U G "
                "G G C U U U A C C U A A, trois prime. Découpons en codons à "
                "partir du début : A U G, G G C, U U U, A C C, U A A. "
                "Traduisons chaque codon à l'aide de la table : méthionine, "
                "glycine, phénylalanine, thréonine, stop. La chaîne "
                "polypeptidique synthétisée comporte donc quatre acides "
                "aminés : le codon U A A n'est pas traduit, il arrête "
                "seulement la traduction."
            )
        ) as tracker:
            self.play(FadeIn(exemple))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(exemple))

        # --- À retenir -----------------------------------------------------------
        propriete = property_box(
            Text(
                _wrap(
                    "Le code génétique est un code à triplets, dégénéré, "
                    "quasi universel, avec un codon d'initiation (AUG) et "
                    "trois codons stop (UAA, UAG, UGA) qui ne sont jamais "
                    "traduits en acide aminé.",
                    width=54,
                ),
                font_size=23,
            ),
            box_width=11.8,
        )
        propriete.next_to(titre, DOWN, buff=0.55)

        with self.voiceover(
            text=(
                "Retenons l'essentiel : le code génétique est un code à "
                "triplets, dégénéré, quasi universel, avec un codon "
                "d'initiation, AUG, et trois codons stop, UAA, UAG et UGA, "
                "qui ne sont jamais traduits en acide aminé."
            )
        ) as tracker:
            self.play(FadeIn(propriete))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(titre), FadeOut(propriete))
