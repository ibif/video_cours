"""
scenes/SVT_EchangesIonsSol_04.py — Chapitre 8 (1ereD, SVT), scène 04.

§ 8.2.1-8.2.2 Les besoins minéraux de la plante : éléments majeurs et
oligo-éléments, tableau des formes ioniques, vocabulaire chlorose /
nécrose / nanisme, tableau des rôles et carences des 6 éléments majeurs,
remarque sur la loi du minimum de Liebig. Source : 1ereD/SVT.pdf,
pages 106-108.
"""

import textwrap

from manim import (
    DOWN,
    GREEN,
    LEFT,
    RIGHT,
    UP,
    WHITE,
    YELLOW,
    FadeIn,
    FadeOut,
    Text,
    VGroup,
    Write,
    config,
)

from shapes.base_scene import NotionScene
from shapes.boxes import definition_box, property_box, scene_title, warning_box


def _wrap(text: str, width: int = 56) -> str:
    return "\n".join(textwrap.fill(line, width=width) for line in text.split("\n"))


def _bullets(items, font_size=24, color=WHITE, width=54):
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


class BesoinsMineraux(NotionScene):
    def construct(self):
        titre = scene_title("8.2 — Les besoins minéraux de la plante")
        titre.scale(0.68)
        titre.to_edge(UP)

        # --- Énoncé : dessèchement et combustion d'une plante --------------
        intro = Text(
            _wrap(
                "Si l'on dessèche une plante à l'étuve, l'eau s'évapore : "
                "il reste la matière sèche. Si on brûle cette matière "
                "sèche, carbone, hydrogène, oxygène et azote partent dans "
                "les fumées : il reste des cendres (~5% de la matière "
                "sèche), contenant les autres éléments minéraux.",
                width=56,
            ),
            font_size=25,
            color=WHITE,
        )
        intro.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Si l'on dessèche une plante à l'étuve, l'eau s'évapore et "
                "il reste la matière sèche. Si l'on brûle cette matière "
                "sèche, le carbone, l'hydrogène, l'oxygène et l'azote "
                "partent dans les fumées : il reste des cendres, environ "
                "cinq pour cent de la matière sèche, qui contiennent les "
                "autres éléments minéraux : phosphore, potassium, "
                "calcium, magnésium, soufre, fer... Tous ces éléments "
                "proviennent du sol, prélevés sous forme d'ions."
            )
        ) as tracker:
            self.play(Write(titre))
            self.play(FadeIn(intro))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(intro))

        # --- Raisonnement : majeurs / oligo-éléments + formes ioniques ----
        def_majeurs = definition_box(
            Text(
                _wrap(
                    "Les éléments majeurs (macro-éléments), en quantités "
                    "relativement grandes : azote (N), phosphore (P), "
                    "potassium (K), calcium (Ca), magnésium (Mg), soufre "
                    "(S). Les oligo-éléments, en très petites quantités "
                    "(traces) : fer (Fe), manganèse (Mn), bore (B), zinc "
                    "(Zn), cuivre (Cu), molybdène (Mo), chlore (Cl). Tous "
                    "indispensables ; aucun ne peut être remplacé.",
                    width=54,
                ),
                font_size=21,
            ),
            box_width=11.8,
        )
        def_majeurs.next_to(titre, DOWN, buff=0.45)

        with self.voiceover(
            text=(
                "On distingue deux catégories. Les éléments majeurs, ou "
                "macro-éléments, sont nécessaires en quantités "
                "relativement grandes : azote, phosphore, potassium, "
                "calcium, magnésium, soufre. Les oligo-éléments sont "
                "nécessaires en très petites quantités, à l'état de "
                "traces : fer, manganèse, bore, zinc, cuivre, molybdène, "
                "chlore. Tous sont indispensables : aucun ne peut être "
                "remplacé par un autre, et l'absence d'un seul bloque la "
                "croissance."
            )
        ) as tracker:
            self.play(FadeIn(def_majeurs))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(def_majeurs))

        tab_titre = Text("Sous quelle forme ionique ?", font_size=27, color=YELLOW, weight="BOLD")
        tab_titre.next_to(titre, DOWN, buff=0.5)

        formes = _bullets(
            [
                "Azote → NO3− (nitrate) ou NH4+ (ammonium)",
                "Phosphore → H2PO4− et HPO4(2−) (phosphates)",
                "Potassium → K+     Calcium → Ca2+     Magnésium → Mg2+",
                "Soufre → SO4(2−)     Fer → Fe2+ ou Fe3+     Chlore → Cl−",
            ],
            font_size=21,
            width=52,
        )
        formes.next_to(tab_titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Chaque élément est absorbé sous une forme ionique "
                "précise. L'azote sous forme de nitrate ou d'ammonium. Le "
                "phosphore sous forme de phosphates. Le potassium sous "
                "forme d'ion K+, le calcium Ca2+, le magnésium Mg2+. Le "
                "soufre sous forme de sulfate, le fer sous forme "
                "d'ions Fe2+ ou Fe3+, le chlore sous forme de chlorure."
            )
        ) as tracker:
            self.play(FadeIn(tab_titre))
            self.play(FadeIn(formes))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(tab_titre), FadeOut(formes))

        # --- Vocabulaire : chlorose, nécrose, nanisme -----------------------
        vocab = definition_box(
            _bullets(
                [
                    "La chlorose : jaunissement du limbe par manque de "
                    "chlorophylle.",
                    "La nécrose : mort localisée de tissus (brunissent, "
                    "se dessèchent).",
                    "Le nanisme : arrêt de croissance, plante "
                    "anormalement petite.",
                ],
                font_size=21,
                width=50,
            ),
            box_width=11.8,
        )
        vocab.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Avant d'étudier les carences, trois mots de vocabulaire à "
                "connaître. La chlorose : un jaunissement du limbe par "
                "manque de chlorophylle. La nécrose : une mort localisée "
                "de tissus, qui brunissent puis se dessèchent. Le "
                "nanisme : un arrêt de croissance, la plante restant "
                "anormalement petite."
            )
        ) as tracker:
            self.play(FadeIn(vocab))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(vocab))

        # --- Exemple traité : tableau des rôles et carences -----------------
        tab2_titre = Text("Rôle et carence des 6 éléments majeurs", font_size=24, color=YELLOW, weight="BOLD")
        tab2_titre.next_to(titre, DOWN, buff=0.4)

        roles = property_box(
            _bullets(
                [
                    "Azote (N) : protéines, chlorophylle, croissance → "
                    "carence : nanisme, chlorose des vieilles feuilles.",
                    "Phosphore (P) : ATP, floraison, enracinement → "
                    "carence : croissance retardée, feuillage violacé.",
                    "Potassium (K) : eau (stomates), résistance → "
                    "carence : chlorose puis nécrose des bordures.",
                    "Magnésium (Mg) : centre de la chlorophylle → "
                    "carence : chlorose internervaire (vieilles feuilles).",
                    "Calcium (Ca) : parois et membranes cellulaires → "
                    "carence : déformation, mort des jeunes pousses.",
                    "Soufre (S) : acides aminés, protéines → carence : "
                    "chlorose générale des jeunes feuilles.",
                ],
                font_size=17,
                width=58,
            ),
            box_width=12.6,
        )
        roles.next_to(tab2_titre, DOWN, buff=0.35)

        # Garde-fou : tableau à 6 lignes, on vérifie qu'il tient sous le titre.
        groupe_tableau = VGroup(tab2_titre, roles)
        _fit(groupe_tableau, titre.get_bottom()[1] - 0.25)

        with self.voiceover(
            text=(
                "Résumons le rôle de chaque élément majeur, et le symptôme "
                "de sa carence. L'azote entre dans les protéines et la "
                "chlorophylle, il pilote la croissance : sa carence "
                "provoque un nanisme et une chlorose des vieilles "
                "feuilles. Le phosphore entre dans l'ATP, il favorise la "
                "floraison et l'enracinement : sa carence retarde la "
                "croissance et donne un feuillage aux reflets violacés. "
                "Le potassium règle l'ouverture des stomates et renforce "
                "la résistance : sa carence provoque une chlorose puis "
                "une nécrose des bordures de feuilles. Le magnésium est "
                "l'atome central de la chlorophylle : sa carence donne "
                "une chlorose internervaire des vieilles feuilles, le "
                "limbe jaunissant entre des nervures restées vertes. Le "
                "calcium consolide les parois et les membranes "
                "cellulaires : sa carence déforme et tue les jeunes "
                "pousses. Le soufre entre dans certains acides aminés : "
                "sa carence donne une chlorose générale, touchant "
                "d'abord les jeunes feuilles."
            )
        ) as tracker:
            self.play(FadeIn(tab2_titre))
            self.play(FadeIn(roles))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(tab2_titre), FadeOut(roles))

        # --- À retenir / piège : la loi du minimum de Liebig ----------------
        loi_minimum = warning_box(
            Text(
                _wrap(
                    "La loi du minimum (Liebig) : la croissance d'une "
                    "plante est limitée par l'élément nutritif présent en "
                    "plus faible quantité par rapport à ses besoins "
                    "(élément limitant). Même si tous les autres "
                    "abondent, un seul élément manquant bloque la "
                    "croissance - comme la planche la plus courte d'un "
                    "tonneau fixe le niveau de l'eau.",
                    width=54,
                ),
                font_size=21,
            ),
            box_width=11.8,
        )
        loi_minimum.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Retenons un principe essentiel, la loi du minimum, "
                "énoncée par Liebig : la croissance d'une plante est "
                "limitée par l'élément nutritif présent en plus faible "
                "quantité par rapport à ses besoins, appelé élément "
                "limitant. Même si tous les autres éléments abondent, un "
                "seul élément manquant suffit à bloquer la croissance. "
                "C'est comme un tonneau fait de planches de hauteurs "
                "différentes : c'est toujours la planche la plus courte "
                "qui fixe le niveau de l'eau que le tonneau peut "
                "contenir. Voilà le piège à éviter : ne jamais conclure "
                "trop vite qu'un seul élément suffit à expliquer une "
                "bonne récolte, c'est l'équilibre de tous qui compte."
            )
        ) as tracker:
            self.play(FadeIn(loi_minimum))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(titre), FadeOut(loi_minimum))
