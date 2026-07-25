"""
scenes/SVT_SyntheseProteines_01.py — Chapitre 5 (1ereD, SVT), scène 01.

Introduction du chapitre « La synthèse des protéines » : activité
d'introduction (Awa et son frère Koffi, atteint de drépanocytose, à
l'hôpital de Bouaké), les deux questions guides, le plan de l'étude,
objectifs et prérequis. Source : 1ereD/SVT.pdf, page 63.
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


class IntroductionSyntheseProteines(NotionScene):
    def construct(self):
        # --- Énoncé : mise en situation ----------------------------------
        titre = scene_title("Chapitre 5 — La synthèse des protéines")
        titre.scale(0.65)
        titre.to_edge(UP)

        sous_titre = Text("Mise en situation", font_size=30, color=YELLOW, weight="BOLD")
        sous_titre.next_to(titre, DOWN, buff=0.5)

        histoire = Text(
            _wrap(
                "À Bouaké, Awa accompagne son petit frère Koffi à l'hôpital : "
                "il est atteint de drépanocytose. Lors des crises, ses "
                "globules rouges se déforment en faucille et bouchent les "
                "petits vaisseaux sanguins, provoquant de violentes "
                "douleurs.",
                width=56,
            ),
            font_size=26,
            color=WHITE,
        )
        histoire.next_to(sous_titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "À Bouaké, Awa, élève en classe de première D, accompagne son "
                "petit frère Koffi à l'hôpital. Koffi est atteint de "
                "drépanocytose : lors des crises, ses globules rouges se "
                "déforment en faucille, bouchent les petits vaisseaux "
                "sanguins et provoquent de violentes douleurs."
            )
        ) as tracker:
            self.play(Write(titre))
            self.play(FadeIn(sous_titre))
            self.play(FadeIn(histoire))
            self.wait(tracker.get_remaining_duration())

        medecin = Text(
            _wrap(
                "Le médecin explique : « Dans le sang de votre frère, "
                "l'hémoglobine est presque normale, mais un seul acide "
                "aminé a changé sur les 146 qui composent une de ses "
                "chaînes. Ce tout petit changement suffit à déformer les "
                "globules rouges. »",
                width=56,
            ),
            font_size=25,
            color=WHITE,
        )
        medecin.next_to(histoire, DOWN, buff=0.35)

        with self.voiceover(
            text=(
                "Le médecin explique à Awa : dans le sang de votre frère, "
                "l'hémoglobine est presque normale, mais un seul acide aminé "
                "a changé sur les cent quarante-six qui composent une de ses "
                "chaînes. Ce tout petit changement suffit à déformer les "
                "globules rouges. Awa est stupéfaite : comment une "
                "information écrite dans le noyau de nos cellules peut-elle "
                "commander la fabrication d'une protéine ?"
            )
        ) as tracker:
            self.play(FadeIn(medecin))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(sous_titre), FadeOut(histoire), FadeOut(medecin))

        # --- Animation du raisonnement : les deux questions guides -------
        entete_questions = Text(
            "Deux questions guideront notre étude :", font_size=28, color=YELLOW, weight="BOLD"
        )
        entete_questions.next_to(titre, DOWN, buff=0.6)

        q1 = Text(
            _wrap("1. Où se trouve, dans la cellule, l'information qui commande la fabrication des protéines ?", width=54),
            font_size=26,
            color=WHITE,
        )
        q2 = Text(
            _wrap(
                "2. Quels sont les deux grands acteurs moléculaires de cette "
                "histoire : celle qui conserve l'information et celle qui "
                "est fabriquée ?",
                width=54,
            ),
            font_size=26,
            color=WHITE,
        )
        questions = VGroup(q1, q2).arrange(DOWN, aligned_edge=LEFT, buff=0.4)
        questions.next_to(entete_questions, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Première question : où se trouve, dans la cellule, "
                "l'information qui commande la fabrication des protéines ?"
            )
        ) as tracker:
            self.play(FadeIn(entete_questions))
            self.play(Write(q1))
            self.wait(tracker.get_remaining_duration())

        with self.voiceover(
            text=(
                "Deuxième question : quels sont les deux grands acteurs "
                "moléculaires de cette histoire, celle qui conserve "
                "l'information et celle qui est fabriquée ?"
            )
        ) as tracker:
            self.play(Write(q2))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(entete_questions), FadeOut(questions))

        # --- Exemple traité : le plan de l'étude --------------------------
        entete_plan = Text("Le plan de notre étude", font_size=28, color=YELLOW, weight="BOLD")
        entete_plan.next_to(titre, DOWN, buff=0.55)

        plan = _bullets(
            [
                "Chaque protéine est commandée par un gène.",
                "Le message du gène est écrit dans un code que toute la "
                "cellule sait lire : le code génétique.",
                "La transcription recopie le message du gène en ARNm.",
                "La traduction utilise l'ARNm pour assembler les acides "
                "aminés et fabriquer la protéine.",
                "Une erreur dans le message, une mutation, peut modifier "
                "la protéine : exemple de la drépanocytose.",
            ],
            font_size=23,
            width=54,
        )
        plan.next_to(entete_plan, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Voici le plan de notre étude. Nous verrons d'abord que "
                "chaque protéine est commandée par un gène, puis que le "
                "message du gène est écrit dans un code que toute la "
                "cellule sait lire, le code génétique. Nous étudierons "
                "ensuite les deux grandes étapes de la fabrication d'une "
                "protéine : la transcription, qui recopie le message, et la "
                "traduction, qui l'utilise pour assembler les acides aminés. "
                "Enfin, nous comprendrons comment une erreur dans le "
                "message, appelée mutation, peut modifier une protéine, avec "
                "l'exemple de la drépanocytose, maladie fréquente en Côte "
                "d'Ivoire et en Afrique de l'Ouest."
            )
        ) as tracker:
            self.play(FadeIn(entete_plan))
            self.play(FadeIn(plan))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(entete_plan), FadeOut(plan))

        # --- À retenir : prérequis à réviser -------------------------------
        prerequis = essentiel_box(
            Text(
                _wrap(
                    "Prérequis à réviser : la cellule (noyau, cytoplasme, "
                    "ribosomes) ; les chromosomes, support de l'information "
                    "génétique ; la structure de l'ADN (double hélice, "
                    "bases A, T, G, C, complémentarité A-T et G-C) ; les "
                    "protéines, chaînes d'acides aminés aux rôles divers ; "
                    "la notion d'enzyme, protéine qui catalyse une réaction "
                    "chimique.",
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
                "cellule et ses constituants, noyau, cytoplasme, ribosomes ; "
                "les chromosomes, support de l'information génétique ; la "
                "structure de l'ADN, une double hélice formée de nucléotides "
                "portant quatre bases azotées, A, T, G, C, avec les règles "
                "de complémentarité, A avec T, G avec C ; les protéines, "
                "chaînes d'acides aminés aux rôles très divers ; et la "
                "notion d'enzyme, une protéine qui catalyse, c'est-à-dire "
                "accélère, une réaction chimique de la cellule."
            )
        ) as tracker:
            self.play(FadeIn(prerequis))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(prerequis))

        # --- Piège à éviter : ne pas réduire le chapitre à du vocabulaire --
        piege = warning_box(
            Text(
                _wrap(
                    "Ce chapitre ne se résume pas à une liste de mots à "
                    "mémoriser (codon, ARNm, ribosome...). L'essentiel est "
                    "de comprendre la chaîne du raisonnement : gène -> ARNm "
                    "-> protéine -> caractère observable, et comment une "
                    "seule lettre changée peut la perturber.",
                    width=56,
                ),
                font_size=24,
            ),
            box_width=11.8,
        )
        piege.next_to(titre, DOWN, buff=0.6)

        with self.voiceover(
            text=(
                "Attention à ne pas réduire ce chapitre à une liste de mots "
                "à mémoriser, comme codon, ARN messager ou ribosome. "
                "L'essentiel est de comprendre la chaîne du raisonnement : "
                "du gène à l'ARN messager, puis à la protéine, puis au "
                "caractère observable, et de saisir comment une seule "
                "lettre changée dans ce message peut tout perturber."
            )
        ) as tracker:
            self.play(FadeIn(piege))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(titre), FadeOut(piege))
