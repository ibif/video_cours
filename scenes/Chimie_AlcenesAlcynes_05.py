"""
scenes/Chimie_AlcenesAlcynes_05.py — Chapitre 3 (1ereC, Chimie), scène 05.

Stéréoisomérie Z/E des alcènes : définition, condition d'existence (chaque
carbone de la double liaison doit porter deux groupes différents), exemple
fondamental du but-2-ène (Z) et (E), avec schéma, et mention cis/trans.
Source : 1ereC/Chimie.pdf, chapitre 3, pages 28-29.
"""

import textwrap

import numpy as np

from manim import (
    DOWN,
    LEFT,
    RIGHT,
    UP,
    WHITE,
    YELLOW,
    BLUE,
    FadeIn,
    FadeOut,
    Dot,
    Line,
    MathTex,
    Text,
    VGroup,
    Write,
    config,
)

from shapes.base_scene import NotionScene
from shapes.boxes import definition_box, example_box, scene_title, warning_box


def _wrap(text: str, width: int = 56) -> str:
    return "\n".join(textwrap.fill(line, width=width) for line in text.split("\n"))


def _fit(mobject, top_y):
    bas_visible = -config.frame_height / 2 + 0.25
    hauteur_dispo = top_y - bas_visible
    if mobject.height > hauteur_dispo:
        mobject.scale(hauteur_dispo / mobject.height, about_point=mobject.get_top())
    return mobject


def _schema_but2ene(cis: bool):
    """Schéma plan du but-2-ène : C=C central, chaque carbone porte un
    groupe CH3 et un H. cis=True -> les deux CH3 du même côté (Z) ;
    cis=False -> de part et d'autre (E)."""
    c_gauche = np.array([-0.5, 0, 0])
    c_droite = np.array([0.5, 0, 0])
    angle = np.pi / 3
    longueur = 0.9

    haut_gauche = c_gauche + longueur * np.array([-np.cos(angle), np.sin(angle), 0])
    bas_gauche = c_gauche + longueur * np.array([-np.cos(angle), -np.sin(angle), 0])
    haut_droite = c_droite + longueur * np.array([np.cos(angle), np.sin(angle), 0])
    bas_droite = c_droite + longueur * np.array([np.cos(angle), -np.sin(angle), 0])

    if cis:
        # les deux CH3 en haut (même côté), les deux H en bas
        pos_ch3_gauche, pos_h_gauche = haut_gauche, bas_gauche
        pos_ch3_droite, pos_h_droite = haut_droite, bas_droite
    else:
        # CH3 de part et d'autre (côtés opposés)
        pos_ch3_gauche, pos_h_gauche = haut_gauche, bas_gauche
        pos_ch3_droite, pos_h_droite = bas_droite, haut_droite

    double_liaison = VGroup(
        Line(c_gauche + UP * 0.05, c_droite + UP * 0.05, color=WHITE, stroke_width=4),
        Line(c_gauche + DOWN * 0.05, c_droite + DOWN * 0.05, color=WHITE, stroke_width=4),
    )
    liaisons = VGroup(
        Line(c_gauche, pos_ch3_gauche, color=WHITE, stroke_width=3),
        Line(c_gauche, pos_h_gauche, color=WHITE, stroke_width=3),
        Line(c_droite, pos_ch3_droite, color=WHITE, stroke_width=3),
        Line(c_droite, pos_h_droite, color=WHITE, stroke_width=3),
    )
    atomes_c = VGroup(Dot(c_gauche, radius=0.07, color=BLUE), Dot(c_droite, radius=0.07, color=BLUE))
    labels = VGroup(
        MathTex("CH_3", font_size=22, color=WHITE).move_to(pos_ch3_gauche),
        MathTex("H", font_size=22, color=WHITE).move_to(pos_h_gauche),
        MathTex("CH_3", font_size=22, color=WHITE).move_to(pos_ch3_droite),
        MathTex("H", font_size=22, color=WHITE).move_to(pos_h_droite),
    )
    return VGroup(double_liaison, liaisons, atomes_c, labels)


class StereoisomerieZE(NotionScene):
    def construct(self):
        titre = scene_title("5. Stéréoisomérie Z / E des alcènes")
        titre.scale(0.55)
        titre.to_edge(UP)

        # --- Énoncé : conséquence de la rigidité de C=C --------------------------
        intro = Text(
            _wrap(
                "Nous avons vu que la double liaison C=C est rigide : "
                "aucune rotation n'est possible autour d'elle. Cette "
                "rigidité peut faire apparaître un nouveau type "
                "d'isomérie, la stéréoisomérie Z/E.",
                width=54,
            ),
            font_size=24,
            color=WHITE,
        )
        intro.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Nous avons vu que la double liaison carbone-carbone est "
                "rigide : aucune rotation n'est possible autour d'elle. "
                "Cette rigidité peut faire apparaître un nouveau type "
                "d'isomérie, appelé stéréoisomérie Z sur E."
            )
        ) as tracker:
            self.play(Write(titre))
            self.play(FadeIn(intro))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(intro))

        # --- Animation du raisonnement : définition + condition d'existence -----
        definition = definition_box(
            VGroup(
                Text(
                    _wrap(
                        "Les isomères Z et E sont deux stéréoisomères qui "
                        "diffèrent par la disposition spatiale des groupes "
                        "autour de la double liaison C=C.",
                        width=46,
                    ),
                    font_size=23,
                ),
                Text(
                    _wrap(
                        "Condition d'existence : chaque carbone de la "
                        "double liaison doit porter deux groupes "
                        "différents.",
                        width=46,
                    ),
                    font_size=23,
                    weight="BOLD",
                ),
            ).arrange(DOWN, buff=0.3),
        )
        definition.next_to(titre, DOWN, buff=0.4)
        _fit(definition, titre.get_bottom()[1] - 0.4)

        with self.voiceover(
            text=(
                "Les isomères Z et E sont deux stéréoisomères qui "
                "diffèrent uniquement par la disposition spatiale de "
                "leurs groupes autour de la double liaison. Mais "
                "attention, cette stéréoisomérie n'existe que sous une "
                "condition précise : chaque carbone de la double liaison "
                "doit porter deux groupes différents. Si un carbone porte "
                "deux fois le même groupe, il n'y a pas de stéréoisomérie "
                "possible."
            )
        ) as tracker:
            self.play(FadeIn(definition))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(definition))

        # --- Exemple traité : but-2-ène (Z) et (E) --------------------------------
        entete = Text("Exemple fondamental : le but-2-ène", font_size=24, color=YELLOW, weight="BOLD")
        entete.next_to(titre, DOWN, buff=0.35)

        schema_z = _schema_but2ene(cis=True)
        label_z = Text("(Z) — cis : les 2 CH₃ du même côté", font_size=18, color=WHITE)
        bloc_z = VGroup(schema_z, label_z).arrange(DOWN, buff=0.3)

        schema_e = _schema_but2ene(cis=False)
        label_e = Text("(E) — trans : les 2 CH₃ de part et d'autre", font_size=18, color=WHITE)
        bloc_e = VGroup(schema_e, label_e).arrange(DOWN, buff=0.3)

        schemas = VGroup(bloc_z, bloc_e).arrange(RIGHT, buff=1.3, aligned_edge=DOWN)
        schemas.next_to(entete, DOWN, buff=0.5)
        _fit(schemas, entete.get_bottom()[1] - 0.4)

        groupe = VGroup(entete, schemas)

        with self.voiceover(
            text=(
                "Le but-deux-ène, C H trois, C H, double liaison, C H, C "
                "H trois, en est l'exemple fondamental : chaque carbone "
                "de la double liaison porte un groupe méthyle et un "
                "hydrogène, deux groupes différents, la condition "
                "d'existence est donc remplie. Dans l'isomère Z, aussi "
                "appelé cis, les deux groupes méthyles se trouvent du "
                "même côté de la double liaison. Dans l'isomère E, aussi "
                "appelé trans, ils se trouvent de part et d'autre."
            )
        ) as tracker:
            self.play(FadeIn(entete))
            self.play(FadeIn(bloc_z))
            self.play(FadeIn(bloc_e))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(groupe))

        # --- À retenir : Z et E sont deux molécules distinctes -------------------
        retenir = example_box(
            VGroup(
                MathTex(r"\text{(Z)-but-2-ène} \neq \text{(E)-but-2-ène}", font_size=30),
                Text(
                    _wrap(
                        "Ce sont deux molécules réellement différentes, "
                        "avec des propriétés physiques distinctes (ex. "
                        "température d'ébullition).",
                        width=46,
                    ),
                    font_size=22,
                ),
            ).arrange(DOWN, buff=0.35),
            box_width=11.0,
        )
        retenir.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Retenons l'essentiel : le Z-but-deux-ène et le "
                "E-but-deux-ène ne sont pas la même molécule. Ce sont deux "
                "stéréoisomères réellement différents, avec des "
                "propriétés physiques distinctes, comme leur température "
                "d'ébullition, bien qu'ils partagent la même formule "
                "brute et la même chaîne carbonée."
            )
        ) as tracker:
            self.play(FadeIn(retenir))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(retenir))

        # --- Pièges à éviter -------------------------------------------------------
        piege = warning_box(
            Text(
                _wrap(
                    "Ne jamais attribuer d'étiquette Z ou E à un alcène "
                    "sans vérifier d'abord la condition d'existence : si "
                    "un des deux carbones de la double liaison porte deux "
                    "fois le même groupe (ex. propène CH2=CH-CH3), il n'y "
                    "a tout simplement pas de stéréoisomérie Z/E.",
                    width=48,
                ),
                font_size=23,
            ),
        )
        piege.next_to(titre, DOWN, buff=0.4)
        _fit(piege, titre.get_bottom()[1] - 0.4)

        with self.voiceover(
            text=(
                "Attention à un piège très fréquent : ne jamais attribuer "
                "d'étiquette Z ou E à un alcène sans vérifier d'abord la "
                "condition d'existence. Si l'un des deux carbones de la "
                "double liaison porte deux fois le même groupe, comme "
                "dans le propène, il n'y a tout simplement pas de "
                "stéréoisomérie Z sur E possible pour cette molécule."
            )
        ) as tracker:
            self.play(FadeIn(piege))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(piege), FadeOut(titre))
