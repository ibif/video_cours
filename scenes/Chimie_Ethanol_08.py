"""
scenes/Chimie_Ethanol_08.py — Chapitre 7 « L'éthanol » (1ereC, Chimie),
scène 08.

§ 5. Le degré alcoolique d'une boisson. Définition du degré alcoolique
(d = Véthanol/Vboisson × 100), formule de calcul de la masse d'éthanol.
Tableau des degrés usuels (bière ≈5°, vin de palme 6-10°, vin de raisin
≈12°, eaux-de-vie 40-50°, alcool pharmaceutique 70°). Exemple résolu 5 :
verre de bière 25 cL à 5° (Véthanol=12,5 mL, m≈9,9 g).
Source : 1ereC/Chimie.pdf, chapitre 7, pages 72-73.
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
from shapes.boxes import definition_box, example_box, property_box, scene_title, warning_box


def _wrap(text: str, width: int = 56) -> str:
    return "\n".join(textwrap.fill(line, width=width) for line in text.split("\n"))


def _fit(mobject, top_y):
    bas_visible = -config.frame_height / 2 + 0.25
    hauteur_dispo = top_y - bas_visible
    if mobject.height > hauteur_dispo:
        mobject.scale(hauteur_dispo / mobject.height, about_point=mobject.get_top())
    return mobject


class DegreAlcooliqueBoisson(NotionScene):
    def construct(self):
        titre = scene_title("7.5 Le degré alcoolique d'une boisson")
        titre.scale(0.55)
        titre.to_edge(UP)

        # --- Énoncé : définition du degré alcoolique ------------------------------
        def_degre = definition_box(
            VGroup(
                Text(
                    _wrap(
                        "Le degré alcoolique (ou titre alcoométrique "
                        "volumique) d'une boisson, noté d et exprimé en "
                        "degrés (°), est le volume d'éthanol pur, en mL, "
                        "contenu dans 100 mL de boisson (mesuré à 20°C).",
                        width=48,
                    ),
                    font_size=21,
                ),
                MathTex(r"d = \dfrac{V_{\text{éthanol}}}{V_{\text{boisson}}}\times 100 \iff V_{\text{éthanol}} = \dfrac{d\times V_{\text{boisson}}}{100}", font_size=24, color="#1A1A1A"),
            ).arrange(DOWN, buff=0.3),
            box_width=12.2,
        )
        def_degre.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Le degré alcoolique, ou titre alcoométrique volumique, "
                "d'une boisson, noté d et exprimé en degrés, est le "
                "volume d'éthanol pur, exprimé en millilitres, contenu "
                "dans cent millilitres de boisson, mesuré à vingt "
                "degrés. Formule : d égale V éthanol sur V boisson, fois "
                "cent, ce qui équivaut à V éthanol égale d fois V "
                "boisson, sur cent."
            )
        ) as tracker:
            self.play(Write(titre))
            self.play(FadeIn(def_degre))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(def_degre))

        formule_masse = MathTex(
            r"m_{\text{éthanol}} = \rho\times V_{\text{éthanol}} \quad (\rho = 0{,}789\ \text{g/mL})",
            font_size=28, color=WHITE,
        )
        formule_masse.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "La masse d'éthanol correspondante s'obtient ensuite avec "
                "la formule habituelle : m égale rho fois V éthanol, avec "
                "rho égale zéro virgule sept-cent-quatre-vingt-neuf "
                "gramme par millilitre."
            )
        ) as tracker:
            self.play(Write(formule_masse))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(formule_masse))

        # --- Raisonnement : tableau des degrés usuels ------------------------------
        entete_tab = Text("Degrés alcooliques usuels", font_size=22, color=YELLOW, weight="BOLD")
        entete_tab.next_to(titre, DOWN, buff=0.35)

        rows = [
            ["Bière (tchapalo, industrielle)", "≈ 5°"],
            ["Vin de palme (bangui)", "6 à 10°"],
            ["Vin de raisin", "≈ 12°"],
            ["Eaux-de-vie (koutoukou, whisky)", "40 à 50°"],
            ["Alcool pharmaceutique", "70°"],
        ]
        table = Table(
            rows,
            col_labels=[Text(c, font_size=15, weight="BOLD") for c in ["Boisson", "Degré alcoolique usuel"]],
            element_to_mobject=Text,
            element_to_mobject_config={"font_size": 14},
            line_config={"color": WHITE, "stroke_width": 1},
            include_outer_lines=True,
            v_buff=0.2,
            h_buff=0.3,
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
                "Voici quelques degrés alcooliques usuels. La bière, "
                "tchapalo ou bière industrielle, titre environ cinq "
                "degrés. Le vin de palme, ou bangui, titre de six à dix "
                "degrés. Le vin de raisin titre environ douze degrés. Les "
                "eaux-de-vie, comme le koutoukou ou le whisky, titrent de "
                "quarante à cinquante degrés. Enfin, l'alcool "
                "pharmaceutique, utilisé comme désinfectant, titre "
                "soixante-dix degrés."
            )
        ) as tracker:
            self.play(FadeIn(entete_tab))
            self.play(FadeIn(table))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(entete_tab), FadeOut(table))

        # --- Exemple résolu 5 : un verre de bière ----------------------------------
        exemple5 = example_box(
            VGroup(
                Text("Exemple résolu 5 — Un verre de bière (V = 25 cL à 5°)", font_size=20, weight="BOLD"),
                MathTex(r"V_{\text{éthanol}} = \dfrac{5\times 250}{100} = 12{,}5\ \text{mL}", font_size=26, color="#1A1A1A"),
                MathTex(r"m_{\text{éthanol}} = 0{,}789\times 12{,}5 \approx 9{,}9\ \text{g}", font_size=26, color="#1A1A1A"),
            ).arrange(DOWN, buff=0.3, aligned_edge=LEFT),
            box_width=11.8,
        )
        exemple5.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Exemple résolu cinq : un verre contient vingt-cinq "
                "centilitres de bière à cinq degrés. Le volume d'éthanol "
                "pur absorbé vaut cinq fois deux cent cinquante, sur "
                "cent, soit douze virgule cinq millilitres. La masse "
                "d'éthanol correspondante vaut zéro virgule sept-cent-"
                "quatre-vingt-neuf fois douze virgule cinq, soit environ "
                "neuf virgule neuf grammes."
            )
        ) as tracker:
            self.play(FadeIn(exemple5))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(exemple5))

        # --- À retenir : fiche récapitulative ---------------------------------------
        propriete = property_box(
            VGroup(
                MathTex(r"d = \dfrac{V_{\text{éthanol}}}{V_{\text{boisson}}}\times 100", font_size=28, color="#1A1A1A"),
                Text("m = ρ × Véthanol, avec ρ = 0,789 g/mL", font_size=21),
            ).arrange(DOWN, buff=0.3),
        )
        propriete.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Retenons l'essentiel : le degré alcoolique est le volume "
                "d'éthanol pur pour cent millilitres de boisson, d égale "
                "V éthanol sur V boisson, fois cent. La masse d'éthanol "
                "s'obtient ensuite avec m égale rho fois V éthanol, où "
                "rho vaut zéro virgule sept-cent-quatre-vingt-neuf gramme "
                "par millilitre."
            )
        ) as tracker:
            self.play(FadeIn(propriete))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(propriete))

        # --- Piège à éviter : ne pas confondre les deux volumes -------------------
        piege = warning_box(
            Text(
                _wrap(
                    "Dans un calcul de degré alcoolique, bien distinguer "
                    "le volume de boisson (donné dans l'énoncé, ex. 25 cL) "
                    "du volume d'éthanol pur (à calculer) : les intervertir "
                    "dans la formule fausse tout le résultat.",
                    width=48,
                ),
                font_size=21,
            ),
        )
        piege.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Attention à un piège fréquent : dans un calcul de degré "
                "alcoolique, il faut bien distinguer le volume de "
                "boisson, donné dans l'énoncé, du volume d'éthanol pur, "
                "qui lui doit être calculé. Intervertir ces deux volumes "
                "dans la formule fausse complètement le résultat."
            )
        ) as tracker:
            self.play(FadeIn(piege))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(piege), FadeOut(titre))
