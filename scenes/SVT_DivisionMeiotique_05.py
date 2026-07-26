"""
scenes/SVT_DivisionMeiotique_05.py — Chapitre 2 (1ereD, SVT), scène 05.

§ 2.3.1 Le brassage interchromosomique : l'assortiment indépendant des
chromosomes homologues (définition, image mentale à 2 paires, propriété
2^n, exemple insecte / être humain / zygotes ≈ 7×10^13).
Source : 1ereD/SVT.pdf, pages 23-24.
"""

import textwrap

from manim import (
    BLUE,
    DOWN,
    LEFT,
    MAROON,
    RIGHT,
    UP,
    WHITE,
    YELLOW,
    Dot,
    FadeIn,
    FadeOut,
    Line,
    MathTex,
    Rectangle,
    Text,
    VGroup,
    Write,
)

from shapes.base_scene import NotionScene
from shapes.boxes import definition_box, example_box, property_box, scene_title


def _wrap(text: str, width: int = 56) -> str:
    return "\n".join(textwrap.fill(line, width=width) for line in text.split("\n"))


def _bullets(items, font_size=22, color=WHITE, width=52):
    lines = VGroup(
        *[Text(f"• {_wrap(it, width=width)}", font_size=font_size, color=color) for it in items]
    )
    lines.arrange(DOWN, aligned_edge=LEFT, buff=0.22)
    return lines


def _chr_double(color, height=0.9, width=0.18, gap=0.06):
    left = Rectangle(width=width, height=height, fill_color=color, fill_opacity=1, stroke_color=WHITE, stroke_width=1)
    right = left.copy()
    paire = VGroup(left, right).arrange(RIGHT, buff=gap)
    dot = Dot(radius=0.045, color=YELLOW)
    dot.move_to(paire.get_center())
    return VGroup(left, right, dot)


class BrassageInterchromosomique(NotionScene):
    def construct(self):
        titre = scene_title("2.3 — Le brassage interchromosomique")
        titre.scale(0.62)
        titre.to_edge(UP)

        # --- Énoncé : retour à la 2ème énigme + définition ---------------------
        intro = Text(
            _wrap(
                "Revenons à la deuxième énigme de la famille d'Adzopé : "
                "pourquoi les trois enfants de Mamadou et Affoué sont-ils "
                "tous différents ? Deux mécanismes de la méiose « mélangent » "
                "les chromosomes et les gènes. Voici le premier.",
                width=56,
            ),
            font_size=24,
            color=WHITE,
        )
        intro.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Revenons à la deuxième énigme de notre activité "
                "d'introduction : pourquoi les trois enfants de Mamadou et "
                "Affoué sont-ils tous différents ? La réponse tient en deux "
                "mécanismes qui ont lieu pendant la méiose et qui mélangent "
                "les chromosomes et les gènes : le brassage "
                "interchromosomique, que nous étudions maintenant, et le "
                "brassage intrachromosomique, vu dans la scène suivante."
            )
        ) as tracker:
            self.play(Write(titre))
            self.play(FadeIn(intro))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(intro))

        definition = definition_box(
            Text(
                _wrap(
                    "En métaphase I, l'orientation de chaque bivalent est "
                    "indépendante de celle des autres bivalents et relève du "
                    "hasard. En anaphase I, les homologues d'origine "
                    "paternelle et maternelle se répartissent donc au hasard "
                    "entre les cellules filles : c'est le brassage "
                    "interchromosomique (entre chromosomes différents).",
                    width=54,
                ),
                font_size=22,
            ),
            box_width=11.8,
        )
        definition.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "En métaphase I, l'orientation de chaque bivalent au plan "
                "équatorial est indépendante de celle des autres bivalents et "
                "relève du hasard. En anaphase I, les homologues d'origine "
                "paternelle et maternelle se répartissent donc au hasard "
                "entre les cellules filles, selon de très nombreuses "
                "combinaisons possibles : c'est le brassage "
                "interchromosomique, entre chromosomes différents."
            )
        ) as tracker:
            self.play(FadeIn(definition))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(definition))

        # --- Animation du raisonnement : image mentale à 2 paires ---------------
        sous_titre = Text("Image mentale : 2 paires d'homologues", font_size=24, color=YELLOW, weight="BOLD")
        sous_titre.next_to(titre, DOWN, buff=0.45)

        def _disposition(long_left_color, court_left_color):
            plan = Line(LEFT * 1.3, RIGHT * 1.3, color=YELLOW)
            long_g = _chr_double(long_left_color, height=1.0)
            court_g = _chr_double(court_left_color, height=0.6)
            gauche = VGroup(long_g, court_g).arrange(DOWN, buff=0.15).move_to(LEFT * 0.8)
            autre_couleur_long = MAROON if long_left_color == BLUE else BLUE
            autre_couleur_court = MAROON if court_left_color == BLUE else BLUE
            long_d = _chr_double(autre_couleur_long, height=1.0)
            court_d = _chr_double(autre_couleur_court, height=0.6)
            droite = VGroup(long_d, court_d).arrange(DOWN, buff=0.15).move_to(RIGHT * 0.8)
            return VGroup(plan, gauche, droite)

        disp_a = _disposition(BLUE, BLUE)
        label_a = Text("Disposition A", font_size=18, color=WHITE)
        bloc_a = VGroup(disp_a, label_a).arrange(DOWN, buff=0.2)

        disp_b = _disposition(BLUE, MAROON)
        label_b = Text("Disposition B", font_size=18, color=WHITE)
        bloc_b = VGroup(disp_b, label_b).arrange(DOWN, buff=0.2)

        dispositions = VGroup(bloc_a, bloc_b).arrange(RIGHT, buff=1.4)
        dispositions.next_to(sous_titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Imagine deux paires d'homologues : une paire de longs "
                "chromosomes et une paire de courts, en bleu l'origine "
                "paternelle, en bordeaux l'origine maternelle. En métaphase "
                "I, deux dispositions sont possibles. Disposition A : le "
                "long paternel et le court paternel migrent vers le même "
                "pôle. Disposition B : le long paternel part avec le court "
                "maternel. Chaque nouvelle paire de chromosomes multiplie "
                "par deux le nombre de combinaisons possibles."
            )
        ) as tracker:
            self.play(FadeIn(sous_titre))
            self.play(FadeIn(bloc_a))
            self.play(FadeIn(bloc_b))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(sous_titre), FadeOut(dispositions))

        # --- Propriété : 2^n types de gamètes -----------------------------------
        propriete = property_box(
            Text(
                _wrap(
                    "Pour une espèce de formule 2n (soit n paires "
                    "d'homologues), le nombre de combinaisons "
                    "chromosomiques possibles dans les gamètes, par le seul "
                    "assortiment indépendant, est 2^n.",
                    width=52,
                ),
                font_size=23,
            ),
            box_width=11.5,
        )
        propriete.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "On peut généraliser : pour une espèce de formule deux n, "
                "soit n paires d'homologues, le nombre de combinaisons "
                "chromosomiques possibles dans les gamètes, par le seul "
                "assortiment indépendant, est deux puissance n."
            )
        ) as tracker:
            self.play(FadeIn(propriete))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(propriete))

        # --- Exemple traité : insecte, être humain, zygotes ----------------------
        exemple = example_box(
            Text(
                _wrap(
                    "Insecte 2n=6 (n=3) -> 2^3=8 types de gamètes. Être "
                    "humain 2n=46 (n=23) -> 2^23=8 388 608 types de "
                    "spermatozoïdes, et autant d'ovules. Zygotes possibles "
                    "pour un couple : 2^23×2^23=2^46 ≈ 7,0×10^13, soit "
                    "environ 70 000 milliards de combinaisons.",
                    width=54,
                ),
                font_size=21,
            ),
            box_width=12.2,
        )
        exemple.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Chez l'insecte de formule deux n égale six, n égale trois "
                "paires, donc deux puissance trois égale huit types de "
                "gamètes différents. Chez l'être humain, deux n égale "
                "quarante-six, n égale vingt-trois paires, donc deux "
                "puissance vingt-trois égale huit millions trois cent "
                "quatre-vingt-huit mille six cent huit types de "
                "spermatozoïdes possibles pour un même homme, et autant "
                "d'ovules possibles pour une même femme. Un zygote résulte "
                "de la rencontre de deux gamètes : deux puissance vingt-trois "
                "fois deux puissance vingt-trois égale deux puissance "
                "quarante-six, soit environ soixante-dix mille milliards de "
                "combinaisons possibles. C'est pourquoi, sauf pour de vrais "
                "jumeaux, deux enfants des mêmes parents ne sont jamais "
                "identiques."
            )
        ) as tracker:
            self.play(FadeIn(exemple))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(exemple))

        # --- À retenir --------------------------------------------------------------
        formule_zygote = MathTex(
            r"2^{23} \times 2^{23} = 2^{46} \approx 7{,}0 \times 10^{13}",
            font_size=32,
            color=WHITE,
        )
        legende = Text("≈ 70 000 milliards de zygotes différents possibles", font_size=22, color=YELLOW)
        bloc_final = VGroup(formule_zygote, legende).arrange(DOWN, buff=0.35)
        bloc_final.next_to(titre, DOWN, buff=0.8)

        with self.voiceover(
            text=(
                "Retiens ce chiffre impressionnant : par le seul assortiment "
                "indépendant, un couple humain peut, en théorie, produire "
                "environ soixante-dix mille milliards de zygotes "
                "génétiquement différents. Et ce n'est encore que le premier "
                "des deux mécanismes du brassage génétique."
            )
        ) as tracker:
            self.play(Write(formule_zygote))
            self.play(FadeIn(legende))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(titre), FadeOut(bloc_final))
