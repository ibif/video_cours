"""
scenes/SVT_ProductionMatiere_01.py — Chapitre 11 (1ereD, SVT), scène 01.

Introduction du chapitre « La production de la matière » : activité
d'introduction (le champ de maïs de Kouadio à Bouaké, les trois questions
de sa fille Aya), objectifs du chapitre, prérequis à réviser.
Source : 1ereD/SVT.pdf, pages 143-144.
"""

import textwrap

from manim import DOWN, LEFT, UP, WHITE, YELLOW, FadeIn, FadeOut, Text, VGroup, Write

from shapes.base_scene import NotionScene
from shapes.boxes import essentiel_box, scene_title


def _wrap(text: str, width: int = 56) -> str:
    return "\n".join(textwrap.fill(line, width=width) for line in text.split("\n"))


def _bullets(items, font_size=24, color=WHITE, width=54):
    lines = VGroup(
        *[Text(f"• {_wrap(it, width=width)}", font_size=font_size, color=color) for it in items]
    )
    lines.arrange(DOWN, aligned_edge=LEFT, buff=0.22)
    return lines


class IntroductionProductionMatiere(NotionScene):
    def construct(self):
        # --- Énoncé : mise en situation --------------------------------
        titre = scene_title("Chapitre 11 — La production de la matière")
        titre.scale(0.6)
        titre.to_edge(UP)

        sous_titre = Text("Le champ de maïs de Kouadio", font_size=28, color=YELLOW, weight="BOLD")
        sous_titre.next_to(titre, DOWN, buff=0.5)

        histoire = Text(
            _wrap(
                "Kouadio cultive un champ de maïs près de Bouaké. En mars, "
                "il sème des grains de quelques grammes. Quatre mois plus "
                "tard, chaque plant mesure plus de deux mètres et porte de "
                "gros épis : l'ensemble pèse plusieurs kilogrammes.",
                width=56,
            ),
            font_size=25,
            color=WHITE,
        )
        histoire.next_to(sous_titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Kouadio cultive un champ de maïs près de Bouaké. Au mois "
                "de mars, il sème des grains de quelques grammes seulement. "
                "Quatre mois plus tard, chaque plant mesure plus de deux "
                "mètres et porte de gros épis : l'ensemble pèse plusieurs "
                "kilogrammes."
            )
        ) as tracker:
            self.play(Write(titre))
            self.play(FadeIn(sous_titre))
            self.play(FadeIn(histoire))
            self.wait(tracker.get_remaining_duration())

        question_intro = Text(
            _wrap(
                "Pourtant, personne n'a vu le maïs « manger » la terre du "
                "champ, et la quantité de terre autour des racines n'a "
                "presque pas diminué. Sa fille Aya, élève en première D, "
                "se pose alors trois questions.",
                width=56,
            ),
            font_size=25,
            color=WHITE,
        )
        question_intro.next_to(histoire, DOWN, buff=0.35)

        with self.voiceover(
            text=(
                "Pourtant, entre-temps, personne n'a vu le maïs manger la "
                "terre du champ, et la quantité de terre autour des racines "
                "n'a presque pas diminué. Sa fille Aya, élève en classe de "
                "première D, se pose alors trois questions."
            )
        ) as tracker:
            self.play(FadeIn(question_intro))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(sous_titre), FadeOut(histoire), FadeOut(question_intro))

        # --- Animation du raisonnement : les trois questions d'Aya ------
        entete_questions = Text(
            "Les trois questions d'Aya :", font_size=27, color=YELLOW, weight="BOLD"
        )
        entete_questions.next_to(titre, DOWN, buff=0.6)

        q1 = Text(
            _wrap("1. D'où vient toute cette matière fabriquée par le maïs ?", width=52),
            font_size=24,
            color=WHITE,
        )
        q2 = Text(
            _wrap(
                "2. Pourquoi les plants placés sous un hangar sombre "
                "jaunissent et finissent par mourir ?",
                width=52,
            ),
            font_size=24,
            color=WHITE,
        )
        q3 = Text(
            _wrap(
                "3. Pourquoi dit-on que les grandes forêts, comme celle de "
                "Taï, sont le « poumon » de la planète ?",
                width=52,
            ),
            font_size=24,
            color=WHITE,
        )
        questions = VGroup(q1, q2, q3).arrange(DOWN, aligned_edge=LEFT, buff=0.35)
        questions.next_to(entete_questions, DOWN, buff=0.5)

        with self.voiceover(
            text="D'où vient toute cette matière fabriquée par le maïs ?"
        ) as tracker:
            self.play(FadeIn(entete_questions))
            self.play(Write(q1))
            self.wait(tracker.get_remaining_duration())

        with self.voiceover(
            text=(
                "Pourquoi les plants placés sous un hangar sombre "
                "jaunissent-ils et finissent-ils par mourir ?"
            )
        ) as tracker:
            self.play(Write(q2))
            self.wait(tracker.get_remaining_duration())

        with self.voiceover(
            text=(
                "Et pourquoi dit-on que les grandes forêts, comme celle de "
                "Taï, sont le poumon de la planète ?"
            )
        ) as tracker:
            self.play(Write(q3))
            self.wait(tracker.get_remaining_duration())

        with self.voiceover(
            text=(
                "Ce chapitre répond à ces questions : il explique comment "
                "le végétal vert produit sa matière à partir de matière "
                "minérale, grâce à l'énergie de la lumière."
            )
        ) as tracker:
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(entete_questions), FadeOut(questions))

        # --- Exemple traité : objectifs du chapitre ----------------------
        entete_objectifs = Text("Objectifs du chapitre", font_size=27, color=YELLOW, weight="BOLD")
        entete_objectifs.next_to(titre, DOWN, buff=0.5)

        objectifs = _bullets(
            [
                "Décrire et interpréter des expériences d'échanges gazeux "
                "entre un végétal vert et l'atmosphère.",
                "Citer et justifier les conditions nécessaires à la "
                "production de matière organique (lumière, chlorophylle, "
                "CO2, eau et sels minéraux).",
                "Mettre en œuvre le test à l'eau iodée et interpréter le "
                "résultat.",
                "Localiser les organes (racine, feuille) et structures "
                "cellulaires (stomates, chloroplastes) concernés.",
                "Écrire et équilibrer l'équation bilan de l'assimilation "
                "chlorophyllienne.",
                "Expliquer l'importance de la production de matière pour "
                "le végétal, l'homme et l'équilibre de la nature.",
            ],
            font_size=20,
            width=56,
        )
        objectifs.next_to(entete_objectifs, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "À l'issue de ce chapitre, l'élève doit être capable de "
                "décrire et interpréter des expériences mettant en "
                "évidence les échanges gazeux entre un végétal vert et "
                "l'atmosphère ; de citer et justifier les conditions "
                "nécessaires à la production de matière organique, à "
                "savoir la lumière, la chlorophylle, le dioxyde de "
                "carbone, l'eau et les sels minéraux ; de mettre en œuvre "
                "le test à l'eau iodée pour rechercher l'amidon dans une "
                "feuille et d'interpréter le résultat ; de localiser les "
                "organes, racine et feuille, et les structures "
                "cellulaires, stomates et chloroplastes, qui interviennent "
                "dans la production de matière ; d'écrire et d'équilibrer "
                "l'équation bilan de l'assimilation chlorophyllienne et "
                "d'expliquer la transformation d'énergie qu'elle traduit ; "
                "et enfin d'expliquer l'importance de la production de "
                "matière par les végétaux verts pour le végétal lui-même, "
                "pour l'homme et pour l'équilibre de la nature."
            )
        ) as tracker:
            self.play(FadeIn(entete_objectifs))
            self.play(FadeIn(objectifs))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(entete_objectifs), FadeOut(objectifs))

        # --- À retenir : prérequis à réviser ------------------------------
        prerequis = essentiel_box(
            _bullets(
                [
                    "La cellule végétale : membrane, cytoplasme, noyau, "
                    "paroi, plastes.",
                    "Les organes de la plante : racine, tige, feuille, "
                    "fleur, fruit.",
                    "Tests de gaz : l'eau de chaux se trouble avec le CO2 ; "
                    "une braise se ravive avec le O2.",
                    "Matière organique (glucides, lipides, protides) et "
                    "matière minérale (eau, sels minéraux).",
                    "Le test à l'eau iodée : jaune-brun, devient bleu-noir "
                    "avec l'amidon.",
                    "Équilibrer une équation chimique simple.",
                ],
                font_size=19,
                width=56,
            ),
            box_width=12.0,
        )
        prerequis.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Avant de commencer, quelques prérequis sont à réviser : "
                "les notions de seconde sur la cellule végétale, membrane, "
                "cytoplasme, noyau, paroi, plastes ; les organes de la "
                "plante étudiés au collège, racine, tige, feuille, fleur, "
                "fruit ; les tests d'identification des gaz, l'eau de "
                "chaux qui se trouble en présence de dioxyde de carbone, et "
                "la braise incandescente qui se ravive en présence de "
                "dioxygène ; la notion de matière organique et de matière "
                "minérale vue en classe de seconde ; le test à l'eau "
                "iodée, jaune-brun, qui devient bleu-noir en présence "
                "d'amidon ; et enfin, savoir équilibrer une équation "
                "chimique simple."
            )
        ) as tracker:
            self.play(FadeIn(prerequis))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(titre), FadeOut(prerequis))
