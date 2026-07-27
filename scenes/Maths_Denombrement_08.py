"""
scenes/Maths_Denombrement_08.py — Chapitre 6 « Dénombrement » (1ereC, Maths),
scène 08.

§ Combinaisons : construction (A={1,2,3,4}, arrangements vs combinaisons),
définition, théorème de la formule (n p)=Aₙᵖ/p!=n!/(p!(n-p)!) avec
démonstration en 2 étapes. Cas particuliers à connaître. Exemple résolu 6
(équipe de 6 parmi 15, (15 6)=5005).
Source : 1ereC/Maths.pdf, chapitre 6, pages 73-75.
"""

import textwrap

from manim import DOWN, UP, FadeIn, FadeOut, MathTex, Text, VGroup, Write, YELLOW

from shapes.base_scene import NotionScene
from shapes.boxes import definition_box, example_box, scene_title, theorem_box


def _wrap(text: str, width: int = 54) -> str:
    return "\n".join(textwrap.fill(line, width=width) for line in text.split("\n"))


class CombinaisonsDefinitionFormule(NotionScene):
    def construct(self):
        titre = scene_title("Dénombrement — Combinaisons")
        titre.scale(0.5)
        titre.to_edge(UP)

        # --- Énoncé : construction, arrangements vs combinaisons ------------
        construction1 = MathTex(
            r"A = \{1,2,3,4\} \quad \text{choisir 2 éléments SANS se soucier de l'ordre}",
            font_size=24,
        )
        construction2 = MathTex(
            r"\text{Arrangements (ordonnés) : } A_4^2 = 12 \ \Rightarrow\ "
            r"(1,2),(2,1),(1,3),(3,1),(1,4),(4,1),\dots",
            font_size=20,
        )
        construction3 = MathTex(
            r"\text{Sous-ensembles (non ordonnés) : } \{1,2\},\{1,3\},\{1,4\},\{2,3\},\{2,4\},\{3,4\}",
            font_size=21,
        )
        construction4 = MathTex(
            r"6 \text{ sous-ensembles, soit } A_4^2 \div 2 \quad (\text{chaque paire comptée 2 fois})",
            font_size=22,
            color=YELLOW,
        )
        construction = VGroup(construction1, construction2, construction3, construction4).arrange(DOWN, buff=0.3)
        construction.next_to(titre, DOWN, buff=0.45)

        with self.voiceover(
            text=(
                "Partons de A égale 1, 2, 3, 4, et choisissons 2 éléments "
                "SANS nous soucier de l'ordre. Les arrangements de 2 "
                "éléments parmi 4 sont au nombre de 12 : ils distinguent "
                "1-2 de 2-1. Mais si l'ordre n'a pas d'importance, ces "
                "deux listes représentent le même sous-ensemble, la paire "
                "1, 2. En regroupant ainsi les listes deux par deux, on "
                "obtient seulement 6 sous-ensembles distincts. C'est "
                "précisément A-4-2 divisé par 2, puisque chaque paire est "
                "comptée exactement deux fois parmi les arrangements."
            )
        ) as tracker:
            self.play(Write(titre))
            self.play(Write(construction1))
            self.play(Write(construction2))
            self.play(Write(construction3))
            self.play(Write(construction4))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(construction))

        # --- Définition -----------------------------------------------------------
        def_combinaison = definition_box(
            VGroup(
                Text("Combinaison de p éléments parmi n", font_size=23, weight="BOLD"),
                Text(
                    _wrap(
                        "Une combinaison de p éléments d'un ensemble E à n "
                        "éléments (p ≤ n) est un SOUS-ENSEMBLE de E à p "
                        "éléments : l'ordre ne compte plus.",
                        width=48,
                    ),
                    font_size=22,
                ),
                MathTex(r"\text{Notation : } \binom{n}{p}", font_size=27),
            ).arrange(DOWN, buff=0.25),
        )
        def_combinaison.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Une combinaison de p éléments d'un ensemble E à n "
                "éléments, avec p inférieur ou égal à n, est un "
                "sous-ensemble de E à p éléments : l'ordre ne compte plus "
                "du tout. On la note n en haut, p en bas, entre "
                "parenthèses, et on lit « p parmi n »."
            )
        ) as tracker:
            self.play(FadeIn(def_combinaison))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(def_combinaison))

        # --- Raisonnement : théorème formule avec démonstration en 2 étapes -------
        theo = theorem_box(
            VGroup(
                Text("Formule des combinaisons", font_size=23, weight="BOLD"),
                MathTex(
                    r"\binom{n}{p} = \dfrac{A_n^p}{p!} = \dfrac{n!}{p!\,(n-p)!}",
                    font_size=28,
                ),
            ).arrange(DOWN, buff=0.25),
        )
        theo.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Voici la formule générale : n choisir p est égal à "
                "A-n-p divisé par p factorielle, ce qui donne aussi n "
                "factorielle, sur p factorielle fois n moins p "
                "factorielle."
            )
        ) as tracker:
            self.play(FadeIn(theo))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(theo))

        demo1 = MathTex(r"\text{Étape 1 — choisir : } \binom{n}{p} \text{ façons de choisir les } p \text{ éléments (sans ordre)}", font_size=21)
        demo2 = MathTex(r"\text{Étape 2 — ordonner : chaque choix peut s'ordonner de } p! \text{ façons}", font_size=21)
        demo3 = MathTex(r"\text{choisir puis ordonner} = \text{arranger : } \ \binom{n}{p} \times p! = A_n^p", font_size=24)
        demo4 = MathTex(r"\Rightarrow\ \binom{n}{p} = \dfrac{A_n^p}{p!} = \dfrac{n!}{p!\,(n-p)!}", font_size=26, color=YELLOW)
        demo = VGroup(demo1, demo2, demo3, demo4).arrange(DOWN, buff=0.32)
        demo.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Démontrons cette formule en deux étapes. Première étape, "
                "choisir : il y a n choisir p façons de sélectionner les p "
                "éléments, sans se soucier de l'ordre. Deuxième étape, "
                "ordonner : chacun de ces choix peut ensuite être ordonné "
                "de p factorielle façons différentes. Or choisir, puis "
                "ordonner, revient exactement à construire un arrangement. "
                "On a donc n choisir p, fois p factorielle, égale A-n-p. "
                "En divisant par p factorielle, on retrouve la formule."
            )
        ) as tracker:
            self.play(Write(demo1))
            self.play(Write(demo2))
            self.play(Write(demo3))
            self.play(Write(demo4))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(demo))

        # --- Cas particuliers à connaître -----------------------------------------
        cas1 = MathTex(r"\binom{n}{0} = 1", font_size=26)
        cas2 = MathTex(r"\binom{n}{n} = 1", font_size=26)
        cas3 = MathTex(r"\binom{n}{1} = n", font_size=26)
        cas4 = MathTex(r"\binom{n}{2} = \dfrac{n(n-1)}{2}", font_size=26)
        cas_titre = Text("Cas particuliers à connaître", font_size=24, weight="BOLD")
        cas_ligne = VGroup(cas1, cas2, cas3, cas4).arrange(DOWN, buff=0.3)
        cas = VGroup(cas_titre, cas_ligne).arrange(DOWN, buff=0.35)
        cas.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Quatre cas particuliers sont à connaître par cœur. n "
                "choisir 0 vaut 1 : il n'y a qu'une façon de ne rien "
                "choisir, le sous-ensemble vide. n choisir n vaut 1 : il "
                "n'y a qu'une façon de tout choisir, E lui-même. n "
                "choisir 1 vaut n : il y a n façons de choisir un seul "
                "élément. Et n choisir 2 vaut n fois n moins 1, le tout "
                "divisé par 2."
            )
        ) as tracker:
            self.play(Write(cas_titre))
            self.play(Write(cas_ligne))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(cas))

        # --- Exemple traité : équipe ------------------------------------------------
        enonce_equipe = Text(
            _wrap(
                "Exemple résolu 6 : un club de basket compte 15 joueurs. "
                "Combien d'équipes de 6 joueurs différentes peut-on "
                "former (sans distinction de poste) ?",
                width=54,
            ),
            font_size=23,
        )
        enonce_equipe.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Terminons par un exemple résolu. Un club de basket "
                "compte 15 joueurs. Combien d'équipes de 6 joueurs "
                "différentes peut-on former, sans distinction de poste ?"
            )
        ) as tracker:
            self.play(FadeIn(enonce_equipe))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(enonce_equipe))

        calcul_equipe = example_box(
            VGroup(
                MathTex(
                    r"\binom{15}{6} = \dfrac{15!}{6!\,9!} = 5005 \text{ équipes possibles}",
                    font_size=26,
                ),
            ),
        )
        calcul_equipe.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Puisque l'ordre des joueurs dans l'équipe n'a pas "
                "d'importance, il s'agit d'une combinaison de 6 joueurs "
                "parmi 15. On calcule 15 choisir 6, égale 15 factorielle "
                "sur 6 factorielle fois 9 factorielle, soit 5005 équipes "
                "possibles."
            )
        ) as tracker:
            self.play(FadeIn(calcul_equipe))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(calcul_equipe), FadeOut(titre))
