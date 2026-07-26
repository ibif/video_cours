"""
scenes/Chimie_ClassificationQuantitativeRedox_08.py — Chapitre 11
« Classification quantitative des couples oxydant/réducteur » (1ereC,
Chimie), scène 08.

§ 8. Prévision quantitative : critère de spontanéité. `theorem_box` du
critère des potentiels standard (si E°₁ > E°₂, la réaction
Ox₁ + Red₂ → Red₁ + Ox₂ est spontanée), définition de ΔE° = E°₁ - E°₂.
Règle empirique sur l'ampleur de la réaction : ΔE° > 0,3 V → réaction
quasi totale, ΔE° < 0,3 V (mais > 0) → réaction limitée (équilibre),
ΔE° < 0 → sens inverse spontané. Exemple résolu 2 : couples Ag⁺/Ag et
Cu²⁺/Cu (ΔE° = 0,46 V, réaction quasi totale). Exemple résolu 3 :
attaque du cuivre par les ions Fe³⁺, application industrielle à la
gravure des circuits imprimés.
Source : 1ereC/Chimie.pdf, chapitre 11, pages 109-110.
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
    GREEN,
    Arrow,
    FadeIn,
    FadeOut,
    MathTex,
    Text,
    VGroup,
    Write,
    config,
)

from shapes.base_scene import NotionScene
from shapes.boxes import example_box, scene_title, theorem_box, warning_box


def _wrap(text: str, width: int = 56) -> str:
    return "\n".join(textwrap.fill(line, width=width) for line in text.split("\n"))


def _bullets(items, font_size=21, color=WHITE, width=54):
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


class PrevisionQuantitativeCritereSpontaneite(NotionScene):
    def construct(self):
        titre = scene_title("11.8 Prévision quantitative : critère de spontanéité")
        titre.scale(0.44)
        titre.to_edge(UP)

        # --- Énoncé -------------------------------------------------------------------
        intro = Text(
            _wrap(
                "La règle du gamma nous donnait un sens de réaction. Le "
                "potentiel standard va faire bien mieux : donner ce "
                "même sens ET chiffrer l'ampleur de la réaction.",
                width=56,
            ),
            font_size=23,
            color=WHITE,
        )
        intro.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "La règle du gamma nous donnait seulement un sens de "
                "réaction. Le potentiel standard va faire bien mieux : "
                "il va nous donner ce même sens, mais aussi nous "
                "permettre de chiffrer l'ampleur de la réaction, "
                "c'est-à-dire de savoir si elle est totale ou seulement "
                "limitée."
            )
        ) as tracker:
            self.play(Write(titre))
            self.play(FadeIn(intro))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(intro))

        # --- Raisonnement : critère + delta E° -----------------------------------------
        theo = theorem_box(
            VGroup(
                Text("Critère des potentiels standard :", font_size=21, weight="BOLD"),
                Text("si E°₁ > E°₂, la réaction suivante est spontanée :", font_size=19),
                MathTex(r"Ox_1 + Red_2 \longrightarrow Red_1 + Ox_2", font_size=28, color="#1A1A1A"),
                MathTex(r"\Delta E^{\circ} = E^{\circ}_1 - E^{\circ}_2 > 0", font_size=26, color="#1A1A1A"),
            ).arrange(DOWN, buff=0.28),
            box_width=12.4,
        )
        theo.next_to(titre, DOWN, buff=0.35)

        with self.voiceover(
            text=(
                "Voici le critère des potentiels standard. Si le "
                "potentiel standard du couple un est supérieur à celui "
                "du couple deux, alors la réaction de l'oxydant du "
                "couple un avec le réducteur du couple deux, donnant le "
                "réducteur du couple un et l'oxydant du couple deux, est "
                "spontanée. On définit l'écart delta E rond comme la "
                "différence E rond un moins E rond deux, qui doit être "
                "positif pour que cette réaction soit spontanée."
            )
        ) as tracker:
            self.play(FadeIn(theo))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(theo))

        entete_regle = Text("Règle empirique sur l'ampleur de la réaction", font_size=21, color=YELLOW, weight="BOLD")
        entete_regle.next_to(titre, DOWN, buff=0.35)

        regle = _bullets(
            [
                "ΔE° > 0,3 V : la réaction est considérée comme "
                "quasi totale.",
                "0 < ΔE° < 0,3 V : la réaction est limitée, elle "
                "atteint un état d'équilibre (réactifs et produits "
                "coexistent).",
                "ΔE° < 0 : c'est le sens inverse qui est spontané.",
            ],
            font_size=20,
            width=54,
        )
        regle.next_to(entete_regle, DOWN, buff=0.3)

        with self.voiceover(
            text=(
                "Une règle empirique permet même de chiffrer l'ampleur "
                "de cette réaction. Si delta E rond dépasse zéro virgule "
                "trois volt, la réaction est considérée comme quasi "
                "totale. Si delta E rond est positif mais inférieur à "
                "zéro virgule trois volt, la réaction est limitée : elle "
                "atteint un état d'équilibre où réactifs et produits "
                "coexistent. Et si delta E rond est négatif, c'est le "
                "sens inverse qui est spontané."
            )
        ) as tracker:
            self.play(FadeIn(entete_regle))
            self.play(FadeIn(regle))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(entete_regle), FadeOut(regle))

        # --- Exemple résolu 2 : Ag+/Ag et Cu2+/Cu ---------------------------------------
        exemple2 = example_box(
            VGroup(
                Text("Exemple résolu — couples Ag⁺/Ag et Cu²⁺/Cu", font_size=20, weight="BOLD"),
                MathTex(
                    r"E^{\circ}(Ag^{+}/Ag) = 0{,}80\ V \; > \; E^{\circ}(Cu^{2+}/Cu) = 0{,}34\ V",
                    font_size=23,
                    color="#1A1A1A",
                ),
                MathTex(
                    r"2\,Ag^{+} + Cu \longrightarrow 2\,Ag + Cu^{2+}",
                    font_size=26,
                    color="#1A1A1A",
                ),
                MathTex(r"\Delta E^{\circ} = 0{,}80 - 0{,}34 = 0{,}46\ V \; (> 0{,}3\ V)", font_size=23, color="#1A1A1A"),
                Text("→ réaction quasi totale : le cuivre attaque les ions Ag⁺.", font_size=18),
            ).arrange(DOWN, buff=0.25, aligned_edge=LEFT),
            box_width=12.4,
        )
        exemple2.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Appliquons ce critère aux couples ion argent sur "
                "argent, et ion cuivre deux plus sur cuivre. Le "
                "potentiel standard de l'argent, zéro virgule quatre-"
                "vingt volt, est supérieur à celui du cuivre, zéro "
                "virgule trente-quatre volt. La réaction spontanée est "
                "donc : deux ions argent, plus cuivre, donne deux argent "
                "métal, plus ion cuivre deux plus. L'écart delta E rond "
                "vaut zéro virgule quarante-six volt, largement "
                "supérieur à zéro virgule trois volt : la réaction est "
                "quasi totale, le cuivre attaque effectivement les ions "
                "argent."
            )
        ) as tracker:
            self.play(FadeIn(exemple2))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(exemple2))

        # --- Exemple résolu 3 : Fe3+ attaque le cuivre (circuits imprimés) --------------
        exemple3 = example_box(
            VGroup(
                Text("Exemple résolu — gravure des circuits imprimés", font_size=20, weight="BOLD"),
                MathTex(
                    r"E^{\circ}(Fe^{3+}/Fe^{2+}) = 0{,}77\ V \; > \; E^{\circ}(Cu^{2+}/Cu) = 0{,}34\ V",
                    font_size=21,
                    color="#1A1A1A",
                ),
                MathTex(
                    r"2\,Fe^{3+} + Cu \longrightarrow 2\,Fe^{2+} + Cu^{2+}",
                    font_size=25,
                    color="#1A1A1A",
                ),
                Text(
                    "Application : le chlorure de fer(III) grave le cuivre non "
                    "protégé par le vernis lors de la fabrication d'un "
                    "circuit imprimé.",
                    font_size=17,
                ),
            ).arrange(DOWN, buff=0.25, aligned_edge=LEFT),
            box_width=12.6,
        )
        exemple3.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Un deuxième exemple, très concret : le potentiel "
                "standard du couple ion fer trois plus sur ion fer deux "
                "plus, zéro virgule soixante-dix-sept volt, est supérieur "
                "à celui du cuivre. Les ions fer trois plus attaquent "
                "donc spontanément le cuivre métal, formant des ions fer "
                "deux plus et des ions cuivre deux plus. C'est exactement "
                "le principe utilisé dans l'industrie électronique : une "
                "solution de chlorure de fer trois grave le cuivre non "
                "protégé par le vernis, lors de la fabrication d'un "
                "circuit imprimé."
            )
        ) as tracker:
            self.play(FadeIn(exemple3))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(exemple3), FadeOut(titre))
