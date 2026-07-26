"""
scenes/SVT_DivisionMeiotique_01.py — Chapitre 2 (1ereD, SVT), scène 01.

Introduction du chapitre « La division méiotique » : activité
d'introduction (la famille de Mamadou et Affoué à Adzopé), les deux
énigmes (stabilité à 46 chromosomes / diversité des enfants), objectifs
du chapitre, prérequis à réviser. Source : 1ereD/SVT.pdf, page 18.
"""

import textwrap

from manim import DOWN, LEFT, UP, WHITE, YELLOW, FadeIn, FadeOut, MathTex, Text, VGroup, Write

from shapes.base_scene import NotionScene
from shapes.boxes import essentiel_box, scene_title, warning_box


def _wrap(text: str, width: int = 58) -> str:
    return "\n".join(textwrap.fill(line, width=width) for line in text.split("\n"))


def _bullets(items, font_size=25, color=WHITE, width=56):
    lines = VGroup(
        *[Text(f"• {_wrap(it, width=width)}", font_size=font_size, color=color) for it in items]
    )
    lines.arrange(DOWN, aligned_edge=LEFT, buff=0.25)
    return lines


class IntroductionDivisionMeiotique(NotionScene):
    def construct(self):
        # --- Énoncé : mise en situation ------------------------------------
        titre = scene_title("Chapitre 2 — La division méiotique")
        titre.scale(0.7)
        titre.to_edge(UP)

        histoire = Text(
            _wrap(
                "À Adzopé, Mamadou et son épouse Affoué ont trois enfants. Ils "
                "se ressemblent un peu, mais aucun n'est identique à un autre "
                "- alors qu'ils ont les mêmes parents. Fait encore plus "
                "étonnant, appris au dispensaire : les cellules de Mamadou, "
                "celles d'Affoué, et celles de chacun des enfants, contiennent "
                "toutes exactement 46 chromosomes.",
                width=56,
            ),
            font_size=25,
            color=WHITE,
        )
        histoire.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "À Adzopé, Mamadou et son épouse Affoué ont trois enfants. Une "
                "remarque amuse toute la famille : les trois enfants se "
                "ressemblent un peu, mais aucun n'est identique à un autre, "
                "alors qu'ils ont les mêmes parents. Autre fait étonnant, appris "
                "au dispensaire du village : les cellules de Mamadou, comme "
                "celles d'Affoué, contiennent quarante-six chromosomes, et les "
                "cellules de chaque enfant en contiennent, elles aussi, "
                "exactement quarante-six."
            )
        ) as tracker:
            self.play(Write(titre))
            self.play(FadeIn(histoire))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(histoire))

        # --- Animation du raisonnement : les deux énigmes -------------------
        entete_enigmes = Text("Deux énigmes à résoudre", font_size=28, color=YELLOW, weight="BOLD")
        entete_enigmes.next_to(titre, DOWN, buff=0.55)

        calcul = MathTex(r"46 + 46 = 92 \;\neq\; 46", font_size=34, color=WHITE)

        enigme1 = Text(
            _wrap(
                "1. Si chaque parent transmettait la totalité de ses 46 "
                "chromosomes, un enfant devrait en recevoir 92. Pourquoi le "
                "nombre reste-t-il stable à 46, génération après génération ?",
                width=54,
            ),
            font_size=23,
            color=WHITE,
        )
        enigme2 = Text(
            _wrap(
                "2. Comment expliquer que trois enfants des mêmes parents "
                "soient pourtant tous différents les uns des autres ?",
                width=54,
            ),
            font_size=23,
            color=WHITE,
        )

        bloc_enigmes = VGroup(calcul, enigme1, enigme2).arrange(DOWN, aligned_edge=LEFT, buff=0.35)
        bloc_enigmes.next_to(entete_enigmes, DOWN, buff=0.45)
        calcul.move_to(calcul.get_center())

        with self.voiceover(
            text=(
                "Deux énigmes se posent alors. Première énigme : si chaque "
                "parent transmettait la totalité de ses quarante-six "
                "chromosomes, un enfant devrait recevoir quarante-six plus "
                "quarante-six, soit quatre-vingt-douze chromosomes. Pourquoi "
                "le nombre de chromosomes reste-t-il stable à quarante-six "
                "d'une génération à l'autre ?"
            )
        ) as tracker:
            self.play(FadeIn(entete_enigmes))
            self.play(Write(calcul))
            self.play(FadeIn(enigme1))
            self.wait(tracker.get_remaining_duration())

        with self.voiceover(
            text=(
                "Deuxième énigme : comment expliquer que trois enfants des "
                "mêmes parents soient tous différents ? Pour résoudre ces deux "
                "énigmes - la constance du nombre de chromosomes et la "
                "diversité des individus - nous étudions dans ce chapitre une "
                "division cellulaire très particulière : la méiose."
            )
        ) as tracker:
            self.play(FadeIn(enigme2))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(entete_enigmes), FadeOut(bloc_enigmes))

        # --- Exemple traité : objectifs du chapitre -------------------------
        entete_objectifs = Text("Objectifs du chapitre", font_size=28, color=YELLOW, weight="BOLD")
        entete_objectifs.next_to(titre, DOWN, buff=0.55)

        objectifs = _bullets(
            [
                "Définir la méiose et situer son rôle dans la reproduction sexuée.",
                "Décrire, dans l'ordre, les étapes des deux divisions de la méiose.",
                "Déterminer la formule chromosomique, le nombre de chromosomes et "
                "de chromatides à chaque étape.",
                "Expliquer les deux mécanismes du brassage génétique.",
                "Comparer la méiose et la mitose.",
                "Expliquer comment l'alternance méiose-fécondation assure la "
                "constance du nombre de chromosomes de l'espèce.",
            ],
            font_size=21,
            width=54,
        )
        objectifs.next_to(entete_objectifs, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "À l'issue de ce chapitre, l'élève doit être capable de définir "
                "la méiose et de situer son rôle dans la reproduction sexuée ; "
                "de décrire, dans l'ordre, les étapes des deux divisions "
                "successives de la méiose ; de déterminer la formule "
                "chromosomique, le nombre de chromosomes et le nombre de "
                "chromatides d'une cellule à chaque étape ; d'expliquer les "
                "deux mécanismes du brassage génétique ; de comparer la méiose "
                "et la mitose ; et enfin d'expliquer comment l'alternance "
                "méiose-fécondation assure la constance du nombre de "
                "chromosomes d'une espèce, tout en produisant des individus "
                "tous différents."
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
                    "Prérequis à réviser : la cellule (membrane, cytoplasme, "
                    "noyau) ; le chromosome, bâtonnet du noyau qui porte "
                    "l'information génétique ; l'ADN, molécule qui porte les "
                    "gènes et que la cellule peut répliquer avant une "
                    "division ; la mitose, division qui donne deux cellules "
                    "filles identiques à la cellule mère ; le vocabulaire de "
                    "base : gamète, fécondation, espèce.",
                    width=56,
                ),
                font_size=23,
            ),
            box_width=12.2,
        )
        prerequis.next_to(titre, DOWN, buff=0.55)

        with self.voiceover(
            text=(
                "Avant de commencer, quelques prérequis sont à réviser : la "
                "notion de cellule, avec sa membrane, son cytoplasme et son "
                "noyau ; la notion de chromosome, ce bâtonnet situé dans le "
                "noyau et support de l'information génétique ; la notion "
                "d'ADN, la molécule qui porte les gènes, et qu'une cellule "
                "peut répliquer, c'est-à-dire recopier, avant une division ; "
                "la notion de mitose, cette division qui donne deux cellules "
                "filles identiques à la cellule mère ; et enfin le vocabulaire "
                "de base : gamète, fécondation, espèce."
            )
        ) as tracker:
            self.play(FadeIn(prerequis))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(prerequis))

        # --- Piège à éviter ---------------------------------------------------
        piege = warning_box(
            Text(
                _wrap(
                    "Ne conclus pas trop vite que les 46 chromosomes de tes "
                    "cellules sont remis en cause : ce chapitre va montrer "
                    "qu'une division très particulière, la méiose, réduit de "
                    "moitié le nombre de chromosomes dans les gamètes, "
                    "justement pour que le total revienne à 46 après la "
                    "fécondation.",
                    width=56,
                ),
                font_size=24,
            ),
            box_width=12.0,
        )
        piege.next_to(titre, DOWN, buff=0.55)

        with self.voiceover(
            text=(
                "Attention à ne pas conclure trop vite que les quarante-six "
                "chromosomes de tes cellules sont remis en cause : ce chapitre "
                "va au contraire montrer qu'une division très particulière, la "
                "méiose, réduit de moitié le nombre de chromosomes dans les "
                "gamètes, précisément pour que le total revienne à quarante-six "
                "après la fécondation."
            )
        ) as tracker:
            self.play(FadeIn(piege))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(titre), FadeOut(piege))
