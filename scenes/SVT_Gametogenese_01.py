"""
scenes/SVT_Gametogenese_01.py — Chapitre 3 (1ereD, SVT), scène 01.

Introduction du chapitre « La gamétogénèse » : les deux documents de
Korhogo (photo du tube séminifère de bélier, carnet de santé d'une
maternité d'Abidjan), les trois questions guides, objectifs du chapitre,
prérequis à réviser. Source : 1ereD/SVT.pdf, page 31.
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


class IntroductionGametogenese(NotionScene):
    def construct(self):
        # --- Énoncé : mise en situation ----------------------------------
        titre = scene_title("Chapitre 3 — La gamétogénèse")
        titre.scale(0.75)
        titre.to_edge(UP)

        sous_titre = Text("Deux observations, à Korhogo", font_size=30, color=YELLOW, weight="BOLD")
        sous_titre.next_to(titre, DOWN, buff=0.5)

        doc1 = Text(
            _wrap(
                "Document 1. Au lycée moderne de Korhogo, une photo prise au "
                "microscope dans un tube séminifère de bélier : des dizaines "
                "de petites cellules rondes près de la paroi, et au centre "
                "une multitude de longues cellules filiformes en têtards.",
                width=56,
            ),
            font_size=24,
            color=WHITE,
        )
        doc1.next_to(sous_titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Au lycée moderne de Korhogo, le professeur de SVT présente à "
                "la classe de première D deux observations. Document un : une "
                "photographie prise au microscope dans un tube séminifère de "
                "bélier, prélevé à la ferme-école. On y voit des dizaines de "
                "petites cellules rondes près de la paroi du tube, et, au "
                "centre, une multitude de longues cellules filiformes "
                "ressemblant à des têtards."
            )
        ) as tracker:
            self.play(Write(titre))
            self.play(FadeIn(sous_titre))
            self.play(FadeIn(doc1))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(doc1))

        doc2 = Text(
            _wrap(
                "Document 2. Le carnet de santé d'une maternité d'Abidjan : "
                "une femme peut avoir un enfant entre environ 13 et 50 ans, "
                "soit une seule cellule reproductrice libérée par mois, "
                "alors que l'éjaculat d'un homme contient des millions de "
                "spermatozoïdes.",
                width=56,
            ),
            font_size=24,
            color=WHITE,
        )
        doc2.next_to(sous_titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Document deux : le carnet de santé d'une maternité "
                "d'Abidjan. Une femme peut avoir un enfant entre environ "
                "treize et cinquante ans, soit une seule cellule "
                "reproductrice libérée par mois, alors que l'éjaculat d'un "
                "homme contient des millions de spermatozoïdes."
            )
        ) as tracker:
            self.play(FadeIn(doc2))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(sous_titre), FadeOut(doc2))

        # --- Animation du raisonnement : les 3 questions guides ----------
        entete_questions = Text(
            "La classe se pose trois questions :", font_size=28, color=YELLOW, weight="BOLD"
        )
        entete_questions.next_to(titre, DOWN, buff=0.6)

        q1 = Text("1. D'où viennent ces cellules reproductrices ?", font_size=26, color=WHITE)
        q2 = Text("2. Comment se forment-elles dans les gonades ?", font_size=26, color=WHITE)
        q3 = Text(
            "3. Pourquoi les quantités produites diffèrent-elles\nautant chez l'homme et chez la femme ?",
            font_size=26,
            color=WHITE,
        )
        questions = VGroup(q1, q2, q3).arrange(DOWN, aligned_edge=LEFT, buff=0.35)
        questions.next_to(entete_questions, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "La classe se pose alors trois questions. Première question : "
                "d'où viennent ces cellules reproductrices ?"
            )
        ) as tracker:
            self.play(FadeIn(entete_questions))
            self.play(Write(q1))
            self.wait(tracker.get_remaining_duration())

        with self.voiceover(
            text="Deuxième question : comment se forment-elles dans les organes reproducteurs ?"
        ) as tracker:
            self.play(Write(q2))
            self.wait(tracker.get_remaining_duration())

        with self.voiceover(
            text=(
                "Troisième question : pourquoi les quantités produites "
                "sont-elles si différentes chez l'homme et chez la femme ? "
                "Pour répondre, nous allons étudier la gamétogénèse, "
                "c'est-à-dire l'ensemble des phénomènes qui conduisent à la "
                "formation des gamètes."
            )
        ) as tracker:
            self.play(Write(q3))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(entete_questions), FadeOut(questions))

        # --- Exemple traité : objectifs du chapitre -----------------------
        entete_objectifs = Text("Objectifs du chapitre", font_size=28, color=YELLOW, weight="BOLD")
        entete_objectifs.next_to(titre, DOWN, buff=0.55)

        objectifs = _bullets(
            [
                "Définir la gamétogénèse et nommer les gonades.",
                "Décrire les étapes de la méiose et son rôle dans la formation de cellules haploïdes.",
                "Décrire les 4 phases de la spermatogenèse et les étapes de l'ovogenèse, puis les comparer.",
                "Identifier les structures du spermatozoïde et de l'ovule, et leur rôle.",
                "Calculer un rendement de gamétogénèse et un nombre de gamètes différents.",
                "Citer les hormones FSH, LH, testostérone et préciser leur rôle.",
            ],
            font_size=22,
            width=54,
        )
        objectifs.next_to(entete_objectifs, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "À la fin de ce chapitre, l'élève doit être capable de "
                "définir la gamétogénèse et de nommer les gonades, "
                "testicules et ovaires ; de décrire les étapes de la méiose "
                "et d'expliquer comment elle produit des cellules haploïdes ; "
                "de décrire les quatre phases de la spermatogenèse et les "
                "étapes de l'ovogenèse, puis de comparer les deux ; "
                "d'identifier sur un schéma les structures du spermatozoïde "
                "et de l'ovule et de relier chacune à son rôle ; de calculer "
                "un rendement de gamétogénèse et un nombre de gamètes "
                "génétiquement différents grâce au brassage ; et enfin de "
                "citer les hormones qui contrôlent la gamétogénèse, FSH, LH "
                "et testostérone, et de préciser leur rôle."
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
                    "Prérequis à réviser : la cellule (membrane, cytoplasme, "
                    "noyau) ; les chromosomes, bâtonnets d'ADN visibles lors "
                    "de la division, 46 chromosomes en 23 paires chez "
                    "l'être humain ; la mitose (seconde), qui donne deux "
                    "cellules filles identiques ; la reproduction sexuée, "
                    "qui unit un gamète mâle et un gamète femelle ; les "
                    "puissances de 2 et les produits simples.",
                    width=56,
                ),
                font_size=22,
            ),
            box_width=12.2,
        )
        prerequis.next_to(titre, DOWN, buff=0.55)

        with self.voiceover(
            text=(
                "Avant de commencer, quelques prérequis sont à réviser : la "
                "cellule, unité structurale du vivant, avec sa membrane, son "
                "cytoplasme et son noyau ; les chromosomes, bâtonnets d'ADN "
                "situés dans le noyau et visibles au moment de la division "
                "cellulaire, quarante-six chromosomes groupés en vingt-trois "
                "paires chez l'être humain ; la mitose, vue en classe de "
                "seconde, qui donne deux cellules filles identiques à la "
                "cellule mère avec le même nombre de chromosomes ; la "
                "reproduction sexuée, qui met en jeu un gamète mâle et un "
                "gamète femelle dont l'union, la fécondation, forme une "
                "cellule œuf ; et enfin quelques notions de calcul, les "
                "puissances de deux, les produits et quotients simples."
            )
        ) as tracker:
            self.play(FadeIn(prerequis))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(prerequis))

        # --- Piège à éviter : ne pas réduire à de l'anatomie ---------------
        piege = warning_box(
            Text(
                _wrap(
                    "Ce chapitre ne se limite pas à décrire des organes : il "
                    "explique le mécanisme cellulaire, la méiose, qui produit "
                    "les gamètes, et pourquoi les quantités et les rythmes de "
                    "production diffèrent radicalement entre l'homme et la "
                    "femme.",
                    width=56,
                ),
                font_size=25,
            ),
            box_width=11.8,
        )
        piege.next_to(titre, DOWN, buff=0.6)

        with self.voiceover(
            text=(
                "Attention à ne pas réduire ce chapitre à une description "
                "d'organes : l'essentiel est de comprendre le mécanisme "
                "cellulaire, la méiose, qui produit les gamètes, et "
                "d'expliquer pourquoi les quantités et les rythmes de "
                "production diffèrent radicalement entre l'homme et la "
                "femme."
            )
        ) as tracker:
            self.play(FadeIn(piege))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(titre), FadeOut(piege))
