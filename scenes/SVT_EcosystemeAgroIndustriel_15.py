"""
scenes/SVT_EcosystemeAgroIndustriel_15.py — Chapitre 11 (1ereC, SVT), scène 15.

§ 7.3 / 8 Tableau comparatif écosystème naturel / agrosystème (origine,
biodiversité, réseau trophique, recyclage, source d'énergie, stabilité,
productivité, devenir sans l'homme), puis vers une agriculture durable en
Côte d'Ivoire (définition, rotation culturale, agroforesterie, engrais
verts, autres pratiques, exemple du cacao d'ombrage à Daloa/Soubré/San
Pedro). Source : 1ereC/SVT.pdf, pages 131-132.
"""

import textwrap

from manim import DOWN, LEFT, UP, WHITE, YELLOW, FadeIn, FadeOut, Text, VGroup, Write, config

from shapes.base_scene import NotionScene
from shapes.boxes import definition_box, example_box, scene_title


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


class ComparatifEtAgricultureDurable(NotionScene):
    def construct(self):
        titre = scene_title("7.3-8 — Écosystème naturel vs agrosystème")
        titre.scale(0.6)
        titre.to_edge(UP)

        # --- Énoncé : tableau comparatif -----------------------------------------
        tab_titre = Text("Tableau comparatif", font_size=24, color=YELLOW, weight="BOLD")
        tab_titre.next_to(titre, DOWN, buff=0.35)
        tableau = _bullets(
            [
                "Origine : naturel  —  vs  créé et entretenu par l'homme",
                "Biodiversité : élevée  —  vs  faible (monoculture)",
                "Réseau trophique : complexe  —  vs  simplifié",
                "Recyclage de la matière : presque complet  —  vs  incomplet (exportation)",
                "Source d'énergie : Soleil uniquement  —  vs  Soleil + énergie fossile",
                "Stabilité : équilibre dynamique, autorégulation  —  vs  instable, interventions permanentes",
                "Productivité primaire : moyenne  —  vs  élevée (avec intrants)",
                "Devenir sans l'homme : persiste et évolue  —  vs  retourne à la friche",
            ],
            font_size=15,
            width=68,
        )
        tableau.next_to(tab_titre, DOWN, buff=0.25)
        groupe_tab = VGroup(tab_titre, tableau)
        _fit(groupe_tab, titre.get_bottom()[1] - 0.15)

        with self.voiceover(
            text=(
                "Résumons dans un tableau comparatif entre l'écosystème "
                "naturel, comme une forêt ou une savane, et l'agrosystème, "
                "comme une cacaoyère ou une palmeraie. L'origine : "
                "naturelle, contre créée et entretenue par l'homme. La "
                "biodiversité : élevée, contre faible, en monoculture. Le "
                "réseau trophique : complexe, contre simplifié. Le "
                "recyclage de la matière : presque complet, contre "
                "incomplet, à cause de l'exportation de la biomasse. La "
                "source d'énergie : le Soleil seul, contre le Soleil plus "
                "l'énergie fossile des intrants. La stabilité : équilibre "
                "dynamique et autorégulation, contre instabilité "
                "nécessitant des interventions permanentes. La "
                "productivité primaire : moyenne, contre élevée grâce aux "
                "intrants. Et le devenir sans l'homme : l'écosystème "
                "naturel persiste et évolue, tandis que l'agrosystème "
                "retourne à la friche."
            )
        ) as tracker:
            self.play(Write(titre))
            self.play(FadeIn(tab_titre))
            self.play(FadeIn(tableau))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(tab_titre), FadeOut(tableau))

        # --- Raisonnement : agriculture durable, définition -----------------------
        definition = definition_box(
            Text(
                _wrap(
                    "L'agriculture durable est un mode de production qui "
                    "cherche à maintenir la productivité et les revenus "
                    "des agriculteurs tout en préservant les ressources "
                    "naturelles (sol, eau, biodiversité) et la santé des "
                    "populations pour les générations futures.",
                    width=54,
                ),
                font_size=20,
            ),
            box_width=11.8,
        )
        definition.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Face à ce constat, comment concilier production agricole "
                "et préservation des écosystèmes ? C'est tout l'enjeu de "
                "l'agriculture durable, un mode de production qui cherche "
                "à maintenir la productivité et les revenus des "
                "agriculteurs tout en préservant les ressources "
                "naturelles, sol, eau, biodiversité, et la santé des "
                "populations pour les générations futures."
            )
        ) as tracker:
            self.play(FadeIn(definition))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(definition))

        # --- Exemple traité : les techniques de base -----------------------------
        tech_titre = Text("Les techniques de base", font_size=23, color=YELLOW, weight="BOLD")
        tech_titre.next_to(titre, DOWN, buff=0.4)
        techniques = _bullets(
            [
                "Rotation culturale : maïs (gourmand en azote) → niébé/arachide (légumineuses fixatrices) → manioc.",
                "Agroforesterie : cacaoyers/caféiers sous l'ombrage d'arbres forestiers ou fruitiers.",
                "Engrais verts : mucuna, crotalaire, pois d'Angole, enfouis pour fertiliser sans polluer.",
                "Autres pratiques : jachère améliorée, compostage, lutte biologique, semis direct, haies anti-érosion.",
            ],
            font_size=18,
            width=60,
        )
        techniques.next_to(tech_titre, DOWN, buff=0.3)
        groupe_tech = VGroup(tech_titre, techniques)
        _fit(groupe_tech, titre.get_bottom()[1] - 0.2)

        with self.voiceover(
            text=(
                "Voici les techniques de base, applicables aux "
                "exploitations ivoiriennes. La rotation culturale : on "
                "fait se succéder sur une même parcelle des cultures aux "
                "besoins différents, par exemple le maïs, gourmand en "
                "azote, puis le niébé ou l'arachide, des légumineuses "
                "fixatrices d'azote, puis le manioc. L'agroforesterie : on "
                "associe des arbres aux cultures, cacaoyers sous "
                "l'ombrage d'arbres forestiers, caféiers sous fruitiers. "
                "Les engrais verts : on cultive une légumineuse, mucuna, "
                "crotalaire, pois d'Angole, non pour la récolter mais pour "
                "l'enfouir dans le sol, ce qui le fertilise naturellement, "
                "gratuitement et sans pollution. Et d'autres pratiques : "
                "la jachère améliorée, le compostage, la lutte biologique, "
                "le semis direct, les haies anti-érosion."
            )
        ) as tracker:
            self.play(FadeIn(tech_titre))
            self.play(FadeIn(techniques))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(tech_titre), FadeOut(techniques))

        # --- À retenir : exemple ivoirien du cacao d'ombrage -----------------------
        exemple = example_box(
            Text(
                _wrap(
                    "Face au vieillissement des cacaoyères et à "
                    "l'appauvrissement des sols de l'ancienne boucle du "
                    "cacao, de nombreux programmes replantent des "
                    "cacaoyers sous couvert forestier (agroforesterie) "
                    "dans les régions de Daloa, Soubré et San Pedro : le "
                    "cacao d'ombrage vit plus longtemps, exige moins "
                    "d'engrais et préserve une partie de la biodiversité.",
                    width=54,
                ),
                font_size=19,
            ),
            box_width=11.8,
        )
        exemple.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Exemple ivoirien concret : face au vieillissement des "
                "cacaoyères et à l'appauvrissement des sols de l'ancienne "
                "boucle du cacao, de nombreux programmes replantent des "
                "cacaoyers sous couvert forestier, c'est l'agroforesterie, "
                "dans les régions de Daloa, de Soubré et de San Pedro. Le "
                "cacao d'ombrage vit plus longtemps, exige moins d'engrais "
                "et préserve une partie de la biodiversité."
            )
        ) as tracker:
            self.play(FadeIn(exemple))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(titre), FadeOut(exemple))
