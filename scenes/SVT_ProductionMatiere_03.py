"""
scenes/SVT_ProductionMatiere_03.py — Chapitre 11 (1ereD, SVT), scène 03.

§ 11.2 / 11.2.1 Les conditions nécessaires à la production de matière :
stratégie générale des biologistes (supprimer un facteur, observer), le
test à l'eau iodée (propriété + protocole de décoloration), méthode
générale de mise en évidence en cinq étapes.
Source : 1ereD/SVT.pdf, pages 146-147, 149.
"""

import textwrap

from manim import (
    DOWN,
    LEFT,
    ORIGIN,
    RIGHT,
    UP,
    WHITE,
    YELLOW,
    Arrow,
    Circle,
    FadeIn,
    FadeOut,
    Text,
    VGroup,
    Write,
    config,
)

from shapes.base_scene import NotionScene
from shapes.boxes import method_box, property_box, scene_title


def _wrap(text: str, width: int = 56) -> str:
    return "\n".join(textwrap.fill(line, width=width) for line in text.split("\n"))


def _bullets(items, font_size=22, color=WHITE, width=52):
    lines = VGroup(
        *[Text(f"• {_wrap(it, width=width)}", font_size=font_size, color=color) for it in items]
    )
    lines.arrange(DOWN, aligned_edge=LEFT, buff=0.22)
    return lines


def _fit(mobject, top_anchor):
    """Réduit l'échelle de `mobject` si sa hauteur dépasse le cadre
    visible OU si sa largeur dépasse la largeur du cadre (cas fréquent
    d'un groupe boîte + schéma placés côte à côte)."""
    bas_visible = -config.frame_height / 2 + 0.25
    hauteur_dispo = top_anchor - bas_visible
    largeur_dispo = config.frame_width - 0.5
    echelle = 1.0
    if mobject.height > hauteur_dispo:
        echelle = min(echelle, hauteur_dispo / mobject.height)
    if mobject.width > largeur_dispo:
        echelle = min(echelle, largeur_dispo / mobject.width)
    if echelle < 1.0:
        mobject.scale(echelle, about_point=mobject.get_top())
    return mobject


def _pastille(couleur, texte):
    """Petit disque coloré + légende, pour illustrer le virage du test."""
    disque = Circle(radius=0.4, fill_color=couleur, fill_opacity=1.0, stroke_color=WHITE, stroke_width=2)
    label = Text(texte, font_size=15, color=WHITE)
    label.next_to(disque, DOWN, buff=0.15)
    return VGroup(disque, label)


class TestEauIodeeEtMethode(NotionScene):
    def construct(self):
        # --- Énoncé ----------------------------------------------------
        titre = scene_title("11.2 — Les conditions de la production de matière")
        titre.scale(0.5)
        titre.to_edge(UP)

        intro = Text(
            _wrap(
                "Nous savons quels gaz sont échangés. Reste à savoir de "
                "quoi le végétal a besoin pour fabriquer sa matière. La "
                "stratégie : supprimer un seul facteur à la fois et "
                "observer si la production continue ou s'arrête.",
                width=56,
            ),
            font_size=24,
            color=WHITE,
        )
        intro.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Nous savons maintenant quels gaz sont échangés. Il reste "
                "à comprendre de quoi le végétal a besoin pour fabriquer "
                "sa matière. La stratégie des biologistes est toujours la "
                "même : supprimer un seul facteur à la fois, et observer "
                "si la production de matière continue ou s'arrête. Mais "
                "d'abord, comment repérer que de la matière organique a "
                "été produite ?"
            )
        ) as tracker:
            self.play(Write(titre))
            self.play(FadeIn(intro))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(intro))

        # --- Raisonnement : le témoin de la production, l'amidon --------
        with self.voiceover(
            text=(
                "Dans les feuilles, une grande partie de la matière "
                "organique fabriquée est stockée sous forme d'amidon, un "
                "glucide de réserve. Or l'amidon possède un test "
                "d'identification simple."
            )
        ) as tracker:
            self.wait(tracker.get_remaining_duration())

        # --- Propriété : le test à l'eau iodée ----------------------------
        propriete = property_box(
            Text(
                _wrap(
                    "L'eau iodée est une solution jaune-brun. En présence "
                    "d'amidon, elle devient bleu-noir (violet très foncé). "
                    "Ce test permet de savoir si une feuille a produit de "
                    "la matière organique.",
                    width=54,
                ),
                font_size=22,
            ),
            box_width=11.5,
        )
        propriete.to_edge(LEFT, buff=0.5).shift(UP * 0.3)

        pastille_avant = _pastille(YELLOW, "eau iodée\n(sans amidon)")
        pastille_apres = _pastille("#0D1B4C", "eau iodée\n(avec amidon)")
        fleche = Arrow(LEFT, RIGHT, color=WHITE, buff=0.1).scale(0.6)
        pastilles = VGroup(pastille_avant, fleche, pastille_apres).arrange(RIGHT, buff=0.3)
        pastilles.next_to(propriete, RIGHT, buff=0.4)

        groupe = VGroup(propriete, pastilles)
        groupe.move_to(ORIGIN).next_to(titre, DOWN, buff=0.5)
        _fit(groupe, titre.get_bottom()[1] - 0.3)

        with self.voiceover(
            text=(
                "L'eau iodée est une solution jaune-brun. En présence "
                "d'amidon, elle devient bleu-noir, un violet très foncé. "
                "Ce test permet donc de savoir si une feuille a produit de "
                "la matière organique."
            )
        ) as tracker:
            self.play(FadeIn(propriete))
            self.play(FadeIn(pastilles))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(groupe))

        # --- Protocole de décoloration -------------------------------------
        etapes_decoloration = _bullets(
            [
                "1. Eau bouillante quelques minutes : tue et ramollit la "
                "feuille.",
                "2. Alcool chauffé au bain-marie : dissout la chlorophylle "
                "verte.",
                "3. La feuille devient blanchâtre, prête pour le test à "
                "l'eau iodée.",
            ],
            font_size=21,
            width=54,
        )
        propriete_decoloration = property_box(etapes_decoloration, box_width=11.8)
        propriete_decoloration.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Avant le test, la feuille doit être décolorée, sinon le "
                "vert de la chlorophylle masque le bleu-noir. On la plonge "
                "d'abord quelques minutes dans l'eau bouillante, pour la "
                "tuer et la ramollir, puis dans l'alcool chauffé au "
                "bain-marie, pour dissoudre la chlorophylle. La feuille "
                "devient blanchâtre et peut alors être mise en contact "
                "avec l'eau iodée. Attention à la sécurité : l'alcool est "
                "inflammable, on ne le chauffe jamais directement sur la "
                "flamme, toujours au bain-marie."
            )
        ) as tracker:
            self.play(FadeIn(propriete_decoloration))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(propriete_decoloration))

        # --- À retenir : méthode générale en cinq étapes ---------------------
        methode = method_box(
            _bullets(
                [
                    "Étape 1 : éliminer l'amidon de réserve (48 h à "
                    "l'obscurité).",
                    "Étape 2 : réaliser deux situations identiques sauf "
                    "pour le facteur étudié (situation + témoin).",
                    "Étape 3 : exposer à la lumière quelques heures.",
                    "Étape 4 : décolorer les feuilles et tester à l'eau "
                    "iodée.",
                    "Étape 5 : comparer les colorations et conclure.",
                ],
                font_size=20,
                width=54,
            ),
            box_width=11.9,
        )
        methode.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Voici la méthode générale pour rédiger le protocole d'une "
                "expérience de mise en évidence d'un facteur, comme la "
                "lumière, la chlorophylle ou le CO2. Étape un : éliminer "
                "l'amidon de réserve, en laissant la plante quarante-huit "
                "heures à l'obscurité. Étape deux : réaliser deux "
                "situations identiques, sauf pour le facteur étudié, une "
                "situation expérimentale et un témoin. Étape trois : "
                "exposer à la lumière pendant quelques heures. Étape "
                "quatre : décolorer les feuilles, eau bouillante puis "
                "alcool au bain-marie, et tester à l'eau iodée. Étape "
                "cinq : comparer les colorations et conclure : si le "
                "bleu-noir n'apparaît que lorsque le facteur est présent, "
                "ce facteur est indispensable."
            )
        ) as tracker:
            self.play(FadeIn(methode))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(titre), FadeOut(methode))
