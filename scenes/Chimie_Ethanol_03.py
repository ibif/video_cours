"""
scenes/Chimie_Ethanol_03.py — Chapitre 7 « L'éthanol » (1ereC, Chimie),
scène 03.

§ 2.2 Obtention de l'éthanol — hydratation de l'éthylène (voie
industrielle). Équation CH₂=CH₂ + H₂O → CH₃-CH₂-OH (catalyseur H₂SO₄,
~300°C, pression élevée), réaction d'addition. Tableau comparatif
fermentation / hydratation. Exemple résolu 2 : fermentation de 90 g de
glucose (n=0,5 mol, n(éthanol)=1 mol, m=46 g, V≈58,3 mL, V(CO₂)=24 L).
Source : 1ereC/Chimie.pdf, chapitre 7, pages 69-70.
"""

import textwrap

from manim import (
    DOWN,
    LEFT,
    RIGHT,
    UP,
    WHITE,
    YELLOW,
    FadeIn,
    FadeOut,
    MathTex,
    Table,
    Text,
    VGroup,
    Write,
    config,
)

from shapes.base_scene import NotionScene
from shapes.boxes import example_box, scene_title, warning_box


def _wrap(text: str, width: int = 56) -> str:
    return "\n".join(textwrap.fill(line, width=width) for line in text.split("\n"))


def _fit(mobject, top_y):
    bas_visible = -config.frame_height / 2 + 0.25
    hauteur_dispo = top_y - bas_visible
    if mobject.height > hauteur_dispo:
        mobject.scale(hauteur_dispo / mobject.height, about_point=mobject.get_top())
    return mobject


class HydratationEthylene(NotionScene):
    def construct(self):
        titre = scene_title("7.2 Obtention de l'éthanol — hydratation de l'éthylène")
        titre.scale(0.46)
        titre.to_edge(UP)

        # --- Énoncé : la voie industrielle ---------------------------------------
        intro = Text(
            _wrap(
                "À côté de la fermentation, il existe une voie "
                "industrielle pour fabriquer l'éthanol, à partir du "
                "pétrole : l'hydratation de l'éthylène.",
                width=54,
            ),
            font_size=25,
            color=WHITE,
        )
        intro.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "À côté de la fermentation biologique, il existe une "
                "seconde voie pour fabriquer l'éthanol : une voie "
                "industrielle, issue de la pétrochimie, appelée "
                "hydratation de l'éthylène."
            )
        ) as tracker:
            self.play(Write(titre))
            self.play(FadeIn(intro))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(intro))

        # --- Raisonnement : équation + réaction d'addition -----------------------
        entete_eq = Text("L'hydratation de l'éthylène", font_size=23, color=YELLOW, weight="BOLD")
        entete_eq.next_to(titre, DOWN, buff=0.4)

        equation = MathTex(
            r"CH_2{=}CH_2 \;+\; H_2O \xrightarrow{H_2SO_4,\ 300°C} CH_3{-}CH_2{-}OH",
            font_size=28,
            color=WHITE,
        )
        equation.next_to(entete_eq, DOWN, buff=0.4)

        conditions = Text(
            _wrap(
                "L'éthylène (CH₂=CH₂), issu du vapocraquage du pétrole, "
                "réagit avec l'eau en présence d'acide sulfurique H₂SO₄ "
                "(catalyseur), à environ 300°C et sous pression élevée.",
                width=50,
            ),
            font_size=21,
            color=WHITE,
        )
        conditions.next_to(equation, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "L'éthylène, un alcène de formule C-H-2 égale C-H-2, "
                "obtenu par vapocraquage du pétrole, réagit avec l'eau en "
                "présence d'un catalyseur, l'acide sulfurique H-2, "
                "S-O-4, à environ trois cents degrés et sous pression "
                "élevée. On obtient directement de l'éthanol : C-H-2 "
                "égale C-H-2, plus H-2-O, donne C-H-3 tiret C-H-2 tiret "
                "O-H."
            )
        ) as tracker:
            self.play(FadeIn(entete_eq))
            self.play(Write(equation))
            self.play(FadeIn(conditions))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(entete_eq), FadeOut(equation), FadeOut(conditions))

        entete_addition = Text("Une réaction d'addition", font_size=23, color=YELLOW, weight="BOLD")
        entete_addition.next_to(titre, DOWN, buff=0.4)

        addition = Text(
            _wrap(
                "Il s'agit d'une réaction d'addition : la double liaison "
                "C=C s'ouvre, un -H se fixe sur un carbone et un -OH sur "
                "l'autre. Aucun atome n'est perdu, aucun sous-produit "
                "n'est formé.",
                width=50,
            ),
            font_size=22,
            color=WHITE,
        )
        addition.next_to(entete_addition, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Il s'agit d'une réaction d'addition : la double liaison "
                "carbone-carbone s'ouvre, un atome d'hydrogène se fixe "
                "sur l'un des deux carbones, et le groupe hydroxyle se "
                "fixe sur l'autre. Contrairement à la combustion, aucun "
                "atome n'est perdu et aucun sous-produit n'est formé : "
                "tous les atomes des réactifs se retrouvent dans "
                "l'éthanol."
            )
        ) as tracker:
            self.play(FadeIn(entete_addition))
            self.play(FadeIn(addition))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(entete_addition), FadeOut(addition))

        # --- Exemple traité : tableau comparatif + exemple résolu 2 -------------
        entete_tab = Text("Fermentation ou hydratation : comparaison", font_size=21, color=YELLOW, weight="BOLD")
        entete_tab.next_to(titre, DOWN, buff=0.35)

        rows = [
            ["Matière première", "sucres naturels", "éthylène (pétrole)"],
            ["Catalyseur", "enzymes (zymase)", "H₂SO₄"],
            ["Conditions", "25-35°C, sans air", "≈300°C, forte pression"],
            ["Degré obtenu", "≤16° (puis distillation)", "grande pureté"],
            ["Usage principal", "boissons, bioéthanol", "alcool industriel"],
        ]
        col_labels = ["Critère", "Fermentation", "Hydratation"]

        table = Table(
            rows,
            col_labels=[Text(c, font_size=15, weight="BOLD") for c in col_labels],
            element_to_mobject=Text,
            element_to_mobject_config={"font_size": 14},
            line_config={"color": WHITE, "stroke_width": 1},
            include_outer_lines=True,
            v_buff=0.18,
            h_buff=0.25,
        )
        table.get_entries().set_color(WHITE)
        table.get_col_labels().set_color(YELLOW)
        for line in table.get_horizontal_lines():
            line.set_color(WHITE)
        for line in table.get_vertical_lines():
            line.set_color(WHITE)
        table.next_to(entete_tab, DOWN, buff=0.3)
        _fit(table, entete_tab.get_bottom()[1] - 0.3)
        table.next_to(entete_tab, DOWN, buff=0.3)

        with self.voiceover(
            text=(
                "Comparons les deux voies. La fermentation part de sucres "
                "naturels et renouvelables, utilise les enzymes des "
                "levures comme catalyseur, se déroule à basse température "
                "sans air, et ne dépasse pas seize degrés sans "
                "distillation : elle sert surtout aux boissons et au "
                "bioéthanol. L'hydratation part de l'éthylène, issu du "
                "pétrole, utilise l'acide sulfurique comme catalyseur, "
                "exige environ trois cents degrés et une forte pression, "
                "et donne directement un alcool de grande pureté, "
                "réservé à l'usage industriel."
            )
        ) as tracker:
            self.play(FadeIn(entete_tab))
            self.play(FadeIn(table))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(entete_tab), FadeOut(table))

        # --- Exemple résolu 2 : fermentation de 90 g de glucose ------------------
        exemple2 = example_box(
            VGroup(
                Text("Fermentation de m = 90 g de glucose C₆H₁₂O₆ (M = 180 g/mol)", font_size=19, weight="BOLD"),
                MathTex(r"n(glucose) = \dfrac{90}{180} = 0{,}5\ \text{mol}", font_size=23, color="#1A1A1A"),
                MathTex(r"n(\text{éthanol}) = 2\times 0{,}5 = 1\ \text{mol} \;\Rightarrow\; m = 1\times 46 = 46\ \text{g}", font_size=23, color="#1A1A1A"),
                MathTex(r"V(\text{éthanol}) = \dfrac{46}{0{,}789} \approx 58{,}3\ \text{mL}", font_size=23, color="#1A1A1A"),
                MathTex(r"n(CO_2) = 1\ \text{mol} \;\Rightarrow\; V(CO_2) = 1\times 24 = 24\ \text{L}", font_size=23, color="#1A1A1A"),
            ).arrange(DOWN, buff=0.28, aligned_edge=LEFT),
            box_width=12.6,
        )
        exemple2.next_to(titre, DOWN, buff=0.35)
        _fit(exemple2, titre.get_bottom()[1] - 0.35)

        with self.voiceover(
            text=(
                "Exemple résolu deux : un jus de canne à sucre contient "
                "quatre-vingt-dix grammes de glucose, de masse molaire "
                "cent quatre-vingts grammes par mole. On réalise sa "
                "fermentation complète. La quantité de glucose vaut "
                "quatre-vingt-dix sur cent quatre-vingts, soit zéro "
                "virgule cinq mole. D'après l'équation, la quantité "
                "d'éthanol formée est le double, soit une mole, ce qui "
                "correspond à une masse de quarante-six grammes. Le "
                "volume d'éthanol vaut quarante-six sur zéro virgule "
                "sept-cent-quatre-vingt-neuf, soit environ cinquante-huit "
                "virgule trois millilitres. Enfin, la quantité de "
                "dioxyde de carbone dégagée est aussi d'une mole, soit un "
                "volume de vingt-quatre litres, avec un volume molaire de "
                "vingt-quatre litres par mole."
            )
        ) as tracker:
            self.play(FadeIn(exemple2))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(exemple2))

        # --- Piège à éviter : addition ≠ substitution -----------------------------
        piege = warning_box(
            Text(
                _wrap(
                    "Ne confondez pas addition et substitution : dans "
                    "l'hydratation de l'éthylène, la double liaison "
                    "disparaît et rien n'est éliminé (réaction d'addition). "
                    "N'oubliez pas non plus de préciser le catalyseur et "
                    "les conditions (H₂SO₄, ~300°C, pression élevée) : "
                    "sans eux, la réaction n'a pas lieu à température "
                    "ordinaire.",
                    width=48,
                ),
                font_size=20,
            ),
        )
        piege.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Attention à ne pas confondre addition et substitution : "
                "dans l'hydratation de l'éthylène, la double liaison "
                "disparaît et rien n'est éliminé, c'est bien une réaction "
                "d'addition. N'oubliez pas non plus de préciser le "
                "catalyseur et les conditions expérimentales, acide "
                "sulfurique, environ trois cents degrés, pression élevée "
                ": sans eux, la réaction n'a pratiquement pas lieu à "
                "température ordinaire."
            )
        ) as tracker:
            self.play(FadeIn(piege))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(piege), FadeOut(titre))
