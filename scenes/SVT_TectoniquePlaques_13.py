"""
scenes/SVT_TectoniquePlaques_13.py — Chapitre 8 (1ereC, SVT), scène 13.

VI. Conséquences : la répartition des séismes (carte des épicentres =
limites de plaques, ceinture de feu, ceinture alpine-himalayenne, séismes
superficiels vs profonds, Côte d'Ivoire asismique) + la répartition des
volcans (80% en subduction, dorsales effusives, points chauds
intraplaques : Hawaï, ligne volcanique du Cameroun) + applications risques
et prévention. Source : 1ereC/SVT.pdf, pages 92-93.
"""

import textwrap

from manim import (
    BLUE_D,
    DOWN,
    LEFT,
    ORANGE,
    RED,
    RIGHT,
    UP,
    WHITE,
    YELLOW,
    Dot,
    FadeIn,
    FadeOut,
    Rectangle,
    Text,
    VGroup,
    Write,
)

from shapes.base_scene import NotionScene
from shapes.boxes import definition_box, property_box, scene_title


def _wrap(text: str, width: int = 56) -> str:
    return "\n".join(textwrap.fill(line, width=width) for line in text.split("\n"))


def _bullets(items, font_size=24, color=WHITE, width=54):
    lines = VGroup(
        *[Text(f"• {_wrap(it, width=width)}", font_size=font_size, color=color) for it in items]
    )
    lines.arrange(DOWN, aligned_edge=LEFT, buff=0.22)
    return lines


class ConsequencesSeismesEtVolcans(NotionScene):
    def construct(self):
        titre = scene_title("VI. Conséquences : séismes et volcans")
        titre.scale(0.6)
        titre.to_edge(UP)
        self.play(Write(titre))

        # --- Énoncé : définitions séisme / foyer / épicentre -------------------
        d_seisme = definition_box(
            Text(
                _wrap(
                    "Séisme (tremblement de terre) : vibration brutale du "
                    "sol provoquée par la rupture de roches accumulant des "
                    "contraintes. Le foyer est le point de rupture en "
                    "profondeur ; l'épicentre est le point de la surface "
                    "situé à la verticale du foyer.",
                    width=54,
                ),
                font_size=21,
            ),
            box_width=12.0,
        )
        d_seisme.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Rappelons trois définitions. Un séisme, ou tremblement de "
                "terre, est une vibration brutale du sol, provoquée par la "
                "rupture de roches qui accumulaient des contraintes. Le "
                "foyer est le point de rupture en profondeur ; l'épicentre "
                "est le point de la surface situé à la verticale du foyer."
            )
        ) as tracker:
            self.play(FadeIn(d_seisme))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(d_seisme))

        # --- Animation du raisonnement : les séismes dessinent les limites ------
        entete_seismes = Text("Les séismes dessinent les limites de plaques", font_size=22, color=YELLOW, weight="BOLD")
        entete_seismes.next_to(titre, DOWN, buff=0.5)

        seismes = _bullets(
            [
                "La carte mondiale des épicentres montre des alignements "
                "étroits coïncidant avec les limites de plaques : ceinture "
                "de feu du Pacifique (subductions), ceinture "
                "alpine-himalayenne (collision), dorsales.",
                "Séismes superficiels (<30 km) : dorsales et failles "
                "transformantes. Séismes superficiels à profonds "
                "(≤700 km) : zones de subduction, le long du plan de "
                "Wadati-Benioff — les plus violents (Japon 2011, Chili "
                "2010).",
                "L'intérieur des plaques est quasi asismique : la Côte "
                "d'Ivoire, au cœur de la plaque africaine, est une zone de "
                "faible sismicité.",
            ],
            font_size=19,
            width=54,
        )
        seismes.next_to(entete_seismes, DOWN, buff=0.3)

        with self.voiceover(
            text=(
                "La carte mondiale des épicentres montre des alignements "
                "étroits qui coïncident précisément avec les limites de "
                "plaques : la ceinture de feu du Pacifique, où s'alignent "
                "les subductions, la ceinture alpine-himalayenne, marquée "
                "par la collision, et les dorsales. Les séismes "
                "superficiels, à moins de trente kilomètres, se "
                "concentrent aux dorsales et aux failles transformantes. "
                "Les séismes superficiels à profonds, jusqu'à environ sept "
                "cents kilomètres, jalonnent les zones de subduction le "
                "long du plan de Wadati-Benioff : ce sont les plus "
                "violents, comme au Japon en deux mille onze, ou au Chili "
                "en deux mille dix. En revanche, l'intérieur des plaques "
                "est quasi asismique : la Côte d'Ivoire, au cœur de la "
                "plaque africaine, est une zone de faible sismicité."
            )
        ) as tracker:
            self.play(FadeIn(entete_seismes))
            self.play(FadeIn(seismes))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(entete_seismes), FadeOut(seismes))

        # --- Schéma : carte simplifiée épicentres le long des limites -----------
        ocean_carte = Rectangle(width=10.0, height=3.5, fill_color=BLUE_D, fill_opacity=0.35, stroke_width=0)

        # ligne de dorsale (épicentres superficiels)
        dorsale_pts = [[-4.0, 1.0, 0], [-2.5, 0.6, 0], [-1.0, 1.0, 0], [0.5, 0.6, 0]]
        epicentres_dorsale = VGroup(*[Dot(point=p, radius=0.06, color=YELLOW) for p in dorsale_pts])

        # ligne de subduction (épicentres profonds, en dégradé)
        subd_pts_couleurs = [([2.0, -1.0, 0], YELLOW), ([2.6, -0.5, 0], ORANGE), ([3.2, 0.0, 0], RED), ([3.8, 0.6, 0], RED)]
        epicentres_subduction = VGroup(*[Dot(point=p, radius=0.07, color=c) for p, c in subd_pts_couleurs])

        label_dorsale_carte = Text("dorsale : séismes superficiels", font_size=14, color=YELLOW).next_to(epicentres_dorsale, DOWN, buff=0.2)
        label_subd_carte = Text("subduction : séismes\nsuperficiels à profonds", font_size=13, color=RED).next_to(epicentres_subduction, UP, buff=0.2)

        interieur = Dot(point=[-2.0, -1.3, 0], radius=0.04, color=WHITE)
        label_interieur = Text("intérieur de plaque : asismique (ex. Côte d'Ivoire)", font_size=13, color=WHITE)
        label_interieur.next_to(interieur, DOWN, buff=0.15)

        carte = VGroup(
            ocean_carte, epicentres_dorsale, epicentres_subduction,
            label_dorsale_carte, label_subd_carte, interieur, label_interieur,
        )
        carte.next_to(titre, DOWN, buff=0.55)

        with self.voiceover(
            text=(
                "Sur cette carte simplifiée, on distingue nettement les "
                "trois situations : les points jaunes alignés le long "
                "d'une dorsale, tous superficiels ; le dégradé de couleurs "
                "le long d'une zone de subduction, du jaune superficiel au "
                "rouge profond ; et, au milieu de la plaque, presque aucun "
                "point : c'est l'intérieur asismique, comme la Côte "
                "d'Ivoire."
            )
        ) as tracker:
            self.play(FadeIn(ocean_carte))
            self.play(FadeIn(epicentres_dorsale), FadeIn(label_dorsale_carte))
            self.play(FadeIn(epicentres_subduction), FadeIn(label_subd_carte))
            self.play(FadeIn(interieur), FadeIn(label_interieur))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(carte))

        # --- Exemple traité : répartition des volcans ---------------------------
        entete_volcans = Text("Les volcans bordent les frontières actives", font_size=22, color=YELLOW, weight="BOLD")
        entete_volcans.next_to(titre, DOWN, buff=0.5)

        volcans = _bullets(
            [
                "Environ 80% des volcans actifs se situent au-dessus des "
                "zones de subduction (volcanisme andésitique explosif : "
                "Andes, Japon, Indonésie) — « l'anneau de feu ».",
                "Les dorsales portent un volcanisme basaltique effusif "
                "(Islande, rift est-africain).",
                "Exception : les points chauds intraplaques (Hawaï ; "
                "ligne volcanique du Cameroun, dont le mont Cameroun, "
                "4095 m, seul volcan actif d'Afrique de l'Ouest).",
            ],
            font_size=20,
            width=54,
        )
        volcans.next_to(entete_volcans, DOWN, buff=0.3)

        with self.voiceover(
            text=(
                "Les volcans, eux aussi, bordent les frontières actives. "
                "Environ quatre-vingts pour cent des volcans actifs se "
                "situent au-dessus des zones de subduction, avec un "
                "volcanisme andésitique explosif, dans les Andes, au "
                "Japon, en Indonésie : c'est l'anneau de feu. Les "
                "dorsales, elles, portent un volcanisme basaltique "
                "effusif, en Islande ou sur le rift est-africain. Exception "
                "notable : les points chauds intraplaques, comme Hawaï, ou "
                "la ligne volcanique du Cameroun, dont le mont Cameroun, "
                "quatre mille quatre-vingt-quinze mètres, est le seul "
                "volcan actif d'Afrique de l'Ouest."
            )
        ) as tracker:
            self.play(FadeIn(entete_volcans))
            self.play(FadeIn(volcans))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(entete_volcans), FadeOut(volcans))

        # --- À retenir : applications risques et prévention ----------------------
        applications = property_box(
            Text(
                _wrap(
                    "Applications : la connaissance des frontières de "
                    "plaques permet de localiser les zones à risque, "
                    "d'établir des normes de construction parasismique, et "
                    "d'organiser la surveillance volcanique — par exemple "
                    "l'observatoire du Nyiragongo à Goma (RDC), voisine de "
                    "l'Afrique de l'Est.",
                    width=54,
                ),
                font_size=21,
            ),
            box_width=12.0,
        )
        applications.next_to(titre, DOWN, buff=0.55)

        with self.voiceover(
            text=(
                "Ces connaissances ont des applications très concrètes : la "
                "localisation des zones à risque, l'établissement de normes "
                "de construction parasismique, et l'organisation de la "
                "surveillance volcanique, comme celle assurée par "
                "l'observatoire du Nyiragongo, à Goma, en République "
                "démocratique du Congo, voisine du rift est-africain."
            )
        ) as tracker:
            self.play(FadeIn(applications))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(applications), FadeOut(titre))
