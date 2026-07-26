"""
scenes/SVT_AbsorptionNutriments_02.py — Chapitre 13 (1ereD, SVT), scène 02.

§ 13.1.1-13.1.2 Le siège de l'absorption : rappels digestion → absorption,
définition de l'absorption intestinale, expérience du sac intestinal de rat
(protocole + tableau de résultats temps/glucose) et exemple d'exploitation
des résultats (augmentation de concentration, vitesse moyenne).
Source : 1ereD/SVT.pdf, pages 168-169.
"""

import textwrap

from manim import (
    DOWN,
    LEFT,
    RIGHT,
    UP,
    WHITE,
    YELLOW,
    BLUE,
    ORANGE,
    Arrow,
    Dot,
    Ellipse,
    FadeIn,
    FadeOut,
    MathTex,
    Rectangle,
    Text,
    VGroup,
    Write,
)

from shapes.base_scene import NotionScene
from shapes.boxes import definition_box, example_box, scene_title, warning_box


def _wrap(text: str, width: int = 56) -> str:
    return "\n".join(textwrap.fill(line, width=width) for line in text.split("\n"))


def _bullets(items, font_size=23, color=WHITE, width=52):
    lines = VGroup(
        *[Text(f"• {_wrap(it, width=width)}", font_size=font_size, color=color) for it in items]
    )
    lines.arrange(DOWN, aligned_edge=LEFT, buff=0.24)
    return lines


class SiegeAbsorption(NotionScene):
    def construct(self):
        titre = scene_title("13.1 — Le siège de l'absorption")
        titre.scale(0.62)
        titre.to_edge(UP)

        # --- Énoncé : de la digestion à l'absorption ------------------------
        rappel = Text(
            _wrap(
                "À la fin de la digestion, le contenu de l'intestin grêle "
                "— le chyme — est une soupe épaisse de nutriments, d'eau, "
                "de sels et de vitamines. Mais tant qu'ils restent dans la "
                "lumière du tube digestif, ces substances ne font pas "
                "encore partie de l'organisme.",
                width=56,
            ),
            font_size=23,
            color=WHITE,
        )
        rappel.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Au cours de la digestion, les aliments sont transformés "
                "en petites molécules solubles, les nutriments : l'amidon "
                "de l'attiéké en glucose, les protéines du poisson en "
                "acides aminés, les lipides de l'huile de palme en acides "
                "gras et en glycérol. À la fin de la digestion, le contenu "
                "de l'intestin grêle, appelé chyme, est une sorte de soupe "
                "épaisse contenant ces nutriments, mélangés à de l'eau, "
                "des sels minéraux et des vitamines. Mais tant que ces "
                "substances restent dans la lumière du tube digestif, "
                "elles ne font pas encore partie de l'organisme : la "
                "lumière intestinale communique avec l'extérieur par la "
                "bouche et par l'anus."
            )
        ) as tracker:
            self.play(Write(titre))
            self.play(FadeIn(rappel))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(rappel))

        definition = definition_box(
            Text(
                _wrap(
                    "L'absorption intestinale est l'ensemble des "
                    "phénomènes par lesquels les nutriments, l'eau, les "
                    "sels minéraux et les vitamines contenus dans le chyme "
                    "passent de la lumière de l'intestin grêle vers le "
                    "sang ou la lymphe, en traversant la paroi "
                    "intestinale.",
                    width=54,
                ),
                font_size=22,
            ),
            box_width=11.9,
        )
        definition.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Pour devenir réellement utiles aux cellules, les "
                "nutriments doivent traverser la paroi intestinale : "
                "c'est précisément l'objet de l'absorption. L'absorption "
                "intestinale est l'ensemble des phénomènes par lesquels "
                "les nutriments, l'eau, les sels minéraux et les vitamines "
                "contenus dans le chyme passent de la lumière de "
                "l'intestin grêle vers le sang ou la lymphe, en traversant "
                "la paroi intestinale."
            )
        ) as tracker:
            self.play(FadeIn(definition))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(definition))

        # --- Animation du raisonnement : le sac intestinal de rat -----------
        entete_exp = Text("Une expérience : le sac intestinal de rat", font_size=25, color=YELLOW, weight="BOLD")
        entete_exp.next_to(titre, DOWN, buff=0.5)

        # Bain extérieur avec glucose
        bain = Rectangle(width=6.0, height=3.2, color=BLUE, fill_color=BLUE, fill_opacity=0.18, stroke_width=3)
        bain_label = Text("Solution glucosée 5 g/L, 37°C", font_size=18, color=BLUE)
        bain_label.next_to(bain, UP, buff=0.15)

        # Sac intestinal ligaturé (ellipse) au centre du bain
        sac = Ellipse(width=3.2, height=1.6, color=ORANGE, fill_color=ORANGE, fill_opacity=0.3, stroke_width=3)
        sac.move_to(bain.get_center())
        ligature_g = Dot(sac.get_left(), color=WHITE, radius=0.06)
        ligature_d = Dot(sac.get_right(), color=WHITE, radius=0.06)
        sac_label = Text("sac (liquide sans glucose)", font_size=16, color=WHITE)
        sac_label.move_to(sac.get_center())

        fleches = VGroup(
            Arrow(sac.point_at_angle(0.3) + RIGHT * 0.7, sac.point_at_angle(0.3), buff=0.02, color=YELLOW, stroke_width=3),
            Arrow(sac.point_at_angle(-0.3) + RIGHT * 0.7, sac.point_at_angle(-0.3), buff=0.02, color=YELLOW, stroke_width=3),
            Arrow(sac.point_at_angle(3.4) + LEFT * 0.7, sac.point_at_angle(3.4), buff=0.02, color=YELLOW, stroke_width=3),
        )

        schema = VGroup(bain, bain_label, sac, ligature_g, ligature_d, sac_label, fleches)
        schema.scale(0.85)
        schema.next_to(entete_exp, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Comment prouver que les nutriments traversent la paroi "
                "de l'intestin grêle ? On ligature un segment d'intestin "
                "grêle de rat à ses deux extrémités, de manière à former "
                "un petit sac. On remplit ce sac d'un liquide "
                "physiologique sans glucose, puis on l'immerge dans une "
                "solution contenant du glucose à cinq grammes par litre, "
                "maintenue à trente-sept degrés et oxygénée. À intervalles "
                "réguliers, on dose le glucose à l'intérieur du sac."
            )
        ) as tracker:
            self.play(FadeIn(entete_exp))
            self.play(FadeIn(schema))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(entete_exp), FadeOut(schema))

        # --- Tableau des résultats -------------------------------------------
        tab_titre = Text("Résultats : glucose dans le sac au cours du temps", font_size=22, color=YELLOW, weight="BOLD")
        tab_titre.next_to(titre, DOWN, buff=0.5)

        ligne_temps = VGroup(
            Text("Temps (min)", font_size=20, color=WHITE, weight="BOLD"),
            Text("0", font_size=20, color=WHITE),
            Text("15", font_size=20, color=WHITE),
            Text("30", font_size=20, color=WHITE),
            Text("45", font_size=20, color=WHITE),
        ).arrange(RIGHT, buff=0.55)

        ligne_glucose = VGroup(
            Text("Glucose (g/L)", font_size=20, color=YELLOW, weight="BOLD"),
            Text("0", font_size=20, color=YELLOW),
            Text("1,5", font_size=20, color=YELLOW),
            Text("2,4", font_size=20, color=YELLOW),
            Text("2,9", font_size=20, color=YELLOW),
        ).arrange(RIGHT, buff=0.4)

        for i in range(1, 5):
            ligne_glucose[i].align_to(ligne_temps[i], LEFT)

        tableau = VGroup(ligne_temps, ligne_glucose).arrange(DOWN, aligned_edge=LEFT, buff=0.4)
        tableau.next_to(tab_titre, DOWN, buff=0.45)

        with self.voiceover(
            text=(
                "Voici les résultats obtenus. Au départ, à zéro minute, le "
                "sac ne contient aucune trace de glucose. Après quinze "
                "minutes, on mesure un virgule cinq gramme par litre ; "
                "après trente minutes, deux virgule quatre grammes par "
                "litre ; après quarante-cinq minutes, deux virgule neuf "
                "grammes par litre."
            )
        ) as tracker:
            self.play(FadeIn(tab_titre))
            self.play(FadeIn(tableau))
            self.wait(tracker.get_remaining_duration())

        interpretation = Text(
            _wrap(
                "Le glucose n'a pu entrer dans le sac qu'en traversant la "
                "paroi intestinale, de la solution extérieure vers "
                "l'intérieur. Cette expérience démontre directement la "
                "réalité du phénomène d'absorption.",
                width=54,
            ),
            font_size=21,
            color=WHITE,
        )
        interpretation.next_to(tableau, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Or, au bout de quarante-cinq minutes, la concentration "
                "atteint deux virgule neuf grammes par litre. Le glucose "
                "n'a pu entrer dans le sac qu'en traversant la paroi "
                "intestinale, de la solution extérieure vers l'intérieur. "
                "Cette expérience démontre directement la réalité du "
                "phénomène d'absorption à travers la paroi de l'intestin "
                "grêle."
            )
        ) as tracker:
            self.play(FadeIn(interpretation))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(tab_titre), FadeOut(tableau), FadeOut(interpretation))

        # --- Exemple traité : exploitation des résultats ----------------------
        calcul = MathTex(
            r"\Delta C = 2{,}4 - 0 = 2{,}4 \ \text{g/L}",
            r"\qquad v = \dfrac{2{,}4}{30} \approx 0{,}08 \ \text{g/L/min}",
            font_size=30,
            color=WHITE,
        )
        calcul.arrange(DOWN, buff=0.5)

        exemple = example_box(
            VGroup(
                Text("Entre 0 et 30 min : augmentation et vitesse moyenne", font_size=20, weight="BOLD"),
                calcul,
            ).arrange(DOWN, buff=0.35),
            box_width=11.5,
        )
        exemple.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Exploitons ces résultats. On relève la concentration "
                "initiale, zéro gramme par litre, et la concentration à "
                "trente minutes, deux virgule quatre grammes par litre. "
                "L'augmentation vaut donc deux virgule quatre moins zéro, "
                "soit deux virgule quatre grammes par litre. La vitesse "
                "moyenne d'entrée du glucose sur cette période est de deux "
                "virgule quatre divisé par trente, soit environ zéro "
                "virgule zéro huit gramme par litre et par minute."
            )
        ) as tracker:
            self.play(FadeIn(exemple))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(exemple))

        # --- À retenir ----------------------------------------------------------
        a_retenir = _bullets(
            [
                "En 30 min, la concentration en glucose dans le sac augmente de 2,4 g/L.",
                "Le glucose de la solution extérieure a traversé la paroi de l'intestin grêle.",
                "L'intestin grêle est donc bien le siège d'un phénomène d'absorption.",
            ],
            font_size=22,
            width=52,
        )
        entete_retenir = Text("À retenir", font_size=26, color=YELLOW, weight="BOLD")
        entete_retenir.next_to(titre, DOWN, buff=0.55)
        a_retenir.next_to(entete_retenir, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "À retenir : en trente minutes, la concentration en "
                "glucose dans le sac a augmenté de deux virgule quatre "
                "grammes par litre. Le glucose de la solution extérieure a "
                "traversé la paroi de l'intestin grêle : l'intestin grêle "
                "est donc bien le siège d'un phénomène d'absorption."
            )
        ) as tracker:
            self.play(FadeIn(entete_retenir))
            self.play(FadeIn(a_retenir))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(entete_retenir), FadeOut(a_retenir))

        # --- Remarque : des substances absorbées sans digestion ---------------
        remarque = warning_box(
            Text(
                _wrap(
                    "L'eau, les sels minéraux et les vitamines sont "
                    "absorbés sans avoir été digérés : ce sont déjà de "
                    "petites molécules directement utilisables par "
                    "l'organisme. La digestion ne concerne que les grosses "
                    "molécules alimentaires — amidon, protéines, lipides.",
                    width=54,
                ),
                font_size=21,
            ),
            box_width=12.0,
        )
        remarque.next_to(titre, DOWN, buff=0.55)

        with self.voiceover(
            text=(
                "Une remarque importante : l'eau, les sels minéraux et les "
                "vitamines sont absorbés sans avoir été digérés, car ce "
                "sont déjà de petites molécules directement utilisables "
                "par l'organisme. La digestion ne concerne que les grosses "
                "molécules alimentaires : l'amidon, les protéines, les "
                "lipides."
            )
        ) as tracker:
            self.play(FadeIn(remarque))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(titre), FadeOut(remarque))
