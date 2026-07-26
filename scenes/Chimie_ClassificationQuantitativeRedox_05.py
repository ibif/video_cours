"""
scenes/Chimie_ClassificationQuantitativeRedox_05.py — Chapitre 11
« Classification quantitative des couples oxydant/réducteur » (1ereC,
Chimie), scène 05.

§ 5. Le potentiel standard d'oxydoréduction. Rappel des conditions
standard (25 °C, concentrations = 1 mol/L, pression = 1 bar).
`definition_box` du potentiel standard E°(Ox/Red) : f.é.m. de la pile
formée par l'ENH et l'électrode standard du couple étudié, avec un signe
qui dépend de la polarité observée (positif si l'électrode standard est
le pôle +, négatif si elle est le pôle -). Deux mesures fondamentales :
Cu²⁺/Cu à +0,34 V (électrode standard = pôle +) et Zn²⁺/Zn à -0,76 V
(électrode standard = pôle -). Exemple résolu 1 : détermination du
potentiel standard du nickel, E°(Ni²⁺/Ni) = -0,23 V.
Source : 1ereC/Chimie.pdf, chapitre 11, pages 106-107.
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
from shapes.boxes import definition_box, example_box, scene_title


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


class PotentielStandardOxydoreduction(NotionScene):
    def construct(self):
        titre = scene_title("11.5 Le potentiel standard d'oxydoréduction")
        titre.scale(0.5)
        titre.to_edge(UP)

        # --- Énoncé : conditions standard --------------------------------------------
        intro = Text(
            _wrap(
                "Pour comparer les couples entre eux de façon fiable, on "
                "fixe des conditions expérimentales précises, dites "
                "conditions standard.",
                width=56,
            ),
            font_size=24,
            color=WHITE,
        )
        intro.next_to(titre, DOWN, buff=0.5)
        conditions = _bullets(
            [
                "Température : 25 °C",
                "Concentration de chaque espèce dissoute : c = 1 mol/L",
                "Pression de chaque espèce gazeuse : p = 1 bar",
            ],
            font_size=21,
            width=50,
        )
        conditions.next_to(intro, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Pour comparer les couples entre eux de façon fiable, on "
                "fixe des conditions expérimentales précises, appelées "
                "conditions standard : température de vingt-cinq degrés "
                "Celsius, concentration de chaque espèce dissoute égale à "
                "un mole par litre, et pression de chaque espèce gazeuse "
                "égale à un bar."
            )
        ) as tracker:
            self.play(Write(titre))
            self.play(FadeIn(intro))
            self.play(FadeIn(conditions))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(intro), FadeOut(conditions))

        # --- Raisonnement : définition du potentiel standard -------------------------
        def_e0 = definition_box(
            Text(
                _wrap(
                    "Le potentiel standard E°(Ox/Red) d'un couple est la "
                    "f.é.m. de la pile formée par l'électrode standard de "
                    "ce couple et l'ENH. Il est positif si l'électrode du "
                    "couple est le pôle +, négatif si elle est le pôle -.",
                    width=48,
                ),
                font_size=21,
            ),
            box_width=12.2,
        )
        def_e0.next_to(titre, DOWN, buff=0.35)

        with self.voiceover(
            text=(
                "On définit alors le potentiel standard d'un couple Ox "
                "sur Red, noté E rond de Ox sur Red, comme la force "
                "électromotrice de la pile formée par l'électrode "
                "standard de ce couple, dans les conditions que nous "
                "venons de fixer, associée à l'électrode normale à "
                "hydrogène. Ce potentiel est compté positif si "
                "l'électrode du couple étudié constitue le pôle positif "
                "de cette pile, et négatif si elle constitue le pôle "
                "négatif."
            )
        ) as tracker:
            self.play(FadeIn(def_e0))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(def_e0))

        # --- Exemple traité : deux mesures fondamentales ------------------------------
        entete_mesures = Text("Deux mesures fondamentales", font_size=22, color=YELLOW, weight="BOLD")
        entete_mesures.next_to(titre, DOWN, buff=0.35)

        mesure_cu = VGroup(
            Text("Pile ENH | Cu²⁺/Cu : le cuivre est le pôle ⊕", font_size=20, color=ORANGE),
            MathTex(r"E^{\circ}(Cu^{2+}/Cu) = +0{,}34\ V", font_size=28, color=WHITE),
        ).arrange(DOWN, buff=0.2)

        mesure_zn = VGroup(
            Text("Pile ENH | Zn²⁺/Zn : le zinc est le pôle ⊖", font_size=20, color=BLUE),
            MathTex(r"E^{\circ}(Zn^{2+}/Zn) = -0{,}76\ V", font_size=28, color=WHITE),
        ).arrange(DOWN, buff=0.2)

        mesures = VGroup(mesure_cu, mesure_zn).arrange(DOWN, buff=0.55)
        mesures.next_to(entete_mesures, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Appliquons cette définition à nos deux couples déjà "
                "connus. Dans la pile formée par l'E-N-H et l'électrode "
                "standard de cuivre, le cuivre est le pôle positif : son "
                "potentiel standard vaut donc plus zéro virgule "
                "trente-quatre volt. Dans la pile formée par l'E-N-H et "
                "l'électrode standard de zinc, le zinc est le pôle "
                "négatif : son potentiel standard vaut donc moins zéro "
                "virgule soixante-seize volt."
            )
        ) as tracker:
            self.play(FadeIn(entete_mesures))
            self.play(Write(mesure_cu))
            self.play(Write(mesure_zn))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(entete_mesures), FadeOut(mesures))

        # --- Exemple résolu 1 : E° du nickel -----------------------------------------
        exemple_ni = example_box(
            VGroup(
                Text(
                    "Exemple résolu — pile ENH | Ni²⁺/Ni",
                    font_size=20,
                    weight="BOLD",
                ),
                Text(
                    "Mesure : le nickel constitue le pôle négatif de la pile.",
                    font_size=19,
                ),
                MathTex(r"E^{\circ}(Ni^{2+}/Ni) = -0{,}23\ V", font_size=26, color="#1A1A1A"),
            ).arrange(DOWN, buff=0.3, aligned_edge=LEFT),
            box_width=12.0,
        )
        exemple_ni.next_to(titre, DOWN, buff=0.45)

        with self.voiceover(
            text=(
                "Prenons un exemple résolu : on forme la pile E-N-H "
                "associée à l'électrode standard du nickel. On observe "
                "que le nickel constitue le pôle négatif de cette pile, "
                "et le voltmètre indique une tension de zéro virgule "
                "vingt-trois volt. On en déduit que le potentiel standard "
                "du couple ion nickel deux plus sur nickel vaut moins "
                "zéro virgule vingt-trois volt : négatif, puisque le "
                "nickel est le pôle négatif."
            )
        ) as tracker:
            self.play(FadeIn(exemple_ni))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(exemple_ni))

        # --- À retenir -----------------------------------------------------------------
        recap = _bullets(
            [
                "E°(Ox/Red) = f.é.m. de la pile [ENH | électrode standard "
                "du couple], avec un signe donné par la polarité.",
                "E°(Cu²⁺/Cu) = +0,34 V ; E°(Zn²⁺/Zn) = -0,76 V ; "
                "E°(Ni²⁺/Ni) = -0,23 V.",
            ],
            font_size=20,
            width=56,
        )
        entete_recap = Text("À retenir", font_size=22, color="#288073", weight="BOLD")
        entete_recap.next_to(titre, DOWN, buff=0.4)
        recap.next_to(entete_recap, DOWN, buff=0.35)

        with self.voiceover(
            text=(
                "Retenons l'essentiel : le potentiel standard d'un couple "
                "est la force électromotrice de la pile formée avec "
                "l'électrode normale à hydrogène, affectée d'un signe qui "
                "dépend de la polarité observée. Nous avons ainsi établi "
                "trois valeurs : plus zéro virgule trente-quatre volt "
                "pour le cuivre, moins zéro virgule soixante-seize volt "
                "pour le zinc, moins zéro virgule vingt-trois volt pour "
                "le nickel."
            )
        ) as tracker:
            self.play(FadeIn(entete_recap))
            self.play(FadeIn(recap))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(entete_recap), FadeOut(recap), FadeOut(titre))
