"""
scenes/Maths_Denombrement_07.py — Chapitre 6 « Dénombrement » (1ereC, Maths),
scène 07.

§ Factorielle n! (définition, exemples, n!=n×(n-1)!). Propriété
Aₙᵖ=n!/(n-p)! avec démonstration. Définition de la permutation, théorème
du nombre de permutations = n! avec démonstration. Définition de
l'anagramme, exemple résolu 5 (AFRIQUE, 7!=5040). Piège des lettres
répétées (BAOBAB, 6!/(3!×2!)=60).
Source : 1ereC/Maths.pdf, chapitre 6, pages 72-73.
"""

import textwrap

from manim import DOWN, UP, FadeIn, FadeOut, MathTex, Text, VGroup, Write, YELLOW

from shapes.base_scene import NotionScene
from shapes.boxes import definition_box, property_box, scene_title, theorem_box, warning_box


def _wrap(text: str, width: int = 54) -> str:
    return "\n".join(textwrap.fill(line, width=width) for line in text.split("\n"))


class FactorielleEtPermutations(NotionScene):
    def construct(self):
        titre = scene_title("Dénombrement — Factorielle, permutations, anagrammes")
        titre.scale(0.5)
        titre.to_edge(UP)

        # --- Énoncé : définition de la factorielle -------------------------------
        def_fact = definition_box(
            VGroup(
                Text("Factorielle d'un entier n", font_size=23, weight="BOLD"),
                MathTex(r"n! = n \times (n-1) \times (n-2) \times \cdots \times 2 \times 1", font_size=26),
                MathTex(r"\text{par convention : } 0! = 1", font_size=24),
            ).arrange(DOWN, buff=0.25),
        )
        def_fact.next_to(titre, DOWN, buff=0.45)

        with self.voiceover(
            text=(
                "Introduisons la factorielle, notation incontournable de "
                "ce chapitre. Pour un entier n, n factorielle, noté n "
                "point d'exclamation, est le produit de tous les entiers "
                "de n jusqu'à 1. Par convention, 0 factorielle vaut 1."
            )
        ) as tracker:
            self.play(Write(titre))
            self.play(FadeIn(def_fact))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(def_fact))

        exemples_fact = MathTex(
            r"1!=1 \quad 2!=2 \quad 3!=6 \quad 4!=24 \quad 5!=120 \quad 6!=720",
            font_size=23,
        )
        exemples_fact.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Voici les premières valeurs : 1 factorielle égale 1, 2 "
                "factorielle égale 2, 3 factorielle égale 6, 4 factorielle "
                "égale 24, 5 factorielle égale 120, et 6 factorielle égale "
                "720. On voit que ces valeurs augmentent très rapidement."
            )
        ) as tracker:
            self.play(Write(exemples_fact))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(exemples_fact))

        prop_recurrence = property_box(
            VGroup(
                MathTex(r"n! = n \times (n-1)!", font_size=27),
            ),
        )
        prop_recurrence.next_to(titre, DOWN, buff=0.45)

        with self.voiceover(
            text=(
                "Une propriété très utile pour calculer ou simplifier : n "
                "factorielle est égal à n fois n moins 1 factorielle. "
                "Cette relation permet, par exemple, de retrouver 6 "
                "factorielle à partir de 5 factorielle, sans tout "
                "recalculer."
            )
        ) as tracker:
            self.play(FadeIn(prop_recurrence))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(prop_recurrence))

        # --- Raisonnement : Aₙᵖ = n!/(n-p)! ---------------------------------------
        prop_anp = property_box(
            VGroup(
                Text("Arrangement en fonction de la factorielle", font_size=22, weight="BOLD"),
                MathTex(r"A_n^{p} = \dfrac{n!}{(n-p)!}", font_size=28),
            ).arrange(DOWN, buff=0.25),
        )
        prop_anp.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "La factorielle permet de réécrire le nombre "
                "d'arrangements de façon compacte : A indice n, exposant "
                "p, est égal à n factorielle sur n moins p factorielle."
            )
        ) as tracker:
            self.play(FadeIn(prop_anp))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(prop_anp))

        demo_anp1 = MathTex(
            r"A_n^p = n(n-1)\cdots(n-p+1)",
            font_size=24,
        )
        demo_anp2 = MathTex(
            r"= \dfrac{n(n-1)\cdots(n-p+1)\ \times\ (n-p)(n-p-1)\cdots 1}{(n-p)(n-p-1)\cdots 1}",
            font_size=21,
        )
        demo_anp3 = MathTex(r"= \dfrac{n!}{(n-p)!}", font_size=26, color=YELLOW)
        demo_anp = VGroup(demo_anp1, demo_anp2, demo_anp3).arrange(DOWN, buff=0.32)
        demo_anp.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Démonstration : on part du produit de p facteurs "
                "décroissants qui définit A-n-p. On multiplie et on "
                "divise par les facteurs manquants, de n moins p jusqu'à "
                "1, sans changer la valeur puisqu'on multiplie et divise "
                "par la même quantité. Le numérateur devient alors n "
                "factorielle tout entier, et le dénominateur, n moins p "
                "factorielle : on retrouve bien la formule."
            )
        ) as tracker:
            self.play(Write(demo_anp1))
            self.play(Write(demo_anp2))
            self.play(Write(demo_anp3))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(demo_anp))

        # --- Permutations -----------------------------------------------------------
        def_permutation = definition_box(
            VGroup(
                Text("Permutation d'un ensemble à n éléments", font_size=22, weight="BOLD"),
                Text(
                    _wrap(
                        "Une permutation de E est un arrangement des n éléments "
                        "de E : c'est le cas particulier p=n (on range TOUS les "
                        "éléments, dans un ordre donné).",
                        width=48,
                    ),
                    font_size=21,
                ),
            ).arrange(DOWN, buff=0.25),
        )
        def_permutation.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Cas particulier fondamental : la permutation. Une "
                "permutation d'un ensemble E à n éléments est un "
                "arrangement de tous les éléments de E, c'est-à-dire le "
                "cas particulier où p est égal à n : on range tous les "
                "éléments, dans un ordre donné."
            )
        ) as tracker:
            self.play(FadeIn(def_permutation))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(def_permutation))

        theo_permutation = theorem_box(
            VGroup(
                Text("Nombre de permutations", font_size=23, weight="BOLD"),
                MathTex(
                    r"\text{nombre de permutations de } E \ = \ A_n^n = \dfrac{n!}{0!} = n!",
                    font_size=26,
                ),
            ).arrange(DOWN, buff=0.25),
        )
        theo_permutation.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Le nombre de permutations d'un ensemble à n éléments vaut "
                "donc A indice n, exposant n, c'est-à-dire n factorielle "
                "sur 0 factorielle, soit tout simplement n factorielle, "
                "puisque 0 factorielle vaut 1."
            )
        ) as tracker:
            self.play(FadeIn(theo_permutation))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(theo_permutation))

        # --- Exemple traité : anagrammes ---------------------------------------------
        def_anagramme = definition_box(
            VGroup(
                Text("Anagramme", font_size=23, weight="BOLD"),
                Text(
                    _wrap("Un anagramme d'un mot est un réarrangement de TOUTES ses lettres.", width=44),
                    font_size=22,
                ),
            ).arrange(DOWN, buff=0.25),
        )
        def_anagramme.next_to(titre, DOWN, buff=0.45)

        with self.voiceover(
            text=(
                "Application très visuelle des permutations : les "
                "anagrammes. Un anagramme d'un mot est un réarrangement de "
                "toutes ses lettres."
            )
        ) as tracker:
            self.play(FadeIn(def_anagramme))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(def_anagramme))

        calcul_afrique = MathTex(
            r"\text{AFRIQUE : 7 lettres toutes distinctes} \ \Rightarrow\ 7! = 5040 \text{ anagrammes}",
            font_size=25,
            color="#DE7C1F",
        )
        calcul_afrique.next_to(titre, DOWN, buff=0.6)

        with self.voiceover(
            text=(
                "Exemple résolu : le mot AFRIQUE comporte 7 lettres, "
                "toutes distinctes. Le nombre de ses anagrammes est donc "
                "7 factorielle, soit 5040."
            )
        ) as tracker:
            self.play(Write(calcul_afrique))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(calcul_afrique))

        # --- Piège à éviter : lettres répétées -----------------------------------------
        piege = warning_box(
            VGroup(
                Text("Piège : lettres répétées", font_size=23, weight="BOLD"),
                Text(
                    _wrap(
                        "Si des lettres se répètent, il faut DIVISER par la "
                        "factorielle du nombre de répétitions de chaque lettre, "
                        "sinon on compte plusieurs fois les mêmes mots.",
                        width=50,
                    ),
                    font_size=21,
                ),
                MathTex(
                    r"\text{BAOBAB : B}\times 3,\ \text{A}\times 2,\ \text{O}\times 1 \ \Rightarrow\ "
                    r"\dfrac{6!}{3!\times 2!} = \dfrac{720}{12} = 60 \text{ anagrammes}",
                    font_size=22,
                ),
            ).arrange(DOWN, buff=0.25),
        )
        piege.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Attention au piège classique des lettres répétées ! Si "
                "une lettre apparaît plusieurs fois, échanger ses copies "
                "entre elles ne change pas le mot obtenu : il faut donc "
                "diviser par la factorielle du nombre de répétitions de "
                "chaque lettre, sinon on compte plusieurs fois les mêmes "
                "mots. Exemple : le mot BAOBAB compte 6 lettres, avec B "
                "répété 3 fois et A répété 2 fois. Le nombre d'anagrammes "
                "distincts vaut donc 6 factorielle, divisé par 3 "
                "factorielle fois 2 factorielle, soit 720 sur 12, c'est-à-"
                "dire 60 anagrammes, et non 720."
            )
        ) as tracker:
            self.play(FadeIn(piege))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(piege), FadeOut(titre))
