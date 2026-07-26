"""
scenes/SVT_EchangesCationiquesSol_10.py — Chapitre 9 (1ereC, SVT), scène 10.

Le lessivage : définition (entraînement en profondeur par les eaux de
pluie), mécanisme en 3 étapes, conséquences (appauvrissement, désaturation,
horizon lessivé, fatigue des sols), schéma du profil de sol, et méthode
point clé sur les anions non retenus (NO3-) et les engrais fractionnés.
Source : 1ereC/SVT.pdf, page 104.
"""

import textwrap

from manim import (
    BLUE,
    DOWN,
    LEFT,
    ORANGE,
    RIGHT,
    UP,
    WHITE,
    YELLOW,
    Arrow,
    Circle,
    Dot,
    FadeIn,
    FadeOut,
    Rectangle,
    Text,
    VGroup,
    Write,
)

from shapes.base_scene import NotionScene
from shapes.boxes import definition_box, method_box, scene_title


def _wrap(text: str, width: int = 56) -> str:
    return "\n".join(textwrap.fill(line, width=width) for line in text.split("\n"))


def _bullets(items, font_size=24, color=WHITE, width=54):
    lines = VGroup(
        *[Text(f"• {_wrap(it, width=width)}", font_size=font_size, color=color) for it in items]
    )
    lines.arrange(DOWN, aligned_edge=LEFT, buff=0.22)
    return lines


class Lessivage(NotionScene):
    def construct(self):
        titre = scene_title("9.9 — Le lessivage du sol")
        titre.scale(0.72)
        titre.to_edge(UP)

        # --- Énoncé : la pluie ne fait pas qu'apporter de l'eau -------------
        intro = Text(
            _wrap(
                "Sous les fortes pluies ivoiriennes, l'eau qui s'infiltre "
                "n'apporte pas que de l'humidité : elle peut aussi "
                "emporter, en profondeur, les éléments nutritifs du sol.",
                width=56,
            ),
            font_size=25,
            color=WHITE,
        )
        intro.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Sous les fortes pluies ivoiriennes, l'eau qui s'infiltre "
                "dans le sol n'apporte pas que de l'humidité : elle peut "
                "aussi emporter, en profondeur, les éléments nutritifs du "
                "sol. C'est le phénomène du lessivage."
            )
        ) as tracker:
            self.play(Write(titre))
            self.play(FadeIn(intro))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(intro))

        # --- Raisonnement : définition + mécanisme en 3 étapes --------------
        def_lessivage = definition_box(
            Text(
                _wrap(
                    "Le lessivage est l'entraînement en profondeur, par "
                    "les eaux de pluie qui s'infiltrent, des ions et des "
                    "particules fines du sol. Les éléments lessivés "
                    "descendent hors de portée des racines, et sont "
                    "définitivement perdus pour les cultures.",
                    width=54,
                ),
                font_size=21,
            ),
            box_width=11.8,
        )
        def_lessivage.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Le lessivage est l'entraînement en profondeur, par les "
                "eaux de pluie qui s'infiltrent, des ions et des "
                "particules fines du sol. Les éléments lessivés "
                "descendent vers les couches profondes, hors de portée "
                "des racines, et sont définitivement perdus pour les "
                "cultures."
            )
        ) as tracker:
            self.play(FadeIn(def_lessivage))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(def_lessivage))

        # Schéma : profil de sol avec pluie, CAH, et horizon lessivé
        zone_racinaire = Rectangle(width=4.0, height=1.6, color=ORANGE, fill_color=ORANGE, fill_opacity=0.15, stroke_width=2)
        label_racinaire = Text("Zone racinaire (CAH)", font_size=15, color=WHITE)
        cah_mini = Circle(radius=0.35, color=ORANGE, fill_color=ORANGE, fill_opacity=0.4, stroke_width=2)
        bloc_haut = VGroup(zone_racinaire, label_racinaire.next_to(zone_racinaire, UP, buff=0.1))
        cah_mini.move_to(zone_racinaire.get_center())

        horizon_lessive = Rectangle(width=4.0, height=1.2, color=WHITE, fill_color=WHITE, fill_opacity=0.08, stroke_width=2)
        label_lessive = Text("Horizon lessivé (profondeur)", font_size=15, color=WHITE)

        profil = VGroup(zone_racinaire, horizon_lessive).arrange(DOWN, buff=0.0)
        profil.next_to(titre, DOWN, buff=1.3)
        cah_mini.move_to(zone_racinaire.get_center())
        label_racinaire.next_to(zone_racinaire, LEFT, buff=0.15)
        label_lessive.next_to(horizon_lessive, LEFT, buff=0.15)

        pluie_fleches = VGroup(
            *[
                Arrow(
                    zone_racinaire.get_top() + LEFT * dx + UP * 0.8,
                    zone_racinaire.get_top() + LEFT * dx,
                    buff=0.02,
                    color=BLUE,
                    stroke_width=2.5,
                    max_tip_length_to_length_ratio=0.3,
                )
                for dx in [-1.3, -0.4, 0.5, 1.3]
            ]
        )
        pluie_label = Text("Pluies", font_size=16, color=BLUE).next_to(pluie_fleches, UP, buff=0.1)

        dots_hauts = VGroup(
            *[Dot(zone_racinaire.get_center() + LEFT * dx + UP * 0.3, color=YELLOW, radius=0.08) for dx in [-1.0, 0.0, 1.0]]
        )

        fleche_descente = Arrow(
            zone_racinaire.get_bottom(), horizon_lessive.get_center(), buff=0.05, color=YELLOW, stroke_width=3
        )
        dots_bas = VGroup(
            *[Dot(horizon_lessive.get_center() + LEFT * dx, color=YELLOW, radius=0.08) for dx in [-1.0, 0.0, 1.0]]
        )

        schema = VGroup(
            profil, cah_mini, label_racinaire, label_lessive, pluie_fleches, pluie_label, dots_hauts,
            fleche_descente, dots_bas,
        )
        schema.scale(0.9)
        schema.move_to([0, 0, 0]).next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Voici le mécanisme en trois étapes. Un : les pluies, "
                "surtout abondantes sous climat équatorial, chargent la "
                "solution du sol en ions H+. Deux : ces ions H+ se "
                "fixent sur le complexe et chassent les bases, calcium, "
                "magnésium, potassium, sodium, dans la solution, c'est "
                "la désorption. Trois : ces bases désorbées, ainsi que "
                "les anions non retenus par le complexe, sont entraînées "
                "vers le bas par l'eau qui percole, jusqu'à un horizon "
                "profond hors de portée des racines."
            )
        ) as tracker:
            self.play(FadeIn(profil), FadeIn(cah_mini), FadeIn(label_racinaire), FadeIn(label_lessive))
            self.play(FadeIn(pluie_fleches), FadeIn(pluie_label))
            self.play(FadeIn(dots_hauts))
            self.play(FadeIn(fleche_descente), FadeIn(dots_bas))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(schema))

        # --- Conséquences du lessivage -----------------------------------------
        consequences_titre = Text("Conséquences du lessivage", font_size=25, color=YELLOW, weight="BOLD")
        consequences_titre.next_to(titre, DOWN, buff=0.5)

        consequences = _bullets(
            [
                "Appauvrissement du sol en éléments fertilisants (bases "
                "nutritives, nitrates)",
                "Désaturation du complexe argilo-humique et "
                "acidification du sol",
                "Déplacement de l'argile vers les horizons profonds "
                "(horizon lessivé pâle en surface)",
                "À terme : fatigue des sols et baisse des rendements "
                "agricoles",
            ],
            font_size=20,
            width=54,
        )
        consequences.next_to(consequences_titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Les conséquences du lessivage sont lourdes. "
                "Appauvrissement du sol en éléments fertilisants, bases "
                "nutritives et nitrates. Désaturation du complexe "
                "argilo-humique et acidification du sol. Déplacement de "
                "l'argile elle-même vers les horizons profonds, laissant "
                "un horizon lessivé, pâle, en surface. Et à terme, la "
                "fatigue des sols et la baisse des rendements agricoles."
            )
        ) as tracker:
            self.play(FadeIn(consequences_titre))
            self.play(FadeIn(consequences))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(consequences_titre), FadeOut(consequences))

        # --- À retenir : point clé sur les anions ------------------------------
        methode = method_box(
            Text(
                _wrap(
                    "Point clé : les anions (NO3- notamment) ne sont pas "
                    "retenus par le complexe chargé négativement : ils "
                    "sont donc les premiers perdus par lessivage. C'est "
                    "pourquoi les engrais azotés doivent être apportés "
                    "fractionnés, au moment des besoins des cultures.",
                    width=54,
                ),
                font_size=21,
            ),
            box_width=11.8,
        )
        methode.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Retenez ce point clé. Les anions, en particulier le "
                "nitrate NO3-, ne sont pas retenus par le complexe "
                "chargé négativement, puisque deux charges négatives se "
                "repoussent : ils sont donc les premiers perdus par "
                "lessivage. C'est pourquoi les engrais azotés doivent "
                "être apportés fractionnés, en plusieurs fois, au moment "
                "précis des besoins des cultures, plutôt qu'en une seule "
                "grosse dose."
            )
        ) as tracker:
            self.play(FadeIn(methode))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(titre), FadeOut(methode))
