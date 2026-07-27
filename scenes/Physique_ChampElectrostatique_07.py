"""
scenes/Physique_ChampElectrostatique_07.py — Chapitre 6 « Champ
électrostatique » (1ereC, Physique), scène 07.

§ Champ électrostatique uniforme entre deux armatures : définition du
condensateur plan, expérience du spectre (lignes rectilignes, parallèles,
équidistantes), définition du champ uniforme (même direction/sens/norme
en tout point, dirigé de l'armature + vers l'armature -), propriété
(admise) E=U/d. Exemple résolu 4 : d=5cm, U=1000V → E=2×10⁴V/m, puis
calcul de U pour E=5×10⁴V/m et d=2cm → U=1000V.
Source : 1ereC/Physique.pdf, pages 54-65 (chapitre 6, § 5).
"""

import textwrap

from manim import (
    DOWN,
    LEFT,
    RIGHT,
    UP,
    WHITE,
    YELLOW,
    RED,
    BLUE,
    Arrow,
    Create,
    FadeIn,
    FadeOut,
    Line,
    MathTex,
    Rectangle,
    Text,
    VGroup,
    Write,
)

from shapes.base_scene import NotionScene
from shapes.boxes import definition_box, essentiel_box, example_box, property_box, scene_title, warning_box


def _wrap(text: str, width: int = 56) -> str:
    return "\n".join(textwrap.fill(line, width=width) for line in text.split("\n"))


class ChampUniformeArmatures(NotionScene):
    def construct(self):
        titre = scene_title("Champ électrostatique uniforme entre deux armatures")
        titre.scale(0.4)
        titre.to_edge(UP)

        # --- Énoncé : le condensateur plan --------------------------------------------
        armature_pos = Line(UP * 1.4 + LEFT * 1.8, UP * 1.4 + RIGHT * 1.8, color=RED, stroke_width=6)
        armature_pos_label = MathTex("+", font_size=30, color=RED).next_to(armature_pos, UP, buff=0.15)
        armature_neg = Line(DOWN * 1.4 + LEFT * 1.8, DOWN * 1.4 + RIGHT * 1.8, color=BLUE, stroke_width=6)
        armature_neg_label = MathTex("-", font_size=30, color=BLUE).next_to(armature_neg, DOWN, buff=0.15)
        d_ligne = Line(UP * 1.4 + RIGHT * 2.3, DOWN * 1.4 + RIGHT * 2.3, color=WHITE, stroke_width=1.5)
        d_label = MathTex("d", font_size=24).next_to(d_ligne, RIGHT, buff=0.15)
        schema = VGroup(armature_pos, armature_pos_label, armature_neg, armature_neg_label, d_ligne, d_label)
        schema.move_to(DOWN * 0.3)

        mise_en_situation = Text(
            _wrap(
                "Un condensateur plan est formé de deux plaques "
                "conductrices planes et parallèles, portant des charges "
                "opposées. Quel champ règne dans l'espace qui les sépare ?",
                width=52,
            ),
            font_size=20,
        )
        mise_en_situation.next_to(titre, DOWN, buff=0.35)
        schema.next_to(mise_en_situation, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Un condensateur plan est formé de deux plaques "
                "conductrices, planes et parallèles, appelées armatures, "
                "portant des charges électriques opposées, plus Q et "
                "moins Q, et séparées d'une distance d. Quel champ règne "
                "dans l'espace qui les sépare ?"
            )
        ) as tracker:
            self.play(Write(titre))
            self.play(FadeIn(mise_en_situation))
            self.play(Create(schema))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(mise_en_situation), FadeOut(schema))

        # --- Raisonnement : spectre entre les armatures -------------------------------
        armature_pos2 = Line(UP * 1.3 + LEFT * 2.2, UP * 1.3 + RIGHT * 2.2, color=RED, stroke_width=6)
        armature_neg2 = Line(DOWN * 1.3 + LEFT * 2.2, DOWN * 1.3 + RIGHT * 2.2, color=BLUE, stroke_width=6)
        lignes_champ = VGroup(*[
            Arrow(
                UP * 1.3 + RIGHT * x, DOWN * 1.3 + RIGHT * x,
                buff=0, color=YELLOW, stroke_width=2.5, max_tip_length_to_length_ratio=0.1,
            )
            for x in [-1.8, -1.0, -0.2, 0.6, 1.4]
        ])
        spectre = VGroup(armature_pos2, armature_neg2, lignes_champ)
        spectre.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Le spectre obtenu entre les deux armatures est très "
                "différent de celui d'une charge ponctuelle : les lignes "
                "de champ y sont rectilignes, parallèles entre elles, et "
                "régulièrement espacées, sauf tout près des bords. Cette "
                "régularité signale un champ dont l'intensité est "
                "identique partout."
            )
        ) as tracker:
            self.play(Create(spectre))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(spectre))

        # --- Définition : champ uniforme -----------------------------------------------
        definition = definition_box(
            VGroup(
                Text("Champ électrostatique uniforme", font_size=22, weight="BOLD"),
                Text("Champ ayant même direction, même sens et même norme", font_size=19),
                Text("en tout point de l'espace entre les armatures.", font_size=19),
                Text("Dirigé de l'armature (+) vers l'armature (-).", font_size=19),
            ).arrange(DOWN, buff=0.2),
            box_width=11.4,
        )
        definition.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "On appelle champ électrostatique uniforme un champ qui a "
                "même direction, même sens et même norme en tout point de "
                "l'espace considéré. Entre les armatures d'un "
                "condensateur plan, ce champ est dirigé de l'armature "
                "positive vers l'armature négative."
            )
        ) as tracker:
            self.play(FadeIn(definition))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(definition))

        # --- Propriété admise : E = U/d --------------------------------------------------
        propriete = property_box(
            VGroup(
                Text("Relation entre champ et tension (admise)", font_size=22, weight="BOLD"),
                MathTex(r"E = \dfrac{U}{d}", font_size=34),
                Text("U : tension entre les armatures (V), d : distance qui", font_size=19),
                Text("les sépare (m), E en V/m (équivalent au N/C).", font_size=19),
            ).arrange(DOWN, buff=0.22),
            box_width=11.0,
        )
        propriete.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "On admet la relation suivante entre le champ uniforme et "
                "la tension appliquée entre les armatures : E égale U sur "
                "d, où U est la tension entre les armatures en volts, et "
                "d la distance qui les sépare, en mètres. Le champ "
                "s'exprime alors en volts par mètre, unité équivalente au "
                "newton par coulomb."
            )
        ) as tracker:
            self.play(FadeIn(propriete))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(propriete))

        # --- Exemple résolu 4 : calcul de E puis de U --------------------------------
        exemple = example_box(
            VGroup(
                Text("d = 5 cm = 0,05 m, U = 1000 V", font_size=20),
                MathTex(r"E = \dfrac{U}{d} = \dfrac{1000}{0{,}05} = 2\times 10^{4}\ \text{V/m}", font_size=25, color=YELLOW),
                Text("Pour E = 5×10⁴ V/m et d = 2 cm = 0,02 m :", font_size=20),
                MathTex(r"U = E\times d = 5\times 10^4 \times 0{,}02 = 1000\ \text{V}", font_size=25, color=YELLOW),
            ).arrange(DOWN, buff=0.24),
            box_width=11.6,
        )
        exemple.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Exemple résolu : les armatures sont séparées de cinq "
                "centimètres, soit zéro virgule zéro cinq mètre, pour une "
                "tension de mille volts. Le champ vaut alors E égale U sur "
                "d, soit deux fois dix puissance quatre volts par mètre. "
                "Inversement, pour obtenir un champ de cinq fois dix "
                "puissance quatre volts par mètre avec des armatures "
                "séparées de deux centimètres, il faut une tension U égale "
                "E fois d, soit mille volts."
            )
        ) as tracker:
            self.play(FadeIn(exemple))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(exemple))

        # --- À retenir -----------------------------------------------------------------
        retenir = essentiel_box(
            VGroup(
                Text("À retenir", font_size=24, weight="BOLD"),
                MathTex(r"E = \dfrac{U}{d} \quad (U \text{ en V}, d \text{ en m}, E \text{ en V/m})", font_size=26),
                Text("Champ uniforme : dirigé de l'armature + vers l'armature -.", font_size=20),
            ).arrange(DOWN, buff=0.22),
            box_width=12.0,
        )
        retenir.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Retenons l'essentiel : entre les armatures d'un "
                "condensateur plan, le champ uniforme vaut E égale U sur "
                "d, avec la tension en volts et la distance en mètres. Il "
                "est dirigé de l'armature positive vers l'armature "
                "négative."
            )
        ) as tracker:
            self.play(FadeIn(retenir))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(retenir))

        # --- Piège à éviter -------------------------------------------------------------
        piege = warning_box(
            VGroup(
                Text("• Toujours convertir d en MÈTRES avant de calculer E", font_size=20),
                Text("   (une distance oubliée en cm fausse le résultat", font_size=20),
                Text("   d'un facteur 100).", font_size=20),
                Text("• Cette formule E = U/d ne vaut QUE pour un champ", font_size=20),
                Text("   UNIFORME (armatures planes parallèles), pas pour", font_size=20),
                Text("   le champ d'une charge ponctuelle.", font_size=20),
            ).arrange(DOWN, aligned_edge=LEFT, buff=0.16),
            box_width=12.0,
        )
        piege.next_to(titre, DOWN, buff=0.35)

        with self.voiceover(
            text=(
                "Deux pièges à éviter. D'abord, toujours convertir la "
                "distance d en mètres avant de calculer E, sous peine de "
                "fausser le résultat d'un facteur cent. Ensuite, cette "
                "formule E égale U sur d ne vaut que pour un champ "
                "uniforme, entre deux armatures planes et parallèles : "
                "elle ne s'applique pas au champ créé par une charge "
                "ponctuelle."
            )
        ) as tracker:
            self.play(FadeIn(piege))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(piege), FadeOut(titre))
