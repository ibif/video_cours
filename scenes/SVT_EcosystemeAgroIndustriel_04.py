"""
scenes/SVT_EcosystemeAgroIndustriel_04.py — Chapitre 11 (1ereC, SVT), scène 04.

§ 2.2 La savane, exemple de la station de Lamto : biotope (climat
tropical, saison sèche, sols sableux), biocénose (strate herbacée
continue, faune herbivore/carnivore/décomposeurs), et le facteur
écologique particulier des feux de brousse annuels.
Source : 1ereC/SVT.pdf, page 122.
"""

import textwrap

from manim import DOWN, LEFT, UP, WHITE, YELLOW, FadeIn, FadeOut, Text, VGroup, Write, config

from shapes.base_scene import NotionScene
from shapes.boxes import property_box, scene_title


def _wrap(text: str, width: int = 56) -> str:
    return "\n".join(textwrap.fill(line, width=width) for line in text.split("\n"))


def _bullets(items, font_size=23, color=WHITE, width=52):
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


class LaSavaneDeLamto(NotionScene):
    def construct(self):
        titre = scene_title("2.2 — La savane : la station de Lamto")
        titre.scale(0.62)
        titre.to_edge(UP)

        # --- Énoncé --------------------------------------------------------
        intro = Text(
            _wrap(
                "La savane occupe le centre et le nord de la Côte "
                "d'Ivoire. La station d'écologie tropicale de Lamto, au "
                "bord de la Bandama, entre Tiassalé et Taabo, est un site "
                "d'étude de référence mondiale.",
                width=56,
            ),
            font_size=24,
            color=WHITE,
        )
        intro.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Deuxième écosystème naturel : la savane, qui occupe le "
                "centre et le nord de la Côte d'Ivoire. La station "
                "d'écologie tropicale de Lamto, au bord de la Bandama, "
                "entre Tiassalé et Taabo, est un site d'étude de référence "
                "mondiale."
            )
        ) as tracker:
            self.play(Write(titre))
            self.play(FadeIn(intro))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(intro))

        # --- Raisonnement : biotope + biocénose -----------------------------
        biotope = property_box(
            Text(
                _wrap(
                    "Biotope : climat tropical de transition, saison sèche "
                    "marquée (novembre à mars), pluies de 1100 à "
                    "1300 mm/an, sols sableux pauvres.",
                    width=54,
                ),
                font_size=22,
            ),
            box_width=11.5,
        )
        biotope.next_to(titre, DOWN, buff=0.45)

        with self.voiceover(
            text=(
                "Le biotope de Lamto se caractérise par un climat "
                "tropical de transition, avec une saison sèche marquée, de "
                "novembre à mars, des pluies de mille cent à mille trois "
                "cents millimètres par an, et des sols sableux pauvres."
            )
        ) as tracker:
            self.play(FadeIn(biotope))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(biotope))

        bioceno_titre = Text("Biocénose : une strate herbacée continue", font_size=24, color=YELLOW, weight="BOLD")
        bioceno_titre.next_to(titre, DOWN, buff=0.45)
        bioceno = _bullets(
            [
                "Graminées hautes (Loudetia, Andropogon), parsemées d'arbres : palmier rônier, karité, néré.",
                "Herbivores : sauterelles, termites, rongeurs, antilopes cob de Buffon.",
                "Carnivores : lézards, serpents, oiseaux rapaces.",
                "Intense activité de décomposeurs et détritivores : termites, vers, bactéries, champignons.",
            ],
            font_size=20,
            width=58,
        )
        bioceno.next_to(bioceno_titre, DOWN, buff=0.35)
        groupe_bioceno = VGroup(bioceno_titre, bioceno)
        _fit(groupe_bioceno, titre.get_bottom()[1] - 0.25)

        with self.voiceover(
            text=(
                "La biocénose est dominée par une strate herbacée "
                "continue, de hautes graminées comme le Loudetia ou "
                "l'Andropogon, parsemée d'arbres et d'arbustes : le "
                "palmier rônier, le karité, le néré. La faune comprend des "
                "herbivores, sauterelles, termites, rongeurs, antilopes "
                "cob de Buffon ; des carnivores, lézards, serpents, "
                "oiseaux rapaces ; et une intense activité de "
                "décomposeurs et de détritivores : termites, vers, "
                "bactéries, champignons."
            )
        ) as tracker:
            self.play(FadeIn(bioceno_titre))
            self.play(FadeIn(bioceno))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(bioceno_titre), FadeOut(bioceno))

        # --- Exemple traité : le facteur écologique des feux de brousse -----
        feux = property_box(
            Text(
                _wrap(
                    "Facteur écologique particulier : les feux de brousse "
                    "annuels détruisent la strate herbacée sèche, mais "
                    "leurs cendres restituent des sels minéraux au sol.",
                    width=54,
                ),
                font_size=22,
            ),
            box_width=11.8,
        )
        feux.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "La savane de Lamto se distingue par un facteur "
                "écologique particulier : les feux de brousse annuels, "
                "généralement en début de saison sèche, détruisent la "
                "strate herbacée devenue sèche et inflammable. Mais leurs "
                "cendres restituent des sels minéraux au sol, ce qui "
                "favorise la repousse dès les premières pluies. Le feu "
                "fait donc partie intégrante du fonctionnement normal de "
                "cet écosystème."
            )
        ) as tracker:
            self.play(FadeIn(feux))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(feux))

        # --- À retenir -------------------------------------------------------
        retenir_titre = Text("À retenir", font_size=26, color=YELLOW, weight="BOLD")
        retenir_titre.next_to(titre, DOWN, buff=0.5)
        retenir = _bullets(
            [
                "La savane est un écosystème herbacé, adapté à une saison sèche marquée.",
                "Elle abrite une chaîne alimentaire complète : herbivores, carnivores, décomposeurs.",
                "Les feux de brousse, loin d'être uniquement destructeurs, participent au recyclage minéral.",
            ],
            font_size=21,
            width=54,
        )
        retenir.next_to(retenir_titre, DOWN, buff=0.35)

        with self.voiceover(
            text=(
                "Retenons : la savane est un écosystème herbacé, adapté à "
                "une saison sèche marquée, qui abrite une chaîne "
                "alimentaire complète, des herbivores aux décomposeurs. "
                "Les feux de brousse, loin d'être uniquement destructeurs, "
                "participent au recyclage minéral du sol."
            )
        ) as tracker:
            self.play(FadeIn(retenir_titre))
            self.play(FadeIn(retenir))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(titre), FadeOut(retenir_titre), FadeOut(retenir))
