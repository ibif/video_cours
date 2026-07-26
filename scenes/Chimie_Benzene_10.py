"""
scenes/Chimie_Benzene_10.py — Chapitre 4 (1ereC, Chimie), scène 10.

§ Usages et toxicité du benzène : usages industriels (styrène, phénol,
cyclohexane → nylon, colorants/médicaments via l'aniline, détergents,
pesticides, explosifs). property_box toxicité (cancérogène, mutagène,
atteintes du sang). Règles de sécurité (sorbonne, gants/lunettes/blouse,
pas de flamme, remplacement par toluène/cyclohexane en labo). Enjeu
environnemental (SIR, stations-service).
Source : 1ereC/Chimie.pdf, chapitre 4, pages 43-44.
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
    FadeIn,
    FadeOut,
    Text,
    VGroup,
    Write,
    config,
)

from shapes.base_scene import NotionScene
from shapes.boxes import property_box, scene_title


def _wrap(text: str, width: int = 56) -> str:
    return "\n".join(textwrap.fill(line, width=width) for line in text.split("\n"))


def _fit(mobject, top_y):
    bas_visible = -config.frame_height / 2 + 0.25
    hauteur_dispo = top_y - bas_visible
    if mobject.height > hauteur_dispo:
        mobject.scale(hauteur_dispo / mobject.height, about_point=mobject.get_top())
    return mobject


def _bullets(items, font_size=22, color=WHITE, width=52):
    lines = VGroup(
        *[Text(f"• {_wrap(it, width=width)}", font_size=font_size, color=color) for it in items]
    )
    lines.arrange(DOWN, aligned_edge=LEFT, buff=0.22)
    return lines


class UsagesToxiciteBenzene(NotionScene):
    def construct(self):
        titre = scene_title("10. Usages et toxicité du benzène")
        titre.scale(0.55)
        titre.to_edge(UP)

        # --- Énoncé : le benzène, matière première industrielle majeure --------
        enonce = Text(
            _wrap(
                "Revenons à la SIR d'Abidjan : le benzène extrait du "
                "pétrole n'est presque jamais utilisé tel quel. C'est "
                "avant tout une matière première pour une multitude de "
                "synthèses industrielles.",
                width=54,
            ),
            font_size=24,
            color=WHITE,
        )
        enonce.next_to(titre, DOWN, buff=0.5)
        _fit(enonce, titre.get_bottom()[1] - 0.4)

        with self.voiceover(
            text=(
                "Revenons à la Société Ivoirienne de Raffinage d'Abidjan, "
                "évoquée en introduction. Le benzène extrait du pétrole "
                "n'est presque jamais utilisé tel quel : c'est avant "
                "tout une matière première pour une multitude de "
                "synthèses industrielles."
            )
        ) as tracker:
            self.play(Write(titre))
            self.play(FadeIn(enonce))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(enonce))

        # --- Animation du raisonnement : les usages industriels -------------------
        entete = Text("Les usages industriels du benzène", font_size=24, color=YELLOW, weight="BOLD")
        entete.next_to(titre, DOWN, buff=0.35)

        usages = _bullets(
            [
                "Styrène → fabrication des matières plastiques (polystyrène)",
                "Phénol → résines, désinfectants",
                "Cyclohexane (par hydrogénation) → fibres de nylon",
                "Aniline (via nitrobenzène) → colorants, médicaments",
                "Détergents, pesticides, explosifs",
            ],
            font_size=21,
            width=54,
        )
        usages.next_to(entete, DOWN, buff=0.35)
        groupe_usages = VGroup(entete, usages)
        _fit(groupe_usages, titre.get_bottom()[1] - 0.35)

        with self.voiceover(
            text=(
                "Le benzène permet de synthétiser le styrène, à la base "
                "des matières plastiques comme le polystyrène ; le "
                "phénol, utilisé dans les résines et les désinfectants ; "
                "le cyclohexane, par hydrogénation, qui sert à fabriquer "
                "les fibres de nylon ; et l'aniline, obtenue via le "
                "nitrobenzène étudié précédemment, matière première des "
                "colorants et de nombreux médicaments. On le retrouve "
                "aussi dans la fabrication de détergents, de pesticides "
                "et d'explosifs."
            )
        ) as tracker:
            self.play(FadeIn(entete))
            self.play(FadeIn(usages))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(groupe_usages))

        # --- Exemple traité : property_box toxicité --------------------------------
        toxicite = property_box(
            Text(
                _wrap(
                    "Le benzène est TOXIQUE : il est cancérogène (risque "
                    "de leucémie), mutagène, et provoque des atteintes du "
                    "sang et de la moelle osseuse en cas d'exposition "
                    "répétée, même à faible dose.",
                    width=48,
                ),
                font_size=24,
            ),
        )
        toxicite.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Mais cette utilité industrielle a un revers grave : le "
                "benzène est toxique. Il est cancérogène, avec un risque "
                "avéré de leucémie, il est mutagène, et il provoque des "
                "atteintes du sang et de la moelle osseuse en cas "
                "d'exposition répétée, même à faible dose."
            )
        ) as tracker:
            self.play(FadeIn(toxicite))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(toxicite))

        # --- À retenir : règles de sécurité + enjeu environnemental ---------------
        entete2 = Text("Sécurité au laboratoire et enjeu environnemental", font_size=20, color=YELLOW, weight="BOLD")
        entete2.next_to(titre, DOWN, buff=0.35)

        securite = _bullets(
            [
                "Toujours manipuler sous sorbonne (hotte aspirante)",
                "Porter gants, lunettes et blouse",
                "Ne jamais approcher de flamme (très inflammable)",
                "En classe : remplacer le benzène par du toluène ou du "
                "cyclohexane, bien moins toxiques",
                "Enjeu environnemental : surveiller les rejets autour de "
                "la SIR et des stations-service (vapeurs de benzène)",
            ],
            font_size=19,
            width=56,
        )
        securite.next_to(entete2, DOWN, buff=0.3)
        groupe2 = VGroup(entete2, securite)
        _fit(groupe2, titre.get_bottom()[1] - 0.35)

        with self.voiceover(
            text=(
                "C'est pourquoi des règles de sécurité strictes "
                "s'imposent : toujours manipuler le benzène sous "
                "sorbonne, porter gants, lunettes et blouse, et ne "
                "jamais l'approcher d'une flamme, puisqu'il est très "
                "inflammable. En classe, on préfère d'ailleurs le "
                "remplacer par du toluène ou du cyclohexane, bien moins "
                "toxiques. Cet enjeu dépasse le laboratoire : autour de "
                "la SIR d'Abidjan comme à proximité des stations-service, "
                "la surveillance des vapeurs de benzène rejetées dans "
                "l'air constitue un véritable enjeu de santé publique et "
                "environnemental."
            )
        ) as tracker:
            self.play(FadeIn(entete2))
            self.play(FadeIn(securite))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(groupe2), FadeOut(titre))
