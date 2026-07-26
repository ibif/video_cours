"""
scenes/SVT_AbsorptionNutriments_09.py — Chapitre 13 (1ereD, SVT), scène 09
(dernière scène du chapitre, et dernière scène du programme SVT 1ereD).

§ 13.4.3 L'absorption de l'eau et des sels minéraux (bilan ~9-10 L/jour,
osmose), application directe : le soluté de réhydratation orale (SRO) et le
co-transport glucose-sodium, contexte du choléra en Côte d'Ivoire, puis
L'ESSENTIEL DU CHAPITRE.
Source : 1ereD/SVT.pdf, pages 177-178.
"""

import textwrap

from manim import DOWN, LEFT, RIGHT, UP, WHITE, YELLOW, BLUE, GREEN, FadeIn, FadeOut, MathTex, Text, VGroup, Write

from shapes.base_scene import NotionScene
from shapes.boxes import essentiel_box, example_box, scene_title, warning_box


def _wrap(text: str, width: int = 56) -> str:
    return "\n".join(textwrap.fill(line, width=width) for line in text.split("\n"))


def _bullets(items, font_size=23, color=WHITE, width=52):
    lines = VGroup(
        *[Text(f"• {_wrap(it, width=width)}", font_size=font_size, color=color) for it in items]
    )
    lines.arrange(DOWN, aligned_edge=LEFT, buff=0.24)
    return lines


class AbsorptionEauEtApplicationSRO(NotionScene):
    def construct(self):
        titre = scene_title("13.4.3 — L'eau, les sels minéraux et le SRO")
        titre.scale(0.58)
        titre.to_edge(UP)

        # --- Énoncé : un bilan hydrique considérable ---------------------------
        intro = Text(
            _wrap(
                "Chaque jour, l'organisme d'un adulte verse dans son tube "
                "digestif environ 9 à 10 litres d'eau : boissons, eau des "
                "aliments, mais aussi salive, suc gastrique, bile, suc "
                "pancréatique et suc intestinal. Que devient tout ce "
                "volume ?",
                width=56,
            ),
            font_size=23,
            color=WHITE,
        )
        intro.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Chaque jour, l'organisme d'un adulte verse dans son tube "
                "digestif environ neuf à dix litres d'eau : les boissons "
                "et l'eau des aliments, mais aussi la salive, le suc "
                "gastrique, la bile, le suc pancréatique et le suc "
                "intestinal. Que devient tout ce volume ?"
            )
        ) as tracker:
            self.play(Write(titre))
            self.play(FadeIn(intro))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(intro))

        # --- Animation du raisonnement : bilan chiffré --------------------------
        bilan = MathTex(
            r"9\text{-}10\ \text{L/jour} \;\longrightarrow\; \text{intestin grêle} + \text{côlon} \;\longrightarrow\; 0{,}1\text{-}0{,}15\ \text{L (fèces)}",
            font_size=26,
            color=WHITE,
        )
        bilan.next_to(titre, DOWN, buff=0.7)

        explication = Text(
            _wrap(
                "L'eau passe par osmose, entraînée par l'absorption des "
                "sels et des nutriments. La presque totalité du volume est "
                "réabsorbée, l'essentiel dans l'intestin grêle, le reste "
                "dans le côlon.",
                width=52,
            ),
            font_size=20,
            color=WHITE,
        )
        explication.next_to(bilan, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "La presque totalité de ce volume est réabsorbée, "
                "l'essentiel dans l'intestin grêle, le reste dans le "
                "côlon : les fèces n'en éliminent qu'environ zéro virgule "
                "un à zéro virgule quinze litre. L'eau passe par osmose, "
                "entraînée par l'absorption des sels et des nutriments. "
                "Les sels minéraux sont absorbés par transport actif ou "
                "par diffusion, puis conduits par le sang jusqu'au foie."
            )
        ) as tracker:
            self.play(Write(bilan))
            self.play(FadeIn(explication))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(bilan), FadeOut(explication))

        # --- Exemple traité : application directe, le SRO -----------------------
        entete_sro = Text("Application : le soluté de réhydratation orale (SRO)", font_size=19, color=YELLOW, weight="BOLD")
        entete_sro.next_to(titre, DOWN, buff=0.5)

        exemple = example_box(
            Text(
                _wrap(
                    "Lors du choléra ou des diarrhées aiguës, fréquentes là "
                    "où l'eau potable manque, l'intestin perd brutalement "
                    "d'énormes quantités d'eau et de sels : c'est la "
                    "déshydratation, qui peut tuer un enfant en quelques "
                    "heures. Le SRO — eau propre + sel + sucre — exploite "
                    "le co-transport actif glucose-sodium de l'entérocyte "
                    ": cette absorption entraîne l'eau par osmose, même "
                    "quand l'intestin est malade. Il réhydrate donc "
                    "beaucoup mieux que l'eau pure.",
                    width=54,
                ),
                font_size=20,
            ),
            box_width=12.2,
        )
        exemple.next_to(entete_sro, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Voici une application qui sauve des vies. Lors du "
                "choléra ou des diarrhées aiguës, fréquentes là où l'eau "
                "potable manque, l'intestin perd brutalement d'énormes "
                "quantités d'eau et de sels : c'est la déshydratation, qui "
                "peut tuer un enfant en quelques heures. Le soluté de "
                "réhydratation orale, le SRO, distribué dans les centres "
                "de santé de Côte d'Ivoire, est un simple mélange d'eau "
                "propre, de sel et de sucre. Son efficacité repose "
                "directement sur ce chapitre : le glucose et le sodium "
                "sont absorbés ensemble par le transporteur actif de "
                "l'entérocyte, et cette absorption entraîne l'eau par "
                "osmose, même quand l'intestin est malade. Le SRO "
                "réhydrate donc beaucoup mieux que l'eau pure."
            )
        ) as tracker:
            self.play(FadeIn(entete_sro))
            self.play(FadeIn(exemple))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(entete_sro), FadeOut(exemple))

        # --- Piège à éviter : le SRO ne guérit pas l'infection --------------------
        piege = warning_box(
            Text(
                _wrap(
                    "Le SRO ne guérit pas l'infection responsable de la "
                    "diarrhée : il maintient seulement le malade en vie, "
                    "en réhydratant son organisme, pendant que "
                    "l'organisme se défend (et qu'un traitement médical "
                    "approprié est recherché).",
                    width=54,
                ),
                font_size=21,
            ),
            box_width=12.0,
        )
        piege.next_to(titre, DOWN, buff=0.55)

        with self.voiceover(
            text=(
                "Attention à ne pas surestimer le SRO : il ne guérit pas "
                "l'infection responsable de la diarrhée. Il maintient "
                "seulement le malade en vie, en réhydratant son "
                "organisme, pendant que celui-ci se défend."
            )
        ) as tracker:
            self.play(FadeIn(piege))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(piege))

        # --- À retenir : L'ESSENTIEL DU CHAPITRE -----------------------------------
        essentiel = essentiel_box(
            _bullets(
                [
                    "L'absorption fait passer nutriments, eau, sels et vitamines vers le sang ou la lymphe, presque exclusivement dans l'intestin grêle.",
                    "Surface d'absorption ≈ 200-300 m² : plis (×3), villosités (×10), microvillosités (×20).",
                    "Villosité : épithélium à 1 couche d'entérocytes, capillaires sanguins, vaisseau chylifère central.",
                    "Diffusion (passive) descend le gradient ; osmose fait passer l'eau ; transport actif (glucose, a. aminés, sels) va contre le gradient grâce à l'ATP.",
                    "Sang (via veine porte → foie) : glucose, a. aminés, eau, sels, vitamines hydrosolubles.",
                    "Lymphe (via vaisseau chylifère → canal thoracique) : acides gras, glycérol, vitamines liposolubles.",
                    "≈9-10 L d'eau/jour traversent le tube digestif ; presque tout est réabsorbé (fèces : 0,1-0,15 L).",
                    "Le SRO exploite le co-transport glucose-sodium pour réhydrater les malades.",
                ],
                font_size=16,
                width=60,
            ),
            box_width=12.6,
        )
        essentiel.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Voici l'essentiel de ce chapitre, et de tout notre "
                "programme de SVT sur la digestion et l'absorption. "
                "L'absorption fait passer les nutriments, l'eau, les sels "
                "et les vitamines de la lumière intestinale vers le sang "
                "ou la lymphe, presque exclusivement dans l'intestin "
                "grêle. Grâce aux plis, aux villosités et aux "
                "microvillosités, sa surface d'absorption atteint deux à "
                "trois cents mètres carrés. Chaque villosité contient un "
                "épithélium à une seule couche d'entérocytes, un réseau de "
                "capillaires sanguins et un vaisseau chylifère central. La "
                "diffusion, passive, descend le gradient de concentration "
                "; l'osmose fait passer l'eau ; le transport actif, pour "
                "le glucose, les acides aminés et de nombreux sels, "
                "fonctionne contre le gradient grâce à l'ATP, et il est "
                "bloqué par le cyanure ou par le froid. Glucose, acides "
                "aminés, eau, sels minéraux et vitamines hydrosolubles "
                "gagnent la veine porte hépatique puis le foie ; les "
                "acides gras, le glycérol et les vitamines liposolubles "
                "gagnent le vaisseau chylifère, la lymphe, puis le sang "
                "par la veine sous-clavière gauche. Environ neuf à dix "
                "litres d'eau traversent chaque jour le tube digestif, et "
                "la quasi-totalité est réabsorbée. Enfin, le soluté de "
                "réhydratation orale exploite le co-transport "
                "glucose-sodium pour réhydrater les malades atteints de "
                "diarrhées sévères, une application qui, en Côte d'Ivoire "
                "comme ailleurs, sauve chaque année de nombreuses vies."
            )
        ) as tracker:
            self.play(FadeIn(essentiel))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(titre), FadeOut(essentiel))
