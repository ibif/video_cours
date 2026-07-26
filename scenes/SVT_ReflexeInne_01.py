"""
scenes/SVT_ReflexeInne_01.py — Chapitre 10 (1ereD, SVT), scène 01.

Introduction du chapitre « Le réflexe inné » : activité de Konan au
dispensaire de Koumassi (réflexe rotulien) et d'Aminata (marmite chaude),
questions guides, objectifs du chapitre, prérequis à réviser.
Source : 1ereD/SVT.pdf, pages 131-132.
"""

import textwrap

from manim import DOWN, LEFT, UP, WHITE, YELLOW, FadeIn, FadeOut, Text, VGroup, Write

from shapes.base_scene import NotionScene
from shapes.boxes import essentiel_box, scene_title, warning_box


def _wrap(text: str, width: int = 56) -> str:
    return "\n".join(textwrap.fill(line, width=width) for line in text.split("\n"))


def _bullets(items, font_size=23, color=WHITE, width=52):
    lines = VGroup(
        *[Text(f"• {_wrap(it, width=width)}", font_size=font_size, color=color) for it in items]
    )
    lines.arrange(DOWN, aligned_edge=LEFT, buff=0.24)
    return lines


class IntroductionReflexeInne(NotionScene):
    def construct(self):
        titre = scene_title("Chapitre 10 — Le réflexe inné")
        titre.scale(0.62)
        titre.to_edge(UP)

        # --- Énoncé : mise en situation ------------------------------------
        sous_titre = Text("Au dispensaire de Koumassi", font_size=28, color=YELLOW, weight="BOLD")
        sous_titre.next_to(titre, DOWN, buff=0.5)

        histoire = Text(
            _wrap(
                "Le médecin examine Konan, un élève de première. Assis au "
                "bord de la table, jambes pendantes et muscles relâchés, "
                "Konan reçoit un petit coup sec du marteau à réflexe sous "
                "la rotule : sa jambe s'étend brusquement, sans qu'il "
                "l'ait décidé. « Impossible de l'empêcher ! » s'étonne-t-il.",
                width=56,
            ),
            font_size=24,
            color=WHITE,
        )
        histoire.next_to(sous_titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Au dispensaire de Koumassi, le médecin examine Konan, un "
                "élève de première. Assis au bord de la table d'examen, "
                "jambes pendantes et muscles bien relâchés, Konan reçoit "
                "un petit coup sec du marteau à réflexe sur le tendon situé "
                "sous la rotule. Sa jambe s'étend brusquement vers l'avant, "
                "sans qu'il l'ait décidé. Impossible de l'empêcher, "
                "s'étonne l'élève."
            )
        ) as tracker:
            self.play(Write(titre))
            self.play(FadeIn(sous_titre))
            self.play(FadeIn(histoire))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(sous_titre), FadeOut(histoire))

        sous_titre2 = Text("Dans la cour de l'école", font_size=28, color=YELLOW, weight="BOLD")
        sous_titre2.next_to(titre, DOWN, buff=0.5)

        histoire2 = Text(
            _wrap(
                "Plus loin, Aminata retire vivement sa main en touchant "
                "par mégarde la marmite chaude du repas. Elle remarque "
                "qu'elle n'a ressenti la brûlure qu'après avoir retiré la "
                "main.",
                width=56,
            ),
            font_size=24,
            color=WHITE,
        )
        histoire2.next_to(sous_titre2, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Plus loin, dans la cour de l'école, Aminata retire "
                "vivement sa main en touchant par mégarde la marmite "
                "chaude du repas. Elle remarque qu'elle n'a ressenti la "
                "brûlure qu'après avoir retiré la main."
            )
        ) as tracker:
            self.play(FadeIn(sous_titre2))
            self.play(FadeIn(histoire2))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(sous_titre2), FadeOut(histoire2))

        # --- Animation du raisonnement : questions guides -------------------
        entete_questions = Text("Ces deux histoires posent des questions :", font_size=26, color=YELLOW, weight="BOLD")
        entete_questions.next_to(titre, DOWN, buff=0.55)

        q1 = Text("1. Ces mouvements sont-ils volontaires ?", font_size=23, color=WHITE)
        q2 = Text("2. Quel organe les déclenche ?", font_size=23, color=WHITE)
        q3 = Text("3. Par quel chemin voyage l'information dans le corps ?", font_size=23, color=WHITE)
        q4 = Text("4. Pourquoi la douleur est-elle ressentie après le mouvement ?", font_size=23, color=WHITE)
        questions = VGroup(q1, q2, q3, q4).arrange(DOWN, aligned_edge=LEFT, buff=0.3)
        questions.next_to(entete_questions, DOWN, buff=0.45)

        with self.voiceover(
            text=(
                "Ces deux histoires posent plusieurs questions. Ces "
                "mouvements sont-ils volontaires ? Quel organe les "
                "déclenche ? Par quel chemin l'information voyage-t-elle "
                "dans le corps ? Et pourquoi la douleur est-elle ressentie "
                "après le mouvement, et non avant ? Ce chapitre répondra à "
                "toutes ces questions."
            )
        ) as tracker:
            self.play(FadeIn(entete_questions))
            self.play(Write(q1))
            self.play(Write(q2))
            self.play(Write(q3))
            self.play(Write(q4))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(entete_questions), FadeOut(questions))

        # --- Exemple traité : objectifs du chapitre -------------------------
        entete_objectifs = Text("Objectifs du chapitre", font_size=27, color=YELLOW, weight="BOLD")
        entete_objectifs.next_to(titre, DOWN, buff=0.55)

        objectifs = _bullets(
            [
                "Définir le réflexe et citer ses propriétés caractéristiques.",
                "Décrire le protocole et l'observation des expériences de mise en évidence (réflexe rotulien, réflexe de retrait).",
                "Nommer, ordonner et situer sur un schéma les cinq éléments de l'arc réflexe.",
                "Décrire la structure de la moelle épinière et le rôle de ses racines rachidiennes.",
                "Distinguer un réflexe monosynaptique d'un réflexe polysynaptique.",
                "Expliquer l'intérêt biologique et médical des réflexes innés.",
            ],
            font_size=19,
            width=56,
        )
        objectifs.next_to(entete_objectifs, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "À l'issue de ce chapitre, l'élève doit être capable de "
                "définir le réflexe et d'en citer les propriétés "
                "caractéristiques ; de décrire le protocole et "
                "l'observation d'une expérience de mise en évidence, "
                "réflexe rotulien ou réflexe de retrait ; de nommer, "
                "ordonner et situer sur un schéma les cinq éléments de "
                "l'arc réflexe ; de décrire la structure de la moelle "
                "épinière et le rôle de ses racines ; de distinguer un "
                "réflexe monosynaptique d'un réflexe polysynaptique ; et "
                "enfin d'expliquer l'intérêt biologique et médical des "
                "réflexes innés."
            )
        ) as tracker:
            self.play(FadeIn(entete_objectifs))
            self.play(FadeIn(objectifs))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(entete_objectifs), FadeOut(objectifs))

        # --- À retenir : prérequis à réviser ---------------------------------
        prerequis = essentiel_box(
            Text(
                _wrap(
                    "Prérequis à réviser : le système nerveux comprend des "
                    "centres nerveux (encéphale, moelle épinière) et des "
                    "nerfs qui relient les organes aux centres ; le muscle "
                    "squelettique se contracte seulement quand il reçoit un "
                    "ordre nerveux ; la peau et les organes des sens "
                    "contiennent des récepteurs sensibles aux stimulations ; "
                    "le neurone (cellule nerveuse) ; stimulation et réponse.",
                    width=56,
                ),
                font_size=20,
            ),
            box_width=12.2,
        )
        prerequis.next_to(titre, DOWN, buff=0.55)

        with self.voiceover(
            text=(
                "Avant de commencer, quelques prérequis sont à réviser : le "
                "système nerveux comprend des centres nerveux, l'encéphale "
                "et la moelle épinière, et des nerfs qui relient les "
                "organes aux centres ; le muscle squelettique ne se "
                "contracte que lorsqu'il reçoit un ordre nerveux ; la peau "
                "et les organes des sens contiennent des récepteurs "
                "sensibles aux stimulations, contact, chaleur, douleur, "
                "lumière ; la notion de neurone, vue en classe de "
                "troisième ; et le vocabulaire de base, stimulation et "
                "réponse."
            )
        ) as tracker:
            self.play(FadeIn(prerequis))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(prerequis))

        # --- Piège à éviter ---------------------------------------------------
        piege = warning_box(
            Text(
                _wrap(
                    "Ce chapitre ne se limite pas à raconter deux "
                    "anecdotes : il explique, circuit nerveux à l'appui, "
                    "pourquoi ces mouvements échappent totalement à la "
                    "volonté de Konan et d'Aminata, et comment le corps "
                    "réagit avant même que le cerveau en soit informé.",
                    width=56,
                ),
                font_size=23,
            ),
            box_width=11.8,
        )
        piege.next_to(titre, DOWN, buff=0.6)

        with self.voiceover(
            text=(
                "Attention à ne pas réduire ce chapitre à deux anecdotes : "
                "l'essentiel est de comprendre, circuit nerveux à l'appui, "
                "pourquoi ces mouvements échappent totalement à la volonté "
                "de Konan et d'Aminata, et comment le corps réagit avant "
                "même que le cerveau en soit informé."
            )
        ) as tracker:
            self.play(FadeIn(piege))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(titre), FadeOut(piege))
