"""
scenes/SVT_ReflexeInne_03.py — Chapitre 10 (1ereD, SVT), scène 03.

§ 10.1.3 : les propriétés du réflexe inné (inné, involontaire, rapide,
stéréotypé, spécifique, transitoire), exemple de vérification du caractère
stéréotypé, piège réflexe / mouvement volontaire.
Source : 1ereD/SVT.pdf, pages 133-134.
"""

import textwrap

from manim import DOWN, LEFT, UP, WHITE, YELLOW, FadeIn, FadeOut, Text, VGroup, Write

from shapes.base_scene import NotionScene
from shapes.boxes import example_box, property_box, scene_title, warning_box


def _wrap(text: str, width: int = 56) -> str:
    return "\n".join(textwrap.fill(line, width=width) for line in text.split("\n"))


def _bullets(items, font_size=23, color=WHITE, width=52):
    lines = VGroup(
        *[Text(f"• {_wrap(it, width=width)}", font_size=font_size, color=color) for it in items]
    )
    lines.arrange(DOWN, aligned_edge=LEFT, buff=0.24)
    return lines


class ProprietesDuReflexeInne(NotionScene):
    def construct(self):
        titre = scene_title("10.1.3 — Les propriétés du réflexe inné")
        titre.scale(0.58)
        titre.to_edge(UP)

        # --- Énoncé -------------------------------------------------------
        intro = Text(
            _wrap(
                "L'étude des deux expériences précédentes, et de bien "
                "d'autres, permet de dégager six propriétés "
                "caractéristiques du réflexe inné.",
                width=54,
            ),
            font_size=24,
            color=WHITE,
        )
        intro.next_to(titre, DOWN, buff=0.55)

        with self.voiceover(
            text=(
                "L'étude des deux expériences précédentes, et de nombreuses "
                "autres, permet de dégager les propriétés caractéristiques "
                "du réflexe inné."
            )
        ) as tracker:
            self.play(Write(titre))
            self.play(FadeIn(intro))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(intro))

        # --- Animation du raisonnement : les six propriétés -----------------
        proprietes = property_box(
            _bullets(
                [
                    "Inné : présent dès la naissance, sans aucun apprentissage.",
                    "Involontaire (inconscient) : échappe à la volonté, ne peut pas être totalement empêché.",
                    "Rapide : la réponse survient quelques centièmes de seconde après la stimulation.",
                    "Stéréotypé : la même stimulation provoque toujours la même réponse, chez tous les individus.",
                    "Spécifique : à une stimulation précise correspond une réponse précise et adaptée.",
                    "Transitoire : la réponse cesse dès que la stimulation cesse.",
                ],
                font_size=18,
                width=58,
            ),
            box_width=12.4,
        )
        proprietes.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Il est inné : il est présent dès la naissance, sans aucun "
                "apprentissage ; le nouveau-né serre par réflexe le doigt "
                "placé dans sa paume. Il est involontaire, ou inconscient : "
                "il échappe à la volonté et ne peut pas être totalement "
                "empêché. Il est rapide : la réponse survient quelques "
                "centièmes de seconde après la stimulation. Il est "
                "stéréotypé : la même stimulation provoque toujours la "
                "même réponse, chez tous les individus. Il est spécifique : "
                "à une stimulation précise correspond une réponse précise "
                "et adaptée. Et il est transitoire : la réponse cesse dès "
                "que la stimulation cesse."
            )
        ) as tracker:
            self.play(FadeIn(proprietes))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(proprietes))

        # --- Exemple traité : vérification du caractère stéréotypé ----------
        exemple = example_box(
            Text(
                _wrap(
                    "On frappe trois fois de suite le tendon rotulien d'un "
                    "élève, avec la même force et au même endroit : on "
                    "observe trois extensions identiques. Si l'on augmente "
                    "légèrement l'intensité du coup, l'amplitude du "
                    "mouvement augmente, mais sa forme ne change pas : "
                    "c'est toujours une extension, jamais une flexion. Le "
                    "réflexe est donc bien stéréotypé et spécifique.",
                    width=54,
                ),
                font_size=21,
            ),
            box_width=12.0,
        )
        exemple.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Vérifions le caractère stéréotypé. On frappe trois fois de "
                "suite le tendon rotulien d'un élève, avec la même force et "
                "au même endroit. On observe trois extensions identiques de "
                "la jambe : le mouvement a toujours la même forme. Si l'on "
                "augmente légèrement l'intensité du coup, l'amplitude du "
                "mouvement augmente, mais sa forme ne change pas : c'est "
                "toujours une extension, jamais une flexion. Le réflexe est "
                "donc bien stéréotypé et spécifique."
            )
        ) as tracker:
            self.play(FadeIn(exemple))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(exemple))

        # --- À retenir --------------------------------------------------------
        a_retenir = _bullets(
            [
                "Six propriétés à retenir : inné, involontaire, rapide, stéréotypé, spécifique, transitoire.",
                "Elles se vérifient toutes sur le réflexe rotulien comme sur le réflexe de retrait.",
            ],
            font_size=22,
            width=54,
        )
        entete_retenir = Text("À retenir", font_size=27, color=YELLOW, weight="BOLD")
        entete_retenir.next_to(titre, DOWN, buff=0.55)
        a_retenir.next_to(entete_retenir, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "À retenir : six propriétés caractérisent le réflexe inné, "
                "inné, involontaire, rapide, stéréotypé, spécifique et "
                "transitoire. Elles se vérifient toutes aussi bien sur le "
                "réflexe rotulien que sur le réflexe de retrait."
            )
        ) as tracker:
            self.play(FadeIn(entete_retenir))
            self.play(FadeIn(a_retenir))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(entete_retenir), FadeOut(a_retenir))

        # --- Piège : réflexe vs mouvement volontaire ---------------------------
        piege = warning_box(
            Text(
                _wrap(
                    "Attraper un ballon, écrire son nom, pédaler : ce sont "
                    "des mouvements volontaires, décidés par le cerveau, "
                    "appris pendant l'enfance et variables d'une fois à "
                    "l'autre. Retirer la main d'une marmite chaude est un "
                    "réflexe : inné, involontaire et stéréotypé. Un même "
                    "muscle peut participer aux deux types de mouvements ; "
                    "ce qui distingue le réflexe, c'est son déclenchement "
                    "automatique, sans décision préalable.",
                    width=54,
                ),
                font_size=19,
            ),
            box_width=12.2,
        )
        piege.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Ne pas confondre réflexe et mouvement volontaire. "
                "Attraper un ballon, écrire son nom, pédaler : ce sont des "
                "mouvements volontaires, décidés par le cerveau, appris "
                "pendant l'enfance et variables d'une fois à l'autre. "
                "Retirer la main d'une marmite chaude est un réflexe : "
                "inné, involontaire et stéréotypé. Attention, un même "
                "muscle, par exemple le biceps, peut participer aux deux "
                "types de mouvements ; ce qui distingue le réflexe, c'est "
                "son déclenchement automatique, sans décision préalable."
            )
        ) as tracker:
            self.play(FadeIn(piege))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(titre), FadeOut(piege))
