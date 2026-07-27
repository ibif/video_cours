"""
scenes/Physique_TravailPuissanceTranslation_06.py — Chapitre 1 « Travail et
puissance dans le cas d'un mouvement de translation » (1ereC, Physique),
scène 06.

§ Unités de travail et de puissance (joule, watt, cheval-vapeur), le
kilowattheure comme unité de TRAVAIL (et non de puissance) :
1 kWh = 3,6×10⁶ J. Piège : ne pas confondre kWh (énergie) et kW
(puissance).
Source : 1ereC/Physique.pdf, chapitre 1, pages 4-12.
"""

import textwrap

from manim import DOWN, LEFT, RIGHT, UP, YELLOW, FadeIn, FadeOut, MathTex, Text, VGroup, Write

from shapes.base_scene import NotionScene
from shapes.boxes import (
    corrige_box,
    definition_box,
    essentiel_box,
    exercise_box,
    property_box,
    scene_title,
    warning_box,
)


def _wrap(text: str, width: int = 56) -> str:
    return "\n".join(textwrap.fill(line, width=width) for line in text.split("\n"))


class UnitesKilowattheure(NotionScene):
    def construct(self):
        titre = scene_title("Unités : joule, watt, kilowattheure")
        titre.scale(0.55)
        titre.to_edge(UP)

        # --- Énoncé : mise en situation ------------------------------------------
        mise_en_situation = Text(
            _wrap(
                "Sur une facture d'électricité en Côte d'Ivoire, la "
                "consommation est affichée en kWh, jamais en joules : que "
                "représente exactement cette unité ?",
                width=54,
            ),
            font_size=23,
        )
        mise_en_situation.next_to(titre, DOWN, buff=0.35)

        with self.voiceover(
            text=(
                "Sur une facture d'électricité en Côte d'Ivoire, la "
                "consommation est toujours affichée en kilowattheures, "
                "jamais en joules. Que représente exactement cette unité, "
                "et en quoi diffère-t-elle du kilowatt ?"
            )
        ) as tracker:
            self.play(Write(titre))
            self.play(FadeIn(mise_en_situation))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(mise_en_situation))

        # --- Raisonnement : tableau des unités ------------------------------------------
        row1 = VGroup(
            Text("Travail / énergie", font_size=22, weight="BOLD"),
            MathTex(r"\text{joule (J)}", font_size=24),
        ).arrange(RIGHT, buff=0.6)
        row2 = VGroup(
            Text("Puissance", font_size=22, weight="BOLD"),
            MathTex(r"\text{watt (W)} = J/s", font_size=24),
        ).arrange(RIGHT, buff=0.6)
        row3 = VGroup(
            Text("Puissance (mécanique, ancienne)", font_size=22, weight="BOLD"),
            MathTex(r"\text{cheval-vapeur (ch)} \approx 736\ W", font_size=22),
        ).arrange(RIGHT, buff=0.6)
        tableau = VGroup(row1, row2, row3).arrange(DOWN, buff=0.3, aligned_edge=LEFT)
        tableau_box = property_box(tableau, box_width=11.8)
        tableau_box.next_to(titre, DOWN, buff=0.35)

        with self.voiceover(
            text=(
                "Récapitulons les unités du chapitre. Le travail et "
                "l'énergie s'expriment en joules. La puissance s'exprime en "
                "watts, soit des joules par seconde. Dans le domaine "
                "mécanique, on rencontre aussi une unité plus ancienne de "
                "puissance, le cheval-vapeur, qui vaut environ sept cent "
                "trente-six watts."
            )
        ) as tracker:
            self.play(FadeIn(tableau_box))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(tableau_box))

        kwh = definition_box(
            VGroup(
                Text("Le kilowattheure (kWh) : une unité de TRAVAIL", font_size=22, weight="BOLD"),
                MathTex(
                    r"1\ kWh = 1\ kW \times 1\ h = 1000 \times 3600 = 3{,}6\times10^{6}\ J",
                    font_size=25,
                ),
            ).arrange(DOWN, buff=0.25),
            box_width=11.0,
        )
        kwh.next_to(titre, DOWN, buff=0.35)

        with self.voiceover(
            text=(
                "Le kilowattheure, malgré son nom qui contient le mot "
                "kilowatt, est en réalité une unité de travail, "
                "c'est-à-dire d'énergie, et non de puissance. Il "
                "correspond au travail fourni par une puissance constante "
                "d'un kilowatt pendant une heure, soit mille watts fois "
                "trois mille six cents secondes, ce qui donne trois virgule "
                "six millions de joules."
            )
        ) as tracker:
            self.play(FadeIn(kwh))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(kwh))

        # --- Exemple traité ---------------------------------------------------------------
        enonce = exercise_box(
            Text(
                _wrap(
                    "Un appareil électrique de puissance constante 2 kW "
                    "fonctionne pendant 3 heures. Calculer l'énergie "
                    "consommée en kWh, puis en joules.",
                    width=52,
                ),
                font_size=22,
            ),
            box_width=11.0,
        )
        enonce.next_to(titre, DOWN, buff=0.35)

        with self.voiceover(
            text=(
                "Exemple : un appareil électrique de puissance constante "
                "deux kilowatts fonctionne pendant trois heures. Calculons "
                "l'énergie consommée en kilowattheures, puis en joules."
            )
        ) as tracker:
            self.play(FadeIn(enonce))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(enonce))

        calc = corrige_box(
            VGroup(
                MathTex(r"W = P \times \Delta t = 2 \times 3 = 6\ kWh", font_size=26),
                MathTex(r"W = 6 \times 3{,}6\times10^{6} = 21{,}6\times10^{6}\ J", font_size=26, color=YELLOW),
            ).arrange(DOWN, buff=0.3),
            box_width=10.5,
        )
        calc.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "L'énergie consommée vaut la puissance fois la durée, soit "
                "deux kilowatts fois trois heures, c'est-à-dire six "
                "kilowattheures. En convertissant en joules, on multiplie "
                "par trois virgule six millions, ce qui donne "
                "vingt-et-un virgule six millions de joules."
            )
        ) as tracker:
            self.play(FadeIn(calc))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(calc))

        # --- À retenir ---------------------------------------------------------------
        retenir = essentiel_box(
            Text(
                _wrap(
                    "Joule (J) : travail/énergie. Watt (W) : puissance. "
                    "Kilowattheure (kWh) : TRAVAIL, égal à 3,6×10⁶ J — pas "
                    "une puissance malgré son nom.",
                    width=54,
                ),
                font_size=22,
            ),
            box_width=11.0,
        )
        retenir.next_to(titre, DOWN, buff=0.35)

        with self.voiceover(
            text=(
                "À retenir : le joule mesure un travail ou une énergie, le "
                "watt mesure une puissance, et le kilowattheure, malgré son "
                "nom, mesure un travail, égal à trois virgule six millions "
                "de joules, et non une puissance."
            )
        ) as tracker:
            self.play(FadeIn(retenir))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(retenir))

        # --- Pièges à éviter --------------------------------------------------------------
        piege = warning_box(
            Text(
                _wrap(
                    "Ne jamais confondre kWh (énergie consommée, ce que "
                    "facture la CIE) et kW (puissance instantanée d'un "
                    "appareil, inscrite sur sa plaque signalétique) : ce ne "
                    "sont pas la même grandeur physique.",
                    width=54,
                ),
                font_size=21,
            ),
            box_width=11.2,
        )
        piege.next_to(titre, DOWN, buff=0.35)

        with self.voiceover(
            text=(
                "Piège très fréquent : ne jamais confondre le "
                "kilowattheure, qui mesure l'énergie consommée et sert de "
                "base à la facturation, avec le kilowatt, qui mesure la "
                "puissance instantanée d'un appareil, indiquée sur sa "
                "plaque signalétique. Ce ne sont pas du tout la même "
                "grandeur physique."
            )
        ) as tracker:
            self.play(FadeIn(piege))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(piege), FadeOut(titre))
