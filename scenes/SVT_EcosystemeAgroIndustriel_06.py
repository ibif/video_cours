"""
scenes/SVT_EcosystemeAgroIndustriel_06.py — Chapitre 11 (1ereC, SVT), scène 06.

§ 3.1 Les catégories fonctionnelles de la biocénose : définition du niveau
trophique, puis tableau (producteurs, consommateurs primaires / secondaires
/ tertiaires, décomposeurs, détritivores — rôle, mode de nutrition,
exemples), et méthode « sans les décomposeurs, la vie s'arrêterait ».
Source : 1ereC/SVT.pdf, page 123.
"""

import textwrap

from manim import DOWN, LEFT, UP, WHITE, YELLOW, FadeIn, FadeOut, Text, VGroup, Write, config

from shapes.base_scene import NotionScene
from shapes.boxes import definition_box, method_box, property_box, scene_title


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


class CategoriesFonctionnellesBiocenose(NotionScene):
    def construct(self):
        titre = scene_title("3.1 — Les catégories fonctionnelles de la biocénose")
        titre.scale(0.5)
        titre.to_edge(UP)

        # --- Énoncé : le niveau trophique -----------------------------------
        intro = Text(
            _wrap(
                "Les relations alimentaires, ou trophiques (du grec "
                "trophê, nourriture), sont le lien principal entre les "
                "membres de la biocénose. On classe les êtres vivants "
                "selon leur place dans ce réseau d'échanges.",
                width=56,
            ),
            font_size=23,
            color=WHITE,
        )
        intro.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Les relations alimentaires, ou relations trophiques, du "
                "grec trophê, nourriture, sont le lien principal entre les "
                "membres de la biocénose. On classe les êtres vivants "
                "selon leur place dans ce réseau d'échanges de matière et "
                "d'énergie."
            )
        ) as tracker:
            self.play(Write(titre))
            self.play(FadeIn(intro))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(intro))

        niveau_def = definition_box(
            Text(
                _wrap(
                    "Un niveau trophique est l'ensemble des organismes qui "
                    "occupent la même place dans le transfert de la "
                    "matière et de l'énergie alimentaires au sein d'un "
                    "écosystème.",
                    width=54,
                ),
                font_size=22,
            ),
            box_width=11.5,
        )
        niveau_def.next_to(titre, DOWN, buff=0.45)

        with self.voiceover(
            text=(
                "Un niveau trophique est l'ensemble des organismes qui "
                "occupent la même place dans le transfert de la matière et "
                "de l'énergie alimentaires au sein d'un écosystème."
            )
        ) as tracker:
            self.play(FadeIn(niveau_def))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(niveau_def))

        # --- Raisonnement : le grand tableau des catégories -----------------
        tab_titre = Text("Les 6 catégories fonctionnelles", font_size=24, color=YELLOW, weight="BOLD")
        tab_titre.next_to(titre, DOWN, buff=0.4)
        tableau = _bullets(
            [
                "Producteurs (P) : fabriquent la matière organique (photosynthèse) — plantes, algues, phytoplancton.",
                "Consommateurs primaires (C1) : mangent les producteurs (herbivores) — sauterelles, zooplancton, buffle.",
                "Consommateurs secondaires (C2) : mangent les C1 (carnivores 1er ordre) — crapauds, lézards, mantes.",
                "Consommateurs tertiaires (C3) : mangent les C2 (superprédateurs) — serpents, aigles, lions.",
                "Décomposeurs : minéralisent la matière morte (saprophagie) — bactéries, champignons.",
                "Détritivores : fragmentent les débris — termites, vers de terre, cloportes.",
            ],
            font_size=17,
            width=64,
        )
        tableau.next_to(tab_titre, DOWN, buff=0.3)
        groupe_tab = VGroup(tab_titre, tableau)
        _fit(groupe_tab, titre.get_bottom()[1] - 0.2)

        with self.voiceover(
            text=(
                "Voici les six catégories fonctionnelles. Les producteurs "
                "fabriquent la matière organique à partir de matière "
                "minérale, par autotrophie, grâce à la photosynthèse : "
                "plantes vertes, algues, phytoplancton. Les consommateurs "
                "primaires mangent les producteurs, ce sont des "
                "herbivores : sauterelles, chenilles, zooplancton, "
                "tilapia, buffle. Les consommateurs secondaires mangent "
                "les consommateurs primaires, ce sont des carnivores de "
                "premier ordre : crapauds, lézards, mantes religieuses. "
                "Les consommateurs tertiaires mangent les consommateurs "
                "secondaires, ce sont des superprédateurs : serpents, "
                "aigles, lions. Les décomposeurs dégradent la matière "
                "organique morte et la transforment en matière minérale, "
                "c'est la minéralisation : bactéries, champignons. Enfin "
                "les détritivores fragmentent les débris, cadavres, "
                "feuilles mortes, excréments, et facilitent le travail des "
                "décomposeurs : termites, vers de terre, cloportes."
            )
        ) as tracker:
            self.play(FadeIn(tab_titre))
            self.play(FadeIn(tableau))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(tab_titre), FadeOut(tableau))

        # --- Exemple traité : décomposeurs vs détritivores -------------------
        exemple = property_box(
            Text(
                _wrap(
                    "Différence pratique : le détritivore (ver de terre, "
                    "termite) fragmente mécaniquement les débris en "
                    "petits morceaux ; le décomposeur (bactérie, "
                    "champignon) achève la transformation chimique en "
                    "matière minérale.",
                    width=54,
                ),
                font_size=21,
            ),
            box_width=11.8,
        )
        exemple.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Un exemple pour bien distinguer décomposeurs et "
                "détritivores : un ver de terre ou un termite, "
                "détritivore, fragmente mécaniquement une feuille morte en "
                "petits morceaux ; des bactéries et des champignons, "
                "décomposeurs, achèvent ensuite la transformation chimique "
                "en matière minérale, nitrates, phosphates, réutilisables "
                "par les plantes."
            )
        ) as tracker:
            self.play(FadeIn(exemple))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(exemple))

        # --- À retenir : point clé --------------------------------------------
        methode = method_box(
            Text(
                _wrap(
                    "Sans les décomposeurs, les cadavres et les déchets "
                    "s'accumuleraient et les éléments minéraux (azote, "
                    "phosphore...) resteraient prisonniers de la matière "
                    "morte : la vie s'arrêterait faute de « recyclage ». "
                    "Les décomposeurs bouclent le cycle de la matière.",
                    width=54,
                ),
                font_size=21,
            ),
            box_width=11.8,
        )
        methode.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Point clé à retenir : sans les décomposeurs, les cadavres "
                "et les déchets s'accumuleraient, et les éléments "
                "minéraux, azote, phosphore, resteraient prisonniers de la "
                "matière morte. La vie s'arrêterait, faute de recyclage. "
                "Les décomposeurs bouclent le cycle de la matière : ce "
                "sont eux qui rendent possible la vie sur le long terme."
            )
        ) as tracker:
            self.play(FadeIn(methode))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(titre), FadeOut(methode))
