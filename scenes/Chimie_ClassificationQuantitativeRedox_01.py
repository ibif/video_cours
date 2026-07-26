"""
scenes/Chimie_ClassificationQuantitativeRedox_01.py — Chapitre 11
« Classification quantitative des couples oxydant/réducteur » (1ereC,
Chimie), scène 01.

§ 1. Rappels et limites de l'approche qualitative. Rappel de la
classification qualitative des métaux (Na>Mg>Al>Zn>Fe>Ni>Sn>Pb>H>Cu>Hg>
Ag>Au) obtenue par des expériences de déplacement, et de la règle du
gamma pour prévoir le sens spontané d'une réaction. Limites de cette
approche : elle ne dit pas si la réaction est totale ou partielle, elle
est inutilisable pour des couples très proches dans le classement, et elle
ne permet aucun calcul (pas de valeur numérique) → nécessité d'un critère
quantitatif, le potentiel standard E°.
Source : 1ereC/Chimie.pdf, chapitre 11, pages 102-103.
"""

import textwrap

from manim import (
    DOWN,
    LEFT,
    RIGHT,
    UP,
    WHITE,
    YELLOW,
    RED,
    GREEN,
    Arrow,
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
from shapes.boxes import scene_title, warning_box


def _wrap(text: str, width: int = 56) -> str:
    return "\n".join(textwrap.fill(line, width=width) for line in text.split("\n"))


def _bullets(items, font_size=21, color=WHITE, width=54):
    lines = VGroup(
        *[Text(f"• {_wrap(it, width=width)}", font_size=font_size, color=color) for it in items]
    )
    lines.arrange(DOWN, aligned_edge=LEFT, buff=0.22)
    return lines


def _fit(mobject, top_y):
    bas_visible = -config.frame_height / 2 + 0.25
    hauteur_dispo = top_y - bas_visible
    if mobject.height > hauteur_dispo:
        mobject.scale(hauteur_dispo / mobject.height, about_point=mobject.get_top())
    return mobject


def _classification_qualitative():
    """Classement Na>Mg>Al>Zn>Fe>Ni>Sn>Pb>H>Cu>Hg>Ag>Au, pouvoir réducteur
    décroissant de gauche à droite, construit avec Text/MathTex."""
    metaux = ["Na", "Mg", "Al", "Zn", "Fe", "Ni", "Sn", "Pb", "H", "Cu", "Hg", "Ag", "Au"]
    ligne1 = VGroup(*[MathTex(m, font_size=26, color=WHITE) for m in metaux[:7]])
    ligne1.arrange(RIGHT, buff=0.42)
    ligne2 = VGroup(*[MathTex(m, font_size=26, color=WHITE) for m in metaux[7:]])
    ligne2.arrange(RIGHT, buff=0.42)

    def _avec_fleches(ligne, noms):
        groupe = VGroup(ligne[0])
        for i in range(1, len(ligne)):
            fleche = MathTex(">", font_size=24, color=YELLOW)
            fleche.move_to((ligne[i - 1].get_right() + ligne[i].get_left()) / 2)
            groupe.add(fleche, ligne[i])
        return groupe

    groupe1 = _avec_fleches(ligne1, metaux[:7])
    groupe2 = _avec_fleches(ligne2, metaux[7:])
    groupe2.next_to(groupe1, DOWN, buff=0.45)

    legende = VGroup(
        Text("pouvoir réducteur du métal décroissant →", font_size=16, color=GREEN),
    )
    legende.next_to(groupe2, DOWN, buff=0.35)

    return VGroup(groupe1, groupe2, legende)


def _regle_du_gamma():
    """Schéma de la règle du gamma : deux couples Ox/Red positionnés selon
    leur rang dans le classement, reliés par une flèche en forme de Γ qui
    indique le sens spontané de la réaction (construit avec Line/Arrow)."""
    # Couple du haut (réducteur fort) : Zn2+/Zn — couple du bas (oxydant
    # fort, plus près de Au) : Cu2+/Cu.
    ox_haut = MathTex(r"Zn^{2+}", font_size=28, color=WHITE)
    red_haut = MathTex(r"Zn", font_size=28, color=WHITE)
    ox_bas = MathTex(r"Cu^{2+}", font_size=28, color=WHITE)
    red_bas = MathTex(r"Cu", font_size=28, color=WHITE)

    col_ox_x, col_red_x = -1.6, 1.6
    ox_haut.move_to([col_ox_x, 0.9, 0])
    red_haut.move_to([col_red_x, 0.9, 0])
    ox_bas.move_to([col_ox_x, -0.9, 0])
    red_bas.move_to([col_red_x, -0.9, 0])

    etiquette_ox = Text("Oxydant", font_size=18, color=YELLOW)
    etiquette_ox.next_to(VGroup(ox_haut, ox_bas), UP, buff=0.5).shift(LEFT * 0)
    etiquette_ox.move_to([col_ox_x, 1.7, 0])
    etiquette_red = Text("Réducteur", font_size=18, color=YELLOW)
    etiquette_red.move_to([col_red_x, 1.7, 0])

    # Trait Γ : segment vertical le long de la colonne "Oxydant" (de Cu2+
    # vers la hauteur de Zn2+), puis segment horizontal vers Zn.
    coin = [col_ox_x, 0.9, 0]
    vertical = Line(ox_bas.get_center() + UP * 0.3, coin, color=RED, stroke_width=5)
    horizontal = Line(coin, red_haut.get_center() + LEFT * 0.3, color=RED, stroke_width=5)
    fleche = Arrow(
        red_haut.get_center() + LEFT * 0.35,
        red_haut.get_left() + LEFT * 0.05,
        color=RED,
        stroke_width=5,
        buff=0,
        max_tip_length_to_length_ratio=0.6,
    )
    gamma = VGroup(vertical, horizontal, fleche)

    trait_couple_haut = Line(ox_haut.get_right(), red_haut.get_left(), color=WHITE, stroke_width=1)
    trait_couple_bas = Line(ox_bas.get_right(), red_bas.get_left(), color=WHITE, stroke_width=1)

    legende = Text(
        "Cu²⁺ (oxydant fort) + Zn (réducteur fort) → Cu + Zn²⁺ : réaction spontanée",
        font_size=16,
        color=GREEN,
    )
    legende.move_to([0, -1.8, 0])

    return VGroup(
        etiquette_ox, etiquette_red,
        ox_haut, red_haut, ox_bas, red_bas,
        trait_couple_haut, trait_couple_bas,
        gamma, legende,
    )


class RappelsLimitesApprocheQualitative(NotionScene):
    def construct(self):
        titre = scene_title("11.1 Rappels : de la classification qualitative au critère quantitatif")
        titre.scale(0.44)
        titre.to_edge(UP)

        # --- Énoncé : mise en situation ------------------------------------------
        intro = Text(
            _wrap(
                "En Seconde puis en Première, une classification qualitative "
                "des couples oxydant/réducteur des métaux a été établie à "
                "partir d'expériences de déplacement. Que dit-elle, et "
                "surtout, que ne dit-elle PAS ?",
                width=58,
            ),
            font_size=24,
            color=WHITE,
        )
        intro.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Nous avons déjà établi, à partir d'expériences de "
                "déplacement entre métaux et ions métalliques, une "
                "classification qualitative des couples oxydant sur "
                "réducteur. Ce chapitre va nous montrer ce que cette "
                "classification qualitative permet de dire, et surtout ce "
                "qu'elle ne permet pas de dire, ce qui nous conduira à "
                "introduire un outil quantitatif : le potentiel standard."
            )
        ) as tracker:
            self.play(Write(titre))
            self.play(FadeIn(intro))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(intro))

        # --- Raisonnement : rappel de la classification --------------------------
        entete_classement = Text("Rappel : classification qualitative des métaux", font_size=22, color=YELLOW, weight="BOLD")
        entete_classement.next_to(titre, DOWN, buff=0.35)

        classement = _classification_qualitative()
        classement.next_to(entete_classement, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Rappelons ce classement, obtenu expérimentalement : "
                "sodium, magnésium, aluminium, zinc, fer, nickel, étain, "
                "plomb, hydrogène, cuivre, mercure, argent, or. Le pouvoir "
                "réducteur du métal diminue de la gauche vers la droite : "
                "le sodium est le réducteur le plus fort de la liste, "
                "l'or est le plus faible. Symétriquement, le pouvoir "
                "oxydant de l'ion métallique correspondant augmente de la "
                "gauche vers la droite."
            )
        ) as tracker:
            self.play(FadeIn(entete_classement))
            self.play(Write(classement))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(entete_classement), FadeOut(classement))

        # --- Raisonnement : règle du gamma ---------------------------------------
        entete_gamma = Text("Rappel : la règle du gamma (Γ)", font_size=22, color=YELLOW, weight="BOLD")
        entete_gamma.next_to(titre, DOWN, buff=0.35)

        gamma = _regle_du_gamma()
        gamma.scale(0.95)
        gamma.next_to(entete_gamma, DOWN, buff=0.45)

        with self.voiceover(
            text=(
                "Pour prévoir le sens spontané d'une réaction entre deux "
                "couples de ce classement, on utilise la règle du gamma. "
                "On place les couples oxydant sur réducteur selon leur "
                "rang dans le classement, puis on trace, avec le doigt ou "
                "sur le schéma, la lettre grecque gamma : elle relie "
                "l'oxydant du couple situé le plus à droite au réducteur "
                "du couple situé le plus à gauche. Ici, l'ion cuivre deux "
                "plus, oxydant, réagit avec le zinc métal, réducteur, pour "
                "donner le cuivre métal et l'ion zinc deux plus : c'est le "
                "sens indiqué par le gamma qui est spontané."
            )
        ) as tracker:
            self.play(FadeIn(entete_gamma))
            self.play(Write(gamma))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(entete_gamma), FadeOut(gamma))

        # --- À retenir / limites : nécessité d'un critère quantitatif ------------
        limites = _bullets(
            [
                "Elle ne dit pas SI la réaction est totale ou seulement "
                "partielle (équilibre) : elle donne juste un sens.",
                "Elle devient peu fiable pour deux couples très proches "
                "dans le classement (l'ordre exact est parfois incertain).",
                "Elle ne permet AUCUN calcul : pas de valeur numérique, "
                "donc impossible de calculer une f.é.m. de pile.",
            ],
            font_size=21,
            width=54,
        )
        entete_limites = Text("Limites de l'approche qualitative", font_size=22, color=RED, weight="BOLD")
        entete_limites.next_to(titre, DOWN, buff=0.4)
        limites.next_to(entete_limites, DOWN, buff=0.35)
        _fit(VGroup(entete_limites, limites), entete_limites.get_bottom()[1] - 0.3)

        with self.voiceover(
            text=(
                "Mais cette classification qualitative a trois limites "
                "importantes. Premièrement, elle ne dit pas si la "
                "réaction est totale ou seulement partielle, c'est-à-dire "
                "limitée par un équilibre. Deuxièmement, elle devient peu "
                "fiable pour deux couples très proches dans le classement. "
                "Troisièmement, et surtout, elle ne permet aucun calcul : "
                "aucune valeur numérique n'est associée aux couples, donc "
                "impossible, par exemple, de calculer la force "
                "électromotrice d'une pile. Il nous faut donc un critère "
                "quantitatif : ce sera le potentiel standard, noté E "
                "rond, que nous allons construire dans ce chapitre à "
                "partir de la pile Daniell."
            )
        ) as tracker:
            self.play(FadeIn(entete_limites))
            self.play(FadeIn(limites))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(entete_limites), FadeOut(limites))

        # --- Piège à éviter -------------------------------------------------------
        piege = warning_box(
            Text(
                _wrap(
                    "La règle du gamma donne un SENS de réaction, jamais une "
                    "valeur : elle ne remplace pas un calcul de f.é.m. ni "
                    "ne renseigne sur le caractère total ou partiel de la "
                    "réaction.",
                    width=48,
                ),
                font_size=21,
            ),
        )
        piege.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Retenons ce piège avant d'avancer : la règle du gamma "
                "donne uniquement un sens de réaction, jamais une valeur "
                "numérique. Elle ne remplace donc ni un calcul de force "
                "électromotrice, ni une information sur le caractère "
                "total ou partiel de la réaction."
            )
        ) as tracker:
            self.play(FadeIn(piege))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(piege), FadeOut(titre))
