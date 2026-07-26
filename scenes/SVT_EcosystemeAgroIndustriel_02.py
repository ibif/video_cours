"""
scenes/SVT_EcosystemeAgroIndustriel_02.py — Chapitre 11 (1ereC, SVT), scène 02.

§ 1.3-1.5 Définition de la biocénose (populations en relation :
prédation/compétition/coopération/parasitisme), définition de la
population, définition de la station, tableau récapitulatif des 4 notions
avec exemples ivoiriens, et méthode « l'écosystème n'a pas de taille
fixe ». Source : 1ereC/SVT.pdf, pages 120-121.
"""

import textwrap

from manim import DOWN, LEFT, UP, WHITE, YELLOW, FadeIn, FadeOut, Text, VGroup, Write, config

from shapes.base_scene import NotionScene
from shapes.boxes import definition_box, method_box, scene_title


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


class DefinitionBiocenoseEtStation(NotionScene):
    def construct(self):
        titre = scene_title("1.3-1.5 — Biocénose, population et station")
        titre.scale(0.62)
        titre.to_edge(UP)

        # --- Énoncé : la biocénose, les acteurs de la pièce ----------------
        intro = Text(
            _wrap(
                "Le biotope est le théâtre. Reste à présenter les acteurs "
                "de la pièce qui s'y joue : la biocénose, et les relations "
                "qu'ils entretiennent entre eux.",
                width=56,
            ),
            font_size=24,
            color=WHITE,
        )
        intro.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Le biotope est le théâtre. Il reste à présenter les "
                "acteurs de la pièce qui s'y joue : la biocénose, et les "
                "relations qu'ils entretiennent entre eux."
            )
        ) as tracker:
            self.play(Write(titre))
            self.play(FadeIn(intro))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(intro))

        # --- Raisonnement : définition de la biocénose + relations --------
        bioceno_def = definition_box(
            Text(
                _wrap(
                    "La biocénose est l'ensemble des populations d'êtres "
                    "vivants (végétaux, animaux, champignons, "
                    "micro-organismes) qui vivent dans un biotope donné et "
                    "qui sont en relation les unes avec les autres.",
                    width=54,
                ),
                font_size=21,
            ),
            box_width=11.8,
        )
        bioceno_def.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "La biocénose est l'ensemble des populations d'êtres "
                "vivants, végétaux, animaux, champignons, "
                "micro-organismes, qui vivent dans un biotope donné et qui "
                "sont en relation les unes avec les autres."
            )
        ) as tracker:
            self.play(FadeIn(bioceno_def))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(bioceno_def))

        relations_titre = Text("Les 4 types de relations entre populations", font_size=25, color=YELLOW, weight="BOLD")
        relations_titre.next_to(titre, DOWN, buff=0.45)
        relations = _bullets(
            [
                "Prédation : manger / être mangé.",
                "Compétition : se disputer la même ressource.",
                "Coopération et symbiose : s'entraider.",
                "Parasitisme : vivre aux dépens d'un hôte.",
            ],
            font_size=23,
            width=48,
        )
        relations.next_to(relations_titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Les relations entre ces acteurs sont de plusieurs types. "
                "La prédation : manger, ou être mangé. La compétition : se "
                "disputer la même ressource, nourriture, espace ou "
                "lumière. La coopération et la symbiose : s'entraider. Et "
                "le parasitisme : vivre aux dépens d'un hôte."
            )
        ) as tracker:
            self.play(FadeIn(relations_titre))
            self.play(FadeIn(relations))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(relations_titre), FadeOut(relations))

        pop_def = definition_box(
            Text(
                _wrap(
                    "Une population est l'ensemble des individus d'une "
                    "même espèce vivant au même moment dans un même lieu.",
                    width=52,
                ),
                font_size=22,
            ),
            box_width=11.0,
        )
        pop_def.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Une population est l'ensemble des individus d'une même "
                "espèce vivant au même moment dans un même lieu — par "
                "exemple, tous les buffles du parc de la Comoé."
            )
        ) as tracker:
            self.play(FadeIn(pop_def))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(pop_def))

        station_def = definition_box(
            Text(
                _wrap(
                    "Une station est une portion de territoire limitée et "
                    "homogène, caractérisée par un biotope et une "
                    "biocénose particuliers. C'est l'unité écologique de "
                    "base : une mare, une parcelle de forêt, un champ.",
                    width=54,
                ),
                font_size=22,
            ),
            box_width=11.8,
        )
        station_def.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Une station est une portion de territoire limitée et "
                "homogène, caractérisée par un biotope et une biocénose "
                "particuliers. C'est l'unité écologique de base : une "
                "mare, une parcelle de forêt, un champ, une mare de "
                "village sont des stations."
            )
        ) as tracker:
            self.play(FadeIn(station_def))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(station_def))

        # --- Exemple traité : tableau récapitulatif ivoirien ---------------
        tab_titre = Text("Tableau récapitulatif — exemples ivoiriens", font_size=24, color=YELLOW, weight="BOLD")
        tab_titre.next_to(titre, DOWN, buff=0.4)
        tableau = _bullets(
            [
                "Écosystème : biotope + biocénose + interactions → la savane de Lamto, la forêt de Taï.",
                "Biotope : facteurs physico-chimiques → sol latéritique, climat subéquatorial humide, eau d'un étang.",
                "Biocénose : populations d'êtres vivants → herbes, termites, antilopes, lions, champignons de la savane.",
                "Population : individus d'une même espèce → les buffles du parc de la Comoé.",
                "Station : portion homogène de territoire → un étang de pisciculture à Adzopé, une cacaoyère.",
            ],
            font_size=18,
            width=62,
        )
        tableau.next_to(tab_titre, DOWN, buff=0.35)
        groupe_tab = VGroup(tab_titre, tableau)
        _fit(groupe_tab, titre.get_bottom()[1] - 0.25)

        with self.voiceover(
            text=(
                "Résumons dans un tableau, avec des exemples ivoiriens. "
                "Écosystème, c'est biotope plus biocénose plus "
                "interactions : la savane de Lamto, la forêt de Taï. "
                "Biotope, ce sont les facteurs physico-chimiques : un sol "
                "latéritique, le climat subéquatorial humide, l'eau d'un "
                "étang. Biocénose, ce sont les populations d'êtres "
                "vivants : herbes, termites, antilopes, lions, champignons "
                "de la savane. Population : les buffles du parc de la "
                "Comoé. Station : un étang de pisciculture à Adzopé, une "
                "cacaoyère."
            )
        ) as tracker:
            self.play(FadeIn(tab_titre))
            self.play(FadeIn(tableau))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(tab_titre), FadeOut(tableau))

        # --- À retenir : point clé -----------------------------------------
        methode = method_box(
            Text(
                _wrap(
                    "L'écosystème n'a pas de taille fixe : une flaque "
                    "d'eau, un tronc d'arbre mort, un étang ou toute une "
                    "forêt peuvent être étudiés comme des écosystèmes. Ce "
                    "qui compte, c'est l'existence d'un milieu et d'une "
                    "communauté vivante en interaction.",
                    width=54,
                ),
                font_size=21,
            ),
            box_width=11.8,
        )
        methode.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Point clé à retenir : l'écosystème n'a pas de taille "
                "fixe. Une flaque d'eau, un tronc d'arbre mort, un étang "
                "ou toute une forêt peuvent être étudiés comme des "
                "écosystèmes. Ce qui compte, ce n'est pas la surface, "
                "c'est l'existence d'un milieu et d'une communauté vivante "
                "en interaction."
            )
        ) as tracker:
            self.play(FadeIn(methode))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(titre), FadeOut(methode))
