"""
scenes/Chimie_Alcanes_02.py — Chapitre 2 « Hydrocarbures saturés — les
alcanes » (1ereC, Chimie), scène 02.

§ 2. Structure des alcanes : le méthane (4 liaisons C–H, structure
tétraédrique, angle 109°28', longueur de liaison 109 pm) et l'éthane
(C₂H₆ / CH₃–CH₃, longueur de liaison C–C 154 pm, libre rotation autour
de la liaison simple). Source : 1ereC/Chimie.pdf, pages 15-16.
"""

import textwrap

import numpy as np
from manim import (
    BLUE,
    DOWN,
    LEFT,
    ORANGE,
    RIGHT,
    UP,
    WHITE,
    YELLOW,
    Dot,
    FadeIn,
    FadeOut,
    Line,
    MathTex,
    Rotate,
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


def _tetraedre_methane():
    """Représentation de Cram simplifiée du méthane : C central, 4 liaisons
    vers les H (2 dans le plan, 1 en avant en trait plein épais, 1 en
    arrière en tirets), avec l'angle 109°28' indiqué entre deux liaisons."""
    centre = Dot(point=[0, 0, 0], color=BLUE, radius=0.09)
    label_c = MathTex("C", font_size=30, color=BLUE)
    label_c.next_to(centre, DOWN, buff=0.12)

    # positions approximatives des 4 sommets du tétraèdre (projection 2D)
    p_haut_gauche = np.array([-1.1, 0.9, 0])
    p_haut_droite = np.array([1.1, 0.9, 0])
    p_avant = np.array([0.0, -0.9, 0])   # liaison en avant du plan (trait plein épais)
    p_arriere = np.array([0.0, 1.3, 0])  # liaison en arrière du plan (tirets)

    liaison1 = Line(centre.get_center(), p_haut_gauche, color=WHITE, stroke_width=3)
    liaison2 = Line(centre.get_center(), p_haut_droite, color=WHITE, stroke_width=3)
    liaison3 = Line(centre.get_center(), p_avant, color=WHITE, stroke_width=6)
    liaison4 = Line(centre.get_center(), p_arriere, color=WHITE, stroke_width=2)
    liaison4.set_stroke(opacity=0.6)

    h1 = MathTex("H", font_size=26, color=WHITE).next_to(p_haut_gauche, UP + LEFT, buff=0.05)
    h2 = MathTex("H", font_size=26, color=WHITE).next_to(p_haut_droite, UP + RIGHT, buff=0.05)
    h3 = MathTex("H", font_size=26, color=WHITE).next_to(p_avant, DOWN, buff=0.1)
    h4 = MathTex("H", font_size=26, color=WHITE).next_to(p_arriere, UP, buff=0.1)

    angle_label = MathTex(r"109°28'", font_size=20, color=YELLOW)
    angle_label.move_to([0.75, 0.35, 0])

    return VGroup(
        liaison1, liaison2, liaison3, liaison4,
        centre, label_c, h1, h2, h3, h4, angle_label,
    )


class StructureMethaneEthane(NotionScene):
    def construct(self):
        titre = scene_title("2. Structure des alcanes : méthane et éthane")
        titre.scale(0.55)
        titre.to_edge(UP)

        # --- Énoncé : le méthane, formule CH₄ ----------------------------------
        intro = MathTex(r"CH_4", font_size=44, color=WHITE)
        intro.next_to(titre, DOWN, buff=0.5)
        sous_titre = Text("le plus simple des alcanes", font_size=22, color=YELLOW)
        sous_titre.next_to(intro, DOWN, buff=0.3)

        with self.voiceover(
            text=(
                "Le méthane, de formule brute C-H-4, est le plus simple des "
                "alcanes. L'atome de carbone y établit quatre liaisons de "
                "covalence avec quatre atomes d'hydrogène. Comment ces "
                "quatre liaisons s'organisent-elles dans l'espace ?"
            )
        ) as tracker:
            self.play(Write(titre))
            self.play(Write(intro))
            self.play(FadeIn(sous_titre))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(intro), FadeOut(sous_titre))

        # --- Raisonnement : structure tétraédrique (figure de Cram) ------------
        entete_tetra = Text("Structure tétraédrique (représentation de Cram)", font_size=22, color=YELLOW, weight="BOLD")
        entete_tetra.next_to(titre, DOWN, buff=0.4)

        tetra = _tetraedre_methane()
        tetra.scale(1.1)
        tetra.next_to(entete_tetra, DOWN, buff=0.6)

        with self.voiceover(
            text=(
                "Ces quatre liaisons se dirigent vers les sommets d'un "
                "tétraèdre régulier dont le carbone occupe le centre : on "
                "dit que le carbone a une structure tétraédrique, ou "
                "tétragonale. Sur cette représentation de Cram, deux "
                "liaisons sont dans le plan de la feuille, une liaison "
                "pointe vers l'avant, en trait épais, et une liaison "
                "pointe vers l'arrière, en tirets."
            )
        ) as tracker:
            self.play(FadeIn(entete_tetra))
            self.play(FadeIn(tetra))
            self.wait(tracker.get_remaining_duration())

        caracteristiques = VGroup(
            MathTex(r"\ell(C\text{-}H) = 109\ \text{pm}", font_size=26, color=WHITE),
            MathTex(r"\widehat{HCH} = 109°28' \approx 109{,}5°", font_size=26, color=WHITE),
        ).arrange(DOWN, buff=0.3)
        caracteristiques.next_to(tetra, RIGHT, buff=1.1)
        _fit(VGroup(entete_tetra, tetra, caracteristiques), entete_tetra.get_bottom()[1] - 0.4)

        with self.voiceover(
            text=(
                "Deux grandeurs caractérisent cette géométrie : la longueur "
                "de la liaison carbone-hydrogène, qui vaut cent neuf "
                "picomètres, un picomètre valant dix puissance moins douze "
                "mètre, et l'angle de liaison H-C-H, qui vaut cent neuf "
                "degrés vingt-huit minutes, soit environ cent neuf virgule "
                "cinq degrés."
            )
        ) as tracker:
            self.play(Write(caracteristiques))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(entete_tetra), FadeOut(tetra), FadeOut(caracteristiques))

        # --- Exemple traité : l'éthane et la libre rotation ---------------------
        entete_ethane = Text("L'éthane : C₂H₆", font_size=25, color=YELLOW, weight="BOLD")
        entete_ethane.next_to(titre, DOWN, buff=0.4)

        formule_ethane = MathTex(r"C_2H_6 \; : \; CH_3-CH_3", font_size=32, color=WHITE)
        formule_ethane.next_to(entete_ethane, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "L'éthane a pour formule brute C-2, H-6, et pour formule "
                "semi-développée C-H-3 tiret C-H-3. Ses deux atomes de "
                "carbone sont eux aussi tétraédriques."
            )
        ) as tracker:
            self.play(FadeIn(entete_ethane))
            self.play(Write(formule_ethane))
            self.wait(tracker.get_remaining_duration())

        # petit schéma : deux tétraèdres (groupes méthyle) reliés par une
        # liaison C-C, avec une flèche circulaire pour la libre rotation
        c_gauche = Dot(point=[-1.0, 0, 0], color=BLUE, radius=0.09)
        c_droite = Dot(point=[1.0, 0, 0], color=BLUE, radius=0.09)
        liaison_cc = Line(c_gauche.get_center(), c_droite.get_center(), color=WHITE, stroke_width=5)
        label_cc = MathTex(r"\ell(C\text{-}C) = 154\ \text{pm}", font_size=24, color=YELLOW)
        label_cc.next_to(liaison_cc, DOWN, buff=0.3)

        h_gauche = VGroup(*[
            Line(c_gauche.get_center(), c_gauche.get_center() + d, color=WHITE, stroke_width=3)
            for d in [np.array([-0.6, 0.5, 0]), np.array([-0.6, -0.5, 0]), np.array([-0.75, 0, 0])]
        ])
        h_droite = VGroup(*[
            Line(c_droite.get_center(), c_droite.get_center() + d, color=WHITE, stroke_width=3)
            for d in [np.array([0.6, 0.5, 0]), np.array([0.6, -0.5, 0]), np.array([0.75, 0, 0])]
        ])

        molecule_ethane = VGroup(h_gauche, h_droite, liaison_cc, c_gauche, c_droite)
        molecule_ethane.next_to(formule_ethane, DOWN, buff=0.7)
        label_cc.next_to(molecule_ethane, DOWN, buff=0.3)

        schema_complet = VGroup(molecule_ethane, label_cc)

        with self.voiceover(
            text=(
                "La longueur de la liaison carbone-carbone vaut environ "
                "cent cinquante-quatre picomètres, un peu plus longue que "
                "la liaison carbone-hydrogène. Les deux groupes méthyle "
                "peuvent tourner librement l'un par rapport à l'autre "
                "autour de l'axe de cette liaison : c'est la libre "
                "rotation autour d'une liaison simple."
            )
        ) as tracker:
            self.play(FadeIn(molecule_ethane))
            self.play(Write(label_cc))
            self.play(Rotate(h_droite, angle=2 * np.pi, about_point=c_droite.get_center(), run_time=2))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(entete_ethane), FadeOut(formule_ethane), FadeOut(schema_complet))

        # --- À retenir : propriété de géométrie ---------------------------------
        propriete = property_box(
            VGroup(
                Text("Méthane CH₄ : tétraédrique, ĤCH = 109°28', ℓ(C–H) = 109 pm", font_size=22),
                Text("Éthane C₂H₆ : ℓ(C–C) = 154 pm, libre rotation autour de C–C", font_size=22),
            ).arrange(DOWN, buff=0.3, aligned_edge=LEFT),
        )
        propriete.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Retenons l'essentiel : dans le méthane, le carbone est "
                "tétraédrique, avec un angle H-C-H de cent neuf degrés "
                "vingt-huit minutes et une liaison C-H de cent neuf "
                "picomètres. Dans l'éthane, la liaison carbone-carbone "
                "mesure cent cinquante-quatre picomètres, et les deux "
                "groupes méthyle tournent librement l'un par rapport à "
                "l'autre."
            )
        ) as tracker:
            self.play(FadeIn(propriete))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(propriete))

        # --- Piège à éviter : une représentation plane reste une projection ----
        piege = warning_box(
            Text(
                _wrap(
                    "La figure de Cram, dessinée à plat, n'est qu'une "
                    "projection : dans la réalité, les quatre liaisons du "
                    "carbone pointent vers les sommets d'un vrai tétraèdre "
                    "en trois dimensions, jamais dans un même plan.",
                    width=48,
                ),
                font_size=23,
            ),
        )
        piege.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Attention : la figure de Cram, dessinée à plat sur une "
                "feuille, n'est qu'une projection. Dans la réalité, les "
                "quatre liaisons du carbone pointent vers les sommets d'un "
                "véritable tétraèdre en trois dimensions, et ne sont "
                "jamais toutes dans un même plan."
            )
        ) as tracker:
            self.play(FadeIn(piege))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(piege), FadeOut(titre))
