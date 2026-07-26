"""
scenes/Chimie_Ethanol_04.py — Chapitre 7 « L'éthanol » (1ereC, Chimie),
scène 04.

§ 3. Propriétés physiques de l'éthanol. Tableau (liquide incolore, odeur
vineuse, Téb=78,5°C, Tfus=-114°C, d=0,789, ρ=789 g/L, miscible à l'eau en
toutes proportions, volatil, inflammable). Définition de la densité d'un
liquide. Explication de la miscibilité (liaisons hydrogène du -OH polaire
malgré la chaîne hydrophobe). Exemple résolu 3 : masse de 250 mL d'éthanol
(≈197,3 g) et volume de 100 g (≈126,7 mL).
Source : 1ereC/Chimie.pdf, chapitre 7, pages 70-71.
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
    FadeIn,
    FadeOut,
    Line,
    MathTex,
    Table,
    Text,
    VGroup,
    Write,
    config,
)

from shapes.base_scene import NotionScene
from shapes.boxes import definition_box, example_box, property_box, scene_title, warning_box


def _wrap(text: str, width: int = 56) -> str:
    return "\n".join(textwrap.fill(line, width=width) for line in text.split("\n"))


def _fit(mobject, top_y):
    bas_visible = -config.frame_height / 2 + 0.25
    hauteur_dispo = top_y - bas_visible
    if mobject.height > hauteur_dispo:
        mobject.scale(hauteur_dispo / mobject.height, about_point=mobject.get_top())
    return mobject


def _schema_liaison_hydrogene():
    """Schéma très simplifié : une molécule d'éthanol (OH polaire, chaîne
    hydrophobe) et une molécule d'eau reliées par une liaison hydrogène en
    pointillés — primitives de base uniquement."""
    ethanol = MathTex(r"\underbrace{CH_3-CH_2}_{\text{hydrophobe}}-\underbrace{O-H}_{\text{polaire}}", font_size=26, color=WHITE)
    eau = MathTex(r"H-O-H", font_size=26, color=BLUE)
    eau.next_to(ethanol, RIGHT, buff=1.4)

    liaison_h = Line(
        ethanol.get_right() + [0.05, 0.15, 0],
        eau.get_left() + [-0.05, 0.15, 0],
        color=YELLOW,
        stroke_width=2,
    )
    liaison_h.set_stroke(opacity=0.9)
    label_liaison = Text("liaison hydrogène", font_size=14, color=YELLOW)
    label_liaison.next_to(liaison_h, UP, buff=0.08)

    return VGroup(ethanol, eau, liaison_h, label_liaison)


class ProprietesPhysiquesEthanol(NotionScene):
    def construct(self):
        titre = scene_title("7.3 Propriétés physiques de l'éthanol")
        titre.scale(0.5)
        titre.to_edge(UP)

        # --- Énoncé : tableau des propriétés physiques --------------------------
        intro = Text("Quelles sont les propriétés physiques de l'éthanol ?", font_size=24, color=WHITE)
        intro.next_to(titre, DOWN, buff=0.4)

        rows = [
            ["État à 20°C", "liquide incolore"],
            ["Odeur", "caractéristique, vineuse"],
            ["Téb", "78,5°C"],
            ["Tfus", "-114°C"],
            ["Densité d", "0,789 (sans unité)"],
            ["Masse volumique ρ", "789 g/L"],
            ["Miscibilité à l'eau", "totale, toutes proportions"],
            ["Autres", "très volatil, inflammable"],
        ]
        table = Table(
            rows,
            col_labels=[Text(c, font_size=15, weight="BOLD") for c in ["Propriété", "Valeur / description"]],
            element_to_mobject=Text,
            element_to_mobject_config={"font_size": 14},
            line_config={"color": WHITE, "stroke_width": 1},
            include_outer_lines=True,
            v_buff=0.16,
            h_buff=0.3,
        )
        table.get_entries().set_color(WHITE)
        table.get_col_labels().set_color(YELLOW)
        for line in table.get_horizontal_lines():
            line.set_color(WHITE)
        for line in table.get_vertical_lines():
            line.set_color(WHITE)
        table.next_to(intro, DOWN, buff=0.3)
        _fit(table, intro.get_bottom()[1] - 0.3)
        table.next_to(intro, DOWN, buff=0.3)

        with self.voiceover(
            text=(
                "Quelles sont les propriétés physiques de l'éthanol ? "
                "À vingt degrés, c'est un liquide incolore à l'odeur "
                "caractéristique, vineuse. Sa température d'ébullition "
                "vaut soixante-dix-huit virgule cinq degrés, inférieure à "
                "celle de l'eau ; sa température de fusion vaut moins "
                "cent quatorze degrés. Sa densité vaut zéro virgule "
                "sept-cent-quatre-vingt-neuf, un nombre sans unité, ce "
                "qui correspond à une masse volumique de sept-cent-"
                "quatre-vingt-neuf grammes par litre. Il est miscible à "
                "l'eau en toutes proportions, très volatil et "
                "inflammable."
            )
        ) as tracker:
            self.play(Write(titre))
            self.play(FadeIn(intro))
            self.play(FadeIn(table))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(intro), FadeOut(table))

        # --- Raisonnement : définition de la densité + miscibilité --------------
        def_densite = definition_box(
            VGroup(
                Text(
                    _wrap(
                        "La densité d d'un liquide par rapport à l'eau est "
                        "le rapport de la masse volumique du liquide à "
                        "celle de l'eau :",
                        width=48,
                    ),
                    font_size=21,
                ),
                MathTex(r"d = \dfrac{\rho_{liquide}}{\rho_{eau}} \quad \text{(sans unité)}", font_size=26, color="#1A1A1A"),
            ).arrange(DOWN, buff=0.25),
        )
        def_densite.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "La densité d'un liquide par rapport à l'eau est le "
                "rapport de la masse volumique du liquide à celle de "
                "l'eau : d égale rho liquide sur rho eau. C'est un "
                "nombre sans unité. Comme la masse volumique de l'eau "
                "vaut un gramme par millilitre, la densité et la masse "
                "volumique exprimée en grammes par millilitre ont "
                "exactement la même valeur numérique."
            )
        ) as tracker:
            self.play(FadeIn(def_densite))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(def_densite))

        entete_miscibilite = Text("Pourquoi l'éthanol est-il miscible à l'eau ?", font_size=22, color=YELLOW, weight="BOLD")
        entete_miscibilite.next_to(titre, DOWN, buff=0.4)

        schema_miscibilite = _schema_liaison_hydrogene()
        schema_miscibilite.scale(0.95)
        schema_miscibilite.next_to(entete_miscibilite, DOWN, buff=0.55)

        explication = Text(
            _wrap(
                "Le groupe -OH est polaire : il forme des liaisons "
                "hydrogène avec l'eau. La courte chaîne carbonée "
                "hydrophobe n'empêche pas cette solubilité totale.",
                width=50,
            ),
            font_size=20,
            color=WHITE,
        )
        explication.next_to(schema_miscibilite, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Pourquoi l'éthanol est-il miscible à l'eau ? Le groupe "
                "hydroxyle, moins O-H, est polaire : il établit des "
                "liaisons hydrogène avec les molécules d'eau. La courte "
                "chaîne carbonée, C-2, H-5, qui elle est hydrophobe, "
                "n'empêche pas cette solubilité : éthanol et eau se "
                "mélangent donc en toutes proportions. C'est pourquoi une "
                "boisson alcoolisée est un mélange homogène."
            )
        ) as tracker:
            self.play(FadeIn(entete_miscibilite))
            self.play(FadeIn(schema_miscibilite))
            self.play(FadeIn(explication))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(entete_miscibilite), FadeOut(schema_miscibilite), FadeOut(explication))

        # --- Exemple résolu 3 : masse et volume d'éthanol -------------------------
        exemple3 = example_box(
            VGroup(
                Text("Exemple résolu 3 — Masse et volume d'éthanol (ρ = 0,789 g/mL)", font_size=19, weight="BOLD"),
                MathTex(r"a)\ m = \rho\times V = 0{,}789\times 250 \approx 197{,}3\ \text{g}\ \ (V=250\ \text{mL})", font_size=22, color="#1A1A1A"),
                MathTex(r"b)\ V = \dfrac{m}{\rho} = \dfrac{100}{0{,}789} \approx 126{,}7\ \text{mL}\ \ (m=100\ \text{g})", font_size=22, color="#1A1A1A"),
            ).arrange(DOWN, buff=0.3, aligned_edge=LEFT),
            box_width=12.4,
        )
        exemple3.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Exemple résolu trois. a) Quelle est la masse de deux "
                "cent cinquante millilitres d'éthanol ? m égale rho fois "
                "V, soit zéro virgule sept-cent-quatre-vingt-neuf fois "
                "deux cent cinquante, environ cent quatre-vingt-dix-sept "
                "virgule trois grammes. b) Quel volume occupent cent "
                "grammes d'éthanol ? V égale m sur rho, soit cent sur "
                "zéro virgule sept-cent-quatre-vingt-neuf, environ cent "
                "vingt-six virgule sept millilitres. L'éthanol est bien "
                "plus léger que l'eau : un litre d'éthanol ne pèse que "
                "sept-cent-quatre-vingt-neuf grammes."
            )
        ) as tracker:
            self.play(FadeIn(exemple3))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(exemple3))

        # --- À retenir : fiche récapitulative -------------------------------------
        propriete = property_box(
            VGroup(
                Text("Téb = 78,5°C ; Tfus = -114°C ; d = 0,789 ; ρ = 789 g/L", font_size=21, weight="BOLD"),
                Text("Miscible à l'eau (liaisons hydrogène) ; volatil, inflammable", font_size=21),
            ).arrange(DOWN, buff=0.3, aligned_edge=LEFT),
        )
        propriete.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Retenons l'essentiel : l'éthanol bout à soixante-dix-"
                "huit virgule cinq degrés et fond à moins cent quatorze "
                "degrés. Sa densité vaut zéro virgule sept-cent-quatre-"
                "vingt-neuf, soit une masse volumique de sept-cent-"
                "quatre-vingt-neuf grammes par litre. Il est miscible à "
                "l'eau grâce aux liaisons hydrogène de son groupe -OH, "
                "et il est à la fois volatil et inflammable."
            )
        ) as tracker:
            self.play(FadeIn(propriete))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(propriete))

        # --- Piège à éviter : volatil ≠ inflammable -------------------------------
        piege = warning_box(
            Text(
                _wrap(
                    "Ne confondez pas « volatil » (passe facilement à "
                    "l'état de vapeur, même à température ambiante) et "
                    "« inflammable » (peut s'enflammer au contact d'une "
                    "flamme) : l'éthanol possède les deux propriétés, mais "
                    "ce sont deux notions physiques distinctes.",
                    width=48,
                ),
                font_size=20,
            ),
        )
        piege.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Attention à ne pas confondre « volatil » et "
                "« inflammable ». Volatil signifie que le liquide passe "
                "facilement à l'état de vapeur, même à température "
                "ambiante. Inflammable signifie qu'il peut s'enflammer au "
                "contact d'une flamme. L'éthanol possède les deux "
                "propriétés, mais ce sont bien deux notions physiques "
                "distinctes, qu'il ne faut pas mélanger dans une "
                "réponse."
            )
        ) as tracker:
            self.play(FadeIn(piege))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(piege), FadeOut(titre))
