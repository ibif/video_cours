"""
scenes/SVT_StructureInterneGlobe_01.py — Chapitre 7 (1ereC, SVT), scène 01.

§ Introduction : le rayon terrestre (6371 km), comment explorer l'intérieur
de la Terre, les indices de surface (forages, mines, volcanisme,
ophiolites, affleurements — exemples ivoiriens/africains), définition du
xénolite, limite de ces indices (10 à 100 premiers km seulement) et
objectifs du chapitre. Source : 1ereC/SVT.pdf, pages 70-71.
"""

import textwrap

from manim import (
    DOWN,
    LEFT,
    RIGHT,
    UP,
    WHITE,
    YELLOW,
    Circle,
    Dot,
    FadeIn,
    FadeOut,
    Line,
    Text,
    VGroup,
    Write,
    config,
)

from shapes.base_scene import NotionScene
from shapes.boxes import definition_box, scene_title, warning_box


def _wrap(text: str, width: int = 56) -> str:
    return "\n".join(textwrap.fill(line, width=width) for line in text.split("\n"))


def _bullets(items, font_size=23, color=WHITE, width=52):
    lines = VGroup(
        *[Text(f"• {_wrap(it, width=width)}", font_size=font_size, color=color) for it in items]
    )
    lines.arrange(DOWN, aligned_edge=LEFT, buff=0.22)
    return lines


def _tableau(rows, font_size=18, header_color=YELLOW, body_color=WHITE, col_alignments=None, buff=(0.5, 0.22)):
    ncols = len(rows[0])
    cells = []
    for i, row in enumerate(rows):
        for c in row:
            cells.append(
                Text(
                    c,
                    font_size=font_size,
                    color=header_color if i == 0 else body_color,
                    weight="BOLD" if i == 0 else "NORMAL",
                )
            )
    grid = VGroup(*cells)
    align = col_alignments or ("l" * ncols)
    grid.arrange_in_grid(rows=len(rows), cols=ncols, buff=buff, col_alignments=align)
    return grid


def _garde_fou(mobject):
    """Réduit l'échelle d'un mobject s'il déborde du cadre visible sous son sommet actuel."""
    bas_visible = -config.frame_height / 2 + 0.3
    hauteur_dispo = mobject.get_top()[1] - bas_visible
    if mobject.height > hauteur_dispo > 0:
        mobject.scale(hauteur_dispo / mobject.height, about_point=mobject.get_top())


class IntroductionStructureInterneGlobe(NotionScene):
    def construct(self):
        titre = scene_title("Chap. 7 — La structure interne du globe terrestre")
        titre.scale(0.58)
        titre.to_edge(UP)

        # --- Énoncé : le rayon terrestre et la question du chapitre --------
        intro = Text(
            _wrap(
                "Le rayon moyen de la Terre vaut environ 6 371 km. Or "
                "l'homme n'a jamais pu descendre ni forer au-delà d'une "
                "dizaine de kilomètres. Comment connaît-on alors la "
                "structure de l'intérieur du globe ?",
                width=56,
            ),
            font_size=25,
            color=WHITE,
        )
        intro.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Le rayon moyen de la Terre vaut environ six mille trois "
                "cent soixante et onze kilomètres. Or l'homme n'a jamais pu "
                "descendre ni forer au-delà d'une dizaine de kilomètres. "
                "Comment connaît-on alors la structure de l'intérieur du "
                "globe ? C'est la question de ce chapitre."
            )
        ) as tracker:
            self.play(Write(titre))
            self.play(FadeIn(intro))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(intro))

        # Schéma : Terre vue de coupe, rayon connu, profondeur explorée minuscule
        terre = Circle(radius=1.6, color="#595959", fill_color="#3A3A3A", fill_opacity=0.9)
        centre = Dot(terre.get_center(), color=YELLOW, radius=0.05)
        rayon = Line(terre.get_center(), terre.point_at_angle(1.2), color=YELLOW, stroke_width=3)
        label_rayon = Text("R ≈ 6 371 km", font_size=18, color=YELLOW)
        label_rayon.next_to(rayon.get_center(), RIGHT, buff=0.15)
        forage = Line(
            terre.point_at_angle(1.5708),
            terre.point_at_angle(1.5708) + DOWN * 0.08,
            color="#E03131",
            stroke_width=6,
        )
        label_forage = Text("~12 km explorés\n(0,2 % du rayon)", font_size=15, color="#E03131")
        label_forage.next_to(terre, UP, buff=0.35)

        schema = VGroup(terre, centre, rayon, label_rayon)
        schema.move_to(LEFT * 0.5)
        label_forage.next_to(schema, RIGHT, buff=0.9)

        with self.voiceover(
            text=(
                "Deux catégories d'indices sont utilisées : les indices de "
                "surface, qui fournissent des échantillons ou des mesures "
                "réels, mais qui ne concernent qu'une pellicule "
                "infinitésimale du globe, et les indices indirects, qui "
                "reposent sur le raisonnement et l'exploitation de "
                "phénomènes physiques, pour explorer tout le reste."
            )
        ) as tracker:
            self.play(FadeIn(schema))
            self.play(FadeIn(forage), FadeIn(label_forage))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(schema), FadeOut(forage), FadeOut(label_forage))

        # --- Animation du raisonnement : les indices de surface (tableau) --
        entete_tab = Text("I.1 — Les indices de surface (indices directs)", font_size=25, color=YELLOW, weight="BOLD")
        entete_tab.next_to(titre, DOWN, buff=0.45)

        tableau = _tableau(
            [
                ["Indice", "Exemple ivoirien / africain", "Renseigne sur"],
                ["Forages", "Kola (Russie) : 12 262 m", "Roches réelles, T° (~180°C)"],
                ["Mines", "Ity, Tongon (Côte d'Ivoire)", "T° croissante avec profondeur"],
                ["Volcanisme", "Hoggar, Cameroun, Virunga", "Xénolites du manteau"],
                ["Ophiolites", "Fragments charriés / collisions", "Coupe croûte + manteau océanique"],
                ["Affleurements", "Socle ouest-africain", "P et T de la croûte profonde"],
            ],
            font_size=17,
        )
        tableau.next_to(entete_tab, DOWN, buff=0.35)
        _garde_fou(VGroup(entete_tab, tableau))

        with self.voiceover(
            text=(
                "Voici les indices de surface. Les forages, comme celui de "
                "Kola en Russie, atteignent douze mille deux cent "
                "soixante-deux mètres et livrent des roches réelles ainsi "
                "que la température, environ cent quatre-vingts degrés au "
                "fond. Les mines, comme celles d'Ity et de Tongon en Côte "
                "d'Ivoire, confirment cette montée de la température avec la "
                "profondeur. Le volcanisme, au Hoggar, au Cameroun ou dans "
                "la chaîne des Virunga, projette en surface des xénolites de "
                "péridotites arrachés au manteau. Les ophiolites sont des "
                "fragments de lithosphère océanique charriés sur les "
                "continents lors de collisions. Enfin, les affleurements de "
                "roches profondes, comme le socle du bouclier ouest-africain, "
                "renseignent sur les conditions de pression et de "
                "température de la croûte profonde."
            )
        ) as tracker:
            self.play(FadeIn(entete_tab))
            self.play(FadeIn(tableau))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(entete_tab), FadeOut(tableau))

        # --- Exemple traité : la définition du xénolite ---------------------
        xenolite_def = definition_box(
            Text(
                _wrap(
                    "Xénolite : fragment de roche étranger (« xénos »="
                    "étranger, « lithos »=pierre) arraché aux parois du "
                    "conduit volcanique ou au manteau, puis remonté en "
                    "surface enfermé dans une lave. Les xénolites de "
                    "péridotites des kimberlites d'Afrique australe sont des "
                    "échantillons directs du manteau.",
                    width=54,
                ),
                font_size=22,
            ),
            box_width=11.9,
        )
        xenolite_def.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Prenons un exemple traité : le xénolite. C'est un fragment "
                "de roche étranger — du grec xénos, étranger, et lithos, "
                "pierre — arraché aux parois du conduit volcanique ou "
                "directement au manteau, puis remonté en surface, enfermé "
                "dans une lave. Les xénolites de péridotites des kimberlites "
                "d'Afrique australe sont ainsi des échantillons directs du "
                "manteau, remontés sans avoir jamais été forés."
            )
        ) as tracker:
            self.play(FadeIn(xenolite_def))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(xenolite_def))

        # --- À retenir : les objectifs du chapitre --------------------------
        entete_obj = Text("Objectifs du chapitre", font_size=26, color=YELLOW, weight="BOLD")
        entete_obj.next_to(titre, DOWN, buff=0.45)

        objectifs = _bullets(
            [
                "Distinguer indices de surface et indices indirects.",
                "Expliquer la nature des ondes P et S et leur réflexion/réfraction.",
                "Déterminer les enveloppes du globe à partir de documents.",
                "Situer les discontinuités de Moho, Gutenberg et Lehmann.",
                "Différencier découpage chimique et découpage mécanique.",
                "Calculer vitesse, distance épicentrale, densité, pression, température.",
            ],
            font_size=20,
            width=52,
        )
        objectifs.next_to(entete_obj, DOWN, buff=0.35)
        bloc_obj = VGroup(entete_obj, objectifs)
        _garde_fou(bloc_obj)

        with self.voiceover(
            text=(
                "À l'issue de ce chapitre, dense et calculatoire, l'élève "
                "doit être capable de distinguer indices de surface et "
                "indices indirects ; d'expliquer la nature des ondes P et S "
                "ainsi que leur réflexion et leur réfraction ; de déterminer "
                "les enveloppes du globe à partir de documents ; de situer "
                "les discontinuités de Moho, de Gutenberg et de Lehmann ; de "
                "différencier le découpage chimique du découpage mécanique ; "
                "et de calculer vitesse d'onde, distance épicentrale, "
                "densité, pression et température internes."
            )
        ) as tracker:
            self.play(FadeIn(entete_obj))
            self.play(FadeIn(objectifs))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(entete_obj), FadeOut(objectifs))

        # --- Piège à éviter : la limite des indices de surface --------------
        piege = warning_box(
            Text(
                _wrap(
                    "Les indices de surface ne renseignent que sur les 10 à "
                    "100 premiers kilomètres, alors que le centre de la "
                    "Terre est à 6 371 km de profondeur. Croire qu'un forage "
                    "ou un xénolite suffit à connaître tout l'intérieur du "
                    "globe est une erreur : il faut des indices indirects.",
                    width=54,
                ),
                font_size=22,
            ),
            box_width=12.0,
        )
        piege.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Attention, piège à éviter : les indices de surface ne "
                "renseignent que sur les dix à cent premiers kilomètres, "
                "alors que le centre de la Terre se situe à six mille trois "
                "cent soixante et onze kilomètres de profondeur. Croire "
                "qu'un forage ou un xénolite suffit à connaître tout "
                "l'intérieur du globe est une erreur : il faut, pour aller "
                "plus loin, des indices indirects, que nous découvrirons "
                "dans les scènes suivantes."
            )
        ) as tracker:
            self.play(FadeIn(piege))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(titre), FadeOut(piege))
