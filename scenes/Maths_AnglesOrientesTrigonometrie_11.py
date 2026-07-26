"""
scenes/Maths_AnglesOrientesTrigonometrie_11.py — Chapitre « Angles orientés
et trigonométrie » (1ereC, Maths), scène 11.

§ Expression de cos a, sin a, tan a en fonction de t = tan(a/2) :
présentée comme un outil pour la résolution d'équations trigonométriques
(sans démonstration complète, mention explicite de son usage).
Source : 1ereC/Maths.pdf, chapitre 2, pages 14-27.
"""

import textwrap

from manim import DOWN, UP, WHITE, FadeIn, FadeOut, MathTex, Text, VGroup, Write

from shapes.base_scene import NotionScene
from shapes.boxes import property_box, scene_title, warning_box


def _wrap(text: str, width: int = 56) -> str:
    return "\n".join(textwrap.fill(line, width=width) for line in text.split("\n"))


class ExpressionEnFonctionDeT(NotionScene):
    def construct(self):
        titre = scene_title("Expression en fonction de t = tan(a/2)")
        titre.scale(0.55)
        titre.to_edge(UP)

        # --- Énoncé : présentation de l'outil ------------------------------
        intro = Text(
            _wrap(
                "Certaines équations trigonométriques compliquées se "
                "résolvent plus facilement en ramenant cosinus, sinus et "
                "tangente à une seule fonction rationnelle de "
                "t = tan(a/2). C'est un outil de calcul, pas une nouvelle "
                "notion de cours à démontrer en détail ici.",
                width=54,
            ),
            font_size=23,
            color=WHITE,
        )
        intro.next_to(titre, DOWN, buff=0.55)

        with self.voiceover(
            text=(
                "Pour terminer la partie « formules » de ce chapitre, "
                "voici un outil de calcul supplémentaire, très utile face "
                "à certaines équations trigonométriques compliquées : "
                "l'expression du cosinus, du sinus et de la tangente d'un "
                "réel a, en fonction du seul nombre t égale tangente de a "
                "sur deux. Ce n'est pas une nouvelle notion à démontrer "
                "en détail : c'est avant tout un outil pratique à "
                "connaître."
            )
        ) as tracker:
            self.play(Write(titre))
            self.play(FadeIn(intro))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(intro))

        # --- Raisonnement : la propriété ---------------------------------------
        propriete = property_box(
            VGroup(
                Text("En posant t = tan(a/2), pour a ≠ π + k2π :", font_size=22, weight="BOLD"),
                MathTex(r"\cos a = \dfrac{1 - t^2}{1 + t^2}", font_size=28),
                MathTex(r"\sin a = \dfrac{2t}{1 + t^2}", font_size=28),
                MathTex(r"\tan a = \dfrac{2t}{1 - t^2} \quad (a \neq \tfrac{\pi}{2} + k\pi)", font_size=25),
            ).arrange(DOWN, buff=0.3),
            box_width=8.6,
        )
        propriete.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "En posant t égale tangente de a sur deux, pour a "
                "différent de pi plus k deux pi, on obtient les trois "
                "formules suivantes. Cosinus a égale un moins t carré, sur "
                "un plus t carré. Sinus a égale deux t, sur un plus t "
                "carré. Et tangente a égale deux t, sur un moins t carré, "
                "sous réserve que a soit différent de pi sur deux plus k "
                "pi."
            )
        ) as tracker:
            self.play(FadeIn(propriete))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(propriete))

        # --- À retenir : utilité ------------------------------------------------
        utilite = property_box(
            Text(
                _wrap(
                    "Intérêt de ce changement de variable : cos a, sin a "
                    "et tan a deviennent des fractions rationnelles en t, "
                    "ce qui permet de transformer une équation "
                    "trigonométrique en équation algébrique (souvent du "
                    "second degré en t), résolue par les méthodes "
                    "usuelles.",
                    width=52,
                ),
                font_size=21,
            ),
            box_width=9.5,
        )
        utilite.next_to(titre, DOWN, buff=0.55)

        with self.voiceover(
            text=(
                "L'intérêt de ce changement de variable est le suivant : "
                "cosinus a, sinus a et tangente a deviennent des "
                "fractions rationnelles en t, c'est-à-dire des quotients "
                "de polynômes en t. Une équation trigonométrique se "
                "transforme alors en équation algébrique, souvent du "
                "second degré en t, que l'on sait résoudre par les "
                "méthodes usuelles vues en algèbre."
            )
        ) as tracker:
            self.play(FadeIn(utilite))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(utilite))

        # --- Piège à éviter -------------------------------------------------------
        piege = warning_box(
            Text(
                _wrap(
                    "Ce changement de variable n'est utile que pour des "
                    "équations qui ne se ramènent pas directement aux "
                    "équations de base cos x=a, sin x=a, tan x=a (scène "
                    "suivante) : ne pas l'utiliser systématiquement, il "
                    "alourdit inutilement un calcul déjà simple.",
                    width=52,
                ),
                font_size=21,
            ),
            box_width=9.5,
        )
        piege.next_to(titre, DOWN, buff=0.55)

        with self.voiceover(
            text=(
                "Attention cependant à ne pas en abuser : ce changement de "
                "variable n'est utile que pour des équations qui ne se "
                "ramènent pas directement aux équations de base, cosinus x "
                "égale a, sinus x égale a, ou tangente x égale a, que nous "
                "allons étudier dans la scène suivante. Utilisé "
                "systématiquement, il alourdit inutilement un calcul qui "
                "était déjà simple."
            )
        ) as tracker:
            self.play(FadeIn(piege))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(piege), FadeOut(titre))
