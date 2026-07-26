"""
scenes/SVT_EvolutionSolsTropicaux_07.py — Chapitre 9 (1ereD, SVT), scène 07.

§ 9.5.3 Les autres processus tropicaux (podsolisation, hydromorphie) +
exemple du bilan d'un lessivage sur 20 ans, méthode pour analyser un
document sur l'évolution d'un sol, attention un sol rouge n'est pas un
sol riche. Source : 1ereD/SVT.pdf, page 123.
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
from shapes.boxes import definition_box, example_box, method_box, scene_title, warning_box


def _wrap(text: str, width: int = 56) -> str:
    return "\n".join(textwrap.fill(line, width=width) for line in text.split("\n"))


def _bullets(items, font_size=23, color=WHITE, width=52):
    lines = VGroup(
        *[Text(f"• {_wrap(it, width=width)}", font_size=font_size, color=color) for it in items]
    )
    lines.arrange(DOWN, aligned_edge=LEFT, buff=0.22)
    return lines


class PodsolisationEtHydromorphie(NotionScene):
    def construct(self):
        titre = scene_title("9.5.3 — Podsolisation et hydromorphie")
        titre.scale(0.68)
        titre.to_edge(UP)

        # --- Énoncé : définitions ------------------------------------------
        definition = definition_box(
            Text(
                _wrap(
                    "La podsolisation : climat très humide, roches très "
                    "siliceuses, litière acide — les acides organiques "
                    "entraînent fer et aluminium vers le bas, horizon "
                    "supérieur blanchâtre cendreux, très pauvre. Limitée en "
                    "Côte d'Ivoire (extrême Sud très arrosé). "
                    "L'hydromorphie : sols des bas-fonds/zones inondables, "
                    "l'eau stagnante chasse l'air, le fer est réduit (Fe3+ "
                    "→ Fe2+), couleurs grises/verdâtres/bleuâtres, taches "
                    "de rouille. Conviennent à la riziculture.",
                    width=54,
                ),
                font_size=19,
            ),
            box_width=12.2,
        )
        definition.next_to(titre, DOWN, buff=0.4)

        _bas_visible = -config.frame_height / 2 + 0.3
        _hauteur_dispo = definition.get_top()[1] - _bas_visible
        if definition.height > _hauteur_dispo:
            definition.scale(_hauteur_dispo / definition.height, about_point=definition.get_top())

        with self.voiceover(
            text=(
                "Deux autres processus tropicaux méritent d'être connus. "
                "La podsolisation apparaît sous climat très humide, sur des "
                "roches très siliceuses, avec une litière acide : les "
                "acides organiques entraînent le fer et l'aluminium vers le "
                "bas, laissant un horizon supérieur blanchâtre, cendreux, "
                "très pauvre. Elle reste limitée en Côte d'Ivoire, à "
                "l'extrême Sud très arrosé. L'hydromorphie, elle, concerne "
                "les sols des bas-fonds et des zones inondables : l'eau "
                "stagnante chasse l'air, le fer est réduit, passant de Fe "
                "trois plus à Fe deux plus, ce qui donne des couleurs "
                "grises, verdâtres ou bleuâtres, avec des taches de "
                "rouille. Ces sols conviennent bien à la riziculture."
            )
        ) as tracker:
            self.play(Write(titre))
            self.play(FadeIn(definition))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(definition))

        # --- Animation du raisonnement : exemple bilan du lessivage ----------
        exemple = example_box(
            Text(
                _wrap(
                    "Mesures sur une parcelle forestière d'un hectare près "
                    "de Soubré, pertes annuelles par lessivage : calcium "
                    "120 kg, magnésium 45 kg, potassium 30 kg, sodium 25 "
                    "kg. Quel bilan sur 20 ans ?",
                    width=54,
                ),
                font_size=21,
            ),
            box_width=12.0,
        )
        exemple.next_to(titre, DOWN, buff=0.45)

        with self.voiceover(
            text=(
                "Exemple traité : le bilan d'un lessivage. Sur une "
                "parcelle forestière d'un hectare, près de Soubré, on "
                "mesure les pertes annuelles par lessivage : cent vingt "
                "kilogrammes de calcium, quarante-cinq kilogrammes de "
                "magnésium, trente kilogrammes de potassium, "
                "vingt-cinq kilogrammes de sodium. Quel est le bilan sur "
                "vingt ans ?"
            )
        ) as tracker:
            self.play(FadeIn(exemple))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(exemple))

        etape1 = MathTex(
            r"120+45+30+25 = 220 \text{ kg/ha/an}",
            font_size=28,
            color=WHITE,
        )
        etape2 = MathTex(
            r"220 \times 20 = 4400 \text{ kg} = 4{,}4 \text{ t/ha en 20 ans}",
            font_size=28,
            color=YELLOW,
        )
        calculs = VGroup(etape1, etape2).arrange(DOWN, buff=0.4)
        calculs.next_to(titre, DOWN, buff=0.7)

        with self.voiceover(
            text=(
                "Étape un : la perte annuelle totale est de cent vingt "
                "plus quarante-cinq plus trente plus vingt-cinq, soit deux "
                "cent vingt kilogrammes par hectare et par an. Étape deux : "
                "sur vingt ans, cela fait deux cent vingt fois vingt, soit "
                "quatre mille quatre cents kilogrammes, c'est-à-dire "
                "quatre virgule quatre tonnes par hectare."
            )
        ) as tracker:
            self.play(Write(etape1))
            self.play(Write(etape2))
            self.wait(tracker.get_remaining_duration())

        conclusion = Text(
            _wrap(
                "Même sans culture, le climat exporte naturellement "
                "plusieurs tonnes de nutriments par hectare en 20 ans. "
                "Sous forêt, la litière compense ; dès qu'on cultive sans "
                "restituer, l'appauvrissement devient brutal.",
                width=54,
            ),
            font_size=22,
            color=WHITE,
        )
        conclusion.next_to(calculs, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Conclusion : même sans aucune culture, le climat exporte "
                "naturellement plusieurs tonnes de nutriments par hectare "
                "en vingt ans. Sous la forêt, la chute continue de litière "
                "compense cette perte ; mais dès qu'on cultive sans rien "
                "restituer au sol, l'appauvrissement devient brutal."
            )
        ) as tracker:
            self.play(FadeIn(conclusion))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(calculs), FadeOut(conclusion))

        # --- À retenir : méthode pour analyser un document -------------------
        methode = method_box(
            _bullets(
                [
                    "Identifier les données (profil, couleurs, analyses chimiques, contexte).",
                    "Repérer les indices : rouge=fer, gris=hydromorphie, horizon clair=lessivage, cuirasse=cuirassement.",
                    "Relier chaque indice à un processus et un facteur.",
                    "Conclure par le type de sol et son aptitude agricole.",
                ],
                font_size=19,
                width=50,
            ),
            box_width=12.2,
        )
        methode.next_to(titre, DOWN, buff=0.45)

        with self.voiceover(
            text=(
                "Méthode pour analyser un document sur l'évolution d'un "
                "sol, en quatre étapes. Un, identifier les données : "
                "profil, couleurs, analyses chimiques, contexte. Deux, "
                "repérer les indices : une couleur rouge signale le fer, "
                "une couleur grise l'hydromorphie, un horizon clair le "
                "lessivage, une cuirasse le cuirassement. Trois, relier "
                "chaque indice à un processus et à un facteur. Quatre, "
                "conclure par le type de sol et son aptitude agricole."
            )
        ) as tracker:
            self.play(FadeIn(methode))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(methode))

        # --- Piège à éviter : un sol rouge n'est pas un sol riche ------------
        piege = warning_box(
            Text(
                _wrap(
                    "Un sol rouge n'est pas un sol riche. La couleur rouge "
                    "signale des oxydes de fer, pas de l'humus. Beaucoup "
                    "de sols ferralitiques, magnifiquement rouges, sont "
                    "pauvres en nutriments et acides. La fertilité se juge "
                    "à la matière organique, aux bases et à la structure, "
                    "pas à la couleur.",
                    width=54,
                ),
                font_size=22,
            ),
            box_width=12.0,
        )
        piege.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Attention, piège classique : un sol rouge n'est pas "
                "forcément un sol riche. La couleur rouge signale la "
                "présence d'oxydes de fer, pas celle de l'humus. Beaucoup "
                "de sols ferralitiques, magnifiquement rouges, sont en "
                "réalité pauvres en nutriments et acides. La fertilité "
                "d'un sol se juge à sa teneur en matière organique, à ses "
                "réserves en bases et à sa structure, jamais à sa seule "
                "couleur."
            )
        ) as tracker:
            self.play(FadeIn(piege))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(titre), FadeOut(piege))
