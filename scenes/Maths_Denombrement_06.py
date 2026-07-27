"""
scenes/Maths_Denombrement_06.py — Chapitre 6 « Dénombrement » (1ereC, Maths),
scène 06.

§ Arrangements : mise en situation (nombres à 3 chiffres distincts),
définition, théorème du nombre d'arrangements Aₙᵖ=n(n-1)...(n-p+1) avec
démonstration (arbre de choix à p niveaux). Exemple résolu 4 (podium de 3
athlètes parmi 10, A³₁₀=720). Propriété admise du nombre d'injections.
Source : 1ereC/Maths.pdf, chapitre 6, pages 71-72.
"""

import textwrap

from manim import DOWN, UP, FadeIn, FadeOut, MathTex, Text, VGroup, Write

from shapes.base_scene import NotionScene
from shapes.boxes import definition_box, property_box, scene_title, theorem_box


def _wrap(text: str, width: int = 54) -> str:
    return "\n".join(textwrap.fill(line, width=width) for line in text.split("\n"))


class Arrangements(NotionScene):
    def construct(self):
        titre = scene_title("Dénombrement — Arrangements")
        titre.scale(0.5)
        titre.to_edge(UP)

        # --- Énoncé : mise en situation --------------------------------------
        mise_en_situation = Text(
            _wrap(
                "Combien de nombres à 3 chiffres DISTINCTS peut-on former "
                "avec les chiffres 1, 2, 3, 4, 5 (chaque chiffre utilisé "
                "au plus une fois) ? Ici, contrairement aux p-listes, un "
                "chiffre ne peut plus se répéter.",
                width=54,
            ),
            font_size=23,
        )
        mise_en_situation.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Voici une nouvelle question : combien de nombres à 3 "
                "chiffres distincts peut-on former avec les chiffres 1, 2, "
                "3, 4, 5, chaque chiffre étant utilisé au plus une fois ? "
                "Cette fois, contrairement aux p-listes du chapitre "
                "précédent, un même chiffre ne peut plus se répéter : nous "
                "avons besoin d'un nouvel outil, l'arrangement."
            )
        ) as tracker:
            self.play(Write(titre))
            self.play(FadeIn(mise_en_situation))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(mise_en_situation))

        # --- Définition ---------------------------------------------------------
        definition = definition_box(
            VGroup(
                Text("Arrangement de p éléments parmi n", font_size=23, weight="BOLD"),
                Text(
                    _wrap(
                        "Un arrangement de p éléments d'un ensemble E à n "
                        "éléments (p ≤ n) est une p-liste d'éléments DEUX À "
                        "DEUX DISTINCTS de E.",
                        width=48,
                    ),
                    font_size=22,
                ),
            ).arrange(DOWN, buff=0.25),
        )
        definition.next_to(titre, DOWN, buff=0.45)

        with self.voiceover(
            text=(
                "Un arrangement de p éléments d'un ensemble E à n "
                "éléments, avec p inférieur ou égal à n, est une p-liste "
                "d'éléments de E deux à deux distincts. C'est donc une "
                "p-liste ordonnée, mais sans répétition."
            )
        ) as tracker:
            self.play(FadeIn(definition))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(definition))

        # --- Raisonnement : théorème + démonstration ------------------------------
        theo = theorem_box(
            VGroup(
                Text("Nombre d'arrangements", font_size=23, weight="BOLD"),
                MathTex(
                    r"A_n^{p} = n(n-1)(n-2)\cdots(n-p+1) \quad (p \text{ facteurs})",
                    font_size=26,
                ),
            ).arrange(DOWN, buff=0.25),
        )
        theo.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Le nombre d'arrangements de p éléments parmi n se note "
                "A indice n, exposant p, et vaut n fois n moins 1, fois n "
                "moins 2, et ainsi de suite, jusqu'à n moins p plus 1 : un "
                "produit de p facteurs qui décroissent d'une unité à "
                "chaque fois."
            )
        ) as tracker:
            self.play(FadeIn(theo))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(theo))

        demo1 = MathTex(
            r"\text{Arbre de choix à } p \text{ niveaux, un niveau par position}",
            font_size=23,
        )
        demo2 = MathTex(
            r"\text{Position 1: } n \text{ choix} \quad \text{Position 2: } (n-1) \text{ choix (1 déjà pris)}",
            font_size=22,
        )
        demo3 = MathTex(
            r"\text{Position 3: } (n-2) \text{ choix} \quad \cdots \quad \text{Position } p: (n-p+1) \text{ choix}",
            font_size=22,
        )
        demo4 = MathTex(
            r"A_n^p = n \times (n-1) \times (n-2) \times \cdots \times (n-p+1)",
            font_size=25,
            color="#DE7C1F",
        )
        demo = VGroup(demo1, demo2, demo3, demo4).arrange(DOWN, buff=0.32)
        demo.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Démontrons ce résultat à l'aide d'un arbre de choix à p "
                "niveaux, un niveau par position de la liste. À la "
                "première position, il y a n choix possibles. À la "
                "seconde, un élément a déjà été utilisé, il ne reste donc "
                "que n moins 1 choix. À la troisième position, n moins 2 "
                "choix, et ainsi de suite, jusqu'à la position p, où il "
                "reste n moins p plus 1 choix. Le principe multiplicatif "
                "donne alors le produit annoncé."
            )
        ) as tracker:
            self.play(Write(demo1))
            self.play(Write(demo2))
            self.play(Write(demo3))
            self.play(Write(demo4))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(demo))

        # --- Exemple traité : podium ----------------------------------------------
        enonce_podium = Text(
            _wrap(
                "Exemple résolu 4 : une course rassemble 10 athlètes. "
                "Combien de podiums différents (1ᵉʳ, 2ᵉ, 3ᵉ) peut-on "
                "former ?",
                width=54,
            ),
            font_size=23,
        )
        enonce_podium.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Illustrons avec un exemple résolu. Une course rassemble "
                "10 athlètes. Combien de podiums différents, c'est-à-dire "
                "de classements pour la première, la deuxième et la "
                "troisième place, peut-on former ?"
            )
        ) as tracker:
            self.play(FadeIn(enonce_podium))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(enonce_podium))

        calcul_podium = MathTex(
            r"A_{10}^{3} = 10 \times 9 \times 8 = 720 \text{ podiums possibles}",
            font_size=27,
            color="#DE7C1F",
        )
        calcul_podium.next_to(titre, DOWN, buff=0.6)

        with self.voiceover(
            text=(
                "Un podium est un arrangement de 3 athlètes parmi 10, "
                "puisque l'ordre compte (première, deuxième, troisième "
                "place) et qu'un même athlète ne peut occuper deux places "
                "à la fois. On calcule A indice 10, exposant 3, égale 10 "
                "fois 9 fois 8, soit 720 podiums possibles."
            )
        ) as tracker:
            self.play(Write(calcul_podium))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(calcul_podium))

        # --- À retenir : propriété admise des injections ---------------------------
        prop_injections = property_box(
            VGroup(
                Text("Nombre d'injections (admise)", font_size=23, weight="BOLD"),
                MathTex(
                    r"\mathrm{Card}(E)=p,\ \ \mathrm{Card}(F)=n,\ \ p \le n \ \Longrightarrow\ "
                    r"\text{nombre d'injections de } E \text{ vers } F \ = \ A_n^{p}",
                    font_size=22,
                ),
                Text(
                    _wrap(
                        "Une injection envoie des éléments distincts de E vers des "
                        "images distinctes dans F : c'est un arrangement de p "
                        "éléments de F.",
                        width=48,
                    ),
                    font_size=21,
                ),
            ).arrange(DOWN, buff=0.25),
        )
        prop_injections.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "À retenir, une dernière propriété, admise : si E a p "
                "éléments et F a n éléments, avec p inférieur ou égal à n, "
                "le nombre d'injections de E vers F vaut A indice n, "
                "exposant p. En effet, une injection associe à chaque "
                "élément de E une image dans F, toutes ces images étant "
                "distinctes : c'est exactement un arrangement de p "
                "éléments choisis dans F."
            )
        ) as tracker:
            self.play(FadeIn(prop_injections))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(prop_injections), FadeOut(titre))
