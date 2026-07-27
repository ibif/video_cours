"""
scenes/Maths_Denombrement_09.py — Chapitre 6 « Dénombrement » (1ereC, Maths),
scène 09.

§ Propriétés des coefficients binomiaux : symétrie (n p)=(n n-p) avec 2
démonstrations (calcul + dénombrement), exemple (20 18)=(20 2)=190.
Formule de Pascal (n p)=(n-1 p-1)+(n-1 p) avec démonstration par
dénombrement (élément fixé a). Construction du triangle de Pascal jusqu'à
n=5, méthode de lecture.
Source : 1ereC/Maths.pdf, chapitre 6, pages 75-76.
"""

import textwrap

from manim import DOWN, LEFT, RIGHT, UP, FadeIn, FadeOut, MathTex, Text, VGroup, Write, YELLOW

from shapes.base_scene import NotionScene
from shapes.boxes import property_box, scene_title


def _wrap(text: str, width: int = 54) -> str:
    return "\n".join(textwrap.fill(line, width=width) for line in text.split("\n"))


def _triangle_pascal() -> VGroup:
    """Triangle de Pascal jusqu'à n=5, valeurs numériques déjà calculées."""
    valeurs = [
        [1],
        [1, 1],
        [1, 2, 1],
        [1, 3, 3, 1],
        [1, 4, 6, 4, 1],
        [1, 5, 10, 10, 5, 1],
    ]
    lignes = VGroup()
    for n, ligne in enumerate(valeurs):
        textes = VGroup(*[MathTex(str(v), font_size=24) for v in ligne]).arrange(RIGHT, buff=0.7)
        lignes.add(textes)
    lignes.arrange(DOWN, buff=0.35)
    for ligne in lignes:
        ligne.move_to([0, ligne.get_y(), 0])
    return lignes


class ProprietesCoefficientsTrianglePascal(NotionScene):
    def construct(self):
        titre = scene_title("Dénombrement — Propriétés et triangle de Pascal")
        titre.scale(0.5)
        titre.to_edge(UP)

        # --- Énoncé : propriété de symétrie ----------------------------------------
        prop_symetrie = property_box(
            VGroup(
                Text("Symétrie des coefficients binomiaux", font_size=23, weight="BOLD"),
                MathTex(r"\binom{n}{p} = \binom{n}{n-p}", font_size=28),
            ).arrange(DOWN, buff=0.25),
        )
        prop_symetrie.next_to(titre, DOWN, buff=0.45)

        with self.voiceover(
            text=(
                "Les coefficients binomiaux possèdent des propriétés "
                "remarquables. La première est la symétrie : n choisir p "
                "est toujours égal à n choisir n moins p."
            )
        ) as tracker:
            self.play(Write(titre))
            self.play(FadeIn(prop_symetrie))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(prop_symetrie))

        demo_calcul = MathTex(
            r"\binom{n}{n-p} = \dfrac{n!}{(n-p)!\,\big(n-(n-p)\big)!} = \dfrac{n!}{(n-p)!\,p!} = \binom{n}{p}",
            font_size=22,
        )
        demo_calcul.next_to(titre, DOWN, buff=0.5)
        demo_denombrement = Text(
            _wrap(
                "Par dénombrement : choisir p éléments à GARDER dans E "
                "revient exactement à choisir les n-p éléments à LAISSER "
                "de côté — même sous-ensemble décrit de deux façons.",
                width=52,
            ),
            font_size=22,
        )
        demo_denombrement.next_to(demo_calcul, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Deux démonstrations sont possibles. Par le calcul "
                "d'abord : n choisir n moins p vaut n factorielle sur n "
                "moins p factorielle, fois n moins n moins p factorielle, "
                "ce qui se simplifie en n factorielle sur n moins p "
                "factorielle fois p factorielle, exactement n choisir p. "
                "Par le dénombrement ensuite, sans aucun calcul : choisir "
                "p éléments à garder dans E revient exactement à choisir "
                "les n moins p éléments à laisser de côté. C'est le même "
                "sous-ensemble décrit de deux façons différentes."
            )
        ) as tracker:
            self.play(Write(demo_calcul))
            self.play(FadeIn(demo_denombrement))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(demo_calcul), FadeOut(demo_denombrement))

        exemple_symetrie = MathTex(
            r"\binom{20}{18} = \binom{20}{2} = \dfrac{20\times 19}{2} = 190",
            font_size=27,
            color=YELLOW,
        )
        exemple_symetrie.next_to(titre, DOWN, buff=0.6)

        with self.voiceover(
            text=(
                "Cette symétrie est très utile en pratique : plutôt que "
                "de calculer 20 choisir 18, on préfère calculer 20 "
                "choisir 2, bien plus rapide, égal à 20 fois 19 sur 2, "
                "soit 190."
            )
        ) as tracker:
            self.play(Write(exemple_symetrie))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(exemple_symetrie))

        # --- Raisonnement : formule de Pascal ---------------------------------------
        prop_pascal = property_box(
            VGroup(
                Text("Formule de Pascal", font_size=23, weight="BOLD"),
                MathTex(r"\binom{n}{p} = \binom{n-1}{p-1} + \binom{n-1}{p}", font_size=28),
            ).arrange(DOWN, buff=0.25),
        )
        prop_pascal.next_to(titre, DOWN, buff=0.45)

        with self.voiceover(
            text=(
                "Deuxième propriété fondamentale, la formule de Pascal : "
                "n choisir p est égal à n moins 1 choisir p moins 1, plus "
                "n moins 1 choisir p."
            )
        ) as tracker:
            self.play(FadeIn(prop_pascal))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(prop_pascal))

        demo_pascal1 = MathTex(
            r"\text{On fixe un élément } a \in E,\ \ \mathrm{Card}(E)=n",
            font_size=23,
        )
        demo_pascal2 = MathTex(
            r"\text{Parties à } p \text{ éléments contenant } a : \text{ choisir } p-1 \text{ parmi les } n-1 \text{ restants} \ \to\ \binom{n-1}{p-1}",
            font_size=19,
        )
        demo_pascal3 = MathTex(
            r"\text{Parties à } p \text{ éléments ne contenant PAS } a : \text{ choisir } p \text{ parmi les } n-1 \text{ restants} \ \to\ \binom{n-1}{p}",
            font_size=19,
        )
        demo_pascal4 = MathTex(
            r"\text{Ces deux familles forment une partition des parties à } p \text{ éléments de } E",
            font_size=20,
        )
        demo_pascal5 = MathTex(
            r"\binom{n}{p} = \binom{n-1}{p-1} + \binom{n-1}{p}",
            font_size=25,
            color=YELLOW,
        )
        demo_pascal = VGroup(demo_pascal1, demo_pascal2, demo_pascal3, demo_pascal4, demo_pascal5).arrange(DOWN, buff=0.3)
        demo_pascal.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Démontrons-la par dénombrement. On fixe un élément a de "
                "E, qui a n éléments. Parmi les parties à p éléments de "
                "E, on distingue celles qui contiennent a : en choisir une "
                "revient à choisir les p moins 1 éléments restants parmi "
                "les n moins 1 autres, soit n moins 1 choisir p moins 1 "
                "façons. Et celles qui ne contiennent pas a : en choisir "
                "une revient à choisir p éléments parmi les n moins 1 "
                "autres, soit n moins 1 choisir p façons. Ces deux "
                "familles, disjointes, forment une partition de toutes "
                "les parties à p éléments de E. Par le principe additif, "
                "on obtient la formule de Pascal."
            )
        ) as tracker:
            self.play(Write(demo_pascal1))
            self.play(Write(demo_pascal2))
            self.play(Write(demo_pascal3))
            self.play(Write(demo_pascal4))
            self.play(Write(demo_pascal5))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(demo_pascal))

        # --- Exemple traité : construction du triangle de Pascal --------------------
        soustitre_triangle = Text("Le triangle de Pascal (jusqu'à n=5)", font_size=24, weight="BOLD")
        soustitre_triangle.next_to(titre, DOWN, buff=0.35)

        triangle = _triangle_pascal()
        triangle.scale(0.85)
        triangle.next_to(soustitre_triangle, DOWN, buff=0.4)

        methode_lecture = Text(
            _wrap(
                "Méthode de lecture : chaque nombre est la somme des deux "
                "nombres juste au-dessus de lui (formule de Pascal). La "
                "ligne n donne les valeurs de (n p) pour p allant de 0 à n.",
                width=54,
            ),
            font_size=20,
        )
        methode_lecture.next_to(triangle, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "La formule de Pascal permet de construire, ligne après "
                "ligne, le célèbre triangle de Pascal. Voici les six "
                "premières lignes, de n égale 0 à n égale 5. La méthode "
                "de lecture est simple : chaque nombre est la somme des "
                "deux nombres juste au-dessus de lui, exactement ce que "
                "dit la formule de Pascal. La ligne numéro n donne "
                "directement toutes les valeurs de n choisir p, pour p "
                "allant de 0 à n."
            )
        ) as tracker:
            self.play(Write(soustitre_triangle))
            self.play(Write(triangle))
            self.play(FadeIn(methode_lecture))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(soustitre_triangle), FadeOut(triangle), FadeOut(methode_lecture), FadeOut(titre))
