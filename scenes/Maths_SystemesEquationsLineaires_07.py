"""
scenes/Maths_SystemesEquationsLineaires_07.py — Chapitre 13 « Systèmes
d'équations linéaires dans ℝ² et ℝ³ » (1ereC, Maths), scène 07.

§ Théorème de Cramer 3×3 (D, Dx, Dy, Dz par substitution de colonne),
exemple résolu 8 (D=11, Dx=11, Dy=22, Dz=33 → (1;2;3) par Sarrus),
discussion du nombre de solutions et interprétation géométrique (plans
sécants en un point / plans de droite commune / plans confondus / plans
parallèles).
Source : 1ereC/Maths.pdf, chapitre 13, pages 154-164.
"""

import textwrap

from manim import DOWN, LEFT, UP, FadeIn, FadeOut, MathTex, Text, VGroup, Write, YELLOW

from shapes.base_scene import NotionScene
from shapes.boxes import definition_box, example_box, scene_title, theorem_box, warning_box


def _wrap(text: str, width: int = 56) -> str:
    return "\n".join(textwrap.fill(line, width=width) for line in text.split("\n"))


class Cramer3x3DiscussionGeometrique(NotionScene):
    def construct(self):
        titre = scene_title("Systèmes 3×3 — Formules de Cramer")
        titre.scale(0.5)
        titre.to_edge(UP)
        self.play(Write(titre))

        # --- Énoncé : théorème de Cramer 3×3 --------------------------------------
        theoreme = theorem_box(
            VGroup(
                Text("Théorème de Cramer (3×3)", font_size=23, weight="BOLD"),
                Text(
                    _wrap(
                        "Dx, Dy, Dz : on remplace, dans D, la colonne des "
                        "coefficients de x (resp. y, z) par la colonne des "
                        "seconds membres.",
                        width=48,
                    ),
                    font_size=20,
                ),
                MathTex(
                    r"D \neq 0 \ \Longrightarrow\ \mathcal{S}=\left\{\left(\dfrac{D_x}{D}\,;\,\dfrac{D_y}{D}\,;\,\dfrac{D_z}{D}\right)\right\}",
                    font_size=25,
                    color=YELLOW,
                ),
            ).arrange(DOWN, buff=0.26),
            box_width=12.0,
        )
        theoreme.next_to(titre, DOWN, buff=0.35)

        with self.voiceover(
            text=(
                "Le théorème de Cramer se généralise aux systèmes de trois "
                "équations. On calcule le déterminant D du système, puis "
                "D indice x, D indice y et D indice z, obtenus en "
                "remplaçant respectivement la colonne des coefficients de "
                "x, de y, puis de z, par la colonne des seconds membres. "
                "Si D est non nul, le système admet une unique solution : "
                "x égale D indice x sur D, y égale D indice y sur D, z "
                "égale D indice z sur D."
            )
        ) as tracker:
            self.play(FadeIn(theoreme))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(theoreme))

        # --- Raisonnement : mise en place de l'exemple 8 ----------------------------
        ex8_systeme = MathTex(
            r"\begin{cases} x+2y+z=8 \\ 2x+y+z=7 \\ 7x+7y+z=24 \end{cases}",
            font_size=27,
        )
        ex8_systeme.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Appliquons ces formules à un système complet : x plus deux "
                "y plus z égale huit ; deux x plus y plus z égale sept ; "
                "sept x plus sept y plus z égale vingt-quatre. Calculons "
                "d'abord le déterminant D par la règle de Sarrus."
            )
        ) as tracker:
            self.play(FadeIn(ex8_systeme))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(ex8_systeme))

        # --- Exemple traité 8 : calcul complet de D par Sarrus -----------------------
        sarrus_D = MathTex(
            r"""
            \begin{array}{ccc|cc}
            1 & 2 & 1 & 1 & 2 \\
            2 & 1 & 1 & 2 & 1 \\
            7 & 7 & 1 & 7 & 7
            \end{array}
            """,
            font_size=26,
        )
        sarrus_D_calc = MathTex(
            r"D = (1{\times}1{\times}1+2{\times}1{\times}7+1{\times}2{\times}7) - "
            r"(1{\times}1{\times}7+1{\times}1{\times}7+2{\times}2{\times}1)",
            font_size=19,
        )
        sarrus_D_val = MathTex(r"D = (1+14+14)-(7+7+4) = 29-18 = 11", font_size=24, color=YELLOW)
        ex8_D = VGroup(sarrus_D, sarrus_D_calc, sarrus_D_val).arrange(DOWN, buff=0.25)
        ex8_D_box = example_box(ex8_D, box_width=12.2)
        ex8_D_box.scale(0.82)
        ex8_D_box.next_to(titre, DOWN, buff=0.3)

        with self.voiceover(
            text=(
                "On recopie les deux premières colonnes, puis on additionne "
                "les diagonales descendantes : un fois un fois un, plus "
                "deux fois un fois sept, plus un fois deux fois sept, ce "
                "qui donne un plus quatorze plus quatorze, soit vingt-neuf. "
                "On soustrait les diagonales montantes : un fois un fois "
                "sept, plus un fois un fois sept, plus deux fois deux fois "
                "un, ce qui donne sept plus sept plus quatre, soit "
                "dix-huit. Le déterminant D vaut donc vingt-neuf moins "
                "dix-huit, soit onze, non nul : le système admet une "
                "unique solution."
            )
        ) as tracker:
            self.play(FadeIn(ex8_D_box))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(ex8_D_box))

        # --- Dx, Dy, Dz et solution finale ------------------------------------------
        ex8_Dx = MathTex(
            r"D_x = \begin{vmatrix} 8&2&1\\7&1&1\\24&7&1 \end{vmatrix} = 11"
            r"\ \Longrightarrow\ x=\dfrac{11}{11}=1",
            font_size=22,
        )
        ex8_Dy = MathTex(
            r"D_y = \begin{vmatrix} 1&8&1\\2&7&1\\7&24&1 \end{vmatrix} = 22"
            r"\ \Longrightarrow\ y=\dfrac{22}{11}=2",
            font_size=22,
        )
        ex8_Dz = MathTex(
            r"D_z = \begin{vmatrix} 1&2&8\\2&1&7\\7&7&24 \end{vmatrix} = 33"
            r"\ \Longrightarrow\ z=\dfrac{33}{11}=3",
            font_size=22,
        )
        ex8_concl = MathTex(r"\mathcal{S} = \{(1\,;\,2\,;\,3)\}", font_size=28, color=YELLOW)
        ex8_final = VGroup(ex8_Dx, ex8_Dy, ex8_Dz, ex8_concl).arrange(DOWN, buff=0.28)
        ex8_final_box = example_box(ex8_final, box_width=12.4)
        ex8_final_box.scale(0.82)
        ex8_final_box.next_to(titre, DOWN, buff=0.3)

        with self.voiceover(
            text=(
                "En remplaçant, dans D, la colonne de x par la colonne des "
                "seconds membres huit, sept, vingt-quatre, on trouve, par "
                "le même calcul de Sarrus, D indice x égale onze, donc x "
                "égale un. En remplaçant la colonne de y, on trouve D "
                "indice y égale vingt-deux, donc y égale deux. En "
                "remplaçant la colonne de z, on trouve D indice z égale "
                "trente-trois, donc z égale trois. L'ensemble des solutions "
                "est S égale l'ensemble contenant le triplet un, deux, "
                "trois."
            )
        ) as tracker:
            self.play(FadeIn(ex8_final_box))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(ex8_final_box))

        # --- À retenir : discussion + interprétation géométrique --------------------
        discussion = MathTex(
            r"""
            \begin{array}{|c|c|c|}
            \hline
            \text{Condition} & \text{Solutions} & \text{Plans } (P_1),(P_2),(P_3) \\
            \hline
            D \neq 0 & \text{une seule} & \text{s\'ecants en UN point} \\
            \hline
            D=0,\ \text{Gauss} \to 0=k\neq0 & \text{aucune} & \text{sans point commun} \\
            \hline
            D=0,\ \text{Gauss} \to \text{1 param.} & \text{infinit\'e (droite)} & \text{s\'ecants selon une droite} \\
            \hline
            D=0,\ \text{Gauss} \to 2 \text{ param.} & \text{infinit\'e (plan)} & \text{confondus} \\
            \hline
            \end{array}
            """,
            font_size=17,
        )
        discussion.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Comme dans le plan, D permet de discuter le nombre de "
                "solutions, en s'appuyant si besoin sur le pivot de Gauss "
                "pour aller plus loin quand D est nul. Si D est non nul, il "
                "y a une unique solution : les trois plans représentés par "
                "les équations sont sécants en un seul point, comme les "
                "trois murs et le plafond d'un coin de pièce. Si D est nul "
                "et que le pivot de Gauss conduit à une égalité fausse, il "
                "n'y a aucune solution : les plans n'ont aucun point "
                "commun. Si D est nul et que le pivot conduit à un seul "
                "paramètre, il y a une infinité de solutions alignées sur "
                "une droite : les plans se coupent le long de cette droite "
                "commune. Enfin, si deux paramètres restent libres, les "
                "trois équations décrivent en réalité un seul et même "
                "plan : les plans sont confondus."
            )
        ) as tracker:
            self.play(FadeIn(discussion))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(discussion))

        # --- Piège à éviter --------------------------------------------------------
        piege = warning_box(
            Text(
                "D=0 ne dit PAS combien de solutions il y a (aucune ou une\n"
                "infinité) : il faut toujours continuer avec le pivot de Gauss\n"
                "pour trancher, exactement comme dans la scène précédente.",
                font_size=22,
            ),
            box_width=12.2,
        )
        piege.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Piège fréquent, déjà rencontré pour les systèmes 2×2 : D "
                "égal à zéro ne dit jamais, à lui seul, combien il y a de "
                "solutions. Il faut toujours poursuivre avec le pivot de "
                "Gauss pour trancher entre aucune solution et une infinité, "
                "exactement comme dans la scène précédente."
            )
        ) as tracker:
            self.play(FadeIn(piege))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(piege), FadeOut(titre))
