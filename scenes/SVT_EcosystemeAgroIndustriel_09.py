"""
scenes/SVT_EcosystemeAgroIndustriel_09.py — Chapitre 11 (1ereC, SVT), scène 09.

§ 4.3 Le rendement écologique : définition et formule
r = (En/En-1) x 100, puis Exemple résolu 1 : calcul complet sur 2 étapes
avec les valeurs de la savane (producteurs 6.10^7, C1 6.10^6, C2 4,8.10^5
kJ/ha/an), calcul des 2 rendements et interprétation.
Source : 1ereC/SVT.pdf, page 125.
"""

import textwrap

from manim import DOWN, LEFT, UP, WHITE, YELLOW, FadeIn, FadeOut, MathTex, Text, VGroup, Write

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


class RendementEcologique(NotionScene):
    def construct(self):
        titre = scene_title("4.3 — Le rendement écologique")
        titre.scale(0.68)
        titre.to_edge(UP)

        # --- Énoncé : définition + formule -----------------------------------
        definition = definition_box(
            VGroup(
                Text(
                    _wrap(
                        "Le rendement écologique (ou efficacité de "
                        "transfert) entre deux niveaux trophiques "
                        "consécutifs est le rapport de l'énergie (ou de la "
                        "biomasse) produite au niveau n à celle produite "
                        "au niveau précédent n-1, exprimé en pourcent.",
                        width=52,
                    ),
                    font_size=20,
                ),
                MathTex(r"r = \dfrac{E_n}{E_{n-1}} \times 100", font_size=32, color=YELLOW),
                Text("Généralement compris entre 5 et 20 %.", font_size=18, color="#555555"),
            ).arrange(DOWN, buff=0.3),
            box_width=11.5,
        )
        definition.next_to(titre, DOWN, buff=0.45)

        with self.voiceover(
            text=(
                "Le rendement écologique, ou efficacité de transfert, "
                "entre deux niveaux trophiques consécutifs, est le "
                "rapport de l'énergie, ou de la biomasse, produite au "
                "niveau n à celle produite au niveau précédent n moins un, "
                "exprimé en pourcent : r égale En sur En moins un, fois "
                "cent. Il est généralement compris entre cinq et vingt "
                "pour cent."
            )
        ) as tracker:
            self.play(Write(titre))
            self.play(FadeIn(definition))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(definition))

        # --- Raisonnement : les données de l'exemple -------------------------
        donnees_titre = Text("Données mesurées dans une savane (par hectare, par an)", font_size=20, color=YELLOW, weight="BOLD")
        donnees_titre.next_to(titre, DOWN, buff=0.4)
        donnees = _bullets(
            [
                "Producteurs (herbes) : 6 × 10⁷ kJ/ha/an",
                "Consommateurs primaires : 6 × 10⁶ kJ/ha/an",
                "Consommateurs secondaires : 4,8 × 10⁵ kJ/ha/an",
            ],
            font_size=22,
            width=48,
        )
        donnees.next_to(donnees_titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Prenons un exemple résolu. Dans une savane, on a mesuré, "
                "sur un an et par hectare : six fois dix puissance sept "
                "kilojoules par hectare et par an pour les producteurs, "
                "les herbes ; six fois dix puissance six pour les "
                "consommateurs primaires ; et quatre virgule huit fois dix "
                "puissance cinq pour les consommateurs secondaires."
            )
        ) as tracker:
            self.play(FadeIn(donnees_titre))
            self.play(FadeIn(donnees))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(donnees_titre), FadeOut(donnees))

        # --- Exemple traité : calcul complet des 2 rendements -----------------
        etape1_titre = Text("Étape 1 — Rendement entre P et C1", font_size=20, color=YELLOW, weight="BOLD")
        etape1 = MathTex(
            r"r_1 = \dfrac{E_{C1}}{E_P} \times 100 = \dfrac{6\times10^6}{6\times10^7} \times 100 = 10\ \%",
            font_size=26,
            color=WHITE,
        )
        bloc1 = VGroup(etape1_titre, etape1).arrange(DOWN, buff=0.3)

        etape2_titre = Text("Étape 2 — Rendement entre C1 et C2", font_size=20, color=YELLOW, weight="BOLD")
        etape2 = MathTex(
            r"r_2 = \dfrac{E_{C2}}{E_{C1}} \times 100 = \dfrac{4{,}8\times10^5}{6\times10^6} \times 100 = 8\ \%",
            font_size=26,
            color=WHITE,
        )
        bloc2 = VGroup(etape2_titre, etape2).arrange(DOWN, buff=0.3)

        calculs = VGroup(bloc1, bloc2).arrange(DOWN, buff=0.5)

        exemple = example_box(calculs, box_width=12.0)
        exemple.next_to(titre, DOWN, buff=0.45)

        with self.voiceover(
            text=(
                "Étape un : le rendement entre les producteurs et les "
                "consommateurs primaires. r un égale E C1 sur E P, fois "
                "cent, soit six fois dix puissance six sur six fois dix "
                "puissance sept, fois cent, égale dix pour cent. Étape "
                "deux : le rendement entre les consommateurs primaires et "
                "secondaires. r deux égale E C2 sur E C1, fois cent, soit "
                "quatre virgule huit fois dix puissance cinq sur six fois "
                "dix puissance six, fois cent, égale huit pour cent."
            )
        ) as tracker:
            self.play(FadeIn(exemple))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(exemple))

        # --- À retenir : interprétation -----------------------------------------
        interpretation = Text(
            _wrap(
                "Interprétation : sur 100 kJ produites par les herbes, "
                "seules 10 kJ parviennent aux herbivores, et seulement "
                "0,8 kJ aux carnivores. L'énergie diminue très vite le "
                "long de la chaîne.",
                width=54,
            ),
            font_size=22,
            color=WHITE,
        )
        interpretation.next_to(titre, DOWN, buff=0.6)

        with self.voiceover(
            text=(
                "Interprétation : sur cent kilojoules produites par les "
                "herbes, seules dix kilojoules parviennent aux "
                "herbivores, et seulement zéro virgule huit kilojoule aux "
                "carnivores. L'énergie diminue donc très vite le long de "
                "la chaîne alimentaire, ce qui confirme la loi de "
                "Lindeman vue précédemment."
            )
        ) as tracker:
            self.play(FadeIn(interpretation))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(titre), FadeOut(interpretation))
