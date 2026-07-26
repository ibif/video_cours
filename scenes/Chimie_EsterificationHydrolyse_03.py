"""
scenes/Chimie_EsterificationHydrolyse_03.py — Chapitre 8 « Estérification et
hydrolyse d'un ester » (1ereC, Chimie), scène 03.

§ Caractéristiques de l'estérification (1/2) : réaction lente à
température ambiante (années), accélérée par chauffage à reflux (heures).
theorem_box réaction athermique → température = facteur cinétique, pas
facteur d'équilibre (même limite à 20°C ou 100°C).
Source : 1ereC/Chimie.pdf, chapitre 8, page 77.
"""

import textwrap

from manim import (
    DOWN,
    LEFT,
    RIGHT,
    UP,
    WHITE,
    YELLOW,
    BLUE,
    Arrow,
    Dot,
    FadeIn,
    FadeOut,
    MathTex,
    Text,
    VGroup,
    Write,
    config,
)

from shapes.base_scene import NotionScene
from shapes.boxes import scene_title, theorem_box


def _wrap(text: str, width: int = 56) -> str:
    return "\n".join(textwrap.fill(line, width=width) for line in text.split("\n"))


def _fit(mobject, top_y):
    bas_visible = -config.frame_height / 2 + 0.25
    hauteur_dispo = top_y - bas_visible
    if mobject.height > hauteur_dispo:
        mobject.scale(hauteur_dispo / mobject.height, about_point=mobject.get_top())
    return mobject


class CaracteristiquesLenteAthermique(NotionScene):
    def construct(self):
        titre = scene_title("3. Caractéristiques (1/2) : lente et athermique")
        titre.scale(0.5)
        titre.to_edge(UP)

        # --- Énoncé -----------------------------------------------------------
        enonce = Text(
            _wrap(
                "L'estérification possède trois caractéristiques "
                "importantes à connaître. Intéressons-nous d'abord à sa "
                "vitesse et à son aspect thermique.",
                width=54,
            ),
            font_size=25,
            color=WHITE,
        )
        enonce.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "L'estérification possède trois caractéristiques "
                "essentielles à connaître. Intéressons-nous d'abord à sa "
                "vitesse, et à son aspect thermique."
            )
        ) as tracker:
            self.play(Write(titre))
            self.play(FadeIn(enonce))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(enonce))

        # --- Raisonnement : une réaction lente ----------------------------------
        entete = Text("Une réaction LENTE", font_size=26, color=YELLOW, weight="BOLD")
        entete.next_to(titre, DOWN, buff=0.4)

        comparaison = VGroup(
            Text("À température ambiante (≈20°C) :", font_size=22, color=WHITE),
            Text("il faut plusieurs mois, voire des ANNÉES,", font_size=22, color=WHITE),
            Text("pour approcher l'état final.", font_size=22, color=WHITE),
        ).arrange(DOWN, buff=0.15)

        comparaison2 = VGroup(
            Text("Par chauffage à reflux :", font_size=22, color=BLUE),
            Text("l'état final est atteint en quelques HEURES.", font_size=22, color=BLUE),
        ).arrange(DOWN, buff=0.15)

        bloc = VGroup(comparaison, comparaison2).arrange(DOWN, buff=0.5)
        bloc.next_to(entete, DOWN, buff=0.4)
        groupe = VGroup(entete, bloc)
        _fit(groupe, titre.get_bottom()[1] - 0.4)

        with self.voiceover(
            text=(
                "Première caractéristique : l'estérification est une "
                "réaction lente. À température ambiante, environ vingt "
                "degrés, il faut plusieurs mois, voire des années, pour "
                "que le système approche son état final. Par chauffage à "
                "reflux, en revanche, cet état final est atteint en "
                "seulement quelques heures : le chauffage accélère "
                "considérablement la réaction, sans en changer la nature."
            )
        ) as tracker:
            self.play(FadeIn(entete))
            self.play(FadeIn(comparaison))
            self.play(FadeIn(comparaison2))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(groupe))

        # --- Exemple traité : diagramme énergétique athermique ---------------------
        entete2 = Text("Une réaction ATHERMIQUE", font_size=26, color=YELLOW, weight="BOLD")
        entete2.next_to(titre, DOWN, buff=0.4)

        niveau_reactifs = Dot(point=[-3, 0.6, 0], color=WHITE)
        niveau_produits = Dot(point=[3, 0.6, 0], color=WHITE)
        ligne_reactifs = Text("acide + alcool", font_size=20, color=WHITE).next_to(niveau_reactifs, LEFT, buff=0.15)
        ligne_produits = Text("ester + eau", font_size=20, color=WHITE).next_to(niveau_produits, RIGHT, buff=0.15)
        fleche = Arrow(start=[-2.3, 0.6, 0], end=[2.3, 0.6, 0], color=BLUE, buff=0)
        deltaH = MathTex(r"\Delta H \approx 0", font_size=32, color=YELLOW)
        deltaH.next_to(fleche, DOWN, buff=0.3)

        diagramme = VGroup(niveau_reactifs, niveau_produits, ligne_reactifs, ligne_produits, fleche, deltaH)
        diagramme.next_to(entete2, DOWN, buff=0.6)

        groupe2 = VGroup(entete2, diagramme)

        with self.voiceover(
            text=(
                "Seconde caractéristique : l'estérification est une "
                "réaction athermique, c'est-à-dire qu'elle se déroule "
                "quasiment sans échange de chaleur avec le milieu "
                "extérieur. L'énergie des produits, ester et eau, est "
                "quasiment la même que celle des réactifs, acide et "
                "alcool : la variation d'enthalpie delta H est quasiment "
                "nulle."
            )
        ) as tracker:
            self.play(FadeIn(entete2))
            self.play(FadeIn(niveau_reactifs), FadeIn(ligne_reactifs), FadeIn(niveau_produits), FadeIn(ligne_produits))
            self.play(Write(fleche), FadeIn(deltaH))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(groupe2))

        # --- À retenir : theorem_box température = facteur cinétique --------------
        theoreme = theorem_box(
            VGroup(
                Text(
                    _wrap(
                        "Étant athermique, l'estérification a la même "
                        "composition finale à l'équilibre, que l'on "
                        "travaille à 20°C ou à 100°C.",
                        width=46,
                    ),
                    font_size=22,
                ),
                Text(
                    "La température est un facteur CINÉTIQUE",
                    font_size=22,
                    weight="BOLD",
                ),
                Text(
                    "(elle accélère), PAS un facteur d'ÉQUILIBRE",
                    font_size=22,
                    weight="BOLD",
                ),
                Text(
                    "(elle ne change pas l'état final).",
                    font_size=22,
                    weight="BOLD",
                ),
            ).arrange(DOWN, buff=0.25),
        )
        theoreme.next_to(titre, DOWN, buff=0.4)
        _fit(theoreme, titre.get_bottom()[1] - 0.4)

        with self.voiceover(
            text=(
                "Retenons ce théorème essentiel : étant athermique, "
                "l'estérification a la même composition finale à "
                "l'équilibre, que l'on travaille à vingt degrés ou à cent "
                "degrés. La température est donc un facteur cinétique, "
                "elle accélère la réaction, mais ce n'est pas un facteur "
                "d'équilibre : elle ne change en rien l'état final "
                "atteint. Chauffer permet seulement d'atteindre plus vite "
                "ce même état final."
            )
        ) as tracker:
            self.play(FadeIn(theoreme))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(theoreme), FadeOut(titre))
