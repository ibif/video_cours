"""
scenes/Chimie_ComposesOxygenes_08.py — Chapitre 6 « Quelques composés
oxygénés » (1ereC, Chimie), scène 08.

§ L'oxydation ménagée des alcools — théorie : définition (conserve le
squelette carboné), 3 moyens (oxydant en solution, O2 de l'air + Cu,
déshydrogénation catalytique), résultats selon la classe (théorème).
Source : 1ereC/Chimie.pdf, chapitre 6, pages 62-63.
"""

import textwrap

from manim import (
    DOWN,
    LEFT,
    RIGHT,
    UP,
    WHITE,
    YELLOW,
    FadeIn,
    FadeOut,
    MathTex,
    Text,
    VGroup,
    Write,
    config,
)

from shapes.base_scene import NotionScene
from shapes.boxes import definition_box, scene_title, theorem_box


def _wrap(text: str, width: int = 56) -> str:
    return "\n".join(textwrap.fill(line, width=width) for line in text.split("\n"))


def _bullets(items, font_size=22, color=WHITE, width=52):
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


class OxydationMenageeTheorie(NotionScene):
    def construct(self):
        titre = scene_title("L'oxydation ménagée des alcools")
        titre.scale(0.6)
        titre.to_edge(UP)

        # --- Énoncé : définition -----------------------------------------------------
        definition = definition_box(
            Text(
                _wrap(
                    "Une oxydation ménagée est une oxydation douce qui "
                    "transforme le groupe -OH d'un alcool sans jamais "
                    "briser le squelette carboné (les liaisons C-C "
                    "restent intactes).",
                    width=48,
                ),
                font_size=23,
            ),
        )
        definition.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Nous avons classé les alcools en trois familles. Voyons "
                "maintenant pourquoi cette classification est essentielle : "
                "elle détermine ce qui se passe lors de leur oxydation "
                "ménagée. Une oxydation ménagée est une oxydation douce, "
                "qui transforme uniquement le groupe hydroxyle d'un "
                "alcool, sans jamais briser le squelette carboné : les "
                "liaisons carbone-carbone restent toujours intactes."
            )
        ) as tracker:
            self.play(Write(titre))
            self.play(FadeIn(definition))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(definition))

        # --- Raisonnement : les trois moyens d'oxyder ---------------------------------
        moyens_titre = Text("Trois moyens de réaliser une oxydation ménagée", font_size=22, color=YELLOW, weight="BOLD")
        moyens_titre.next_to(titre, DOWN, buff=0.35)

        moyens = _bullets(
            [
                "un oxydant en solution acidifiée : permanganate de "
                "potassium KMnO₄, ou dichromate de potassium K₂Cr₂O₇ ;",
                "le dioxygène de l'air, en présence d'un catalyseur "
                "au cuivre ;",
                "la déshydrogénation catalytique : le catalyseur (cuivre "
                "chaud) arrache un H₂ sans intervention d'un oxydant.",
            ],
            width=48,
        )
        moyens.next_to(moyens_titre, DOWN, buff=0.4)

        groupe_moyens = VGroup(moyens_titre, moyens)
        _fit(groupe_moyens, titre.get_bottom()[1] - 0.4)

        with self.voiceover(
            text=(
                "Il existe trois moyens principaux de réaliser une "
                "oxydation ménagée. Premièrement, un oxydant en solution "
                "acidifiée, comme le permanganate de potassium ou le "
                "dichromate de potassium. Deuxièmement, le dioxygène de "
                "l'air, en présence d'un catalyseur au cuivre. "
                "Troisièmement, la déshydrogénation catalytique : le "
                "catalyseur, du cuivre chaud, arrache directement une "
                "molécule de dihydrogène, sans intervention d'un oxydant "
                "extérieur."
            )
        ) as tracker:
            self.play(FadeIn(moyens_titre))
            self.play(FadeIn(moyens))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(groupe_moyens))

        # --- Exemple traité / théorème : résultats selon la classe --------------------
        resultats = theorem_box(
            VGroup(
                Text("Alcool primaire →  aldéhyde  → (si excès) → acide carboxylique", font_size=19),
                Text("Alcool secondaire →  cétone  (l'oxydation s'arrête là)", font_size=19),
                Text("Alcool tertiaire →  PAS d'oxydation ménagée possible", font_size=19),
            ).arrange(DOWN, buff=0.32, aligned_edge=LEFT),
            box_width=12.0,
        )
        resultats.next_to(titre, DOWN, buff=0.4)
        _fit(resultats, titre.get_bottom()[1] - 0.4)

        with self.voiceover(
            text=(
                "Voici le résultat central de ce chapitre, à connaître "
                "parfaitement. Un alcool primaire s'oxyde d'abord en "
                "aldéhyde, puis, si l'oxydant est en excès, cet aldéhyde "
                "s'oxyde à son tour en acide carboxylique. Un alcool "
                "secondaire s'oxyde en cétone, et l'oxydation s'arrête là, "
                "même en excès d'oxydant. Un alcool tertiaire, lui, ne "
                "subit aucune oxydation ménagée, quel que soit l'oxydant "
                "utilisé."
            )
        ) as tracker:
            self.play(FadeIn(resultats))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(resultats))

        # --- À retenir / piège : justification du blocage tertiaire -------------------
        justification = definition_box(
            Text(
                _wrap(
                    "Pourquoi l'alcool tertiaire résiste-t-il ? Une "
                    "oxydation ménagée retire un atome d'hydrogène porté "
                    "PAR le carbone fonctionnel. Or, le carbone fonctionnel "
                    "d'un alcool tertiaire est déjà relié à trois autres "
                    "carbones : il ne porte plus AUCUN hydrogène à retirer.",
                    width=48,
                ),
                font_size=22,
            ),
        )
        justification.next_to(titre, DOWN, buff=0.4)
        _fit(justification, titre.get_bottom()[1] - 0.4)

        with self.voiceover(
            text=(
                "Pourquoi l'alcool tertiaire résiste-t-il à toute "
                "oxydation ménagée ? Parce qu'une oxydation ménagée "
                "consiste précisément à retirer un atome d'hydrogène porté "
                "par le carbone fonctionnel lui-même. Or, le carbone "
                "fonctionnel d'un alcool tertiaire est déjà relié à trois "
                "autres atomes de carbone : il ne porte plus aucun "
                "hydrogène disponible à retirer. C'est une conséquence "
                "directe de sa structure, pas une règle arbitraire à "
                "mémoriser sans comprendre."
            )
        ) as tracker:
            self.play(FadeIn(justification))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(justification), FadeOut(titre))
