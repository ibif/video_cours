"""
scenes/Physique_ReflexionRefractionLumiere_10.py — Chapitre « Réflexion et
réfraction de la lumière blanche » (1ereC, Physique), scène 10.

§ Déplacement latéral de la lame à faces parallèles : propriété
d = e·sin(i1-i2)/cos(i2) avec justification géométrique (triangle I1I2H),
remarques (d augmente avec e, n, i1 ; nul en incidence normale), exemple
résolu 5 (n=1,50, e=1cm, i1=30°).
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
from shapes.boxes import essentiel_box, example_box, property_box, scene_title, warning_box


def _wrap(text: str, width: int = 56) -> str:
    return "\n".join(textwrap.fill(line, width=width) for line in text.split("\n"))


class DeplacementLateralLame(NotionScene):
    def construct(self):
        titre = scene_title("Déplacement latéral de la lame à faces parallèles")
        titre.scale(0.42)
        titre.to_edge(UP)

        # --- Énoncé : où se trouve exactement le rayon émergent ? -------------------
        mise_en_situation = Text(
            _wrap(
                "Le rayon émergent d'une lame à faces parallèles est "
                "parallèle au rayon incident. Mais est-il exactement "
                "aligné avec lui, ou légèrement décalé ?",
                width=48,
            ),
            font_size=21,
        )
        mise_en_situation.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Le rayon émergent d'une lame à faces parallèles est "
                "parallèle au rayon incident. Mais est-il exactement "
                "aligné avec lui, ou légèrement décalé ?"
            )
        ) as tracker:
            self.play(Write(titre))
            self.play(FadeIn(mise_en_situation))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(mise_en_situation))

        # --- Raisonnement : construction géométrique du déplacement d ----------------
        e = 1.6
        lame = Rectangle(width=6.0, height=e, fill_color=BLUE, fill_opacity=0.12, stroke_color=GREY, stroke_width=3)
        lame.move_to(DOWN * 0.2)
        face_haute = lame.get_top()[1]
        face_basse = lame.get_bottom()[1]

        i1 = np.radians(30)
        i2 = np.radians(19.5)

        I1 = np.array([-1.0, face_haute, 0])
        I2 = np.array([-1.0 + e * np.tan(i2), face_basse, 0])

        S = I1 + 1.4 * np.array([-np.sin(i1), np.cos(i1), 0])
        entree = Line(S, I1, color=YELLOW, stroke_width=4)
        interne = Line(I1, I2, color=YELLOW, stroke_width=4)
        prolongement_direct = DashedLine(I1, I1 + 2.4 * np.array([np.sin(i1), -np.cos(i1), 0]), color=GREY, stroke_width=2)
        Tpt = I2 + 1.4 * np.array([np.sin(i1), -np.cos(i1), 0])
        sortie = Line(I2, Tpt, color=YELLOW, stroke_width=4)

        # H : pied de la perpendiculaire de I2 sur le prolongement du rayon incident non dévié
        dir_inc = np.array([np.sin(i1), -np.cos(i1), 0])
        vec_I1I2 = I2 - I1
        proj_len = np.dot(vec_I1I2, dir_inc)
        H = I1 + proj_len * dir_inc
        seg_I2H = DashedLine(I2, H, color=RED, stroke_width=3)
        dotH = Dot(H, color=RED, radius=0.05)
        label_H = MathTex("H", font_size=20, color=RED).next_to(H, RIGHT, buff=0.1)
        label_d = MathTex("d", font_size=22, color=RED).move_to((I2 + H) / 2 + LEFT * 0.35)

        dotI1 = Dot(I1, color=WHITE, radius=0.05)
        dotI2 = Dot(I2, color=WHITE, radius=0.05)

        schema = VGroup(
            lame, entree, interne, sortie, prolongement_direct,
            seg_I2H, dotH, label_H, label_d, dotI1, dotI2,
        )

        with self.voiceover(
            text=(
                "Traçons, en pointillés gris, le prolongement direct du "
                "rayon incident, comme s'il n'y avait pas eu de "
                "réfraction. Le vrai rayon, lui, ressort en I2, "
                "parallèlement à ce prolongement mais décalé. Notons H le "
                "pied de la perpendiculaire abaissée de I2 sur ce "
                "prolongement direct. La distance I2, H, tracée en rouge, "
                "est précisément le déplacement latéral d, mesuré "
                "perpendiculairement à la direction initiale du rayon."
            )
        ) as tracker:
            self.play(Create(lame))
            self.play(Create(entree), Create(prolongement_direct), FadeIn(dotI1))
            self.play(Create(interne), FadeIn(dotI2))
            self.play(Create(sortie))
            self.play(Create(seg_I2H), FadeIn(dotH), Write(label_H), Write(label_d))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(schema))

        # --- Propriété : formule du déplacement latéral -------------------------------
        propriete = property_box(
            VGroup(
                Text("Déplacement latéral d'une lame à faces parallèles", font_size=21, weight="BOLD"),
                MathTex(r"d = e\,\dfrac{\sin(i_1 - i_2)}{\cos i_2}", font_size=30, color=YELLOW),
                Text("Justification : dans le triangle I1I2H, rectangle en H,", font_size=19),
                MathTex(r"I_1I_2 = \dfrac{e}{\cos i_2} \ , \quad \widehat{I_2I_1H} = i_1 - i_2 \ \Rightarrow \ d = I_1I_2 \sin(i_1-i_2)", font_size=20),
            ).arrange(DOWN, buff=0.2),
            box_width=12.0,
        )
        propriete.next_to(titre, DOWN, buff=0.3)

        with self.voiceover(
            text=(
                "On établit ainsi la formule du déplacement latéral : d "
                "est égal à e fois le sinus de la différence i1 moins i2, "
                "le tout divisé par le cosinus de i2. La justification "
                "géométrique utilise le triangle I1, I2, H, rectangle en "
                "H : le segment I1 I2, à l'intérieur de la lame "
                "d'épaisseur e inclinée de l'angle i2 par rapport à la "
                "normale, mesure e sur cosinus de i2. Et l'angle entre le "
                "segment I1 I2 et le prolongement direct du rayon vaut "
                "exactement i1 moins i2. On en déduit d égal I1 I2 fois "
                "sinus de i1 moins i2, ce qui donne la formule annoncée."
            )
        ) as tracker:
            self.play(FadeIn(propriete))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(propriete))

        # --- Remarques -----------------------------------------------------------------
        remarques = VGroup(
            Text("Remarques :", font_size=20, weight="BOLD"),
            Text("• d augmente avec e (lame plus épaisse)", font_size=19),
            Text("• d augmente avec n (verre plus réfringent, i2 plus petit)", font_size=19),
            Text("• d augmente avec i1 (incidence plus oblique)", font_size=19),
            Text("• d = 0 en incidence normale (i1 = i2 = 0)", font_size=19),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.16)
        remarques.next_to(titre, DOWN, buff=0.35)

        with self.voiceover(
            text=(
                "Quelques remarques utiles. Le déplacement d augmente "
                "avec l'épaisseur e de la lame. Il augmente aussi avec "
                "l'indice n, car un verre plus réfringent rend i2 plus "
                "petit, donc l'écart i1 moins i2 plus grand. Il augmente "
                "avec l'angle d'incidence i1, une incidence plus oblique "
                "donnant un décalage plus marqué. Et en incidence "
                "normale, i1 et i2 valent tous deux zéro : il n'y a "
                "alors aucun déplacement latéral."
            )
        ) as tracker:
            self.play(Write(remarques))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(remarques))

        # --- Exemple résolu 5 ------------------------------------------------------------
        exemple = example_box(
            VGroup(
                Text("Lame de verre n=1,50, e=1 cm, i1=30°. Calculer d.", font_size=20),
                MathTex(r"\sin i_2 = \dfrac{\sin 30^\circ}{1{,}50} = 0{,}333 \ \Rightarrow \ i_2 \approx 19{,}5^\circ", font_size=22, color=YELLOW),
                MathTex(r"d = 1 \times \dfrac{\sin(30^\circ - 19{,}5^\circ)}{\cos 19{,}5^\circ} \approx \dfrac{0{,}182}{0{,}943}", font_size=22, color=YELLOW),
                MathTex(r"d \approx 0{,}19\ \text{cm} \approx 1{,}9\ \text{mm}", font_size=24, color=YELLOW),
            ).arrange(DOWN, aligned_edge=LEFT, buff=0.2),
            box_width=11.8,
        )
        exemple.next_to(titre, DOWN, buff=0.3)

        with self.voiceover(
            text=(
                "Exemple résolu. Une lame de verre d'indice un virgule "
                "cinquante, d'épaisseur un centimètre, reçoit un rayon "
                "avec un angle d'incidence de trente degrés. Calculons "
                "d'abord i2 : sinus de i2 égale sinus de trente degrés "
                "sur un virgule cinquante, soit zéro virgule "
                "trois-cent-trente-trois, ce qui donne i2 environ égal à "
                "dix-neuf virgule cinq degrés. Puis d égale un fois sinus "
                "de trente moins dix-neuf virgule cinq, sur cosinus de "
                "dix-neuf virgule cinq, soit environ zéro virgule "
                "cent-quatre-vingt-deux sur zéro virgule neuf-cent-quarante-trois. "
                "On trouve d environ égal à zéro virgule dix-neuf "
                "centimètre, soit environ un virgule neuf millimètre."
            )
        ) as tracker:
            self.play(FadeIn(exemple))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(exemple))

        # --- À retenir --------------------------------------------------------------
        retenir = essentiel_box(
            VGroup(
                Text("À retenir", font_size=24, weight="BOLD"),
                MathTex(r"d = e\,\dfrac{\sin(i_1-i_2)}{\cos i_2}", font_size=28),
                Text("d augmente avec e, n, i1 ; d = 0 en incidence normale.", font_size=20),
            ).arrange(DOWN, buff=0.22),
            box_width=11.6,
        )
        retenir.next_to(titre, DOWN, buff=0.3)

        with self.voiceover(
            text=(
                "Retenons l'essentiel : le déplacement latéral d vaut e "
                "fois sinus de i1 moins i2, sur cosinus de i2. Il "
                "augmente avec l'épaisseur, l'indice et l'angle "
                "d'incidence, et il est nul en incidence normale."
            )
        ) as tracker:
            self.play(FadeIn(retenir))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(retenir))

        # --- Piège à éviter ------------------------------------------------------------
        piege = warning_box(
            VGroup(
                Text("• d se mesure PERPENDICULAIREMENT à la direction du", font_size=20),
                Text("   rayon incident, pas horizontalement ni verticalement.", font_size=20),
                Text("• Le rayon émergent N'EST PAS dévié (même direction),", font_size=20),
                Text("   seulement déplacé : ne pas parler d'un \"angle de", font_size=20),
                Text("   déviation\" pour une lame à faces parallèles.", font_size=20),
            ).arrange(DOWN, aligned_edge=LEFT, buff=0.16),
            box_width=12.4,
        )
        piege.next_to(titre, DOWN, buff=0.3)

        with self.voiceover(
            text=(
                "Piège à éviter : le déplacement d se mesure "
                "perpendiculairement à la direction du rayon incident, "
                "pas horizontalement ni verticalement. Et surtout, le "
                "rayon émergent n'est pas dévié, il garde la même "
                "direction, il est seulement déplacé : on ne doit "
                "jamais parler d'un angle de déviation pour une lame à "
                "faces parallèles."
            )
        ) as tracker:
            self.play(FadeIn(piege))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(piege), FadeOut(titre))
