"""
scenes/SVT_Photosynthese_14.py — Chapitre 10 (1ereC, SVT), scène 14.

§ 10.6.3-10.6.4 Les facteurs (2/2) : la température (rôle des
enzymes/Rubisco, courbe en cloche, optimum 25-30°C, dénaturation au-delà
de 40-45°C) + autres facteurs (eau — fermeture des stomates en cas de
déficit — et sels minéraux — Mg dans la chlorophylle, N dans les enzymes)
+ tableau récapitulatif des 4 facteurs + Exemple résolu 2 (tableau de
données éclairement/O2 dégagé pour une feuille de manioc, détermination du
point de compensation, intensité de la respiration, explication du
plafonnement).
Source : 1ereC/SVT.pdf, pages 113-114.
"""

import math
import textwrap

from manim import DOWN, LEFT, RIGHT, UP, WHITE, YELLOW, Axes, DashedLine, FadeIn, FadeOut, Text, VGroup, Write, config

from shapes.base_scene import NotionScene
from shapes.boxes import corrige_box, definition_box, exercise_box, scene_title, warning_box


def _wrap(text: str, width: int = 56) -> str:
    return "\n".join(textwrap.fill(line, width=width) for line in text.split("\n"))


def _bullets(items, font_size=22, color=WHITE, width=52):
    lines = VGroup(
        *[Text(f"• {_wrap(it, width=width)}", font_size=font_size, color=color) for it in items]
    )
    lines.arrange(DOWN, aligned_edge=LEFT, buff=0.22)
    return lines


def _cell(text: str, x: float, y: float, font_size=13, color=WHITE, bold=False):
    t = Text(text, font_size=font_size, color=color, weight="BOLD" if bold else "NORMAL")
    t.move_to([x, y, 0])
    t.shift(RIGHT * (t.width / 2))
    return t


def _courbe_temperature():
    """Courbe en cloche : intensité photosynthétique en fonction de la
    température, optimum vers 25-30°C, chute au-delà de 40-45°C."""
    axes = Axes(
        x_range=[0, 50, 10],
        y_range=[0, 8, 2],
        x_length=8.0,
        y_length=4.0,
        axis_config={"font_size": 16, "include_numbers": True, "stroke_width": 2},
        tips=True,
    )
    label_x = Text("température (°C)", font_size=15, color=WHITE).next_to(axes.x_axis, RIGHT, buff=0.15)
    label_y = Text("intensité photo-\nsynthétique", font_size=13, color=WHITE).next_to(axes.y_axis, UP, buff=0.1)

    def f(x):
        return 7.2 * math.exp(-((x - 27) ** 2) / (2 * 8.5 ** 2))

    courbe = axes.plot(f, x_range=[0, 48], color="#DE7C1F", stroke_width=3)

    ligne_opt = DashedLine(axes.c2p(27, 0), axes.c2p(27, f(27)), color=YELLOW, stroke_width=2)
    label_opt = Text("optimum\n25-30°C", font_size=13, color=YELLOW).next_to(ligne_opt, UP, buff=0.1)

    ligne_denat = DashedLine(axes.c2p(43, 0), axes.c2p(43, f(43)), color="#B42E41", stroke_width=2)
    label_denat = Text("dénaturation\n(>40-45°C)", font_size=12, color="#B42E41").next_to(ligne_denat, RIGHT, buff=0.1).shift(UP * 0.3)

    return VGroup(axes, label_x, label_y, courbe, ligne_opt, label_opt, ligne_denat, label_denat)


class FacteursTemperatureEtAutres(NotionScene):
    def construct(self):
        titre = scene_title("10.6.3-10.6.4 — Facteurs : température et autres")
        titre.scale(0.5)
        titre.to_edge(UP)

        # --- Énoncé : le rôle des enzymes -------------------------------------
        intro = Text(
            _wrap(
                "La phase sombre fait intervenir des enzymes (Rubisco...), "
                "dont l'activité dépend fortement de la température.",
                width=56,
            ),
            font_size=23,
            color=WHITE,
        )
        intro.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Troisième facteur influençant la photosynthèse : la "
                "température. La phase sombre fait intervenir des "
                "enzymes, dont la Rubisco, dont l'activité dépend "
                "fortement de la température."
            )
        ) as tracker:
            self.play(Write(titre))
            self.play(FadeIn(intro))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(intro))

        # --- Animation du raisonnement : la courbe en cloche --------------------
        courbe = _courbe_temperature()
        courbe.scale(0.95)
        courbe.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "À basse température, proche de zéro degré, l'activité "
                "enzymatique est très faible. L'intensité photo-"
                "synthétique augmente avec la température jusqu'à un "
                "optimum, environ vingt-cinq à trente degrés pour de "
                "nombreuses plantes tropicales. Au-delà de quarante à "
                "quarante-cinq degrés, les enzymes se dénaturent : "
                "l'intensité s'effondre brutalement. La courbe a donc "
                "une forme de cloche."
            )
        ) as tracker:
            self.play(FadeIn(courbe))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(courbe))

        # --- Exemple traité : autres facteurs + tableau récapitulatif -----------
        autres = _bullets(
            [
                "L'eau : un déficit hydrique ferme les stomates -> "
                "moins de CO2 absorbé -> photosynthèse ralentie "
                "(fréquent en saison sèche au nord de la Côte d'Ivoire).",
                "Les sels minéraux : le magnésium (Mg) entre dans la "
                "chlorophylle ; l'azote (N) entre dans les enzymes. Une "
                "carence limite donc la photosynthèse.",
            ],
            font_size=19,
            width=54,
        )
        autres.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Deux autres facteurs jouent aussi un rôle. L'eau : un "
                "déficit hydrique ferme les stomates, ce qui réduit "
                "l'entrée de CO2 et ralentit la photosynthèse — un "
                "phénomène fréquent en saison sèche, au nord de la Côte "
                "d'Ivoire. Les sels minéraux : le magnésium entre dans "
                "la composition de la chlorophylle, l'azote dans celle "
                "des enzymes ; une carence minérale limite donc, elle "
                "aussi, la photosynthèse."
            )
        ) as tracker:
            self.play(FadeIn(autres))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(autres))

        entete_tab = Text("Tableau récapitulatif des quatre facteurs", font_size=21, color=YELLOW, weight="BOLD")
        entete_tab.next_to(titre, DOWN, buff=0.4)

        x_fact, x_effet, x_allure = -6.3, -1.6, 2.6
        headers = ["Facteur", "Effet sur l'intensité", "Allure de la courbe"]
        row_y0 = entete_tab.get_bottom()[1] - 0.5
        row_h = 0.85

        header_row = VGroup(
            *[_cell(h, x, row_y0, font_size=15, color=YELLOW, bold=True) for h, x in zip(headers, [x_fact, x_effet, x_allure])]
        )

        rows_data = [
            ("Éclairement", "Augmente puis plafonne\n(saturation lumineuse)", "Croissante puis\nplateau"),
            ("Concentration\nen CO2", "Augmente puis plafonne\n(saturation en CO2)", "Croissante puis\nplateau"),
            ("Température", "Optimum vers 25-30°C\npuis chute brutale", "En cloche"),
            ("Eau disponible", "Déficit -> fermeture des\nstomates -> baisse", "Baisse en cas de\nstress hydrique"),
        ]
        data_rows = VGroup()
        for i, (fact, effet, allure) in enumerate(rows_data):
            y = row_y0 - (i + 1) * row_h
            data_rows.add(
                VGroup(
                    _cell(fact, x_fact, y, font_size=13, color=YELLOW),
                    _cell(effet, x_effet, y, font_size=12),
                    _cell(allure, x_allure, y, font_size=12),
                )
            )
        tableau = VGroup(header_row, data_rows)
        bas_visible = -config.frame_height / 2 + 0.25
        hauteur_dispo = row_y0 - bas_visible + 0.25
        if tableau.height > hauteur_dispo:
            tableau.scale(hauteur_dispo / tableau.height, about_point=[0, row_y0, 0])

        with self.voiceover(
            text=(
                "Résumons dans un tableau les quatre facteurs étudiés. "
                "L'éclairement : l'intensité augmente puis plafonne, "
                "saturation lumineuse ; courbe croissante puis plateau. "
                "La concentration en CO2 : même profil, courbe croissante "
                "puis plateau, jusqu'à saturation en CO2. La température : "
                "optimum vers vingt-cinq à trente degrés, puis chute "
                "brutale ; courbe en cloche. L'eau disponible : un "
                "déficit ferme les stomates et fait baisser l'intensité."
            )
        ) as tracker:
            self.play(FadeIn(entete_tab))
            self.play(FadeIn(header_row))
            for row in data_rows:
                self.play(FadeIn(row), run_time=0.4)
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(entete_tab), FadeOut(tableau))

        # --- À retenir : Exemple résolu 2 (feuille de manioc) --------------------
        enonce = exercise_box(
            Text(
                _wrap(
                    "Exemple résolu : intensité photosynthétique d'une "
                    "feuille de manioc (O2 dégagé, mL/h) selon "
                    "l'éclairement (lux) : 0 -> -2 ; 2000 -> 0 ; "
                    "4000 -> 2 ; 6000 -> 4 ; 8000 -> 5 ; 10000 -> 5,5 ; "
                    "12000 -> 5,6. 1. Point de compensation ? 2. "
                    "Intensité de la respiration ? 3. Pourquoi la "
                    "courbe plafonne-t-elle au-delà de 8000 lux ?",
                    width=54,
                ),
                font_size=17,
            ),
            box_width=12.4,
        )
        enonce.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Exemple résolu. On mesure l'intensité photosynthétique "
                "d'une feuille de manioc en fonction de l'éclairement : "
                "à zéro lux, moins deux millilitres d'O2 par heure ; à "
                "deux mille lux, zéro ; à quatre mille lux, deux ; à six "
                "mille lux, quatre ; à huit mille lux, cinq ; à dix mille "
                "lux, cinq virgule cinq ; à douze mille lux, cinq "
                "virgule six. Première question : déterminer le point de "
                "compensation lumineux. Deuxième question : quelle est "
                "l'intensité de la respiration ? Troisième question : "
                "pourquoi la courbe plafonne-t-elle au-delà de huit mille "
                "lux ?"
            )
        ) as tracker:
            self.play(FadeIn(enonce))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(enonce))

        correction = corrige_box(
            _bullets(
                [
                    "Point de compensation : éclairement où O2 net=0, "
                    "soit 2000 lux (photosynthèse = respiration).",
                    "Intensité de la respiration : à l'obscurité (0 "
                    "lux), la feuille consomme 2 mL d'O2/h -> "
                    "respiration = 2 mL O2/h.",
                    "Plafonnement au-delà de 8000 lux : la lumière "
                    "n'est plus le facteur limitant ; un autre facteur "
                    "(CO2 ou température) empêche toute augmentation "
                    "supplémentaire : c'est le point de saturation "
                    "lumineuse.",
                ],
                font_size=17,
                width=52,
            ),
            box_width=12.4,
        )
        correction.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Corrigeons. Le point de compensation est l'éclairement "
                "pour lequel le bilan net est nul, O2 dégagé égal zéro : "
                "c'est deux mille lux, où photosynthèse et respiration "
                "s'équilibrent exactement. À l'obscurité, zéro lux, la "
                "feuille consomme deux millilitres d'O2 par heure, la "
                "valeur moins deux : l'intensité de la respiration est "
                "donc de deux millilitres d'O2 par heure. Enfin, "
                "au-delà de huit mille lux, la lumière n'est plus le "
                "facteur limitant : un autre facteur, concentration en "
                "CO2 ou température, empêche toute augmentation "
                "supplémentaire. C'est le point de saturation lumineuse."
            )
        ) as tracker:
            self.play(FadeIn(correction))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(correction))

        # --- Piège à éviter : optimum ≠ maximum absolu, dénaturation irréversible
        piege = warning_box(
            Text(
                _wrap(
                    "Piège à éviter : ne pas confondre l'optimum "
                    "thermique (meilleure activité enzymatique) avec un "
                    "maximum que la plante pourrait dépasser sans "
                    "risque. Au-delà de 40-45°C, la dénaturation des "
                    "enzymes est souvent IRRÉVERSIBLE : la photosynthèse "
                    "ne repart pas simplement en revenant à 25°C.",
                    width=54,
                ),
                font_size=19,
            ),
            box_width=12.2,
        )
        piege.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Attention à ne pas confondre l'optimum thermique, la "
                "meilleure activité enzymatique, avec un simple maximum "
                "que la plante pourrait dépasser sans risque. Au-delà de "
                "quarante à quarante-cinq degrés, la dénaturation des "
                "enzymes est souvent irréversible : la photosynthèse ne "
                "repart pas simplement en revenant à vingt-cinq degrés, "
                "contrairement à ce qu'on pourrait croire en lisant "
                "seulement la forme de la courbe."
            )
        ) as tracker:
            self.play(FadeIn(piege))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(titre), FadeOut(piege))
