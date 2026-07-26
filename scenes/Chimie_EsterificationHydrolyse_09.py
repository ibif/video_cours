"""
scenes/Chimie_EsterificationHydrolyse_09.py — Chapitre 8 « Estérification et
hydrolyse d'un ester » (1ereC, Chimie), scène 09.

§ Comment augmenter le rendement ? Éliminer l'eau ou l'ester formé.
Distillation de l'ester au fur et à mesure (exemple éthanoate de méthyle
Téb=57°C). Élimination de l'eau par déshydratant. Exemple résolu 3 (acide
méthanoïque 101°C + éthanol 78°C → méthanoate d'éthyle 54°C, protocole de
distillation sélective pour rendement ≈100%).
Source : 1ereC/Chimie.pdf, chapitre 8, page 81.
"""

import textwrap

from manim import (
    DOWN,
    UP,
    WHITE,
    YELLOW,
    GREEN,
    FadeIn,
    FadeOut,
    MathTex,
    Text,
    VGroup,
    Write,
    config,
)

from shapes.base_scene import NotionScene
from shapes.boxes import example_box, scene_title


def _wrap(text: str, width: int = 56) -> str:
    return "\n".join(textwrap.fill(line, width=width) for line in text.split("\n"))


def _fit(mobject, top_y):
    bas_visible = -config.frame_height / 2 + 0.25
    hauteur_dispo = top_y - bas_visible
    if mobject.height > hauteur_dispo:
        mobject.scale(hauteur_dispo / mobject.height, about_point=mobject.get_top())
    return mobject


class AugmenterRendementEliminationProduit(NotionScene):
    def construct(self):
        titre = scene_title("9. Augmenter le rendement : éliminer un produit")
        titre.scale(0.48)
        titre.to_edge(UP)

        # --- Énoncé -----------------------------------------------------------
        enonce = Text(
            _wrap(
                "Le second levier ne consiste pas à ajouter un réactif, "
                "mais à faire l'inverse : retirer un produit au fur et à "
                "mesure qu'il se forme.",
                width=54,
            ),
            font_size=25,
            color=WHITE,
        )
        enonce.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Le second levier ne consiste pas à ajouter un réactif, "
                "mais à faire l'inverse : retirer un produit au fur et à "
                "mesure qu'il se forme. D'après la loi de déplacement "
                "d'équilibre vue précédemment, retirer un produit "
                "déplace lui aussi l'équilibre dans le sens direct."
            )
        ) as tracker:
            self.play(Write(titre))
            self.play(FadeIn(enonce))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(enonce))

        # --- Raisonnement : deux façons de retirer un produit -----------------------
        entete = Text("Deux façons de retirer un produit", font_size=24, color=YELLOW, weight="BOLD")
        entete.next_to(titre, DOWN, buff=0.4)

        methode1 = Text(
            _wrap(
                "1) Distiller l'ester au fur et à mesure de sa formation "
                "— possible s'il est plus volatil que l'acide et l'alcool "
                "(exemple : éthanoate de méthyle, Téb = 57°C).",
                width=48,
            ),
            font_size=21,
            color=WHITE,
        )
        methode2 = Text(
            _wrap(
                "2) Éliminer l'eau formée avec un agent déshydratant "
                "(qui la piège chimiquement au fur et à mesure).",
                width=48,
            ),
            font_size=21,
            color=WHITE,
        )
        bloc = VGroup(methode1, methode2).arrange(DOWN, buff=0.35)
        bloc.next_to(entete, DOWN, buff=0.4)
        groupe = VGroup(entete, bloc)
        _fit(groupe, titre.get_bottom()[1] - 0.4)

        with self.voiceover(
            text=(
                "Il existe deux façons de procéder. Première méthode : "
                "distiller l'ester au fur et à mesure de sa formation, "
                "ce qui est possible lorsqu'il est plus volatil que "
                "l'acide et l'alcool restants. C'est le cas, par exemple, "
                "de l'éthanoate de méthyle, dont le point d'ébullition, "
                "seulement cinquante-sept degrés, est nettement plus bas "
                "que celui des réactifs. Seconde méthode : éliminer "
                "l'eau formée à l'aide d'un agent déshydratant, qui la "
                "piège chimiquement au fur et à mesure."
            )
        ) as tracker:
            self.play(FadeIn(entete))
            self.play(FadeIn(methode1))
            self.play(FadeIn(methode2))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(groupe))

        # --- Exemple résolu 3 : distillation sélective ------------------------------
        exemple = example_box(
            VGroup(
                Text(
                    "Acide méthanoïque (Téb = 101°C) + éthanol (Téb = 78°C)",
                    font_size=20,
                    weight="BOLD",
                ),
                MathTex(
                    r"HCOOH + C_2H_5-OH \;\rightleftharpoons\; HCOO-C_2H_5 + H_2O",
                    font_size=24,
                ),
                Text(
                    "→ méthanoate d'éthyle formé, Téb = 54°C",
                    font_size=20,
                    color=GREEN,
                ),
                Text(
                    _wrap(
                        "Le méthanoate d'éthyle, nettement plus volatil que "
                        "les 2 réactifs, distille en continu au fur et à "
                        "mesure de sa formation : l'équilibre est déplacé "
                        "en permanence vers le sens direct, jusqu'à un "
                        "rendement proche de 100 %.",
                        width=46,
                    ),
                    font_size=19,
                ),
            ).arrange(DOWN, buff=0.28),
            box_width=12.2,
        )
        exemple.next_to(titre, DOWN, buff=0.4)
        _fit(exemple, titre.get_bottom()[1] - 0.4)

        with self.voiceover(
            text=(
                "Voyons un exemple résolu complet. On fait réagir l'acide "
                "méthanoïque, point d'ébullition cent un degrés, avec "
                "l'éthanol, point d'ébullition soixante-dix-huit degrés. "
                "Il se forme le méthanoate d'éthyle, dont le point "
                "d'ébullition n'est que de cinquante-quatre degrés : "
                "nettement plus bas que celui des deux réactifs. En "
                "chauffant le mélange à une température bien choisie, le "
                "méthanoate d'éthyle distille en continu, dès qu'il se "
                "forme, avant même d'avoir le temps de subir "
                "l'hydrolyse inverse. L'équilibre est ainsi déplacé en "
                "permanence vers le sens direct, et l'on obtient, par ce "
                "protocole de distillation sélective, un rendement "
                "proche de cent pour cent."
            )
        ) as tracker:
            self.play(FadeIn(exemple))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(exemple))

        # --- À retenir ----------------------------------------------------------------
        retenir = Text(
            _wrap(
                "Ajouter un réactif en excès OU retirer un produit formé : "
                "ces deux leviers, tous deux fondés sur le déplacement "
                "d'équilibre, permettent d'augmenter le rendement d'une "
                "estérification, sans jamais dépasser 100 % puisqu'on "
                "reste limité par les quantités de réactifs disponibles.",
                width=50,
            ),
            font_size=22,
            color=WHITE,
        )
        retenir.next_to(titre, DOWN, buff=0.5)
        _fit(retenir, titre.get_bottom()[1] - 0.5)

        with self.voiceover(
            text=(
                "Retenons donc ces deux leviers, tous deux fondés sur le "
                "déplacement d'équilibre : ajouter un réactif en excès, "
                "ou retirer un produit formé. Chacun permet d'augmenter "
                "le rendement d'une estérification, sans jamais dépasser "
                "cent pour cent, puisqu'on reste toujours limité par les "
                "quantités de réactifs réellement disponibles."
            )
        ) as tracker:
            self.play(FadeIn(retenir))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(retenir), FadeOut(titre))
