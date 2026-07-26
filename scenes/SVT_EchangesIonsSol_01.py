"""
scenes/SVT_EchangesIonsSol_01.py — Chapitre 8 (1ereD, SVT), scène 01.

Introduction du chapitre « Les échanges d'ions au niveau du sol » : les
parcelles d'Adama et de Konan à Daloa, questions guides, objectifs et
prérequis du chapitre. Source : 1ereD/SVT.pdf, page 103.
"""

import textwrap

from manim import DOWN, LEFT, UP, WHITE, YELLOW, FadeIn, FadeOut, Text, VGroup, Write

from shapes.base_scene import NotionScene
from shapes.boxes import essentiel_box, scene_title, warning_box


def _wrap(text: str, width: int = 58) -> str:
    return "\n".join(textwrap.fill(line, width=width) for line in text.split("\n"))


def _bullets(items, font_size=26, color=WHITE, width=58):
    lines = VGroup(
        *[Text(f"• {_wrap(it, width=width)}", font_size=font_size, color=color) for it in items]
    )
    lines.arrange(DOWN, aligned_edge=LEFT, buff=0.22)
    return lines


class IntroductionEchangesIonsSol(NotionScene):
    def construct(self):
        # --- Énoncé : mise en situation ----------------------------------
        titre = scene_title("Chapitre 8 — Les échanges d'ions au niveau du sol")
        titre.scale(0.62)
        titre.to_edge(UP)

        sous_titre = Text("Mise en situation", font_size=30, color=YELLOW, weight="BOLD")
        sous_titre.next_to(titre, DOWN, buff=0.5)

        histoire = Text(
            _wrap(
                "Dans un village de la région de Daloa, deux parcelles "
                "voisines portent la même variété de maïs, semée le même "
                "jour. Sur la parcelle d'Adama, les plants sont hauts, "
                "d'un vert franc. Sur celle de son voisin Konan, ils "
                "restent chétifs et leurs feuilles jaunissent.",
                width=56,
            ),
            font_size=25,
            color=WHITE,
        )
        histoire.next_to(sous_titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Dans un village de la région de Daloa, deux parcelles "
                "voisines portent la même variété de maïs, semée le même "
                "jour. Sur la parcelle d'Adama, les plants sont hauts, d'un "
                "vert franc. Sur celle de son voisin Konan, ils restent "
                "chétifs et leurs feuilles jaunissent."
            )
        ) as tracker:
            self.play(Write(titre))
            self.play(FadeIn(sous_titre))
            self.play(FadeIn(histoire))
            self.wait(tracker.get_remaining_duration())

        question_konan = Text(
            _wrap(
                "Konan s'étonne : « Nous avons pourtant reçu la même "
                "pluie ! » Un technicien agricole analyse les deux sols : "
                "la parcelle de Konan est appauvrie en azote et en "
                "potassium, et son sol sableux retient mal les éléments "
                "nutritifs apportés par les engrais.",
                width=56,
            ),
            font_size=25,
            color=WHITE,
        )
        question_konan.next_to(histoire, DOWN, buff=0.35)

        with self.voiceover(
            text=(
                "Konan s'étonne : nous avons pourtant reçu la même pluie ! "
                "Un technicien agricole analyse les deux sols : la parcelle "
                "de Konan est appauvrie en azote et en potassium, et son "
                "sol sableux retient mal les éléments nutritifs apportés "
                "par les engrais."
            )
        ) as tracker:
            self.play(FadeIn(question_konan))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(sous_titre), FadeOut(histoire), FadeOut(question_konan))

        # --- Animation du raisonnement : les 3 questions guides ----------
        entete_questions = Text(
            "Trois questions guideront notre étude :", font_size=28, color=YELLOW, weight="BOLD"
        )
        entete_questions.next_to(titre, DOWN, buff=0.6)

        q1 = Text("1. Comment le sol fournit-il les éléments minéraux à la plante ?", font_size=25, color=WHITE)
        q2 = Text("2. Comment ces éléments passent-ils du sol dans la racine ?", font_size=25, color=WHITE)
        q3 = Text("3. Pourquoi certains sols « gardent-ils » mieux les engrais ?", font_size=25, color=WHITE)
        questions = VGroup(q1, q2, q3).arrange(DOWN, aligned_edge=LEFT, buff=0.35)
        questions.next_to(entete_questions, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Première question : comment le sol fournit-il à la plante "
                "les éléments minéraux dont elle a besoin ?"
            )
        ) as tracker:
            self.play(FadeIn(entete_questions))
            self.play(Write(q1))
            self.wait(tracker.get_remaining_duration())

        with self.voiceover(
            text="Deuxième question : comment ces éléments passent-ils du sol dans la racine ?"
        ) as tracker:
            self.play(Write(q2))
            self.wait(tracker.get_remaining_duration())

        with self.voiceover(
            text="Troisième question : pourquoi certains sols gardent-ils mieux les engrais que d'autres ?"
        ) as tracker:
            self.play(Write(q3))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(entete_questions), FadeOut(questions))

        # --- Exemple traité : objectifs du chapitre -----------------------
        entete_objectifs = Text("Objectifs du chapitre", font_size=28, color=YELLOW, weight="BOLD")
        entete_objectifs.next_to(titre, DOWN, buff=0.55)

        objectifs = _bullets(
            [
                "Décrire la composition du sol et le rôle du complexe argilo-humique.",
                "Définir la capacité d'échange de cations (CEC) et comparer deux sols.",
                "Citer les éléments minéraux nécessaires et leurs carences.",
                "Interpréter des cultures sur solutions nutritives (carence, sélectivité).",
                "Décrire l'absorption racinaire et expliquer l'intérêt de la fumure.",
            ],
            font_size=23,
            width=54,
        )
        objectifs.next_to(entete_objectifs, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "À la fin de ce chapitre, l'élève doit être capable de "
                "décrire la composition du sol et d'expliquer le rôle du "
                "complexe argilo-humique dans la rétention des cations, de "
                "définir la capacité d'échange de cations, ou CEC, et de "
                "s'en servir pour comparer la fertilité de deux sols, de "
                "citer les principaux éléments minéraux nécessaires aux "
                "plantes et de reconnaître les symptômes de leur carence, "
                "d'interpréter des expériences de culture sur solutions "
                "nutritives, de décrire les mécanismes d'absorption des "
                "ions par la racine, et enfin d'expliquer l'intérêt "
                "agronomique de la fumure pour préserver la fertilité des "
                "sols ivoiriens."
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
                    "Prérequis à réviser : structure générale d'une plante "
                    "(racine, tige, feuille) ; cellule végétale (paroi, "
                    "membrane, vacuole, cytoplasme) ; notion d'ion (cations "
                    "chargés +, anions chargés -) ; absorption de l'eau par "
                    "les racines (osmose) ; respiration cellulaire (dégrade "
                    "la matière organique, fournit l'ATP).",
                    width=56,
                ),
                font_size=23,
            ),
            box_width=12.0,
        )
        prerequis.next_to(titre, DOWN, buff=0.6)

        with self.voiceover(
            text=(
                "Avant de commencer, quelques prérequis sont à réviser : la "
                "structure générale d'une plante, avec ses racines, sa tige "
                "et ses feuilles ; la cellule végétale, avec sa paroi, sa "
                "membrane, sa vacuole et son cytoplasme ; la notion d'ion, "
                "cation chargé positivement, anion chargé négativement ; "
                "l'absorption de l'eau par les racines, ou osmose ; et la "
                "respiration cellulaire, qui dégrade la matière organique "
                "et fournit l'énergie sous forme d'ATP."
            )
        ) as tracker:
            self.play(FadeIn(prerequis))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(prerequis))

        # --- Piège à éviter : ne pas réduire à une histoire d'engrais -----
        piege = warning_box(
            Text(
                _wrap(
                    "Ce chapitre ne se limite pas à « mettre de l'engrais » "
                    ": il explique le mécanisme précis, à l'échelle des "
                    "ions, par lequel le sol retient puis libère les "
                    "éléments minéraux, et par lequel la racine les "
                    "absorbe sélectivement.",
                    width=56,
                ),
                font_size=24,
            ),
            box_width=11.5,
        )
        piege.next_to(titre, DOWN, buff=0.6)

        with self.voiceover(
            text=(
                "Attention à ne pas réduire ce chapitre à une simple "
                "consigne : mettre de l'engrais. L'essentiel est de "
                "comprendre le mécanisme précis, à l'échelle des ions, par "
                "lequel le sol retient puis libère les éléments minéraux, "
                "et par lequel la racine les absorbe, souvent de façon "
                "sélective et active."
            )
        ) as tracker:
            self.play(FadeIn(piege))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(titre), FadeOut(piege))
