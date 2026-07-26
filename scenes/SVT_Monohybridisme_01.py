"""
scenes/SVT_Monohybridisme_01.py — Chapitre 4 (1ereD, SVT), scène 01.

Introduction du chapitre « La transmission d'un caractère héréditaire : le
monohybridisme » : activité d'introduction (le maïs violet/blanc de
Bouaké), trois questions guides, objectifs du chapitre, prérequis à
réviser, piège à éviter dès le départ. Source : 1ereD/SVT.pdf, page 47.
"""

import textwrap

from manim import DOWN, LEFT, UP, WHITE, YELLOW, FadeIn, FadeOut, MathTex, Text, VGroup, Write

from shapes.base_scene import NotionScene
from shapes.boxes import essentiel_box, scene_title, warning_box


def _wrap(text: str, width: int = 58) -> str:
    return "\n".join(textwrap.fill(line, width=width) for line in text.split("\n"))


def _bullets(items, font_size=24, color=WHITE, width=56):
    lines = VGroup(
        *[Text(f"• {_wrap(it, width=width)}", font_size=font_size, color=color) for it in items]
    )
    lines.arrange(DOWN, aligned_edge=LEFT, buff=0.22)
    return lines


class IntroductionMonohybridisme(NotionScene):
    def construct(self):
        titre = scene_title("Chapitre 4 — Le monohybridisme")
        titre.scale(0.72)
        titre.to_edge(UP)

        # --- Énoncé : l'activité du maïs de Bouaké --------------------------
        sous_titre = Text("Mise en situation", font_size=30, color=YELLOW, weight="BOLD")
        sous_titre.next_to(titre, DOWN, buff=0.5)

        histoire1 = Text(
            _wrap(
                "À Bouaké, un producteur cultive séparément deux lignées "
                "pures de maïs : grains violets et grains blancs. Il croise "
                "les deux variétés. Surprise à la récolte : tous les grains "
                "de la première génération (F1) sont violets.",
                width=56,
            ),
            font_size=26,
            color=WHITE,
        )
        histoire1.next_to(sous_titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "À Bouaké, dans une coopérative agricole, un producteur de "
                "maïs cultive séparément deux variétés depuis plusieurs "
                "années : une à grains violets, une à grains blancs. Semée "
                "seule, chacune donne toujours des épis identiques à "
                "elle-même : ce sont des lignées pures. Par curiosité, il "
                "croise les deux variétés. À la récolte, surprise : tous les "
                "grains de cette première génération, notée F1, sont "
                "violets. Le caractère grains blancs semble avoir disparu."
            )
        ) as tracker:
            self.play(Write(titre))
            self.play(FadeIn(sous_titre))
            self.play(FadeIn(histoire1))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(histoire1))

        # --- Animation du raisonnement : la F2 et les 3 questions -----------
        histoire2 = Text(
            _wrap(
                "Le producteur sème ces grains violets de la F1 et laisse "
                "les plants se féconder entre eux. Nouvelle surprise dans "
                "la récolte suivante (F2) : 598 épis à grains violets et "
                "202 épis à grains blancs — environ 3/4 de violets et 1/4 "
                "de blancs. Le caractère blanc est réapparu.",
                width=56,
            ),
            font_size=25,
            color=WHITE,
        )
        histoire2.next_to(sous_titre, DOWN, buff=0.4)

        proportions = MathTex(
            r"598 \;\text{violets} \;\approx\; \dfrac{3}{4} \qquad\qquad 202 \;\text{blancs} \;\approx\; \dfrac{1}{4}",
            font_size=30,
            color=YELLOW,
        )
        proportions.next_to(histoire2, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Le producteur sème alors ces grains violets de la F1 et "
                "laisse les plants se féconder entre eux. Nouvelle surprise "
                "dans la récolte suivante, la F2 : il compte cinq cent "
                "quatre-vingt-dix-huit épis à grains violets et deux cent "
                "deux épis à grains blancs, soit environ trois quarts de "
                "violets et un quart de blancs. Le caractère blanc est "
                "réapparu."
            )
        ) as tracker:
            self.play(FadeIn(histoire2))
            self.play(Write(proportions))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(sous_titre), FadeOut(histoire2), FadeOut(proportions))

        entete_questions = Text(
            "Trois questions guideront ce chapitre :", font_size=28, color=YELLOW, weight="BOLD"
        )
        entete_questions.next_to(titre, DOWN, buff=0.6)

        q1 = Text("1. Où était passé le caractère « blanc » dans la F1 ?", font_size=25, color=WHITE)
        q2 = Text("2. Pourquoi réapparaît-il dans la F2 ?", font_size=25, color=WHITE)
        q3 = Text("3. Pourquoi toujours des proportions voisines de 3/4 et 1/4 ?", font_size=25, color=WHITE)
        questions = VGroup(q1, q2, q3).arrange(DOWN, aligned_edge=LEFT, buff=0.35)
        questions.next_to(entete_questions, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Trois questions guideront ce chapitre. Première question : "
                "où était passé le caractère blanc dans la F1 ? Deuxième "
                "question : pourquoi réapparaît-il dans la F2 ? Troisième "
                "question : pourquoi toujours dans des proportions voisines "
                "de trois quarts et un quart ? C'est à ces questions, et à "
                "bien d'autres, que répond ce chapitre."
            )
        ) as tracker:
            self.play(FadeIn(entete_questions))
            self.play(Write(q1))
            self.play(Write(q2))
            self.play(Write(q3))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(entete_questions), FadeOut(questions))

        # --- Exemple traité : objectifs du chapitre --------------------------
        entete_objectifs = Text("Objectifs du chapitre", font_size=28, color=YELLOW, weight="BOLD")
        entete_objectifs.next_to(titre, DOWN, buff=0.55)

        objectifs = _bullets(
            [
                "Définir et distinguer caractère héréditaire, gène, allèle, "
                "locus, génotype, phénotype, homozygote, hétérozygote.",
                "Distinguer un allèle dominant d'un allèle récessif à "
                "partir des résultats d'un croisement.",
                "Interpréter un croisement monohybride (F1 uniforme ; F2 en "
                "3/4 dominant - 1/4 récessif) avec un échiquier.",
                "Exploiter un croisement-test pour déterminer le génotype "
                "d'un individu de phénotype dominant.",
                "Traiter codominance (1/4-1/2-1/4) et allèle létal "
                "(2/3-1/3).",
                "Calculer des probabilités de transmission, par exemple "
                "pour l'albinisme dans une famille.",
            ],
            font_size=21,
            width=56,
        )
        objectifs.next_to(entete_objectifs, DOWN, buff=0.35)

        with self.voiceover(
            text=(
                "À l'issue de ce chapitre, l'élève doit être capable de "
                "définir et distinguer les termes caractère héréditaire, "
                "gène, allèle, locus, génotype, phénotype, homozygote et "
                "hétérozygote ; de distinguer un allèle dominant d'un allèle "
                "récessif à partir des résultats d'un croisement ; "
                "d'interpréter les résultats d'un croisement monohybride, "
                "avec une F1 uniforme et une F2 composée de trois quarts de "
                "phénotype dominant et un quart de phénotype récessif, en "
                "construisant un échiquier de croisement ; d'exploiter un "
                "croisement-test pour déterminer le génotype d'un individu "
                "de phénotype dominant ; de traiter des situations "
                "particulières comme la codominance et l'allèle létal ; et "
                "enfin de calculer des probabilités de transmission d'un "
                "caractère, par exemple dans une famille humaine, dans le "
                "cas de l'albinisme."
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
                    "Prérequis à réviser : la cellule et son noyau, les "
                    "chromosomes, supports de l'information héréditaire ; "
                    "la mitose (conserve 2n) ; la méiose (2n -> n dans les "
                    "gamètes) ; la fécondation (rétablit 2n dans le "
                    "zygote) ; la reproduction sexuée (gamètes, zygote, "
                    "parents mâle et femelle) ; les fractions et calculs de "
                    "proportions (1/4, 1/2, 3/4).",
                    width=56,
                ),
                font_size=23,
            ),
            box_width=12.3,
        )
        prerequis.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Quelques prérequis sont à réviser avant de commencer : la "
                "cellule et son noyau ; les chromosomes, supports de "
                "l'information héréditaire ; la mitose, division qui "
                "conserve le nombre de chromosomes ; la méiose, division qui "
                "produit des gamètes à n chromosomes ; la fécondation, qui "
                "rétablit le nombre deux n dans le zygote ; la reproduction "
                "sexuée, avec ses gamètes, son zygote, son parent mâle et "
                "son parent femelle ; et enfin les fractions et le calcul de "
                "proportions : un quart, un demi, trois quarts."
            )
        ) as tracker:
            self.play(FadeIn(prerequis))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(prerequis))

        # --- Piège à éviter ----------------------------------------------------
        piege = warning_box(
            Text(
                _wrap(
                    "Ne concluez pas trop vite que le caractère blanc a "
                    "« disparu » dans la F1 : ce serait faux, et c'est "
                    "justement l'erreur que ce chapitre va vous apprendre à "
                    "éviter. La bonne explication viendra avec la notion "
                    "d'allèle dominant et récessif.",
                    width=56,
                ),
                font_size=24,
            ),
            box_width=12.0,
        )
        piege.next_to(titre, DOWN, buff=0.55)

        with self.voiceover(
            text=(
                "Attention, dès à présent : ne concluez pas trop vite que le "
                "caractère blanc a disparu dans la F1. Ce serait une erreur "
                "— et c'est justement le genre d'erreur que ce chapitre va "
                "vous apprendre à éviter, grâce à la notion d'allèle "
                "dominant et d'allèle récessif."
            )
        ) as tracker:
            self.play(FadeIn(piege))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(titre), FadeOut(piege))
