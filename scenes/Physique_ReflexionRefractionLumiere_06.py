"""
scenes/Physique_ReflexionRefractionLumiere_06.py — Chapitre « Réflexion et
réfraction de la lumière blanche » (1ereC, Physique), scène 06.

§ Réflexion totale et angle limite : établissement du phénomène (n1>n2,
sin i2 peut dépasser 1), définition de la réflexion totale, définition de
l'angle limite λ (sin λ = n2/n1), théorème des conditions de la réflexion
totale (n1>n2 ET i1>λ), exemple résolu (eau→air, diamant→air).
Source : 1ereC/Physique.pdf, pages 117-129.
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
    GREY,
    RED,
    Create,
    DashedLine,
    Dot,
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
from shapes.boxes import definition_box, essentiel_box, example_box, theorem_box, scene_title, warning_box


def _wrap(text: str, width: int = 56) -> str:
    return "\n".join(textwrap.fill(line, width=width) for line in text.split("\n"))


def _dioptre_base(center, surf_half=2.2):
    milieu1 = Rectangle(width=2 * surf_half, height=1.6, fill_color=BLUE, fill_opacity=0.18, stroke_width=0).move_to(center + UP * 0.8)
    milieu2 = Rectangle(width=2 * surf_half, height=1.6, fill_color=BLUE, fill_opacity=0.05, stroke_width=0).move_to(center + DOWN * 0.8)
    dioptre = Line(center + LEFT * surf_half, center + RIGHT * surf_half, color=GREY, stroke_width=4)
    normale = DashedLine(center + DOWN * 1.4, center + UP * 1.7, color=WHITE, stroke_width=2)
    return VGroup(milieu1, milieu2, dioptre, normale)


class ReflexionTotaleAngleLimite(NotionScene):
    def construct(self):
        titre = scene_title("Réflexion totale et angle limite")
        titre.scale(0.5)
        titre.to_edge(UP)

        # --- Énoncé : que se passe-t-il quand n1 > n2 et i1 augmente ? -------------
        mise_en_situation = Text(
            _wrap(
                "Une lampe est immergée dans une piscine et éclaire vers "
                "la surface avec un angle d'incidence de plus en plus "
                "grand (n1 = eau > n2 = air). Que devient le rayon "
                "réfracté quand i1 devient trop grand ?",
                width=48,
            ),
            font_size=20,
        )
        mise_en_situation.next_to(titre, DOWN, buff=0.35)

        with self.voiceover(
            text=(
                "Une lampe est immergée dans une piscine, et éclaire vers "
                "la surface avec un angle d'incidence de plus en plus "
                "grand, l'eau étant plus réfringente que l'air. Que "
                "devient le rayon réfracté quand i1 devient trop grand ?"
            )
        ) as tracker:
            self.play(Write(titre))
            self.play(FadeIn(mise_en_situation))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(mise_en_situation))

        # --- Raisonnement : sin i2 peut dépasser 1 ------------------------------------
        base = _dioptre_base(LEFT * 3.0 + DOWN * 0.2)
        I = LEFT * 3.0 + DOWN * 0.2
        i1v = np.radians(55)
        S = I + 1.7 * np.array([-np.sin(i1v), np.cos(i1v), 0])
        rayon_inc = Line(S, I, color=YELLOW, stroke_width=4)
        # sin i2 = (n1/n2) sin i1 > 1 : pas de rayon réfracté, tout est réfléchi.
        i1p = i1v
        R = I + 1.7 * np.array([np.sin(i1p), np.cos(i1p), 0])
        rayon_reflechi = Line(I, R, color=RED, stroke_width=4)
        point_I = Dot(I, color=WHITE, radius=0.06)
        schema1 = VGroup(base, rayon_inc, rayon_reflechi, point_I)

        formule = MathTex(
            r"\sin i_2 = \dfrac{n_1}{n_2} \sin i_1 \quad \text{avec } n_1 > n_2",
            font_size=26,
        )
        consequence = MathTex(
            r"\text{si } i_1 \text{ est assez grand : } \dfrac{n_1}{n_2}\sin i_1 > 1 \Rightarrow \text{PAS de solution pour } i_2",
            font_size=22, color=RED,
        )
        texte_groupe = VGroup(formule, consequence).arrange(DOWN, buff=0.3)
        texte_groupe.next_to(schema1, RIGHT, buff=0.7)

        with self.voiceover(
            text=(
                "Reprenons la loi de Snell-Descartes : sinus de i2 est "
                "égal à n1 sur n2, fois sinus de i1, avec n1 supérieur à "
                "n2 puisque l'eau est plus réfringente que l'air. Or un "
                "sinus ne peut jamais dépasser un. Si i1 devient assez "
                "grand, le membre de droite dépasse un, et il n'existe "
                "alors plus aucune solution pour i2 : il n'y a plus de "
                "rayon réfracté du tout. Toute la lumière repart dans "
                "l'eau, réfléchie."
            )
        ) as tracker:
            self.play(Create(schema1))
            self.play(Write(texte_groupe))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(schema1), FadeOut(texte_groupe))

        # --- Définition : réflexion totale et angle limite ----------------------------
        definition = definition_box(
            VGroup(
                Text("Réflexion totale et angle limite", font_size=22, weight="BOLD"),
                Text("Réflexion totale : toute la lumière incidente est réfléchie,", font_size=20),
                Text("sans aucun rayon réfracté.", font_size=20),
                Text("Angle limite λ : angle d'incidence pour lequel le rayon", font_size=20),
                Text("réfracté devient rasant (i2 = 90°).", font_size=20),
                MathTex(r"\sin \lambda = \dfrac{n_2}{n_1}", font_size=28, color=YELLOW),
            ).arrange(DOWN, aligned_edge=LEFT, buff=0.18),
            box_width=11.8,
        )
        definition.next_to(titre, DOWN, buff=0.3)

        with self.voiceover(
            text=(
                "On définit ainsi la réflexion totale : c'est le "
                "phénomène par lequel toute la lumière incidente est "
                "réfléchie, sans aucun rayon réfracté. Le seuil exact à "
                "partir duquel cela se produit est appelé l'angle limite, "
                "noté lambda : c'est l'angle d'incidence pour lequel le "
                "rayon réfracté devient rasant, c'est-à-dire pour lequel "
                "i2 vaut exactement quatre-vingt-dix degrés. En posant "
                "i2 égal quatre-vingt-dix degrés dans la loi de "
                "Snell-Descartes, on obtient sinus de lambda égal n2 sur "
                "n1."
            )
        ) as tracker:
            self.play(FadeIn(definition))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(definition))

        # --- Théorème : conditions de la réflexion totale ------------------------------
        theoreme = theorem_box(
            VGroup(
                Text("Conditions de la réflexion totale", font_size=22, weight="BOLD"),
                Text("Il y a réflexion totale si, et seulement si :", font_size=20),
                MathTex(r"n_1 > n_2 \quad \text{ET} \quad i_1 > \lambda", font_size=28, color=YELLOW),
                Text("(le rayon doit partir d'un milieu plus réfringent,", font_size=19),
                Text("avec un angle d'incidence supérieur à l'angle limite)", font_size=19),
            ).arrange(DOWN, aligned_edge=LEFT, buff=0.18),
            box_width=11.8,
        )
        theoreme.next_to(titre, DOWN, buff=0.3)

        with self.voiceover(
            text=(
                "On peut donc énoncer les deux conditions nécessaires et "
                "suffisantes de la réflexion totale : il faut que n1 soit "
                "supérieur à n2, c'est-à-dire que la lumière parte d'un "
                "milieu plus réfringent, ET que l'angle d'incidence i1 "
                "soit supérieur à l'angle limite lambda. Si l'une de ces "
                "deux conditions manque, la réflexion totale ne se "
                "produit pas."
            )
        ) as tracker:
            self.play(FadeIn(theoreme))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(theoreme))

        # --- Exemple résolu 4 : angle limite eau/air et diamant/air ------------------
        exemple = example_box(
            VGroup(
                Text("Calculer l'angle limite pour l'eau (n=1,33) et le", font_size=20),
                Text("diamant (n=2,42), tous deux vers l'air (n=1).", font_size=20),
                MathTex(r"\text{eau} \to \text{air : } \sin\lambda = \dfrac{1}{1{,}33} \Rightarrow \lambda \approx 48{,}8^\circ", font_size=22, color=YELLOW),
                MathTex(r"\text{diamant} \to \text{air : } \sin\lambda = \dfrac{1}{2{,}42} \Rightarrow \lambda \approx 24{,}4^\circ", font_size=22, color=YELLOW),
                Text("Angle limite très petit ⇒ réflexions totales fréquentes,", font_size=19),
                Text("ce qui explique l'éclat si particulier du diamant.", font_size=19),
            ).arrange(DOWN, aligned_edge=LEFT, buff=0.2),
            box_width=11.8,
        )
        exemple.next_to(titre, DOWN, buff=0.3)

        with self.voiceover(
            text=(
                "Exemple résolu. Calculons l'angle limite pour l'eau, "
                "d'indice un virgule trente-trois, et pour le diamant, "
                "d'indice deux virgule quarante-deux, tous deux vers "
                "l'air. Pour l'eau : sinus lambda égal un sur un virgule "
                "trente-trois, ce qui donne lambda environ égal à "
                "quarante-huit virgule huit degrés. Pour le diamant : "
                "sinus lambda égal un sur deux virgule quarante-deux, ce "
                "qui donne lambda environ égal à vingt-quatre virgule "
                "quatre degrés seulement. Cet angle limite très petit "
                "signifie que la lumière subit des réflexions totales "
                "beaucoup plus facilement dans le diamant : c'est ce qui "
                "explique en grande partie son éclat si particulier."
            )
        ) as tracker:
            self.play(FadeIn(exemple))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(exemple))

        # --- À retenir --------------------------------------------------------------
        retenir = essentiel_box(
            VGroup(
                Text("À retenir", font_size=24, weight="BOLD"),
                MathTex(r"\sin \lambda = \dfrac{n_2}{n_1}", font_size=26),
                Text("Réflexion totale ⟺ n1 > n2 ET i1 > λ.", font_size=20),
                Text("Plus n1 est grand devant n2, plus λ est petit.", font_size=20),
            ).arrange(DOWN, buff=0.2),
            box_width=12.0,
        )
        retenir.next_to(titre, DOWN, buff=0.3)

        with self.voiceover(
            text=(
                "Retenons l'essentiel : sinus de l'angle limite lambda "
                "vaut n2 sur n1. La réflexion totale se produit si, et "
                "seulement si, n1 est supérieur à n2 et l'angle "
                "d'incidence i1 est supérieur à lambda. Et plus n1 est "
                "grand devant n2, plus l'angle limite est petit."
            )
        ) as tracker:
            self.play(FadeIn(retenir))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(retenir))

        # --- Piège à éviter ------------------------------------------------------------
        piege = warning_box(
            VGroup(
                Text("• L'angle limite n'existe QUE si n1 > n2. Si n1 < n2,", font_size=20),
                Text("   il n'y a jamais de réflexion totale, quel que soit i1.", font_size=20),
                Text("• Toujours calculer λ AVANT de chercher i2, dès que", font_size=20),
                Text("   n1 > n2 : c'est le réflexe indispensable pour éviter", font_size=20),
                Text("   un calcul d'arcsin(x>1), impossible.", font_size=20),
            ).arrange(DOWN, aligned_edge=LEFT, buff=0.16),
            box_width=12.2,
        )
        piege.next_to(titre, DOWN, buff=0.3)

        with self.voiceover(
            text=(
                "Piège à éviter : l'angle limite n'existe que si n1 est "
                "supérieur à n2. Si n1 est inférieur à n2, il n'y a "
                "jamais de réflexion totale, quel que soit l'angle "
                "d'incidence. Le réflexe indispensable, dès que n1 est "
                "supérieur à n2, est de toujours calculer l'angle limite "
                "avant de chercher i2, pour éviter de tomber sur un "
                "calcul d'arc sinus d'un nombre supérieur à un, qui est "
                "impossible."
            )
        ) as tracker:
            self.play(FadeIn(piege))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(piege), FadeOut(titre))
