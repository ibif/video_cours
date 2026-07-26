"""
scenes/SVT_StructureInterneGlobe_09.py — Chapitre 7 (1ereC, SVT), scène 09.

§ III.3 La discontinuité de Lehmann : découverte (1936), profondeur
5150 km, sépare noyau externe/noyau interne, signature (remontée vP
10 → 11, ondes P réfléchies, noyau interne solide) + § III.4 tableau
récapitulatif des 3 discontinuités + graphique vitesse des ondes P et S en
fonction de la profondeur. Source : 1ereC/SVT.pdf, page 74.
"""

import textwrap

from manim import DOWN, LEFT, RIGHT, UP, WHITE, YELLOW, Axes, DashedLine, FadeIn, FadeOut, Text, VGroup, Write, config

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


def _tableau(rows, font_size=17, header_color=YELLOW, body_color=WHITE, col_alignments=None, buff=(0.45, 0.2)):
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
    bas_visible = -config.frame_height / 2 + 0.3
    hauteur_dispo = mobject.get_top()[1] - bas_visible
    if mobject.height > hauteur_dispo > 0:
        mobject.scale(hauteur_dispo / mobject.height, about_point=mobject.get_top())


class DiscontinuiteDeLehmannEtSynthese(NotionScene):
    def construct(self):
        titre = scene_title("III.3 — La discontinuité de Lehmann")
        titre.scale(0.65)
        titre.to_edge(UP)

        # --- Énoncé : comment sait-on que le noyau a deux parties ? ----------
        intro = Text(
            _wrap(
                "En 1936, la sismologue danoise Inge Lehmann détecte des "
                "ondes P inattendues, à l'intérieur même du noyau : le "
                "noyau, jusque-là considéré comme liquide, cache en réalité "
                "une seconde frontière interne.",
                width=56,
            ),
            font_size=23,
            color=WHITE,
        )
        intro.next_to(titre, DOWN, buff=0.55)

        with self.voiceover(
            text=(
                "En mille neuf cent trente-six, la sismologue danoise Inge "
                "Lehmann détecte des ondes P inattendues, à l'intérieur même "
                "du noyau : le noyau, jusque-là considéré comme entièrement "
                "liquide, cache en réalité une seconde frontière interne."
            )
        ) as tracker:
            self.play(Write(titre))
            self.play(FadeIn(intro))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(intro))

        # --- Définition / signature de la discontinuité de Lehmann -----------
        definition = definition_box(
            Text(
                _wrap(
                    "La discontinuité de Lehmann se situe à 5 150 km de "
                    "profondeur et sépare le noyau externe du noyau interne "
                    "(la « graine »). Signature : nouvelle augmentation de "
                    "vP (d'environ 10 à 11 km/s) et existence d'ondes P "
                    "réfléchies à cette limite : le noyau interne est "
                    "SOLIDE.",
                    width=54,
                ),
                font_size=20,
            ),
            box_width=11.9,
        )
        definition.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "La discontinuité de Lehmann se situe à cinq mille cent "
                "cinquante kilomètres de profondeur et sépare le noyau "
                "externe du noyau interne, aussi appelé la graine. Elle se "
                "traduit par une nouvelle augmentation de la vitesse des "
                "ondes P, qui passe d'environ dix à onze kilomètres par "
                "seconde, et par l'existence d'ondes P réfléchies à cette "
                "limite : preuve que le noyau interne est solide."
            )
        ) as tracker:
            self.play(FadeIn(definition))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(definition))

        # --- Animation du raisonnement : le graphique vitesse / profondeur ---
        axes = Axes(
            x_range=[0, 6371, 1000],
            y_range=[0, 14, 2],
            x_length=8.5,
            y_length=4.2,
            axis_config={"font_size": 16, "include_numbers": False, "stroke_width": 2},
        )
        axes.next_to(titre, DOWN, buff=0.45)

        x_label = Text("Profondeur (km)", font_size=15, color=WHITE).next_to(axes.x_axis, DOWN, buff=0.2)
        y_label = Text("Vitesse (km/s)", font_size=15, color=WHITE).next_to(axes.y_axis, LEFT, buff=0.2).rotate(1.5708)

        # Courbe vP simplifiée par segments (croûte -> manteau -> Gutenberg -> Lehmann -> centre)
        pts_p = [(0, 6), (35, 8), (2900, 13.7), (2900, 8), (5150, 10), (5150, 11), (6371, 11.3)]
        courbe_p = VGroup(
            *[
                axes.plot_line_graph(
                    x_values=[pts_p[i][0], pts_p[i + 1][0]],
                    y_values=[pts_p[i][1], pts_p[i + 1][1]],
                    line_color="#4DABF7",
                    add_vertex_dots=False,
                    stroke_width=3,
                )
                for i in range(len(pts_p) - 1)
            ]
        )

        # Courbe vS simplifiée (s'arrête net à Gutenberg, reprend légèrement à Lehmann pour la graine... en fait vS reste nulle dans tout le noyau externe/interne selon modèle simple)
        pts_s = [(0, 3.5), (35, 4.5), (2900, 7.3)]
        courbe_s = VGroup(
            *[
                axes.plot_line_graph(
                    x_values=[pts_s[i][0], pts_s[i + 1][0]],
                    y_values=[pts_s[i][1], pts_s[i + 1][1]],
                    line_color=YELLOW,
                    add_vertex_dots=False,
                    stroke_width=3,
                )
                for i in range(len(pts_s) - 1)
            ]
        )

        ligne_gutenberg = DashedLine(axes.c2p(2900, 0), axes.c2p(2900, 14), color="#FF6B6B", stroke_width=2)
        label_gutenberg = Text("Gutenberg\n2 900 km", font_size=12, color="#FF6B6B").next_to(ligne_gutenberg, UP, buff=0.05)
        ligne_lehmann = DashedLine(axes.c2p(5150, 0), axes.c2p(5150, 14), color="#69DB7C", stroke_width=2)
        label_lehmann = Text("Lehmann\n5 150 km", font_size=12, color="#69DB7C").next_to(ligne_lehmann, UP, buff=0.05)

        legende_p = Text("— vP", font_size=14, color="#4DABF7")
        legende_s = Text("— vS", font_size=14, color=YELLOW)
        legende = VGroup(legende_p, legende_s).arrange(RIGHT, buff=0.5)
        legende.next_to(axes, DOWN, buff=0.55)

        schema = VGroup(axes, x_label, y_label, courbe_p, courbe_s, ligne_gutenberg, label_gutenberg, ligne_lehmann, label_lehmann, legende)
        schema.scale(0.82)
        schema.next_to(titre, DOWN, buff=0.3)

        with self.voiceover(
            text=(
                "Voici le graphique de la vitesse des ondes P et S en "
                "fonction de la profondeur. La courbe bleue, celle des "
                "ondes P, croît progressivement, chute brutalement à deux "
                "mille neuf cents kilomètres, au niveau de Gutenberg, puis "
                "remonte à nouveau à cinq mille cent cinquante kilomètres, "
                "au niveau de Lehmann. La courbe jaune, celle des ondes S, "
                "s'arrête net à Gutenberg et ne réapparaît jamais : entre "
                "deux mille neuf cents et six mille trois cent soixante et "
                "onze kilomètres, les ondes S sont totalement absentes, "
                "preuve que tout le noyau, externe comme interne, empêche "
                "leur propagation directe — seule la remontée de vP signale "
                "que le centre redevient localement plus rigide."
            )
        ) as tracker:
            self.play(FadeIn(axes), FadeIn(x_label), FadeIn(y_label))
            self.play(FadeIn(courbe_p))
            self.play(FadeIn(courbe_s))
            self.play(FadeIn(ligne_gutenberg), FadeIn(label_gutenberg))
            self.play(FadeIn(ligne_lehmann), FadeIn(label_lehmann))
            self.play(FadeIn(legende))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(schema))

        # --- Exemple traité / tableau récapitulatif des 3 discontinuités -----
        entete_tab = Text("Tableau récapitulatif des trois discontinuités", font_size=22, color=YELLOW, weight="BOLD")
        entete_tab.next_to(titre, DOWN, buff=0.4)

        tableau = _tableau(
            [
                ["Discontinuité", "Année", "Profondeur", "Sépare", "Signature (vP)"],
                ["Moho", "1909", "5-70 km", "Croûte/Manteau", "6 → 8 km/s"],
                ["Gutenberg", "1914", "2 900 km", "Manteau/Noyau", "13,7 → 8 ; S disparaît"],
                ["Lehmann", "1936", "5 150 km", "Noyau ext./int.", "10 → 11 ; P réfléchies"],
            ],
            font_size=16,
        )
        tableau.next_to(entete_tab, DOWN, buff=0.35)
        bloc_tab = VGroup(entete_tab, tableau)
        _garde_fou(bloc_tab)

        with self.voiceover(
            text=(
                "Résumons dans un tableau les trois discontinuités "
                "majeures. Le Moho, découvert en mille neuf cent neuf, "
                "situé entre cinq et soixante-dix kilomètres, sépare la "
                "croûte du manteau : vP passe de six à huit kilomètres par "
                "seconde. Gutenberg, découvert en mille neuf cent quatorze, "
                "à deux mille neuf cents kilomètres, sépare le manteau du "
                "noyau : vP chute à huit, et les ondes S disparaissent. "
                "Lehmann, découvert en mille neuf cent trente-six, à cinq "
                "mille cent cinquante kilomètres, sépare le noyau externe "
                "du noyau interne : vP remonte à onze, avec des ondes P "
                "réfléchies."
            )
        ) as tracker:
            self.play(FadeIn(entete_tab))
            self.play(FadeIn(tableau))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(entete_tab), FadeOut(tableau))

        # --- À retenir ---------------------------------------------------------
        retenir = _bullets(
            [
                "Lehmann (1936) : sépare noyau externe (liquide) et noyau interne (solide).",
                "vP remonte de 10 à 11 km/s ; ondes P réfléchies à 5 150 km.",
                "Ordre, du centre vers la surface : Lehmann, Gutenberg, Moho.",
            ],
            width=50,
        )
        entete_retenir = Text("À retenir", font_size=27, color=YELLOW, weight="BOLD")
        entete_retenir.next_to(titre, DOWN, buff=0.5)
        retenir.next_to(entete_retenir, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "À retenir : la discontinuité de Lehmann sépare le noyau "
                "externe liquide du noyau interne solide, avec une remontée "
                "de la vitesse des ondes P de dix à onze kilomètres par "
                "seconde, et des ondes P réfléchies. Dans l'ordre, du "
                "centre vers la surface, on rencontre Lehmann, puis "
                "Gutenberg, puis le Moho."
            )
        ) as tracker:
            self.play(FadeIn(entete_retenir))
            self.play(FadeIn(retenir))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(entete_retenir), FadeOut(retenir))

        # --- Piège à éviter -----------------------------------------------------
        piege = warning_box(
            Text(
                _wrap(
                    "Ne pas confondre noyau externe et noyau interne : "
                    "l'externe est LIQUIDE (Gutenberg), l'interne, la "
                    "graine, est SOLIDE (Lehmann) malgré une température "
                    "encore plus élevée — nous verrons pourquoi (pression) "
                    "plus loin dans ce chapitre.",
                    width=54,
                ),
                font_size=21,
            ),
            box_width=12.0,
        )
        piege.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Attention, piège à éviter : ne confondez jamais noyau "
                "externe et noyau interne. Le noyau externe, révélé par "
                "Gutenberg, est liquide. Le noyau interne, la graine, "
                "révélé par Lehmann, est solide, malgré une température "
                "encore plus élevée en son centre. Nous expliquerons ce "
                "paradoxe apparent plus loin dans ce chapitre, grâce à la "
                "pression."
            )
        ) as tracker:
            self.play(FadeIn(piege))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(titre), FadeOut(piege))
