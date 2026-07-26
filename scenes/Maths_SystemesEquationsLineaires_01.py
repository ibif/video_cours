"""
scenes/Maths_SystemesEquationsLineaires_01.py — Chapitre 13 « Systèmes
d'équations linéaires dans ℝ² et ℝ³ » (1ereC, Maths), scène 01.

§ Système linéaire 2×2 : mise en situation, définition (système, solution,
ensemble des solutions 𝒮, systèmes équivalents), méthode de substitution,
exemple résolu 1 (2x-5y=4, x+2y=11 → 𝒮={(7;2)}), à retenir, piège (vérifier
la solution dans LES DEUX équations).
Source : 1ereC/Maths.pdf, chapitre 13, pages 154-164.
"""

import textwrap

from manim import DOWN, LEFT, UP, FadeIn, FadeOut, MathTex, Text, VGroup, Write, YELLOW

from shapes.base_scene import NotionScene
from shapes.boxes import definition_box, example_box, method_box, scene_title, warning_box


def _wrap(text: str, width: int = 56) -> str:
    return "\n".join(textwrap.fill(line, width=width) for line in text.split("\n"))


class SystemeDefinitionSubstitution(NotionScene):
    def construct(self):
        titre = scene_title("Systèmes linéaires 2×2 — Définition, substitution")
        titre.scale(0.5)
        titre.to_edge(UP)

        # --- Énoncé : mise en situation --------------------------------------
        mise_en_situation = Text(
            _wrap(
                "Sur un marché, deux quantités inconnues (par exemple deux "
                "prix) sont liées par deux relations différentes en même "
                "temps. Trouver les deux valeurs qui satisfont les deux "
                "relations à la fois, c'est résoudre un système "
                "d'équations.",
                width=58,
            ),
            font_size=24,
        )
        mise_en_situation.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Imaginons deux quantités inconnues, reliées par deux "
                "relations différentes en même temps : par exemple deux "
                "prix, contraints à la fois par un budget total et par un "
                "rapport entre eux. Trouver les deux valeurs qui vérifient "
                "ces deux relations simultanément, c'est résoudre ce qu'on "
                "appelle un système d'équations. C'est l'objet de ce "
                "chapitre."
            )
        ) as tracker:
            self.play(Write(titre))
            self.play(FadeIn(mise_en_situation))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(mise_en_situation))

        # --- Raisonnement : définitions ---------------------------------------
        def_systeme = definition_box(
            VGroup(
                Text("Système linéaire de deux équations à deux inconnues", font_size=23, weight="BOLD"),
                MathTex(
                    r"\begin{cases} a x + b y = c \\ a' x + b' y = c' \end{cases}"
                    r"\qquad a,b,c,a',b',c' \in \mathbb{R}",
                    font_size=27,
                ),
                Text(
                    _wrap(
                        "Une SOLUTION est un couple (x;y) qui vérifie les "
                        "DEUX équations à la fois. L'ensemble des solutions "
                        "se note 𝒮.",
                        width=48,
                    ),
                    font_size=22,
                ),
            ).arrange(DOWN, buff=0.25),
        )
        def_systeme.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Voici la définition générale. Un système linéaire de deux "
                "équations à deux inconnues x et y s'écrit : a x plus b y "
                "égale c, et a prime x plus b prime y égale c prime, où a, "
                "b, c, a prime, b prime et c prime sont des réels donnés. "
                "Une solution du système est un couple x, y qui vérifie les "
                "deux équations à la fois, pas une seule. L'ensemble de "
                "toutes les solutions se note S calligraphié."
            )
        ) as tracker:
            self.play(FadeIn(def_systeme))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(def_systeme))

        def_equivalents = definition_box(
            VGroup(
                Text("Systèmes équivalents", font_size=23, weight="BOLD"),
                Text(
                    _wrap(
                        "Deux systèmes sont équivalents lorsqu'ils ont "
                        "exactement le même ensemble de solutions 𝒮. "
                        "Résoudre un système, c'est le transformer en un "
                        "système équivalent plus simple.",
                        width=50,
                    ),
                    font_size=22,
                ),
            ).arrange(DOWN, buff=0.25),
        )
        def_equivalents.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Deux systèmes sont dits équivalents lorsqu'ils ont "
                "exactement le même ensemble de solutions S. Toute la "
                "démarche de résolution consiste donc à transformer le "
                "système de départ en un système équivalent, mais plus "
                "simple, jusqu'à pouvoir lire directement la solution."
            )
        ) as tracker:
            self.play(FadeIn(def_equivalents))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(def_equivalents))

        # --- Méthode de substitution -------------------------------------------
        methode = VGroup(
            Text("1. Isoler une inconnue dans l'une des deux équations.", font_size=24),
            Text("2. La remplacer (substituer) dans l'AUTRE équation.", font_size=24),
            Text("3. Résoudre l'équation à une seule inconnue obtenue.", font_size=24),
            Text("4. Revenir à l'expression isolée pour trouver la seconde.", font_size=24),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.28)
        methode_box = method_box(methode, box_width=11.8)
        methode_box.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Voici la méthode de substitution, la plus naturelle. "
                "Première étape : isoler une inconnue dans l'une des deux "
                "équations, de préférence celle dont le coefficient vaut un "
                "ou moins un, pour éviter les fractions. Deuxième étape : "
                "remplacer, c'est-à-dire substituer, cette expression dans "
                "l'autre équation. Troisième étape : résoudre l'équation à "
                "une seule inconnue ainsi obtenue. Quatrième étape : "
                "revenir à l'expression isolée pour trouver la seconde "
                "inconnue."
            )
        ) as tracker:
            self.play(FadeIn(methode_box))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(methode_box))

        # --- Exemple traité 1 ----------------------------------------------------
        ex1_enonce = MathTex(
            r"\begin{cases} 2x - 5y = 4 \\ x + 2y = 11 \end{cases}",
            font_size=30,
        )
        ex1_isole = MathTex(r"x = 11 - 2y \quad \text{(2e équation)}", font_size=27)
        ex1_subst = MathTex(r"2(11-2y) - 5y = 4 \;\Longrightarrow\; 22 - 9y = 4", font_size=27)
        ex1_y = MathTex(r"-9y = -18 \;\Longrightarrow\; y = 2", font_size=28, color=YELLOW)
        ex1_x = MathTex(r"x = 11 - 2\times 2 = 7", font_size=28, color=YELLOW)
        ex1_concl = MathTex(r"\mathcal{S} = \{(7\,;\,2)\}", font_size=30, color=YELLOW)
        ex1 = VGroup(ex1_enonce, ex1_isole, ex1_subst, ex1_y, ex1_x, ex1_concl).arrange(
            DOWN, buff=0.28
        )
        ex1_box = example_box(ex1, box_width=11.5)
        ex1_box.scale(0.85)
        ex1_box.next_to(titre, DOWN, buff=0.3)

        with self.voiceover(
            text=(
                "Appliquons la méthode. Le système est : deux x moins cinq "
                "y égale quatre, et x plus deux y égale onze. Dans la "
                "seconde équation, x a pour coefficient un : on isole donc "
                "x, qui vaut onze moins deux y. On substitue dans la "
                "première équation : deux fois, onze moins deux y, moins "
                "cinq y, égale quatre, ce qui donne vingt-deux moins neuf y "
                "égale quatre. D'où moins neuf y égale moins dix-huit, donc "
                "y égale deux. On revient alors à x égale onze moins deux "
                "fois deux, soit x égale sept. L'ensemble des solutions est "
                "S égale l'ensemble contenant le seul couple sept, deux."
            )
        ) as tracker:
            self.play(FadeIn(ex1_box))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(ex1_box))

        # --- À retenir -----------------------------------------------------------
        retenir = definition_box(
            VGroup(
                Text("À retenir", font_size=24, weight="BOLD"),
                Text(
                    _wrap(
                        "Un système 2×2 se résout par substitution : isoler "
                        "une inconnue, la remplacer dans l'autre équation, "
                        "résoudre, puis revenir en arrière.",
                        width=48,
                    ),
                    font_size=22,
                ),
            ).arrange(DOWN, buff=0.25),
        )
        retenir.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "À retenir : un système de deux équations à deux inconnues "
                "se résout par substitution en isolant une inconnue, en la "
                "remplaçant dans l'autre équation, en résolvant l'équation "
                "obtenue, puis en revenant en arrière pour trouver la "
                "seconde inconnue. Nous verrons dans la scène suivante une "
                "seconde méthode, souvent plus rapide."
            )
        ) as tracker:
            self.play(FadeIn(retenir))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(retenir))

        # --- Piège à éviter --------------------------------------------------------
        piege = warning_box(
            Text(
                "Après résolution, toujours vérifier la solution dans LES DEUX\n"
                "équations de départ, pas une seule : une erreur de calcul\n"
                "n'affecte souvent qu'une seule des deux.",
                font_size=23,
            ),
            box_width=11.8,
        )
        piege.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Piège fréquent : une fois la solution trouvée, il faut "
                "toujours la vérifier dans les deux équations de départ, et "
                "pas seulement dans une seule. Une erreur de calcul "
                "n'affecte souvent qu'une des deux équations : la "
                "vérification complète est le seul moyen sûr de la "
                "détecter."
            )
        ) as tracker:
            self.play(FadeIn(piege))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(piege), FadeOut(titre))
