"""
scenes/Physique_Condensateur_06.py — Chapitre 9 « Le condensateur »
(1ereC, Physique), scène 06.

§ 4a. Association de condensateurs en parallèle. Montage (armatures de
même signe reliées, même tension u aux bornes de chaque condensateur).
Démonstration q=q1+q2=(C1+C2)u. Théorème C_éq=C1+C2 (généralisation à n
condensateurs). C_éq est toujours supérieure à la plus grande des
capacités.
Exemple résolu 4 : C1=1 µF, C2=2,2 µF, C3=4,7 µF, u=9 V → C_éq=7,9 µF,
q=71,1 µC, charges individuelles q1=9 µC, q2=19,8 µC, q3=42,3 µC.
Source : 1ereC/Physique.pdf, pages 88-98 (chapitre 9, § 4a).
"""

import textwrap

from manim import DOWN, LEFT, RIGHT, UP, WHITE, YELLOW, FadeIn, FadeOut, Line, MathTex, Text, VGroup, Write

from shapes.base_scene import NotionScene
from shapes.boxes import essentiel_box, example_box, scene_title, theorem_box, warning_box


def _wrap(text: str, width: int = 56) -> str:
    return "\n".join(textwrap.fill(line, width=width) for line in text.split("\n"))


def _condensateur_symbole(pos, label=""):
    """Petit symbole de condensateur (deux traits verticaux) centré en
    `pos`, avec une étiquette optionnelle en dessous."""
    p1 = Line(UP * 0.28, DOWN * 0.28, stroke_width=5, color=WHITE).shift(pos + LEFT * 0.08)
    p2 = Line(UP * 0.28, DOWN * 0.28, stroke_width=5, color=WHITE).shift(pos + RIGHT * 0.08)
    group = VGroup(p1, p2)
    if label:
        txt = Text(label, font_size=18, color=YELLOW).next_to(group, DOWN, buff=0.12)
        group.add(txt)
    return group


def _montage_parallele():
    """Deux condensateurs en parallèle : mêmes deux nœuds A (haut) et B
    (bas), reliés par deux branches verticales."""
    haut = UP * 1.0
    bas = DOWN * 1.0
    fil_haut = Line(LEFT * 1.6 + haut, RIGHT * 1.6 + haut, stroke_width=3, color=WHITE)
    fil_bas = Line(LEFT * 1.6 + bas, RIGHT * 1.6 + bas, stroke_width=3, color=WHITE)

    branche1 = VGroup(
        Line(LEFT * 0.8 + haut, LEFT * 0.8 + UP * 0.28, stroke_width=3, color=WHITE),
        _condensateur_symbole(LEFT * 0.8, "C1"),
        Line(LEFT * 0.8 + DOWN * 0.28, LEFT * 0.8 + bas, stroke_width=3, color=WHITE),
    )
    branche2 = VGroup(
        Line(RIGHT * 0.8 + haut, RIGHT * 0.8 + UP * 0.28, stroke_width=3, color=WHITE),
        _condensateur_symbole(RIGHT * 0.8, "C2"),
        Line(RIGHT * 0.8 + DOWN * 0.28, RIGHT * 0.8 + bas, stroke_width=3, color=WHITE),
    )

    label_a = Text("A", font_size=20, color=YELLOW).next_to(fil_haut, UP, buff=0.1)
    label_b = Text("B", font_size=20, color=YELLOW).next_to(fil_bas, DOWN, buff=0.1)

    return VGroup(fil_haut, fil_bas, branche1, branche2, label_a, label_b)


class AssociationParallele(NotionScene):
    def construct(self):
        titre = scene_title("Association de condensateurs en parallèle")
        titre.scale(0.44)
        titre.to_edge(UP)

        # --- Énoncé -------------------------------------------------------
        mise_en_situation = Text(
            _wrap(
                "On souhaite parfois combiner plusieurs condensateurs pour "
                "obtenir une capacité différente. Premier cas : les "
                "condensateurs sont montés en PARALLÈLE, entre les deux "
                "mêmes nœuds du circuit.",
                width=56,
            ),
            font_size=23,
        )
        mise_en_situation.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "On souhaite parfois combiner plusieurs condensateurs pour "
                "obtenir une capacité différente. Premier cas : les "
                "condensateurs sont montés en parallèle, c'est-à-dire "
                "reliés entre les deux mêmes nœuds du circuit."
            )
        ) as tracker:
            self.play(Write(titre))
            self.play(FadeIn(mise_en_situation))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(mise_en_situation))

        # --- Raisonnement : montage + démonstration ----------------------------
        montage = _montage_parallele()
        montage.scale(1.15)
        montage.next_to(titre, DOWN, buff=0.55)

        with self.voiceover(
            text=(
                "Voici le montage : les deux condensateurs C un et C deux "
                "sont reliés aux mêmes nœuds A et B. Ils supportent donc "
                "TOUS LES DEUX exactement la même tension u, celle du "
                "générateur."
            )
        ) as tracker:
            self.play(FadeIn(montage))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(montage))

        demonstration = VGroup(
            Text("La charge totale fournie par le générateur se répartit :", font_size=20),
            MathTex(r"q = q_1 + q_2 = C_1 u + C_2 u = (C_1 + C_2)\, u", font_size=28),
            Text("On identifie cette expression à q = C_éq · u :", font_size=20),
        ).arrange(DOWN, buff=0.22)
        demonstration.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "La charge totale fournie par le générateur se répartit "
                "entre les deux condensateurs : q égale q un plus q deux, "
                "soit C un u plus C deux u, c'est-à-dire C un plus C deux, "
                "le tout multiplié par u. En identifiant cette expression à "
                "q égale C équivalent fois u, on obtient la capacité "
                "équivalente du groupement."
            )
        ) as tracker:
            self.play(FadeIn(demonstration))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(demonstration))

        # --- Théorème --------------------------------------------------------------
        theoreme = theorem_box(
            VGroup(
                Text("Association en PARALLÈLE (n condensateurs)", font_size=22, weight="BOLD"),
                MathTex(r"C_{\text{éq}} = C_1 + C_2 + \dots + C_n", font_size=30),
                Text("La capacité équivalente est TOUJOURS supérieure à la plus", font_size=19),
                Text("grande des capacités du groupement.", font_size=19),
            ).arrange(DOWN, buff=0.2),
            box_width=11.4,
        )
        theoreme.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "En parallèle, la capacité équivalente d'un groupement de n "
                "condensateurs est simplement la somme des capacités : C "
                "équivalent égale C un plus C deux, et ainsi de suite "
                "jusqu'à C n. Elle est donc toujours supérieure à la plus "
                "grande des capacités du groupement."
            )
        ) as tracker:
            self.play(FadeIn(theoreme))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(theoreme))

        # --- Exemple résolu 4 ------------------------------------------------------
        exemple = example_box(
            VGroup(
                Text("C1 = 1 µF, C2 = 2,2 µF, C3 = 4,7 µF en parallèle, u = 9 V.", font_size=19),
                MathTex(r"C_{\text{éq}} = 1 + 2{,}2 + 4{,}7 = 7{,}9\ \mu\text{F}", font_size=24),
                MathTex(r"q = C_{\text{éq}}\, u = 7{,}9 \times 9 = 71{,}1\ \mu\text{C}", font_size=24),
                MathTex(r"q_1 = 9\ \mu\text{C}, \quad q_2 = 19{,}8\ \mu\text{C}, \quad q_3 = 42{,}3\ \mu\text{C}", font_size=22),
            ).arrange(DOWN, buff=0.2),
            box_width=12.2,
        )
        exemple.next_to(titre, DOWN, buff=0.35)

        with self.voiceover(
            text=(
                "Exemple résolu : trois condensateurs, un microfarad, deux "
                "virgule deux microfarads, quatre virgule sept "
                "microfarads, sont associés en parallèle sous neuf volts. "
                "La capacité équivalente vaut sept virgule neuf "
                "microfarads. La charge totale fournie vaut soixante et "
                "onze virgule un microcoulombs, qui se répartit en neuf, "
                "dix-neuf virgule huit, et quarante-deux virgule trois "
                "microcoulombs sur chaque condensateur, chacun étant sous "
                "la même tension de neuf volts."
            )
        ) as tracker:
            self.play(FadeIn(exemple))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(exemple))

        # --- À retenir -------------------------------------------------------------
        retenir = essentiel_box(
            VGroup(
                Text("À retenir", font_size=24, weight="BOLD"),
                MathTex(r"C_{\text{éq}} = C_1 + C_2 + \dots + C_n", font_size=28),
                Text("Même tension u sur chaque condensateur ; C_éq > toutes les Ci.", font_size=20),
            ).arrange(DOWN, buff=0.22),
            box_width=11.6,
        )
        retenir.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Retenons l'essentiel : en parallèle, C équivalent égale la "
                "somme des capacités. Chaque condensateur supporte la même "
                "tension u, et la capacité équivalente est toujours "
                "supérieure à chacune des capacités du groupement."
            )
        ) as tracker:
            self.play(FadeIn(retenir))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(retenir))

        # --- Pièges à éviter --------------------------------------------------------
        pieges = warning_box(
            VGroup(
                Text("• En parallèle, les capacités s'ADDITIONNENT directement —", font_size=20),
                Text("   contrairement aux résistances, qui s'additionnent en série.", font_size=20),
                Text("• Vérifier que les armatures reliées sont bien de MÊME SIGNE", font_size=20),
                Text("   (même potentiel), sinon le montage n'est pas parallèle.", font_size=20),
            ).arrange(DOWN, aligned_edge=LEFT, buff=0.16),
            box_width=12.2,
        )
        pieges.next_to(titre, DOWN, buff=0.35)

        with self.voiceover(
            text=(
                "Deux pièges à éviter. En parallèle, les capacités "
                "s'additionnent directement, contrairement aux "
                "résistances, qui elles s'additionnent en série : c'est "
                "l'inverse de ce que l'on connaît pour les résistors. Et il "
                "faut vérifier que les armatures reliées entre elles sont "
                "bien de même signe, c'est-à-dire au même potentiel, sinon "
                "le montage n'est pas un véritable parallèle."
            )
        ) as tracker:
            self.play(FadeIn(pieges))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(pieges), FadeOut(titre))
