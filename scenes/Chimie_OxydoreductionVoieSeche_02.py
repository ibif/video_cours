"""
scenes/Chimie_OxydoreductionVoieSeche_02.py — Chapitre 13 « Oxydoréduction
par voie sèche » (1ereC, Chimie), scène 02.

§ 1 (fin). Définition de la réaction d'oxydoréduction par voie sèche
(absence d'eau, réactifs solides/gazeux, amorcée par la chaleur) et
opposition avec la voie humide (aqueuse) déjà étudiée.
Source : 1ereC/Chimie.pdf, chapitre 13, page 125.
"""

import textwrap

from manim import (
    DOWN,
    LEFT,
    ORANGE,
    RIGHT,
    UP,
    WHITE,
    YELLOW,
    FadeIn,
    FadeOut,
    Line,
    MathTex,
    Text,
    VGroup,
    Write,
    config,
)

from shapes.base_scene import NotionScene
from shapes.boxes import definition_box, scene_title, warning_box


def _wrap(text: str, width: int = 56) -> str:
    return "\n".join(textwrap.fill(line, width=width) for line in text.split("\n"))


def _fit(mobject, top_y):
    bas_visible = -config.frame_height / 2 + 0.25
    hauteur_dispo = top_y - bas_visible
    if mobject.height > hauteur_dispo:
        mobject.scale(hauteur_dispo / mobject.height, about_point=mobject.get_top())
    return mobject


def _tableau_comparatif():
    """Tableau à deux colonnes comparant voie humide et voie sèche,
    construit avec des primitives Manim de base (Line, Text, VGroup)."""
    entetes = VGroup(
        Text("Voie humide (aqueuse)", font_size=19, color=YELLOW, weight="BOLD"),
        Text("Voie sèche", font_size=19, color=ORANGE, weight="BOLD"),
    )

    lignes = [
        ("Milieu : solution aqueuse", "Milieu : sans eau (solide/gaz)"),
        ("Réactifs souvent en ions dissous", "Réactifs solides et/ou gazeux"),
        ("Amorçage : simple contact", "Amorçage : chaleur (flamme...)"),
        ("Ex : Fe + Cu²⁺ → Fe²⁺ + Cu", "Ex : 2Mg + O₂ → 2MgO"),
    ]

    col1 = VGroup(*[Text(t[0], font_size=18, color=WHITE) for t in lignes])
    col2 = VGroup(*[Text(t[1], font_size=18, color=WHITE) for t in lignes])
    col1.arrange(DOWN, buff=0.32, aligned_edge=LEFT)
    col2.arrange(DOWN, buff=0.32, aligned_edge=LEFT)

    entetes[0].next_to(col1, UP, buff=0.3, aligned_edge=LEFT)
    col2.next_to(col1, RIGHT, buff=0.8)
    entetes[1].next_to(col2, UP, buff=0.3, aligned_edge=LEFT)

    ligne_sep = Line(
        entetes.get_left() + LEFT * 0.15 + DOWN * 0.2,
        [col2.get_right()[0] + 0.15, entetes.get_bottom()[1] - 0.2, 0],
        color=WHITE,
        stroke_width=1.5,
    )
    ligne_verticale = Line(
        [col1.get_right()[0] + 0.4, entetes.get_top()[1] + 0.1, 0],
        [col1.get_right()[0] + 0.4, col1.get_bottom()[1] - 0.15, 0],
        color=WHITE,
        stroke_width=1,
    )

    return VGroup(entetes, col1, col2, ligne_sep, ligne_verticale)


class DefinitionVoieSeche(NotionScene):
    def construct(self):
        titre = scene_title("13.1 La réaction d'oxydoréduction par voie sèche")
        titre.scale(0.46)
        titre.to_edge(UP)

        # --- Énoncé -----------------------------------------------------------
        intro = Text(
            _wrap(
                "Les deux expériences précédentes ont un point commun : "
                "aucune eau n'intervient. Comment nommer et caractériser "
                "ce type de réaction ?",
                width=56,
            ),
            font_size=24,
            color=WHITE,
        )
        intro.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Les deux expériences précédentes, la combustion du "
                "magnésium dans le dioxygène et dans le dichlore, ont un "
                "point commun : aucune eau n'intervient. Comment nommer et "
                "caractériser ce type de réaction ?"
            )
        ) as tracker:
            self.play(Write(titre))
            self.play(FadeIn(intro))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(intro))

        # --- Raisonnement : tableau comparatif -------------------------------
        entete_tab = Text("Deux façons de faire réagir un oxydant et un réducteur", font_size=21, color=YELLOW, weight="BOLD")
        entete_tab.next_to(titre, DOWN, buff=0.35)

        tableau = _tableau_comparatif()
        tableau.next_to(entete_tab, DOWN, buff=0.4)
        groupe_tab = VGroup(entete_tab, tableau)
        _fit(groupe_tab, titre.get_bottom()[1] - 0.2)
        groupe_tab.next_to(titre, DOWN, buff=0.3)

        with self.voiceover(
            text=(
                "En solution aqueuse, comme pour la réaction entre le fer "
                "et les ions cuivre deux plus, les réactifs sont dissous "
                "dans l'eau, et la réaction s'amorce par simple contact. "
                "Par voie sèche, au contraire, les réactifs sont solides ou "
                "gazeux, sans aucune eau, et la réaction ne démarre "
                "généralement qu'après un apport de chaleur suffisant, par "
                "exemple une flamme."
            )
        ) as tracker:
            self.play(FadeIn(entete_tab))
            self.play(FadeIn(tableau))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(groupe_tab))

        # --- Exemple traité : reconnaître la voie sèche ------------------------
        exemple = MathTex(r"2\,Mg + O_2 \longrightarrow 2\,MgO", font_size=32, color=ORANGE)
        exemple.next_to(titre, DOWN, buff=0.6)

        note_exemple = Text(
            _wrap(
                "Mg (solide) et O₂ (gaz) réagissent directement, sans eau, "
                "après amorçage par une flamme : c'est bien une "
                "oxydoréduction par voie sèche.",
                width=52,
            ),
            font_size=22, color=WHITE,
        )
        note_exemple.next_to(exemple, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Reprenons l'exemple de la combustion du magnésium : "
                "deux Mg plus O deux donne deux MgO. Le magnésium solide "
                "et le dioxygène gazeux réagissent directement, sans la "
                "moindre trace d'eau, après amorçage par une flamme. "
                "C'est exactement la définition d'une oxydoréduction par "
                "voie sèche."
            )
        ) as tracker:
            self.play(Write(exemple))
            self.play(FadeIn(note_exemple))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(exemple), FadeOut(note_exemple))

        # --- À retenir : définition formelle -----------------------------------
        definition = definition_box(
            Text(
                _wrap(
                    "Une réaction d'oxydoréduction par voie sèche est une "
                    "réaction au cours de laquelle des électrons sont "
                    "transférés directement entre des réactifs SOLIDES "
                    "et/ou GAZEUX, EN L'ABSENCE D'EAU, généralement "
                    "amorcée par un fort apport de chaleur.",
                    width=46,
                ),
                font_size=23,
            ),
        )
        definition.next_to(titre, DOWN, buff=0.45)

        with self.voiceover(
            text=(
                "Retenons la définition : une réaction d'oxydoréduction "
                "par voie sèche est une réaction au cours de laquelle des "
                "électrons sont transférés directement entre des réactifs "
                "solides et, ou, gazeux, en l'absence totale d'eau, "
                "généralement amorcée par un fort apport de chaleur."
            )
        ) as tracker:
            self.play(FadeIn(definition))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(definition))

        # --- Piège à éviter -----------------------------------------------------
        piege = warning_box(
            Text(
                _wrap(
                    "Ne pas confondre les deux voies à cause du mot "
                    "« oxydoréduction » commun : le critère de distinction "
                    "est la PRÉSENCE OU L'ABSENCE D'EAU, pas la nature "
                    "chimique du transfert d'électrons lui-même, qui reste "
                    "identique dans les deux cas.",
                    width=48,
                ),
                font_size=21,
            ),
        )
        piege.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Attention à ne pas confondre les deux voies à cause du "
                "mot « oxydoréduction », commun aux deux. Le critère de "
                "distinction est uniquement la présence ou l'absence "
                "d'eau : le transfert d'électrons lui-même reste "
                "exactement le même phénomène chimique dans les deux cas."
            )
        ) as tracker:
            self.play(FadeIn(piege))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(piege), FadeOut(titre))
