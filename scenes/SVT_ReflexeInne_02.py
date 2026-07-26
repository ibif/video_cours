"""
scenes/SVT_ReflexeInne_02.py — Chapitre 10 (1ereD, SVT), scène 02.

§ 10.1.1-10.1.2 : les deux expériences de mise en évidence du réflexe
(réflexe rotulien, retrait de la main), définition du réflexe, vocabulaire
(stimulus, récepteur, effecteur, influx nerveux).
Source : 1ereD/SVT.pdf, pages 132-133.
"""

import textwrap

from manim import DOWN, LEFT, UP, WHITE, YELLOW, FadeIn, FadeOut, Text, VGroup, Write

from shapes.base_scene import NotionScene
from shapes.boxes import definition_box, scene_title, warning_box


def _wrap(text: str, width: int = 56) -> str:
    return "\n".join(textwrap.fill(line, width=width) for line in text.split("\n"))


def _bullets(items, font_size=23, color=WHITE, width=52):
    lines = VGroup(
        *[Text(f"• {_wrap(it, width=width)}", font_size=font_size, color=color) for it in items]
    )
    lines.arrange(DOWN, aligned_edge=LEFT, buff=0.24)
    return lines


class MiseEnEvidenceDuReflexe(NotionScene):
    def construct(self):
        titre = scene_title("10.1 — Mise en évidence du réflexe")
        titre.scale(0.6)
        titre.to_edge(UP)

        # --- Énoncé : expérience 1, le réflexe rotulien ----------------------
        exp1_titre = Text("Expérience 1 : le réflexe rotulien", font_size=26, color=YELLOW, weight="BOLD")
        exp1_titre.next_to(titre, DOWN, buff=0.5)

        exp1_protocole = _bullets(
            [
                "Protocole : élève assis, jambes pendantes, muscles de la cuisse relâchés. On frappe doucement le tendon rotulien.",
                "Observation : la jambe s'étend brusquement ; l'élève ne peut pas retenir le mouvement ; même coup → même réponse.",
                "Interprétation : l'étirement bref du quadriceps déclenche sa contraction, qui soulève la jambe.",
            ],
            font_size=20,
            width=56,
        )
        exp1_protocole.next_to(exp1_titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Expérience 1, le réflexe rotulien. Protocole : un élève "
                "est assis sur une table, les jambes pendant librement "
                "dans le vide, les muscles de la cuisse complètement "
                "relâchés. L'expérimentateur frappe doucement le tendon "
                "situé juste sous la rotule, le tendon rotulien. "
                "Observation : immédiatement après le coup, la jambe "
                "s'étend brusquement vers l'avant. L'élève n'a pas décidé "
                "ce mouvement, et s'il essaie de le retenir, il n'y "
                "parvient pas complètement. Si l'on renouvelle le coup "
                "dans les mêmes conditions, on obtient exactement le même "
                "mouvement. Interprétation : le coup sur le tendon "
                "provoque un étirement bref du quadriceps, le muscle situé "
                "à la face avant de la cuisse ; ce muscle répond en se "
                "contractant, ce qui soulève la jambe."
            )
        ) as tracker:
            self.play(Write(titre))
            self.play(FadeIn(exp1_titre))
            self.play(FadeIn(exp1_protocole))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(exp1_titre), FadeOut(exp1_protocole))

        # --- Animation du raisonnement : expérience 2, le retrait ------------
        exp2_titre = Text("Expérience 2 : le retrait de la main", font_size=26, color=YELLOW, weight="BOLD")
        exp2_titre.next_to(titre, DOWN, buff=0.5)

        exp2_protocole = _bullets(
            [
                "Protocole : sans prévenir, on approche une source de chaleur de la paume de la main.",
                "Observation : la main se retire immédiatement, avant même que la douleur soit ressentie.",
                "Interprétation : la peau excitée provoque la contraction des muscles fléchisseurs du bras, qui replient le membre.",
            ],
            font_size=20,
            width=56,
        )
        exp2_protocole.next_to(exp2_titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Expérience 2, le retrait de la main. Protocole : sans "
                "prévenir, on approche une source de chaleur, ou une "
                "pointe fine, de la paume de la main d'un camarade. "
                "Observation : la main se retire immédiatement, avant même "
                "que la personne ne ressente la douleur. Interprétation : "
                "la peau de la main a été excitée, les muscles fléchisseurs "
                "du bras se sont contractés et le membre s'est replié, "
                "mettant la main à l'abri."
            )
        ) as tracker:
            self.play(FadeIn(exp2_titre))
            self.play(FadeIn(exp2_protocole))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(exp2_titre), FadeOut(exp2_protocole))

        conclusion = Text(
            _wrap(
                "Dans les deux cas, la réponse est rapide, involontaire et "
                "toujours la même pour la même stimulation : ce sont des "
                "réflexes.",
                width=54,
            ),
            font_size=25,
            color=WHITE,
        )
        conclusion.next_to(titre, DOWN, buff=0.7)

        with self.voiceover(
            text=(
                "Dans les deux cas, la réponse est rapide, involontaire et "
                "toujours la même pour la même stimulation : ce sont des "
                "réflexes."
            )
        ) as tracker:
            self.play(FadeIn(conclusion))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(conclusion))

        # --- Exemple traité : la définition du réflexe -----------------------
        definition = definition_box(
            Text(
                _wrap(
                    "Un réflexe est une réponse motrice rapide, involontaire "
                    "et stéréotypée d'un organe effecteur (muscle ou "
                    "glande), déclenchée par la stimulation d'un récepteur "
                    "et réalisée grâce à un circuit nerveux précis appelé "
                    "arc réflexe.",
                    width=54,
                ),
                font_size=22,
            ),
            box_width=12.0,
        )
        definition.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Un réflexe est une réponse motrice rapide, involontaire et "
                "stéréotypée d'un organe effecteur, muscle ou glande, "
                "déclenchée par la stimulation d'un récepteur et réalisée "
                "grâce à un circuit nerveux précis appelé arc réflexe."
            )
        ) as tracker:
            self.play(FadeIn(definition))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(definition))

        # --- À retenir : vocabulaire ------------------------------------------
        entete_vocab = Text("Vocabulaire", font_size=27, color=YELLOW, weight="BOLD")
        entete_vocab.next_to(titre, DOWN, buff=0.5)

        vocab = _bullets(
            [
                "Stimulus : agent excitateur (coup, chaleur, lumière, étirement…) qui provoque la stimulation du récepteur.",
                "Récepteur : structure qui reçoit la stimulation (récepteurs de la peau, fuseau neuromusculaire du muscle…).",
                "Effecteur : organe qui produit la réponse (muscle qui se contracte, glande qui sécrète).",
                "Influx nerveux : message électrique qui circule le long des fibres nerveuses, du récepteur vers le centre nerveux, puis du centre vers l'effecteur.",
            ],
            font_size=20,
            width=56,
        )
        vocab.next_to(entete_vocab, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Quelques mots de vocabulaire à retenir. Le stimulus est "
                "l'agent excitateur : coup, chaleur, lumière, étirement ; "
                "il provoque la stimulation du récepteur. Le récepteur est "
                "la structure qui reçoit la stimulation, par exemple les "
                "récepteurs de la peau ou le fuseau neuromusculaire du "
                "muscle. L'effecteur est l'organe qui produit la réponse, "
                "un muscle qui se contracte ou une glande qui sécrète. "
                "Enfin, l'influx nerveux est le message de nature "
                "électrique qui circule le long des fibres nerveuses, du "
                "récepteur vers le centre nerveux, puis du centre nerveux "
                "vers l'effecteur."
            )
        ) as tracker:
            self.play(FadeIn(entete_vocab))
            self.play(FadeIn(vocab))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(entete_vocab), FadeOut(vocab))

        # --- Piège à éviter : stimulus ≠ récepteur ----------------------------
        piege = warning_box(
            Text(
                _wrap(
                    "Ne pas confondre stimulus et récepteur : le stimulus "
                    "est l'agent extérieur qui excite (le coup de marteau, "
                    "la chaleur de la marmite) ; le récepteur est la "
                    "structure biologique qui perçoit ce stimulus (le "
                    "fuseau neuromusculaire, les récepteurs de la peau). "
                    "Sans récepteur fonctionnel, le stimulus le plus fort "
                    "ne déclenche aucun réflexe.",
                    width=54,
                ),
                font_size=20,
            ),
            box_width=12.0,
        )
        piege.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Attention à ne pas confondre stimulus et récepteur. Le "
                "stimulus est l'agent extérieur qui excite, le coup de "
                "marteau, la chaleur de la marmite ; le récepteur est la "
                "structure biologique qui perçoit ce stimulus, le fuseau "
                "neuromusculaire, les récepteurs de la peau. Sans récepteur "
                "fonctionnel, le stimulus le plus fort ne déclenche aucun "
                "réflexe."
            )
        ) as tracker:
            self.play(FadeIn(piege))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(titre), FadeOut(piege))
