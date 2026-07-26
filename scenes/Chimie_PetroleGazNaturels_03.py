"""
scenes/Chimie_PetroleGazNaturels_03.py — Chapitre 5 « Pétrole et gaz
naturels » (1ereC, Chimie), scène 03.

§ 3. Le raffinage : principe de la distillation fractionnée. Définitions
(raffinage, distillation fractionnée), procédé en 5 étapes (chauffage au
four à 400°C → vapeurs en bas de colonne → condensation par plateaux
selon la température d'ébullition → hydrocarbures lourds en bas, légers
en haut → bitume résiduel), schéma de la colonne à plateaux avec
température décroissante, et propriété : plus la chaîne carbonée est
longue, plus la température d'ébullition est élevée.
Source : 1ereC/Chimie.pdf, chapitre 5, pages 47-48.
"""

import textwrap

from manim import (
    DOWN,
    LEFT,
    RIGHT,
    UP,
    WHITE,
    YELLOW,
    RED,
    ORANGE,
    BLUE,
    Arrow,
    FadeIn,
    FadeOut,
    Line,
    Rectangle,
    Text,
    VGroup,
    Write,
    config,
)

from shapes.base_scene import NotionScene
from shapes.boxes import definition_box, property_box, scene_title


def _wrap(text: str, width: int = 56) -> str:
    return "\n".join(textwrap.fill(line, width=width) for line in text.split("\n"))


def _fit(mobject, top_y):
    bas_visible = -config.frame_height / 2 + 0.25
    hauteur_dispo = top_y - bas_visible
    if mobject.height > hauteur_dispo:
        mobject.scale(hauteur_dispo / mobject.height, about_point=mobject.get_top())
    return mobject


def _bullets(items, font_size=22, color=WHITE, width=52):
    lines = VGroup(
        *[Text(f"{i+1}) {_wrap(it, width=width)}", font_size=font_size, color=color) for i, it in enumerate(items)]
    )
    lines.arrange(DOWN, aligned_edge=LEFT, buff=0.25)
    return lines


def _colonne_plateaux():
    largeur = 2.6
    hauteur = 5.2
    colonne = Rectangle(width=largeur, height=hauteur, color=WHITE, stroke_width=2)

    n_plateaux = 5
    plateaux = VGroup()
    for i in range(1, n_plateaux):
        y = colonne.get_top()[1] - i * hauteur / n_plateaux
        plateau = Line(
            colonne.get_left() + [0, y - colonne.get_center()[1], 0],
            colonne.get_right() + [0, y - colonne.get_center()[1], 0],
            color=BLUE,
            stroke_width=1.5,
        )
        plateaux.add(plateau)

    four = Rectangle(width=largeur, height=0.7, fill_color=RED, fill_opacity=0.85, stroke_color=WHITE)
    four.next_to(colonne, DOWN, buff=0.15)
    label_four = Text("Four (≈400°C)", font_size=15, color=WHITE)
    label_four.next_to(four, DOWN, buff=0.15)

    label_haut = Text("légers\n(basse Téb)\nvapeurs froides", font_size=13, color=BLUE)
    label_haut.next_to(colonne, RIGHT, buff=0.7).align_to(colonne, UP)
    fleche_haut = Arrow(colonne.get_top() + RIGHT * 0.3, label_haut.get_left(), buff=0.1, color=WHITE, stroke_width=2)

    label_bas = Text("lourds\n(haute Téb)\nliquides chauds", font_size=13, color=ORANGE)
    label_bas.next_to(colonne, RIGHT, buff=0.7).align_to(colonne, DOWN)
    fleche_bas = Arrow(colonne.get_bottom() + RIGHT * 0.3 + UP * 0.2, label_bas.get_left(), buff=0.1, color=WHITE, stroke_width=2)

    gradient_label = Text("Température décroissante ↑", font_size=13, color=YELLOW)
    gradient_label.rotate(90 * 3.14159 / 180)
    gradient_label.next_to(colonne, LEFT, buff=0.35)

    return VGroup(colonne, plateaux, four, label_four, label_haut, fleche_haut, label_bas, fleche_bas, gradient_label)


class RaffinageDistillationFractionnee(NotionScene):
    def construct(self):
        titre = scene_title("3. Le raffinage : la distillation fractionnée")
        titre.scale(0.5)
        titre.to_edge(UP)

        # --- Énoncé : définitions raffinage + distillation fractionnée --------
        definition = definition_box(
            VGroup(
                Text(
                    _wrap(
                        "Raffinage : ensemble des opérations qui "
                        "transforment le pétrole brut en produits "
                        "utilisables (carburants, bitume, etc.).",
                        width=50,
                    ),
                    font_size=22,
                ),
                Text(
                    _wrap(
                        "Distillation fractionnée : première étape du "
                        "raffinage, qui sépare le brut en fractions selon "
                        "leur température d'ébullition.",
                        width=50,
                    ),
                    font_size=22,
                ),
            ).arrange(DOWN, aligned_edge=LEFT, buff=0.35),
            box_width=11.5,
        )
        definition.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Le raffinage regroupe l'ensemble des opérations qui "
                "transforment le pétrole brut en produits utilisables : "
                "carburants, bitume, et bien d'autres. La première étape "
                "de ce raffinage est la distillation fractionnée, qui "
                "sépare le brut en fractions selon leur température "
                "d'ébullition."
            )
        ) as tracker:
            self.play(Write(titre))
            self.play(FadeIn(definition))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(definition))

        # --- Raisonnement : le procédé en 5 étapes ------------------------------
        entete_etapes = Text("Le procédé, en 5 étapes", font_size=24, color=YELLOW, weight="BOLD")
        entete_etapes.next_to(titre, DOWN, buff=0.35)

        etapes = _bullets(
            [
                "Le pétrole brut est chauffé dans un four à environ 400°C",
                "Les vapeurs obtenues entrent en bas d'une colonne de distillation",
                "En montant, elles se condensent sur des plateaux, selon leur température d'ébullition",
                "Les hydrocarbures lourds se recueillent en bas, les légers en haut",
                "Le résidu non vaporisé, le bitume, reste tout en bas de la colonne",
            ],
            font_size=19,
            width=54,
        )
        etapes.next_to(entete_etapes, DOWN, buff=0.35)
        _fit(etapes, entete_etapes.get_bottom()[1] - 0.3)

        with self.voiceover(
            text=(
                "Le procédé se déroule en cinq étapes. Un : le pétrole "
                "brut est chauffé dans un four à environ quatre cents "
                "degrés Celsius. Deux : les vapeurs ainsi obtenues entrent "
                "en bas d'une haute colonne de distillation. Trois : en "
                "montant dans la colonne, qui devient de plus en plus "
                "froide, ces vapeurs se condensent sur des plateaux, "
                "chacune à la hauteur correspondant à sa température "
                "d'ébullition. Quatre : les hydrocarbures lourds se "
                "recueillent donc en bas de la colonne, et les plus "
                "légers tout en haut. Cinq : le résidu qui n'a jamais été "
                "vaporisé, le bitume, reste tout en bas."
            )
        ) as tracker:
            self.play(FadeIn(entete_etapes))
            self.play(FadeIn(etapes))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(entete_etapes), FadeOut(etapes))

        # --- Exemple traité : schéma de la colonne à plateaux -------------------
        entete_colonne = Text("La colonne à plateaux", font_size=24, color=YELLOW, weight="BOLD")
        entete_colonne.next_to(titre, DOWN, buff=0.3)

        colonne = _colonne_plateaux()
        colonne.next_to(entete_colonne, DOWN, buff=0.35)
        _fit(colonne, entete_colonne.get_bottom()[1] - 0.25)

        with self.voiceover(
            text=(
                "Voici le schéma d'une colonne à plateaux. Le pétrole "
                "chauffé entre par le four, en bas. La température "
                "décroît progressivement du bas vers le haut de la "
                "colonne. Les hydrocarbures lourds, à haute température "
                "d'ébullition, se condensent dès les premiers plateaux, "
                "en bas, sous forme de liquides chauds. Les hydrocarbures "
                "légers, à basse température d'ébullition, ne se "
                "condensent que tout en haut, où la colonne est la plus "
                "froide."
            )
        ) as tracker:
            self.play(FadeIn(entete_colonne))
            self.play(FadeIn(colonne))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(entete_colonne), FadeOut(colonne))

        # --- À retenir : plus la chaîne est longue, plus Téb est élevée --------
        propriete = property_box(
            Text(
                _wrap(
                    "Plus la chaîne carbonée d'un hydrocarbure est longue, "
                    "plus sa température d'ébullition est élevée : c'est "
                    "ce principe qui permet à la colonne de séparer le "
                    "pétrole en fractions.",
                    width=48,
                ),
                font_size=23,
            ),
        )
        propriete.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Retenons le principe physique à l'œuvre : plus la "
                "chaîne carbonée d'un hydrocarbure est longue, plus sa "
                "température d'ébullition est élevée. C'est précisément "
                "ce principe qui permet à la colonne de séparer le "
                "pétrole brut en fractions distinctes, chacune "
                "correspondant à une gamme de longueurs de chaîne."
            )
        ) as tracker:
            self.play(FadeIn(propriete))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(propriete), FadeOut(titre))
