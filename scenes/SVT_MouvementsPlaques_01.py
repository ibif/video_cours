"""
scenes/SVT_MouvementsPlaques_01.py — Chapitre 7 (1ereD, SVT), scène 01.

Introduction du chapitre « Les mouvements des plaques lithosphériques » :
activité d'introduction (le puzzle de Grand-Bassam, le Mésosaure, la
dorsale médio-atlantique), objectifs du chapitre, prérequis à réviser.
Source : 1ereD/SVT.pdf, page 90.
"""

import textwrap

from manim import DOWN, LEFT, UP, WHITE, YELLOW, FadeIn, FadeOut, Text, VGroup, Write

from shapes.base_scene import NotionScene
from shapes.boxes import essentiel_box, scene_title, warning_box


def _wrap(text: str, width: int = 56) -> str:
    return "\n".join(textwrap.fill(line, width=width) for line in text.split("\n"))


def _bullets(items, font_size=24, color=WHITE, width=54):
    lines = VGroup(
        *[Text(f"• {_wrap(it, width=width)}", font_size=font_size, color=color) for it in items]
    )
    lines.arrange(DOWN, aligned_edge=LEFT, buff=0.22)
    return lines


class IntroductionMouvementsPlaques(NotionScene):
    def construct(self):
        # --- Énoncé : mise en situation ----------------------------------
        titre = scene_title("Chapitre 7 — Les mouvements des plaques")
        titre.scale(0.68)
        titre.to_edge(UP)

        sous_titre = Text("Le puzzle de Grand-Bassam", font_size=28, color=YELLOW, weight="BOLD")
        sous_titre.next_to(titre, DOWN, buff=0.5)

        histoire = Text(
            _wrap(
                "Sur la plage de Grand-Bassam, un élève regarde l'Atlantique. "
                "Son professeur projette une carte : la côte africaine semble "
                "« emboîter » celle de l'Amérique du Sud, comme deux pièces "
                "d'un puzzle.",
                width=56,
            ),
            font_size=25,
            color=WHITE,
        )
        histoire.next_to(sous_titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Sur la plage de Grand-Bassam, un élève regarde l'océan "
                "Atlantique. Son professeur projette alors une carte du "
                "monde : la côte africaine semble « emboîter » celle de "
                "l'Amérique du Sud, comme deux pièces d'un même puzzle. "
                "Simple hasard, ou souvenir d'un ancien voisinage ?"
            )
        ) as tracker:
            self.play(Write(titre))
            self.play(FadeIn(sous_titre))
            self.play(FadeIn(histoire))
            self.wait(tracker.get_remaining_duration())

        indices = Text(
            _wrap(
                "On retrouve au Brésil les mêmes fossiles d'un petit reptile "
                "d'eau douce, le Mésosaure, qu'en Afrique de l'Ouest ; or cet "
                "animal ne pouvait pas traverser plusieurs milliers de km "
                "d'eau salée. Au milieu de l'Atlantique, les sondeurs ont "
                "découvert une immense chaîne de montagnes sous-marines, la "
                "dorsale médio-atlantique, d'où s'échappent des laves.",
                width=56,
            ),
            font_size=24,
            color=WHITE,
        )
        indices.next_to(histoire, DOWN, buff=0.35)

        with self.voiceover(
            text=(
                "Autre indice troublant : on retrouve au Brésil les mêmes "
                "fossiles d'un petit reptile d'eau douce, le Mésosaure, qu'en "
                "Afrique de l'Ouest. Or cet animal ne pouvait absolument pas "
                "traverser plusieurs milliers de kilomètres d'eau salée à la "
                "nage. Dernier indice : au milieu de l'Atlantique, les "
                "sondeurs ont découvert une immense chaîne de montagnes "
                "sous-marines, la dorsale médio-atlantique, d'où "
                "s'échappent des laves."
            )
        ) as tracker:
            self.play(FadeIn(indices))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(sous_titre), FadeOut(histoire), FadeOut(indices))

        # --- Animation du raisonnement : les questions guides -------------
        entete_questions = Text(
            "Quatre questions guideront notre étude :", font_size=27, color=YELLOW, weight="BOLD"
        )
        entete_questions.next_to(titre, DOWN, buff=0.6)

        q1 = Text("1. Les continents sont-ils fixes depuis toujours ?", font_size=24, color=WHITE)
        q2 = Text("2. L'Atlantique s'est-il ouvert, et s'élargit-il encore ?", font_size=24, color=WHITE)
        q3 = Text("3. À quelle vitesse les plaques se déplacent-elles ?", font_size=24, color=WHITE)
        q4 = Text("4. Quelle force peut déplacer des continents entiers ?", font_size=24, color=WHITE)
        questions = VGroup(q1, q2, q3, q4).arrange(DOWN, aligned_edge=LEFT, buff=0.32)
        questions.next_to(entete_questions, DOWN, buff=0.5)

        with self.voiceover(
            text="Première question : les continents sont-ils fixes depuis toujours ?"
        ) as tracker:
            self.play(FadeIn(entete_questions))
            self.play(Write(q1))
            self.wait(tracker.get_remaining_duration())

        with self.voiceover(
            text="Deuxième question : l'Atlantique s'est-il ouvert, et s'élargit-il encore aujourd'hui ?"
        ) as tracker:
            self.play(Write(q2))
            self.wait(tracker.get_remaining_duration())

        with self.voiceover(
            text="Troisième question : à quelle vitesse les plaques se déplacent-elles ?"
        ) as tracker:
            self.play(Write(q3))
            self.wait(tracker.get_remaining_duration())

        with self.voiceover(
            text="Quatrième question : quelle force peut bien déplacer des continents entiers ?"
        ) as tracker:
            self.play(Write(q4))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(entete_questions), FadeOut(questions))

        # --- Exemple traité : objectifs du chapitre ------------------------
        entete_objectifs = Text("Objectifs du chapitre", font_size=27, color=YELLOW, weight="BOLD")
        entete_objectifs.next_to(titre, DOWN, buff=0.55)

        objectifs = _bullets(
            [
                "Décrire la structure interne du globe et distinguer croûte, "
                "lithosphère et asthénosphère.",
                "Définir une plaque lithosphérique et citer les principales plaques.",
                "Expliquer les preuves des mouvements (expansion océanique, "
                "paléomagnétisme, âge des fonds).",
                "Décrire et reconnaître les trois types de limites de plaques "
                "et leurs manifestations.",
                "Calculer une vitesse de déplacement de plaque et expliquer le "
                "moteur des mouvements.",
            ],
            font_size=21,
            width=52,
        )
        objectifs.next_to(entete_objectifs, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "À la fin de ce chapitre, l'élève doit être capable de "
                "décrire la structure interne du globe et de distinguer "
                "croûte, lithosphère et asthénosphère ; de définir une "
                "plaque lithosphérique et de citer les principales plaques ; "
                "d'expliquer les preuves des mouvements des plaques : "
                "expansion océanique, paléomagnétisme et âge des fonds "
                "océaniques ; de décrire et reconnaître les trois types de "
                "limites de plaques, divergence, convergence et coulissage, "
                "ainsi que leurs manifestations ; et enfin de calculer une "
                "vitesse de déplacement de plaque et d'expliquer le moteur "
                "de ces mouvements."
            )
        ) as tracker:
            self.play(FadeIn(entete_objectifs))
            self.play(FadeIn(objectifs))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(entete_objectifs), FadeOut(objectifs))

        # --- À retenir : prérequis à réviser -------------------------------
        prerequis = essentiel_box(
            Text(
                _wrap(
                    "Prérequis à réviser : la structure interne de la Terre "
                    "(croûte, manteau, noyau) ; les notions de séisme et de "
                    "volcan ; les échelles de temps géologique (an, Ma, Ga) ; "
                    "les conversions d'unités de longueur ; la formule de "
                    "vitesse v=d/t.",
                    width=56,
                ),
                font_size=24,
            ),
            box_width=12.0,
        )
        prerequis.next_to(titre, DOWN, buff=0.6)

        with self.voiceover(
            text=(
                "Avant de commencer, quelques prérequis sont à réviser : la "
                "structure interne de la Terre, croûte, manteau et noyau ; "
                "les notions de séisme et de volcan ; les échelles de temps "
                "géologique, l'an, le million d'années noté Ma, le milliard "
                "d'années noté Ga ; les conversions d'unités de longueur ; "
                "et la formule de vitesse, v égale d sur t."
            )
        ) as tracker:
            self.play(FadeIn(prerequis))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(prerequis))

        # --- Piège à éviter : réduire ce chapitre à une redite du chapitre 6
        piege = warning_box(
            Text(
                _wrap(
                    "Ce chapitre reprend des notions déjà vues (structure du "
                    "globe, tectonique des plaques) mais ne s'y arrête pas : "
                    "il apporte les preuves concrètes du mouvement "
                    "(paléomagnétisme, âge des fonds océaniques) et détaille "
                    "les trois types de limites entre plaques.",
                    width=56,
                ),
                font_size=24,
            ),
            box_width=11.5,
        )
        piege.next_to(titre, DOWN, buff=0.6)

        with self.voiceover(
            text=(
                "Attention : ce chapitre reprend des notions déjà abordées, "
                "comme la structure du globe ou la tectonique des plaques, "
                "mais il ne s'y arrête pas. Il apporte les preuves concrètes "
                "du mouvement, paléomagnétisme et âge des fonds océaniques, "
                "et détaille les trois types de limites entre plaques. Ne "
                "vous contentez pas de réviser : ce chapitre va plus loin."
            )
        ) as tracker:
            self.play(FadeIn(piege))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(titre), FadeOut(piege))
