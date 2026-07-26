"""
scenes/Chimie_ComposesOxygenes_09.py — Chapitre 6 « Quelques composés
oxygénés » (1ereC, Chimie), scène 09.

§ Exemple résolu : l'expérience de « la lampe sans flamme » (fil de cuivre
incandescent + vapeurs d'éthanol) — protocole, observations, équations en
2 étapes (éthanol → éthanal → acide éthanoïque), application sociale
(anciens alcootests au dichromate).
Source : 1ereC/Chimie.pdf, chapitre 6, page 63.
"""

import textwrap

from manim import (
    DOWN,
    LEFT,
    RIGHT,
    UP,
    WHITE,
    YELLOW,
    ORANGE,
    FadeIn,
    FadeOut,
    MathTex,
    Text,
    VGroup,
    Write,
    config,
)

from shapes.base_scene import NotionScene
from shapes.boxes import corrige_box, exercise_box, property_box, scene_title


def _wrap(text: str, width: int = 56) -> str:
    return "\n".join(textwrap.fill(line, width=width) for line in text.split("\n"))


def _bullets(items, font_size=22, color=WHITE, width=52):
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


class ExperienceLaLampeSansFlamme(NotionScene):
    def construct(self):
        titre = scene_title("Exemple résolu : la lampe sans flamme")
        titre.scale(0.6)
        titre.to_edge(UP)

        # --- Énoncé : le protocole expérimental --------------------------------------
        protocole = exercise_box(
            Text(
                _wrap(
                    "On chauffe une spirale de fil de cuivre jusqu'à "
                    "incandescence (rouge), puis on la plonge, encore "
                    "chaude, dans un tube contenant de l'éthanol légèrement "
                    "réchauffé, sans la mettre en contact direct avec le "
                    "liquide (elle reste dans les vapeurs).",
                    width=48,
                ),
                font_size=22,
                color="#1A1A1A",
            ),
            box_width=11.5,
        )
        protocole.next_to(titre, DOWN, buff=0.4)
        _fit(protocole, titre.get_bottom()[1] - 0.4)

        with self.voiceover(
            text=(
                "Étudions une expérience classique, appelée « la lampe "
                "sans flamme ». Le protocole : on chauffe une spirale de "
                "fil de cuivre jusqu'à ce qu'elle devienne incandescente, "
                "rouge, puis on la plonge, encore chaude, dans un tube à "
                "essai contenant de l'éthanol légèrement réchauffé — sans "
                "toucher le liquide, la spirale reste dans les vapeurs "
                "d'éthanol qui s'en dégagent."
            )
        ) as tracker:
            self.play(Write(titre))
            self.play(FadeIn(protocole))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(protocole))

        # --- Raisonnement : les observations ------------------------------------------
        obs_titre = Text("Observations", font_size=24, color=YELLOW, weight="BOLD")
        obs_titre.next_to(titre, DOWN, buff=0.35)

        observations = _bullets(
            [
                "le fil de cuivre reste incandescent SANS flamme, "
                "de façon entretenue, tant qu'il baigne dans les vapeurs ;",
                "quelques gouttes de réactif de Schiff, ajoutées au "
                "liquide recueilli, ROSISSENT : signe d'un aldéhyde ;",
                "après un contact prolongé, le papier pH plongé dans le "
                "liquide ROUGIT : signe de l'apparition d'un acide.",
            ],
            width=48,
        )
        observations.next_to(obs_titre, DOWN, buff=0.4)

        groupe_obs = VGroup(obs_titre, observations)
        _fit(groupe_obs, titre.get_bottom()[1] - 0.4)

        with self.voiceover(
            text=(
                "Voici les observations. Le fil de cuivre reste "
                "incandescent, sans flamme visible, de façon entretenue, "
                "tant qu'il baigne dans les vapeurs d'éthanol — d'où le nom "
                "de l'expérience. En ajoutant quelques gouttes de réactif "
                "de Schiff au liquide recueilli, celui-ci rosit : c'est le "
                "signe de la présence d'un aldéhyde. Après un contact plus "
                "prolongé, le papier pH plongé dans ce même liquide "
                "rougit : c'est le signe de l'apparition d'un acide."
            )
        ) as tracker:
            self.play(FadeIn(obs_titre))
            self.play(FadeIn(observations))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(groupe_obs))

        # --- Exemple traité : équations-bilans en 2 étapes ----------------------------
        etape1_titre = Text("Étape 1 — éthanol → éthanal", font_size=23, color=YELLOW, weight="BOLD")
        etape1_titre.next_to(titre, DOWN, buff=0.35)

        eq1 = MathTex(
            r"CH_3-CH_2-OH \xrightarrow{Cu,\;\Delta} CH_3-CHO + H_2",
            font_size=27,
            color=WHITE,
        )
        eq1.next_to(etape1_titre, DOWN, buff=0.45)

        groupe1 = VGroup(etape1_titre, eq1)

        with self.voiceover(
            text=(
                "Interprétons chimiquement ces observations, en deux "
                "étapes. Étape un : le cuivre chaud catalyse la "
                "déshydrogénation de l'éthanol, un alcool primaire, qui "
                "s'oxyde en éthanal, un aldéhyde, avec dégagement "
                "d'hydrogène. C'est ce dihydrogène qui, en brûlant "
                "silencieusement au contact de l'air, entretient "
                "l'incandescence du fil sans flamme visible — d'où le "
                "rosissement au réactif de Schiff, révélateur de "
                "l'aldéhyde formé."
            )
        ) as tracker:
            self.play(FadeIn(etape1_titre))
            self.play(Write(eq1))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(groupe1))

        etape2_titre = Text("Étape 2 — éthanal → acide éthanoïque", font_size=23, color=YELLOW, weight="BOLD")
        etape2_titre.next_to(titre, DOWN, buff=0.35)

        eq2 = MathTex(
            r"CH_3-CHO + \tfrac{1}{2}O_2 \xrightarrow{Cu} CH_3-COOH",
            font_size=27,
            color=WHITE,
        )
        eq2.next_to(etape2_titre, DOWN, buff=0.45)

        groupe2 = VGroup(etape2_titre, eq2)

        with self.voiceover(
            text=(
                "Étape deux : si le contact se prolonge, l'éthanal formé "
                "s'oxyde à son tour, cette fois par le dioxygène de l'air "
                "toujours catalysé par le cuivre, en acide éthanoïque. "
                "C'est cet acide qui fait rougir le papier pH."
            )
        ) as tracker:
            self.play(FadeIn(etape2_titre))
            self.play(Write(eq2))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(groupe2))

        # --- À retenir : application sociale ------------------------------------------
        application = property_box(
            Text(
                _wrap(
                    "Application sociale : les anciens alcootests reposaient "
                    "sur ce même principe d'oxydation ménagée, avec le "
                    "dichromate de potassium K₂Cr₂O₇ (orange), réduit en "
                    "ions Cr³⁺ (vert) au contact de l'éthanol expiré — un "
                    "changement de couleur qui trahissait l'alcoolémie.",
                    width=48,
                ),
                font_size=21,
            ),
            box_width=12.0,
        )
        application.next_to(titre, DOWN, buff=0.4)
        _fit(application, titre.get_bottom()[1] - 0.4)

        with self.voiceover(
            text=(
                "Cette réaction a une application sociale importante : les "
                "anciens alcootests reposaient sur ce même principe "
                "d'oxydation ménagée. Ils contenaient des cristaux de "
                "dichromate de potassium, de couleur orange, qui se "
                "réduisaient en ions chrome trois plus, de couleur verte, "
                "au contact de l'éthanol contenu dans l'air expiré. Ce "
                "changement de couleur trahissait la présence, et le taux, "
                "d'alcool dans le sang du conducteur."
            )
        ) as tracker:
            self.play(FadeIn(application))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(application), FadeOut(titre))
