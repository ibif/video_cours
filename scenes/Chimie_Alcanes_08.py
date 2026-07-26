"""
scenes/Chimie_Alcanes_08.py — Chapitre 2 « Hydrocarbures saturés — les
alcanes » (1ereC, Chimie), scène 08.

§ 6.1 Propriétés physiques (1/2) : état physique et points d'ébullition
(gazeux C₁-C₄, liquides C₅-C₁₇, solides ≥C₁₈, tableau des 10 premiers
alcanes, graphique Téb vs n), propriété « Téb augmente régulièrement
avec n », propriété « à formule brute égale, plus la chaîne est
ramifiée, plus Téb est bas » (C₅H₁₂ : 36°C/28°C/9,5°C).
Source : 1ereC/Chimie.pdf, pages 20-21.
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
    Axes,
    Create,
    Dot,
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
from shapes.boxes import property_box, scene_title, warning_box


def _wrap(text: str, width: int = 56) -> str:
    return "\n".join(textwrap.fill(line, width=width) for line in text.split("\n"))


def _fit(mobject, top_y):
    bas_visible = -config.frame_height / 2 + 0.25
    hauteur_dispo = top_y - bas_visible
    if mobject.height > hauteur_dispo:
        mobject.scale(hauteur_dispo / mobject.height, about_point=mobject.get_top())
    return mobject


class ProprietesPhysiques1(NotionScene):
    def construct(self):
        titre = scene_title("6. Propriétés physiques (1/2) : Téb et état")
        titre.scale(0.55)
        titre.to_edge(UP)

        # --- Énoncé : état physique selon le nombre de carbones -----------------
        etats = Text(
            _wrap(
                "Dans les conditions ordinaires (25°C, pression "
                "atmosphérique) : les alcanes de C₁ à C₄ sont gazeux ; de "
                "C₅ à C₁₇ environ, liquides ; au-delà de C₁₈, solides "
                "(paraffines, cires).",
                width=54,
            ),
            font_size=24,
            color=WHITE,
        )
        etats.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Dans les conditions ordinaires de température, environ "
                "vingt-cinq degrés, et de pression, l'état physique des "
                "alcanes dépend directement du nombre de carbones. Les "
                "alcanes de C-1 à C-4 sont gazeux : méthane, éthane, "
                "propane, butane. Ceux de C-5 à C-17 environ sont "
                "liquides : ce sont les composants de l'essence et du "
                "gas-oil. Au-delà de C-18, ils sont solides : ce sont les "
                "paraffines et les cires."
            )
        ) as tracker:
            self.play(Write(titre))
            self.play(FadeIn(etats))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(etats))

        # --- Raisonnement : tableau des 10 premiers alcanes ----------------------
        entete_tab = Text("État et point d'ébullition des 10 premiers alcanes", font_size=18, color=YELLOW, weight="BOLD")
        entete_tab.next_to(titre, DOWN, buff=0.3)

        rows = [
            ["méthane", "CH₄", "gaz", "-162°C"],
            ["éthane", "C₂H₆", "gaz", "-89°C"],
            ["propane", "C₃H₈", "gaz", "-42°C"],
            ["butane", "C₄H₁₀", "gaz", "-0,5°C"],
            ["pentane", "C₅H₁₂", "liquide", "36°C"],
            ["hexane", "C₆H₁₄", "liquide", "69°C"],
            ["heptane", "C₇H₁₆", "liquide", "98°C"],
            ["octane", "C₈H₁₈", "liquide", "126°C"],
            ["nonane", "C₉H₂₀", "liquide", "151°C"],
            ["décane", "C₁₀H₂₂", "liquide", "174°C"],
        ]
        col_labels = ["nom", "formule", "état (25°C)", "Téb"]
        table = Table(
            rows,
            col_labels=[Text(c, font_size=15, weight="BOLD") for c in col_labels],
            element_to_mobject=Text,
            element_to_mobject_config={"font_size": 14},
            line_config={"color": WHITE, "stroke_width": 1},
            include_outer_lines=True,
            v_buff=0.18,
            h_buff=0.3,
        )
        table.get_entries().set_color(WHITE)
        table.get_col_labels().set_color(YELLOW)
        for line in table.get_horizontal_lines():
            line.set_color(WHITE)
        for line in table.get_vertical_lines():
            line.set_color(WHITE)
        table.next_to(entete_tab, DOWN, buff=0.25)

        _bas_visible = -config.frame_height / 2 + 0.3
        _hauteur_dispo = table.get_top()[1] - _bas_visible
        if table.height > _hauteur_dispo:
            table.scale(_hauteur_dispo / table.height, about_point=table.get_top())
        _largeur_dispo = config.frame_width - 0.6
        if table.width > _largeur_dispo:
            table.scale(_largeur_dispo / table.width, about_point=table.get_top())
        table.next_to(entete_tab, DOWN, buff=0.25)

        with self.voiceover(
            text=(
                "Voici le tableau des dix premiers alcanes, avec leur "
                "état à vingt-cinq degrés et leur point d'ébullition. On "
                "observe une bascule nette entre le butane, gazeux, à "
                "moins zéro virgule cinq degré, et le pentane, liquide, à "
                "trente-six degrés."
            )
        ) as tracker:
            self.play(FadeIn(entete_tab))
            self.play(FadeIn(table))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(entete_tab), FadeOut(table))

        # --- Exemple traité : graphique Téb en fonction de n ---------------------
        entete_graphe = Text("Évolution du point d'ébullition avec n", font_size=22, color=YELLOW, weight="BOLD")
        entete_graphe.next_to(titre, DOWN, buff=0.35)

        axes = Axes(
            x_range=[0, 11, 1],
            y_range=[-200, 200, 50],
            x_length=8.5,
            y_length=4.3,
            axis_config={"color": WHITE, "stroke_width": 2, "include_tip": True, "font_size": 16},
        )
        x_label = Text("n (nb de C)", font_size=16, color=WHITE).next_to(axes.x_axis, RIGHT, buff=0.15)
        y_label = Text("Téb (°C)", font_size=16, color=WHITE).next_to(axes.y_axis, UP, buff=0.15)

        valeurs = [-162, -89, -42, -0.5, 36, 69, 98, 126, 151, 174]
        points = VGroup(*[Dot(axes.c2p(n + 1, valeurs[n]), color=BLUE, radius=0.06) for n in range(10)])
        courbe = axes.plot_line_graph(
            x_values=list(range(1, 11)),
            y_values=valeurs,
            line_color=YELLOW,
            add_vertex_dots=False,
            stroke_width=2.5,
        )

        graphe = VGroup(axes, x_label, y_label, courbe, points)
        graphe.next_to(entete_graphe, DOWN, buff=0.35)
        _fit(graphe, entete_graphe.get_bottom()[1] - 0.35)

        with self.voiceover(
            text=(
                "Reportons ces valeurs sur un graphique, le point "
                "d'ébullition en fonction du nombre de carbones n. On "
                "observe une courbe régulièrement croissante : plus la "
                "chaîne s'allonge, plus il faut chauffer pour vaporiser "
                "le liquide."
            )
        ) as tracker:
            self.play(FadeIn(entete_graphe))
            self.play(Create(axes), FadeIn(x_label), FadeIn(y_label))
            self.play(Create(courbe), FadeIn(points))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(entete_graphe), FadeOut(graphe))

        # --- À retenir : les deux propriétés du Téb -------------------------------
        propriete1 = property_box(
            Text(
                _wrap(
                    "Le point d'ébullition des alcanes linéaires augmente "
                    "régulièrement avec le nombre n d'atomes de carbone "
                    "(masse molaire et interactions de van der Waals "
                    "croissantes).",
                    width=48,
                ),
                font_size=23,
            ),
        )
        propriete1.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Retenons deux propriétés essentielles. D'abord : le "
                "point d'ébullition des alcanes linéaires augmente "
                "régulièrement avec le nombre n d'atomes de carbone, car "
                "la masse molaire augmente, et les interactions entre "
                "molécules, les forces de van der Waals, deviennent plus "
                "fortes."
            )
        ) as tracker:
            self.play(FadeIn(propriete1))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(propriete1))

        propriete2 = property_box(
            VGroup(
                Text(
                    _wrap(
                        "À formule brute égale, plus la chaîne est "
                        "ramifiée, plus le point d'ébullition est bas "
                        "(molécules plus compactes, qui s'attirent moins).",
                        width=44,
                    ),
                    font_size=22,
                ),
                MathTex(
                    r"C_5H_{12} : 36°C \; (\text{pentane}) > 28°C \; (\text{2-méthylbutane}) > 9{,}5°C \; (\text{2,2-diméthylpropane})",
                    font_size=18,
                ),
            ).arrange(DOWN, buff=0.3),
            box_width=12.0,
        )
        propriete2.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Ensuite : à formule brute égale, plus la chaîne est "
                "ramifiée, plus le point d'ébullition est bas. Exemple "
                "pour C-5, H-12 : le pentane bout à trente-six degrés, le "
                "deux-méthylbutane à vingt-huit degrés, et le "
                "deux-virgule-deux-diméthylpropane à seulement neuf "
                "virgule cinq degrés. Les molécules ramifiées, plus "
                "compactes, s'attirent moins fortement entre elles."
            )
        ) as tracker:
            self.play(FadeIn(propriete2))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(propriete2))

        # --- Piège à éviter : valeurs données à pression atmosphérique ---------
        piege = warning_box(
            Text(
                _wrap(
                    "Ces points d'ébullition sont donnés à pression "
                    "atmosphérique normale : ils changent avec l'altitude "
                    "ou la pression. Et la croissance du Téb avec n, bien "
                    "que régulière, n'est pas parfaitement linéaire : "
                    "l'écart entre alcanes voisins diminue peu à peu.",
                    width=48,
                ),
                font_size=22,
            ),
        )
        piege.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Attention : ces points d'ébullition sont donnés à "
                "pression atmosphérique normale, ils changeraient avec "
                "l'altitude ou la pression. Et si la croissance du point "
                "d'ébullition avec n est régulière, elle n'est pas "
                "parfaitement linéaire : l'écart entre deux alcanes "
                "voisins diminue peu à peu quand n augmente."
            )
        ) as tracker:
            self.play(FadeIn(piege))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(piege), FadeOut(titre))
