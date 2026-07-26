"""
scenes/SVT_ReflexeInne_08.py — Chapitre 10 (1ereD, SVT), scène 08.

§ 10.4.1 : le réflexe rotulien en détail — trajet complet de l'influx (6
étapes), inhibition réciproque, réflexe monosynaptique, exemple « pourquoi
monosynaptique ? », piège monosynaptique ≠ une seule cellule.
Source : 1ereD/SVT.pdf, pages 139-140.
"""

import textwrap

from manim import (
    BLUE_D,
    DOWN,
    LEFT,
    RED_D,
    RIGHT,
    UP,
    WHITE,
    YELLOW,
    Dot,
    FadeIn,
    FadeOut,
    Line,
    Text,
    VGroup,
    Write,
)

from shapes.base_scene import NotionScene
from shapes.boxes import example_box, scene_title, warning_box


def _wrap(text: str, width: int = 56) -> str:
    return "\n".join(textwrap.fill(line, width=width) for line in text.split("\n"))


def _bullets(items, font_size=23, color=WHITE, width=52):
    lines = VGroup(
        *[Text(f"• {_wrap(it, width=width)}", font_size=font_size, color=color) for it in items]
    )
    lines.arrange(DOWN, aligned_edge=LEFT, buff=0.24)
    return lines


def _numbered(items, font_size=19, color=WHITE, width=58):
    lines = VGroup(
        *[Text(f"{i+1}. {_wrap(it, width=width)}", font_size=font_size, color=color) for i, it in enumerate(items)]
    )
    lines.arrange(DOWN, aligned_edge=LEFT, buff=0.22)
    return lines


def _schema_monosynaptique():
    """Neurone sensitif → une seule synapse → motoneurone (schéma simplifié)."""
    n_sens = Line(LEFT * 2.6, LEFT * 0.3, color=BLUE_D, stroke_width=5)
    label_sens = Text("neurone sensitif", font_size=15, color=BLUE_D)
    label_sens.next_to(n_sens, UP, buff=0.15)

    synapse = Dot(point=[0, 0, 0], radius=0.1, color=YELLOW)
    label_syn = Text("1 synapse", font_size=14, color=YELLOW, weight="BOLD")
    label_syn.next_to(synapse, DOWN, buff=0.2)

    n_mot = Line(RIGHT * 0.3, RIGHT * 2.6, color=RED_D, stroke_width=5)
    label_mot = Text("motoneurone", font_size=15, color=RED_D)
    label_mot.next_to(n_mot, UP, buff=0.15)

    return VGroup(n_sens, label_sens, synapse, label_syn, n_mot, label_mot)


class LeReflexeRotulien(NotionScene):
    def construct(self):
        titre = scene_title("10.4.1 — Le réflexe rotulien, un réflexe monosynaptique")
        titre.scale(0.48)
        titre.to_edge(UP)

        # --- Énoncé ---------------------------------------------------------
        intro = Text(
            _wrap(
                "Reprenons le réflexe rotulien et décrivons précisément le "
                "trajet de l'influx nerveux, étape par étape.",
                width=54,
            ),
            font_size=24,
            color=WHITE,
        )
        intro.next_to(titre, DOWN, buff=0.55)

        with self.voiceover(
            text=(
                "Reprenons le réflexe rotulien et décrivons précisément le "
                "trajet de l'influx nerveux."
            )
        ) as tracker:
            self.play(Write(titre))
            self.play(FadeIn(intro))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(intro))

        # --- Animation du raisonnement : les six étapes du trajet -----------------
        trajet = _numbered(
            [
                "le coup sur le tendon rotulien étire le quadriceps ;",
                "les fuseaux neuromusculaires du quadriceps sont excités ;",
                "l'influx sensitif remonte par le nerf crural et entre dans la moelle par la racine dorsale ;",
                "dans la substance grise, le neurone sensitif fait synapse directement avec le motoneurone : une seule synapse (réflexe monosynaptique) ;",
                "l'influx moteur redescend, sort par la racine ventrale et rejoint le quadriceps par le nerf crural ;",
                "le quadriceps se contracte : la jambe s'étend vers l'avant.",
            ],
            font_size=18,
            width=60,
        )
        trajet.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Un : le coup sur le tendon rotulien étire le quadriceps. "
                "Deux : les fuseaux neuromusculaires du quadriceps, "
                "récepteurs d'étirement, sont excités. Trois : l'influx "
                "sensitif remonte par la fibre sensitive du nerf crural, "
                "ou nerf fémoral, et pénètre dans la moelle épinière par la "
                "racine dorsale. Quatre : dans la substance grise, le "
                "neurone sensitif fait synapse directement avec le "
                "motoneurone de la corne ventrale ; il n'y a qu'une seule "
                "synapse entre les deux neurones, on dit que le réflexe "
                "myotatique est un réflexe monosynaptique. Cinq : l'influx "
                "moteur redescend par la fibre motrice, quitte la moelle "
                "par la racine ventrale et rejoint le quadriceps par le "
                "nerf crural. Six : le quadriceps se contracte, la jambe "
                "s'étend vers l'avant."
            )
        ) as tracker:
            self.play(FadeIn(trajet))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(trajet))

        # --- Schéma simplifié : une seule synapse ---------------------------------
        schema = _schema_monosynaptique()
        schema.next_to(titre, DOWN, buff=0.9)

        inhibition = Text(
            _wrap(
                "Détail important : le neurone sensitif excite aussi, par "
                "une ramification, un interneurone inhibiteur qui bloque "
                "les motoneurones des ischio-jambiers (antagonistes du "
                "quadriceps) : c'est l'inhibition réciproque, qui permet "
                "un mouvement fluide.",
                width=54,
            ),
            font_size=19,
            color=WHITE,
        )
        inhibition.next_to(schema, DOWN, buff=0.6)

        with self.voiceover(
            text=(
                "Un détail important complète ce circuit : le neurone "
                "sensitif excite aussi, par une ramification, un "
                "interneurone inhibiteur qui bloque les motoneurones des "
                "muscles ischio-jambiers, les muscles de la face arrière de "
                "la cuisse, antagonistes du quadriceps. Ceux-ci se "
                "relâchent pendant que le quadriceps se contracte : c'est "
                "l'inhibition réciproque, qui permet un mouvement fluide. "
                "La réponse est extrêmement rapide : le temps de latence "
                "n'est que de quelques centièmes de seconde, car le "
                "circuit est court et ne comporte qu'une synapse."
            )
        ) as tracker:
            self.play(FadeIn(schema))
            self.play(FadeIn(inhibition))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(schema), FadeOut(inhibition))

        # --- Exemple traité : pourquoi monosynaptique ? -----------------------------
        exemple = example_box(
            Text(
                _wrap(
                    "Comptons les relais de l'influx dans le centre "
                    "nerveux. Entre le fuseau neuromusculaire et le "
                    "quadriceps, l'influx emprunte deux neurones : un "
                    "neurone sensitif et un motoneurone. Ces deux neurones "
                    "se touchent en un seul point de contact dans la corne "
                    "ventrale : une seule synapse. Le réflexe rotulien est "
                    "donc monosynaptique — le seul connu chez l'Homme, ce "
                    "qui explique sa grande rapidité.",
                    width=54,
                ),
                font_size=19,
            ),
            box_width=12.2,
        )
        exemple.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Pourquoi dit-on que le réflexe rotulien est "
                "monosynaptique ? Comptons les relais de l'influx dans le "
                "centre nerveux. Entre le fuseau neuromusculaire et le "
                "quadriceps, l'influx emprunte deux neurones, un neurone "
                "sensitif et un motoneurone. Ces deux neurones se touchent "
                "en un seul point de contact dans la corne ventrale de la "
                "moelle : une seule synapse. Le réflexe rotulien est donc "
                "qualifié de monosynaptique, mono voulant dire un seul. "
                "C'est d'ailleurs le seul réflexe monosynaptique connu chez "
                "l'Homme, ce qui explique sa grande rapidité."
            )
        ) as tracker:
            self.play(FadeIn(exemple))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(exemple))

        # --- À retenir --------------------------------------------------------------
        a_retenir = _bullets(
            [
                "Chaîne : fuseau neuromusculaire → nerf crural (sensitif) → moelle (1 synapse) → nerf crural (moteur) → quadriceps.",
                "Réflexe myotatique = monosynaptique = très court temps de latence.",
                "Inhibition réciproque : les antagonistes se relâchent pendant que l'agoniste se contracte.",
            ],
            font_size=19,
            width=58,
        )
        entete_retenir = Text("À retenir", font_size=26, color=YELLOW, weight="BOLD")
        entete_retenir.next_to(titre, DOWN, buff=0.5)
        a_retenir.next_to(entete_retenir, DOWN, buff=0.35)

        with self.voiceover(
            text=(
                "À retenir : la chaîne complète va du fuseau neuromusculaire "
                "au nerf crural sensitif, puis à la moelle où il n'y a "
                "qu'une synapse, puis au nerf crural moteur, puis au "
                "quadriceps. Le réflexe myotatique est monosynaptique, ce "
                "qui explique son très court temps de latence. Et "
                "l'inhibition réciproque fait que les muscles antagonistes "
                "se relâchent pendant que le muscle agoniste se contracte."
            )
        ) as tracker:
            self.play(FadeIn(entete_retenir))
            self.play(FadeIn(a_retenir))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(entete_retenir), FadeOut(a_retenir))

        # --- Piège à éviter -----------------------------------------------------------
        piege = warning_box(
            Text(
                _wrap(
                    "Monosynaptique ne veut pas dire « une seule cellule "
                    "nerveuse » : le réflexe monosynaptique met en jeu deux "
                    "neurones, un sensitif et un moteur, séparés par une "
                    "seule synapse. Dans un réflexe polysynaptique, il y a "
                    "trois neurones ou plus, car un ou plusieurs "
                    "interneurones sont intercalés, ce qui crée plusieurs "
                    "synapses.",
                    width=54,
                ),
                font_size=19,
            ),
            box_width=12.2,
        )
        piege.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Attention : monosynaptique ne veut pas dire une seule "
                "cellule nerveuse. Le réflexe monosynaptique met en jeu "
                "deux neurones, un sensitif et un moteur, séparés par une "
                "seule synapse. Dans un réflexe polysynaptique, il y a "
                "trois neurones ou plus, car un ou plusieurs interneurones "
                "sont intercalés, ce qui crée plusieurs synapses."
            )
        ) as tracker:
            self.play(FadeIn(piege))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(titre), FadeOut(piege))
