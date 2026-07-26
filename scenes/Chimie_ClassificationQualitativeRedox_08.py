"""
scenes/Chimie_ClassificationQualitativeRedox_08.py — Chapitre 10
« Classification qualitative des couples oxydant/réducteur » (1ereC,
Chimie), scène 08.

§ 4 (suite). Applications : protection des métaux contre la corrosion
(anode sacrificielle en magnésium ou zinc, fer galvanisé), exemple
contextualisé (pirogue, canalisation en Côte d'Ivoire). Cimentation :
récupération du cuivre des eaux de mine par la ferraille,
Cu²⁺ + Fe → Cu + Fe²⁺.
Source : 1ereC/Chimie.pdf, chapitre 10, pages 99-100.
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
    BLUE,
    Arrow,
    FadeIn,
    FadeOut,
    Line,
    MathTex,
    Rectangle,
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


def _schema_anode_sacrificielle():
    """Schéma simplifié d'une canalisation en fer protégée par une anode
    sacrificielle en zinc, construit uniquement avec des primitives Manim
    de base (Rectangle, Line, Arrow, Text, VGroup)."""

    canalisation = Rectangle(width=3.2, height=0.6, color=WHITE, fill_color="#595959", fill_opacity=0.5, stroke_width=2)
    label_canal = Text("canalisation en fer", font_size=15, color=WHITE)
    label_canal.next_to(canalisation, UP, buff=0.12)

    anode = Rectangle(width=0.5, height=0.9, color="#288073", fill_color="#288073", fill_opacity=0.6, stroke_width=2)
    anode.next_to(canalisation, DOWN, buff=0.35)
    fil = Line(canalisation.get_bottom(), anode.get_top(), color=YELLOW, stroke_width=2)
    label_anode = Text("anode sacrificielle\nen zinc (s'oxyde à\nla place du fer)", font_size=13, color="#288073", line_spacing=0.8)
    label_anode.next_to(anode, DOWN, buff=0.15)

    fleche_electrons = Arrow(anode.get_top() + UP * 0.05, canalisation.get_bottom() + DOWN * 0.05, color=YELLOW, stroke_width=2, buff=0, max_tip_length_to_length_ratio=0.3)
    label_electrons = Text("électrons cédés par Zn", font_size=12, color=YELLOW)
    label_electrons.next_to(fleche_electrons, RIGHT, buff=0.1)

    schema = VGroup(canalisation, label_canal, anode, fil, label_anode, fleche_electrons, label_electrons)
    return schema


class ApplicationsProtectionCimentation(NotionScene):
    def construct(self):
        titre = scene_title("10.4 Applications — protection des métaux et cimentation")
        titre.scale(0.42)
        titre.to_edge(UP)

        # --- Énoncé -----------------------------------------------------------
        intro = Text(
            _wrap(
                "La classification qualitative ne sert pas qu'à prévoir des "
                "réactions en tube à essai : elle guide aussi deux "
                "applications très concrètes, la protection des métaux et "
                "la récupération du cuivre.",
                width=56,
            ),
            font_size=23,
            color=WHITE,
        )
        intro.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "La classification qualitative ne sert pas seulement à "
                "prévoir des réactions en tube à essai : elle guide aussi "
                "deux applications très concrètes, la protection des "
                "métaux contre la corrosion, et la récupération du cuivre "
                "par cimentation."
            )
        ) as tracker:
            self.play(Write(titre))
            self.play(FadeIn(intro))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(intro))

        # --- Raisonnement : la protection par anode sacrificielle ---------------
        entete_prot = Text("Protection contre la corrosion : l'anode sacrificielle", font_size=19, color=YELLOW, weight="BOLD")
        entete_prot.next_to(titre, DOWN, buff=0.3)

        texte_prot = Text(
            _wrap(
                "Pour protéger un objet en fer, on le relie à un métal "
                "plus réducteur (Mg, Zn) : ce dernier s'oxyde à la place "
                "du fer, qui reste intact tant que l'anode n'est pas "
                "entièrement consommée.",
                width=54,
            ),
            font_size=18, color=WHITE,
        )
        texte_prot.next_to(entete_prot, DOWN, buff=0.25)

        schema_anode = _schema_anode_sacrificielle()
        schema_anode.scale(0.9)
        schema_anode.next_to(texte_prot, DOWN, buff=0.3)

        groupe_prot = VGroup(entete_prot, texte_prot, schema_anode)
        _fit(groupe_prot, titre.get_bottom()[1] - 0.15)
        groupe_prot.next_to(titre, DOWN, buff=0.2)

        with self.voiceover(
            text=(
                "Pour protéger un objet en fer contre la corrosion, on le "
                "relie électriquement à un métal plus réducteur, comme le "
                "magnésium ou le zinc : ce métal, appelé anode "
                "sacrificielle, s'oxyde à la place du fer, puisqu'il est un "
                "réducteur plus fort. Le fer reste ainsi protégé tant que "
                "l'anode n'est pas entièrement consommée."
            )
        ) as tracker:
            self.play(FadeIn(entete_prot))
            self.play(FadeIn(texte_prot))
            self.play(FadeIn(schema_anode))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(groupe_prot))

        # --- Exemple traité : contexte ivoirien + fer galvanisé ------------------
        entete_ex = Text("Exemples contextualisés", font_size=20, color=YELLOW, weight="BOLD")
        entete_ex.next_to(titre, DOWN, buff=0.3)

        exemples = VGroup(
            Text(
                "• Le fer galvanisé (toitures, tôles) est recouvert d'une",
                font_size=19, color=WHITE,
            ),
            Text(
                "  fine couche de zinc protecteur, très répandu en Côte",
                font_size=19, color=WHITE,
            ),
            Text("  d'Ivoire pour les toitures et clôtures.", font_size=19, color=WHITE),
            Text(
                "• Les canalisations enterrées et les coques métalliques",
                font_size=19, color=WHITE,
            ),
            Text(
                "  de pirogues motorisées utilisent des blocs de zinc ou",
                font_size=19, color=WHITE,
            ),
            Text("  de magnésium comme anodes sacrificielles.", font_size=19, color=WHITE),
        ).arrange(DOWN, buff=0.15, aligned_edge=LEFT)
        exemples.next_to(entete_ex, DOWN, buff=0.3)

        with self.voiceover(
            text=(
                "On retrouve ce principe très concrètement : le fer "
                "galvanisé, utilisé pour les toitures et les tôles en Côte "
                "d'Ivoire, est recouvert d'une fine couche de zinc "
                "protecteur. De même, les canalisations enterrées et les "
                "coques métalliques de pirogues motorisées utilisent des "
                "blocs de zinc ou de magnésium comme anodes sacrificielles, "
                "remplacés régulièrement."
            )
        ) as tracker:
            self.play(FadeIn(entete_ex))
            self.play(FadeIn(exemples))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(entete_ex), FadeOut(exemples))

        # --- À retenir : la cimentation -------------------------------------------
        entete_ciment = Text("La cimentation : récupérer le cuivre", font_size=20, color=YELLOW, weight="BOLD")
        entete_ciment.next_to(titre, DOWN, buff=0.3)

        texte_ciment = Text(
            _wrap(
                "Les eaux de drainage des mines de cuivre contiennent des "
                "ions Cu²⁺ dissous. En les faisant couler sur de la "
                "ferraille (Fe), on récupère le cuivre métal :",
                width=54,
            ),
            font_size=19, color=WHITE,
        )
        eq_ciment = MathTex(r"Cu^{2+} + Fe \longrightarrow Cu + Fe^{2+}", font_size=28, color=ORANGE)

        contenu_ciment = VGroup(texte_ciment, eq_ciment).arrange(DOWN, buff=0.3)
        contenu_ciment.next_to(entete_ciment, DOWN, buff=0.3)
        groupe_ciment = VGroup(entete_ciment, contenu_ciment)
        _fit(groupe_ciment, titre.get_bottom()[1] - 0.15)
        groupe_ciment.next_to(titre, DOWN, buff=0.25)

        with self.voiceover(
            text=(
                "Retenons l'essentiel avec la cimentation : les eaux de "
                "drainage des mines de cuivre contiennent des ions cuivre "
                "deux plus dissous. En les faisant couler sur de la "
                "ferraille, riche en fer, on récupère le cuivre sous forme "
                "métallique, selon la même équation que dans notre toute "
                "première expérience : ions cuivre deux plus, plus fer, "
                "donne cuivre, plus ions fer deux plus. C'est un procédé "
                "économique de récupération du cuivre."
            )
        ) as tracker:
            self.play(FadeIn(entete_ciment))
            self.play(FadeIn(texte_ciment))
            self.play(Write(eq_ciment))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(groupe_ciment))

        # --- Piège à éviter ---------------------------------------------------
        piege = warning_box(
            Text(
                _wrap(
                    "L'anode sacrificielle ne protège PAS comme une barrière "
                    "mécanique (une peinture) : elle protège parce qu'elle "
                    "s'oxyde préférentiellement, un phénomène électrochimique. "
                    "Une fois l'anode consommée, la protection disparaît.",
                    width=48,
                ),
                font_size=19,
            ),
        )
        piege.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Attention à un piège fréquent : l'anode sacrificielle ne "
                "protège pas comme le ferait une simple barrière physique, "
                "une couche de peinture par exemple. Elle protège parce "
                "qu'elle s'oxyde préférentiellement, un phénomène "
                "électrochimique. Une fois l'anode entièrement consommée, "
                "la protection disparaît et doit être renouvelée."
            )
        ) as tracker:
            self.play(FadeIn(piege))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(piege), FadeOut(titre))
