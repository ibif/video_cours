"""
scenes/Chimie_Ethanol_01.py — Chapitre 7 « L'éthanol » (1ereC, Chimie),
scène 01.

§ 1. Généralités : formule et classe de l'éthanol. Rappels : définition
d'un alcool (groupe -OH sur carbone tétragonal), classe d'un alcool
(primaire / secondaire / tertiaire selon le nombre de groupes alkyles liés
au carbone fonctionnel). Éthanol : formule brute C₂H₆O, formule
semi-développée CH₃-CH₂-OH, classe primaire, masse molaire M=46 g/mol.
Exemple résolu 1 : composition centésimale massique (52,2% C / 13,0% H /
34,8% O, vérification = 100%).
Source : 1ereC/Chimie.pdf, chapitre 7, pages 67-68.
"""

import textwrap

from manim import (
    DOWN,
    LEFT,
    RIGHT,
    UP,
    WHITE,
    YELLOW,
    FadeIn,
    FadeOut,
    MathTex,
    Text,
    VGroup,
    Write,
    config,
)

from shapes.base_scene import NotionScene
from shapes.boxes import definition_box, property_box, scene_title, warning_box


def _wrap(text: str, width: int = 56) -> str:
    return "\n".join(textwrap.fill(line, width=width) for line in text.split("\n"))


def _bullets(items, font_size=22, color=WHITE, width=54):
    lines = VGroup(
        *[Text(f"• {_wrap(it, width=width)}", font_size=font_size, color=color) for it in items]
    )
    lines.arrange(DOWN, aligned_edge=LEFT, buff=0.22)
    return lines


def _fit(mobject, top_y):
    bas_visible = -config.frame_height / 2 + 0.25
    hauteur_dispo = top_y - bas_visible
    if mobject.height > hauteur_dispo:
        mobject.scale(hauteur_dispo / mobject.height, about_point=mobject.get_top())
    return mobject


class GeneralitesFormuleClasseEthanol(NotionScene):
    def construct(self):
        titre = scene_title("7. Généralités : formule et classe de l'éthanol")
        titre.scale(0.52)
        titre.to_edge(UP)

        # --- Énoncé : mise en situation -----------------------------------------
        intro = Text(
            _wrap(
                "L'éthanol, ou alcool éthylique, est le plus connu de tous "
                "les alcools. On le trouve dans les boissons fermentées, "
                "mais aussi comme solvant, désinfectant ou carburant. "
                "Quelle est sa formule ? À quelle classe d'alcool "
                "appartient-il ?",
                width=56,
            ),
            font_size=25,
            color=WHITE,
        )
        intro.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "L'éthanol, appelé aussi alcool éthylique, est le plus "
                "connu de tous les alcools. On le trouve dans les boissons "
                "fermentées, mais aussi comme solvant, comme désinfectant "
                "ou comme carburant. Dans ce chapitre, nous allons "
                "répondre à plusieurs questions : quelle est sa formule ? "
                "Comment l'obtenir ? Comment réagit-il ? Commençons par "
                "deux rappels indispensables : qu'est-ce qu'un alcool, et "
                "qu'est-ce que la classe d'un alcool ?"
            )
        ) as tracker:
            self.play(Write(titre))
            self.play(FadeIn(intro))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(intro))

        # --- Raisonnement : rappel définition d'un alcool -----------------------
        def_alcool = definition_box(
            Text(
                _wrap(
                    "Un alcool est un composé organique oxygéné dont la "
                    "molécule possède un groupe hydroxyle -OH porté par un "
                    "atome de carbone tétragonal (carbone fonctionnel), "
                    "lié uniquement à des atomes de carbone ou "
                    "d'hydrogène. Formule générale : CₙH₂ₙ₊₁-OH, notée "
                    "aussi R-OH.",
                    width=48,
                ),
                font_size=23,
            ),
        )
        def_alcool.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Rappel : un alcool est un composé organique oxygéné dont "
                "la molécule possède un groupe hydroxyle, moins O H, porté "
                "par un atome de carbone tétragonal, appelé carbone "
                "fonctionnel, lui-même lié uniquement à des atomes de "
                "carbone ou d'hydrogène. La formule générale d'un alcool "
                "saturé à chaîne ouverte est C indice n, H indice deux n "
                "plus un, tiret O H, que l'on note aussi R tiret O H, où R "
                "représente un groupe alkyle."
            )
        ) as tracker:
            self.play(FadeIn(def_alcool))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(def_alcool))

        def_classe = definition_box(
            VGroup(
                Text(
                    _wrap(
                        "La classe d'un alcool est le nombre de groupes "
                        "alkyles (R, R', R'') liés au carbone fonctionnel.",
                        width=50,
                    ),
                    font_size=22,
                ),
                MathTex(r"\text{Primaire : } R-CH_2-OH", font_size=26, color="#1A1A1A"),
                MathTex(r"\text{Secondaire : } R-CH(OH)-R'", font_size=26, color="#1A1A1A"),
                MathTex(r"\text{Tertiaire : } R-C(OH)(R')(R'')", font_size=26, color="#1A1A1A"),
            ).arrange(DOWN, buff=0.28, aligned_edge=LEFT),
            box_width=12.2,
        )
        def_classe.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "La classe d'un alcool est le nombre de groupes alkyles, "
                "notés R, R prime, R seconde, liés au carbone fonctionnel. "
                "Un alcool primaire a son carbone fonctionnel lié à un "
                "seul groupe alkyle : R tiret C H deux tiret O H. Un "
                "alcool secondaire l'a lié à deux groupes alkyles : R "
                "tiret C H, O H, tiret R prime. Un alcool tertiaire l'a "
                "lié à trois groupes alkyles : R tiret C, O H, R prime, R "
                "seconde."
            )
        ) as tracker:
            self.play(FadeIn(def_classe))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(def_classe))

        # --- Exemple traité : l'éthanol lui-même ---------------------------------
        entete_ex = Text("L'éthanol : formule et classe", font_size=24, color=YELLOW, weight="BOLD")
        entete_ex.next_to(titre, DOWN, buff=0.35)

        fiche_ethanol = VGroup(
            MathTex(r"\text{Formule brute : } C_2H_6O", font_size=28, color=WHITE),
            MathTex(r"\text{Formule semi-développée : } CH_3-CH_2-OH", font_size=28, color=WHITE),
            Text("Classe : alcool primaire (carbone fonctionnel lié à un seul CH₃-)", font_size=22, color=WHITE),
            MathTex(r"M = 2\times 12 + 6\times 1 + 16 = 46\ \text{g/mol}", font_size=28, color=WHITE),
        ).arrange(DOWN, buff=0.3, aligned_edge=LEFT)
        fiche_ethanol.next_to(entete_ex, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "L'éthanol a pour formule brute C-2, H-6, O, et pour "
                "formule semi-développée C-H-3 tiret C-H-2 tiret O-H, que "
                "l'on note aussi C-2, H-5, O-H. C'est un alcool primaire : "
                "son carbone fonctionnel, celui qui porte le groupe O-H, "
                "n'est lié qu'à un seul groupe méthyle, C-H-3. Sa masse "
                "molaire moléculaire vaut deux fois douze, plus six fois "
                "un, plus seize, soit quarante-six grammes par mole."
            )
        ) as tracker:
            self.play(FadeIn(entete_ex))
            self.play(Write(fiche_ethanol))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(entete_ex), FadeOut(fiche_ethanol))

        # --- Exemple résolu 1 : composition centésimale massique ---------------
        entete_res1 = Text("Exemple résolu 1 — Composition centésimale massique", font_size=22, color=YELLOW, weight="BOLD")
        entete_res1.next_to(titre, DOWN, buff=0.35)

        calc_c = MathTex(r"\%C = \dfrac{2\times 12}{46}\times 100 \approx 52{,}2\%", font_size=26, color=WHITE)
        calc_h = MathTex(r"\%H = \dfrac{6\times 1}{46}\times 100 \approx 13{,}0\%", font_size=26, color=WHITE)
        calc_o = MathTex(r"\%O = \dfrac{1\times 16}{46}\times 100 \approx 34{,}8\%", font_size=26, color=WHITE)
        verif = MathTex(r"52{,}2 + 13{,}0 + 34{,}8 = 100\%", font_size=26, color=YELLOW)

        calculs = VGroup(calc_c, calc_h, calc_o, verif).arrange(DOWN, buff=0.28)
        calculs.next_to(entete_res1, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Calculons le pourcentage massique de chaque élément dans "
                "l'éthanol, C-2, H-6, O, de masse molaire quarante-six "
                "grammes par mole. Pour le carbone : deux fois douze, sur "
                "quarante-six, fois cent, soit environ cinquante-deux "
                "virgule deux pour cent. Pour l'hydrogène : six fois un, "
                "sur quarante-six, fois cent, soit environ treize pour "
                "cent. Pour l'oxygène : seize sur quarante-six, fois cent, "
                "soit environ trente-quatre virgule huit pour cent. "
                "Vérification : cinquante-deux virgule deux plus treize "
                "plus trente-quatre virgule huit égale cent pour cent, "
                "exactement ce qu'il fallait retrouver."
            )
        ) as tracker:
            self.play(FadeIn(entete_res1))
            self.play(Write(calc_c))
            self.play(Write(calc_h))
            self.play(Write(calc_o))
            self.play(Write(verif))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(entete_res1), FadeOut(calculs))

        # --- À retenir : fiche récapitulative ------------------------------------
        propriete = property_box(
            VGroup(
                Text("Éthanol : C₂H₆O, soit CH₃-CH₂-OH — alcool primaire", font_size=22, weight="BOLD"),
                Text("M = 46 g/mol (≈ 52% C, 13% H, 35% O en masse)", font_size=22),
            ).arrange(DOWN, buff=0.3, aligned_edge=LEFT),
        )
        propriete.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Retenons l'essentiel : l'éthanol a pour formule brute "
                "C-2, H-6, O, soit C-H-3 tiret C-H-2 tiret O-H en formule "
                "semi-développée. C'est un alcool primaire, de masse "
                "molaire quarante-six grammes par mole, composé en masse "
                "d'environ cinquante-deux pour cent de carbone, treize "
                "pour cent d'hydrogène et trente-cinq pour cent "
                "d'oxygène."
            )
        ) as tracker:
            self.play(FadeIn(propriete))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(propriete))

        # --- Piège à éviter : classe ≠ position dans la chaîne -------------------
        piege = warning_box(
            Text(
                _wrap(
                    "La classe d'un alcool ne dépend PAS de la position du "
                    "-OH « dans » la chaîne, mais du nombre de groupes "
                    "alkyles réellement liés au carbone fonctionnel : il "
                    "faut compter les R, R' et R'', pas seulement regarder "
                    "si le -OH semble « au bout » du dessin.",
                    width=48,
                ),
                font_size=22,
            ),
        )
        piege.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Attention à un piège fréquent : la classe d'un alcool ne "
                "dépend pas de la position du groupe O-H « dans » la "
                "chaîne dessinée, mais bien du nombre de groupes alkyles "
                "réellement liés au carbone fonctionnel. Il faut compter "
                "précisément les groupes R, R prime et R seconde, et pas "
                "simplement regarder si le O-H semble se trouver au bout "
                "du dessin."
            )
        ) as tracker:
            self.play(FadeIn(piege))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(piege), FadeOut(titre))
