"""
scenes/Chimie_Ethanol_07.py — Chapitre 7 « L'éthanol » (1ereC, Chimie),
scène 07.

§ 4.2 (suite) Autres voies d'oxydation de l'éthanol + tableau de synthèse.
Déshydrogénation catalytique (CH₃-CH₂-OH → CH₃-CHO + H₂, sans O₂),
oxydation par KMnO₄ acide (décoloration violet → incolore). Tableau
récapitulatif classe d'alcool → produit d'oxydation (primaire / secondaire
/ tertiaire), chaîne complète éthanol → éthanal → acide éthanoïque.
Application quotidienne (vin qui s'aigrit en vinaigre, bactérie
Acetobacter).
Source : 1ereC/Chimie.pdf, chapitre 7, page 72.
"""

import textwrap

from manim import (
    DOWN,
    LEFT,
    RIGHT,
    UP,
    WHITE,
    YELLOW,
    PURPLE,
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


class AutresVoiesOxydationSynthese(NotionScene):
    def construct(self):
        titre = scene_title("7.4 Autres voies d'oxydation et tableau de synthèse")
        titre.scale(0.46)
        titre.to_edge(UP)

        # --- Énoncé : d'autres façons d'oxyder l'éthanol -------------------------
        intro = Text(
            _wrap(
                "La lampe sans flamme n'est pas le seul moyen d'oxyder "
                "l'éthanol : deux autres méthodes sont couramment "
                "utilisées en laboratoire.",
                width=54,
            ),
            font_size=24,
            color=WHITE,
        )
        intro.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "La lampe sans flamme n'est pas le seul moyen d'oxyder "
                "l'éthanol : deux autres méthodes sont couramment "
                "utilisées en laboratoire. Voyons-les, puis dressons un "
                "tableau de synthèse."
            )
        ) as tracker:
            self.play(Write(titre))
            self.play(FadeIn(intro))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(intro))

        # --- Raisonnement : déshydrogénation + KMnO4 -----------------------------
        entete_deshydro = Text("a) Déshydrogénation catalytique (sans O₂)", font_size=21, color=YELLOW, weight="BOLD")
        entete_deshydro.next_to(titre, DOWN, buff=0.4)

        eq_deshydro = MathTex(r"CH_3{-}CH_2{-}OH \xrightarrow{Cu,\ 300°C} CH_3{-}CHO + H_2", font_size=27, color=WHITE)
        eq_deshydro.next_to(entete_deshydro, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Chauffé vers trois cents degrés en présence de cuivre, "
                "mais sans dioxygène cette fois, l'éthanol perd deux "
                "atomes d'hydrogène : on parle de déshydrogénation. Il se "
                "transforme directement en éthanal : C-H-3 tiret C-H-2 "
                "tiret O-H donne C-H-3 tiret C-H-O, plus H-2."
            )
        ) as tracker:
            self.play(FadeIn(entete_deshydro))
            self.play(Write(eq_deshydro))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(entete_deshydro), FadeOut(eq_deshydro))

        entete_kmno4 = Text("b) Oxydation par le permanganate de potassium (KMnO₄) en milieu acide", font_size=18, color=YELLOW, weight="BOLD")
        entete_kmno4.next_to(titre, DOWN, buff=0.4)

        kmno4_texte = Text(
            _wrap(
                "La solution violette de KMnO₄ contient les ions "
                "permanganate MnO₄⁻. En milieu acide, ils oxydent "
                "l'éthanol : on observe une décoloration, du violet vers "
                "l'incolore (formation d'ions Mn²⁺ incolores). On obtient "
                "l'éthanal, puis l'acide éthanoïque si MnO₄⁻ est en "
                "excès.",
                width=52,
            ),
            font_size=20,
            color=WHITE,
        )
        kmno4_texte.next_to(entete_kmno4, DOWN, buff=0.35)

        pastille_violette = MathTex(r"\text{violet (MnO}_4^-\text{)} \;\longrightarrow\; \text{incolore (Mn}^{2+}\text{)}", font_size=24, color=PURPLE)
        pastille_violette.next_to(kmno4_texte, DOWN, buff=0.35)

        with self.voiceover(
            text=(
                "La solution violette de permanganate de potassium "
                "contient les ions permanganate, M-n-O-4 moins. En milieu "
                "acide, en présence d'acide sulfurique, ces ions oxydent "
                "l'éthanol : on observe une décoloration de la solution, "
                "qui passe du violet à l'incolore, avec formation d'ions "
                "manganèse deux plus, incolores. On obtient de l'éthanal, "
                "puis de l'acide éthanoïque si les ions permanganate sont "
                "en excès."
            )
        ) as tracker:
            self.play(FadeIn(entete_kmno4))
            self.play(FadeIn(kmno4_texte))
            self.play(Write(pastille_violette))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(entete_kmno4), FadeOut(kmno4_texte), FadeOut(pastille_violette))

        # --- Exemple traité : tableau récapitulatif classe → oxydation ----------
        entete_tab = Text("Le produit d'oxydation dépend de la classe de l'alcool", font_size=19, color=YELLOW, weight="BOLD")
        entete_tab.next_to(titre, DOWN, buff=0.35)

        rows = [
            ["Primaire\nR-CH₂-OH", "Aldéhyde\nR-CHO", "Acide carboxylique\nR-COOH"],
            ["Secondaire\nR-CH(OH)-R'", "Cétone\nR-CO-R'", "pas d'oxydation\nsupplémentaire"],
            ["Tertiaire", "pas d'oxydation ménagée", "—"],
        ]
        col_labels = ["Classe de l'alcool", "1ère étape", "2ème étape (excès)"]
        table = Table(
            rows,
            col_labels=[Text(c, font_size=14, weight="BOLD") for c in col_labels],
            element_to_mobject=Text,
            element_to_mobject_config={"font_size": 13, "line_spacing": 0.8},
            line_config={"color": WHITE, "stroke_width": 1},
            include_outer_lines=True,
            v_buff=0.22,
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
                "Le produit de l'oxydation ménagée d'un alcool dépend de "
                "sa classe. Un alcool primaire, R tiret C-H-2 tiret O-H, "
                "donne d'abord un aldéhyde, R tiret C-H-O, puis un acide "
                "carboxylique, R tiret C-O-O-H, si l'oxydant est en "
                "excès. Un alcool secondaire donne une cétone, R tiret "
                "C-O tiret R prime, sans oxydation supplémentaire "
                "possible. Un alcool tertiaire, lui, ne subit aucune "
                "oxydation ménagée."
            )
        ) as tracker:
            self.play(FadeIn(entete_tab))
            self.play(FadeIn(table))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(entete_tab), FadeOut(table))

        chaine = MathTex(
            r"CH_3{-}CH_2{-}OH \;\longrightarrow\; CH_3{-}CHO \;\longrightarrow\; CH_3{-}COOH",
            font_size=27, color=WHITE,
        )
        chaine.next_to(titre, DOWN, buff=0.6)

        legende_chaine = Text("éthanol → éthanal → acide éthanoïque (alcool primaire)", font_size=18, color=YELLOW)
        legende_chaine.next_to(chaine, DOWN, buff=0.35)

        with self.voiceover(
            text=(
                "L'éthanol, alcool primaire, suit donc la chaîne "
                "d'oxydation complète : C-H-3 tiret C-H-2 tiret O-H, "
                "donne C-H-3 tiret C-H-O, donne C-H-3 tiret C-O-O-H, "
                "c'est-à-dire éthanol, puis éthanal, puis acide "
                "éthanoïque."
            )
        ) as tracker:
            self.play(Write(chaine))
            self.play(FadeIn(legende_chaine))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(chaine), FadeOut(legende_chaine))

        # --- À retenir : application quotidienne (le vin qui s'aigrit) ----------
        propriete = property_box(
            Text(
                _wrap(
                    "Application quotidienne : une bouteille de vin "
                    "laissée à l'air libre s'aigrit — l'éthanol s'oxyde en "
                    "acide éthanoïque (le vinaigre) sous l'action du "
                    "dioxygène de l'air et de bactéries du genre "
                    "Acetobacter. C'est la fabrication traditionnelle du "
                    "vinaigre.",
                    width=50,
                ),
                font_size=20,
            ),
            box_width=12.4,
        )
        propriete.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Une application très concrète de cette chimie : une "
                "bouteille de vin laissée ouverte à l'air libre s'aigrit "
                "avec le temps. L'éthanol qu'elle contient s'oxyde "
                "progressivement en acide éthanoïque, c'est-à-dire en "
                "vinaigre, sous l'action du dioxygène de l'air et de "
                "bactéries du genre Acetobacter. C'est exactement le "
                "principe de la fabrication traditionnelle du vinaigre."
            )
        ) as tracker:
            self.play(FadeIn(propriete))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(propriete))

        # --- Piège à éviter : un alcool tertiaire ne s'oxyde pas ------------------
        piege = warning_box(
            Text(
                _wrap(
                    "Un alcool tertiaire ne subit PAS d'oxydation ménagée. "
                    "Avant de prédire un produit d'oxydation, toujours "
                    "identifier d'abord la classe de l'alcool à partir de "
                    "sa formule semi-développée.",
                    width=48,
                ),
                font_size=21,
            ),
        )
        piege.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Piège à éviter : un alcool tertiaire ne subit pas "
                "d'oxydation ménagée, quelles que soient les conditions. "
                "Avant de prédire un produit d'oxydation, il faut donc "
                "toujours commencer par identifier la classe de l'alcool "
                "à partir de sa formule semi-développée."
            )
        ) as tracker:
            self.play(FadeIn(piege))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(piege), FadeOut(titre))
