"""
scenes/SVT_ReflexeInne_05.py — Chapitre 10 (1ereD, SVT), scène 05.

§ 10.3.1 : l'arc réflexe, les cinq éléments dans l'ordre (récepteur → voie
sensitive → centre → voie motrice → effecteur), schéma de la chaîne,
méthode d'analyse d'un réflexe en cinq étapes.
Source : 1ereD/SVT.pdf, page 136.
"""

import textwrap

from manim import (
    BLUE_D,
    DOWN,
    GREEN_D,
    LEFT,
    ORANGE,
    PURPLE_D,
    RED_D,
    RIGHT,
    UP,
    WHITE,
    YELLOW,
    Arrow,
    FadeIn,
    FadeOut,
    Rectangle,
    Text,
    VGroup,
    Write,
)

from shapes.base_scene import NotionScene
from shapes.boxes import method_box, scene_title, warning_box


def _wrap(text: str, width: int = 56) -> str:
    return "\n".join(textwrap.fill(line, width=width) for line in text.split("\n"))


def _bullets(items, font_size=23, color=WHITE, width=52):
    lines = VGroup(
        *[Text(f"• {_wrap(it, width=width)}", font_size=font_size, color=color) for it in items]
    )
    lines.arrange(DOWN, aligned_edge=LEFT, buff=0.24)
    return lines


def _element_box(label, sub_label, color, box_width=2.15, box_height=1.5):
    """Un des cinq maillons de l'arc réflexe : rectangle coloré + libellé."""
    rect = Rectangle(
        width=box_width,
        height=box_height,
        fill_color=color,
        fill_opacity=0.85,
        stroke_color=WHITE,
        stroke_width=2,
    )
    titre = Text(label, font_size=17, color=WHITE, weight="BOLD")
    titre.set(width=min(titre.width, box_width - 0.2))
    sous = Text(sub_label, font_size=13, color=WHITE)
    sous.set(width=min(sous.width, box_width - 0.2))
    texte = VGroup(titre, sous).arrange(DOWN, buff=0.12)
    texte.move_to(rect.get_center())
    return VGroup(rect, texte)


def _arc_reflexe_schema():
    recepteur = _element_box("Récepteur", "peau/muscle", BLUE_D)
    voie_sens = _element_box("Voie\nsensitive", "afférente", GREEN_D)
    centre = _element_box("Centre\nnerveux", "moelle épinière", ORANGE)
    voie_mot = _element_box("Voie\nmotrice", "efférente", PURPLE_D)
    effecteur = _element_box("Effecteur", "muscle/glande", RED_D)

    elements = VGroup(recepteur, voie_sens, centre, voie_mot, effecteur)
    elements.arrange(RIGHT, buff=0.55)

    fleches = VGroup()
    for gauche, droite in zip(elements[:-1], elements[1:]):
        fleches.add(Arrow(gauche.get_right(), droite.get_left(), buff=0.05, color=YELLOW, stroke_width=3))

    return VGroup(elements, fleches)


class LArcReflexe(NotionScene):
    def construct(self):
        titre = scene_title("10.3 — Le circuit nerveux : l'arc réflexe")
        titre.scale(0.56)
        titre.to_edge(UP)

        # --- Énoncé -----------------------------------------------------------
        intro = Text(
            _wrap(
                "Pour qu'un réflexe se produise, l'information doit "
                "parcourir un circuit nerveux complet, toujours le même, "
                "appelé arc réflexe. Il comprend cinq éléments, parcourus "
                "dans un ordre immuable.",
                width=54,
            ),
            font_size=24,
            color=WHITE,
        )
        intro.next_to(titre, DOWN, buff=0.55)

        with self.voiceover(
            text=(
                "Pour qu'un réflexe se produise, l'information doit "
                "parcourir un circuit nerveux complet, toujours le même, "
                "appelé arc réflexe. Il comprend cinq éléments, parcourus "
                "dans un ordre immuable."
            )
        ) as tracker:
            self.play(Write(titre))
            self.play(FadeIn(intro))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(intro))

        # --- Animation du raisonnement : les cinq éléments, un par un ----------
        schema = _arc_reflexe_schema()
        schema.scale(0.95)
        schema.next_to(titre, DOWN, buff=0.9)
        elements, fleches = schema

        with self.voiceover(
            text=(
                "Premier élément : le récepteur, qui reçoit la stimulation "
                "et la transforme en influx nerveux."
            )
        ) as tracker:
            self.play(FadeIn(elements[0]))
            self.wait(tracker.get_remaining_duration())

        with self.voiceover(
            text=(
                "Deuxième élément : la voie sensitive, ou voie afférente — "
                "une fibre nerveuse sensitive qui conduit l'influx du "
                "récepteur vers le centre nerveux."
            )
        ) as tracker:
            self.play(FadeIn(elements[1]), FadeIn(fleches[0]))
            self.wait(tracker.get_remaining_duration())

        with self.voiceover(
            text=(
                "Troisième élément : le centre nerveux — ici la moelle "
                "épinière — qui reçoit l'influx sensitif et émet en retour "
                "un ordre moteur."
            )
        ) as tracker:
            self.play(FadeIn(elements[2]), FadeIn(fleches[1]))
            self.wait(tracker.get_remaining_duration())

        with self.voiceover(
            text=(
                "Quatrième élément : la voie motrice, ou voie efférente — "
                "une fibre nerveuse motrice qui conduit l'ordre du centre "
                "nerveux vers l'effecteur."
            )
        ) as tracker:
            self.play(FadeIn(elements[3]), FadeIn(fleches[2]))
            self.wait(tracker.get_remaining_duration())

        with self.voiceover(
            text=(
                "Cinquième et dernier élément : l'effecteur, muscle ou "
                "glande, qui exécute la réponse."
            )
        ) as tracker:
            self.play(FadeIn(elements[4]), FadeIn(fleches[3]))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(schema))

        # --- Exemple traité : la chaîne écrite ---------------------------------
        chaine = Text(
            "récepteur → voie sensitive → centre nerveux → voie motrice → effecteur",
            font_size=19,
            color=YELLOW,
            weight="BOLD",
        )
        chaine.set(width=min(chaine.width, 12.0))
        chaine.next_to(titre, DOWN, buff=0.8)

        with self.voiceover(
            text=(
                "On peut résumer l'arc réflexe par une chaîne : récepteur, "
                "puis voie sensitive, puis centre nerveux, puis voie "
                "motrice, puis effecteur."
            )
        ) as tracker:
            self.play(Write(chaine))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(chaine))

        # --- À retenir : méthode d'analyse en cinq étapes ------------------------
        methode = method_box(
            _bullets(
                [
                    "Étape 1 : décrire la stimulation et identifier le récepteur excité.",
                    "Étape 2 : décrire la réponse observable et identifier l'effecteur.",
                    "Étape 3 : en déduire la voie sensitive (quel nerf monte l'information ?).",
                    "Étape 4 : situer le centre nerveux (moelle épinière, à quel niveau ?).",
                    "Étape 5 : en déduire la voie motrice (quel nerf redescend l'ordre ?).",
                ],
                font_size=17,
                width=58,
            ),
            box_width=12.4,
        )
        methode.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Pour décrire complètement un réflexe, on procède toujours "
                "dans le même ordre. Étape 1 : décrire la stimulation et "
                "identifier le récepteur excité. Étape 2 : décrire la "
                "réponse observable et identifier l'effecteur, quel muscle "
                "se contracte. Étape 3 : en déduire la voie sensitive, par "
                "quel nerf l'information monte-t-elle. Étape 4 : situer le "
                "centre nerveux, la moelle épinière, à quel niveau. Étape "
                "5 : en déduire la voie motrice, par quel nerf l'ordre "
                "redescend-il. On conclut en écrivant la chaîne complète."
            )
        ) as tracker:
            self.play(FadeIn(methode))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(methode))

        # --- Piège à éviter : le centre n'est pas forcément le cerveau ---------
        piege = warning_box(
            Text(
                _wrap(
                    "Ne pas croire que l'arc réflexe passe forcément par le "
                    "cerveau : le centre nerveux d'un réflexe des membres "
                    "est la moelle épinière, pas l'encéphale. C'est ce que "
                    "confirmeront les expériences historiques du paragraphe "
                    "suivant.",
                    width=54,
                ),
                font_size=21,
            ),
            box_width=12.0,
        )
        piege.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Attention, ne crois pas que l'arc réflexe passe forcément "
                "par le cerveau : le centre nerveux d'un réflexe des "
                "membres est la moelle épinière, pas l'encéphale. C'est ce "
                "que confirmeront les expériences historiques du paragraphe "
                "suivant."
            )
        ) as tracker:
            self.play(FadeIn(piege))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(titre), FadeOut(piege))
