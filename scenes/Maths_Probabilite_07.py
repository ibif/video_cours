"""
scenes/Maths_Probabilite_07.py — Chapitre 12 « Probabilité » (1ereC, Maths),
scène 07.

§ Arbres de choix et tableaux à double entrée : méthode de l'arbre de
choix (chemins = issues, principe multiplicatif le long des branches),
méthode du tableau à double entrée (ex. deux dés). Exemple résolu 1
(arbre) : urne 3 rouges / 2 vertes, tirage AVEC remise de 2 boules,
P(même couleur) = 13/25 (RR:9/25 + VV:4/25). Exemple résolu 2
(tableau) : deux dés, P(S=7) = 6/36 = 1/6, tableau 6×6 complet. Piège
souligné : les 11 sommes possibles de deux dés ne sont PAS
équiprobables — l'univers équiprobable est l'ensemble des 36 couples.
Source : 1ereC/Maths.pdf, chapitre 12, pages 149-150.
"""

import textwrap

from manim import DOWN, LEFT, RIGHT, UP, WHITE, YELLOW, Dot, FadeIn, FadeOut, Line, MathTex, Table, Text, VGroup, Write

from shapes.base_scene import NotionScene
from shapes.boxes import example_box, method_box, scene_title, warning_box


def _wrap(text: str, width: int = 54) -> str:
    return "\n".join(textwrap.fill(line, width=width) for line in text.split("\n"))


def _arbre_2_niveaux() -> VGroup:
    """
    Arbre pondéré à 2 niveaux : urne 3 rouges / 2 vertes, tirage AVEC
    remise de 2 boules. Racine -> R (3/5) / V (2/5) -> R (3/5) / V (2/5).
    """
    racine = Dot(UP * 2.2, radius=0.05, color=WHITE)

    # Niveau 1
    n1_R = Dot(racine.get_center() + DOWN * 1.1 + LEFT * 2.2, radius=0.05, color=WHITE)
    n1_V = Dot(racine.get_center() + DOWN * 1.1 + RIGHT * 2.2, radius=0.05, color=WHITE)

    # Niveau 2 (sous chaque nœud de niveau 1)
    n2_RR = Dot(n1_R.get_center() + DOWN * 1.1 + LEFT * 0.9, radius=0.05, color=WHITE)
    n2_RV = Dot(n1_R.get_center() + DOWN * 1.1 + RIGHT * 0.9, radius=0.05, color=WHITE)
    n2_VR = Dot(n1_V.get_center() + DOWN * 1.1 + LEFT * 0.9, radius=0.05, color=WHITE)
    n2_VV = Dot(n1_V.get_center() + DOWN * 1.1 + RIGHT * 0.9, radius=0.05, color=WHITE)

    branches_niv1 = VGroup(
        Line(racine.get_center(), n1_R.get_center(), color=WHITE),
        Line(racine.get_center(), n1_V.get_center(), color=WHITE),
    )
    branches_niv2 = VGroup(
        Line(n1_R.get_center(), n2_RR.get_center(), color=WHITE),
        Line(n1_R.get_center(), n2_RV.get_center(), color=WHITE),
        Line(n1_V.get_center(), n2_VR.get_center(), color=WHITE),
        Line(n1_V.get_center(), n2_VV.get_center(), color=WHITE),
    )

    label_R1 = MathTex(r"\tfrac{3}{5}\ R", font_size=20, color="#B42E41").move_to(
        (racine.get_center() + n1_R.get_center()) / 2 + LEFT * 0.35
    )
    label_V1 = MathTex(r"\tfrac{2}{5}\ V", font_size=20, color="#267540").move_to(
        (racine.get_center() + n1_V.get_center()) / 2 + RIGHT * 0.35
    )
    label_RR = MathTex(r"\tfrac{3}{5}\ R", font_size=18, color="#B42E41").move_to(
        (n1_R.get_center() + n2_RR.get_center()) / 2 + LEFT * 0.28
    )
    label_RV = MathTex(r"\tfrac{2}{5}\ V", font_size=18, color="#267540").move_to(
        (n1_R.get_center() + n2_RV.get_center()) / 2 + RIGHT * 0.28
    )
    label_VR = MathTex(r"\tfrac{3}{5}\ R", font_size=18, color="#B42E41").move_to(
        (n1_V.get_center() + n2_VR.get_center()) / 2 + LEFT * 0.28
    )
    label_VV = MathTex(r"\tfrac{2}{5}\ V", font_size=18, color="#267540").move_to(
        (n1_V.get_center() + n2_VV.get_center()) / 2 + RIGHT * 0.28
    )

    feuille_RR = MathTex(r"RR:\ \tfrac{9}{25}", font_size=18).next_to(n2_RR, DOWN, buff=0.12)
    feuille_RV = MathTex(r"RV:\ \tfrac{6}{25}", font_size=18).next_to(n2_RV, DOWN, buff=0.12)
    feuille_VR = MathTex(r"VR:\ \tfrac{6}{25}", font_size=18).next_to(n2_VR, DOWN, buff=0.12)
    feuille_VV = MathTex(r"VV:\ \tfrac{4}{25}", font_size=18).next_to(n2_VV, DOWN, buff=0.12)

    return VGroup(
        branches_niv1, branches_niv2,
        racine, n1_R, n1_V, n2_RR, n2_RV, n2_VR, n2_VV,
        label_R1, label_V1, label_RR, label_RV, label_VR, label_VV,
        feuille_RR, feuille_RV, feuille_VR, feuille_VV,
    )


def _tableau_deux_des() -> Table:
    valeurs = [[str(i + j) for j in range(1, 7)] for i in range(1, 7)]
    table = Table(
        valeurs,
        row_labels=[MathTex(str(i), font_size=18) for i in range(1, 7)],
        col_labels=[MathTex(str(j), font_size=18) for j in range(1, 7)],
        element_to_mobject=MathTex,
        element_to_mobject_config={"font_size": 18},
        line_config={"color": WHITE, "stroke_width": 1},
        include_outer_lines=True,
        v_buff=0.18,
        h_buff=0.3,
    )
    table.get_entries().set_color(WHITE)
    table.get_row_labels().set_color(YELLOW)
    table.get_col_labels().set_color(YELLOW)
    for line in table.get_horizontal_lines():
        line.set_color(WHITE)
    for line in table.get_vertical_lines():
        line.set_color(WHITE)
    return table


class ArbresTableauxDoubleEntree(NotionScene):
    def construct(self):
        titre = scene_title("Probabilité — Arbres et tableaux à double entrée")
        titre.scale(0.5)
        titre.to_edge(UP)

        # --- Énoncé : mise en situation --------------------------------------
        mise_en_situation = Text(
            _wrap(
                "Quand une expérience se déroule en plusieurs étapes "
                "(tirages successifs) ou combine deux expériences "
                "(deux dés), deux outils visuels aident à ne rien "
                "oublier : l'arbre et le tableau.",
                width=56,
            ),
            font_size=23,
        )
        mise_en_situation.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Quand une expérience se déroule en plusieurs étapes, "
                "comme des tirages successifs, ou combine deux "
                "expériences indépendantes, comme deux dés lancés "
                "ensemble, deux outils visuels aident à lister toutes les "
                "issues sans rien oublier : l'arbre de choix, et le "
                "tableau à double entrée."
            )
        ) as tracker:
            self.play(Write(titre))
            self.play(FadeIn(mise_en_situation))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(mise_en_situation))

        # --- Méthode arbre + exemple résolu 1 -----------------------------------
        methode_arbre = method_box(
            VGroup(
                Text("Méthode — Arbre de choix", font_size=21, weight="BOLD"),
                Text(
                    _wrap(
                        "Chaque CHEMIN de la racine à une feuille est une "
                        "issue. Sa probabilité est le PRODUIT des "
                        "probabilités portées par les branches parcourues.",
                        width=44,
                    ),
                    font_size=19,
                ),
            ).arrange(DOWN, buff=0.2),
        )
        methode_arbre.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Dans un arbre de choix, chaque chemin complet, de la "
                "racine jusqu'à une feuille, représente une issue. Sa "
                "probabilité s'obtient en multipliant les probabilités "
                "portées par les branches parcourues le long de ce chemin."
            )
        ) as tracker:
            self.play(FadeIn(methode_arbre))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(methode_arbre))

        enonce1 = Text(
            _wrap(
                "Exemple résolu 1 : une urne contient 3 boules rouges et "
                "2 vertes. On tire une boule, on la remet, puis on en "
                "tire une seconde (tirage AVEC remise). Quelle est la "
                "probabilité d'obtenir deux boules de MÊME couleur ?",
                width=52,
            ),
            font_size=21,
        )
        enonce1.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Exemple résolu 1. Une urne contient 3 boules rouges et 2 "
                "vertes. On tire une boule, on la remet dans l'urne, puis "
                "on en tire une seconde : c'est un tirage avec remise. "
                "Quelle est la probabilité d'obtenir deux boules de même "
                "couleur ?"
            )
        ) as tracker:
            self.play(FadeIn(enonce1))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(enonce1))

        arbre = _arbre_2_niveaux()
        arbre.scale(0.95)
        arbre.next_to(titre, DOWN, buff=0.35)

        with self.voiceover(
            text=(
                "Comme le tirage se fait avec remise, les proportions "
                "restent identiques à chaque tirage : 3 cinquièmes de "
                "rouge, 2 cinquièmes de vert. L'arbre à deux niveaux donne "
                "quatre chemins : rouge-rouge de probabilité 3 cinquièmes "
                "fois 3 cinquièmes, soit 9 vingt-cinquièmes ; "
                "rouge-vert et vert-rouge, chacun 6 vingt-cinquièmes ; et "
                "vert-vert, 4 vingt-cinquièmes."
            )
        ) as tracker:
            self.play(FadeIn(arbre))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(arbre))

        conclusion1 = MathTex(
            r"P(\text{même couleur}) = P(RR) + P(VV) = \dfrac{9}{25} + \dfrac{4}{25} = \dfrac{13}{25}",
            font_size=26,
            color=YELLOW,
        )
        conclusion1.next_to(titre, DOWN, buff=0.6)

        with self.voiceover(
            text=(
                "« Même couleur » correspond aux deux chemins "
                "rouge-rouge et vert-vert, incompatibles entre eux : on "
                "additionne. 9 vingt-cinquièmes plus 4 vingt-cinquièmes, "
                "égale 13 vingt-cinquièmes."
            )
        ) as tracker:
            self.play(Write(conclusion1))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(conclusion1))

        # --- Méthode tableau + exemple résolu 2 ---------------------------------
        methode_tableau = method_box(
            VGroup(
                Text("Méthode — Tableau à double entrée", font_size=21, weight="BOLD"),
                Text(
                    _wrap(
                        "Adapté quand DEUX expériences se combinent : "
                        "lignes = résultats de la 1ère, colonnes = "
                        "résultats de la 2nde, cases = issues du couple.",
                        width=44,
                    ),
                    font_size=19,
                ),
            ).arrange(DOWN, buff=0.2),
        )
        methode_tableau.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Le tableau à double entrée est particulièrement adapté "
                "quand deux expériences se combinent. En ligne, les "
                "résultats de la première expérience ; en colonne, ceux "
                "de la seconde ; et dans chaque case, le résultat associé "
                "au couple."
            )
        ) as tracker:
            self.play(FadeIn(methode_tableau))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(methode_tableau))

        enonce2 = Text(
            _wrap(
                "Exemple résolu 2 : on lance deux dés cubiques équilibrés "
                "et on note S la somme des deux résultats. Quelle est la "
                "probabilité que S=7 ?",
                width=52,
            ),
            font_size=21,
        )
        enonce2.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Exemple résolu 2. On lance deux dés cubiques équilibrés, "
                "et on note S la somme des deux résultats obtenus. Quelle "
                "est la probabilité que S égale 7 ?"
            )
        ) as tracker:
            self.play(FadeIn(enonce2))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(enonce2))

        tableau2 = _tableau_deux_des()
        tableau2.scale(0.62)
        tableau2.next_to(titre, DOWN, buff=0.35)

        with self.voiceover(
            text=(
                "Le tableau à double entrée liste les 36 sommes "
                "possibles, une pour chacun des 36 couples de résultats "
                "des deux dés. On repère la diagonale où la somme vaut 7 : "
                "elle contient exactement 6 cases."
            )
        ) as tracker:
            self.play(FadeIn(tableau2))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(tableau2))

        conclusion2 = MathTex(
            r"\mathrm{Card}(\Omega) = 36 \quad\Rightarrow\quad P(S=7) = \dfrac{6}{36} = \dfrac{1}{6}",
            font_size=27,
            color=YELLOW,
        )
        conclusion2.next_to(titre, DOWN, buff=0.6)

        with self.voiceover(
            text=(
                "L'univers équiprobable est ici l'ensemble des 36 "
                "couples de résultats. La probabilité que S égale 7 vaut "
                "donc 6 trente-sixièmes, soit 1 sixième."
            )
        ) as tracker:
            self.play(Write(conclusion2))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(conclusion2))

        # --- Piège à éviter : les sommes ne sont PAS équiprobables ----------------
        piege = warning_box(
            VGroup(
                Text("Piège — Les 11 sommes NE SONT PAS équiprobables !", font_size=19, weight="BOLD"),
                Text(
                    _wrap(
                        "S va de 2 à 12 : onze valeurs possibles, mais PAS "
                        "la même probabilité chacune (S=7 a 6 chances, "
                        "S=2 n'en a qu'une).",
                        width=46,
                    ),
                    font_size=18,
                ),
                MathTex(
                    r"\text{Univers ÉQUIPROBABLE} = \text{les 36 COUPLES}, \ \text{PAS les 11 sommes}",
                    font_size=19,
                    color=YELLOW,
                ),
            ).arrange(DOWN, buff=0.2),
        )
        piege.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Piège très classique, à souligner absolument : la somme "
                "S peut prendre onze valeurs, de 2 à 12, mais ces onze "
                "valeurs ne sont PAS équiprobables. Il y a six façons "
                "d'obtenir 7, mais une seule d'obtenir 2. L'univers "
                "équiprobable n'est jamais l'ensemble des onze sommes : "
                "c'est toujours l'ensemble des 36 couples de résultats des "
                "deux dés, comme dans le tableau."
            )
        ) as tracker:
            self.play(FadeIn(piege))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(piege), FadeOut(titre))
