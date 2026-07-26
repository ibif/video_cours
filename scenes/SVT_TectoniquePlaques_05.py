"""
scenes/SVT_TectoniquePlaques_05.py — Chapitre 8 (1ereC, SVT), scène 05.

III.B.3 Les anomalies magnétiques du plancher océanique (Vine et Matthews,
1963) : bandes parallèles, symétriques, d'autant plus anciennes qu'on
s'éloigne de l'axe, schéma + interprétation (enregistreur magnétique) ;
Exemple résolu 1 : calcul complet d'une vitesse d'expansion (anomalie à
150 km datée de 10 Ma). Source : 1ereC/SVT.pdf, page 88.
"""

import textwrap

from manim import (
    BLUE_D,
    DOWN,
    LEFT,
    RED,
    RIGHT,
    UP,
    WHITE,
    YELLOW,
    FadeIn,
    FadeOut,
    MathTex,
    Rectangle,
    Text,
    VGroup,
    Write,
)

from shapes.base_scene import NotionScene
from shapes.boxes import example_box, scene_title


def _wrap(text: str, width: int = 56) -> str:
    return "\n".join(textwrap.fill(line, width=width) for line in text.split("\n"))


def _bullets(items, font_size=24, color=WHITE, width=54):
    lines = VGroup(
        *[Text(f"• {_wrap(it, width=width)}", font_size=font_size, color=color) for it in items]
    )
    lines.arrange(DOWN, aligned_edge=LEFT, buff=0.22)
    return lines


def _bande_magnetique(largeur, polarite):
    couleur = BLUE_D if polarite == "N" else RED
    rect = Rectangle(width=largeur, height=1.1, fill_color=couleur, fill_opacity=0.85, stroke_color=WHITE, stroke_width=0.5)
    label = Text(polarite, font_size=16, color=WHITE, weight="BOLD")
    label.move_to(rect.get_center())
    return VGroup(rect, label)


class AnomaliesMagnetiquesEtVitesse(NotionScene):
    def construct(self):
        titre = scene_title("III. Les anomalies magnétiques (Vine, Matthews)")
        titre.scale(0.58)
        titre.to_edge(UP)
        self.play(Write(titre))

        # --- Énoncé : la découverte de 1963 ----------------------------------
        intro = Text(
            _wrap(
                "En 1963, Vine et Matthews mesurent le champ magnétique "
                "au-dessus des océans et découvrent des bandes alternées, "
                "positives et négatives, disposées symétriquement de part "
                "et d'autre de l'axe d'une dorsale.",
                width=56,
            ),
            font_size=24,
            color=WHITE,
        )
        intro.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "En dix-neuf cent soixante-trois, les géophysiciens Vine et "
                "Matthews mesurent le champ magnétique au-dessus des "
                "océans, et découvrent des bandes alternées, positives et "
                "négatives, disposées symétriquement de part et d'autre de "
                "l'axe d'une dorsale."
            )
        ) as tracker:
            self.play(FadeIn(intro))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(intro))

        # --- Animation du raisonnement : schéma des bandes symétriques ------
        ages = [30, 20, 10]
        polarites = ["I", "N", "I"]
        largeurs = [1.4, 1.0, 0.7]

        gauche_bandes = VGroup()
        for age, pol, larg in zip(ages, polarites, largeurs):
            gauche_bandes.add(_bande_magnetique(larg, pol))
        gauche_bandes.arrange(RIGHT, buff=0)

        droite_bandes = VGroup()
        for age, pol, larg in zip(reversed(ages), reversed(polarites), reversed(largeurs)):
            droite_bandes.add(_bande_magnetique(larg, pol))
        droite_bandes.arrange(RIGHT, buff=0)

        axe = Rectangle(width=0.08, height=1.1, fill_color=YELLOW, fill_opacity=1, stroke_width=0)

        toutes_bandes = VGroup(gauche_bandes, axe, droite_bandes).arrange(RIGHT, buff=0)
        toutes_bandes.next_to(titre, DOWN, buff=0.7)

        etiquettes = VGroup(
            Text("30 Ma", font_size=14, color=WHITE).next_to(toutes_bandes[0][0], UP, buff=0.1),
            Text("20 Ma", font_size=14, color=WHITE).next_to(toutes_bandes[0][1], UP, buff=0.1),
            Text("10 Ma", font_size=14, color=WHITE).next_to(toutes_bandes[0][2], UP, buff=0.1),
            Text("Axe", font_size=14, color=YELLOW).next_to(axe, UP, buff=0.1),
            Text("10 Ma", font_size=14, color=WHITE).next_to(toutes_bandes[2][0], UP, buff=0.1),
            Text("20 Ma", font_size=14, color=WHITE).next_to(toutes_bandes[2][1], UP, buff=0.1),
            Text("30 Ma", font_size=14, color=WHITE).next_to(toutes_bandes[2][2], UP, buff=0.1),
        )

        legende_n = VGroup(
            Rectangle(width=0.3, height=0.2, fill_color=BLUE_D, fill_opacity=0.85, stroke_width=0),
            Text("N = polarité normale", font_size=16, color=WHITE),
        ).arrange(RIGHT, buff=0.15)
        legende_i = VGroup(
            Rectangle(width=0.3, height=0.2, fill_color=RED, fill_opacity=0.85, stroke_width=0),
            Text("I = polarité inversée", font_size=16, color=WHITE),
        ).arrange(RIGHT, buff=0.15)
        legende = VGroup(legende_n, legende_i).arrange(DOWN, aligned_edge=LEFT, buff=0.15)
        legende.next_to(toutes_bandes, DOWN, buff=0.5)

        schema = VGroup(toutes_bandes, etiquettes, legende)

        with self.voiceover(
            text=(
                "Ces bandes ont trois propriétés remarquables : elles sont "
                "parallèles à l'axe de la dorsale ; elles sont symétriques "
                "par rapport à cet axe, la même bande se retrouvant à la "
                "même distance de chaque côté ; et elles sont d'autant plus "
                "anciennes que l'on s'éloigne de l'axe."
            )
        ) as tracker:
            self.play(FadeIn(toutes_bandes))
            self.play(FadeIn(etiquettes), FadeIn(legende))
            self.wait(tracker.get_remaining_duration())

        with self.voiceover(
            text=(
                "Interprétation : la croûte se forme à l'axe de la dorsale, "
                "s'y aimante selon le champ magnétique du moment, puis est "
                "poussée de part et d'autre à mesure que de la nouvelle "
                "croûte se forme derrière elle. Le plancher océanique "
                "fonctionne ainsi comme un véritable enregistreur "
                "magnétique : les anomalies magnétiques sont une preuve "
                "directe et mesurable de l'expansion océanique."
            )
        ) as tracker:
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(schema))

        # --- Exemple traité : calcul de la vitesse d'expansion --------------
        enonce_ex = Text(
            _wrap(
                "Exemple résolu : une anomalie magnétique datée de 10 Ma se "
                "situe à 150 km de l'axe de la dorsale médio-atlantique. "
                "Calculer la vitesse d'écartement (demi-vitesse), puis la "
                "vitesse d'expansion totale.",
                width=54,
            ),
            font_size=22,
            color=WHITE,
        )
        enonce_ex.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Mettons cela en pratique. Énoncé : une anomalie magnétique "
                "datée de dix millions d'années se situe à cent cinquante "
                "kilomètres de l'axe de la dorsale médio-atlantique. "
                "Calculons la vitesse d'écartement de la croûte, c'est-à-dire "
                "la demi-vitesse d'expansion, puis la vitesse d'expansion "
                "totale de l'océan."
            )
        ) as tracker:
            self.play(FadeIn(enonce_ex))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(enonce_ex))

        etape1 = MathTex(r"v = \dfrac{d}{t} = \dfrac{150\ \text{km}}{10\ \text{Ma}} = 15\ \text{km/Ma}", font_size=32, color=WHITE)
        etape2 = MathTex(r"1\ \text{km/Ma} = \dfrac{10^{5}\ \text{cm}}{10^{6}\ \text{ans}} = 0{,}1\ \text{cm/an}", font_size=30, color=WHITE)
        etape3 = MathTex(r"v = 15 \times 0{,}1 = 1{,}5\ \text{cm/an}\ \text{(demi-vitesse)}", font_size=32, color=WHITE)
        etape4 = MathTex(r"v_{\text{totale}} = 2 \times 1{,}5 = 3\ \text{cm/an}", font_size=34, color=YELLOW)

        etapes = VGroup(etape1, etape2, etape3, etape4).arrange(DOWN, aligned_edge=LEFT, buff=0.35)
        etapes.next_to(titre, DOWN, buff=0.6)

        with self.voiceover(
            text=(
                "Première étape : la croûte de cette anomalie s'est formée "
                "à l'axe il y a dix millions d'années, et a parcouru cent "
                "cinquante kilomètres depuis. Sa vitesse d'écartement vaut "
                "donc v égale d sur t, soit cent cinquante kilomètres "
                "divisé par dix mégaannées, c'est-à-dire quinze kilomètres "
                "par mégaannée."
            )
        ) as tracker:
            self.play(Write(etape1))
            self.wait(tracker.get_remaining_duration())

        with self.voiceover(
            text=(
                "Deuxième étape : convertissons cette unité. Un kilomètre "
                "par mégaannée équivaut à dix puissance cinq centimètres "
                "divisé par dix puissance six ans, soit zéro virgule un "
                "centimètre par an, c'est-à-dire un millimètre par an."
            )
        ) as tracker:
            self.play(Write(etape2))
            self.wait(tracker.get_remaining_duration())

        with self.voiceover(
            text=(
                "Troisième étape : quinze kilomètres par mégaannée "
                "correspondent donc à quinze fois zéro virgule un, soit un "
                "virgule cinq centimètre par an. C'est la demi-vitesse, "
                "celle d'un seul flanc de la dorsale."
            )
        ) as tracker:
            self.play(Write(etape3))
            self.wait(tracker.get_remaining_duration())

        with self.voiceover(
            text=(
                "Quatrième étape : la croûte s'écarte symétriquement des "
                "deux côtés de la dorsale. La vitesse d'expansion totale "
                "vaut donc deux fois un virgule cinq, soit trois "
                "centimètres par an."
            )
        ) as tracker:
            self.play(Write(etape4))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(etapes))

        # --- À retenir : encart méthode récapitulatif -------------------------
        recap = example_box(
            Text(
                _wrap(
                    "Méthode : v = d/t, puis convertir (1 km/Ma = "
                    "0,1 cm/an) ; distinguer demi-vitesse (un flanc) et "
                    "vitesse totale (= 2 × demi-vitesse). Ici : demi-vitesse "
                    "= 1,5 cm/an, vitesse d'expansion totale = 3 cm/an.",
                    width=54,
                ),
                font_size=22,
            ),
            box_width=12.0,
        )
        recap.next_to(titre, DOWN, buff=0.55)

        with self.voiceover(
            text=(
                "Retenons la méthode : vitesse égale distance sur temps, "
                "puis conversion d'unités, en n'oubliant jamais de "
                "distinguer la demi-vitesse, celle d'un seul flanc, de la "
                "vitesse d'expansion totale, qui vaut deux fois la "
                "demi-vitesse. Ici, la demi-vitesse est de un virgule cinq "
                "centimètre par an, et la vitesse d'expansion totale de "
                "trois centimètres par an."
            )
        ) as tracker:
            self.play(FadeIn(recap))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(recap), FadeOut(titre))
