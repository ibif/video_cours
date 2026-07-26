"""
scenes/SVT_EcosystemeAgroIndustriel_03.py — Chapitre 11 (1ereC, SVT), scène 03.

§ 2.1 La forêt dense humide, exemple du parc national de Taï : biotope
(climat subéquatorial, sols ferrallitiques) et biocénose stratifiée
(strate émergente, canopée, sous-bois, strate herbacée, faune), puis
méthode « les éléments minéraux sont stockés dans la biomasse, pas le
sol ». Source : 1ereC/SVT.pdf, page 121.
"""

import textwrap

from manim import DOWN, LEFT, UP, WHITE, FadeIn, FadeOut, Rectangle, Text, VGroup, Write, config

from shapes.base_scene import NotionScene
from shapes.boxes import example_box, method_box, property_box, scene_title


def _wrap(text: str, width: int = 56) -> str:
    return "\n".join(textwrap.fill(line, width=width) for line in text.split("\n"))


def _bullets(items, font_size=23, color=WHITE, width=52):
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


def _strate(largeur, hauteur, couleur, texte):
    rect = Rectangle(width=largeur, height=hauteur, fill_color=couleur, fill_opacity=0.85, stroke_color=WHITE, stroke_width=1.5)
    label = Text(texte, font_size=14, color=WHITE, weight="BOLD")
    label.move_to(rect.get_center())
    return VGroup(rect, label)


class LaForetDenseDeTai(NotionScene):
    def construct(self):
        titre = scene_title("2.1 — La forêt dense humide : le parc de Taï")
        titre.scale(0.58)
        titre.to_edge(UP)

        # --- Énoncé --------------------------------------------------------
        intro = Text(
            _wrap(
                "La forêt dense humide occupe le sud de la Côte d'Ivoire. "
                "Le parc national de Taï, au Sud-Ouest, classé patrimoine "
                "mondial de l'UNESCO, en est le plus grand reliquat "
                "protégé.",
                width=56,
            ),
            font_size=24,
            color=WHITE,
        )
        intro.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Après avoir posé les définitions, étudions trois "
                "écosystèmes naturels ivoiriens. Premier exemple : la "
                "forêt dense humide, qui occupe le sud de la Côte "
                "d'Ivoire. Le parc national de Taï, au Sud-Ouest, classé "
                "patrimoine mondial de l'UNESCO, en est le plus grand "
                "reliquat protégé."
            )
        ) as tracker:
            self.play(Write(titre))
            self.play(FadeIn(intro))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(intro))

        # --- Raisonnement : le biotope de Taï -------------------------------
        biotope = property_box(
            Text(
                _wrap(
                    "Biotope : climat subéquatorial, forte pluviométrie "
                    "(1500 à 2500 mm/an), température moyenne 25 à 27°C, "
                    "sols ferrallitiques pauvres mais profonds, humidité "
                    "permanente.",
                    width=54,
                ),
                font_size=21,
            ),
            box_width=11.8,
        )
        biotope.next_to(titre, DOWN, buff=0.45)

        with self.voiceover(
            text=(
                "Le biotope de la forêt de Taï se caractérise par un "
                "climat subéquatorial : une forte pluviométrie, de mille "
                "cinq cents à deux mille cinq cents millimètres par an, "
                "une température moyenne voisine de vingt-cinq à "
                "vingt-sept degrés, des sols ferrallitiques pauvres mais "
                "profonds, et une humidité permanente."
            )
        ) as tracker:
            self.play(FadeIn(biotope))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(biotope))

        # --- Schéma : la stratification de la végétation --------------------
        emergente = _strate(9.5, 0.55, "#1B4D2E", "Strate émergente (>40 m) : iroko, samba")
        canopee = _strate(9.0, 0.75, "#2E7D32", "Canopée (25-35 m) : toiture continue")
        sousbois = _strate(8.3, 0.85, "#66BB6A", "Sous-bois : arbustes, jeunes arbres à l'ombre")
        herbacee = _strate(7.5, 0.55, "#A5D6A7", "Strate herbacée : fougères, mousses (clairsemée)")
        strates = VGroup(emergente, canopee, sousbois, herbacee).arrange(DOWN, buff=0.06)
        strates.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "La biocénose de Taï présente une biodiversité très "
                "élevée. La végétation est organisée en étages : la "
                "strate émergente, des arbres géants de plus de "
                "quarante mètres, comme l'iroko ou le samba ; la canopée, "
                "une toiture continue vers vingt-cinq à trente-cinq "
                "mètres ; le sous-bois, des arbustes et de jeunes arbres à "
                "l'ombre ; et la strate herbacée, très clairsemée, faite "
                "de fougères et de mousses."
            )
        ) as tracker:
            self.play(FadeIn(strates))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(strates))

        # --- Exemple traité : la faune ---------------------------------------
        faune = example_box(
            Text(
                _wrap(
                    "On y trouve chimpanzés, éléphants de forêt, colobes, "
                    "pangolins, d'innombrables insectes, et des champignons "
                    "décomposeurs.",
                    width=52,
                ),
                font_size=22,
            ),
            box_width=11.2,
        )
        faune.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Parmi les espèces emblématiques de cette biocénose : les "
                "chimpanzés, les éléphants de forêt, les colobes, les "
                "pangolins, d'innombrables insectes, et des champignons "
                "décomposeurs qui recyclent la matière morte au sol."
            )
        ) as tracker:
            self.play(FadeIn(faune))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(faune))

        # --- À retenir : point clé ---------------------------------------
        methode = method_box(
            Text(
                _wrap(
                    "Dans la forêt dense, l'essentiel des éléments "
                    "minéraux (azote, potassium, phosphore) est stocké "
                    "dans la biomasse vivante, et non dans le sol. Abattre "
                    "et brûler la forêt fait perdre ces éléments, lessivés "
                    "par les pluies : le sol nu s'appauvrit très vite.",
                    width=54,
                ),
                font_size=21,
            ),
            box_width=11.8,
        )
        methode.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Point clé essentiel à retenir : dans la forêt dense, "
                "l'essentiel des éléments minéraux, azote, potassium, "
                "phosphore, est stocké dans la biomasse vivante, et non "
                "dans le sol. Quand on abat la forêt et qu'on brûle la "
                "végétation, ces éléments sont perdus ou lessivés par les "
                "pluies : le sol nu s'appauvrit très vite. C'est pourquoi "
                "une forêt défrichée ne donne que quelques années de "
                "bonnes récoltes avant de s'épuiser."
            )
        ) as tracker:
            self.play(FadeIn(methode))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(titre), FadeOut(methode))
