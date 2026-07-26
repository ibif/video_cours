"""
scenes/Chimie_AlcenesAlcynes_09.py — Chapitre 3 (1ereC, Chimie), scène 09.

Réactions d'addition sur les alcènes : définition générale, hydrogénation
catalytique (Ni/Pd → alcane, application à la fabrication de la margarine),
action des dihalogènes (Cl2, Br2 → dérivé dihalogéné vicinal), et mise en
garde : l'addition a lieu à l'obscurité, ce n'est pas une réaction
photochimique, contrairement à la substitution radicalaire des alcanes.
Source : 1ereC/Chimie.pdf, chapitre 3, pages 31-32.
"""

import textwrap

import numpy as np

from manim import (
    DOWN,
    LEFT,
    RIGHT,
    UP,
    WHITE,
    YELLOW,
    BLUE,
    GREEN,
    FadeIn,
    FadeOut,
    Dot,
    Line,
    MathTex,
    Text,
    VGroup,
    Write,
    config,
)

from shapes.base_scene import NotionScene
from shapes.boxes import definition_box, scene_title, warning_box


def _wrap(text: str, width: int = 56) -> str:
    return "\n".join(textwrap.fill(line, width=width) for line in text.split("\n"))


def _fit(mobject, top_y):
    bas_visible = -config.frame_height / 2 + 0.25
    hauteur_dispo = top_y - bas_visible
    if mobject.height > hauteur_dispo:
        mobject.scale(hauteur_dispo / mobject.height, about_point=mobject.get_top())
    return mobject


def _schema_addition(symbole_ajoute="X", couleur=GREEN):
    """Schéma générique : C=C qui devient C-C avec un groupe ajouté sur
    chaque carbone (principe de l'addition)."""
    c_g = np.array([-0.6, 0, 0])
    c_d = np.array([0.6, 0, 0])
    liaison_avant = VGroup(
        Line(c_g + UP * 0.05, c_d + UP * 0.05, color=WHITE, stroke_width=4),
        Line(c_g + DOWN * 0.05, c_d + DOWN * 0.05, color=WHITE, stroke_width=4),
    )
    labels_avant = VGroup(
        MathTex("C", font_size=26, color=WHITE).move_to(c_g),
        MathTex("C", font_size=26, color=WHITE).move_to(c_d),
    )
    avant = VGroup(liaison_avant, labels_avant)

    fleche = MathTex(r"\longrightarrow", font_size=34, color=YELLOW)

    c_g2 = np.array([-0.6, 0, 0])
    c_d2 = np.array([0.6, 0, 0])
    liaison_apres = Line(c_g2, c_d2, color=WHITE, stroke_width=4)
    ajout_g = c_g2 + UP * 0.8
    ajout_d = c_d2 + UP * 0.8
    liaisons_ajout = VGroup(
        Line(c_g2, ajout_g, color=couleur, stroke_width=3),
        Line(c_d2, ajout_d, color=couleur, stroke_width=3),
    )
    labels_apres = VGroup(
        MathTex("C", font_size=26, color=WHITE).move_to(c_g2),
        MathTex("C", font_size=26, color=WHITE).move_to(c_d2),
        MathTex(symbole_ajoute, font_size=24, color=couleur).move_to(ajout_g),
        MathTex(symbole_ajoute, font_size=24, color=couleur).move_to(ajout_d),
    )
    apres = VGroup(liaison_apres, liaisons_ajout, labels_apres)

    groupe = VGroup(avant, fleche, apres).arrange(RIGHT, buff=0.6)
    return groupe


class AdditionHydrogeneDihalogenes(NotionScene):
    def construct(self):
        titre = scene_title("9. Réactions d'addition sur les alcènes")
        titre.scale(0.5)
        titre.to_edge(UP)

        # --- Énoncé : définition de la réaction d'addition ------------------------
        definition = definition_box(
            Text(
                _wrap(
                    "Une réaction d'addition consiste en la rupture de la "
                    "double liaison C=C d'un alcène, chacun des deux "
                    "atomes de carbone fixant alors un nouvel atome ou "
                    "groupe d'atomes.",
                    width=48,
                ),
                font_size=25,
            ),
        )
        definition.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Une réaction d'addition consiste en la rupture de la "
                "double liaison carbone-carbone d'un alcène : chacun des "
                "deux atomes de carbone fixe alors un nouvel atome ou "
                "groupe d'atomes, et la molécule devient saturée."
            )
        ) as tracker:
            self.play(Write(titre))
            self.play(FadeIn(definition))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(definition))

        # --- Animation du raisonnement : hydrogénation catalytique --------------
        entete1 = Text("L'hydrogénation catalytique", font_size=24, color=YELLOW, weight="BOLD")
        entete1.next_to(titre, DOWN, buff=0.4)

        eq_hydro = MathTex(
            r"C_nH_{2n} + H_2 \xrightarrow{Ni \text{ ou } Pd} C_nH_{2n+2}",
            font_size=30,
        )
        eq_hydro.next_to(entete1, DOWN, buff=0.45)

        schema_hydro = _schema_addition("H", GREEN)
        schema_hydro.scale(0.8)
        schema_hydro.next_to(eq_hydro, DOWN, buff=0.5)

        groupe1 = VGroup(entete1, eq_hydro, schema_hydro)

        with self.voiceover(
            text=(
                "Premier exemple : l'hydrogénation. En présence d'un "
                "catalyseur métallique, nickel ou palladium, un alcène "
                "additionne du dihydrogène et se transforme en alcane. "
                "Cette réaction est très utilisée dans l'industrie "
                "agroalimentaire pour transformer des huiles végétales "
                "liquides, riches en doubles liaisons, en margarines "
                "solides."
            )
        ) as tracker:
            self.play(FadeIn(entete1))
            self.play(FadeIn(eq_hydro))
            self.play(FadeIn(schema_hydro))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(groupe1))

        # --- Exemple traité : action des dihalogènes ------------------------------
        entete2 = Text("Action des dihalogènes (Cl₂, Br₂)", font_size=24, color=YELLOW, weight="BOLD")
        entete2.next_to(titre, DOWN, buff=0.4)

        eq_br = MathTex(
            r"CH_2=CH_2 + Br_2 \longrightarrow CH_2Br-CH_2Br",
            font_size=28,
        )
        eq_br.next_to(entete2, DOWN, buff=0.45)

        label_vicinal = Text("dérivé dihalogéné vicinal (les 2 Br sur des C voisins)", font_size=19, color=WHITE)
        label_vicinal.next_to(eq_br, DOWN, buff=0.35)

        groupe2 = VGroup(entete2, eq_br, label_vicinal)

        with self.voiceover(
            text=(
                "Deuxième exemple : l'action des dihalogènes, comme le "
                "dichlore ou le dibrome. L'éthylène additionne du "
                "dibrome pour donner le un-deux-dibromoéthane. On "
                "obtient un dérivé dihalogéné dit vicinal, car les deux "
                "atomes de brome se fixent sur deux atomes de carbone "
                "voisins, ceux qui portaient la double liaison."
            )
        ) as tracker:
            self.play(FadeIn(entete2))
            self.play(FadeIn(eq_br))
            self.play(FadeIn(label_vicinal))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(groupe2))

        # --- À retenir : bilan des additions vues -----------------------------------
        retenir = definition_box(
            Text(
                _wrap(
                    "Dans toute réaction d'addition, l'insaturation "
                    "(double ou triple liaison) disparaît partiellement "
                    "ou totalement, et le nombre d'atomes fixés sur la "
                    "chaîne carbonée augmente.",
                    width=48,
                ),
                font_size=25,
            ),
        )
        retenir.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Retenons l'essentiel : dans toute réaction d'addition, "
                "l'insaturation de la molécule diminue ou disparaît, et "
                "le nombre d'atomes fixés sur la chaîne carbonée "
                "augmente. C'est l'inverse d'une élimination."
            )
        ) as tracker:
            self.play(FadeIn(retenir))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(retenir))

        # --- Pièges à éviter : addition à l'obscurité, pas photochimique --------
        piege = warning_box(
            Text(
                _wrap(
                    "Ne pas confondre : l'addition de Cl₂/Br₂ sur un "
                    "alcène se produit spontanément, même à l'obscurité "
                    "(pas besoin de lumière). C'est très différent de la "
                    "substitution radicalaire des alcanes, qui exige "
                    "elle une activation par la lumière ou la chaleur.",
                    width=48,
                ),
                font_size=22,
            ),
        )
        piege.next_to(titre, DOWN, buff=0.4)
        _fit(piege, titre.get_bottom()[1] - 0.4)

        with self.voiceover(
            text=(
                "Attention à un piège important : l'addition du dichlore "
                "ou du dibrome sur un alcène se produit spontanément, "
                "même à l'obscurité, sans besoin de lumière. C'est très "
                "différent de la substitution radicalaire des alcanes, "
                "qui exige au contraire une activation par la lumière ou "
                "par la chaleur. Ne confondez jamais ces deux mécanismes."
            )
        ) as tracker:
            self.play(FadeIn(piege))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(piege), FadeOut(titre))
