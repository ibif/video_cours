"""
scenes/SVT_EvolutionSolsTropicaux_03.py — Chapitre 9 (1ereD, SVT), scène 03.

§ 9.2 Le profil d'un sol : la succession des horizons — définition
horizon/profil, les 6 horizons O-A-E-B-C-R (schéma en pile), exemple de
reconstitution d'un profil près de Daloa, méthode pour décrire un profil,
attention : tous les horizons ne sont pas toujours présents. Source :
1ereD/SVT.pdf, pages 117-118.
"""

import textwrap

from manim import (
    DOWN,
    LEFT,
    RIGHT,
    UP,
    WHITE,
    YELLOW,
    FadeIn,
    FadeOut,
    Rectangle,
    Text,
    VGroup,
    Write,
    config,
)

from shapes.base_scene import NotionScene
from shapes.boxes import definition_box, example_box, method_box, scene_title, warning_box

HORIZON_COLORS = {
    "O": "#3B2A1A",
    "A": "#5B3A29",
    "E": "#C9C0B0",
    "B": "#B5451B",
    "C": "#8A7A63",
    "R": "#5A5A5A",
}


def _wrap(text: str, width: int = 56) -> str:
    return "\n".join(textwrap.fill(line, width=width) for line in text.split("\n"))


def _bullets(items, font_size=23, color=WHITE, width=52):
    lines = VGroup(
        *[Text(f"• {_wrap(it, width=width)}", font_size=font_size, color=color) for it in items]
    )
    lines.arrange(DOWN, aligned_edge=LEFT, buff=0.22)
    return lines


def _horizon_pile():
    """Construit la pile verticale des 6 horizons O-A-E-B-C-R, chacun avec
    sa légende à droite (schéma le plus important du chapitre)."""
    donnees = [
        ("O", "Litière : restes végétaux visibles", 0.5),
        ("A", "Humifère, brun sombre, départ du lessivage", 0.8),
        ("E", "Grisâtre, lessivage maximal (souvent absent)", 0.5),
        ("B", "Accumulation : argiles, fer, aluminium (rouge/ocre)", 1.0),
        ("C", "Roche altérée sur place (altérites)", 0.9),
        ("R", "Roche mère saine, non altérée", 0.8),
    ]
    blocs = VGroup()
    legendes = VGroup()
    largeur = 2.4
    for nom, description, hauteur in donnees:
        rect = Rectangle(
            width=largeur,
            height=hauteur,
            fill_color=HORIZON_COLORS[nom],
            fill_opacity=1.0,
            stroke_color=WHITE,
            stroke_width=1.5,
        )
        etiquette = Text(nom, font_size=24, color=WHITE, weight="BOLD")
        etiquette.move_to(rect.get_center())
        bloc = VGroup(rect, etiquette)
        blocs.add(bloc)

        legende = Text(f"Horizon {nom} — {description}", font_size=17, color=WHITE)
        legendes.add(legende)

    blocs.arrange(DOWN, buff=0)
    for bloc, legende in zip(blocs, legendes):
        legende.next_to(bloc, RIGHT, buff=0.35)

    return VGroup(blocs, legendes)


class LeProfilDuSolLesHorizons(NotionScene):
    def construct(self):
        titre = scene_title("9.2 — Le profil d'un sol : les horizons")
        titre.scale(0.65)
        titre.to_edge(UP)

        # --- Énoncé : définition horizon / profil ----------------------------
        intro = Text(
            _wrap(
                "Une tranchée verticale révèle des couches superposées de "
                "couleurs et de textures différentes.",
                width=56,
            ),
            font_size=25,
            color=WHITE,
        )
        intro.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Quand on creuse une tranchée verticale dans le sol, on "
                "découvre des couches superposées, de couleurs et de "
                "textures différentes."
            )
        ) as tracker:
            self.play(Write(titre))
            self.play(FadeIn(intro))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(intro))

        definition = definition_box(
            Text(
                _wrap(
                    "Un horizon est une couche de sol à peu près "
                    "horizontale, aux caractères propres (couleur, "
                    "texture, structure, composition). Le profil est la "
                    "succession verticale des horizons, de la surface à la "
                    "roche mère.",
                    width=54,
                ),
                font_size=23,
            ),
            box_width=12.0,
        )
        definition.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Un horizon est une couche de sol à peu près horizontale, "
                "aux caractères propres : couleur, texture, structure, "
                "composition. Le profil est la succession verticale de ces "
                "horizons, de la surface jusqu'à la roche mère."
            )
        ) as tracker:
            self.play(FadeIn(definition))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(definition))

        # --- Animation du raisonnement : la pile des horizons ----------------
        entete_pile = Text("Les horizons d'un sol évolué", font_size=26, color=YELLOW, weight="BOLD")
        entete_pile.to_edge(UP).shift(DOWN * 0.9)

        pile = _horizon_pile()
        pile.scale(0.85)
        pile.next_to(entete_pile, DOWN, buff=0.35)

        with self.voiceover(
            text=(
                "Voici, de haut en bas, les horizons d'un sol évolué. "
                "L'horizon O, la litière, formée de restes végétaux plus ou "
                "moins décomposés. L'horizon A, minéral et sombre, enrichi "
                "en humus, où commence le lessivage. L'horizon E, souvent "
                "absent sous les tropiques, appauvri et décoloré, très "
                "lessivé. L'horizon B, zone d'accumulation : argiles, "
                "oxydes de fer et d'aluminium, souvent rouge ou ocre, "
                "compact. L'horizon C, la roche mère altérée sur place, "
                "désagrégée, qu'on appelle les altérites. Et enfin "
                "l'horizon R, la roche mère saine, non altérée."
            )
        ) as tracker:
            self.play(FadeIn(entete_pile))
            for bloc, legende in zip(pile[0], pile[1]):
                self.play(FadeIn(bloc), FadeIn(legende), run_time=0.6)
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(entete_pile), FadeOut(pile))

        # --- Exemple traité : reconstituer un profil (Daloa) -----------------
        exemple = example_box(
            Text(
                _wrap(
                    "Près de Daloa, des élèves observent une carrière et "
                    "notent dans le désordre : (1) fragments de granite "
                    "friables ; (2) couche rouge vif, riche en graviers "
                    "ferrugineux ; (3) terre brun sombre souple pleine de "
                    "racines ; (4) granite dur et sain ; (5) tapis de "
                    "feuilles mortes en décomposition. Résolution : "
                    "(5)=O ; (3)=A ; (2)=B ; (1)=C ; (4)=R. Ordre : "
                    "5,3,2,1,4 soit O,A,B,C,R.",
                    width=54,
                ),
                font_size=19,
            ),
            box_width=12.2,
        )
        exemple.next_to(titre, DOWN, buff=0.45)

        _bas_visible = -config.frame_height / 2 + 0.3
        _hauteur_dispo = exemple.get_top()[1] - _bas_visible
        if exemple.height > _hauteur_dispo:
            exemple.scale(_hauteur_dispo / exemple.height, about_point=exemple.get_top())

        with self.voiceover(
            text=(
                "Exemple traité : près de Daloa, des élèves observent une "
                "carrière et notent, dans le désordre, cinq éléments. Un, "
                "des fragments de granite friables et reconnaissables. "
                "Deux, une couche rouge vif, riche en graviers "
                "ferrugineux. Trois, une terre brun sombre, souple, pleine "
                "de racines. Quatre, du granite dur et sain. Cinq, un tapis "
                "de feuilles mortes en décomposition. Résolution : le "
                "cinq, la litière, correspond à l'horizon O. Le trois, "
                "riche en humus et en racines, correspond à l'horizon A. "
                "Le deux, zone d'accumulation ferrugineuse, correspond à "
                "l'horizon B. Le un, roche altérée, correspond à l'horizon "
                "C. Et le quatre, roche mère saine, correspond à "
                "l'horizon R. L'ordre du profil est donc cinq, trois, deux, "
                "un, quatre, soit O, A, B, C, R."
            )
        ) as tracker:
            self.play(FadeIn(exemple))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(exemple))

        # --- À retenir : méthode pour décrire un profil -----------------------
        methode = method_box(
            _bullets(
                [
                    "Creuser une tranchée verticale (ou choisir une paroi naturelle fraîche).",
                    "Nettoyer et laisser sécher pour mieux voir les couleurs.",
                    "Repérer les changements de couleur, texture, structure : limites des horizons.",
                    "Mesurer l'épaisseur de chaque horizon, prélever un échantillon.",
                    "Dessiner un schéma légendé.",
                ],
                font_size=19,
                width=48,
            ),
            box_width=12.2,
        )
        methode.next_to(titre, DOWN, buff=0.45)

        _hauteur_dispo2 = methode.get_top()[1] - _bas_visible
        if methode.height > _hauteur_dispo2:
            methode.scale(_hauteur_dispo2 / methode.height, about_point=methode.get_top())

        with self.voiceover(
            text=(
                "Méthode pour décrire le profil d'un sol, en cinq étapes. "
                "Un, creuser une tranchée verticale, ou choisir une paroi "
                "naturelle fraîche. Deux, nettoyer et laisser sécher pour "
                "mieux voir les couleurs. Trois, repérer les changements de "
                "couleur, de texture et de structure : ce sont les limites "
                "des horizons. Quatre, mesurer l'épaisseur de chaque "
                "horizon et prélever un échantillon. Cinq, dessiner un "
                "schéma légendé."
            )
        ) as tracker:
            self.play(FadeIn(methode))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(methode))

        # --- Piège à éviter ------------------------------------------------------
        piege = warning_box(
            Text(
                _wrap(
                    "Tous les horizons ne sont pas toujours présents. Le "
                    "profil complet O-A-E-B-C-R est un modèle : l'horizon E "
                    "est rare sous les tropiques ; un sol jeune sur versant "
                    "peut se résumer à A-C-R ; un sol de bas-fond diffère "
                    "d'un sol de plateau. Décrire d'abord ce qu'on voit, "
                    "puis comparer au modèle.",
                    width=54,
                ),
                font_size=22,
            ),
            box_width=12.0,
        )
        piege.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Attention, tous les horizons ne sont pas toujours "
                "présents. Le profil complet O, A, E, B, C, R n'est qu'un "
                "modèle : l'horizon E est rare sous les tropiques, un sol "
                "jeune sur un versant peut se résumer à A, C, R, et un sol "
                "de bas-fond diffère d'un sol de plateau. La bonne méthode "
                "consiste à décrire d'abord ce que l'on observe réellement, "
                "puis à comparer ensuite au modèle."
            )
        ) as tracker:
            self.play(FadeIn(piege))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(titre), FadeOut(piege))
