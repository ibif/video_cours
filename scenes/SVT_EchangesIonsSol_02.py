"""
scenes/SVT_EchangesIonsSol_02.py — Chapitre 8 (1ereD, SVT), scène 02.

§ 8.1.1-8.1.2 Composition du sol et complexe argilo-humique : définition du
sol, définition de l'humus, exemple d'analyse qualitative d'une terre de
jardin (3 expériences), définition du complexe argilo-humique (CAH) avec
schéma de la micelle, propriété du pouvoir absorbant, attention
adsorption ≠ absorption. Source : 1ereD/SVT.pdf, pages 103-104.
"""

import textwrap

from manim import (
    BLUE,
    DOWN,
    GREEN,
    LEFT,
    ORANGE,
    PURPLE,
    RED,
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
from shapes.boxes import definition_box, property_box, scene_title, warning_box


def _wrap(text: str, width: int = 56) -> str:
    return "\n".join(textwrap.fill(line, width=width) for line in text.split("\n"))


def _bullets(items, font_size=24, color=WHITE, width=54):
    lines = VGroup(
        *[Text(f"• {_wrap(it, width=width)}", font_size=font_size, color=color) for it in items]
    )
    lines.arrange(DOWN, aligned_edge=LEFT, buff=0.22)
    return lines


def _fit(mobject, top_anchor):
    """Réduit l'échelle de `mobject` si son bas dépasse le cadre visible,
    en conservant l'ancrage en haut (garde-fou pour boîte dense)."""
    bas_visible = -config.frame_height / 2 + 0.25
    hauteur_dispo = top_anchor - bas_visible
    if mobject.height > hauteur_dispo:
        mobject.scale(hauteur_dispo / mobject.height, about_point=mobject.get_top())
    return mobject


class CompositionDuSolEtCAH(NotionScene):
    def construct(self):
        titre = scene_title("8.1 — Composition du sol, complexe argilo-humique")
        titre.scale(0.58)
        titre.to_edge(UP)

        # --- Énoncé : la plante autotrophe a besoin d'ions du sol ---------
        intro = Text(
            _wrap(
                "La plante verte est autotrophe : elle fabrique sa matière "
                "organique par photosynthèse, mais a besoin d'éléments "
                "minéraux qu'elle ne trouve que dans le sol, sous forme "
                "d'ions dissous.",
                width=56,
            ),
            font_size=26,
            color=WHITE,
        )
        intro.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "La plante verte est autotrophe : elle fabrique sa propre "
                "matière organique par photosynthèse. Mais pour cela, elle "
                "a besoin d'éléments minéraux qu'elle ne trouve que dans le "
                "sol, sous forme d'ions dissous. Voyons d'abord de quoi le "
                "sol est fait."
            )
        ) as tracker:
            self.play(Write(titre))
            self.play(FadeIn(intro))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(intro))

        def_sol = definition_box(
            Text(
                _wrap(
                    "Le sol est la couche superficielle et meuble de "
                    "l'écorce terrestre. Il résulte de l'altération lente "
                    "de la roche-mère (pluie, chaleur, gel, vent) et de la "
                    "décomposition des débris d'êtres vivants. C'est le "
                    "milieu d'ancrage des plantes et la source de leurs "
                    "éléments minéraux.",
                    width=54,
                ),
                font_size=22,
            ),
            box_width=11.8,
        )
        def_sol.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Le sol est la couche superficielle et meuble de l'écorce "
                "terrestre. Il résulte de l'altération lente de la "
                "roche-mère, sous l'effet de la pluie, de la chaleur, du "
                "gel et du vent, et de la décomposition des débris d'êtres "
                "vivants. C'est le milieu d'ancrage des plantes, et la "
                "source de leurs éléments minéraux."
            )
        ) as tracker:
            self.play(FadeIn(def_sol))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(def_sol))

        def_humus = definition_box(
            Text(
                _wrap(
                    "L'humus est la matière organique du sol, issue de la "
                    "décomposition (humification) des restes végétaux et "
                    "animaux par les micro-organismes. Brun foncé, "
                    "concentré dans les premiers centimètres. Triple rôle "
                    ": réserve nutritive à libération lente ; améliore la "
                    "structure du sol ; participe au pouvoir absorbant "
                    "avec l'argile.",
                    width=54,
                ),
                font_size=22,
            ),
            box_width=11.8,
        )
        def_humus.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Un échantillon de terre révèle trois phases mélangées, "
                "plus des organismes vivants : les particules minérales, "
                "de tailles variées, la matière organique appelée humus, "
                "l'eau avec ses ions dissous, et l'air du sol. L'humus est "
                "la matière organique du sol, issue de la décomposition "
                "des restes végétaux et animaux par les micro-organismes. "
                "Brun foncé, concentré dans les premiers centimètres, il "
                "joue un triple rôle : réserve nutritive à libération "
                "lente, amélioration de la structure du sol, et "
                "participation au pouvoir absorbant, avec l'argile."
            )
        ) as tracker:
            self.play(FadeIn(def_humus))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(def_humus))

        # --- Exemple traité : analyse qualitative d'une terre de jardin ---
        exemple_analyse = property_box(
            _bullets(
                [
                    "1. Terre chauffée doucement, couverte : gouttelettes "
                    "sur les parois froides -> le sol contient de l'eau.",
                    "2. Terre séchée chauffée fortement : fumée âcre, "
                    "masse diminue -> le sol contient de l'humus.",
                    "3. Terre délayée dans l'eau, agitée, reposée : sable "
                    "au fond, limon ensuite, argile en suspension, débris "
                    "flottent ; le liquide conduit le courant -> ions "
                    "dissous.",
                ],
                font_size=21,
                width=52,
            ),
            box_width=12.2,
        )
        exemple_analyse.next_to(titre, DOWN, buff=0.45)

        with self.voiceover(
            text=(
                "Trois expériences simples le prouvent. Première "
                "expérience : on chauffe doucement de la terre fraîche "
                "dans un récipient couvert ; des gouttelettes d'eau se "
                "déposent sur les parois froides : le sol contient donc de "
                "l'eau. Deuxième expérience : on chauffe fortement de la "
                "terre séchée ; une fumée âcre s'échappe et la masse "
                "diminue : le sol contient de la matière organique, "
                "l'humus. Troisième expérience : on délaye de la terre "
                "dans l'eau, on agite, on laisse reposer ; le sable se "
                "dépose au fond, le limon ensuite, l'argile reste en "
                "suspension longtemps, et des débris flottent ; le liquide "
                "surnageant conduit le courant électrique, preuve qu'il "
                "contient des ions dissous. Conclusion : le sol est fait "
                "de particules minérales de tailles différentes et d'ions "
                "en solution."
            )
        ) as tracker:
            self.play(FadeIn(exemple_analyse))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(exemple_analyse))

        # --- Raisonnement : le complexe argilo-humique et son schéma ------
        def_cah = definition_box(
            Text(
                _wrap(
                    "Dans un sol de bonne qualité, l'argile et l'humus "
                    "s'associent pour former le complexe argilo-humique "
                    "(CAH), ou complexe absorbant. Ses micelles portent à "
                    "leur surface des charges électriques négatives, qui "
                    "attirent et retiennent les cations de la solution du "
                    "sol.",
                    width=54,
                ),
                font_size=22,
            ),
            box_width=11.8,
        )
        def_cah.next_to(titre, DOWN, buff=0.45)

        with self.voiceover(
            text=(
                "Dans un sol de bonne qualité, l'argile et l'humus "
                "s'associent pour former le complexe argilo-humique, ou "
                "CAH, aussi appelé complexe absorbant. Ses micelles "
                "portent à leur surface des charges électriques "
                "négatives, qui attirent et retiennent les cations de la "
                "solution du sol."
            )
        ) as tracker:
            self.play(FadeIn(def_cah))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(def_cah))

        # Schéma de la micelle : cercle central chargé négativement, cations
        # attirés autour, anions libres qui s'éloignent.
        micelle = Circle(radius=1.0, color=ORANGE, fill_color=ORANGE, fill_opacity=0.35, stroke_width=3)
        micelle_label = Text("micelle du CAH", font_size=18, color=WHITE).move_to(micelle.get_center())
        charges_neg = VGroup(
            *[
                Text("−", font_size=26, color=WHITE, weight="BOLD").move_to(
                    micelle.point_at_angle(angle)
                )
                for angle in [0, 60, 120, 180, 240, 300]
            ]
        )
        micelle_group = VGroup(micelle, charges_neg, micelle_label)

        cation_labels = ["Ca2+", "Mg2+", "K+", "NH4+", "H+"]
        cation_colors = [BLUE, PURPLE, GREEN, YELLOW, RED]
        cations = VGroup()
        liens = VGroup()
        angles_cations = [30, 90, 150, 210, 270]
        for label, color, angle in zip(cation_labels, cation_colors, angles_cations):
            pt_bord = micelle.point_at_angle(angle)
            direction = pt_bord - micelle.get_center()
            direction = direction / (direction[0] ** 2 + direction[1] ** 2) ** 0.5
            pt_dot = pt_bord + direction * 0.55
            dot = Dot(pt_dot, color=color, radius=0.09)
            txt = Text(label, font_size=18, color=color).next_to(dot, direction, buff=0.08)
            lien = Line(pt_bord, pt_dot, color=color, stroke_width=2)
            cations.add(VGroup(dot, txt))
            liens.add(lien)

        anion_txt = Text("anions (NO3−, Cl−...) : libres, non retenus", font_size=18, color=WHITE)
        anion_arrow = Text("→ →", font_size=20, color=WHITE)
        anions_group = VGroup(anion_arrow, anion_txt).arrange(RIGHT, buff=0.15)

        schema_cah = VGroup(micelle_group, liens, cations)
        schema_cah.scale(0.95)
        schema_cah.next_to(titre, DOWN, buff=0.6)
        anions_group.next_to(schema_cah, DOWN, buff=0.4)
        schema_complet = VGroup(schema_cah, anions_group)
        _fit(schema_complet, titre.get_bottom()[1] - 0.3)

        with self.voiceover(
            text=(
                "Voici la micelle du complexe argilo-humique : sa surface "
                "est chargée négativement. Elle attire donc et retient les "
                "cations : le calcium deux plus, le magnésium deux plus, "
                "le potassium plus, l'ammonium plus, et l'hydrogène plus. "
                "En revanche, les anions, comme le nitrate ou le chlorure, "
                "ne sont pas retenus : ils restent libres dans la solution "
                "du sol, et peuvent être facilement lessivés par les "
                "pluies."
            )
        ) as tracker:
            self.play(FadeIn(micelle_group))
            self.play(FadeIn(liens), FadeIn(cations))
            self.play(FadeIn(anions_group))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(schema_complet))

        prop_absorbant = property_box(
            Text(
                _wrap(
                    "Le CAH retient à sa surface, par liaisons électriques "
                    "réversibles, les cations : c'est l'adsorption. Les "
                    "cations retenus forment la réserve échangeable du "
                    "sol, protégés du lessivage mais disponibles pour la "
                    "plante.",
                    width=54,
                ),
                font_size=23,
            ),
            box_width=11.8,
        )
        prop_absorbant.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "C'est ce qu'on appelle le pouvoir absorbant du sol : le "
                "complexe argilo-humique retient à sa surface, par des "
                "liaisons électriques réversibles, les cations. Ce "
                "phénomène s'appelle l'adsorption. Les cations ainsi "
                "retenus forment la réserve échangeable du sol : ils sont "
                "protégés du lessivage par les pluies, mais restent "
                "disponibles pour la plante."
            )
        ) as tracker:
            self.play(FadeIn(prop_absorbant))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(prop_absorbant))

        # --- Piège à éviter : adsorption ≠ absorption ----------------------
        piege = warning_box(
            Text(
                _wrap(
                    "L'adsorption (avec un d) : fixation d'un ion à la "
                    "surface d'un support (le CAH). L'absorption (avec un "
                    "b) : entrée d'une substance à l'intérieur d'un "
                    "organisme/cellule (la racine). Les cations sont "
                    "d'abord adsorbés sur le complexe, puis absorbés par "
                    "la racine.",
                    width=54,
                ),
                font_size=22,
            ),
            box_width=11.8,
        )
        piege.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Attention à ne pas confondre deux mots très proches. "
                "L'adsorption, avec un d, c'est la fixation d'un ion à la "
                "surface d'un support, ici le complexe argilo-humique. "
                "L'absorption, avec un b, c'est l'entrée d'une substance à "
                "l'intérieur d'un organisme ou d'une cellule, ici la "
                "racine. Les cations sont donc d'abord adsorbés sur le "
                "complexe, puis, dans un second temps, absorbés par la "
                "racine."
            )
        ) as tracker:
            self.play(FadeIn(piege))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(titre), FadeOut(piege))
