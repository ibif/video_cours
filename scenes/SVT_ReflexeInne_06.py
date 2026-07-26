"""
scenes/SVT_ReflexeInne_06.py — Chapitre 10 (1ereD, SVT), scène 06.

§ 10.3.2 : le centre du réflexe est la moelle épinière — les trois
expériences historiques sur la grenouille médullaire (a, b, c), leurs
conclusions, remarque sur la moelle sectionnée chez l'Homme.
Source : 1ereD/SVT.pdf, pages 136-137.
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


class LeCentreEstLaMoelleEpiniere(NotionScene):
    def construct(self):
        titre = scene_title("10.3.2 — Le centre du réflexe : la moelle épinière")
        titre.scale(0.5)
        titre.to_edge(UP)

        # --- Énoncé -------------------------------------------------------
        intro = Text(
            _wrap(
                "Quel organe joue le rôle de centre nerveux dans les "
                "réflexes des membres ? Trois expériences historiques sur "
                "la grenouille permettent de répondre.",
                width=54,
            ),
            font_size=24,
            color=WHITE,
        )
        intro.next_to(titre, DOWN, buff=0.55)

        with self.voiceover(
            text=(
                "Quel organe joue le rôle de centre nerveux dans les "
                "réflexes des membres ? Les expériences historiques "
                "réalisées sur la grenouille permettent de répondre."
            )
        ) as tracker:
            self.play(Write(titre))
            self.play(FadeIn(intro))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(intro))

        # --- Animation du raisonnement : les trois expériences -----------------
        exp_a_titre = Text("Expérience a — grenouille médullaire", font_size=22, color=YELLOW, weight="BOLD")
        exp_a_titre.next_to(titre, DOWN, buff=0.5)
        exp_a = _bullets(
            [
                "Une grenouille médullaire a l'encéphale détruit, mais la moelle épinière intacte ; elle ne se déplace plus spontanément (le cœur bat toujours, automaticité propre).",
                "On pince la patte arrière : la patte se retire.",
            ],
            font_size=19,
            width=58,
        )
        exp_a.next_to(exp_a_titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Expérience a. On utilise une grenouille médullaire, "
                "c'est-à-dire une grenouille dont l'encéphale, cerveau et "
                "bulbe, a été détruit, mais dont la moelle épinière est "
                "intacte. L'animal ne se déplace plus spontanément ; son "
                "cœur continue de battre car le cœur possède sa propre "
                "automaticité. On pince doucement la patte arrière : la "
                "patte se retire."
            )
        ) as tracker:
            self.play(FadeIn(exp_a_titre))
            self.play(FadeIn(exp_a))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(exp_a_titre), FadeOut(exp_a))

        exp_b_titre = Text("Expérience b — moelle détruite", font_size=22, color=YELLOW, weight="BOLD")
        exp_b_titre.next_to(titre, DOWN, buff=0.5)
        exp_b = _bullets(
            [
                "On détruit maintenant la moelle épinière de la même grenouille (stylet dans le canal vertébral).",
                "La même stimulation de la patte ne provoque plus aucune réponse.",
            ],
            font_size=20,
            width=56,
        )
        exp_b.next_to(exp_b_titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Expérience b. On détruit maintenant la moelle épinière de "
                "la même grenouille à l'aide d'un stylet introduit dans le "
                "canal vertébral. La même stimulation de la patte ne "
                "provoque plus aucune réponse."
            )
        ) as tracker:
            self.play(FadeIn(exp_b_titre))
            self.play(FadeIn(exp_b))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(exp_b_titre), FadeOut(exp_b))

        exp_c_titre = Text("Expérience c — peau retirée", font_size=22, color=YELLOW, weight="BOLD")
        exp_c_titre.next_to(titre, DOWN, buff=0.5)
        exp_c = _bullets(
            [
                "Sur une autre grenouille médullaire, on enlève la peau de la patte (récepteurs supprimés), sans toucher à la moelle.",
                "La stimulation ne provoque plus de réponse, bien que la moelle soit intacte.",
            ],
            font_size=20,
            width=56,
        )
        exp_c.next_to(exp_c_titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Expérience c. Sur une autre grenouille médullaire, on "
                "enlève la peau de la patte, ce qui supprime les "
                "récepteurs, sans toucher à la moelle. La stimulation ne "
                "provoque plus de réponse, bien que la moelle soit intacte."
            )
        ) as tracker:
            self.play(FadeIn(exp_c_titre))
            self.play(FadeIn(exp_c))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(exp_c_titre), FadeOut(exp_c))

        # --- Exemple traité : les conclusions ------------------------------------
        conclusions = property_box(
            _bullets(
                [
                    "La moelle épinière est le centre nerveux de ces réflexes : sans elle, aucun réflexe n'est possible (exp. b).",
                    "Le cerveau n'est pas indispensable au réflexe, puisque la grenouille privée d'encéphale réagit encore (exp. a).",
                    "Le récepteur est tout aussi indispensable : pas de récepteur, pas de réflexe (exp. c).",
                ],
                font_size=18,
                width=58,
            ),
            box_width=12.4,
        )
        conclusions.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Ces trois expériences permettent de conclure. La moelle "
                "épinière est le centre nerveux de ces réflexes : sans "
                "elle, aucun réflexe n'est possible. Le cerveau n'est pas "
                "indispensable au réflexe, puisque la grenouille privée "
                "d'encéphale réagit encore. Enfin, le récepteur est tout "
                "aussi indispensable : pas de récepteur, pas de réflexe."
            )
        ) as tracker:
            self.play(FadeIn(conclusions))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(conclusions))

        # --- À retenir : remarque clinique chez l'Homme ---------------------------
        remarque = example_box(
            Text(
                _wrap(
                    "Chez l'Homme, on ne peut évidemment pas reproduire ces "
                    "expériences, mais l'observation clinique aboutit aux "
                    "mêmes conclusions : un blessé dont la moelle épinière "
                    "est sectionnée à la suite d'un accident conserve les "
                    "réflexes des membres situés sous la lésion, alors "
                    "qu'il a perdu la sensibilité et le mouvement volontaire "
                    "de ces mêmes membres.",
                    width=54,
                ),
                font_size=19,
            ),
            box_width=12.2,
        )
        remarque.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Chez l'Homme, on ne peut évidemment pas reproduire ces "
                "expériences, mais l'observation clinique aboutit aux "
                "mêmes conclusions : un blessé dont la moelle épinière est "
                "sectionnée à la suite d'un accident conserve les réflexes "
                "des membres situés sous la lésion, alors qu'il a perdu la "
                "sensibilité et le mouvement volontaire de ces mêmes "
                "membres."
            )
        ) as tracker:
            self.play(FadeIn(remarque))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(remarque))

        # --- Piège à éviter --------------------------------------------------------
        piege = warning_box(
            Text(
                _wrap(
                    "Ne pas conclure que le cerveau ne sert à rien : "
                    "l'expérience montre seulement qu'il n'est pas "
                    "indispensable au déclenchement du réflexe. Il reste "
                    "informé de ce qui se passe, comme on le verra au "
                    "paragraphe 10.5.",
                    width=54,
                ),
                font_size=21,
            ),
            box_width=12.0,
        )
        piege.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Attention à ne pas conclure que le cerveau ne sert à rien "
                "dans cette histoire : l'expérience montre seulement qu'il "
                "n'est pas indispensable au déclenchement du réflexe. Il "
                "reste informé de ce qui se passe, comme nous le verrons "
                "plus loin dans ce chapitre."
            )
        ) as tracker:
            self.play(FadeIn(piege))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(titre), FadeOut(piege))
