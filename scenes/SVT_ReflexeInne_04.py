"""
scenes/SVT_ReflexeInne_04.py — Chapitre 10 (1ereD, SVT), scène 04.

§ 10.2 : le réflexe myotatique (rotulien, achilléen, tonus), le réflexe de
retrait, tableau d'autres réflexes innés, exemple du clignement palpébral,
piège « inné ne signifie pas tout mouvement automatique ».
Source : 1ereD/SVT.pdf, pages 134-136.
"""

import textwrap

from manim import DOWN, LEFT, UP, WHITE, YELLOW, FadeIn, FadeOut, Text, VGroup, Write

from shapes.base_scene import NotionScene
from shapes.boxes import definition_box, example_box, scene_title, warning_box


def _wrap(text: str, width: int = 56) -> str:
    return "\n".join(textwrap.fill(line, width=width) for line in text.split("\n"))


def _bullets(items, font_size=23, color=WHITE, width=52):
    lines = VGroup(
        *[Text(f"• {_wrap(it, width=width)}", font_size=font_size, color=color) for it in items]
    )
    lines.arrange(DOWN, aligned_edge=LEFT, buff=0.24)
    return lines


class ExemplesDeReflexesInnes(NotionScene):
    def construct(self):
        titre = scene_title("10.2 — Quelques exemples de réflexes innés")
        titre.scale(0.56)
        titre.to_edge(UP)

        # --- Énoncé : le réflexe myotatique -----------------------------------
        def_myotatique = definition_box(
            Text(
                _wrap(
                    "Un réflexe myotatique est un réflexe provoqué par "
                    "l'étirement brusque d'un muscle ; la réponse est la "
                    "contraction du muscle étiré. Le récepteur est le "
                    "fuseau neuromusculaire, une structure sensible à "
                    "l'étirement, logée à l'intérieur du muscle.",
                    width=54,
                ),
                font_size=21,
            ),
            box_width=12.0,
        )
        def_myotatique.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Un réflexe myotatique est un réflexe provoqué par "
                "l'étirement brusque d'un muscle ; la réponse est la "
                "contraction du muscle étiré. Le récepteur est le fuseau "
                "neuromusculaire, une petite structure sensible à "
                "l'étirement, logée à l'intérieur du muscle."
            )
        ) as tracker:
            self.play(Write(titre))
            self.play(FadeIn(def_myotatique))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(def_myotatique))

        # --- Animation du raisonnement : rotulien, achilléen, tonus ----------
        entete_myo = Text("Deux réflexes myotatiques", font_size=26, color=YELLOW, weight="BOLD")
        entete_myo.next_to(titre, DOWN, buff=0.5)

        myo_liste = _bullets(
            [
                "Réflexe rotulien : coup sur le tendon rotulien → extension de la jambe (déjà étudié).",
                "Réflexe achilléen : coup sur le tendon d'Achille → étirement du triceps sural → extension du pied.",
                "Rôle discret et permanent : les réflexes myotatiques maintiennent le tonus musculaire et la posture debout.",
            ],
            font_size=20,
            width=56,
        )
        myo_liste.next_to(entete_myo, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Le réflexe rotulien, étudié plus haut, est le réflexe "
                "myotatique le plus connu. Un autre exemple est le réflexe "
                "achilléen : un coup bref sur le tendon d'Achille, "
                "au-dessus du talon, étire le triceps sural, le muscle du "
                "mollet, qui se contracte et provoque l'extension du pied. "
                "Les réflexes myotatiques jouent aussi un rôle permanent et "
                "discret : en maintenant les muscles légèrement contractés, "
                "ils contribuent au tonus musculaire et au maintien de la "
                "posture debout."
            )
        ) as tracker:
            self.play(FadeIn(entete_myo))
            self.play(FadeIn(myo_liste))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(entete_myo), FadeOut(myo_liste))

        # --- Le réflexe de retrait ---------------------------------------------
        def_retrait = definition_box(
            Text(
                _wrap(
                    "Le réflexe de retrait est un réflexe provoqué par une "
                    "stimulation douloureuse ou brutale de la peau (piqûre, "
                    "brûlure, contact coupant) ; la réponse est la flexion "
                    "du membre, qui l'éloigne de l'agression. Récepteurs : "
                    "récepteurs de douleur et de contact de la peau. "
                    "Effecteurs : les muscles fléchisseurs.",
                    width=54,
                ),
                font_size=20,
            ),
            box_width=12.0,
        )
        def_retrait.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Le réflexe de retrait est un réflexe provoqué par une "
                "stimulation douloureuse ou brutale de la peau, piqûre, "
                "brûlure, contact coupant ; la réponse est la flexion du "
                "membre, qui l'éloigne de l'agression. Les récepteurs sont "
                "les récepteurs de douleur et de contact de la peau ; les "
                "effecteurs sont les muscles fléchisseurs. C'est le "
                "réflexe de la marmite chaude de notre activité : son rôle "
                "est de protéger l'organisme en écartant rapidement le "
                "membre du danger."
            )
        ) as tracker:
            self.play(FadeIn(def_retrait))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(def_retrait))

        # --- Exemple traité : le clignement palpébral ---------------------------
        exemple = example_box(
            Text(
                _wrap(
                    "Un grain de poussière touche la cornée de Mariam ; ses "
                    "paupières se ferment aussitôt. Stimulus : le contact "
                    "du grain de poussière. Récepteur : les récepteurs "
                    "tactiles de la cornée. Réponse : la fermeture des "
                    "paupières, donc effecteur = muscle orbiculaire des "
                    "paupières. Mouvement rapide, involontaire, identique à "
                    "chaque fois : c'est un réflexe inné qui protège l'œil.",
                    width=54,
                ),
                font_size=19,
            ),
            box_width=12.2,
        )
        exemple.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Analysons le clignement palpébral. Un grain de poussière "
                "touche la cornée de Mariam ; ses paupières se ferment "
                "aussitôt. Le stimulus est le contact du grain de "
                "poussière. Le récepteur est constitué par les récepteurs "
                "tactiles de la cornée. La réponse est la fermeture des "
                "paupières ; l'effecteur est donc le muscle orbiculaire des "
                "paupières. Le mouvement est rapide, involontaire et "
                "identique à chaque fois : il s'agit bien d'un réflexe "
                "inné, dont le rôle est de protéger l'œil."
            )
        ) as tracker:
            self.play(FadeIn(exemple))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(exemple))

        # --- À retenir : tableau d'autres réflexes innés -------------------------
        entete_tab = Text("D'autres réflexes innés courants", font_size=25, color=YELLOW, weight="BOLD")
        entete_tab.next_to(titre, DOWN, buff=0.5)

        tableau = _bullets(
            [
                "Réflexe pupillaire : lumière vive → contraction de la pupille.",
                "Éternuement : poussière dans le nez → expulsion brutale d'air.",
                "Toux : corps étranger dans la trachée → expulsion d'air.",
                "Succion : contact sur les lèvres du nouveau-né → mouvements de succion.",
            ],
            font_size=19,
            width=56,
        )
        tableau.next_to(entete_tab, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "D'autres réflexes innés sont courants. Le réflexe "
                "pupillaire : une lumière vive provoque la contraction de "
                "la pupille par le muscle de l'iris. L'éternuement : de la "
                "poussière dans le nez déclenche l'expulsion brutale "
                "d'air par les muscles respiratoires. La toux : un corps "
                "étranger dans la trachée déclenche aussi une expulsion "
                "d'air. Et la succion, chez le nouveau-né : un contact sur "
                "les lèvres déclenche des mouvements de succion."
            )
        ) as tracker:
            self.play(FadeIn(entete_tab))
            self.play(FadeIn(tableau))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(entete_tab), FadeOut(tableau))

        # --- Piège : inné ne signifie pas tout mouvement automatique -------------
        piege = warning_box(
            Text(
                _wrap(
                    "Conduire un vélo, taper à la machine, dribbler au "
                    "football deviennent automatiques à force "
                    "d'entraînement, mais ce ne sont pas des réflexes "
                    "innés : ce sont des automatismes acquis, construits "
                    "par l'apprentissage. Le réflexe inné, lui, est présent "
                    "dès la naissance et commun à tous les individus de "
                    "l'espèce.",
                    width=54,
                ),
                font_size=20,
            ),
            box_width=12.0,
        )
        piege.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Attention : inné ne signifie pas tout mouvement rapide et "
                "automatique. Conduire un vélo, taper à la machine, "
                "dribbler au football deviennent automatiques à force "
                "d'entraînement, mais ce ne sont pas des réflexes innés : "
                "ce sont des automatismes acquis, construits par "
                "l'apprentissage, qu'on appellera réflexes conditionnels "
                "dans un autre chapitre. Le réflexe inné, lui, est présent "
                "dès la naissance et commun à tous les individus de "
                "l'espèce."
            )
        ) as tracker:
            self.play(FadeIn(piege))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(titre), FadeOut(piege))
