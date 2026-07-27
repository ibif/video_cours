"""
scenes/Maths_StatistiqueUneVariable_04.py — Chapitre 17 « Statistique à une
variable » (1ereC, Maths), scène 04.

§ Polygones des effectifs et des effectifs cumulés : définition polygone
des effectifs (ligne brisée par les points (x_i ; n_i), centres de classe).
Définitions polygones des effectifs cumulés croissants/décroissants
(bornes sup/inf de classe). Reprise de l'exemple des sacs de cacao (scène
03) : tracé des deux polygones cumulés, leur intersection donne la
médiane M≈73,3 kg.
Source : 1ereC/Maths.pdf, chapitre 17, pages 203-204.
"""

import textwrap

from manim import DOWN, UP, WHITE, YELLOW, Axes, Dot, FadeIn, FadeOut, MathTex, Text, VGroup, Write

from shapes.base_scene import NotionScene
from shapes.boxes import definition_box, example_box, scene_title, warning_box

# --- Données reprises de la scène 03 (60 sacs de cacao pesés à Daloa) -----
BORNES = [60, 65, 70, 75, 80, 85]
EFFECTIFS = [4, 10, 24, 14, 8]
CENTRES = [62.5, 67.5, 72.5, 77.5, 82.5]
N_TOTAL = 60
ECC = [0, 4, 14, 38, 52, 60]   # ECC(borne) pour chacune des 6 bornes
ECD = [60, 56, 46, 22, 8, 0]   # ECD(borne) pour chacune des 6 bornes
MEDIANE = 220 / 3              # ≈ 73,33 kg (calculée en scène 06)


def _wrap(text: str, width: int = 54) -> str:
    return "\n".join(textwrap.fill(line, width=width) for line in text.split("\n"))


def _polygone_effectifs() -> VGroup:
    axes = Axes(
        x_range=[58, 87, 5],
        y_range=[0, 26, 5],
        x_length=8,
        y_length=3.2,
        axis_config={"color": WHITE, "include_tip": False, "font_size": 16},
    )
    ligne = axes.plot_line_graph(
        x_values=CENTRES, y_values=EFFECTIFS, add_vertex_dots=True,
        vertex_dot_radius=0.06, vertex_dot_style={"color": YELLOW},
        line_color=YELLOW, stroke_width=3,
    )
    return VGroup(axes, ligne)


def _polygones_cumules() -> VGroup:
    axes = Axes(
        x_range=[58, 87, 5],
        y_range=[0, 62, 10],
        x_length=8.3,
        y_length=3.6,
        axis_config={"color": WHITE, "include_tip": False, "font_size": 16},
    )
    croissant = axes.plot_line_graph(
        x_values=BORNES, y_values=ECC, add_vertex_dots=True,
        vertex_dot_radius=0.05, vertex_dot_style={"color": YELLOW},
        line_color=YELLOW, stroke_width=3,
    )
    decroissant = axes.plot_line_graph(
        x_values=BORNES, y_values=ECD, add_vertex_dots=True,
        vertex_dot_radius=0.05, vertex_dot_style={"color": "#57C4E5"},
        line_color="#57C4E5", stroke_width=3,
    )
    intersection = Dot(axes.c2p(MEDIANE, 30), color="#FFFFFF", radius=0.07)
    label_inter = MathTex(r"M", font_size=22, color="#FFFFFF").next_to(intersection, UP, buff=0.1)
    return VGroup(axes, croissant, decroissant, intersection, label_inter)


class PolygonesEffectifsCumules(NotionScene):
    def construct(self):
        titre = scene_title("Statistique — Polygones des effectifs et cumuls")
        titre.scale(0.46)
        titre.to_edge(UP)

        # --- Énoncé : mise en situation --------------------------------------
        mise_en_situation = Text(
            _wrap(
                "L'histogramme montre bien la répartition, mais pour "
                "comparer l'évolution des effectifs, ou repérer "
                "graphiquement la médiane, on préfère une ligne brisée : "
                "le polygone.",
                width=56,
            ),
            font_size=23,
        )
        mise_en_situation.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "L'histogramme montre bien la répartition des effectifs, "
                "mais pour comparer leur évolution d'une classe à "
                "l'autre, ou repérer graphiquement une caractéristique "
                "comme la médiane, on préfère souvent une ligne brisée : "
                "le polygone."
            )
        ) as tracker:
            self.play(Write(titre))
            self.play(FadeIn(mise_en_situation))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(mise_en_situation))

        # --- Raisonnement : polygone des effectifs -----------------------------
        def_polygone = definition_box(
            VGroup(
                Text("Polygone des effectifs", font_size=22, weight="BOLD"),
                Text(
                    _wrap(
                        "Ligne brisée reliant les points (x_i ; n_i), où "
                        "x_i est le CENTRE de chaque classe.",
                        width=46,
                    ),
                    font_size=20,
                ),
            ).arrange(DOWN, buff=0.22),
        )
        def_polygone.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Le polygone des effectifs est la ligne brisée qui "
                "relie les points de coordonnées x indice i, n indice "
                "i, où x indice i est le centre de chaque classe."
            )
        ) as tracker:
            self.play(FadeIn(def_polygone))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(def_polygone))

        poly_eff = _polygone_effectifs()
        poly_eff.scale(0.9)
        poly_eff.next_to(titre, DOWN, buff=0.35)

        with self.voiceover(
            text=(
                "Reprenons l'exemple des sacs de cacao de Daloa. Le "
                "polygone des effectifs relie les cinq points portés "
                "par les centres des classes : 62,5 ; 67,5 ; 72,5 ; "
                "77,5 ; et 82,5 kilogrammes."
            )
        ) as tracker:
            self.play(FadeIn(poly_eff))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(poly_eff))

        # --- Raisonnement : polygones cumulés -----------------------------------
        def_polygones_cumules = definition_box(
            VGroup(
                Text("Polygones des effectifs cumulés", font_size=21, weight="BOLD"),
                Text(
                    _wrap(
                        "CROISSANT : relie les points (borne SUPÉRIEURE "
                        "de classe ; ECC). DÉCROISSANT : relie les "
                        "points (borne INFÉRIEURE de classe ; ECD).",
                        width=46,
                    ),
                    font_size=19,
                ),
            ).arrange(DOWN, buff=0.22),
        )
        def_polygones_cumules.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Pour les cumuls, on utilise cette fois les bornes des "
                "classes, et non plus leurs centres. Le polygone des "
                "effectifs cumulés croissants relie les points portés "
                "par la borne supérieure de chaque classe et l'effectif "
                "cumulé croissant correspondant. Le polygone des "
                "effectifs cumulés décroissants relie, lui, les points "
                "portés par la borne inférieure de chaque classe et "
                "l'effectif cumulé décroissant."
            )
        ) as tracker:
            self.play(FadeIn(def_polygones_cumules))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(def_polygones_cumules))

        # --- Exemple traité : intersection = médiane ---------------------------
        enonce = Text(
            _wrap(
                "Reprenons encore l'exemple des sacs de cacao : traçons "
                "les deux polygones cumulés sur les mêmes axes et "
                "observons leur point d'intersection.",
                width=52,
            ),
            font_size=21,
        )
        enonce.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Reprenons une dernière fois l'exemple des sacs de "
                "cacao : traçons les deux polygones cumulés sur les "
                "mêmes axes, et observons leur point d'intersection."
            )
        ) as tracker:
            self.play(FadeIn(enonce))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(enonce))

        poly_cumules = _polygones_cumules()
        poly_cumules.scale(0.9)
        poly_cumules.next_to(titre, DOWN, buff=0.35)

        with self.voiceover(
            text=(
                "En jaune, le polygone croissant qui monte de 0 à 60 ; "
                "en bleu clair, le polygone décroissant qui descend de "
                "60 à 0. Ils se croisent en un point remarquable, marqué "
                "M sur le graphique : ce point partage la population en "
                "deux effectifs égaux, 30 sacs de chaque côté. C'est "
                "précisément la MÉDIANE, dont nous verrons le calcul "
                "exact par interpolation dans une prochaine scène."
            )
        ) as tracker:
            self.play(Write(poly_cumules))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(poly_cumules))

        # --- À retenir --------------------------------------------------------
        recap = example_box(
            VGroup(
                Text("À retenir", font_size=22, weight="BOLD"),
                Text(
                    _wrap(
                        "L'intersection des deux polygones cumulés donne "
                        "une lecture GRAPHIQUE de la médiane.",
                        width=46,
                    ),
                    font_size=20,
                ),
            ).arrange(DOWN, buff=0.25),
        )
        recap.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Retenons l'essentiel : l'intersection des deux "
                "polygones cumulés donne une lecture graphique directe "
                "de la médiane, avant même tout calcul."
            )
        ) as tracker:
            self.play(FadeIn(recap))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(recap))

        # --- Piège à éviter -----------------------------------------------------
        piege = warning_box(
            VGroup(
                Text("Piège — Centres pour les effectifs, bornes pour les cumuls", font_size=16, weight="BOLD"),
                Text(
                    _wrap(
                        "Ne pas confondre les deux abscisses : le "
                        "polygone des EFFECTIFS utilise les CENTRES de "
                        "classe, les polygones des CUMULÉS utilisent les "
                        "BORNES. Les intervertir fausse tout le tracé.",
                        width=46,
                    ),
                    font_size=18,
                ),
            ).arrange(DOWN, buff=0.2),
        )
        piege.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Piège à éviter absolument : ne confondez pas les deux "
                "abscisses utilisées. Le polygone des effectifs se "
                "construit avec les centres de classe, tandis que les "
                "polygones des cumulés se construisent avec les bornes "
                "de classe. Les intervertir fausse complètement le "
                "tracé, et donc la lecture de la médiane."
            )
        ) as tracker:
            self.play(FadeIn(piege))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(piege), FadeOut(titre))
