"""
scenes/Physique_LentillesMinces_07.py — Chapitre 13 « Les lentilles minces »
(1ereC, Physique), scène 07.

§ Tableau récapitulatif des positions image (lentille convergente, objet
réel) : à l'infini → image en F' ; au-delà de 2F → image réelle renversée
plus petite ; en 2F → même taille ; entre F et 2F → agrandie ; en F →
rejetée à l'infini ; entre F et O → virtuelle droite agrandie (cas de la
loupe). Propriété du sens de déplacement (objet et image réelle se
déplacent dans le même sens).
Source : 1ereC/Physique.pdf, pages 130-140 (chapitre 13, § 3).
"""

import textwrap

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
    Text,
    VGroup,
    Write,
)

from shapes.base_scene import NotionScene
from shapes.boxes import essentiel_box, example_box, property_box, scene_title, warning_box


def _wrap(text: str, width: int = 56) -> str:
    return "\n".join(textwrap.fill(line, width=width) for line in text.split("\n"))


def _ligne_tableau(position: str, resultat: str, color=WHITE) -> VGroup:
    gauche = Text(position, font_size=18, weight="BOLD")
    fleche = Text("→", font_size=18)
    droite = Text(resultat, font_size=18, color=color)
    ligne = VGroup(gauche, fleche, droite).arrange(RIGHT, buff=0.25)
    return ligne


class TableauPositionsImage(NotionScene):
    def construct(self):
        titre = scene_title("Tableau des positions de l'image (lentille convergente)")
        titre.scale(0.34)
        titre.to_edge(UP)
        self.play(Write(titre))

        # --- Énoncé -----------------------------------------------------------------
        enonce = Text(
            _wrap(
                "Pour une lentille convergente et un objet réel, la "
                "nature, le sens et la taille de l'image dépendent "
                "entièrement de la position de l'objet par rapport à F "
                "et 2F. Récapitulons tous les cas.",
                width=52,
            ),
            font_size=21,
        )
        enonce.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Pour une lentille convergente et un objet réel, la "
                "nature, le sens et la taille de l'image dépendent "
                "entièrement de la position de l'objet par rapport à F et "
                "à 2F. Récapitulons tous les cas possibles."
            )
        ) as tracker:
            self.play(FadeIn(enonce))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(enonce))

        # --- Raisonnement : le tableau -----------------------------------------------
        lignes = VGroup(
            _ligne_tableau("objet à l'infini", "image ponctuelle en F'", YELLOW),
            _ligne_tableau("au-delà de 2F", "réelle, renversée, plus petite", WHITE),
            _ligne_tableau("exactement en 2F", "réelle, renversée, même taille", WHITE),
            _ligne_tableau("entre F et 2F", "réelle, renversée, agrandie", WHITE),
            _ligne_tableau("exactement en F", "image rejetée à l'infini", YELLOW),
            _ligne_tableau("entre F et O", "virtuelle, droite, agrandie (loupe)", BLUE),
        ).arrange(DOWN, buff=0.22, aligned_edge=LEFT)
        lignes.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Quand l'objet est à l'infini, l'image est ponctuelle, "
                "en F prime. Au-delà de 2F, l'image est réelle, "
                "renversée, et plus petite que l'objet. Exactement en "
                "2F, l'image est réelle, renversée, de même taille. Entre "
                "F et 2F, elle est réelle, renversée, mais agrandie. "
                "Exactement en F, l'image est rejetée à l'infini. Et "
                "entre F et O, l'objet étant plus proche de la lentille "
                "que le foyer, l'image devient virtuelle, droite, et "
                "agrandie : c'est exactement le principe de la loupe."
            )
        ) as tracker:
            for ligne in lignes:
                self.play(Write(ligne), run_time=0.9)
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(lignes))

        # --- Propriété : sens de déplacement -----------------------------------------
        propriete = property_box(
            VGroup(
                Text("Sens de déplacement", font_size=22, weight="BOLD"),
                Text("Tant que l'objet et l'image sont tous deux réels,", font_size=19),
                Text("ils se déplacent dans le MÊME SENS :", font_size=19),
                Text("objet et image se rapprochent - ou s'éloignent -", font_size=19),
                Text("simultanément de la lentille.", font_size=19),
            ).arrange(DOWN, buff=0.18, aligned_edge=LEFT),
            box_width=11.4,
        )
        propriete.next_to(titre, DOWN, buff=0.45)

        with self.voiceover(
            text=(
                "Propriété utile : tant que l'objet et l'image restent "
                "tous les deux réels, ils se déplacent dans le même sens. "
                "Autrement dit, objet et image se rapprochent, ou "
                "s'éloignent, simultanément de la lentille."
            )
        ) as tracker:
            self.play(FadeIn(propriete))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(propriete))

        # --- Exemple --------------------------------------------------------------------
        exemple = example_box(
            VGroup(
                Text("Une lentille convergente a f' = 5 cm.", font_size=20),
                Text("Un objet placé à 20 cm (au-delà de 2F = 10 cm) donne", font_size=20),
                Text("une image réelle, renversée, plus petite que l'objet.", font_size=20),
            ).arrange(DOWN, buff=0.18, aligned_edge=LEFT),
            box_width=11.6,
        )
        exemple.next_to(titre, DOWN, buff=0.45)

        with self.voiceover(
            text=(
                "Exemple : une lentille convergente de distance focale 5 "
                "centimètres a 2F situé à 10 centimètres. Un objet placé "
                "à 20 centimètres, donc au-delà de 2F, donne une image "
                "réelle, renversée, et plus petite que l'objet."
            )
        ) as tracker:
            self.play(FadeIn(exemple))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(exemple))

        # --- À retenir --------------------------------------------------------------
        retenir = essentiel_box(
            VGroup(
                Text("À retenir", font_size=23, weight="BOLD"),
                Text("Objet au-delà de F : image réelle, renversée", font_size=18),
                Text("(taille selon la position par rapport à 2F).", font_size=18),
                Text("Objet entre F et O : image virtuelle, droite,", font_size=18),
                Text("agrandie — c'est la loupe.", font_size=18),
            ).arrange(DOWN, buff=0.14, aligned_edge=LEFT),
            box_width=11.4,
        )
        retenir.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Retenons l'essentiel : pour un objet réel au-delà de F, "
                "l'image est toujours réelle et renversée, sa taille "
                "dépendant de la position par rapport à 2F. Pour un objet "
                "entre F et O, l'image devient virtuelle, droite et "
                "agrandie : c'est exactement le principe de la loupe."
            )
        ) as tracker:
            self.play(FadeIn(retenir))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(retenir))

        # --- Piège --------------------------------------------------------------------
        piege = warning_box(
            VGroup(
                Text("• Un objet réel devant une lentille CONVERGENTE ne", font_size=19),
                Text("   donne pas toujours une image réelle : entre F et", font_size=19),
                Text("   O, elle est virtuelle (piège fréquent).", font_size=19),
                Text("• « En F » n'est pas « pas d'image » : l'image existe,", font_size=19),
                Text("   simplement rejetée à l'infini (rayons émergents", font_size=19),
                Text("   parallèles entre eux).", font_size=19),
            ).arrange(DOWN, aligned_edge=LEFT, buff=0.12),
            box_width=12.0,
        )
        piege.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Piège fréquent : un objet réel devant une lentille "
                "convergente ne donne pas toujours une image réelle. "
                "Entre F et O, l'image est virtuelle. Et « objet en F » "
                "ne veut pas dire qu'il n'y a pas d'image : l'image "
                "existe bel et bien, simplement rejetée à l'infini, les "
                "rayons émergents devenant parallèles entre eux."
            )
        ) as tracker:
            self.play(FadeIn(piege))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(piege), FadeOut(titre))
