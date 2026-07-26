"""
scenes/Chimie_ComposesOxygenes_02.py — Chapitre 6 « Quelques composés
oxygénés » (1ereC, Chimie), scène 02.

§ Les trois classes d'alcools : primaire / secondaire / tertiaire, selon le
nombre de groupes alkyles portés par le carbone fonctionnel. Exemple
résolu 1 : déterminer la classe de trois alcools donnés.
Source : 1ereC/Chimie.pdf, chapitre 6, page 56.
"""

import textwrap

from manim import (
    DOWN,
    LEFT,
    RIGHT,
    UP,
    WHITE,
    YELLOW,
    GREEN,
    FadeIn,
    FadeOut,
    MathTex,
    Text,
    VGroup,
    Write,
    config,
)

from shapes.base_scene import NotionScene
from shapes.boxes import corrige_box, definition_box, exercise_box, scene_title


def _wrap(text: str, width: int = 56) -> str:
    return "\n".join(textwrap.fill(line, width=width) for line in text.split("\n"))


def _fit(mobject, top_y):
    bas_visible = -config.frame_height / 2 + 0.25
    hauteur_dispo = top_y - bas_visible
    if mobject.height > hauteur_dispo:
        mobject.scale(hauteur_dispo / mobject.height, about_point=mobject.get_top())
    return mobject


class ClassesDesAlcools(NotionScene):
    def construct(self):
        titre = scene_title("Les trois classes d'alcools")
        titre.scale(0.6)
        titre.to_edge(UP)

        # --- Énoncé : pourquoi classer les alcools -------------------------------
        intro = Text(
            _wrap(
                "Tous les alcools ne réagissent pas de la même façon : on "
                "les classe en trois catégories selon la structure de leur "
                "carbone fonctionnel.",
                width=54,
            ),
            font_size=24,
            color=WHITE,
        )
        intro.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Tous les alcools ne réagissent pas de la même façon, "
                "notamment lors de leur oxydation ménagée que nous verrons "
                "plus tard. On les classe donc en trois catégories, selon "
                "la structure du carbone fonctionnel, celui qui porte le "
                "groupe hydroxyle."
            )
        ) as tracker:
            self.play(Write(titre))
            self.play(FadeIn(intro))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(intro))

        # --- Raisonnement : définition des 3 classes -----------------------------
        definition = definition_box(
            Text(
                _wrap(
                    "La classe d'un alcool dépend du nombre de groupes "
                    "alkyles (R) directement fixés sur le carbone "
                    "fonctionnel : un alcool primaire en porte un (ou "
                    "zéro), un alcool secondaire en porte deux, un alcool "
                    "tertiaire en porte trois.",
                    width=48,
                ),
                font_size=23,
            ),
        )
        definition.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "La classe d'un alcool dépend du nombre de groupes alkyles, "
                "notés R, directement fixés sur le carbone fonctionnel. Un "
                "alcool primaire porte un seul groupe alkyle sur ce carbone "
                "— ou aucun, dans le cas particulier du méthanol. Un "
                "alcool secondaire en porte deux. Un alcool tertiaire en "
                "porte trois."
            )
        ) as tracker:
            self.play(FadeIn(definition))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(definition))

        # --- Schéma des 3 classes -------------------------------------------------
        schema_titre = Text("Les trois classes, carbone fonctionnel en évidence", font_size=21, color=YELLOW, weight="BOLD")
        schema_titre.next_to(titre, DOWN, buff=0.35)

        primaire = VGroup(
            MathTex(r"R-CH_2-OH", font_size=28, color=WHITE),
            Text("primaire", font_size=20, color=GREEN),
        ).arrange(DOWN, buff=0.25)

        secondaire = VGroup(
            MathTex(r"R_1-CH(OH)-R_2", font_size=28, color=WHITE),
            Text("secondaire", font_size=20, color=GREEN),
        ).arrange(DOWN, buff=0.25)

        tertiaire = VGroup(
            MathTex(r"R_1-C(OH)(R_2)-R_3", font_size=28, color=WHITE),
            Text("tertiaire", font_size=20, color=GREEN),
        ).arrange(DOWN, buff=0.25)

        trois_classes = VGroup(primaire, secondaire, tertiaire).arrange(DOWN, buff=0.45, aligned_edge=LEFT)
        trois_classes.next_to(schema_titre, DOWN, buff=0.45)
        groupe_schema = VGroup(schema_titre, trois_classes)
        _fit(groupe_schema, titre.get_bottom()[1] - 0.4)

        with self.voiceover(
            text=(
                "Voici les trois classes. Le carbone fonctionnel d'un "
                "alcool primaire, R-C-H-2-O-H, est relié à un seul autre "
                "carbone. Celui d'un alcool secondaire, R-1-C-H "
                "parenthèse O-H fermée parenthèse-R-2, est relié à deux "
                "autres carbones, R-1 et R-2. Celui d'un alcool tertiaire, "
                "R-1-C parenthèse O-H fermée parenthèse parenthèse R-2 "
                "fermée parenthèse-R-3, est relié à trois autres carbones : "
                "il ne porte alors plus aucun atome d'hydrogène."
            )
        ) as tracker:
            self.play(FadeIn(schema_titre))
            self.play(FadeIn(trois_classes))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(groupe_schema))

        # --- Exemple traité : déterminer la classe de 3 alcools -----------------
        enonce = exercise_box(
            VGroup(
                Text("Déterminer la classe de :", font_size=22, weight="BOLD"),
                MathTex(r"a)\; CH_3-CH_2-CH_2-OH", font_size=26),
                MathTex(r"b)\; CH_3-CH(OH)-CH_3", font_size=26),
                MathTex(r"c)\; CH_3-C(OH)(CH_3)-CH_3", font_size=26),
            ).arrange(DOWN, buff=0.3, aligned_edge=LEFT),
            box_width=10.5,
        )
        enonce.next_to(titre, DOWN, buff=0.4)
        _fit(enonce, titre.get_bottom()[1] - 0.4)

        with self.voiceover(
            text=(
                "Exemple résolu : déterminons la classe de trois alcools. "
                "a, C-H-3, C-H-2, C-H-2, O-H. b, C-H-3, C-H parenthèse O-H "
                "fermée parenthèse, C-H-3. c, C-H-3, C parenthèse O-H "
                "fermée parenthèse parenthèse C-H-3 fermée parenthèse, "
                "C-H-3."
            )
        ) as tracker:
            self.play(FadeIn(enonce))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(enonce))

        corrige = corrige_box(
            VGroup(
                Text(
                    "a) le carbone fonctionnel ne porte qu'1 carbone voisin → primaire (propan-1-ol).",
                    font_size=20,
                ),
                Text(
                    "b) le carbone fonctionnel porte 2 carbones voisins → secondaire (propan-2-ol).",
                    font_size=20,
                ),
                Text(
                    "c) le carbone fonctionnel porte 3 carbones voisins → tertiaire (2-méthylpropan-2-ol).",
                    font_size=20,
                ),
            ).arrange(DOWN, buff=0.3, aligned_edge=LEFT),
            box_width=11.5,
        )
        corrige.next_to(titre, DOWN, buff=0.4)
        _fit(corrige, titre.get_bottom()[1] - 0.4)

        with self.voiceover(
            text=(
                "Pour a, le carbone fonctionnel, celui qui porte O-H, "
                "n'est relié qu'à un seul autre carbone : c'est un alcool "
                "primaire, le propan-1-ol. Pour b, le carbone fonctionnel "
                "est relié à deux autres carbones : c'est un alcool "
                "secondaire, le propan-2-ol. Pour c, le carbone "
                "fonctionnel est relié à trois autres carbones : c'est un "
                "alcool tertiaire, le deux-méthylpropan-2-ol."
            )
        ) as tracker:
            self.play(FadeIn(corrige))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(corrige), FadeOut(titre))
