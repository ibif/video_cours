"""
scenes/SVT_DigestionAliments_01.py — Chapitre 12 (1ereD, SVT), scène 01.

Introduction du chapitre « La digestion des aliments » : activité d'Awa au
marché Gouro d'Adjamé et le repas familial, questions guides, objectifs du
chapitre, prérequis à réviser.
Source : 1ereD/SVT.pdf, pages 155-156.
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


class IntroductionDigestionAliments(NotionScene):
    def construct(self):
        titre = scene_title("Chapitre 12 — La digestion des aliments")
        titre.scale(0.6)
        titre.to_edge(UP)

        # --- Énoncé : mise en situation --------------------------------
        sous_titre = Text("Au marché Gouro d'Adjamé", font_size=28, color=YELLOW, weight="BOLD")
        sous_titre.next_to(titre, DOWN, buff=0.5)

        histoire = Text(
            _wrap(
                "Awa a acheté de l'attiéké, un capitaine, des bananes "
                "plantain et de l'huile rouge. Le soir, toute la famille "
                "partage un repas : attiéké, poisson braisé et aloko. "
                "Pendant le dîner, la grand-mère répète : « Mâche bien "
                "avant d'avaler ! »",
                width=56,
            ),
            font_size=25,
            color=WHITE,
        )
        histoire.next_to(sous_titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Au marché Gouro d'Adjamé, Awa a acheté de l'attiéké, un "
                "capitaine, des bananes plantain et de l'huile rouge. Le "
                "soir, toute la famille partage un repas : attiéké, "
                "poisson braisé et aloko. Pendant le dîner, la grand-mère "
                "répète à Awa : mâche bien avant d'avaler !"
            )
        ) as tracker:
            self.play(Write(titre))
            self.play(FadeIn(sous_titre))
            self.play(FadeIn(histoire))
            self.wait(tracker.get_remaining_duration())

        question = Text(
            _wrap(
                "Que deviennent ces aliments dans l'organisme d'Awa ? "
                "Pourquoi faut-il bien mastiquer ? Comment les grosses "
                "molécules des aliments — amidon, protéines, graisses — "
                "peuvent-elles devenir de petites molécules utilisables "
                "par les cellules du corps ?",
                width=56,
            ),
            font_size=25,
            color=WHITE,
        )
        question.next_to(histoire, DOWN, buff=0.35)

        with self.voiceover(
            text=(
                "Que deviennent ces aliments dans l'organisme d'Awa ? "
                "Pourquoi faut-il bien mastiquer ? Comment les grosses "
                "molécules des aliments — l'amidon de l'attiéké, les "
                "protéines du poisson, les graisses de l'huile — "
                "peuvent-elles devenir de petites molécules utilisables "
                "par les cellules du corps ? Pour répondre, suivons le "
                "voyage d'une bouchée d'attiéké au poisson, organe après "
                "organe."
            )
        ) as tracker:
            self.play(FadeIn(question))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(sous_titre), FadeOut(histoire), FadeOut(question))

        # --- Animation du raisonnement : les questions guides -----------
        entete_questions = Text(
            "Trois questions guideront notre étude :", font_size=27, color=YELLOW, weight="BOLD"
        )
        entete_questions.next_to(titre, DOWN, buff=0.6)

        q1 = Text("1. Quels organes transforment les aliments, et comment ?", font_size=23, color=WHITE)
        q2 = Text("2. Quelles enzymes agissent, sur quels nutriments ?", font_size=23, color=WHITE)
        q3 = Text("3. Comment les nutriments passent-ils dans le sang ?", font_size=23, color=WHITE)
        questions = VGroup(q1, q2, q3).arrange(DOWN, aligned_edge=LEFT, buff=0.32)
        questions.next_to(entete_questions, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Première question : quels organes transforment les "
                "aliments, et comment ?"
            )
        ) as tracker:
            self.play(FadeIn(entete_questions))
            self.play(Write(q1))
            self.wait(tracker.get_remaining_duration())

        with self.voiceover(
            text="Deuxième question : quelles enzymes agissent, et sur quels nutriments ?"
        ) as tracker:
            self.play(Write(q2))
            self.wait(tracker.get_remaining_duration())

        with self.voiceover(
            text="Troisième question : comment les nutriments passent-ils finalement dans le sang ?"
        ) as tracker:
            self.play(Write(q3))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(entete_questions), FadeOut(questions))

        # --- Exemple traité : objectifs du chapitre ----------------------
        entete_objectifs = Text("Objectifs du chapitre", font_size=27, color=YELLOW, weight="BOLD")
        entete_objectifs.next_to(titre, DOWN, buff=0.55)

        objectifs = _bullets(
            [
                "Définir aliment, nutriment et digestion ; distinguer transformations mécaniques et chimiques.",
                "Décrire le système digestif : organes du tube digestif et glandes annexes.",
                "Citer les sucs digestifs et leurs enzymes, et leur rôle sur glucides, protéines, lipides.",
                "Interpréter des expériences simples sur les enzymes digestives et leurs conditions d'action.",
                "Expliquer l'absorption intestinale et le devenir des nutriments.",
                "Appliquer les règles d'hygiène du système digestif.",
            ],
            font_size=20,
            width=54,
        )
        objectifs.next_to(entete_objectifs, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "À l'issue de ce chapitre, l'élève doit être capable de "
                "définir les notions d'aliment, de nutriment et de "
                "digestion, et de distinguer les transformations "
                "mécaniques des transformations chimiques ; de décrire "
                "l'organisation du système digestif, ses organes et ses "
                "glandes annexes ; de citer les sucs digestifs et leurs "
                "enzymes ; d'interpréter des expériences simples sur les "
                "enzymes digestives ; d'expliquer l'absorption intestinale "
                "et le devenir des nutriments ; et enfin d'appliquer les "
                "règles d'hygiène qui protègent le système digestif."
            )
        ) as tracker:
            self.play(FadeIn(entete_objectifs))
            self.play(FadeIn(objectifs))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(entete_objectifs), FadeOut(objectifs))

        # --- À retenir : prérequis à réviser ------------------------------
        prerequis = essentiel_box(
            Text(
                _wrap(
                    "Prérequis à réviser : les nutriments (glucides, "
                    "protéines, lipides, vitamines, sels minéraux, eau) ; "
                    "les tests — eau iodée (amidon → bleu violet), liqueur "
                    "de Fehling (sucre réducteur → précipité rouge brique), "
                    "réactif biuret (protéines → violet) ; la notion "
                    "d'organe ; le pH (acide, neutre, basique).",
                    width=56,
                ),
                font_size=22,
            ),
            box_width=12.2,
        )
        prerequis.next_to(titre, DOWN, buff=0.55)

        with self.voiceover(
            text=(
                "Avant de commencer, quelques prérequis sont à réviser : "
                "les nutriments — glucides, protéines, lipides, vitamines, "
                "sels minéraux et eau ; les tests d'identification, l'eau "
                "iodée qui devient bleu violet en présence d'amidon, la "
                "liqueur de Fehling qui donne un précipité rouge brique en "
                "présence d'un sucre réducteur, et le réactif biuret qui "
                "vire au violet en présence de protéines ; la notion "
                "d'organe ; et enfin la notion de pH, un milieu acide, "
                "neutre ou basique."
            )
        ) as tracker:
            self.play(FadeIn(prerequis))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(prerequis))

        # --- Piège à éviter : réduire ce chapitre à un menu -----------------
        piege = warning_box(
            Text(
                _wrap(
                    "Ce chapitre ne se limite pas à décrire un repas : il "
                    "explique, organe après organe, comment les grosses "
                    "molécules des aliments deviennent des nutriments "
                    "capables de traverser la paroi de l'intestin et de "
                    "nourrir chaque cellule du corps d'Awa.",
                    width=56,
                ),
                font_size=23,
            ),
            box_width=11.8,
        )
        piege.next_to(titre, DOWN, buff=0.6)

        with self.voiceover(
            text=(
                "Attention à ne pas réduire ce chapitre à la description "
                "d'un repas : l'essentiel est de comprendre, organe après "
                "organe, comment les grosses molécules des aliments "
                "deviennent des nutriments capables de traverser la paroi "
                "de l'intestin et de nourrir chaque cellule du corps "
                "d'Awa."
            )
        ) as tracker:
            self.play(FadeIn(piege))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(titre), FadeOut(piege))
