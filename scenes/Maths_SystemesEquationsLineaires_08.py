"""
scenes/Maths_SystemesEquationsLineaires_08.py — Chapitre 13 « Systèmes
d'équations linéaires dans ℝ² et ℝ³ » (1ereC, Maths), scène 08.

§ Interprétation géométrique dans l'espace : équation cartésienne d'un
plan ax+by+cz=d, résoudre un système 3×3 = chercher l'intersection de
trois plans. Les 3 configurations principales (sécants en un point /
strictement parallèles / droite commune), et le piège du « prisme »
(plans sécants deux à deux, sans point commun aux trois).
Source : 1ereC/Maths.pdf, chapitre 13, pages 154-164.
"""

import textwrap

from manim import (
    DOWN,
    LEFT,
    RIGHT,
    UP,
    Dot,
    FadeIn,
    FadeOut,
    Create,
    MathTex,
    Polygon,
    Text,
    VGroup,
    Write,
    YELLOW,
)

from shapes.base_scene import NotionScene
from shapes.boxes import definition_box, property_box, scene_title, warning_box


def _wrap(text: str, width: int = 56) -> str:
    return "\n".join(textwrap.fill(line, width=width) for line in text.split("\n"))


def _plan(color, center, tilt=0.5, width=3.2, height=1.9, opacity=0.35):
    """Parallélogramme suggérant un plan vu en perspective cavalière."""
    pts = [
        center + LEFT * width / 2 + DOWN * height / 2,
        center + RIGHT * width / 2 + DOWN * height / 2 + RIGHT * tilt,
        center + RIGHT * width / 2 + UP * height / 2 + RIGHT * tilt,
        center + LEFT * width / 2 + UP * height / 2,
    ]
    return Polygon(*pts, fill_color=color, fill_opacity=opacity, stroke_color=color, stroke_width=2.5)


class InterpretationGeometriqueEspace(NotionScene):
    def construct(self):
        titre = scene_title("Interprétation géométrique — Intersection de plans")
        titre.scale(0.46)
        titre.to_edge(UP)
        self.play(Write(titre))

        # --- Énoncé : équation cartésienne d'un plan ------------------------------
        def_plan = definition_box(
            VGroup(
                Text("Équation cartésienne d'un plan", font_size=23, weight="BOLD"),
                MathTex(r"ax+by+cz=d \qquad (a,b,c) \neq (0,0,0)", font_size=27),
                Text(
                    _wrap(
                        "Chaque équation d'un système 3×3 représente donc "
                        "UN PLAN de l'espace.",
                        width=46,
                    ),
                    font_size=21,
                ),
            ).arrange(DOWN, buff=0.26),
            box_width=11.8,
        )
        def_plan.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Dans l'espace, une équation de la forme a x plus b y plus "
                "c z égale d, où a, b, c ne sont pas tous nuls, représente "
                "un plan. Chaque équation d'un système 3×3 correspond donc "
                "à un plan de l'espace : résoudre le système, c'est "
                "chercher les points communs à ces trois plans, c'est-à "
                "dire leur intersection."
            )
        ) as tracker:
            self.play(FadeIn(def_plan))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(def_plan))

        # --- Raisonnement : les 3 configurations, une par une ----------------------
        p1a = _plan("#DE7C1F", LEFT * 3.5 + DOWN * 0.2)
        p2a = _plan("#288073", LEFT * 3.5 + DOWN * 0.2 + RIGHT * 0.4 + UP * 0.3)
        p3a = _plan("#1E5FA8", LEFT * 3.5 + DOWN * 0.2 + LEFT * 0.3 + UP * 0.5)
        point_commun = Dot(LEFT * 3.5 + DOWN * 0.2, color=YELLOW, radius=0.08)
        label1 = Text("sécants en un point", font_size=18).next_to(
            VGroup(p1a, p2a, p3a), DOWN, buff=0.3
        )
        config1 = VGroup(p1a, p2a, p3a, point_commun, label1)

        p1b = _plan("#DE7C1F", RIGHT * 3.5 + UP * 0.9)
        p2b = _plan("#288073", RIGHT * 3.5)
        p3b = _plan("#1E5FA8", RIGHT * 3.5 + DOWN * 0.9)
        label2 = Text("strictement parallèles", font_size=18).next_to(
            VGroup(p1b, p2b, p3b), DOWN, buff=0.3
        )
        config2 = VGroup(p1b, p2b, p3b, label2)

        with self.voiceover(
            text=(
                "Regardons trois configurations possibles. À gauche, les "
                "trois plans se coupent tous en un seul et même point : "
                "c'est le cas où le système a une solution unique, D non "
                "nul, comme trois murs et le sol qui se rejoignent dans un "
                "coin de pièce. À droite, les trois plans sont strictement "
                "parallèles entre eux, comme les étages d'un immeuble : ils "
                "n'ont aucun point commun, le système n'a aucune solution."
            )
        ) as tracker:
            self.play(Create(config1))
            self.play(Create(config2))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(config1), FadeOut(config2))

        p1c = _plan("#DE7C1F", DOWN * 0.2, tilt=1.0, width=3.4)
        p2c = _plan("#288073", DOWN * 0.2, tilt=-1.0, width=3.4)
        p3c = _plan("#1E5FA8", DOWN * 0.2, tilt=0.0, width=3.4)
        droite_commune = Polygon(
            DOWN * 0.2 + DOWN * 1.5,
            DOWN * 0.2 + UP * 1.5,
            fill_opacity=0,
            stroke_color=YELLOW,
            stroke_width=5,
        )
        label3 = Text("les 3 plans partagent UNE MÊME droite", font_size=18).next_to(
            VGroup(p1c, p2c, p3c), DOWN, buff=0.3
        )
        config3 = VGroup(p1c, p2c, p3c, droite_commune, label3)
        config3.next_to(titre, DOWN, buff=0.6)

        with self.voiceover(
            text=(
                "Troisième configuration, comme les pages d'un livre "
                "ouvert autour de sa reliure : les trois plans, distincts, "
                "partagent une même droite commune. Le système a alors une "
                "infinité de solutions, tous les points de cette droite, "
                "obtenue avec un seul paramètre lors du pivot de Gauss."
            )
        ) as tracker:
            self.play(Create(config3))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(config3))

        # --- À retenir : tableau de correspondance ----------------------------------
        recap = property_box(
            VGroup(
                Text("Résoudre un système 3×3 = intersecter 3 plans", font_size=22, weight="BOLD"),
                Text("• D≠0 → point unique", font_size=20),
                Text("• D=0, Gauss → 0=k≠0 → aucun point commun", font_size=20),
                Text("• D=0, Gauss → 1 paramètre → droite commune", font_size=20),
                Text("• D=0, Gauss → 2 paramètres → plans confondus", font_size=20),
            ).arrange(DOWN, aligned_edge=LEFT, buff=0.18),
            box_width=11.8,
        )
        recap.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Résumons la correspondance. Résoudre un système de trois "
                "équations à trois inconnues revient toujours à "
                "intersecter trois plans. Si D est non nul, un point "
                "unique. Si D est nul et que le pivot de Gauss aboutit à "
                "une égalité fausse, aucun point commun. S'il reste un "
                "paramètre, une droite commune. S'il en reste deux, les "
                "trois plans sont en réalité confondus."
            )
        ) as tracker:
            self.play(FadeIn(recap))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(recap))

        # --- Piège à éviter : le cas du « prisme » ----------------------------------
        piege = warning_box(
            Text(
                "Piège : D=0 avec « aucune solution » ne signifie pas toujours\n"
                "que les plans sont parallèles ! Ils peuvent se couper deux à\n"
                "deux selon 3 droites parallèles DISTINCTES (comme un prisme\n"
                "triangulaire) : aucun point n'appartient aux 3 plans à la fois.",
                font_size=21,
            ),
            box_width=12.3,
        )
        piege.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Piège à connaître : quand D est nul et que le système n'a "
                "aucune solution, cela ne signifie pas forcément que les "
                "trois plans sont parallèles entre eux. Ils peuvent aussi "
                "se couper deux à deux selon trois droites parallèles mais "
                "distinctes, comme les trois faces latérales d'un prisme "
                "triangulaire : aucun point n'appartient alors aux trois "
                "plans à la fois, bien qu'aucun couple de plans ne soit "
                "parallèle."
            )
        ) as tracker:
            self.play(FadeIn(piege))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(piege), FadeOut(titre))
