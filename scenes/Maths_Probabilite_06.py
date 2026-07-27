"""
scenes/Maths_Probabilite_06.py — Chapitre 12 « Probabilité » (1ereC, Maths),
scène 06.

§ Probabilités et dénombrement : rappel des outils du chapitre
« Dénombrement » (p-uplets nᵖ, arrangements Aₙᵖ, permutations n!,
combinaisons Cₙᵖ) via un tableau situation/formule, principe
multiplicatif, principe additif. Exemple résolu complet : urne de 8
boules (5 rouges, 3 noires), tirage simultané de 3 boules,
P(exactement 2 rouges) = C(5,2)×C(3,1)/C(8,3) = 30/56 = 15/28.
Source : 1ereC/Maths.pdf, chapitre 12, pages 148-149.
"""

import textwrap

from manim import DOWN, RIGHT, UP, WHITE, YELLOW, Dot, FadeIn, FadeOut, MathTex, Text, VGroup, Write

from shapes.base_scene import NotionScene
from shapes.boxes import definition_box, example_box, scene_title, method_box


def _wrap(text: str, width: int = 54) -> str:
    return "\n".join(textwrap.fill(line, width=width) for line in text.split("\n"))


def _urne_boules(rouges: int, noires: int) -> VGroup:
    boules = VGroup()
    for _ in range(rouges):
        boules.add(Dot(radius=0.16, color="#B42E41"))
    for _ in range(noires):
        boules.add(Dot(radius=0.16, color=WHITE))
    boules.arrange(RIGHT, buff=0.2)
    return boules


class ProbabilitesDenombrement(NotionScene):
    def construct(self):
        titre = scene_title("Probabilité — Probabilités et dénombrement")
        titre.scale(0.5)
        titre.to_edge(UP)

        # --- Énoncé : mise en situation --------------------------------------
        mise_en_situation = Text(
            _wrap(
                "Card(A) et Card(Ω) ne se comptent pas toujours à la "
                "main : dès qu'un tirage porte sur plusieurs objets, on "
                "retrouve les outils du chapitre Dénombrement.",
                width=56,
            ),
            font_size=24,
        )
        mise_en_situation.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Card de A et Card de Ω ne se comptent pas toujours à la "
                "main. Dès qu'un tirage porte sur plusieurs objets à la "
                "fois, on retrouve exactement les outils déjà rencontrés "
                "au chapitre précédent, le dénombrement : p-listes, "
                "arrangements, permutations, combinaisons."
            )
        ) as tracker:
            self.play(Write(titre))
            self.play(FadeIn(mise_en_situation))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(mise_en_situation))

        # --- Raisonnement : rappel du tableau situation/formule -----------------
        rappel_titre = Text("Rappel — chapitre Dénombrement", font_size=23, weight="BOLD")
        tableau = VGroup(
            MathTex(r"\text{Ordonné, avec répétition} \ \to\ n^{p} \quad \text{(p-liste)}", font_size=22),
            MathTex(r"\text{Ordonné, sans répétition} \ \to\ A_n^{p} \quad \text{(arrangement)}", font_size=22),
            MathTex(r"\text{Ordonné, } p=n \ \to\ n! \quad \text{(permutation)}", font_size=22),
            MathTex(r"\text{Non ordonné} \ \to\ \binom{n}{p} \quad \text{(combinaison)}", font_size=22),
        ).arrange(DOWN, buff=0.22)
        bloc_rappel = VGroup(rappel_titre, tableau).arrange(DOWN, buff=0.35)
        bloc_rappel.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Petit rappel du chapitre Dénombrement. Pour un tirage "
                "ordonné avec répétitions possibles, on utilise les "
                "p-listes, n puissance p. Pour un tirage ordonné sans "
                "répétition, les arrangements, A-n-p. Quand on ordonne "
                "tous les éléments d'un coup, p égale n, ce sont les "
                "permutations, n factorielle. Et pour un tirage non "
                "ordonné, les combinaisons, n choisir p."
            )
        ) as tracker:
            self.play(Write(rappel_titre))
            self.play(Write(tableau))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(bloc_rappel))

        principes = definition_box(
            VGroup(
                Text("Principes multiplicatif et additif", font_size=22, weight="BOLD"),
                MathTex(r"\text{« ET » (choix indépendants successifs)} \ \to\ \text{on MULTIPLIE}", font_size=21),
                MathTex(r"\text{« OU » (cas qui s'excluent)} \ \to\ \text{on ADDITIONNE}", font_size=21),
            ).arrange(DOWN, buff=0.25),
        )
        principes.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Deux principes complètent la boîte à outils. Le "
                "principe multiplicatif : pour des choix indépendants "
                "réalisés l'un après l'autre, on multiplie les nombres de "
                "possibilités. Le principe additif : pour des cas qui "
                "s'excluent mutuellement, on additionne."
            )
        ) as tracker:
            self.play(FadeIn(principes))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(principes))

        # --- Exemple traité : urne 8 boules, tirage simultané de 3 --------------
        enonce = Text(
            _wrap(
                "Exemple résolu : une urne contient 8 boules "
                "indiscernables, 5 rouges et 3 noires. On en tire "
                "simultanément 3. Quelle est la probabilité d'obtenir "
                "exactement 2 rouges ?",
                width=52,
            ),
            font_size=22,
        )
        enonce.next_to(titre, DOWN, buff=0.5)
        urne = _urne_boules(5, 3)
        urne.next_to(enonce, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Exemple résolu complet. Une urne contient 8 boules "
                "indiscernables au toucher, 5 rouges et 3 noires. On en "
                "tire simultanément 3. Quelle est la probabilité "
                "d'obtenir exactement 2 boules rouges ?"
            )
        ) as tracker:
            self.play(FadeIn(enonce))
            self.play(FadeIn(urne))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(enonce), FadeOut(urne))

        etape1_titre = Text("Étape 1 — Univers : tirage simultané, non ordonné", font_size=20, weight="BOLD")
        etape1 = MathTex(r"\mathrm{Card}(\Omega) = \binom{8}{3} = 56", font_size=25)
        bloc1 = VGroup(etape1_titre, etape1).arrange(DOWN, buff=0.3)
        bloc1.next_to(titre, DOWN, buff=0.45)

        with self.voiceover(
            text=(
                "Étape 1, l'univers. Le tirage est simultané, donc non "
                "ordonné : on choisit 3 boules parmi 8, sans distinction "
                "d'ordre. Card de Ω vaut donc 8 choisir 3, soit 56."
            )
        ) as tracker:
            self.play(Write(etape1_titre))
            self.play(Write(etape1))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(bloc1))

        etape2_titre = Text("Étape 2 — Cas favorables : 2 rouges ET 1 noire", font_size=20, weight="BOLD")
        etape2 = MathTex(
            r"\mathrm{Card}(A) = \binom{5}{2} \times \binom{3}{1} = 10 \times 3 = 30",
            font_size=24,
        )
        bloc2 = VGroup(etape2_titre, etape2).arrange(DOWN, buff=0.3)
        bloc2.next_to(titre, DOWN, buff=0.45)

        with self.voiceover(
            text=(
                "Étape 2, les cas favorables. « Exactement 2 rouges » "
                "signifie 2 rouges ET 1 noire — le mot « et » impose de "
                "multiplier. On choisit 2 rouges parmi les 5 : 5 choisir "
                "2, égale 10. Et 1 noire parmi les 3 : 3 choisir 1, égale "
                "3. Par principe multiplicatif : 10 fois 3, égale 30 cas "
                "favorables."
            )
        ) as tracker:
            self.play(Write(etape2_titre))
            self.play(Write(etape2))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(bloc2))

        etape3_titre = Text("Étape 3 — Probabilité (équiprobabilité du tirage)", font_size=20, weight="BOLD")
        etape3 = MathTex(
            r"P(\text{« exactement 2 rouges »}) = \dfrac{\binom{5}{2}\binom{3}{1}}{\binom{8}{3}} = \dfrac{30}{56} = \dfrac{15}{28}",
            font_size=26,
            color=YELLOW,
        )
        bloc3 = VGroup(etape3_titre, etape3).arrange(DOWN, buff=0.35)
        bloc3.next_to(titre, DOWN, buff=0.45)

        with self.voiceover(
            text=(
                "Étape 3, enfin, la probabilité. Le tirage étant "
                "simultané parmi des boules indiscernables, il y a "
                "équiprobabilité. La probabilité cherchée est donc le "
                "rapport des cardinaux : 30 sur 56, qui se simplifie en "
                "15 vingt-huitièmes."
            )
        ) as tracker:
            self.play(Write(etape3_titre))
            self.play(Write(etape3))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(bloc3))

        # --- À retenir : méthode en 3 étapes -------------------------------------
        methode = method_box(
            VGroup(
                Text("Méthode en 3 étapes", font_size=21, weight="BOLD"),
                Text(
                    _wrap(
                        "1) Identifier le type de tirage → Card(Ω). "
                        "2) Dénombrer les cas favorables avec le bon "
                        "outil. 3) Diviser (si équiprobabilité).",
                        width=46,
                    ),
                    font_size=20,
                ),
            ).arrange(DOWN, buff=0.22),
        )
        methode.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Retenons la méthode en trois étapes, systématique dans "
                "tous ces exercices : un, identifier le type de tirage "
                "pour calculer Card de Ω ; deux, dénombrer les cas "
                "favorables avec le bon outil de dénombrement ; trois, "
                "diviser l'un par l'autre, à condition d'avoir vérifié "
                "l'équiprobabilité."
            )
        ) as tracker:
            self.play(FadeIn(methode))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(methode), FadeOut(titre))
