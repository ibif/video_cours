"""
scenes/Maths_SystemesEquationsLineaires_05.py — Chapitre 13 « Systèmes
d'équations linéaires dans ℝ² et ℝ³ » (1ereC, Maths), scène 05.

§ Système 3×3 : définition, méthode de substitution (exemple résolu 4 →
(2;3;-1)), théorème des opérations élémentaires, méthode du pivot de Gauss
(exemple résolu 5, système triangulaire, remontée → (2;-3;2)).
Source : 1ereC/Maths.pdf, chapitre 13, pages 154-164.
"""

import textwrap

from manim import DOWN, LEFT, UP, FadeIn, FadeOut, MathTex, Text, VGroup, Write, YELLOW

from shapes.base_scene import NotionScene
from shapes.boxes import definition_box, example_box, method_box, scene_title, theorem_box, warning_box


def _wrap(text: str, width: int = 56) -> str:
    return "\n".join(textwrap.fill(line, width=width) for line in text.split("\n"))


class Systeme3x3SubstitutionPivotGauss(NotionScene):
    def construct(self):
        titre = scene_title("Systèmes 3×3 — Substitution, pivot de Gauss")
        titre.scale(0.48)
        titre.to_edge(UP)
        self.play(Write(titre))

        # --- Énoncé : définition ------------------------------------------------
        def_systeme3 = definition_box(
            VGroup(
                Text("Système linéaire de trois équations à trois inconnues", font_size=22, weight="BOLD"),
                MathTex(
                    r"\begin{cases} a_1x+b_1y+c_1z=d_1 \\ a_2x+b_2y+c_2z=d_2 \\ a_3x+b_3y+c_3z=d_3 \end{cases}",
                    font_size=27,
                ),
                Text(
                    _wrap(
                        "Une solution est un TRIPLET (x;y;z) qui vérifie "
                        "les TROIS équations à la fois.",
                        width=48,
                    ),
                    font_size=21,
                ),
            ).arrange(DOWN, buff=0.26),
        )
        def_systeme3.next_to(titre, DOWN, buff=0.35)

        with self.voiceover(
            text=(
                "Un système linéaire de trois équations à trois inconnues "
                "x, y, z s'écrit avec trois lignes, chacune de la forme a x "
                "plus b y plus c z égale d. Une solution est ici un "
                "triplet x, y, z qui vérifie les trois équations à la "
                "fois. Voyons deux méthodes pour le résoudre : la "
                "substitution, déjà connue, et le pivot de Gauss, plus "
                "efficace à trois inconnues."
            )
        ) as tracker:
            self.play(FadeIn(def_systeme3))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(def_systeme3))

        # --- Exemple résolu 4 : substitution ---------------------------------------
        ex4_enonce = MathTex(
            r"\begin{cases} x+y+z=4 \\ 2x-y+3z=-2 \\ x+2y-z=9 \end{cases}",
            font_size=27,
        )
        ex4_isole = MathTex(r"x = 4-y-z \quad (\text{1re \'eq.})", font_size=23)
        ex4_report = MathTex(
            r"2(4-y-z)-y+3z=-2 \;\Rightarrow\; -3y+z=-10", font_size=22,
        )
        ex4_report2 = MathTex(
            r"(4-y-z)+2y-z=9 \;\Rightarrow\; y-2z=5", font_size=22,
        )
        ex4_resol = MathTex(
            r"z=3y-10 \ \text{ dans } \ y-2z=5 \;\Rightarrow\; y=3,\ z=-1", font_size=22, color=YELLOW,
        )
        ex4_x = MathTex(r"x = 4-3-(-1) = 2", font_size=23, color=YELLOW)
        ex4_concl = MathTex(r"\mathcal{S} = \{(2\,;\,3\,;\,-1)\}", font_size=27, color=YELLOW)
        ex4 = VGroup(ex4_enonce, ex4_isole, ex4_report, ex4_report2, ex4_resol, ex4_x, ex4_concl).arrange(
            DOWN, buff=0.2
        )
        ex4_box = example_box(ex4, box_width=11.5)
        ex4_box.scale(0.78)
        ex4_box.next_to(titre, DOWN, buff=0.25)

        with self.voiceover(
            text=(
                "Premier exemple, par substitution. Système : x plus y plus "
                "z égale quatre ; deux x moins y plus trois z égale moins "
                "deux ; x plus deux y moins z égale neuf. On isole x dans "
                "la première équation : x égale quatre moins y moins z. En "
                "reportant dans la deuxième équation, on obtient moins "
                "trois y plus z égale moins dix. En reportant dans la "
                "troisième, on obtient y moins deux z égale cinq. On "
                "résout alors ce sous-système à deux inconnues : y égale "
                "trois, z égale moins un. On revient enfin à x égale quatre "
                "moins trois moins moins un, soit x égale deux. L'ensemble "
                "des solutions est S égale l'ensemble contenant le triplet "
                "deux, trois, moins un."
            )
        ) as tracker:
            self.play(FadeIn(ex4_box))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(ex4_box))

        # --- Raisonnement : opérations élémentaires + pivot de Gauss --------------
        theoreme_ops = theorem_box(
            VGroup(
                Text("Opérations élémentaires (transforment un système", font_size=21, weight="BOLD"),
                Text("équivalent)", font_size=21, weight="BOLD"),
                Text("• Échanger deux équations.", font_size=20),
                Text("• Multiplier une équation par un réel non nul.", font_size=20),
                Text("• Ajouter à une équation un multiple d'une autre.", font_size=20),
            ).arrange(DOWN, aligned_edge=LEFT, buff=0.18),
            box_width=11.5,
        )
        theoreme_ops.next_to(titre, DOWN, buff=0.35)

        with self.voiceover(
            text=(
                "Trois opérations, dites élémentaires, transforment un "
                "système en un système équivalent, c'est-à-dire ayant "
                "exactement le même ensemble de solutions : échanger deux "
                "équations, multiplier une équation par un réel non nul, "
                "ou ajouter à une équation un multiple d'une autre "
                "équation. C'est sur la troisième opération que repose la "
                "méthode du pivot de Gauss."
            )
        ) as tracker:
            self.play(FadeIn(theoreme_ops))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(theoreme_ops))

        methode_gauss = VGroup(
            Text("1. Choisir un pivot (coefficient non nul) sur la 1re ligne.", font_size=21),
            Text("2. Éliminer cette inconnue des lignes suivantes.", font_size=21),
            Text("3. Recommencer sur le sous-système restant (2e pivot).", font_size=21),
            Text("4. Le système devient triangulaire : remonter de la", font_size=21),
            Text("    dernière équation à la première.", font_size=21),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.2)
        methode_gauss_box = method_box(methode_gauss, box_width=11.8)
        methode_gauss_box.next_to(titre, DOWN, buff=0.35)

        with self.voiceover(
            text=(
                "Voici la méthode du pivot de Gauss. On choisit un pivot, "
                "un coefficient non nul, sur la première ligne, et on "
                "l'utilise pour éliminer cette inconnue de toutes les "
                "lignes suivantes. On recommence ensuite sur le "
                "sous-système restant, avec un second pivot. Le système "
                "devient alors triangulaire : chaque ligne contient une "
                "inconnue de moins que la précédente. Il ne reste plus qu'à "
                "remonter, de la dernière équation vers la première, pour "
                "trouver toutes les inconnues."
            )
        ) as tracker:
            self.play(FadeIn(methode_gauss_box))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(methode_gauss_box))

        # --- Exemple résolu 5 : pivot de Gauss ---------------------------------------
        ex5_L = MathTex(
            r"""
            \begin{cases}
            x+y+z=1 & (L_1) \\
            2x-y+z=9 & (L_2) \\
            x+2y-z=-6 & (L_3)
            \end{cases}
            """,
            font_size=25,
        )
        ex5_pivot1 = MathTex(
            r"L_2 \leftarrow L_2-2L_1 : \ -3y-z=7 \qquad L_3 \leftarrow L_3-L_1 : \ y-2z=-7",
            font_size=21,
        )
        ex5_pivot2 = MathTex(
            r"L_3 \leftarrow 3L_3+L_2 : \ -7z=-14 \;\Rightarrow\; z=2",
            font_size=22,
        )
        ex5_remontee = MathTex(
            r"-3y-2=7 \;\Rightarrow\; y=-3 \qquad x=1-(-3)-2=2",
            font_size=22, color=YELLOW,
        )
        ex5_concl = MathTex(r"\mathcal{S} = \{(2\,;\,-3\,;\,2)\}", font_size=27, color=YELLOW)
        ex5 = VGroup(ex5_L, ex5_pivot1, ex5_pivot2, ex5_remontee, ex5_concl).arrange(DOWN, buff=0.25)
        ex5_box = example_box(ex5, box_width=12.2)
        ex5_box.scale(0.82)
        ex5_box.next_to(titre, DOWN, buff=0.3)

        with self.voiceover(
            text=(
                "Second exemple, par le pivot de Gauss. Système : x plus y "
                "plus z égale un, c'est la ligne L1 ; deux x moins y plus z "
                "égale neuf, ligne L2 ; x plus deux y moins z égale moins "
                "six, ligne L3. On prend x de L1 comme pivot : L2 moins "
                "deux fois L1 donne moins trois y moins z égale sept ; L3 "
                "moins L1 donne y moins deux z égale moins sept. On prend "
                "maintenant y comme second pivot : trois fois la nouvelle "
                "L3, plus la nouvelle L2, élimine y et donne moins sept z "
                "égale moins quatorze, donc z égale deux. On remonte : "
                "moins trois y moins deux égale sept donne y égale moins "
                "trois, puis x égale un, moins moins trois, moins deux, "
                "soit x égale deux. L'ensemble des solutions est S égale "
                "l'ensemble contenant le triplet deux, moins trois, deux."
            )
        ) as tracker:
            self.play(FadeIn(ex5_box))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(ex5_box))

        # --- À retenir --------------------------------------------------------------
        retenir = definition_box(
            VGroup(
                Text("À retenir", font_size=23, weight="BOLD"),
                Text(
                    _wrap(
                        "Substitution : pratique si une inconnue a un "
                        "coefficient 1 ou -1. Pivot de Gauss : plus sûr et "
                        "plus systématique dès que le système est plus "
                        "complexe — on triangule, puis on remonte.",
                        width=48,
                    ),
                    font_size=21,
                ),
            ).arrange(DOWN, buff=0.24),
            box_width=11.8,
        )
        retenir.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "À retenir : la substitution reste pratique dès qu'une "
                "inconnue a un coefficient un ou moins un dans une "
                "équation. Le pivot de Gauss, lui, est plus sûr et plus "
                "systématique dès que le système est plus complexe : on "
                "triangule le système étape par étape, puis on remonte "
                "pour trouver toutes les inconnues."
            )
        ) as tracker:
            self.play(FadeIn(retenir))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(retenir))

        # --- Piège à éviter --------------------------------------------------------
        piege = warning_box(
            Text(
                "Au pivot de Gauss, appliquer CHAQUE opération à la ligne\n"
                "ENTIÈRE (tous les termes, y compris le second membre), et\n"
                "réécrire le système complet à chaque étape : mélanger une\n"
                "ancienne et une nouvelle ligne est une erreur fréquente.",
                font_size=21,
            ),
            box_width=12.2,
        )
        piege.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Piège fréquent avec le pivot de Gauss : chaque opération "
                "doit être appliquée à la ligne entière, c'est-à-dire tous "
                "ses termes, y compris le second membre, et il faut "
                "réécrire le système complet à chaque étape. Mélanger une "
                "ancienne ligne avec une nouvelle ligne, en cours de route, "
                "est une erreur très fréquente."
            )
        ) as tracker:
            self.play(FadeIn(piege))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(piege), FadeOut(titre))
