"""
scenes/SVT_Photosynthese_13.py — Chapitre 10 (1ereC, SVT), scène 13.

§ 10.6.1-10.6.2 Les facteurs influençant la photosynthèse (1/2) :
définition de l'intensité photosynthétique + la lumière (point de
compensation lumineux — définition — puis zone d'augmentation, puis point
de saturation) + le dioxyde de carbone (facteur limitant le plus fréquent,
enrichissement en serre, point de saturation en CO2).
Source : 1ereC/SVT.pdf, pages 112-113.
"""

import math
import textwrap

from manim import DOWN, LEFT, RIGHT, UP, WHITE, YELLOW, Axes, DashedLine, FadeIn, FadeOut, Text, VGroup, Write

from shapes.base_scene import NotionScene
from shapes.boxes import definition_box, scene_title, warning_box


def _wrap(text: str, width: int = 56) -> str:
    return "\n".join(textwrap.fill(line, width=width) for line in text.split("\n"))


def _bullets(items, font_size=22, color=WHITE, width=52):
    lines = VGroup(
        *[Text(f"• {_wrap(it, width=width)}", font_size=font_size, color=color) for it in items]
    )
    lines.arrange(DOWN, aligned_edge=LEFT, buff=0.22)
    return lines


def _courbe_lumiere():
    """Courbe intensité photosynthétique en fonction de l'éclairement :
    zone négative (respiration domine), point de compensation, zone
    d'augmentation, point de saturation (plateau)."""
    axes = Axes(
        x_range=[0, 10, 2],
        y_range=[-3, 7, 2],
        x_length=8.0,
        y_length=4.2,
        axis_config={"font_size": 16, "include_numbers": False, "stroke_width": 2},
        tips=True,
    )
    label_x = Text("éclairement", font_size=16, color=WHITE).next_to(axes.x_axis, RIGHT, buff=0.15)
    label_y = Text("O2 net (mL/h)", font_size=15, color=WHITE).next_to(axes.y_axis, UP, buff=0.15)

    def f(x):
        return -2 + 8 * (1 - math.exp(-0.5 * x))

    courbe = axes.plot(f, x_range=[0, 9.5], color="#3FCB63", stroke_width=3)

    # Point de compensation : intersection avec l'axe des abscisses.
    x_comp = 0.575
    point_comp = axes.c2p(x_comp, 0)
    ligne_comp = DashedLine(axes.c2p(x_comp, -3), axes.c2p(x_comp, 0), color=YELLOW, stroke_width=2)
    label_comp = Text("point de\ncompensation", font_size=13, color=YELLOW)
    label_comp.next_to(ligne_comp, DOWN, buff=0.15)

    # Point de saturation : là où la courbe s'aplatit.
    x_sat = 6.0
    ligne_sat = DashedLine(axes.c2p(x_sat, -3), axes.c2p(x_sat, f(x_sat)), color="#DE7C1F", stroke_width=2)
    label_sat = Text("point de\nsaturation", font_size=13, color="#DE7C1F")
    label_sat.next_to(ligne_sat, DOWN, buff=0.15)

    label_neg = Text("respiration > photosynthèse", font_size=12, color="#B42E41")
    label_neg.move_to(axes.c2p(0.3, -2.4), aligned_edge=LEFT)

    return VGroup(axes, label_x, label_y, courbe, ligne_comp, label_comp, ligne_sat, label_sat, label_neg)


class FacteursLumiereEtCO2(NotionScene):
    def construct(self):
        titre = scene_title("10.6.1-10.6.2 — Facteurs : lumière et CO2")
        titre.scale(0.55)
        titre.to_edge(UP)

        # --- Énoncé : l'intensité photosynthétique -----------------------------
        definition = definition_box(
            Text(
                _wrap(
                    "L'intensité photosynthétique est la quantité de "
                    "matière organique produite par unité de temps "
                    "(mesurable par le volume d'O2 dégagé, la quantité "
                    "de CO2 absorbée ou la masse de matière sèche "
                    "formée par heure). Elle dépend de plusieurs "
                    "facteurs du milieu.",
                    width=54,
                ),
                font_size=21,
            ),
            box_width=12.0,
        )
        definition.next_to(titre, DOWN, buff=0.45)

        with self.voiceover(
            text=(
                "La photosynthèse n'a pas toujours la même efficacité : "
                "elle dépend des conditions du milieu. On appelle "
                "intensité photosynthétique la quantité de matière "
                "organique produite par unité de temps, mesurable par le "
                "volume d'O2 dégagé, la quantité de CO2 absorbée, ou la "
                "masse de matière sèche formée par heure. Elle dépend de "
                "plusieurs facteurs du milieu, que nous allons étudier "
                "un par un."
            )
        ) as tracker:
            self.play(Write(titre))
            self.play(FadeIn(definition))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(definition))

        # --- Animation du raisonnement : la lumière et sa courbe ---------------
        def_compensation = definition_box(
            Text(
                _wrap(
                    "Point de compensation lumineux : éclairement pour "
                    "lequel la quantité d'O2 produite par la "
                    "photosynthèse est exactement égale à celle "
                    "consommée par la respiration : le bilan gazeux net "
                    "est nul.",
                    width=54,
                ),
                font_size=20,
            ),
            box_width=12.0,
        )
        def_compensation.next_to(titre, DOWN, buff=0.45)

        with self.voiceover(
            text=(
                "Premier facteur : la lumière. En dessous du point de "
                "compensation lumineux, la plante respire plus qu'elle "
                "ne photosynthétise : le bilan gazeux est négatif, elle "
                "consomme de l'O2. Définition : le point de compensation "
                "lumineux est l'éclairement pour lequel la quantité d'O2 "
                "produite par la photosynthèse est exactement égale à "
                "celle consommée par la respiration : le bilan gazeux "
                "net est nul."
            )
        ) as tracker:
            self.play(FadeIn(def_compensation))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(def_compensation))

        courbe = _courbe_lumiere()
        courbe.scale(0.95)
        courbe.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Voici l'allure de la courbe. Entre le point de "
                "compensation et le point de saturation, l'intensité "
                "photosynthétique augmente avec l'éclairement : c'est la "
                "zone d'augmentation. Au-delà du point de saturation, "
                "l'intensité plafonne : la lumière n'est plus le facteur "
                "limitant, c'est alors le CO2 ou la température qui "
                "prend le relais."
            )
        ) as tracker:
            self.play(FadeIn(courbe))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(courbe))

        # --- Exemple traité : le dioxyde de carbone -----------------------------
        co2_texte = _bullets(
            [
                "Le CO2 est le facteur limitant le plus fréquent en "
                "plein champ (sa concentration dans l'air n'est "
                "qu'environ 0,04 %).",
                "Un enrichissement en CO2 (comme dans les serres) "
                "augmente l'intensité photosynthétique.",
                "...jusqu'à un point de saturation en CO2, au-delà "
                "duquel un autre facteur devient limitant.",
            ],
            font_size=21,
            width=52,
        )
        co2_texte.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Deuxième facteur : le dioxyde de carbone. C'est le "
                "facteur limitant le plus fréquent en plein champ, car "
                "sa concentration dans l'air n'est que d'environ zéro "
                "virgule zéro quatre pour cent. Un enrichissement en "
                "CO2, comme on le pratique dans les serres, augmente "
                "l'intensité photosynthétique, jusqu'à un point de "
                "saturation en CO2, au-delà duquel un autre facteur "
                "devient limitant."
            )
        ) as tracker:
            self.play(FadeIn(co2_texte))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(co2_texte))

        # --- À retenir -----------------------------------------------------------
        essentiel = definition_box(
            Text(
                _wrap(
                    "À retenir : la lumière et le CO2 suivent tous deux "
                    "un profil « point de compensation -> zone "
                    "d'augmentation -> point de saturation ». Au-delà de "
                    "la saturation d'un facteur, c'est TOUJOURS un autre "
                    "facteur qui devient limitant.",
                    width=54,
                ),
                font_size=20,
            ),
            box_width=12.0,
        )
        essentiel.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Retenons l'essentiel : la lumière et le CO2 suivent "
                "tous deux un profil identique, point de compensation, "
                "puis zone d'augmentation, puis point de saturation. Et "
                "au-delà de la saturation d'un facteur, c'est toujours "
                "un autre facteur qui devient limitant : c'est la loi "
                "du facteur limitant."
            )
        ) as tracker:
            self.play(FadeIn(essentiel))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(essentiel))

        # --- Piège à éviter : lumière infinie ≠ photosynthèse infinie --------
        piege = warning_box(
            Text(
                _wrap(
                    "Piège à éviter : ne pas croire que plus de lumière "
                    "produit toujours plus de photosynthèse. Au-delà du "
                    "point de saturation lumineuse, la courbe plafonne : "
                    "un excès de lumière n'apporte plus rien (et peut "
                    "même endommager les pigments à très haute "
                    "intensité).",
                    width=54,
                ),
                font_size=20,
            ),
            box_width=12.0,
        )
        piege.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Attention à ne pas croire que plus de lumière produit "
                "toujours plus de photosynthèse. Au-delà du point de "
                "saturation lumineuse, la courbe plafonne : un excès de "
                "lumière n'apporte plus rien à la plante, et peut même, "
                "à très haute intensité, endommager les pigments "
                "chlorophylliens."
            )
        ) as tracker:
            self.play(FadeIn(piege))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(titre), FadeOut(piege))
