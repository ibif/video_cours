"""
scenes/Physique_Condensateur_07.py — Chapitre 9 « Le condensateur »
(1ereC, Physique), scène 07.

§ 4b. Association de condensateurs en série. Montage (bout à bout, même
charge q sur chaque condensateur, tensions qui s'ajoutent u=u1+u2).
Démonstration 1/C_éq=1/C1+1/C2 (généralisation à n condensateurs).
Formule pratique pour deux condensateurs C_éq=C1C2/(C1+C2). C_éq est
toujours inférieure à la plus petite des capacités.
Exemple résolu 5 : C1=4 µF, C2=12 µF, u=24 V → C_éq=3 µF, q=72 µC,
u1=18 V, u2=6 V.
Source : 1ereC/Physique.pdf, pages 88-98 (chapitre 9, § 4b).
"""

import textwrap

from manim import DOWN, LEFT, RIGHT, UP, WHITE, YELLOW, FadeIn, FadeOut, Line, MathTex, Text, VGroup, Write

from shapes.base_scene import NotionScene
from shapes.boxes import essentiel_box, example_box, scene_title, theorem_box, warning_box


def _wrap(text: str, width: int = 56) -> str:
    return "\n".join(textwrap.fill(line, width=width) for line in text.split("\n"))


def _condensateur_symbole(pos, label=""):
    p1 = Line(UP * 0.28, DOWN * 0.28, stroke_width=5, color=WHITE).shift(pos + LEFT * 0.08)
    p2 = Line(UP * 0.28, DOWN * 0.28, stroke_width=5, color=WHITE).shift(pos + RIGHT * 0.08)
    group = VGroup(p1, p2)
    if label:
        txt = Text(label, font_size=18, color=YELLOW).next_to(group, UP, buff=0.12)
        group.add(txt)
    return group


def _montage_serie():
    """Deux condensateurs bout à bout, sur une seule branche horizontale."""
    c1 = _condensateur_symbole(LEFT * 0.8, "C1")
    c2 = _condensateur_symbole(RIGHT * 0.8, "C2")

    fil_1 = Line(LEFT * 2.6, LEFT * 0.8 + LEFT * 0.08, stroke_width=3, color=WHITE)
    fil_milieu = Line(LEFT * 0.8 + RIGHT * 0.08, RIGHT * 0.8 + LEFT * 0.08, stroke_width=3, color=WHITE)
    fil_2 = Line(RIGHT * 0.8 + RIGHT * 0.08, RIGHT * 2.6, stroke_width=3, color=WHITE)

    label_a = Text("A", font_size=18, color=YELLOW).next_to(fil_1.get_start(), UP, buff=0.15)
    label_m = Text("M", font_size=18, color=YELLOW).next_to(fil_milieu, DOWN, buff=0.15)
    label_b = Text("B", font_size=18, color=YELLOW).next_to(fil_2.get_end(), UP, buff=0.15)

    return VGroup(fil_1, fil_milieu, fil_2, c1, c2, label_a, label_m, label_b)


class AssociationSerie(NotionScene):
    def construct(self):
        titre = scene_title("Association de condensateurs en série")
        titre.scale(0.46)
        titre.to_edge(UP)

        # --- Énoncé -------------------------------------------------------
        mise_en_situation = Text(
            _wrap(
                "Second cas de figure : les condensateurs sont montés "
                "BOUT À BOUT, en série, sur une même branche. Comment "
                "calculer, cette fois, la capacité équivalente du "
                "groupement ?",
                width=56,
            ),
            font_size=23,
        )
        mise_en_situation.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Second cas de figure : les condensateurs sont montés bout "
                "à bout, en série, sur une même branche du circuit. "
                "Comment calculer, cette fois, la capacité équivalente du "
                "groupement ?"
            )
        ) as tracker:
            self.play(Write(titre))
            self.play(FadeIn(mise_en_situation))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(mise_en_situation))

        # --- Raisonnement : montage + démonstration ----------------------------
        montage = _montage_serie()
        montage.scale(1.15)
        montage.next_to(titre, DOWN, buff=0.55)

        with self.voiceover(
            text=(
                "Voici le montage : les deux condensateurs C un et C deux "
                "sont placés l'un après l'autre, entre A et B, avec un "
                "point milieu M. En série, tous les condensateurs "
                "traversés portent la MÊME charge q, tandis que les "
                "tensions s'ajoutent : u égale u un plus u deux."
            )
        ) as tracker:
            self.play(FadeIn(montage))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(montage))

        demonstration = VGroup(
            MathTex(r"u = u_1 + u_2 = \dfrac{q}{C_1} + \dfrac{q}{C_2} = q \left( \dfrac{1}{C_1} + \dfrac{1}{C_2} \right)", font_size=27),
            Text("En identifiant à u = q / C_éq, on obtient :", font_size=20),
            MathTex(r"\dfrac{1}{C_{\text{éq}}} = \dfrac{1}{C_1} + \dfrac{1}{C_2}", font_size=30, color=YELLOW),
        ).arrange(DOWN, buff=0.25)
        demonstration.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "La tension totale u égale u un plus u deux, c'est-à-dire q "
                "sur C un plus q sur C deux, soit q multiplié par la somme "
                "de un sur C un et un sur C deux. En identifiant cette "
                "expression à u égale q sur C équivalent, on obtient : un "
                "sur C équivalent égale un sur C un plus un sur C deux."
            )
        ) as tracker:
            self.play(FadeIn(demonstration))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(demonstration))

        # --- Théorème --------------------------------------------------------------
        theoreme = theorem_box(
            VGroup(
                Text("Association en SÉRIE (n condensateurs)", font_size=22, weight="BOLD"),
                MathTex(r"\dfrac{1}{C_{\text{éq}}} = \dfrac{1}{C_1} + \dfrac{1}{C_2} + \dots + \dfrac{1}{C_n}", font_size=28),
                Text("Cas particulier de DEUX condensateurs :", font_size=19),
                MathTex(r"C_{\text{éq}} = \dfrac{C_1 C_2}{C_1 + C_2}", font_size=28),
                Text("La capacité équivalente est TOUJOURS inférieure à la plus", font_size=19),
                Text("petite des capacités du groupement.", font_size=19),
            ).arrange(DOWN, buff=0.18),
            box_width=11.8,
        )
        theoreme.next_to(titre, DOWN, buff=0.45)

        with self.voiceover(
            text=(
                "En série, l'inverse de la capacité équivalente d'un "
                "groupement de n condensateurs est la somme des inverses "
                "des capacités. Pour deux condensateurs seulement, on "
                "dispose d'une formule pratique : C équivalent égale C un "
                "fois C deux, sur C un plus C deux. Dans tous les cas, "
                "cette capacité équivalente est toujours inférieure à la "
                "plus petite des capacités du groupement."
            )
        ) as tracker:
            self.play(FadeIn(theoreme))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(theoreme))

        # --- Exemple résolu 5 ------------------------------------------------------
        exemple = example_box(
            VGroup(
                Text("C1 = 4 µF, C2 = 12 µF en série, sous u = 24 V.", font_size=20),
                MathTex(r"C_{\text{éq}} = \dfrac{C_1 C_2}{C_1 + C_2} = \dfrac{4 \times 12}{4 + 12} = 3\ \mu\text{F}", font_size=25),
                MathTex(r"q = C_{\text{éq}}\, u = 3 \times 24 = 72\ \mu\text{C} \ \ (\text{même charge sur C1 et C2})", font_size=23),
                MathTex(r"u_1 = \dfrac{q}{C_1} = \dfrac{72}{4} = 18\ \text{V}, \qquad u_2 = \dfrac{q}{C_2} = \dfrac{72}{12} = 6\ \text{V}", font_size=23),
            ).arrange(DOWN, buff=0.2),
            box_width=12.4,
        )
        exemple.next_to(titre, DOWN, buff=0.35)

        with self.voiceover(
            text=(
                "Exemple résolu : quatre microfarads et douze microfarads "
                "associés en série sous vingt-quatre volts. La capacité "
                "équivalente vaut C un fois C deux sur C un plus C deux, "
                "soit trois microfarads. La charge commune vaut C "
                "équivalent fois u, soit soixante-douze microcoulombs, "
                "identique sur les deux condensateurs. On en déduit u un "
                "égal dix-huit volts et u deux égal six volts : leur somme "
                "redonne bien les vingt-quatre volts appliqués."
            )
        ) as tracker:
            self.play(FadeIn(exemple))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(exemple))

        # --- À retenir -------------------------------------------------------------
        retenir = essentiel_box(
            VGroup(
                Text("À retenir", font_size=24, weight="BOLD"),
                MathTex(r"\dfrac{1}{C_{\text{éq}}} = \sum \dfrac{1}{C_i}, \qquad C_{\text{éq}} = \dfrac{C_1 C_2}{C_1+C_2}\ (\text{2 condensateurs})", font_size=24),
                Text("Même charge q sur chaque condensateur ; C_éq < toutes les Ci.", font_size=20),
            ).arrange(DOWN, buff=0.22),
            box_width=12.4,
        )
        retenir.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Retenons l'essentiel : en série, l'inverse de C équivalent "
                "égale la somme des inverses, ou C un C deux sur leur somme "
                "pour deux condensateurs. Chaque condensateur porte la même "
                "charge q, et la capacité équivalente est toujours "
                "inférieure à chacune des capacités du groupement."
            )
        ) as tracker:
            self.play(FadeIn(retenir))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(retenir))

        # --- Pièges à éviter --------------------------------------------------------
        pieges = warning_box(
            VGroup(
                Text("• LE piège n°1 du chapitre : les formules SÉRIE / PARALLÈLE", font_size=20),
                Text("   des condensateurs sont INVERSÉES par rapport à celles des", font_size=20),
                Text("   résistors (où R_éq série = somme, parallèle = inverses).", font_size=20),
                Text("• En série, c'est le PLUS PETIT condensateur qui supporte la", font_size=20),
                Text("   PLUS GRANDE tension (voir u1 = 18 V > u2 = 6 V ci-dessus).", font_size=20),
            ).arrange(DOWN, aligned_edge=LEFT, buff=0.16),
            box_width=12.4,
        )
        pieges.next_to(titre, DOWN, buff=0.35)

        with self.voiceover(
            text=(
                "Voici le piège numéro un de tout ce chapitre : pour les "
                "condensateurs, les formules de série et de parallèle sont "
                "inversées par rapport à celles des résistors, où c'est en "
                "série que les résistances s'additionnent directement. Ici, "
                "c'est l'inverse. Deuxième piège : en série, c'est le plus "
                "petit condensateur qui supporte la plus grande tension, "
                "comme on l'a vu avec u un égal dix-huit volts, supérieur à "
                "u deux égal six volts."
            )
        ) as tracker:
            self.play(FadeIn(pieges))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(pieges), FadeOut(titre))
