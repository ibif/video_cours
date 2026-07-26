"""
scenes/Chimie_Ethanol_05.py — Chapitre 7 « L'éthanol » (1ereC, Chimie),
scène 05.

§ 4.1 Combustion de l'éthanol : oxydation totale (destruction du squelette
carboné). Équation C₂H₅OH + 3O₂ → 2CO₂ + 3H₂O, flamme bleue pâle, très
exothermique (≈1360 kJ/mol), usages (lampes à alcool, cheminées
bioéthanol). Exemple résolu 4 : combustion de 9,2 g d'éthanol (n=0,2 mol,
calculs O₂ consommé / CO₂ formé / H₂O formée).
Source : 1ereC/Chimie.pdf, chapitre 7, pages 70-71.
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
    Ellipse,
    FadeIn,
    FadeOut,
    MathTex,
    Text,
    VGroup,
    Write,
    config,
)

from shapes.base_scene import NotionScene
from shapes.boxes import example_box, property_box, scene_title, warning_box


def _wrap(text: str, width: int = 56) -> str:
    return "\n".join(textwrap.fill(line, width=width) for line in text.split("\n"))


def _bullets(items, font_size=22, color=WHITE, width=54):
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


def _flamme_bleue():
    """Flamme stylisée bleu pâle, construite avec deux ellipses imbriquées
    (primitives Manim de base)."""
    exterieure = Ellipse(width=0.7, height=1.3, color=BLUE, fill_color=BLUE, fill_opacity=0.5, stroke_width=2)
    interieure = Ellipse(width=0.35, height=0.75, color="#CFE9FF", fill_color="#CFE9FF", fill_opacity=0.8, stroke_width=1)
    interieure.move_to(exterieure.get_center() + DOWN * 0.15)
    return VGroup(exterieure, interieure)


class CombustionEthanol(NotionScene):
    def construct(self):
        titre = scene_title("7.4 Combustion de l'éthanol")
        titre.scale(0.55)
        titre.to_edge(UP)

        # --- Énoncé : la combustion, une oxydation totale ------------------------
        flamme = _flamme_bleue()
        flamme.scale(1.3)
        flamme.next_to(titre, DOWN, buff=0.5)

        intro = Text(
            _wrap(
                "L'éthanol brûle dans le dioxygène de l'air avec une "
                "flamme bleue pâle, en produisant du dioxyde de carbone "
                "et de l'eau : le squelette carboné est détruit.",
                width=52,
            ),
            font_size=22,
            color=WHITE,
        )
        intro.next_to(flamme, RIGHT, buff=0.6)

        with self.voiceover(
            text=(
                "L'éthanol brûle dans le dioxygène de l'air avec une "
                "flamme bleue pâle, en produisant du dioxyde de carbone "
                "et de l'eau. Le squelette carboné de la molécule est "
                "entièrement détruit : on parle d'oxydation totale."
            )
        ) as tracker:
            self.play(Write(titre))
            self.play(FadeIn(flamme))
            self.play(FadeIn(intro))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(flamme), FadeOut(intro))

        # --- Raisonnement : équation + caractère exothermique --------------------
        equation = MathTex(r"C_2H_5OH + 3\,O_2 \longrightarrow 2\,CO_2 + 3\,H_2O", font_size=30, color=WHITE)
        equation.next_to(titre, DOWN, buff=0.5)

        energie = MathTex(r"\Delta H \approx -1360\ \text{kJ/mol} \quad (\text{très exothermique})", font_size=26, color=YELLOW)
        energie.next_to(equation, DOWN, buff=0.45)

        usages = _bullets(
            [
                "Lampes à alcool de laboratoire.",
                "Cheminées et poêles au bioéthanol.",
                "Production de chaleur en général (carburants).",
            ],
            font_size=20,
            width=52,
        )
        usages.next_to(energie, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "L'équation-bilan de la combustion s'écrit : C-2, H-5, "
                "O-H, plus trois O-2, donne deux C-O-2, plus trois H-2-O. "
                "Cette réaction est très exothermique : la combustion "
                "d'une mole d'éthanol dégage environ mille trois cent "
                "soixante kilojoules. C'est pourquoi on l'utilise pour "
                "produire de la chaleur : lampes à alcool de laboratoire, "
                "cheminées et poêles au bioéthanol, et plus généralement "
                "comme carburant."
            )
        ) as tracker:
            self.play(Write(equation))
            self.play(FadeIn(energie))
            self.play(FadeIn(usages))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(equation), FadeOut(energie), FadeOut(usages))

        # --- Exemple résolu 4 : combustion de 9,2 g d'éthanol --------------------
        exemple4 = example_box(
            VGroup(
                Text("Exemple résolu 4 — Combustion de m = 9,2 g d'éthanol (Vₘ = 24 L/mol)", font_size=18, weight="BOLD"),
                MathTex(r"n(\text{éthanol}) = \dfrac{9{,}2}{46} = 0{,}2\ \text{mol}", font_size=22, color="#1A1A1A"),
                MathTex(r"n(O_2) = 3\times 0{,}2 = 0{,}6\ \text{mol} \;\Rightarrow\; V(O_2) = 0{,}6\times 24 = 14{,}4\ \text{L}", font_size=21, color="#1A1A1A"),
                MathTex(r"n(CO_2) = 2\times 0{,}2 = 0{,}4\ \text{mol} \;\Rightarrow\; V(CO_2) = 0{,}4\times 24 = 9{,}6\ \text{L}", font_size=21, color="#1A1A1A"),
                MathTex(r"n(H_2O) = 3\times 0{,}2 = 0{,}6\ \text{mol} \;\Rightarrow\; m(H_2O) = 0{,}6\times 18 = 10{,}8\ \text{g}", font_size=21, color="#1A1A1A"),
            ).arrange(DOWN, buff=0.26, aligned_edge=LEFT),
            box_width=12.8,
        )
        exemple4.next_to(titre, DOWN, buff=0.35)
        _fit(exemple4, titre.get_bottom()[1] - 0.35)

        with self.voiceover(
            text=(
                "Exemple résolu quatre : on brûle neuf virgule deux "
                "grammes d'éthanol. La quantité d'éthanol vaut neuf "
                "virgule deux sur quarante-six, soit zéro virgule deux "
                "mole. Le dioxygène consommé vaut trois fois zéro virgule "
                "deux, soit zéro virgule six mole, c'est-à-dire quatorze "
                "virgule quatre litres. Le dioxyde de carbone formé vaut "
                "deux fois zéro virgule deux, soit zéro virgule quatre "
                "mole, c'est-à-dire neuf virgule six litres. Enfin, l'eau "
                "formée vaut trois fois zéro virgule deux, soit zéro "
                "virgule six mole, c'est-à-dire dix virgule huit "
                "grammes."
            )
        ) as tracker:
            self.play(FadeIn(exemple4))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(exemple4))

        # --- À retenir : fiche récapitulative -------------------------------------
        propriete = property_box(
            VGroup(
                MathTex(r"C_2H_5OH + 3\,O_2 \rightarrow 2\,CO_2 + 3\,H_2O", font_size=26, color="#1A1A1A"),
                Text("Flamme bleue pâle, oxydation totale, très exothermique (≈1360 kJ/mol)", font_size=19),
            ).arrange(DOWN, buff=0.3),
        )
        propriete.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Retenons l'essentiel : la combustion complète de "
                "l'éthanol produit du dioxyde de carbone et de l'eau, "
                "avec une flamme bleue pâle. C'est une oxydation totale, "
                "qui détruit le squelette carboné, et une réaction très "
                "exothermique, environ mille trois cent soixante "
                "kilojoules par mole."
            )
        ) as tracker:
            self.play(FadeIn(propriete))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(propriete))

        # --- Piège à éviter : coefficient 3n/2 peut être fractionnaire ---------
        piege = warning_box(
            Text(
                _wrap(
                    "Pour un alcool CₙH₂ₙ₊₂O, le coefficient devant O₂ "
                    "dans la combustion vaut 3n/2. Pour l'éthanol (n=2), "
                    "cela tombe juste sur 3, mais pour d'autres alcools ce "
                    "peut être un nombre fractionnaire : il faut alors "
                    "multiplier toute l'équation par 2, ce n'est pas une "
                    "erreur d'équilibrage.",
                    width=48,
                ),
                font_size=20,
            ),
        )
        piege.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Attention à un piège classique : pour un alcool de "
                "formule C indice n, H indice deux n plus deux, O, le "
                "coefficient devant le dioxygène dans la combustion vaut "
                "trois n sur deux. Pour l'éthanol, où n égale deux, cela "
                "tombe juste sur trois, mais pour d'autres alcools ce "
                "peut être un nombre fractionnaire : il faut alors "
                "multiplier toute l'équation par deux, ce n'est pas une "
                "erreur d'équilibrage."
            )
        ) as tracker:
            self.play(FadeIn(piege))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(piege), FadeOut(titre))
