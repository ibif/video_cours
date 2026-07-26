"""
scenes/SVT_EvolutionSolsTropicaux_01.py — Chapitre 9 (1ereD, SVT), scène 01.

Introduction du chapitre « L'évolution des sols tropicaux » : activité
d'introduction (Konan à Soubré, Ibrahim à Korhogo), questions guides,
objectifs, prérequis. Source : 1ereD/SVT.pdf, page 116.
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


class IntroductionEvolutionSolsTropicaux(NotionScene):
    def construct(self):
        # --- Énoncé : mise en situation ----------------------------------
        titre = scene_title("Chapitre 9 — L'évolution des sols tropicaux")
        titre.scale(0.65)
        titre.to_edge(UP)

        sous_titre = Text("Mise en situation", font_size=30, color=YELLOW, weight="BOLD")
        sous_titre.next_to(titre, DOWN, buff=0.5)

        histoire = Text(
            _wrap(
                "À Soubré, dans le Sud forestier, monsieur Konan cultive le "
                "manioc et le cacao. Il y a dix ans, sa terre était sombre, "
                "souple, pleine de vers de terre. Aujourd'hui, elle est "
                "rouge vif, dure en saison sèche, et les pluies y creusent "
                "des rigoles : les rendements ont chuté.",
                width=56,
            ),
            font_size=25,
            color=WHITE,
        )
        histoire.next_to(sous_titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "À Soubré, dans le Sud forestier ivoirien, monsieur Konan "
                "cultive le manioc et le cacao. Quand il a défriché sa "
                "parcelle il y a dix ans, la terre était sombre, souple, "
                "pleine de vers de terre : les récoltes étaient excellentes. "
                "Aujourd'hui, la terre est rouge vif, dure en saison sèche, "
                "et les pluies y creusent des rigoles. Les rendements ont "
                "nettement chuté."
            )
        ) as tracker:
            self.play(Write(titre))
            self.play(FadeIn(sous_titre))
            self.play(FadeIn(histoire))
            self.wait(tracker.get_remaining_duration())

        histoire2 = Text(
            _wrap(
                "À Korhogo, son cousin Ibrahim observe autre chose : sur "
                "certaines collines, le sol rouge durcit jusqu'à former "
                "une « dalle de pierre rouge » que la houe ne pénètre "
                "plus.",
                width=56,
            ),
            font_size=25,
            color=WHITE,
        )
        histoire2.next_to(histoire, DOWN, buff=0.35)

        with self.voiceover(
            text=(
                "À Korhogo, dans le Nord, son cousin Ibrahim observe autre "
                "chose : sur certaines collines, le sol rouge durcit jusqu'à "
                "former une véritable « dalle de pierre rouge », que la houe "
                "ne pénètre plus."
            )
        ) as tracker:
            self.play(FadeIn(histoire2))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(sous_titre), FadeOut(histoire), FadeOut(histoire2))

        # --- Animation du raisonnement : les questions guides ---------------
        entete_questions = Text(
            "Trois questions guideront notre étude :", font_size=28, color=YELLOW, weight="BOLD"
        )
        entete_questions.next_to(titre, DOWN, buff=0.6)

        q1 = Text("1. D'où vient la terre de nos champs ?", font_size=25, color=WHITE)
        q2 = Text(
            "2. Pourquoi change-t-elle de couleur, de texture et de fertilité ?",
            font_size=25,
            color=WHITE,
        )
        q3 = Text(
            "3. Que peuvent faire Konan et Ibrahim pour préserver leur outil de travail ?",
            font_size=25,
            color=WHITE,
        )
        questions = VGroup(q1, q2, q3).arrange(DOWN, aligned_edge=LEFT, buff=0.35)
        questions.next_to(entete_questions, DOWN, buff=0.5)

        with self.voiceover(
            text="Première question : d'où vient donc la terre de nos champs ?"
        ) as tracker:
            self.play(FadeIn(entete_questions))
            self.play(Write(q1))
            self.wait(tracker.get_remaining_duration())

        with self.voiceover(
            text=(
                "Deuxième question : pourquoi change-t-elle de couleur, de "
                "texture et de fertilité au fil des années ?"
            )
        ) as tracker:
            self.play(Write(q2))
            self.wait(tracker.get_remaining_duration())

        with self.voiceover(
            text=(
                "Troisième question : que peuvent faire Konan et Ibrahim "
                "pour préserver leur outil de travail, ce sol dont ils "
                "dépendent ?"
            )
        ) as tracker:
            self.play(Write(q3))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(entete_questions), FadeOut(questions))

        # --- Exemple traité : objectifs du chapitre -------------------------
        entete_objectifs = Text("Objectifs du chapitre", font_size=28, color=YELLOW, weight="BOLD")
        entete_objectifs.next_to(titre, DOWN, buff=0.55)

        objectifs = _bullets(
            [
                "Définir le sol et décrire sa composition (minéraux, matière organique, eau, air, êtres vivants).",
                "Décrire le profil d'un sol tropical : nommer et ordonner ses horizons.",
                "Expliquer la formation du sol par altération physique, chimique et biologique de la roche mère.",
                "Identifier les processus d'évolution des sols tropicaux : lessivage, ferralitisation, hydromorphie.",
                "Distinguer les principaux types de sols tropicaux et les relier aux régions de Côte d'Ivoire.",
                "Analyser les causes de dégradation des sols et proposer des mesures de conservation.",
            ],
            font_size=21,
            width=56,
        )
        objectifs.next_to(entete_objectifs, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "À la fin de ce chapitre, l'élève doit être capable de "
                "définir le sol et de décrire sa composition en éléments "
                "minéraux, matière organique, eau, air et êtres vivants ; de "
                "décrire le profil d'un sol tropical en nommant et en "
                "ordonnant ses horizons ; d'expliquer comment le sol se "
                "forme par altération physique, chimique et biologique de la "
                "roche mère ; d'identifier les processus qui font évoluer "
                "les sols sous les climats tropicaux, lessivage, "
                "ferralitisation et hydromorphie ; de distinguer les "
                "principaux types de sols tropicaux et de les relier aux "
                "grandes régions de Côte d'Ivoire ; et enfin d'analyser les "
                "causes de la dégradation des sols et de proposer des "
                "mesures de conservation adaptées."
            )
        ) as tracker:
            self.play(FadeIn(entete_objectifs))
            self.play(FadeIn(objectifs))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(entete_objectifs), FadeOut(objectifs))

        # --- À retenir : prérequis à réviser --------------------------------
        prerequis = essentiel_box(
            Text(
                _wrap(
                    "Prérequis à réviser : roches et minéraux usuels "
                    "(granite, basalte, calcaire, quartz, feldspath, "
                    "argiles) ; le cycle de l'eau ; réactions chimiques "
                    "simples (dissolution, oxydation) ; les zones "
                    "climatiques ivoiriennes (Sud forestier humide, "
                    "savanes du Centre et du Nord plus sèches) ; le rôle "
                    "des végétaux et des microorganismes dans la "
                    "décomposition.",
                    width=56,
                ),
                font_size=23,
            ),
            box_width=12.0,
        )
        prerequis.next_to(titre, DOWN, buff=0.6)

        with self.voiceover(
            text=(
                "Avant de commencer, quelques prérequis sont à réviser : les "
                "roches et minéraux usuels, granite, basalte, calcaire, "
                "quartz, feldspath, argiles ; le cycle de l'eau ; des "
                "réactions chimiques simples comme la dissolution et "
                "l'oxydation ; les zones climatiques ivoiriennes, un Sud "
                "forestier humide et des savanes du Centre et du Nord plus "
                "sèches ; et le rôle des végétaux et des microorganismes "
                "dans la décomposition de la matière organique."
            )
        ) as tracker:
            self.play(FadeIn(prerequis))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(prerequis))

        # --- Piège à éviter --------------------------------------------------
        piege = warning_box(
            Text(
                _wrap(
                    "Ce chapitre ne se limite pas à la couleur de la terre : "
                    "il explique, par des processus physiques, chimiques et "
                    "biologiques précis, pourquoi un sol change et comment "
                    "on peut agir pour le préserver.",
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
                "observation de la couleur de la terre : l'essentiel est de "
                "comprendre, par des processus physiques, chimiques et "
                "biologiques précis, pourquoi un sol évolue, et comment on "
                "peut agir concrètement pour le préserver."
            )
        ) as tracker:
            self.play(FadeIn(piege))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(titre), FadeOut(piege))
