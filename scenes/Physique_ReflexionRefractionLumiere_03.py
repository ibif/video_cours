"""
scenes/Physique_ReflexionRefractionLumiere_03.py — Chapitre « Réflexion et
réfraction de la lumière blanche » (1ereC, Physique), scène 03.

§ Construction de l'image d'un objet étendu AB par un miroir plan (symétrie
point par point, tracé en pointillés), caractéristiques de l'image
(virtuelle, symétrique, même grandeur, droite), exemple résolu (Awa devant
une glace), propriété de rotation d'un miroir (rotation α du miroir →
rotation 2α du rayon réfléchi).
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
    Text,
    VGroup,
    Write,
)

from shapes.base_scene import NotionScene
from shapes.boxes import example_box, essentiel_box, property_box, scene_title, warning_box


def _wrap(text: str, width: int = 56) -> str:
    return "\n".join(textwrap.fill(line, width=width) for line in text.split("\n"))


class ConstructionCaracteristiquesImageMiroir(NotionScene):
    def construct(self):
        titre = scene_title("Construction et caractéristiques de l'image")
        titre.scale(0.44)
        titre.to_edge(UP)

        # --- Énoncé : image d'un objet étendu AB -----------------------------------
        mise_en_situation = Text(
            _wrap(
                "Le miroir plan donne l'image d'un point A. Mais un objet "
                "réel, comme une flèche AB, est un ensemble de points. "
                "Comment construire l'image A'B' de tout l'objet ?",
                width=48,
            ),
            font_size=21,
        )
        mise_en_situation.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Le miroir plan donne l'image d'un point A. Mais un objet "
                "réel, comme une flèche AB, est un ensemble de points. "
                "Comment construire l'image A prime B prime de tout "
                "l'objet ?"
            )
        ) as tracker:
            self.play(Write(titre))
            self.play(FadeIn(mise_en_situation))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(mise_en_situation))

        # --- Raisonnement : construction point par point ----------------------------
        miroir = Line(UP * 2.0, DOWN * 2.0, color=GREY, stroke_width=5)
        A = LEFT * 2.2 + DOWN * 0.6
        B = LEFT * 2.2 + UP * 1.0
        Ap = RIGHT * 2.2 + DOWN * 0.6
        Bp = RIGHT * 2.2 + UP * 1.0

        fleche_objet = Line(A, B, color=YELLOW, stroke_width=4)
        dotA = Dot(A, color=YELLOW, radius=0.06)
        dotB = Dot(B, color=YELLOW, radius=0.06)
        lA = MathTex("A", font_size=22).next_to(A, LEFT, buff=0.1)
        lB = MathTex("B", font_size=22).next_to(B, LEFT, buff=0.1)

        perp_A = DashedLine(A, Ap, color=BLUE, stroke_width=2)
        perp_B = DashedLine(B, Bp, color=BLUE, stroke_width=2)
        fleche_image = DashedLine(Ap, Bp, color=BLUE, stroke_width=4)
        dotAp = Dot(Ap, color=BLUE, radius=0.06)
        dotBp = Dot(Bp, color=BLUE, radius=0.06)
        lAp = MathTex("A'", font_size=22, color=BLUE).next_to(Ap, RIGHT, buff=0.1)
        lBp = MathTex("B'", font_size=22, color=BLUE).next_to(Bp, RIGHT, buff=0.1)

        schema = VGroup(
            miroir, fleche_objet, dotA, dotB, lA, lB,
            perp_A, perp_B, fleche_image, dotAp, dotBp, lAp, lBp,
        )
        schema.move_to(DOWN * 0.2)

        with self.voiceover(
            text=(
                "La méthode est simple : on construit séparément le "
                "symétrique de chaque point de l'objet par rapport au "
                "plan du miroir. Le symétrique de A donne A prime, le "
                "symétrique de B donne B prime, chacun sur la "
                "perpendiculaire au miroir passant par le point, à égale "
                "distance de part et d'autre. En reliant A prime à B "
                "prime, on obtient l'image complète de la flèche, tracée "
                "en pointillés puisqu'elle est virtuelle."
            )
        ) as tracker:
            self.play(Create(miroir))
            self.play(Create(fleche_objet), FadeIn(dotA), FadeIn(dotB), Write(lA), Write(lB))
            self.play(Create(perp_A), Create(perp_B))
            self.play(Create(fleche_image), FadeIn(dotAp), FadeIn(dotBp), Write(lAp), Write(lBp))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(schema))

        # --- Propriété : caractéristiques de l'image --------------------------------
        proprietes = property_box(
            VGroup(
                Text("Caractéristiques de l'image par un miroir plan", font_size=22, weight="BOLD"),
                Text("• Virtuelle (ne peut être recueillie sur un écran)", font_size=20),
                Text("• Symétrique de l'objet par rapport au plan du miroir", font_size=20),
                Text("• De même grandeur que l'objet", font_size=20),
                Text("• Droite (même orientation que l'objet, non renversée)", font_size=20),
            ).arrange(DOWN, aligned_edge=LEFT, buff=0.18),
            box_width=11.8,
        )
        proprietes.next_to(titre, DOWN, buff=0.35)

        with self.voiceover(
            text=(
                "On retient quatre caractéristiques de l'image donnée par "
                "un miroir plan : elle est virtuelle, elle est symétrique "
                "de l'objet par rapport au plan du miroir, elle a "
                "exactement la même grandeur que l'objet, et elle est "
                "droite, c'est-à-dire de même orientation que l'objet, "
                "contrairement à une image renversée."
            )
        ) as tracker:
            self.play(FadeIn(proprietes))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(proprietes))

        # --- Exemple résolu 2 : Awa devant une glace ---------------------------------
        exemple = example_box(
            VGroup(
                Text("Awa, 1,6 m, se tient à 2 m d'une glace (miroir plan).", font_size=20),
                Text("Caractériser son image.", font_size=20),
                MathTex(r"\text{image virtuelle, à } 2\ \text{m derrière la glace}", font_size=22, color=YELLOW),
                MathTex(r"\text{taille de l'image} = 1{,}6\ \text{m}", font_size=22, color=YELLOW),
                MathTex(r"\text{distance Awa} \leftrightarrow \text{image} = 2 + 2 = 4\ \text{m}", font_size=22, color=YELLOW),
            ).arrange(DOWN, aligned_edge=LEFT, buff=0.2),
            box_width=11.8,
        )
        exemple.next_to(titre, DOWN, buff=0.35)

        with self.voiceover(
            text=(
                "Exemple résolu. Awa, qui mesure un virgule six mètre, se "
                "tient à deux mètres d'une glace. Caractérisons son image. "
                "L'image est virtuelle, elle se trouve à deux mètres "
                "derrière la glace, exactement symétrique de sa position. "
                "Sa taille est égale à celle d'Awa, un virgule six mètre. "
                "Et la distance entre Awa elle-même et son image vaut deux "
                "mètres plus deux mètres, soit quatre mètres."
            )
        ) as tracker:
            self.play(FadeIn(exemple))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(exemple))

        # --- Propriété : rotation d'un miroir ----------------------------------------
        pivot = LEFT * 0.5
        miroir_r1 = Line(pivot + UP * 1.6, pivot + DOWN * 1.6, color=GREY, stroke_width=5)
        rayon_inc = Line(pivot + LEFT * 3.0 + UP * 0.9, pivot, color=YELLOW, stroke_width=3)
        rayon_ref1 = Line(pivot, pivot + RIGHT * 2.6 + UP * 0.9, color=YELLOW, stroke_width=3)

        alpha = np.radians(20)
        miroir_dir = np.array([np.sin(alpha), np.cos(alpha), 0])
        miroir_r2 = Line(pivot - 1.6 * miroir_dir, pivot + 1.6 * miroir_dir, color=BLUE, stroke_width=3)
        # Rayon réfléchi tourné de 2*alpha par rapport au premier (propriété de rotation
        # du miroir), rotation trigonométrique négative car le rayon bascule vers le bas.
        beta = np.radians(20 * 2)
        v1 = np.array([2.6, 0.9, 0]) / np.linalg.norm([2.6, 0.9, 0])
        cos_b, sin_b = np.cos(-beta), np.sin(-beta)
        v2 = np.array([v1[0] * cos_b - v1[1] * sin_b, v1[0] * sin_b + v1[1] * cos_b, 0])
        rayon_ref2 = Line(pivot, pivot + 2.6 * v2, color=BLUE, stroke_width=3)

        label_alpha = Text("miroir tourné de α", font_size=17, color=BLUE)
        label_2alpha = Text("rayon réfléchi tourné de 2α", font_size=17, color=BLUE)
        schema_rot = VGroup(miroir_r1, rayon_inc, rayon_ref1, miroir_r2, rayon_ref2)
        schema_rot.move_to(DOWN * 0.3)
        labels_rot = VGroup(label_alpha, label_2alpha).arrange(DOWN, buff=0.15)
        labels_rot.next_to(schema_rot, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Une dernière propriété utile : si l'on fait tourner un "
                "miroir plan d'un angle alpha, en gardant le rayon "
                "incident fixe, le rayon réfléchi tourne d'un angle deux "
                "fois plus grand, deux alpha. Cette propriété est utilisée "
                "dans certains instruments de mesure de précision, comme "
                "le miroir tournant d'un galvanomètre optique."
            )
        ) as tracker:
            self.play(Create(miroir_r1), Create(rayon_inc), Create(rayon_ref1))
            self.play(Create(miroir_r2), Write(label_alpha))
            self.play(Create(rayon_ref2), Write(label_2alpha))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(schema_rot), FadeOut(labels_rot))

        # --- À retenir --------------------------------------------------------------
        retenir = essentiel_box(
            VGroup(
                Text("À retenir", font_size=24, weight="BOLD"),
                Text("Image virtuelle, symétrique, de même grandeur, droite.", font_size=20),
                Text("Construction : symétrique point par point de l'objet.", font_size=20),
                Text("Rotation α du miroir ⇒ rotation 2α du rayon réfléchi.", font_size=20),
            ).arrange(DOWN, buff=0.2),
            box_width=12.0,
        )
        retenir.next_to(titre, DOWN, buff=0.35)

        with self.voiceover(
            text=(
                "Retenons l'essentiel : l'image donnée par un miroir plan "
                "est virtuelle, symétrique, de même grandeur, et droite. "
                "On la construit en prenant le symétrique de chaque point "
                "de l'objet. Et si le miroir tourne d'un angle alpha, le "
                "rayon réfléchi tourne d'un angle deux fois plus grand."
            )
        ) as tracker:
            self.play(FadeIn(retenir))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(retenir))

        # --- Piège à éviter ------------------------------------------------------------
        piege = warning_box(
            VGroup(
                Text("• Une image DROITE ne veut pas dire NON INVERSÉE", font_size=20),
                Text("   gauche-droite : un miroir plan inverse la profondeur", font_size=20),
                Text("   (avant/arrière), pas le haut et le bas.", font_size=20),
                Text("• La distance objet-image se compte TOUJOURS depuis", font_size=20),
                Text("   l'objet JUSQU'À l'image, en passant par le miroir.", font_size=20),
            ).arrange(DOWN, aligned_edge=LEFT, buff=0.16),
            box_width=12.2,
        )
        piege.next_to(titre, DOWN, buff=0.35)

        with self.voiceover(
            text=(
                "Piège à éviter : une image dite droite ne signifie pas "
                "qu'elle n'est pas inversée gauche-droite. En réalité, un "
                "miroir plan inverse la profondeur, avant contre arrière, "
                "et non le haut et le bas. Et la distance objet-image se "
                "compte toujours depuis l'objet jusqu'à l'image, en "
                "passant par le miroir, comme dans l'exemple d'Awa."
            )
        ) as tracker:
            self.play(FadeIn(piege))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(piege), FadeOut(titre))
