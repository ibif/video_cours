"""
scenes/SVT_ActivitesInternesGlobe_01.py — Chapitre 6 (1ereD, SVT), scène 01.

Introduction du chapitre « Les activités internes du globe terrestre » :
activité d'introduction (l'énigme du mont Cameroun / Nyiragongo actifs vs
Côte d'Ivoire calme), objectifs du chapitre, prérequis à réviser.
Source : 1ereD/SVT.pdf, page 77.
"""

import textwrap

from manim import DOWN, LEFT, UP, WHITE, YELLOW, FadeIn, FadeOut, Text, VGroup, Write

from shapes.base_scene import NotionScene
from shapes.boxes import essentiel_box, scene_title, warning_box


def _wrap(text: str, width: int = 56) -> str:
    return "\n".join(textwrap.fill(line, width=width) for line in text.split("\n"))


def _bullets(items, font_size=24, color=WHITE, width=54):
    lines = VGroup(
        *[Text(f"• {_wrap(it, width=width)}", font_size=font_size, color=color) for it in items]
    )
    lines.arrange(DOWN, aligned_edge=LEFT, buff=0.22)
    return lines


class IntroductionActivitesInternesGlobe(NotionScene):
    def construct(self):
        # --- Énoncé : mise en situation ----------------------------------
        titre = scene_title("Chapitre 6 — Les activités internes du globe")
        titre.scale(0.68)
        titre.to_edge(UP)

        sous_titre = Text("Une énigme d'Afrique de l'Ouest", font_size=28, color=YELLOW, weight="BOLD")
        sous_titre.next_to(titre, DOWN, buff=0.5)

        histoire = Text(
            _wrap(
                "Au lycée, Aya observe une carte d'Afrique. Le mont Cameroun "
                "(4 095 m) est un volcan actif : éruptions en 1999 puis 2000. "
                "En RD Congo, le Nyiragongo a détruit une partie de Goma en "
                "2002 puis 2021.",
                width=56,
            ),
            font_size=25,
            color=WHITE,
        )
        histoire.next_to(sous_titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Au lycée, Aya observe une carte d'Afrique. Le mont Cameroun, "
                "point culminant d'Afrique de l'Ouest avec ses quatre mille "
                "quatre-vingt-quinze mètres, est un volcan actif : il est "
                "entré en éruption en mille neuf cent quatre-vingt-dix-neuf "
                "puis en deux mille, coulant de la lave sur des bananeraies. "
                "En République Démocratique du Congo, le volcan Nyiragongo a "
                "détruit une partie de la ville de Goma en deux mille deux, "
                "puis à nouveau en deux mille vingt et un."
            )
        ) as tracker:
            self.play(Write(titre))
            self.play(FadeIn(sous_titre))
            self.play(FadeIn(histoire))
            self.wait(tracker.get_remaining_duration())

        question_aya = Text(
            _wrap(
                "Pourtant, en Côte d'Ivoire, aucun volcan n'est entré en "
                "éruption de mémoire d'homme, et les séismes y sont rares et "
                "faibles. D'où viennent les volcans et les séismes ? Que "
                "cache l'intérieur de la Terre ?",
                width=56,
            ),
            font_size=25,
            color=WHITE,
        )
        question_aya.next_to(histoire, DOWN, buff=0.35)

        with self.voiceover(
            text=(
                "Pourtant, en Côte d'Ivoire, aucun volcan n'est entré en "
                "éruption de mémoire d'homme, et les séismes y sont rares et "
                "faibles. Aya se demande alors : d'où viennent les volcans et "
                "les séismes ? Pourquoi certaines régions en comptent-elles "
                "beaucoup et d'autres aucun ? Et surtout, que cache "
                "l'intérieur de la Terre ? Ce chapitre, consacré aux "
                "activités internes du globe terrestre, apporte les réponses."
            )
        ) as tracker:
            self.play(FadeIn(question_aya))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(sous_titre), FadeOut(histoire), FadeOut(question_aya))

        # --- Animation du raisonnement : les questions guides -------------
        entete_questions = Text(
            "Quatre questions guideront notre étude :", font_size=27, color=YELLOW, weight="BOLD"
        )
        entete_questions.next_to(titre, DOWN, buff=0.6)

        q1 = Text("1. Comment se manifestent volcanisme et séismes ?", font_size=24, color=WHITE)
        q2 = Text("2. Comment localiser un séisme et mesurer sa force ?", font_size=24, color=WHITE)
        q3 = Text("3. Que révèlent les ondes sismiques de l'intérieur du globe ?", font_size=24, color=WHITE)
        q4 = Text("4. Pourquoi volcans et séismes ne sont-ils pas partout ?", font_size=24, color=WHITE)
        questions = VGroup(q1, q2, q3, q4).arrange(DOWN, aligned_edge=LEFT, buff=0.32)
        questions.next_to(entete_questions, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Première question : comment se manifestent le volcanisme et "
                "les séismes à la surface de la Terre ?"
            )
        ) as tracker:
            self.play(FadeIn(entete_questions))
            self.play(Write(q1))
            self.wait(tracker.get_remaining_duration())

        with self.voiceover(
            text="Deuxième question : comment localiser un séisme et mesurer sa force ?"
        ) as tracker:
            self.play(Write(q2))
            self.wait(tracker.get_remaining_duration())

        with self.voiceover(
            text="Troisième question : que révèlent les ondes sismiques sur l'intérieur du globe ?"
        ) as tracker:
            self.play(Write(q3))
            self.wait(tracker.get_remaining_duration())

        with self.voiceover(
            text="Quatrième question : pourquoi volcans et séismes ne sont-ils pas répartis partout ?"
        ) as tracker:
            self.play(Write(q4))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(entete_questions), FadeOut(questions))

        # --- Exemple traité : objectifs du chapitre ------------------------
        entete_objectifs = Text("Objectifs du chapitre", font_size=27, color=YELLOW, weight="BOLD")
        entete_objectifs.next_to(titre, DOWN, buff=0.55)

        objectifs = _bullets(
            [
                "Définir le volcanisme et le séisme, décrire leurs manifestations.",
                "Distinguer les deux grands types d'éruptions et leurs produits.",
                "Exploiter les vitesses des ondes sismiques pour calculer une distance épicentrale.",
                "Décrire la structure interne du globe : enveloppes et discontinuités.",
                "Expliquer la répartition mondiale des volcans et séismes par la tectonique des plaques.",
            ],
            font_size=22,
            width=52,
        )
        objectifs.next_to(entete_objectifs, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "À la fin de ce chapitre, l'élève doit être capable de "
                "définir le volcanisme et le séisme, et de décrire leurs "
                "manifestations ; de distinguer les deux grands types "
                "d'éruptions volcaniques ainsi que leurs produits ; "
                "d'exploiter les vitesses des ondes sismiques pour calculer "
                "une distance épicentrale ; de décrire la structure interne "
                "du globe terrestre, ses enveloppes et ses discontinuités ; "
                "et enfin d'expliquer la répartition mondiale des volcans et "
                "des séismes à l'aide de la tectonique des plaques."
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
                    "Prérequis à réviser : la vitesse moyenne v=d/t (physique "
                    "de seconde) ; les éléments chimiques courants et les "
                    "états physiques de la matière ; les notions de "
                    "géographie (continents, océans, chaînes de montagnes, "
                    "fosses) ; la Terre assimilée à une sphère de rayon "
                    "moyen R ≈ 6 371 km.",
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
                "formule de la vitesse moyenne, v égale d sur t, vue en "
                "physique de seconde ; les éléments chimiques courants et "
                "les états physiques de la matière, solide, liquide, gazeux "
                "; quelques notions de géographie, continents, océans, "
                "chaînes de montagnes, fosses océaniques ; et enfin, on "
                "assimilera la Terre à une sphère de rayon moyen environ "
                "six mille trois cent soixante et onze kilomètres."
            )
        ) as tracker:
            self.play(FadeIn(prerequis))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(prerequis))

        # --- Piège à éviter : réduire ce chapitre à une leçon d'anatomie ---
        piege = warning_box(
            Text(
                _wrap(
                    "Ce chapitre ne se limite pas à décrire des volcans et "
                    "des tremblements de terre isolés : il explique, par un "
                    "seul mécanisme global, la tectonique des plaques, "
                    "pourquoi ces phénomènes se concentrent en certains "
                    "endroits du globe et sont absents ailleurs, comme en "
                    "Côte d'Ivoire.",
                    width=56,
                ),
                font_size=24,
            ),
            box_width=11.5,
        )
        piege.next_to(titre, DOWN, buff=0.6)

        with self.voiceover(
            text=(
                "Attention à ne pas réduire ce chapitre à une collection de "
                "volcans et de séismes isolés : l'essentiel est de "
                "comprendre comment un seul mécanisme global, la tectonique "
                "des plaques, explique pourquoi ces phénomènes se "
                "concentrent en certains endroits du globe et sont absents "
                "ailleurs, comme en Côte d'Ivoire."
            )
        ) as tracker:
            self.play(FadeIn(piege))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(titre), FadeOut(piege))
