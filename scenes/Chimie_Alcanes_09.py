"""
scenes/Chimie_Alcanes_09.py — Chapitre 2 « Hydrocarbures saturés — les
alcanes » (1ereC, Chimie), scène 09.

§ 6.2 Propriétés physiques (2/2) : incolores, inodores pour les plus
légers, insolubles dans l'eau mais solubles dans les solvants organiques,
moins denses que l'eau (nappes d'hydrocarbures) mais alcanes gazeux plus
denses que l'air (risque d'explosion en cas de fuite).
Source : 1ereC/Chimie.pdf, page 21.
"""

import textwrap

from manim import (
    BLUE,
    DOWN,
    GRAY,
    LEFT,
    ORANGE,
    RIGHT,
    UP,
    WHITE,
    YELLOW,
    FadeIn,
    FadeOut,
    Rectangle,
    Text,
    VGroup,
    Write,
    config,
)

from shapes.base_scene import NotionScene
from shapes.boxes import property_box, scene_title, warning_box


def _wrap(text: str, width: int = 56) -> str:
    return "\n".join(textwrap.fill(line, width=width) for line in text.split("\n"))


def _bullets(items, font_size=23, color=WHITE, width=54):
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


class ProprietesPhysiques2(NotionScene):
    def construct(self):
        titre = scene_title("6. Propriétés physiques (2/2) : autres propriétés")
        titre.scale(0.5)
        titre.to_edge(UP)

        # --- Énoncé : incolores et inodores --------------------------------------
        intro = Text(
            _wrap(
                "Au-delà de l'état physique, les alcanes partagent "
                "d'autres propriétés physiques communes, importantes "
                "pour comprendre leur comportement dans la vie "
                "quotidienne.",
                width=54,
            ),
            font_size=24,
            color=WHITE,
        )
        intro.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Au-delà de l'état physique, les alcanes partagent "
                "d'autres propriétés physiques communes, importantes pour "
                "comprendre leur comportement dans la vie quotidienne."
            )
        ) as tracker:
            self.play(Write(titre))
            self.play(FadeIn(intro))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(intro))

        # --- Raisonnement : couleur, odeur, solubilité ---------------------------
        entete1 = Text("Couleur, odeur, solubilité", font_size=24, color=YELLOW, weight="BOLD")
        entete1.next_to(titre, DOWN, buff=0.4)

        proprietes1 = _bullets(
            [
                "Incolores ; les plus légers sont pratiquement inodores.",
                "Insolubles dans l'eau (molécules apolaires).",
                "Solubles dans les solvants organiques (essence, "
                "tétrachlorométhane…).",
            ],
            font_size=23,
            width=52,
        )
        proprietes1.next_to(entete1, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Les alcanes sont incolores ; les plus légers sont "
                "pratiquement inodores. Ils sont insolubles dans l'eau, "
                "car ce sont des molécules apolaires, mais solubles dans "
                "les solvants organiques, comme l'essence ou le "
                "tétrachlorométhane."
            )
        ) as tracker:
            self.play(FadeIn(entete1))
            self.play(FadeIn(proprietes1))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(entete1), FadeOut(proprietes1))

        # --- Exemple traité : densité par rapport à l'eau (nappes) --------------
        entete2 = Text("Moins denses que l'eau : les nappes d'hydrocarbures", font_size=20, color=YELLOW, weight="BOLD")
        entete2.next_to(titre, DOWN, buff=0.4)

        # schéma : bécher d'eau avec une couche d'hydrocarbure qui surnage
        beaker = Rectangle(width=3.0, height=2.2, color=WHITE, stroke_width=3)
        eau = Rectangle(width=2.9, height=1.5, fill_color=BLUE, fill_opacity=0.5, stroke_width=0)
        eau.align_to(beaker, DOWN).shift(UP * 0.05)
        hydrocarbure = Rectangle(width=2.9, height=0.55, fill_color=ORANGE, fill_opacity=0.6, stroke_width=0)
        hydrocarbure.next_to(eau, UP, buff=0)
        label_eau = Text("eau", font_size=16, color=WHITE).move_to(eau.get_center())
        label_hc = Text("alcane liquide", font_size=14, color=WHITE).move_to(hydrocarbure.get_center())

        schema_nappe = VGroup(beaker, eau, hydrocarbure, label_eau, label_hc)
        schema_nappe.next_to(entete2, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Les alcanes sont moins denses que l'eau : un alcane "
                "liquide surnage toujours à la surface. C'est ce "
                "phénomène qui explique les nappes d'hydrocarbures "
                "observées en cas de marée noire."
            )
        ) as tracker:
            self.play(FadeIn(entete2))
            self.play(FadeIn(beaker), FadeIn(eau), FadeIn(label_eau))
            self.play(FadeIn(hydrocarbure), FadeIn(label_hc))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(entete2), FadeOut(schema_nappe))

        # --- Exemple traité : gaz plus denses que l'air (risque explosion) ------
        entete3 = Text("Alcanes gazeux : plus denses que l'air", font_size=22, color=YELLOW, weight="BOLD")
        entete3.next_to(titre, DOWN, buff=0.4)

        # schéma : pièce avec fuite de gaz qui s'accumule au sol
        piece = Rectangle(width=3.4, height=2.4, color=WHITE, stroke_width=3)
        sol_gaz = Rectangle(width=3.3, height=0.6, fill_color=GRAY, fill_opacity=0.6, stroke_width=0)
        sol_gaz.align_to(piece, DOWN).shift(UP * 0.05)
        label_gaz = Text("gaz (butane, propane)\naccumulé au ras du sol", font_size=13, color=WHITE)
        label_gaz.move_to(sol_gaz.get_center())
        fuite = Text("fuite", font_size=14, color=YELLOW).next_to(piece, UP, buff=0.15)

        schema_gaz = VGroup(piece, sol_gaz, label_gaz, fuite)
        schema_gaz.next_to(entete3, DOWN, buff=0.4)
        _fit(schema_gaz, entete3.get_bottom()[1] - 0.4)

        with self.voiceover(
            text=(
                "À l'inverse, les alcanes gazeux, comme le butane et le "
                "propane, sont plus denses que l'air. En cas de fuite, "
                "ils s'accumulent au ras du sol plutôt que de se "
                "disperser vers le haut, d'où un risque d'explosion si "
                "une flamme ou une étincelle survient."
            )
        ) as tracker:
            self.play(FadeIn(entete3))
            self.play(FadeIn(piece), FadeIn(fuite))
            self.play(FadeIn(sol_gaz), FadeIn(label_gaz))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(entete3), FadeOut(schema_gaz))

        # --- À retenir : résumé des propriétés physiques -------------------------
        propriete = property_box(
            _bullets(
                [
                    "Incolores, inodores pour les plus légers.",
                    "Insolubles dans l'eau, solubles dans les solvants "
                    "organiques.",
                    "Liquides : moins denses que l'eau (surnagent).",
                    "Gazeux : plus denses que l'air (s'accumulent au sol).",
                ],
                font_size=20,
                width=48,
            ),
            box_width=11.0,
        )
        propriete.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Retenons l'essentiel : les alcanes sont incolores, "
                "inodores pour les plus légers, insolubles dans l'eau "
                "mais solubles dans les solvants organiques ; les alcanes "
                "liquides sont moins denses que l'eau et surnagent ; les "
                "alcanes gazeux sont plus denses que l'air et "
                "s'accumulent au ras du sol."
            )
        ) as tracker:
            self.play(FadeIn(propriete))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(propriete))

        # --- Piège à éviter : ne pas confondre les deux cas de densité ---------
        piege = warning_box(
            Text(
                _wrap(
                    "Ne confondez pas les deux cas : par rapport à l'EAU, "
                    "les alcanes liquides sont MOINS denses (ils "
                    "flottent). Par rapport à l'AIR, les alcanes gazeux "
                    "sont PLUS denses (ils s'accumulent au sol). Ce n'est "
                    "pas la même comparaison !",
                    width=48,
                ),
                font_size=22,
            ),
        )
        piege.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Attention à ne pas confondre les deux comparaisons : par "
                "rapport à l'eau, les alcanes liquides sont moins denses, "
                "ils flottent ; par rapport à l'air, les alcanes gazeux "
                "sont plus denses, ils s'accumulent au sol. Ce n'est pas "
                "du tout la même comparaison, et c'est une source "
                "fréquente d'erreur."
            )
        ) as tracker:
            self.play(FadeIn(piege))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(piege), FadeOut(titre))
