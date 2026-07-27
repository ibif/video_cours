"""
scenes/Physique_ReflexionRefractionLumiere_09.py — Chapitre « Réflexion et
réfraction de la lumière blanche » (1ereC, Physique), scène 09.

§ La lame à faces parallèles : définition, trajet du rayon (entrée
air→verre, sortie verre→air, angles alternes-internes), théorème de la
propriété fondamentale (le rayon émergent est parallèle au rayon incident)
avec démonstration complète (sin i1 = n sin i2 à l'entrée, n sin i2 = sin
i1' à la sortie ⇒ i1' = i1).
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
from shapes.boxes import definition_box, essentiel_box, theorem_box, scene_title, warning_box


def _wrap(text: str, width: int = 56) -> str:
    return "\n".join(textwrap.fill(line, width=width) for line in text.split("\n"))


class LameFacesParallelesTrajetPropriete(NotionScene):
    def construct(self):
        titre = scene_title("La lame à faces parallèles : trajet et propriété fondamentale")
        titre.scale(0.36)
        titre.to_edge(UP)

        # --- Énoncé : un bloc de verre à faces parallèles -----------------------------
        mise_en_situation = Text(
            _wrap(
                "On regarde un objet à travers une vitre épaisse posée à "
                "plat, aux deux faces parfaitement parallèles. L'objet "
                "paraît légèrement décalé, mais jamais déformé en angle. "
                "Pourquoi ?",
                width=48,
            ),
            font_size=21,
        )
        mise_en_situation.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "On regarde un objet à travers une vitre épaisse posée à "
                "plat, dont les deux faces sont parfaitement parallèles. "
                "L'objet paraît légèrement décalé, mais jamais déformé en "
                "angle. Pourquoi ?"
            )
        ) as tracker:
            self.play(Write(titre))
            self.play(FadeIn(mise_en_situation))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(mise_en_situation))

        # --- Définition : lame à faces parallèles -------------------------------------
        definition = definition_box(
            VGroup(
                Text("Lame à faces parallèles", font_size=22, weight="BOLD"),
                Text("Bloc de matériau transparent (verre, indice n), d'épaisseur", font_size=20),
                Text("e, limité par deux faces planes strictement parallèles.", font_size=20),
            ).arrange(DOWN, buff=0.2),
            box_width=11.8,
        )
        definition.next_to(titre, DOWN, buff=0.35)

        with self.voiceover(
            text=(
                "Une lame à faces parallèles est un bloc de matériau "
                "transparent, de verre par exemple, d'indice n, "
                "d'épaisseur e, limité par deux faces planes strictement "
                "parallèles entre elles."
            )
        ) as tracker:
            self.play(FadeIn(definition))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(definition))

        # --- Raisonnement : trajet du rayon --------------------------------------------
        e = 1.6
        lame = Rectangle(width=6.0, height=e, fill_color=BLUE, fill_opacity=0.12, stroke_color=GREY, stroke_width=3)
        lame.move_to(DOWN * 0.2)
        face_haute = lame.get_top()[1]
        face_basse = lame.get_bottom()[1]

        I1 = np.array([-1.0, face_haute, 0])
        I2 = np.array([-1.0 + e * np.tan(np.radians(19.5)), face_basse, 0])

        i1 = np.radians(30)
        i2 = np.radians(19.5)

        S = I1 + 1.6 * np.array([-np.sin(i1), np.cos(i1), 0])
        entree = Line(S, I1, color=YELLOW, stroke_width=4)
        interne = Line(I1, I2, color=YELLOW, stroke_width=4)
        Tpt = I2 + 1.6 * np.array([np.sin(i1), -np.cos(i1), 0])
        sortie = Line(I2, Tpt, color=YELLOW, stroke_width=4)

        normale1 = DashedLine(I1 + DOWN * 0.7, I1 + UP * 1.0, color=WHITE, stroke_width=2)
        normale2 = DashedLine(I2 + DOWN * 1.0, I2 + UP * 0.7, color=WHITE, stroke_width=2)
        dotI1 = Dot(I1, color=WHITE, radius=0.05)
        dotI2 = Dot(I2, color=WHITE, radius=0.05)

        label_i1 = MathTex("i_1", font_size=20, color=BLUE).move_to(I1 + UP * 0.55 + LEFT * 0.35)
        label_i2h = MathTex("i_2", font_size=20, color=BLUE).move_to(I1 + DOWN * 0.35 + RIGHT * 0.3)
        label_i2b = MathTex("i_2", font_size=20, color=BLUE).move_to(I2 + UP * 0.35 + LEFT * 0.3)
        label_i1p = MathTex("i_1'", font_size=20, color=BLUE).move_to(I2 + DOWN * 0.55 + RIGHT * 0.35)
        label_air1 = Text("air", font_size=16).move_to(I1 + UP * 1.2 + LEFT * 1.6)
        label_verre = Text("verre (n)", font_size=16).move_to(DOWN * 0.2)
        label_air2 = Text("air", font_size=16).move_to(I2 + DOWN * 1.2 + RIGHT * 1.6)

        schema = VGroup(
            lame, entree, interne, sortie, normale1, normale2, dotI1, dotI2,
            label_i1, label_i2h, label_i2b, label_i1p, label_air1, label_verre, label_air2,
        )

        with self.voiceover(
            text=(
                "Suivons le trajet du rayon. À l'entrée de la lame, en "
                "I1, le rayon passe de l'air au verre : il se rapproche "
                "de la normale, i1 devient i2. Il traverse ensuite la "
                "lame en ligne droite jusqu'à la seconde face, en I2. Là, "
                "il repasse du verre à l'air : comme les deux normales, "
                "en I1 et en I2, sont parallèles puisque les deux faces "
                "le sont, l'angle d'incidence interne en I2 est encore i2 "
                "— ce sont des angles alternes-internes entre droites "
                "parallèles. Le rayon ressort donc avec un nouvel angle, "
                "que nous appelons i1 prime."
            )
        ) as tracker:
            self.play(Create(lame), Write(label_air1), Write(label_verre), Write(label_air2))
            self.play(Create(entree), Create(normale1), FadeIn(dotI1), Write(label_i1))
            self.play(Write(label_i2h))
            self.play(Create(interne))
            self.play(Create(normale2), FadeIn(dotI2), Write(label_i2b))
            self.play(Create(sortie), Write(label_i1p))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(schema))

        # --- Théorème + démonstration : rayon émergent parallèle ---------------------
        theoreme = theorem_box(
            VGroup(
                Text("Propriété fondamentale de la lame à faces parallèles", font_size=21, weight="BOLD"),
                Text("Le rayon émergent est parallèle au rayon incident", font_size=20),
                MathTex(r"(\text{il est seulement décalé, voir scène suivante) :} \quad i_1' = i_1", font_size=22, color=YELLOW),
            ).arrange(DOWN, aligned_edge=LEFT, buff=0.2),
            box_width=11.8,
        )
        theoreme.next_to(titre, DOWN, buff=0.3)

        with self.voiceover(
            text=(
                "On obtient ainsi le théorème central de cette scène : le "
                "rayon émergent d'une lame à faces parallèles est "
                "parallèle au rayon incident, il est seulement décalé "
                "latéralement, ce que nous étudierons dans la scène "
                "suivante. Autrement dit, i1 prime est égal à i1."
            )
        ) as tracker:
            self.play(FadeIn(theoreme))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(theoreme))

        # --- Démonstration détaillée ----------------------------------------------------
        demo = VGroup(
            Text("Démonstration :", font_size=20, weight="BOLD"),
            Text("• À l'entrée (I1), air → verre :", font_size=19),
            MathTex(r"\sin i_1 = n \sin i_2", font_size=22),
            Text("• À la sortie (I2), verre → air, avec le MÊME i2", font_size=19),
            Text("   (angles alternes-internes, normales parallèles) :", font_size=19),
            MathTex(r"n \sin i_2 = \sin i_1'", font_size=22),
            Text("• En combinant les deux relations :", font_size=19),
            MathTex(r"\sin i_1' = n \sin i_2 = \sin i_1 \ \Rightarrow \ i_1' = i_1", font_size=24, color=YELLOW),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.16)
        demo.next_to(titre, DOWN, buff=0.3)

        with self.voiceover(
            text=(
                "Détaillons la démonstration. À l'entrée, en I1, la loi "
                "de Snell-Descartes de l'air vers le verre donne sinus de "
                "i1 égal n fois sinus de i2. À la sortie, en I2, du verre "
                "vers l'air, avec le même angle interne i2 grâce au "
                "parallélisme des deux normales, la loi donne n fois "
                "sinus de i2 égal sinus de i1 prime. En combinant ces "
                "deux relations, sinus de i1 prime est égal à n sinus i2, "
                "qui est égal à sinus de i1 : donc i1 prime est "
                "rigoureusement égal à i1. Le rayon émergent a donc "
                "exactement la même direction que le rayon incident."
            )
        ) as tracker:
            self.play(Write(demo))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(demo))

        # --- À retenir --------------------------------------------------------------
        retenir = essentiel_box(
            VGroup(
                Text("À retenir", font_size=24, weight="BOLD"),
                MathTex(r"\sin i_1 = n \sin i_2 \quad \text{(entrée)}, \quad n \sin i_2 = \sin i_1' \quad \text{(sortie)}", font_size=22),
                MathTex(r"\Rightarrow \ i_1' = i_1 \ (\text{rayon émergent} \parallel \text{rayon incident})", font_size=24),
            ).arrange(DOWN, buff=0.22),
            box_width=12.4,
        )
        retenir.next_to(titre, DOWN, buff=0.3)

        with self.voiceover(
            text=(
                "Retenons l'essentiel : à l'entrée, sinus de i1 égale n "
                "sinus de i2 ; à la sortie, n sinus de i2 égale sinus de "
                "i1 prime. On en déduit que i1 prime égale i1 : le rayon "
                "émergent est parallèle au rayon incident."
            )
        ) as tracker:
            self.play(FadeIn(retenir))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(retenir))

        # --- Piège à éviter ------------------------------------------------------------
        piege = warning_box(
            VGroup(
                Text("• Parallèle NE VEUT PAS DIRE identique : le rayon", font_size=20),
                Text("   émergent a la même direction que l'incident, mais", font_size=20),
                Text("   PAS la même position (voir déplacement latéral d).", font_size=20),
                Text("• Cette propriété suppose que les DEUX faces sont", font_size=20),
                Text("   parallèles ; ce n'est plus vrai pour un prisme.", font_size=20),
            ).arrange(DOWN, aligned_edge=LEFT, buff=0.16),
            box_width=12.2,
        )
        piege.next_to(titre, DOWN, buff=0.3)

        with self.voiceover(
            text=(
                "Piège à éviter : parallèle ne veut pas dire identique. "
                "Le rayon émergent a la même direction que le rayon "
                "incident, mais pas la même position : il est décalé "
                "latéralement, comme nous le verrons dans la prochaine "
                "scène. Et cette propriété suppose que les deux faces "
                "sont bien parallèles : elle ne s'applique plus à un "
                "prisme, dont les faces forment un angle."
            )
        ) as tracker:
            self.play(FadeIn(piege))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(piege), FadeOut(titre))
