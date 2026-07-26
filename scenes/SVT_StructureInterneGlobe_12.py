"""
scenes/SVT_StructureInterneGlobe_12.py — Chapitre 7 (1ereC, SVT), scène 12.

§ V. Lithosphère et asthénosphère : un découpage mécanique — lithosphère
(croûte + manteau supérieur rigide, plaques lithosphériques), asthénosphère
(péridotites partiellement fondues, ductile), indices de l'asthénosphère
(ralentissement des ondes, isostasie) + tableau « les deux découpages à ne
pas confondre » + méthode « la lithosphère n'est pas la croûte ».
Source : 1ereC/SVT.pdf, pages 76-77.
"""

import textwrap

from manim import DOWN, LEFT, RIGHT, UP, WHITE, YELLOW, FadeIn, FadeOut, Line, Text, VGroup, Write, config

from shapes.base_scene import NotionScene
from shapes.boxes import definition_box, method_box, scene_title, warning_box


def _wrap(text: str, width: int = 56) -> str:
    return "\n".join(textwrap.fill(line, width=width) for line in text.split("\n"))


def _bullets(items, font_size=23, color=WHITE, width=52):
    lines = VGroup(
        *[Text(f"• {_wrap(it, width=width)}", font_size=font_size, color=color) for it in items]
    )
    lines.arrange(DOWN, aligned_edge=LEFT, buff=0.22)
    return lines


def _tableau(rows, font_size=16, header_color=YELLOW, body_color=WHITE, col_alignments=None, buff=(0.4, 0.2)):
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


class LithosphereEtAsthenosphere(NotionScene):
    def construct(self):
        titre = scene_title("V — Lithosphère et asthénosphère")
        titre.scale(0.68)
        titre.to_edge(UP)

        # --- Énoncé : un second découpage, mécanique cette fois --------------
        intro = Text(
            _wrap(
                "Croûte, manteau, noyau : un découpage selon la composition "
                "chimique. Mais les sismologues ont montré que la partie "
                "supérieure du globe peut aussi être découpée selon la "
                "rigidité des roches — un découpage tout différent.",
                width=56,
            ),
            font_size=23,
            color=WHITE,
        )
        intro.next_to(titre, DOWN, buff=0.55)

        with self.voiceover(
            text=(
                "Croûte, manteau, noyau : voilà un découpage selon la "
                "composition chimique des matériaux. Mais les sismologues "
                "ont montré que la partie supérieure du globe peut aussi "
                "être découpée selon un tout autre critère, le comportement "
                "mécanique, c'est-à-dire la rigidité des roches."
            )
        ) as tracker:
            self.play(Write(titre))
            self.play(FadeIn(intro))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(intro))

        # --- Définitions lithosphère / asthénosphère --------------------------
        lithosphere_def = definition_box(
            Text(
                _wrap(
                    "Lithosphère : enveloppe superficielle RIGIDE du globe, "
                    "~100 km (60-100 km sous les océans ; 100-250 km sous "
                    "les vieux continents comme le bouclier ouest-africain). "
                    "Comprend la croûte + la partie supérieure du manteau. "
                    "Fragmentée en plaques lithosphériques ; foyers des "
                    "séismes presque tous situés en son sein.",
                    width=54,
                ),
                font_size=18,
            ),
            box_width=11.9,
        )
        lithosphere_def.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "La lithosphère est l'enveloppe superficielle rigide du "
                "globe, épaisse d'environ cent kilomètres, de soixante à "
                "cent kilomètres sous les océans, et de cent à deux cent "
                "cinquante kilomètres sous les vieux continents, comme le "
                "bouclier ouest-africain. Elle comprend la croûte et la "
                "partie supérieure du manteau, dite manteau lithosphérique. "
                "Elle est fragmentée en blocs rigides, les plaques "
                "lithosphériques. Sa rigidité explique qu'elle se rompe "
                "brutalement lors des séismes : les foyers sont presque "
                "tous situés dans la lithosphère."
            )
        ) as tracker:
            self.play(FadeIn(lithosphere_def))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(lithosphere_def))

        asthenosphere_def = definition_box(
            Text(
                _wrap(
                    "Asthénosphère : partie du manteau sous la lithosphère "
                    "(~100-350 km), péridotites PARTIELLEMENT fondues (1 à "
                    "10 % de liquide). DUCTILE (plastique, déformable sans "
                    "se rompre), s'écoule lentement comme un matériau très "
                    "visqueux.",
                    width=54,
                ),
                font_size=20,
            ),
            box_width=11.9,
        )
        asthenosphere_def.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "L'asthénosphère est la partie du manteau située sous la "
                "lithosphère, environ de cent à trois cent cinquante "
                "kilomètres de profondeur, constituée de péridotites "
                "partiellement fondues, seulement un à dix pour cent de "
                "liquide. Elle est ductile, c'est-à-dire plastique, "
                "déformable sans se rompre, et s'écoule très lentement, à "
                "la manière d'un matériau très visqueux."
            )
        ) as tracker:
            self.play(FadeIn(asthenosphere_def))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(asthenosphere_def))

        # --- Animation du raisonnement : schéma des deux limites ---------------
        surface = Line(LEFT * 3.3, RIGHT * 3.3, color=WHITE, stroke_width=3).shift(UP * 1.6)
        moho = Line(LEFT * 3.3, RIGHT * 3.3, color=YELLOW, stroke_width=2).shift(UP * 1.15)
        base_litho = Line(LEFT * 3.3, RIGHT * 3.3, color="#4DABF7", stroke_width=2).shift(UP * 0.35)

        zone_croute = Line(LEFT * 3.3, RIGHT * 3.3, stroke_width=45, color="#A9A9A9").move_to(UP * 1.38)
        zone_litho_manteau = Line(LEFT * 3.3, RIGHT * 3.3, stroke_width=45, color="#C2B280").move_to(UP * 0.75)
        zone_astheno = Line(LEFT * 3.3, RIGHT * 3.3, stroke_width=55, color="#D9822B").move_to(DOWN * 0.15)

        label_moho = Text("Moho (limite chimique)", font_size=13, color=YELLOW).next_to(moho, RIGHT, buff=0.15).shift(UP*0.1)
        label_base_litho = Text("Base de la lithosphère\n(limite mécanique, ~100 km)", font_size=12, color="#4DABF7").next_to(base_litho, RIGHT, buff=0.15)

        label_litho = Text("LITHOSPHÈRE (rigide)", font_size=14, color=WHITE, weight="BOLD").next_to(surface, UP, buff=0.3)
        label_astheno = Text("ASTHÉNOSPHÈRE (ductile)", font_size=14, color=WHITE, weight="BOLD").move_to(DOWN * 0.9)

        schema = VGroup(
            zone_croute, zone_litho_manteau, zone_astheno,
            surface, moho, base_litho,
            label_moho, label_base_litho, label_litho, label_astheno,
        )
        schema.scale(0.85)
        schema.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Ce schéma superpose les deux découpages. Le Moho, en "
                "jaune, est une limite chimique : il sépare la croûte, en "
                "gris, du manteau. Mais la base de la lithosphère, en bleu, "
                "est une limite mécanique bien plus basse, vers cent "
                "kilomètres : elle sépare la lithosphère rigide, qui "
                "englobe la croûte ET le sommet du manteau, de "
                "l'asthénosphère ductile, en dessous."
            )
        ) as tracker:
            self.play(FadeIn(zone_croute), FadeIn(zone_litho_manteau), FadeIn(zone_astheno))
            self.play(FadeIn(surface), FadeIn(moho), FadeIn(label_moho))
            self.play(FadeIn(base_litho), FadeIn(label_base_litho))
            self.play(FadeIn(label_litho), FadeIn(label_astheno))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(schema))

        # --- Exemple traité : les indices de l'asthénosphère -------------------
        indices = definition_box(
            Text(
                _wrap(
                    "Indices de l'asthénosphère : ralentissement des ondes "
                    "P et S entre 100 et 350 km (zone de basse vitesse), "
                    "sans disparition des ondes S (fusion seulement "
                    "partielle) ; l'isostasie, la lithosphère « flotte » "
                    "sur l'asthénosphère comme un iceberg sur l'eau.",
                    width=54,
                ),
                font_size=20,
            ),
            box_width=11.9,
        )
        indices.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Exemple traité : quels sont les indices de l'existence de "
                "l'asthénosphère ? D'abord, un ralentissement des ondes P "
                "et S entre cent et trois cent cinquante kilomètres, une "
                "zone dite de basse vitesse, mais sans disparition des "
                "ondes S : la fusion n'est donc que partielle. Ensuite, "
                "l'isostasie : la lithosphère flotte sur l'asthénosphère "
                "comme un iceberg sur l'eau, avec des chaînes de montagnes "
                "qui possèdent des racines profondes, et des blocs qui "
                "remontent ou s'enfoncent lentement, comme après la fonte "
                "des grands glaciers."
            )
        ) as tracker:
            self.play(FadeIn(indices))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(indices))

        # --- À retenir : tableau des deux découpages ----------------------------
        entete_tab = Text("Les deux découpages à ne pas confondre", font_size=21, color=YELLOW, weight="BOLD")
        entete_tab.next_to(titre, DOWN, buff=0.4)

        tableau = _tableau(
            [
                ["Découpage", "Critère", "Enveloppes"],
                ["Chimique", "Nature des roches", "Croûte - Manteau - Noyau"],
                ["", "", "(limites : Moho, Gutenberg, Lehmann)"],
                ["Mécanique", "Rigidité (rigide/ductile)", "Lithosphère - Asthénosphère"],
                ["", "", "- Mésosphère"],
            ],
            font_size=16,
        )
        tableau.next_to(entete_tab, DOWN, buff=0.35)
        bloc_tab = VGroup(entete_tab, tableau)
        _garde_fou(bloc_tab)

        with self.voiceover(
            text=(
                "Résumons dans un tableau. Le découpage chimique, fondé sur "
                "la nature des roches, donne croûte, manteau et noyau, "
                "limités par Moho, Gutenberg et Lehmann. Le découpage "
                "mécanique, fondé sur la rigidité, donne lithosphère, "
                "asthénosphère, puis mésosphère, la partie du manteau "
                "redevenue rigide sous l'asthénosphère car la pression y "
                "empêche la fusion malgré la température."
            )
        ) as tracker:
            self.play(FadeIn(entete_tab))
            self.play(FadeIn(tableau))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(entete_tab), FadeOut(tableau))

        # --- Méthode point clé : la lithosphère n'est pas la croûte -----------
        methode = method_box(
            Text(
                _wrap(
                    "Point clé : la lithosphère n'est pas la croûte. Elle "
                    "comprend la croûte PLUS le manteau supérieur rigide. "
                    "Le Moho est une limite chimique ; la base de la "
                    "lithosphère est une limite mécanique, située vers "
                    "100 km, donc au-dessous du Moho.",
                    width=54,
                ),
                font_size=20,
            ),
            box_width=11.9,
        )
        methode.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Point clé à retenir absolument : la lithosphère n'est pas "
                "la croûte. Elle comprend la croûte, plus le manteau "
                "supérieur rigide. Le Moho est une limite chimique ; la "
                "base de la lithosphère est une limite mécanique, située "
                "vers cent kilomètres, donc bien au-dessous du Moho."
            )
        ) as tracker:
            self.play(FadeIn(methode))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(methode))

        # --- Piège à éviter -----------------------------------------------------
        piege = warning_box(
            Text(
                _wrap(
                    "Erreur fréquente : écrire que « la lithosphère est "
                    "située entre le Moho et Gutenberg ». C'est FAUX : la "
                    "lithosphère s'arrête vers 100 km (limite mécanique), "
                    "bien avant Gutenberg (2 900 km, limite chimique).",
                    width=54,
                ),
                font_size=21,
            ),
            box_width=12.0,
        )
        piege.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Attention, piège à éviter : une erreur fréquente consiste "
                "à écrire que la lithosphère est située entre le Moho et "
                "Gutenberg. C'est faux : la lithosphère s'arrête vers cent "
                "kilomètres seulement, une limite mécanique, bien avant "
                "Gutenberg, situé à deux mille neuf cents kilomètres, une "
                "limite chimique. Ne mélangez jamais les deux découpages."
            )
        ) as tracker:
            self.play(FadeIn(piege))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(titre), FadeOut(piege))
