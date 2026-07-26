"""
scenes/Chimie_ClassificationQualitativeRedox_01.py — Chapitre 10
« Classification qualitative des couples oxydant/réducteur » (1ereC,
Chimie), scène 01.

§ 1. Force des oxydants et des réducteurs — expériences et interprétation.
Trois expériences : lame de cuivre dans une solution de sulfate de cuivre
(rien), lame de fer dans une solution de sulfate de cuivre (dépôt
rouge-orangé de cuivre + décoloration du bleu), lame de cuivre dans une
solution de sulfate de fer II (rien). Tableau récapitulatif des
observations, interprétation par demi-équations électroniques et équation
bilan Cu²⁺ + Fe → Cu + Fe²⁺. Conclusion : le fer est un réducteur plus
fort que le cuivre.
Source : 1ereC/Chimie.pdf, chapitre 10, pages 94-95.
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
from shapes.boxes import property_box, scene_title, warning_box


def _wrap(text: str, width: int = 56) -> str:
    return "\n".join(textwrap.fill(line, width=width) for line in text.split("\n"))


def _fit(mobject, top_y):
    bas_visible = -config.frame_height / 2 + 0.25
    hauteur_dispo = top_y - bas_visible
    if mobject.height > hauteur_dispo:
        mobject.scale(hauteur_dispo / mobject.height, about_point=mobject.get_top())
    return mobject


def _tableau_experiences():
    """Tableau récapitulatif des 3 expériences, construit avec des
    primitives Manim de base (Line, Text, VGroup) — aucune bibliothèque
    externe."""
    entetes = VGroup(
        Text("Expérience", font_size=20, color=YELLOW, weight="BOLD"),
        Text("Observation", font_size=20, color=YELLOW, weight="BOLD"),
    )

    lignes_texte = [
        ("Cu dans Cu²⁺(aq)", "aucun changement"),
        ("Fe dans Cu²⁺(aq)", "dépôt rouge-orangé + bleu qui pâlit"),
        ("Cu dans Fe²⁺(aq)", "aucun changement"),
    ]

    col1 = VGroup(*[Text(t[0], font_size=19, color=WHITE) for t in lignes_texte])
    col2 = VGroup(*[Text(t[1], font_size=19, color=WHITE) for t in lignes_texte])
    col1.arrange(DOWN, buff=0.35, aligned_edge=LEFT)
    col2.arrange(DOWN, buff=0.35, aligned_edge=LEFT)

    entetes[0].next_to(col1, UP, buff=0.3, aligned_edge=LEFT)
    col2.next_to(col1, RIGHT, buff=0.9)
    entetes[1].next_to(col2, UP, buff=0.3, aligned_edge=LEFT)

    ligne_sep = Line(
        entetes.get_left() + LEFT * 0.15 + DOWN * 0.2,
        [col2.get_right()[0] + 0.15, entetes.get_bottom()[1] - 0.2, 0],
        color=WHITE,
        stroke_width=1.5,
    )

    tableau = VGroup(entetes, col1, col2, ligne_sep)
    return tableau


class ForceOxydantsReducteursExperiences(NotionScene):
    def construct(self):
        titre = scene_title("10.1 Force des oxydants et réducteurs — expériences")
        titre.scale(0.48)
        titre.to_edge(UP)

        # --- Énoncé : mise en situation -----------------------------------
        intro = Text(
            _wrap(
                "Tous les métaux ne réagissent pas de la même façon avec les "
                "ions métalliques en solution. Comparons trois expériences "
                "avec des lames de cuivre et de fer pour comprendre ce qui "
                "distingue un réducteur fort d'un réducteur faible.",
                width=56,
            ),
            font_size=24,
            color=WHITE,
        )
        intro.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Tous les métaux ne réagissent pas de la même façon avec "
                "les ions métalliques en solution. Comparons trois "
                "expériences réalisées avec des lames de cuivre et de fer, "
                "pour comprendre ce qui distingue un réducteur fort d'un "
                "réducteur faible."
            )
        ) as tracker:
            self.play(Write(titre))
            self.play(FadeIn(intro))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(intro))

        # --- Raisonnement : les trois expériences et le tableau -----------
        entete_exp = Text("Trois expériences", font_size=22, color=YELLOW, weight="BOLD")
        entete_exp.next_to(titre, DOWN, buff=0.35)

        tableau = _tableau_experiences()
        tableau.next_to(entete_exp, DOWN, buff=0.45)
        groupe_exp = VGroup(entete_exp, tableau)
        _fit(groupe_exp, titre.get_bottom()[1] - 0.2)
        groupe_exp.next_to(titre, DOWN, buff=0.35)

        with self.voiceover(
            text=(
                "Première expérience : on plonge une lame de cuivre dans "
                "une solution de sulfate de cuivre deux : aucun changement "
                "n'est observé. Deuxième expérience : on plonge une lame "
                "de fer dans cette même solution de sulfate de cuivre "
                "deux : un dépôt rouge-orangé de cuivre métallique apparaît "
                "sur le fer, et la couleur bleue de la solution pâlit "
                "progressivement. Troisième expérience : on plonge une "
                "lame de cuivre dans une solution de sulfate de fer deux : "
                "là encore, aucun changement n'est observé."
            )
        ) as tracker:
            self.play(FadeIn(entete_exp))
            self.play(FadeIn(tableau))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(groupe_exp))

        # --- Exemple traité : interprétation par demi-équations ------------
        entete_interp = Text("Interprétation : demi-équations et bilan", font_size=22, color=YELLOW, weight="BOLD")
        entete_interp.next_to(titre, DOWN, buff=0.35)

        demi_reduction = MathTex(r"Cu^{2+} + 2e^{-} \longrightarrow Cu", font_size=28, color=WHITE)
        demi_oxydation = MathTex(r"Fe \longrightarrow Fe^{2+} + 2e^{-}", font_size=28, color=WHITE)
        bilan = MathTex(r"Cu^{2+} + Fe \longrightarrow Cu + Fe^{2+}", font_size=30, color=ORANGE)

        equations = VGroup(demi_reduction, demi_oxydation, bilan).arrange(DOWN, buff=0.4)
        equations.next_to(entete_interp, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Seule l'expérience du fer dans le sulfate de cuivre donne "
                "lieu à une réaction. Le dépôt rouge-orangé montre que les "
                "ions cuivre deux ont capté des électrons pour redonner du "
                "cuivre métal : c'est une réduction, C-u deux plus, deux "
                "électrons, donne C-u. La décoloration du bleu montre que "
                "le fer, lui, a cédé des électrons pour former des ions fer "
                "deux : c'est une oxydation, F-e donne F-e deux plus, deux "
                "électrons. En combinant ces deux demi-équations, on "
                "obtient l'équation bilan : C-u deux plus, plus F-e, donne "
                "C-u, plus F-e deux plus."
            )
        ) as tracker:
            self.play(FadeIn(entete_interp))
            self.play(Write(demi_reduction))
            self.play(Write(demi_oxydation))
            self.play(Write(bilan))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(entete_interp), FadeOut(equations))

        # --- À retenir : conclusion -----------------------------------------
        conclusion = property_box(
            VGroup(
                Text(
                    "Le fer cède ses électrons plus facilement que le cuivre :",
                    font_size=22, weight="BOLD",
                ),
                Text("le fer est un réducteur plus fort que le cuivre.", font_size=22, weight="BOLD"),
                Text("Réciproquement, Cu²⁺ est un oxydant plus fort que Fe²⁺.", font_size=21),
            ).arrange(DOWN, buff=0.3, aligned_edge=LEFT),
            box_width=12.0,
        )
        conclusion.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Retenons l'essentiel : le fer cède ses électrons plus "
                "facilement que le cuivre, c'est donc un réducteur plus "
                "fort que le cuivre. Réciproquement, les ions cuivre deux "
                "sont un oxydant plus fort que les ions fer deux, puisque "
                "ce sont eux qui ont capté les électrons."
            )
        ) as tracker:
            self.play(FadeIn(conclusion))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(conclusion))

        # --- Piège à éviter -----------------------------------------------
        piege = warning_box(
            Text(
                _wrap(
                    "Ne pas se fier à l'aspect du métal qui « reste intact » : "
                    "c'est le métal qui se transforme (qui s'oxyde, ici le "
                    "fer) qui est le réducteur le plus fort, pas celui qui "
                    "semble ne rien faire.",
                    width=48,
                ),
                font_size=22,
            ),
        )
        piege.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Attention à un piège fréquent : il ne faut pas se fier à "
                "l'aspect du métal qui « reste intact ». C'est au contraire "
                "le métal qui se transforme, qui s'oxyde — ici le fer — qui "
                "est le réducteur le plus fort, et non celui qui semble ne "
                "rien faire."
            )
        ) as tracker:
            self.play(FadeIn(piege))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(piege), FadeOut(titre))
