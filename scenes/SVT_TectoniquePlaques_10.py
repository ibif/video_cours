"""
scenes/SVT_TectoniquePlaques_10.py — Chapitre 8 (1ereC, SVT), scène 10.

IV.B.2 Les frontières convergentes (2/2) — la collision : mécanisme
(disparition de l'océan, raccourcissement, épaississement, racine
crustale, chaîne de montagnes, ligne de suture), séismes superficiels
sans volcanisme, exemples (Himalaya, Alpes) + Exemple résolu 2 (identifier
le type de frontière : fosse Pérou-Chili → subduction Nazca / Amérique du
Sud). Source : 1ereC/SVT.pdf, page 91.
"""

import textwrap

from manim import (
    DOWN,
    LEFT,
    ORANGE,
    RIGHT,
    UP,
    WHITE,
    YELLOW,
    Arrow,
    Create,
    FadeIn,
    FadeOut,
    GRAY_C,
    Polygon,
    Text,
    VGroup,
    Write,
)

from shapes.base_scene import NotionScene
from shapes.boxes import corrige_box, exercise_box, scene_title


def _wrap(text: str, width: int = 56) -> str:
    return "\n".join(textwrap.fill(line, width=width) for line in text.split("\n"))


def _bullets(items, font_size=24, color=WHITE, width=54):
    lines = VGroup(
        *[Text(f"• {_wrap(it, width=width)}", font_size=font_size, color=color) for it in items]
    )
    lines.arrange(DOWN, aligned_edge=LEFT, buff=0.22)
    return lines


class FrontieresConvergentesCollision(NotionScene):
    def construct(self):
        titre = scene_title("IV.B La collision (frontière convergente 2/2)")
        titre.scale(0.55)
        titre.to_edge(UP)
        self.play(Write(titre))

        # --- Énoncé : le mécanisme de la collision ------------------------------
        mecanisme = _bullets(
            [
                "Après disparition de l'océan par subduction, les deux "
                "continents entrent en contact. Leurs densités, proches et "
                "trop faibles, les empêchent de plonger.",
                "La convergence se traduit par un raccourcissement (plis, "
                "chevauchements) et un épaississement de la croûte "
                "(racine crustale) → chaîne de montagnes. L'ancienne mer "
                "disparue laisse une ligne de suture.",
            ],
            font_size=21,
            width=52,
        )
        mecanisme.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Après la disparition complète de l'océan par subduction, "
                "les deux continents entrent en contact. Leurs densités, "
                "proches et trop faibles, les empêchent de plonger l'un "
                "sous l'autre : c'est la collision. La convergence se "
                "traduit alors par un raccourcissement, plis et "
                "chevauchements, et un épaississement de la croûte, avec "
                "formation d'une racine crustale, ce qui édifie une chaîne "
                "de montagnes. L'ancienne mer disparue laisse une trace, "
                "une ligne de suture."
            )
        ) as tracker:
            self.play(FadeIn(mecanisme))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(mecanisme))

        # --- Animation du raisonnement : schéma de la collision -----------------
        plaque_g = Polygon(
            [-4.5, 0.4, 0], [-1.3, 0.4, 0], [-1.0, -1.8, 0], [-4.5, -1.8, 0],
            fill_color=ORANGE, fill_opacity=0.7, stroke_color=WHITE, stroke_width=1,
        )
        plaque_d = Polygon(
            [4.5, 0.4, 0], [1.3, 0.4, 0], [1.0, -1.8, 0], [4.5, -1.8, 0],
            fill_color=GRAY_C, fill_opacity=0.7, stroke_color=WHITE, stroke_width=1,
        )
        chaine = Polygon(
            [-1.3, 0.4, 0], [-0.6, 1.6, 0], [0.6, 1.6, 0], [1.3, 0.4, 0],
            fill_color=ORANGE, fill_opacity=0.9, stroke_color=WHITE, stroke_width=1,
        )
        racine = Polygon(
            [-1.0, -1.8, 0], [-0.4, -3.0, 0], [0.4, -3.0, 0], [1.0, -1.8, 0],
            fill_color=GRAY_C, fill_opacity=0.6, stroke_color=WHITE, stroke_width=1,
        )
        label_chaine = Text("chaîne de montagnes", font_size=14, color=WHITE).next_to(chaine, UP, buff=0.15)
        label_racine = Text("racine crustale\n(épaississement)", font_size=13, color=WHITE).next_to(racine, DOWN, buff=0.15)
        label_suture = Text("suture", font_size=13, color=YELLOW).move_to([0, 0.3, 0])

        fleche_g = Arrow(start=[-3.5, 0.9, 0], end=[-1.8, 0.9, 0], color=WHITE, buff=0, stroke_width=3)
        fleche_d = Arrow(start=[3.5, 0.9, 0], end=[1.8, 0.9, 0], color=WHITE, buff=0, stroke_width=3)

        schema = VGroup(
            plaque_g, plaque_d, chaine, racine, label_chaine, label_racine,
            label_suture, fleche_g, fleche_d,
        )
        schema.scale(0.85)
        schema.next_to(titre, DOWN, buff=0.6)

        with self.voiceover(
            text=(
                "On observe des séismes superficiels, répartis sur une "
                "large zone, mais aucun volcanisme, faute de fusion de "
                "matériau : les deux plaques, continentales, sont trop peu "
                "denses pour plonger et fondre."
            )
        ) as tracker:
            self.play(FadeIn(plaque_g), FadeIn(plaque_d))
            self.play(Create(fleche_g), Create(fleche_d))
            self.play(FadeIn(chaine), FadeIn(label_chaine))
            self.play(FadeIn(racine), FadeIn(label_racine), FadeIn(label_suture))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(schema))

        # --- Exemple traité : Himalaya, Alpes -----------------------------------
        exemples = _bullets(
            [
                "Himalaya : collision Inde-Eurasie depuis ~50 Ma, "
                "convergence actuelle ~4 à 5 cm/an.",
                "Alpes : poussée de la plaque africaine vers l'Europe.",
            ],
            font_size=22,
            width=52,
        )
        exemples.next_to(titre, DOWN, buff=0.55)

        with self.voiceover(
            text=(
                "Deux exemples célèbres : l'Himalaya, issu de la collision "
                "entre l'Inde et l'Eurasie depuis environ cinquante "
                "millions d'années, avec une convergence actuelle "
                "d'environ quatre à cinq centimètres par an ; et les Alpes, "
                "issues de la poussée de la plaque africaine vers "
                "l'Europe."
            )
        ) as tracker:
            self.play(FadeIn(exemples))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(exemples))

        # --- À retenir / exemple résolu 2 : identifier une frontière -----------
        enonce_ex2 = exercise_box(
            Text(
                _wrap(
                    "Exemple résolu 2 : au large de l'Amérique du Sud, on "
                    "observe une fosse océanique très profonde (fosse du "
                    "Pérou-Chili, ~8000 m), des séismes dont les foyers "
                    "s'enfoncent vers l'Est jusqu'à 600 km, et une chaîne de "
                    "volcans explosifs (les Andes). Identifier le type de "
                    "frontière et décrire le processus en jeu.",
                    width=54,
                ),
                font_size=20,
            ),
            box_width=12.2,
        )
        enonce_ex2.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Mettons nos connaissances en pratique. Énoncé : au large "
                "de la côte ouest de l'Amérique du Sud, on observe une "
                "fosse océanique très profonde, la fosse du Pérou-Chili, "
                "environ huit mille mètres, des séismes dont les foyers "
                "s'enfoncent vers l'Est jusqu'à six cents kilomètres de "
                "profondeur, et une chaîne de volcans explosifs, les Andes. "
                "Identifions le type de frontière et décrivons le processus "
                "en jeu."
            )
        ) as tracker:
            self.play(FadeIn(enonce_ex2))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(enonce_ex2))

        correction = corrige_box(
            Text(
                _wrap(
                    "La présence conjointe d'une fosse, de séismes de "
                    "profondeur croissante et d'un volcanisme explosif "
                    "caractérise une convergence avec subduction. La plaque "
                    "de Nazca (océanique, dense) plonge vers l'Est sous la "
                    "plaque sud-américaine (continentale) : la fosse marque "
                    "le lieu d'enfoncement, les foyers dessinent le plan de "
                    "Wadati-Benioff, et la fusion au-dessus de la plaque "
                    "plongeante alimente les volcans andésitiques des "
                    "Andes.",
                    width=54,
                ),
                font_size=19,
            ),
            box_width=12.4,
        )
        correction.next_to(titre, DOWN, buff=0.55)

        with self.voiceover(
            text=(
                "Correction : la présence conjointe d'une fosse, de séismes "
                "de profondeur croissante, et d'un volcanisme explosif, "
                "caractérise une convergence avec subduction. La plaque de "
                "Nazca, océanique et dense, plonge vers l'Est sous la "
                "plaque sud-américaine, continentale. La fosse marque le "
                "lieu d'enfoncement, les foyers dessinent le plan de "
                "Wadati-Benioff, et la fusion au-dessus de la plaque "
                "plongeante alimente les volcans andésitiques des Andes. "
                "Attention à ne pas confondre avec une collision : ici, il "
                "y a bien un volcanisme actif et une fosse, deux signatures "
                "absentes d'une collision comme celle de l'Himalaya."
            )
        ) as tracker:
            self.play(FadeIn(correction))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(correction), FadeOut(titre))
