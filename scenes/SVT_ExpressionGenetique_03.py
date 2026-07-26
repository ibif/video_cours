"""
scenes/SVT_ExpressionGenetique_03.py — Chapitre 5 (1ereC, SVT), scène 03.

I.C-D. Les règles de Chargaff (%A=%T, %G=%C), Exemple résolu 2 (calcul de
pourcentages à partir de 22% d'adénine), et pourquoi la complémentarité des
bases est fondamentale (réplication + expression des gènes).
Source : 1ereC/SVT.pdf, page 46.
"""

import textwrap

from manim import DOWN, LEFT, UP, WHITE, YELLOW, FadeIn, FadeOut, MathTex, Text, VGroup, Write

from shapes.base_scene import NotionScene
from shapes.boxes import example_box, method_box, property_box, scene_title


def _wrap(text: str, width: int = 56) -> str:
    return "\n".join(textwrap.fill(line, width=width) for line in text.split("\n"))


def _bullets(items, font_size=22, color=WHITE, width=52):
    lines = VGroup(
        *[Text(f"• {_wrap(it, width=width)}", font_size=font_size, color=color) for it in items]
    )
    lines.arrange(DOWN, aligned_edge=LEFT, buff=0.22)
    return lines


class ReglesDeChargaff(NotionScene):
    def construct(self):
        titre = scene_title("I.D — Les règles de Chargaff")
        titre.scale(0.6)
        titre.to_edge(UP)

        with self.voiceover(
            text=(
                "La complémentarité des bases a une conséquence directement "
                "mesurable dans un échantillon d'ADN : les règles de "
                "Chargaff."
            )
        ) as tracker:
            self.play(Write(titre))
            self.wait(tracker.get_remaining_duration())

        # --- Énoncé : la règle -------------------------------------------------
        methode = method_box(
            MathTex(
                r"\%A = \%T \qquad \%G = \%C",
                font_size=34,
            ),
            box_width=8.0,
        )
        methode.next_to(titre, DOWN, buff=0.6)

        precision = Text(
            _wrap(
                "Dans tout ADN double brin : %A=%T et %G=%C. "
                "Attention : ces égalités sont fausses si l'on ne considère "
                "qu'un seul brin.",
                width=52,
            ),
            font_size=22,
            color=WHITE,
        )
        precision.next_to(methode, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Puisque, dans un ADN double brin, chaque adénine d'un brin "
                "fait face à une thymine de l'autre brin, il y a "
                "nécessairement autant d'adénines que de thymines sur "
                "l'ensemble de la molécule : le pourcentage d'adénine égale "
                "le pourcentage de thymine. Le même raisonnement s'applique "
                "à la guanine et à la cytosine. Attention, ces égalités sont "
                "fausses si l'on ne considère qu'un seul brin isolé : elles "
                "ne valent que pour l'ADN double brin dans son ensemble."
            )
        ) as tracker:
            self.play(FadeIn(methode))
            self.play(FadeIn(precision))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(methode), FadeOut(precision))

        # --- Exemple résolu 2 : calcul de pourcentages -------------------------
        enonce = Text(
            "On mesure 22% d'adénine dans un ADN double brin.\nDéterminons les autres pourcentages.",
            font_size=22,
            color=WHITE,
        )
        etape1 = MathTex(r"\%T = \%A = 22\%", font_size=28, color=WHITE)
        etape2 = MathTex(r"\%G + \%C = 100 - 22 - 22 = 56\%", font_size=28, color=WHITE)
        etape3 = MathTex(r"\%G = \%C = 28\%", font_size=28, color=YELLOW)
        calcul = VGroup(enonce, etape1, etape2, etape3).arrange(DOWN, buff=0.3)

        exemple = example_box(calcul, box_width=11.0)
        exemple.next_to(titre, DOWN, buff=0.55)

        with self.voiceover(
            text=(
                "Exemple résolu. Dans un ADN double brin, on mesure vingt-"
                "deux pour cent d'adénine. Déterminons les pourcentages des "
                "autres bases. Comme A fait toujours face à T : le "
                "pourcentage de thymine égale celui de l'adénine, soit vingt-"
                "deux pour cent. Le reste, cent moins vingt-deux moins vingt-"
                "deux, soit cinquante-six pour cent, est partagé également "
                "entre G et C. Donc le pourcentage de guanine et celui de "
                "cytosine valent chacun vingt-huit pour cent."
            )
        ) as tracker:
            self.play(FadeIn(exemple))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(exemple))

        # --- À retenir : pourquoi la complémentarité est fondamentale ---------
        entete = Text("Pourquoi la complémentarité est-elle fondamentale ?", font_size=23, color=YELLOW, weight="BOLD")
        entete.next_to(titre, DOWN, buff=0.5)

        raisons = _bullets(
            [
                "La réplication : avant chaque division cellulaire, chaque "
                "brin sert de matrice pour fabriquer un brin neuf "
                "complémentaire — l'information est recopiée fidèlement.",
                "L'expression des gènes : c'est aussi grâce à la "
                "complémentarité qu'un brin d'ADN sert de modèle pour "
                "fabriquer une molécule d'ARN (la transcription, voir plus "
                "loin).",
            ],
            font_size=21,
            width=52,
        )
        raisons.next_to(entete, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Pourquoi cette règle de complémentarité est-elle si "
                "fondamentale ? Elle explique deux propriétés essentielles "
                "de l'ADN. D'abord, la réplication : avant chaque division "
                "cellulaire, chaque brin sert de matrice pour fabriquer un "
                "brin neuf complémentaire, et l'information génétique est "
                "ainsi recopiée fidèlement et transmise aux cellules filles. "
                "Ensuite, l'expression des gènes : c'est encore grâce à la "
                "complémentarité qu'un brin d'ADN peut servir de modèle pour "
                "fabriquer une molécule d'ARN — ce mécanisme, la "
                "transcription, sera notre prochain arrêt."
            )
        ) as tracker:
            self.play(FadeIn(entete))
            self.play(FadeIn(raisons))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(entete), FadeOut(raisons))

        # --- Propriété de synthèse ----------------------------------------------
        propriete = property_box(
            Text(
                _wrap(
                    "La complémentarité des bases (A-T, G-C) garantit à la "
                    "fois la fidélité de la copie de l'ADN (réplication) et "
                    "la possibilité de fabriquer un ARN messager à partir "
                    "d'un gène (transcription).",
                    width=54,
                ),
                font_size=23,
            ),
            box_width=11.5,
        )
        propriete.next_to(titre, DOWN, buff=0.55)

        with self.voiceover(
            text=(
                "Retenons cette propriété centrale : la complémentarité des "
                "bases garantit à la fois la fidélité de la copie de l'ADN "
                "lors de la réplication, et la possibilité de fabriquer un "
                "ARN messager à partir d'un gène lors de la transcription."
            )
        ) as tracker:
            self.play(FadeIn(propriete))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(titre), FadeOut(propriete))
