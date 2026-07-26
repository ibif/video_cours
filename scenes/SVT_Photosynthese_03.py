"""
scenes/SVT_Photosynthese_03.py — Chapitre 10 (1ereC, SVT), scène 03.

§ 10.1.4 + 10.2.1 La photosynthèse, une conversion d'énergie (énergie
lumineuse → énergie chimique, anabolisme, processus endergonique, point
d'entrée de l'énergie solaire dans le monde vivant) + localisation dans la
plante et la cellule (parties vertes, parenchymes, 20-100 chloroplastes
par cellule, stomates pour le CO2, xylème pour l'eau, phloème pour le
glucose exporté).
Source : 1ereC/SVT.pdf, pages 107-108.
"""

import textwrap

from manim import (
    DOWN,
    GREEN,
    LEFT,
    RIGHT,
    UP,
    WHITE,
    YELLOW,
    Arrow,
    Dot,
    Ellipse,
    FadeIn,
    FadeOut,
    Rectangle,
    RoundedRectangle,
    Text,
    VGroup,
    Write,
)

from shapes.base_scene import NotionScene
from shapes.boxes import property_box, scene_title, warning_box


def _wrap(text: str, width: int = 56) -> str:
    return "\n".join(textwrap.fill(line, width=width) for line in text.split("\n"))


def _bullets(items, font_size=22, color=WHITE, width=52):
    lines = VGroup(
        *[Text(f"• {_wrap(it, width=width)}", font_size=font_size, color=color) for it in items]
    )
    lines.arrange(DOWN, aligned_edge=LEFT, buff=0.22)
    return lines


def _schema_localisation():
    """Schéma simplifié d'une feuille : cellule du parenchyme avec
    chloroplastes, stomate (entrée CO2), xylème (entrée eau) et phloème
    (sortie glucose)."""
    cellule = RoundedRectangle(width=3.0, height=2.0, corner_radius=0.15, stroke_color=WHITE, stroke_width=2, fill_opacity=0)

    chloroplastes = VGroup(
        *[
            Ellipse(width=0.4, height=0.22, fill_color=GREEN, fill_opacity=0.85, stroke_color="#0F5A22", stroke_width=1)
            for _ in range(6)
        ]
    )
    positions = [(0.7, 0.5), (1.0, -0.1), (0.4, -0.6), (-0.4, 0.6), (0.0, 0.0), (-0.7, -0.4)]
    for chloro, (dx, dy) in zip(chloroplastes, positions):
        chloro.move_to(cellule.get_center() + [dx, dy, 0])

    label_cellule = Text("cellule du parenchyme\n(20 à 100 chloroplastes)", font_size=14, color=WHITE)
    label_cellule.next_to(cellule, UP, buff=0.25)

    fleche_co2 = Arrow(LEFT * 1.3, LEFT * 0.05, color="#5AA9E6", buff=0).scale(0.9)
    fleche_co2.next_to(cellule, LEFT, buff=0.1)
    label_co2 = Text("CO2 (stomate)", font_size=13, color="#5AA9E6").next_to(fleche_co2, DOWN, buff=0.1)

    fleche_eau = Arrow(DOWN * 1.1, UP * 0.05, color="#2E8B57", buff=0).scale(0.9)
    fleche_eau.next_to(cellule, DOWN, buff=0.1)
    label_eau = Text("eau (xylème)", font_size=13, color="#2E8B57").next_to(fleche_eau, DOWN, buff=0.1)

    fleche_glucose = Arrow(RIGHT * 0.05, RIGHT * 1.3, color=YELLOW, buff=0).scale(0.9)
    fleche_glucose.next_to(cellule, RIGHT, buff=0.1)
    label_glucose = Text("glucose (phloème)", font_size=13, color=YELLOW).next_to(fleche_glucose, UP, buff=0.1)

    return VGroup(
        cellule, chloroplastes, label_cellule,
        fleche_co2, label_co2, fleche_eau, label_eau, fleche_glucose, label_glucose,
    )


class ConversionEnergieEtLocalisation(NotionScene):
    def construct(self):
        titre = scene_title("10.1.4-10.2.1 — Conversion d'énergie et localisation")
        titre.scale(0.44)
        titre.to_edge(UP)

        # --- Énoncé : la photosynthèse, une conversion d'énergie ------------
        conversion = Text(
            _wrap(
                "L'énergie lumineuse (énergie radiante) captée par la "
                "chlorophylle est transformée en énergie chimique, "
                "stockée dans les liaisons de la molécule de glucose. "
                "La photosynthèse convertit donc une forme d'énergie en "
                "une autre.",
                width=56,
            ),
            font_size=23,
            color=WHITE,
        )
        conversion.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "La photosynthèse n'est pas seulement une fabrication de "
                "matière : c'est aussi une conversion d'énergie. "
                "L'énergie lumineuse, ou énergie radiante, captée par la "
                "chlorophylle, est transformée en énergie chimique, "
                "stockée dans les liaisons de la molécule de glucose."
            )
        ) as tracker:
            self.play(Write(titre))
            self.play(FadeIn(conversion))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(conversion))

        # --- Animation du raisonnement : trois propriétés du processus -------
        proprietes = property_box(
            _bullets(
                [
                    "Un processus d'anabolisme : fabrication de "
                    "molécules complexes (glucose) à partir de molécules "
                    "simples.",
                    "Un processus endergonique : il consomme de "
                    "l'énergie (celle de la lumière) au lieu d'en "
                    "libérer.",
                    "Le point d'entrée de l'énergie solaire dans le "
                    "monde vivant : toute la chaîne alimentaire en "
                    "dépend.",
                ],
                font_size=20,
                width=54,
            ),
            box_width=12.0,
        )
        proprietes.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "La photosynthèse est donc : un processus d'anabolisme, "
                "c'est-à-dire une fabrication de molécules complexes à "
                "partir de molécules simples ; un processus endergonique, "
                "qui consomme de l'énergie au lieu d'en libérer ; et "
                "surtout, le point d'entrée de l'énergie solaire dans le "
                "monde vivant. C'est cette énergie captée par les "
                "plantes qui, de proche en proche, alimente toutes les "
                "chaînes alimentaires de la planète."
            )
        ) as tracker:
            self.play(FadeIn(proprietes))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(proprietes))

        # --- Exemple traité : localisation dans la plante et la cellule ------
        localisation_texte = _bullets(
            [
                "La photosynthèse se déroule dans toutes les parties "
                "vertes de la plante, surtout les feuilles.",
                "Les cellules des parenchymes palissadique et lacuneux "
                "contiennent chacune 20 à 100 chloroplastes.",
                "Le CO2 entre par les stomates ; l'eau arrive par le "
                "xylème (sève brute) ; le glucose sort par le phloème "
                "(sève élaborée).",
            ],
            font_size=19,
            width=48,
        )
        localisation_texte.to_edge(LEFT, buff=0.5).shift(UP * 0.2)

        schema = _schema_localisation()
        schema.scale(0.95)
        schema.next_to(localisation_texte, RIGHT, buff=0.6)

        with self.voiceover(
            text=(
                "Où se déroule concrètement la photosynthèse ? Dans "
                "toutes les parties vertes de la plante, mais "
                "principalement dans les feuilles. À l'intérieur de la "
                "feuille, les cellules du parenchyme palissadique et du "
                "parenchyme lacuneux contiennent chacune de vingt à cent "
                "chloroplastes. Le dioxyde de carbone de l'air pénètre "
                "par de petits orifices, les stomates, situés surtout à "
                "la face inférieure de l'épiderme. L'eau arrive par les "
                "vaisseaux du xylème, c'est la sève brute. Le glucose "
                "fabriqué est exporté par les vaisseaux du phloème, la "
                "sève élaborée, vers toute la plante."
            )
        ) as tracker:
            self.play(FadeIn(localisation_texte))
            self.play(FadeIn(schema))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(localisation_texte), FadeOut(schema))

        # --- À retenir : synthèse en une phrase --------------------------------
        essentiel = property_box(
            Text(
                _wrap(
                    "À retenir : la photosynthèse convertit l'énergie "
                    "lumineuse en énergie chimique dans les chloroplastes "
                    "des cellules chlorophylliennes de la feuille, où se "
                    "rencontrent le CO2 (stomates), l'eau (xylème) et la "
                    "lumière, pour produire du glucose exporté par le "
                    "phloème.",
                    width=54,
                ),
                font_size=20,
            ),
            box_width=12.0,
        )
        essentiel.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Retenons l'essentiel : la photosynthèse convertit "
                "l'énergie lumineuse en énergie chimique, dans les "
                "chloroplastes des cellules chlorophylliennes de la "
                "feuille, là où se rencontrent le dioxyde de carbone "
                "venu des stomates, l'eau venue du xylème et la lumière "
                "du soleil, pour produire du glucose ensuite exporté par "
                "le phloème."
            )
        ) as tracker:
            self.play(FadeIn(essentiel))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(essentiel))

        # --- Piège à éviter : ne pas limiter la photosynthèse aux feuilles ---
        piege = warning_box(
            Text(
                _wrap(
                    "Piège à éviter : la photosynthèse n'a pas lieu "
                    "uniquement dans les feuilles. Toute partie verte de "
                    "la plante (jeune tige, sépale vert...) contenant des "
                    "chloroplastes est capable de photosynthèse, car "
                    "c'est la chlorophylle, pas la forme de l'organe, qui "
                    "est le critère déterminant.",
                    width=54,
                ),
                font_size=21,
            ),
            box_width=12.0,
        )
        piege.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Attention à un piège classique : la photosynthèse n'a "
                "pas lieu uniquement dans les feuilles. Toute partie "
                "verte de la plante, une jeune tige, un sépale vert, est "
                "capable de photosynthèse dès lors qu'elle contient des "
                "chloroplastes. C'est la présence de chlorophylle, et non "
                "la forme de l'organe, qui est le critère déterminant."
            )
        ) as tracker:
            self.play(FadeIn(piege))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(titre), FadeOut(piege))
