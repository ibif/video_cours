"""
scenes/SVT_FonctionsGonades_01.py — Chapitre 1 (1ereD, SVT), scène 01.

Introduction du chapitre « Les fonctions des gonades » : activité
d'introduction (le coq castré de Bouaké), objectifs du chapitre, prérequis
à réviser. Source : 1ereD/SVT.pdf, page 5.
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


class IntroductionFonctionsGonades(NotionScene):
    def construct(self):
        # --- Énoncé : mise en situation ----------------------------------
        titre = scene_title("Chapitre 1 — Les fonctions des gonades")
        titre.scale(0.75)
        titre.to_edge(UP)

        sous_titre = Text("Mise en situation", font_size=30, color=YELLOW, weight="BOLD")
        sous_titre.next_to(titre, DOWN, buff=0.5)

        histoire = Text(
            _wrap(
                "Au marché de Bouaké, Mamadou transforme des coqs en « chapons » : "
                "il leur retire les testicules pour qu'ils grossissent plus vite. "
                "Sa fille Awa, en 1ère D, observe que la crête du chapon pâlit et "
                "retombe, qu'il ne chante presque plus et ignore les poules.",
                width=56,
            ),
            font_size=26,
            color=WHITE,
        )
        histoire.next_to(sous_titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Au marché de Bouaké, Mamadou, jeune éleveur de volailles, "
                "transforme certains coqs en chapons : il leur retire les "
                "testicules pour qu'ils grossissent plus vite et que leur chair "
                "reste tendre. Quelques semaines plus tard, sa fille Awa, élève "
                "en première D, observe des changements surprenants : la crête "
                "du chapon, autrefois rouge vif et dressée, pâlit et retombe ; "
                "l'animal ne chante presque plus et ignore totalement les poules."
            )
        ) as tracker:
            self.play(Write(titre))
            self.play(FadeIn(sous_titre))
            self.play(FadeIn(histoire))
            self.wait(tracker.get_remaining_duration())

        question_awa = Text(
            _wrap(
                "Awa se demande : que fabriquaient donc les testicules du coq "
                "pour que leur retrait transforme ainsi son allure et son "
                "comportement ? Comment un organe si petit peut-il commander "
                "à distance tout le corps ?",
                width=56,
            ),
            font_size=26,
            color=WHITE,
        )
        question_awa.next_to(histoire, DOWN, buff=0.35)

        with self.voiceover(
            text=(
                "Awa se demande alors : que fabriquaient donc les testicules du "
                "coq pour que leur retrait transforme ainsi son allure et son "
                "comportement ? Comment un organe si petit peut-il commander à "
                "distance tout le corps ? Ce chapitre, intitulé les fonctions "
                "des gonades, apporte les réponses."
            )
        ) as tracker:
            self.play(FadeIn(question_awa))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(sous_titre), FadeOut(histoire), FadeOut(question_awa))

        # --- Animation du raisonnement : les 3 questions guides ----------
        entete_questions = Text(
            "Trois questions guideront notre étude :", font_size=28, color=YELLOW, weight="BOLD"
        )
        entete_questions.next_to(titre, DOWN, buff=0.6)

        q1 = Text("1. Quels sont les organes appelés gonades, et où se trouvent-ils ?", font_size=26, color=WHITE)
        q2 = Text("2. Que produisent-ils exactement ?", font_size=26, color=WHITE)
        q3 = Text("3. Comment leurs produits agissent-ils sur l'organisme ?", font_size=26, color=WHITE)
        questions = VGroup(q1, q2, q3).arrange(DOWN, aligned_edge=LEFT, buff=0.35)
        questions.next_to(entete_questions, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Première question : quels sont les organes appelés gonades, et "
                "où se trouvent-ils dans le corps ?"
            )
        ) as tracker:
            self.play(FadeIn(entete_questions))
            self.play(Write(q1))
            self.wait(tracker.get_remaining_duration())

        with self.voiceover(text="Deuxième question : que produisent-ils exactement ?") as tracker:
            self.play(Write(q2))
            self.wait(tracker.get_remaining_duration())

        with self.voiceover(
            text="Troisième question : comment leurs produits agissent-ils sur l'organisme ?"
        ) as tracker:
            self.play(Write(q3))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(entete_questions), FadeOut(questions))

        # --- Exemple traité : objectifs du chapitre (ce que l'on va apprendre) --
        entete_objectifs = Text("Objectifs du chapitre", font_size=28, color=YELLOW, weight="BOLD")
        entete_objectifs.next_to(titre, DOWN, buff=0.55)

        objectifs = _bullets(
            [
                "Définir une gonade et citer les gonades humaines.",
                "Distinguer fonction exocrine (gamètes) et fonction endocrine (hormones).",
                "Exploiter des expériences de castration, greffe et ligature.",
                "Décrire et comparer spermatogenèse et ovogenèse.",
                "Relier chaque hormone sexuelle à sa structure productrice et à ses rôles.",
            ],
            font_size=24,
            width=54,
        )
        objectifs.next_to(entete_objectifs, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "À la fin de ce chapitre, l'élève doit être capable de définir "
                "une gonade et de citer les gonades de l'espèce humaine, de "
                "distinguer la fonction exocrine, qui produit des gamètes, et "
                "la fonction endocrine, qui produit des hormones sexuelles, "
                "d'exploiter des expériences de castration, de greffe et de "
                "ligature des voies génitales, de décrire et comparer la "
                "spermatogenèse et l'ovogenèse, et enfin de relier chaque "
                "hormone sexuelle à sa structure productrice et à ses rôles."
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
                    "Prérequis à réviser : la cellule et son noyau, la notion de "
                    "chromosome ; le caryotype humain (2n=46 dans les cellules "
                    "ordinaires, n=23 dans les cellules reproductrices) ; la "
                    "méiose, qui transforme une cellule à 2n=46 en cellules à "
                    "n=23 ; l'anatomie des appareils reproducteurs ; la notion "
                    "d'hormone, substance transportée par le sang et agissant "
                    "à distance sur un organe cible.",
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
                "cellule et son noyau, la notion de chromosome, support de "
                "l'information héréditaire ; le caryotype humain, avec deux n "
                "égale quarante-six chromosomes dans nos cellules et n égale "
                "vingt-trois dans les cellules reproductrices ; la méiose, qui "
                "transforme une cellule à deux n égale quarante-six en cellules "
                "à n égale vingt-trois ; l'anatomie générale des appareils "
                "reproducteurs ; et la notion d'hormone, une substance chimique "
                "transportée par le sang et agissant à distance sur un organe "
                "cible."
            )
        ) as tracker:
            self.play(FadeIn(prerequis))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(prerequis))

        # --- Piège à éviter : réduire ce chapitre à de l'anatomie ---------
        piege = warning_box(
            Text(
                _wrap(
                    "Ce chapitre ne se limite pas à repérer la position des "
                    "gonades : il explique comment leurs produits, gamètes et "
                    "hormones, agissent - parfois à distance - sur tout "
                    "l'organisme.",
                    width=56,
                ),
                font_size=25,
            ),
            box_width=11.5,
        )
        piege.next_to(titre, DOWN, buff=0.6)

        with self.voiceover(
            text=(
                "Attention à ne pas réduire ce chapitre à une simple leçon "
                "d'anatomie : l'essentiel est de comprendre comment un petit "
                "organe, la gonade, produit des substances qui agissent, "
                "parfois à distance, sur tout le corps."
            )
        ) as tracker:
            self.play(FadeIn(piege))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(titre), FadeOut(piege))
