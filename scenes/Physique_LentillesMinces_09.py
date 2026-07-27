"""
scenes/Physique_LentillesMinces_09.py — Chapitre 13 « Les lentilles minces »
(1ereC, Physique), scène 09.

§ Grandissement γ = A'B'/AB = OA'/OA (sans unité). Tableau d'interprétation
du signe et de la valeur (γ<0 renversée, γ>0 droite, |γ|>1 agrandie,
|γ|<1 réduite, |γ|=1 même taille). Exemple résolu 2 complet : lentille
convergente f' = +5 cm, objet AB = 2 cm à 15 cm → OA' = +7,5 cm (réelle),
γ = -0,5 (renversée, 2× plus petite, taille 1 cm).
Source : 1ereC/Physique.pdf, pages 130-140 (chapitre 13, § 4).
"""

import textwrap

from manim import (
    DOWN,
    LEFT,
    RIGHT,
    UP,
    YELLOW,
    BLUE,
    FadeIn,
    FadeOut,
    MathTex,
    Text,
    VGroup,
    Write,
)

from shapes.base_scene import NotionScene
from shapes.boxes import definition_box, essentiel_box, example_box, scene_title, warning_box


def _wrap(text: str, width: int = 56) -> str:
    return "\n".join(textwrap.fill(line, width=width) for line in text.split("\n"))


class Grandissement(NotionScene):
    def construct(self):
        titre = scene_title("Le grandissement")
        titre.scale(0.48)
        titre.to_edge(UP)
        self.play(Write(titre))

        # --- Énoncé : définition -----------------------------------------------------
        definition = definition_box(
            VGroup(
                Text("Grandissement", font_size=23, weight="BOLD"),
                MathTex(r"\gamma = \dfrac{\overline{A'B'}}{\overline{AB}} = \dfrac{\overline{OA'}}{\overline{OA}}", font_size=32),
                Text("grandeur algébrique, SANS UNITÉ.", font_size=20),
            ).arrange(DOWN, buff=0.28),
            box_width=9.6,
        )
        definition.next_to(titre, DOWN, buff=0.45)

        with self.voiceover(
            text=(
                "Le grandissement, noté gamma, compare la taille de "
                "l'image à celle de l'objet. Il est défini par gamma "
                "égale A prime B prime sur A B, ce qui est égal, d'après "
                "la géométrie de la construction, à O A prime sur O A. "
                "C'est une grandeur algébrique, sans unité."
            )
        ) as tracker:
            self.play(FadeIn(definition))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(definition))

        # --- Raisonnement : interprétation du signe et de la valeur ------------------
        table = VGroup(
            VGroup(
                MathTex(r"\gamma < 0", font_size=24, color=YELLOW),
                Text("image renversée", font_size=19),
            ).arrange(RIGHT, buff=0.4),
            VGroup(
                MathTex(r"\gamma > 0", font_size=24, color=YELLOW),
                Text("image droite", font_size=19),
            ).arrange(RIGHT, buff=0.4),
            VGroup(
                MathTex(r"|\gamma| > 1", font_size=24, color=BLUE),
                Text("image agrandie", font_size=19),
            ).arrange(RIGHT, buff=0.4),
            VGroup(
                MathTex(r"|\gamma| < 1", font_size=24, color=BLUE),
                Text("image réduite", font_size=19),
            ).arrange(RIGHT, buff=0.4),
            VGroup(
                MathTex(r"|\gamma| = 1", font_size=24, color=BLUE),
                Text("même taille que l'objet", font_size=19),
            ).arrange(RIGHT, buff=0.4),
        ).arrange(DOWN, buff=0.28, aligned_edge=LEFT)
        table.next_to(titre, DOWN, buff=0.55)

        with self.voiceover(
            text=(
                "Le signe et la valeur absolue de gamma renseignent "
                "complètement sur l'image. Si gamma est négatif, l'image "
                "est renversée. Si gamma est positif, l'image est droite. "
                "Si la valeur absolue de gamma est supérieure à 1, "
                "l'image est agrandie. Si elle est inférieure à 1, "
                "l'image est réduite. Et si elle vaut exactement 1, "
                "l'image a la même taille que l'objet."
            )
        ) as tracker:
            for ligne in table:
                self.play(Write(ligne), run_time=0.8)
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(table))

        # --- Exemple résolu 2 -------------------------------------------------------------
        exemple = example_box(
            VGroup(
                Text("Lentille convergente f' = +5 cm, AB = 2 cm, OA = -15 cm.", font_size=19),
                MathTex(
                    r"\dfrac{1}{\overline{OA'}} = \dfrac{1}{f'} + \dfrac{1}{\overline{OA}} = \dfrac{1}{5} - \dfrac{1}{15} = \dfrac{2}{15}",
                    font_size=23,
                ),
                MathTex(r"\overline{OA'} = +7{,}5\ \text{cm} \quad (\text{image réelle})", font_size=23, color=YELLOW),
                MathTex(r"\gamma = \dfrac{\overline{OA'}}{\overline{OA}} = \dfrac{7{,}5}{-15} = -0{,}5", font_size=23, color=YELLOW),
                Text("Image renversée, 2× plus petite, taille |A'B'| = 1 cm.", font_size=19),
            ).arrange(DOWN, buff=0.18),
            box_width=11.6,
        )
        exemple.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Exemple résolu. Une lentille convergente a une distance "
                "focale f prime égale à plus 5 centimètres. L'objet A B "
                "mesure 2 centimètres, et O A vaut moins 15 centimètres. "
                "La formule de Descartes donne un sur O A prime égale un "
                "sur 5, moins un sur 15, soit 2 sur 15. On en tire O A "
                "prime égale plus 7,5 centimètres : l'image est réelle. "
                "Le grandissement gamma vaut O A prime sur O A, soit 7,5 "
                "divisé par moins 15, c'est-à-dire moins 0,5. L'image est "
                "donc renversée, deux fois plus petite que l'objet, de "
                "taille 1 centimètre."
            )
        ) as tracker:
            self.play(FadeIn(exemple))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(exemple))

        # --- À retenir --------------------------------------------------------------
        retenir = essentiel_box(
            VGroup(
                Text("À retenir", font_size=23, weight="BOLD"),
                MathTex(r"\gamma = \dfrac{\overline{A'B'}}{\overline{AB}} = \dfrac{\overline{OA'}}{\overline{OA}}", font_size=28),
                Text("signe → sens ; valeur absolue → taille relative.", font_size=19),
            ).arrange(DOWN, buff=0.22),
            box_width=10.6,
        )
        retenir.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Retenons l'essentiel : le grandissement gamma égale A "
                "prime B prime sur A B, égale O A prime sur O A. Son "
                "signe donne le sens de l'image, sa valeur absolue donne "
                "la taille relative de l'image par rapport à l'objet."
            )
        ) as tracker:
            self.play(FadeIn(retenir))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(retenir))

        # --- Piège --------------------------------------------------------------------
        piege = warning_box(
            VGroup(
                Text("• γ compare des mesures ALGÉBRIQUES : ne pas prendre", font_size=19),
                Text("   les valeurs absolues avant de calculer le rapport,", font_size=19),
                Text("   sous peine de perdre l'information de sens (droite", font_size=19),
                Text("   ou renversée).", font_size=19),
                Text("• AB est la taille de l'objet, prise ici positive par", font_size=19),
                Text("   convention (objet dressé vers le haut) : ne pas la", font_size=19),
                Text("   confondre avec OA, la position de l'objet.", font_size=19),
            ).arrange(DOWN, aligned_edge=LEFT, buff=0.12),
            box_width=12.0,
        )
        piege.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Piège à éviter : le grandissement compare des mesures "
                "algébriques. Il ne faut jamais prendre les valeurs "
                "absolues avant de calculer le rapport, sous peine de "
                "perdre l'information de sens, droite ou renversée. Et il "
                "ne faut pas confondre A B, la taille de l'objet, avec O "
                "A, qui est la position de l'objet sur l'axe."
            )
        ) as tracker:
            self.play(FadeIn(piege))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(piege), FadeOut(titre))
