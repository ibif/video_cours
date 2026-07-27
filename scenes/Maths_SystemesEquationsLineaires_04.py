"""
scenes/Maths_SystemesEquationsLineaires_04.py — Chapitre 13 « Systèmes
d'équations linéaires dans ℝ² et ℝ³ » (1ereC, Maths), scène 04.

§ Déterminant d'ordre 3 : définition, règle de Sarrus (recopier les deux
premières colonnes, diagonales descendantes +, montantes -), exemple de
calcul complet (D=12), propriétés admises (multiplication d'une ligne,
échange de lignes, combinaison linéaire, lignes proportionnelles).
Source : 1ereC/Maths.pdf, chapitre 13, pages 154-164.
"""

import textwrap

from manim import DOWN, LEFT, RIGHT, UP, FadeIn, FadeOut, MathTex, Text, VGroup, Write, YELLOW

from shapes.base_scene import NotionScene
from shapes.boxes import definition_box, example_box, property_box, scene_title, warning_box


def _wrap(text: str, width: int = 56) -> str:
    return "\n".join(textwrap.fill(line, width=width) for line in text.split("\n"))


class DeterminantOrdre3Sarrus(NotionScene):
    def construct(self):
        titre = scene_title("Déterminant d'ordre 3 — Règle de Sarrus")
        titre.scale(0.5)
        titre.to_edge(UP)
        self.play(Write(titre))

        # --- Énoncé : définition ---------------------------------------------
        def_det3 = definition_box(
            VGroup(
                Text("Déterminant d'une matrice 3×3", font_size=24, weight="BOLD"),
                MathTex(
                    r"D = \begin{vmatrix} a_1 & b_1 & c_1 \\ a_2 & b_2 & c_2 \\ a_3 & b_3 & c_3 \end{vmatrix}",
                    font_size=30,
                ),
                Text(
                    _wrap(
                        "D est un nombre associé à un tableau 3×3 de "
                        "réels ; il jouera pour les systèmes 3×3 le même "
                        "rôle que D pour les systèmes 2×2.",
                        width=48,
                    ),
                    font_size=22,
                ),
            ).arrange(DOWN, buff=0.28),
        )
        def_det3.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Pour préparer les systèmes de trois équations à trois "
                "inconnues, il nous faut d'abord définir le déterminant "
                "d'un tableau de neuf nombres, disposé en trois lignes et "
                "trois colonnes, noté avec deux barres verticales. Ce "
                "nombre D jouera exactement le même rôle que le "
                "déterminant 2×2 : il permettra de résoudre et de discuter "
                "les systèmes de trois équations."
            )
        ) as tracker:
            self.play(FadeIn(def_det3))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(def_det3))

        # --- Raisonnement : règle de Sarrus -------------------------------------
        regle_texte = VGroup(
            Text("1. Recopier les deux premières colonnes à droite du tableau.", font_size=22),
            Text("2. Sommer les produits des 3 diagonales descendantes (signe +).", font_size=22),
            Text("3. Soustraire les produits des 3 diagonales montantes (signe -).", font_size=22),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.25)
        regle_box = property_box(regle_texte, box_width=12.0)
        regle_box.next_to(titre, DOWN, buff=0.35)

        with self.voiceover(
            text=(
                "La règle de Sarrus permet de calculer D uniquement pour un "
                "tableau 3×3 : on recopie les deux premières colonnes à "
                "droite du tableau, ce qui donne cinq colonnes en tout. On "
                "additionne alors les produits des trois diagonales qui "
                "descendent de gauche à droite, avec un signe plus, puis on "
                "soustrait les produits des trois diagonales qui montent de "
                "gauche à droite, avec un signe moins."
            )
        ) as tracker:
            self.play(FadeIn(regle_box))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(regle_box))

        # --- Exemple de calcul complet (D=12) -------------------------------------
        sarrus_tableau = MathTex(
            r"""
            \begin{array}{ccc|cc}
            1 & 2 & 0 & 1 & 2 \\
            0 & 1 & 3 & 0 & 1 \\
            2 & 0 & 0 & 2 & 0
            \end{array}
            """,
            font_size=30,
        )
        sarrus_desc = MathTex(
            r"\text{Descendantes : } 1{\times}1{\times}0 + 2{\times}3{\times}2 + 0{\times}0{\times}0 = 0+12+0=12",
            font_size=22,
        )
        sarrus_asc = MathTex(
            r"\text{Montantes : } 0{\times}1{\times}2 + 1{\times}3{\times}0 + 2{\times}0{\times}0 = 0+0+0=0",
            font_size=22,
        )
        sarrus_concl = MathTex(r"D = 12 - 0 = 12", font_size=28, color=YELLOW)
        sarrus = VGroup(sarrus_tableau, sarrus_desc, sarrus_asc, sarrus_concl).arrange(
            DOWN, buff=0.3
        )
        sarrus_box = example_box(sarrus, box_width=12.2)
        sarrus_box.scale(0.85)
        sarrus_box.next_to(titre, DOWN, buff=0.3)

        with self.voiceover(
            text=(
                "Calculons le déterminant du tableau un, deux, zéro ; zéro, "
                "un, trois ; deux, zéro, zéro. On recopie les deux "
                "premières colonnes à droite. Les trois diagonales "
                "descendantes donnent : un fois un fois zéro, plus deux "
                "fois trois fois deux, plus zéro fois zéro fois zéro, soit "
                "zéro plus douze plus zéro, donc douze. Les trois "
                "diagonales montantes donnent : zéro fois un fois deux, "
                "plus un fois trois fois zéro, plus deux fois zéro fois "
                "zéro, soit zéro dans les trois cas. Le déterminant D vaut "
                "donc douze moins zéro, soit douze."
            )
        ) as tracker:
            self.play(FadeIn(sarrus_box))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(sarrus_box))

        # --- À retenir : propriétés admises --------------------------------------
        proprietes = VGroup(
            Text("1. Multiplier une ligne par k multiplie D par k.", font_size=22),
            Text("2. Échanger deux lignes change le signe de D.", font_size=22),
            Text("3. Ajouter à une ligne une combinaison linéaire des autres", font_size=22),
            Text("    lignes ne change pas D.", font_size=22),
            Text("4. Deux lignes proportionnelles ⟹ D = 0.", font_size=22),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.22)
        proprietes_box = property_box(proprietes, box_width=12.2)
        proprietes_box.next_to(titre, DOWN, buff=0.35)

        with self.voiceover(
            text=(
                "Retenons quatre propriétés admises, très utiles pour "
                "simplifier un calcul de déterminant sans repasser par "
                "Sarrus à chaque fois. Multiplier tous les termes d'une "
                "ligne par un nombre k multiplie D par k. Échanger deux "
                "lignes change le signe de D. Ajouter à une ligne une "
                "combinaison linéaire des autres lignes ne change pas D. "
                "Enfin, si deux lignes sont proportionnelles, D est "
                "automatiquement nul."
            )
        ) as tracker:
            self.play(FadeIn(proprietes_box))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(proprietes_box))

        # --- Piège à éviter --------------------------------------------------------
        piege = warning_box(
            VGroup(
                Text(
                    "La règle de Sarrus ne s'applique QU'à l'ordre 3 (jamais à\n"
                    "un tableau 2×2 ou 4×4). Les diagonales MONTANTES sont\n"
                    "toujours précédées d'un signe moins : un oubli de signe\n"
                    "est l'erreur la plus fréquente.",
                    font_size=22,
                ),
            ).arrange(DOWN, buff=0.2),
            box_width=12.2,
        )
        piege.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Piège fréquent : la règle de Sarrus, avec les colonnes "
                "recopiées, ne fonctionne QUE pour un tableau trois par "
                "trois, jamais pour un deux par deux ni pour un tableau "
                "plus grand. Et surtout, les trois diagonales montantes "
                "sont toujours précédées d'un signe moins : oublier ce "
                "signe est l'erreur la plus fréquente. Si une vérification "
                "ultérieure du système ne tombe pas juste, recalculez "
                "d'abord ce déterminant."
            )
        ) as tracker:
            self.play(FadeIn(piege))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(piege), FadeOut(titre))
