"""
scenes/SVT_ReflexeInne_10.py — Chapitre 10 (1ereD, SVT), scène 10.

§ 10.5 : le cerveau et les réflexes (informé mais ne commande pas), exemple
complet « pourquoi Aminata sent la brûlure après avoir retiré la main »,
intérêt biologique et médical des réflexes, remarque sur la chaîne/rupture
d'un maillon, puis L'ESSENTIEL DU CHAPITRE.
Source : 1ereD/SVT.pdf, pages 141-142.
"""

import textwrap

from manim import DOWN, LEFT, UP, WHITE, YELLOW, FadeIn, FadeOut, Text, VGroup, Write

from shapes.base_scene import NotionScene
from shapes.boxes import essentiel_box, example_box, scene_title, warning_box


def _wrap(text: str, width: int = 56) -> str:
    return "\n".join(textwrap.fill(line, width=width) for line in text.split("\n"))


def _bullets(items, font_size=23, color=WHITE, width=52):
    lines = VGroup(
        *[Text(f"• {_wrap(it, width=width)}", font_size=font_size, color=color) for it in items]
    )
    lines.arrange(DOWN, aligned_edge=LEFT, buff=0.24)
    return lines


class LeCerveauEtLesReflexes(NotionScene):
    def construct(self):
        titre = scene_title("10.5 — Le cerveau et les réflexes")
        titre.scale(0.58)
        titre.to_edge(UP)

        # --- Énoncé : le cerveau est informé, mais ne commande pas -------------
        intro = Text(
            _wrap(
                "Lors d'un réflexe, le cerveau n'est pas le chef "
                "d'orchestre : la grenouille médullaire réagit sans "
                "cerveau, et Aminata retire sa main avant de ressentir la "
                "douleur.",
                width=54,
            ),
            font_size=23,
            color=WHITE,
        )
        intro.next_to(titre, DOWN, buff=0.55)

        with self.voiceover(
            text=(
                "Lors d'un réflexe, le cerveau n'est pas le chef "
                "d'orchestre : la preuve, la grenouille médullaire réagit "
                "sans cerveau, et Aminata retire sa main avant de ressentir "
                "la douleur."
            )
        ) as tracker:
            self.play(Write(titre))
            self.play(FadeIn(intro))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(intro))

        # --- Animation du raisonnement : le cerveau informé et modulateur --------
        raisonnement = _bullets(
            [
                "Une partie de l'influx sensitif emprunte les voies ascendantes de la substance blanche et parvient au cerveau, qui en prend conscience : c'est la sensation.",
                "Ce trajet vers le cerveau est plus long et traverse davantage de synapses : la douleur est donc ressentie après le mouvement.",
                "Le cerveau peut moduler certains réflexes (les faciliter ou les atténuer) sans les commander.",
            ],
            font_size=20,
            width=56,
        )
        raisonnement.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Cependant, le cerveau n'est pas totalement à l'écart : une "
                "partie de l'influx sensitif emprunte les voies ascendantes "
                "de la substance blanche et parvient au cerveau, qui en "
                "prend conscience, c'est la sensation. Ce trajet vers le "
                "cerveau est plus long et traverse davantage de synapses : "
                "voilà pourquoi la douleur est ressentie après le "
                "mouvement. Le cerveau peut aussi moduler certains "
                "réflexes : il peut les faciliter ou les atténuer "
                "partiellement. Ainsi, pour renforcer un réflexe rotulien "
                "faible, le médecin demande parfois au patient d'entrelacer "
                "les doigts des deux mains et de tirer fort : cette "
                "contraction volontaire facilite la réponse réflexe."
            )
        ) as tracker:
            self.play(FadeIn(raisonnement))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(raisonnement))

        # --- Exemple traité : pourquoi Aminata sent la brûlure après coup --------
        exemple = example_box(
            Text(
                _wrap(
                    "Au contact de la marmite, l'influx sensitif emprunte "
                    "deux trajets. Le premier, court, aboutit à la moelle "
                    "épinière : c'est le circuit du réflexe, qui déclenche "
                    "le retrait en quelques centièmes de seconde. Le "
                    "second, long, monte jusqu'au cerveau, qui élabore "
                    "alors la sensation de douleur. Comme ce second trajet "
                    "est plus long, la conscience de la brûlure arrive "
                    "après le mouvement : le réflexe protège le corps "
                    "avant même que le cerveau soit informé du danger.",
                    width=54,
                ),
                font_size=19,
            ),
            box_width=12.2,
        )
        exemple.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Pourquoi Aminata sent-elle la brûlure après avoir retiré "
                "la main ? Au contact de la marmite, l'influx sensitif "
                "emprunte deux trajets. Le premier trajet, court, aboutit à "
                "la moelle épinière : c'est le circuit du réflexe, qui "
                "déclenche le retrait de la main en quelques centièmes de "
                "seconde. Le second trajet, long, monte par les faisceaux "
                "ascendants de la substance blanche jusqu'au cerveau, qui "
                "élabore alors la sensation de douleur. Comme ce second "
                "trajet est plus long, la conscience de la brûlure arrive "
                "après le mouvement de retrait. Conclusion : le réflexe "
                "protège le corps avant même que le cerveau soit informé du "
                "danger."
            )
        ) as tracker:
            self.play(FadeIn(exemple))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(exemple))

        # --- Intérêt biologique et médical des réflexes ---------------------------
        entete_interet = Text("Intérêt biologique et médical des réflexes", font_size=23, color=YELLOW, weight="BOLD")
        entete_interet.next_to(titre, DOWN, buff=0.5)

        interet = _bullets(
            [
                "Protection : retrait d'un membre menacé, clignement des paupières, toux et éternuement qui dégagent les voies respiratoires.",
                "Maintien de la posture : les réflexes myotatiques entretiennent le tonus des muscles et nous maintiennent debout sans effort conscient.",
                "Diagnostic médical : un réflexe aboli, faible ou exagéré révèle une atteinte du système nerveux et aide à localiser la lésion.",
            ],
            font_size=19,
            width=56,
        )
        interet.next_to(entete_interet, DOWN, buff=0.35)

        with self.voiceover(
            text=(
                "Les réflexes innés rendent de grands services à "
                "l'organisme. La protection : retrait d'un membre menacé, "
                "clignement des paupières, toux et éternuement qui dégagent "
                "les voies respiratoires. Le maintien de la posture : les "
                "réflexes myotatiques entretiennent le tonus des muscles et "
                "nous maintiennent debout sans effort conscient. Et le "
                "diagnostic médical : le médecin teste les réflexes, "
                "rotulien, achilléen, pupillaire, cutané plantaire, car un "
                "réflexe aboli, faible ou exagéré révèle une atteinte du "
                "système nerveux et aide à localiser la lésion."
            )
        ) as tracker:
            self.play(FadeIn(entete_interet))
            self.play(FadeIn(interet))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(entete_interet), FadeOut(interet))

        # --- À retenir / piège : la chaîne et la rupture d'un maillon --------------
        remarque = warning_box(
            Text(
                _wrap(
                    "L'arc réflexe fonctionne comme une chaîne : la rupture "
                    "d'un seul maillon suffit à abolir le réflexe — "
                    "destruction du récepteur, section de la voie "
                    "sensitive, lésion du centre nerveux, section de la "
                    "voie motrice ou destruction de l'effecteur. C'est ce "
                    "principe que le médecin utilise pour localiser une "
                    "lésion nerveuse.",
                    width=54,
                ),
                font_size=19,
            ),
            box_width=12.2,
        )
        remarque.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Remarque importante : l'arc réflexe fonctionne comme une "
                "chaîne, la rupture d'un seul maillon suffit à abolir le "
                "réflexe. Destruction du récepteur, section de la voie "
                "sensitive, lésion du centre nerveux, section de la voie "
                "motrice ou destruction de l'effecteur : dans chaque cas, "
                "la réponse disparaît. C'est ce principe que le médecin "
                "utilise pour localiser une lésion nerveuse."
            )
        ) as tracker:
            self.play(FadeIn(remarque))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(remarque))

        # --- L'essentiel du chapitre ------------------------------------------------
        essentiel = essentiel_box(
            _bullets(
                [
                    "Réflexe = réponse motrice rapide, involontaire, stéréotypée d'un effecteur à la stimulation d'un récepteur, via l'arc réflexe.",
                    "Propriétés : inné, involontaire, rapide, stéréotypé, spécifique, transitoire.",
                    "Arc réflexe : récepteur → voie sensitive → centre nerveux → voie motrice → effecteur.",
                    "Centre des réflexes des membres = moelle épinière (grenouille médullaire) ; le cerveau n'est pas indispensable.",
                    "Moelle : substance grise centrale (cornes dorsales/ventrales) + substance blanche périphérique.",
                    "Racine dorsale = sensitive (ganglion spinal) ; racine ventrale = motrice ; réunion = nerf rachidien mixte.",
                    "Réflexe myotatique (rotulien) : étirement du muscle, monosynaptique.",
                    "Réflexe de retrait : stimulation douloureuse de la peau, polysynaptique (interneurones).",
                    "Inhibition réciproque : le muscle antagoniste se relâche pendant que l'agoniste se contracte.",
                    "Le cerveau est informé (sensation) mais ne commande pas le réflexe ; il peut le moduler.",
                    "Rôles des réflexes : protection, posture, diagnostic médical.",
                ],
                font_size=14,
                width=64,
            ),
            box_width=12.8,
        )
        essentiel.next_to(titre, DOWN, buff=0.3)

        with self.voiceover(
            text=(
                "Résumons l'essentiel du chapitre. Un réflexe est une "
                "réponse motrice rapide, involontaire et stéréotypée d'un "
                "effecteur à la stimulation d'un récepteur, réalisée par "
                "l'arc réflexe. Ses propriétés : inné, involontaire, "
                "rapide, stéréotypé, spécifique, transitoire. L'arc "
                "réflexe comporte cinq éléments dans l'ordre : récepteur, "
                "voie sensitive, centre nerveux, voie motrice, effecteur. "
                "Le centre nerveux des réflexes des membres est la moelle "
                "épinière, l'expérience de la grenouille médullaire le "
                "prouve ; le cerveau n'est pas indispensable au réflexe. "
                "La moelle épinière comprend une substance grise centrale "
                "et une substance blanche périphérique. La racine dorsale "
                "est sensitive, avec le ganglion spinal ; la racine "
                "ventrale est motrice ; leur réunion forme le nerf "
                "rachidien mixte. Le réflexe myotatique, ou rotulien, est "
                "provoqué par l'étirement d'un muscle, il est "
                "monosynaptique. Le réflexe de retrait est provoqué par "
                "une stimulation douloureuse de la peau, il est "
                "polysynaptique. L'inhibition réciproque relâche le muscle "
                "antagoniste pendant que le muscle agoniste se contracte. "
                "Le cerveau est informé du réflexe, la sensation, par les "
                "voies ascendantes, mais ne le commande pas ; il peut "
                "seulement le moduler. Enfin, les réflexes innés protègent "
                "l'organisme, maintiennent la posture et servent au "
                "diagnostic médical."
            )
        ) as tracker:
            self.play(FadeIn(essentiel))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(titre), FadeOut(essentiel))
