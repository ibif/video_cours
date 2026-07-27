"""
scenes/Physique_ReflexionRefractionLumiere_02.py — Chapitre « Réflexion et
réfraction de la lumière blanche » (1ereC, Physique), scène 02.

§ Le miroir plan : définition, construction de l'image A' d'un point A par
deux rayons réfléchis dont les prolongements se coupent en A' (image
virtuelle), théorème « A' est le symétrique de A par rapport au plan du
miroir » avec démonstration complète par triangles isométriques (angles
égaux via la loi de la réflexion).
Source : 1ereC/Physique.pdf, pages 117-129.
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
from shapes.boxes import definition_box, essentiel_box, theorem_box, scene_title, warning_box


def _wrap(text: str, width: int = 56) -> str:
    return "\n".join(textwrap.fill(line, width=width) for line in text.split("\n"))


class MiroirPlanImageDemonstration(NotionScene):
    def construct(self):
        titre = scene_title("Le miroir plan : image d'un point, démonstration")
        titre.scale(0.42)
        titre.to_edge(UP)

        # --- Énoncé : qu'est-ce qu'un miroir plan ? ------------------------------
        miroir0 = Line(UP * 1.8, DOWN * 1.8, color=GREY, stroke_width=5).shift(RIGHT * 0.5)
        objetA0 = Dot(LEFT * 2.2, color=YELLOW, radius=0.09)
        labelA0 = MathTex("A", font_size=24).next_to(objetA0, LEFT, buff=0.1)
        oeil0 = Dot(LEFT * 3.0 + DOWN * 1.2, color=WHITE, radius=0.08)
        schema0 = VGroup(miroir0, objetA0, labelA0, oeil0)
        schema0.move_to(DOWN * 0.4)

        mise_en_situation = Text(
            _wrap(
                "Un point lumineux A est placé devant une surface plane et "
                "parfaitement polie : un miroir plan. Un œil placé devant "
                "voit un point A qui semble se trouver DERRIÈRE le miroir. "
                "Où se trouve exactement cette image ?",
                width=50,
            ),
            font_size=21,
        )
        mise_en_situation.next_to(titre, DOWN, buff=0.4)
        schema0.next_to(mise_en_situation, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Un point lumineux A est placé devant une surface plane et "
                "parfaitement polie, un miroir plan. Un œil placé devant "
                "voit un point qui semble se trouver derrière le miroir. "
                "Où se trouve exactement cette image ?"
            )
        ) as tracker:
            self.play(Write(titre))
            self.play(FadeIn(mise_en_situation))
            self.play(Create(schema0))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(mise_en_situation), FadeOut(schema0))

        # --- Définition : miroir plan --------------------------------------------
        definition = definition_box(
            VGroup(
                Text("Miroir plan", font_size=23, weight="BOLD"),
                Text("Surface plane parfaitement polie qui réfléchit la lumière", font_size=20),
                Text("en respectant les lois de Snell-Descartes de la réflexion.", font_size=20),
            ).arrange(DOWN, buff=0.22),
            box_width=11.6,
        )
        definition.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Un miroir plan est une surface plane parfaitement polie, "
                "qui réfléchit la lumière en respectant les lois de "
                "Snell-Descartes de la réflexion vues précédemment."
            )
        ) as tracker:
            self.play(FadeIn(definition))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(definition))

        # --- Raisonnement : construction de l'image par deux rayons -------------
        miroir = Line(UP * 2.0, DOWN * 2.0, color=GREY, stroke_width=5)
        A = LEFT * 3.0 + UP * 0.3
        I1 = UP * 1.2
        I2 = DOWN * 0.6
        pointA = Dot(A, color=YELLOW, radius=0.08)
        labelA = MathTex("A", font_size=24).next_to(A, LEFT, buff=0.12)

        rayon1 = Line(A, I1, color=YELLOW, stroke_width=3)
        rayon2 = Line(A, I2, color=YELLOW, stroke_width=3)

        # Prolongements réfléchis vers l'œil (à droite du miroir, symétrique de A)
        Aprime = RIGHT * 3.0 + UP * 0.3
        oeil = RIGHT * 4.6 + DOWN * 0.9
        reflechi1 = Line(I1, oeil, color=YELLOW, stroke_width=3)
        reflechi2 = Line(I2, oeil, color=YELLOW, stroke_width=3)
        prolong1 = DashedLine(I1, Aprime, color=BLUE, stroke_width=2)
        prolong2 = DashedLine(I2, Aprime, color=BLUE, stroke_width=2)
        pointAprime = Dot(Aprime, color=BLUE, radius=0.08)
        labelAprime = MathTex("A'", font_size=24, color=BLUE).next_to(Aprime, RIGHT, buff=0.12)
        oeil_dot = Dot(oeil, color=WHITE, radius=0.07)

        schema = VGroup(miroir, pointA, labelA, rayon1, rayon2, reflechi1, reflechi2, oeil_dot)
        prolongations = VGroup(prolong1, prolong2, pointAprime, labelAprime)
        ensemble = VGroup(schema, prolongations)
        ensemble.scale(0.8)
        ensemble.move_to(DOWN * 0.2)

        with self.voiceover(
            text=(
                "Traçons deux rayons issus de A, qui touchent le miroir en "
                "deux points différents, puis qui se réfléchissent selon "
                "la loi i'1 égale i1 vers l'œil de l'observateur. L'œil "
                "reçoit ces deux rayons réfléchis et les perçoit comme "
                "venant en ligne droite de l'endroit où ils semblent se "
                "croiser. Prolongeons donc ces deux rayons réfléchis "
                "derrière le miroir, en pointillés : ils se coupent "
                "exactement en un point A prime. C'est là que l'œil situe "
                "l'image du point A. Comme aucune lumière ne traverse "
                "réellement le miroir, cette image ne peut pas être "
                "recueillie sur un écran : c'est une image virtuelle."
            )
        ) as tracker:
            self.play(Create(miroir), FadeIn(pointA), Write(labelA))
            self.play(Create(rayon1), Create(rayon2))
            self.play(Create(reflechi1), Create(reflechi2), FadeIn(oeil_dot))
            self.play(Create(prolong1), Create(prolong2))
            self.play(FadeIn(pointAprime), Write(labelAprime))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(schema), FadeOut(prolongations))

        # --- Théorème + démonstration : A' symétrique de A -----------------------
        theoreme_enonce = theorem_box(
            VGroup(
                Text("Image d'un point par un miroir plan", font_size=22, weight="BOLD"),
                Text("L'image A' d'un point A est le symétrique de A par", font_size=20),
                Text("rapport au plan du miroir : A' est virtuelle, sur la", font_size=20),
                Text("perpendiculaire au miroir passant par A, à la même", font_size=20),
                Text("distance derrière le miroir que A devant.", font_size=20),
            ).arrange(DOWN, aligned_edge=LEFT, buff=0.18),
            box_width=12.0,
        )
        theoreme_enonce.next_to(titre, DOWN, buff=0.35)

        with self.voiceover(
            text=(
                "Ce résultat se généralise en un théorème : l'image A "
                "prime d'un point A par un miroir plan est le symétrique "
                "de A par rapport au plan du miroir."
            )
        ) as tracker:
            self.play(FadeIn(theoreme_enonce))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(theoreme_enonce))

        # --- Démonstration géométrique (triangles isométriques) ------------------
        H = RIGHT * 0.0
        miroir_d = Line(UP * 2.0, DOWN * 2.0, color=GREY, stroke_width=5)
        Ad = LEFT * 2.6 + UP * 0.5
        Hd = LEFT * 0.0 + UP * 0.5
        Id = UP * 1.6
        Apd = RIGHT * 2.6 + UP * 0.5

        seg_AH = Line(Ad, Hd, color=YELLOW, stroke_width=2)
        seg_HAp = DashedLine(Hd, Apd, color=BLUE, stroke_width=2)
        seg_AI = Line(Ad, Id, color=YELLOW, stroke_width=3)
        seg_IAp = DashedLine(Id, Apd, color=BLUE, stroke_width=3)
        seg_IH = Line(Id, Hd, color=WHITE, stroke_width=2)

        dotA = Dot(Ad, color=YELLOW, radius=0.07)
        dotH = Dot(Hd, color=WHITE, radius=0.06)
        dotI = Dot(Id, color=WHITE, radius=0.06)
        dotAp = Dot(Apd, color=BLUE, radius=0.07)

        lA = MathTex("A", font_size=22).next_to(Ad, LEFT, buff=0.1)
        lH = MathTex("H", font_size=22).next_to(Hd, DOWN, buff=0.1)
        lI = MathTex("I", font_size=22).next_to(Id, UP, buff=0.1)
        lAp = MathTex("A'", font_size=22, color=BLUE).next_to(Apd, RIGHT, buff=0.1)

        demo_schema = VGroup(
            miroir_d, seg_AH, seg_HAp, seg_AI, seg_IAp, seg_IH,
            dotA, dotH, dotI, dotAp, lA, lH, lI, lAp,
        )
        demo_schema.scale(0.85)
        demo_schema.move_to(LEFT * 3.4 + DOWN * 0.3)

        demo_texte = VGroup(
            Text("Soit H le pied de la perpendiculaire de A au miroir,", font_size=18),
            Text("et I un point d'incidence quelconque du miroir.", font_size=18),
            Text("Triangles AIH et A'IH :", font_size=18, weight="BOLD"),
            Text("• angle en H = 90° (commun aux deux triangles)", font_size=18),
            Text("• IH est un côté commun", font_size=18),
            Text("• angle AIH = angle A'IH (loi i1' = i1, par construction", font_size=18),
            Text("   de A' sur le prolongement du rayon réfléchi)", font_size=18),
            Text("⇒ triangles AIH et A'IH isométriques (ASA)", font_size=18, color=YELLOW),
            Text("⇒ AH = A'H, pour TOUT point I choisi.", font_size=18, color=YELLOW),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.14)
        demo_texte.next_to(demo_schema, RIGHT, buff=0.5)

        with self.voiceover(
            text=(
                "Voici la démonstration complète. Soit H le pied de la "
                "perpendiculaire abaissée de A sur le plan du miroir, et I "
                "un point d'incidence quelconque du miroir. Comparons les "
                "triangles A, I, H et A prime, I, H. L'angle en H vaut "
                "quatre-vingt-dix degrés dans les deux triangles, car A "
                "prime est construit sur la perpendiculaire au miroir "
                "passant par A. Le côté I H est commun aux deux triangles. "
                "Et l'angle A, I, H est égal à l'angle A prime, I, H, "
                "précisément parce que la loi de la réflexion impose i'1 "
                "égal i1. Les deux triangles ont donc un côté et les deux "
                "angles adjacents égaux : ils sont isométriques. On en "
                "déduit que A H est égal à A prime H, et ce, quel que soit "
                "le point I choisi sur le miroir. Le point A prime est "
                "donc bien unique, indépendant du rayon choisi, et "
                "symétrique de A par rapport au miroir."
            )
        ) as tracker:
            self.play(Create(miroir_d))
            self.play(Create(seg_AH), FadeIn(dotA), FadeIn(dotH), Write(lA), Write(lH))
            self.play(Create(seg_AI), FadeIn(dotI), Write(lI))
            self.play(Create(seg_IH))
            self.play(Create(seg_HAp), Create(seg_IAp), FadeIn(dotAp), Write(lAp))
            self.play(Write(demo_texte))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(demo_schema), FadeOut(demo_texte))

        # --- À retenir --------------------------------------------------------------
        retenir = essentiel_box(
            VGroup(
                Text("À retenir", font_size=24, weight="BOLD"),
                Text("A' est le symétrique de A par rapport au plan du miroir.", font_size=20),
                Text("Démonstration : triangles AIH et A'IH isométriques,", font_size=20),
                Text("via l'angle droit en H, le côté IH commun, et i1'=i1.", font_size=20),
            ).arrange(DOWN, buff=0.2),
            box_width=12.0,
        )
        retenir.next_to(titre, DOWN, buff=0.35)

        with self.voiceover(
            text=(
                "Retenons l'essentiel : l'image A prime d'un point A par "
                "un miroir plan est son symétrique par rapport au plan du "
                "miroir. La démonstration repose sur l'isométrie des "
                "triangles A, I, H et A prime, I, H, grâce à l'angle droit "
                "en H, au côté I H commun, et à l'égalité i'1 égale i1."
            )
        ) as tracker:
            self.play(FadeIn(retenir))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(retenir))

        # --- Piège à éviter ------------------------------------------------------------
        piege = warning_box(
            VGroup(
                Text("• L'image A' est VIRTUELLE : aucune lumière ne passe", font_size=20),
                Text("   réellement par A'. On ne peut pas la recueillir sur", font_size=20),
                Text("   un écran, seul un œil (ou une caméra) peut la voir.", font_size=20),
                Text("• Ne pas confondre avec une image RÉELLE, obtenue par", font_size=20),
                Text("   des lentilles ou miroirs courbes.", font_size=20),
            ).arrange(DOWN, aligned_edge=LEFT, buff=0.16),
            box_width=12.0,
        )
        piege.next_to(titre, DOWN, buff=0.35)

        with self.voiceover(
            text=(
                "Piège à éviter : l'image A prime donnée par un miroir "
                "plan est toujours virtuelle. Aucune lumière ne passe "
                "réellement par ce point, on ne peut donc pas la recueillir "
                "sur un écran, seul un œil ou une caméra peut la "
                "percevoir. Ne la confondez pas avec une image réelle, que "
                "l'on obtient avec des lentilles ou des miroirs courbes."
            )
        ) as tracker:
            self.play(FadeIn(piege))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(piege), FadeOut(titre))
