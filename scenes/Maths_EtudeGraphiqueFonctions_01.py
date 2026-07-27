"""
scenes/Maths_EtudeGraphiqueFonctions_01.py — Chapitre 11 (1ereC, Maths), scène 01.

Le plan complet d'étude d'une fonction : les sept étapes ordonnées à
respecter systématiquement (ensemble de définition, parité/périodicité,
limites aux bornes, asymptotes, dérivée et signe, tableau de variation,
points remarquables et tracé).
Source : 1ereC/Maths.pdf, chapitre 11, pages 130-141.
"""

import textwrap

from manim import DOWN, UP, FadeIn, FadeOut, MathTex, Text, VGroup, Write, YELLOW

from shapes.base_scene import NotionScene
from shapes.boxes import essentiel_box, method_box, scene_title, warning_box


def _wrap(text: str, width: int = 58) -> str:
    return "\n".join(textwrap.fill(line, width=width) for line in text.split("\n"))


class PlanEtudeFonction(NotionScene):
    def construct(self):
        titre = scene_title("Le plan complet d'étude d'une fonction")
        titre.scale(0.5)
        titre.to_edge(UP)

        # --- Énoncé ----------------------------------------------------------
        enonce = Text(
            "Comment étudier une fonction sans rien oublier ?",
            font_size=27,
            color=YELLOW,
            weight="BOLD",
        )
        enonce.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Étudier une fonction et tracer sa courbe demande de suivre "
                "une démarche complète, toujours dans le même ordre. Voici "
                "le plan en sept étapes qu'il faut désormais appliquer "
                "systématiquement, chapitre après chapitre."
            )
        ) as tracker:
            self.play(Write(titre))
            self.play(FadeIn(enonce))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(enonce))

        # --- Animation du raisonnement : les 7 étapes -------------------------
        etapes = method_box(
            MathTex(
                r"""
                \begin{array}{ll}
                1. & \text{Ensemble de définition } D_f \\
                2. & \text{Parité, périodicité — réduction du domaine d'étude} \\
                3. & \text{Limites aux bornes de } D_f \\
                4. & \text{Asymptotes (verticale, horizontale, oblique)} \\
                5. & \text{Dérivée } f' \text{ et étude de son signe} \\
                6. & \text{Tableau de variation} \\
                7. & \text{Points remarquables et tracé de la courbe}
                \end{array}
                """,
                font_size=25,
            ),
            box_width=10.8,
        )
        etapes.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Première étape : déterminer l'ensemble de définition D "
                "indice f. Deuxième étape : étudier la parité et la "
                "périodicité éventuelles, pour réduire le domaine d'étude. "
                "Troisième étape : calculer les limites aux bornes de ce "
                "domaine. Quatrième étape : en déduire les asymptotes "
                "éventuelles — verticale, horizontale ou oblique. Cinquième "
                "étape : calculer la dérivée f prime et étudier son signe. "
                "Sixième étape : dresser le tableau de variation complet. "
                "Septième et dernière étape : placer les points "
                "remarquables et tracer la courbe."
            )
        ) as tracker:
            self.play(FadeIn(etapes))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(etapes))

        # --- Exemple : pourquoi l'ordre compte --------------------------------
        exemple_ordre = method_box(
            Text(
                _wrap(
                    "Exemple concret : sans l'étape 2 (parité), on étudie "
                    "deux fois le même travail pour une fonction paire. "
                    "Sans l'étape 4 (asymptotes), le tracé de l'étape 7 est "
                    "faux même si le tableau de variation est correct.",
                    width=58,
                ),
                font_size=23,
            ),
            box_width=11.0,
        )
        exemple_ordre.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Pourquoi respecter cet ordre précis ? Prenons un exemple "
                "concret : si on saute l'étape deux, la parité, on risque "
                "de refaire deux fois le même travail pour une fonction "
                "paire, alors qu'une seule moitié suffisait. Et si on saute "
                "l'étape quatre, les asymptotes, le tracé final sera faux "
                "même si le tableau de variation, lui, est parfaitement "
                "correct : la courbe s'écraserait sur une droite qu'on "
                "n'aurait pas identifiée."
            )
        ) as tracker:
            self.play(FadeIn(exemple_ordre))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(exemple_ordre))

        # --- À retenir ---------------------------------------------------------
        retenir = essentiel_box(
            Text(
                _wrap(
                    "Toujours suivre les 7 étapes dans l'ordre : Df → "
                    "parité/périodicité → limites → asymptotes → dérivée et "
                    "signe → tableau de variation → points remarquables et "
                    "tracé. Ce plan s'applique à TOUTE fonction du programme.",
                    width=58,
                ),
                font_size=23,
            ),
            box_width=11.4,
        )
        retenir.next_to(titre, DOWN, buff=0.6)

        with self.voiceover(
            text=(
                "À retenir : ce plan en sept étapes — domaine, parité, "
                "limites, asymptotes, dérivée, tableau de variation, points "
                "remarquables — s'applique à toute fonction du programme, "
                "qu'elle soit polynôme, homographique, rationnelle, "
                "irrationnelle ou trigonométrique. C'est la même démarche "
                "qu'on va maintenant décliner sur chaque famille de "
                "fonctions."
            )
        ) as tracker:
            self.play(FadeIn(retenir))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(retenir))

        # --- Piège à éviter ------------------------------------------------
        piege = warning_box(
            Text(
                _wrap(
                    "Piège au bac ivoirien : chaque étape oubliée ou "
                    "inversée coûte des points, même si le résultat final "
                    "semble correct. Rédiger les sept étapes dans l'ordre, "
                    "sans en sauter aucune, même quand la réponse paraît "
                    "évidente.",
                    width=58,
                ),
                font_size=23,
            ),
            box_width=11.2,
        )
        piege.next_to(titre, DOWN, buff=0.6)

        with self.voiceover(
            text=(
                "Attention, piège fréquent au bac ivoirien : chaque étape "
                "oubliée ou inversée coûte des points au barème, même si le "
                "résultat final semble correct. Il faut rédiger les sept "
                "étapes dans l'ordre, sans en sauter aucune, même quand la "
                "réponse paraît évidente à l'œil."
            )
        ) as tracker:
            self.play(FadeIn(piege))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(titre), FadeOut(piege))
