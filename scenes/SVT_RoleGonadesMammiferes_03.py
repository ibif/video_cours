"""
scenes/SVT_RoleGonadesMammiferes_03.py — Chapitre 1 (1ereC, SVT), scène 03.

L'appareil reproducteur femelle : schéma simplifié (ovaires, trompes de
Fallope, utérus, col de l'utérus, vagin, vulve), trajet de l'ovule, tableau
des organes et de leur rôle. Source : 1ereC/SVT.pdf, pages 6-7.
"""

import textwrap

from manim import (
    DOWN,
    LEFT,
    RIGHT,
    UP,
    WHITE,
    YELLOW,
    Arc,
    Circle,
    Dot,
    FadeIn,
    FadeOut,
    Line,
    MoveAlongPath,
    Polygon,
    Rectangle,
    Text,
    VGroup,
    Write,
)

from shapes.base_scene import NotionScene
from shapes.boxes import definition_box, scene_title, warning_box


def _wrap(text: str, width: int = 56) -> str:
    return "\n".join(textwrap.fill(line, width=width) for line in text.split("\n"))


def _bullets(items, font_size=19, color=WHITE, width=48):
    lines = VGroup(
        *[Text(f"• {_wrap(it, width=width)}", font_size=font_size, color=color) for it in items]
    )
    lines.arrange(DOWN, aligned_edge=LEFT, buff=0.2)
    return lines


class AppareilReproducteurFemelle(NotionScene):
    def construct(self):
        titre = scene_title("1.3 — L'appareil reproducteur femelle")
        titre.scale(0.65)
        titre.to_edge(UP)

        # --- Énoncé : présentation générale ----------------------------------
        definition = definition_box(
            Text(
                _wrap(
                    "L'appareil reproducteur femelle est l'ensemble des "
                    "organes qui produisent l'ovule, accueillent la "
                    "fécondation, puis abritent le développement de "
                    "l'embryon.",
                    width=54,
                ),
                font_size=25,
            ),
            box_width=11.8,
        )
        definition.next_to(titre, DOWN, buff=0.55)

        with self.voiceover(
            text=(
                "L'appareil reproducteur femelle est l'ensemble des organes "
                "qui produisent l'ovule, accueillent la fécondation, puis "
                "abritent le développement de l'embryon. Découvrons ses "
                "différents organes sur un schéma simplifié."
            )
        ) as tracker:
            self.play(Write(titre))
            self.play(FadeIn(definition))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(definition))

        # --- Animation du raisonnement : construction du schéma --------------
        uterus = Polygon(
            [-1.1, 0.8, 0], [1.1, 0.8, 0], [0.35, -0.6, 0], [-0.35, -0.6, 0],
            color="#A42A5A", fill_opacity=0.8, stroke_width=2,
        )
        uterus.next_to(titre, DOWN, buff=0.9)
        uterus_lbl = Text("utérus", font_size=16, color=WHITE).move_to(uterus.get_center() + UP * 0.15)

        col = Rectangle(width=0.35, height=0.35, color="#288073", fill_opacity=0.85)
        col.next_to(uterus, DOWN, buff=0.0)
        col_lbl = Text("col de l'utérus", font_size=13, color=WHITE).next_to(col, LEFT, buff=0.15)

        vagin = Rectangle(width=0.55, height=1.1, color=WHITE, stroke_width=3)
        vagin.next_to(col, DOWN, buff=0.0)
        vagin_lbl = Text("vagin", font_size=15, color=WHITE).next_to(vagin, RIGHT, buff=0.15)

        vulve = Arc(radius=0.3, angle=3.14, start_angle=3.9, color="#DE7C1F", stroke_width=5)
        vulve.next_to(vagin, DOWN, buff=-0.05)
        vulve_lbl = Text("vulve", font_size=14, color=WHITE).next_to(vulve, DOWN, buff=0.15)

        ovaire_g = Circle(radius=0.35, color="#1E5FA8", fill_opacity=0.85)
        ovaire_g.next_to(uterus, LEFT, buff=0.9).shift(UP * 0.1)
        ovaire_g_lbl = Text("ovaire", font_size=14, color=WHITE).next_to(ovaire_g, LEFT, buff=0.1)

        ovaire_d = Circle(radius=0.35, color="#1E5FA8", fill_opacity=0.85)
        ovaire_d.next_to(uterus, RIGHT, buff=0.9).shift(UP * 0.1)
        ovaire_d_lbl = Text("ovaire", font_size=14, color=WHITE).next_to(ovaire_d, RIGHT, buff=0.1)

        trompe_g = Arc(radius=1.0, angle=-1.5, start_angle=3.0, color="#DE7C1F", stroke_width=4)
        trompe_g.move_to((ovaire_g.get_center() + uterus.get_top()) / 2 + LEFT * 0.1 + UP * 0.3)
        trompe_d = Arc(radius=1.0, angle=1.5, start_angle=-0.5, color="#DE7C1F", stroke_width=4)
        trompe_d.move_to((ovaire_d.get_center() + uterus.get_top()) / 2 + RIGHT * 0.1 + UP * 0.3)
        trompes_lbl = Text("trompes de Fallope", font_size=14, color=YELLOW).next_to(
            VGroup(trompe_g, trompe_d), UP, buff=0.15
        )

        schema = VGroup(
            ovaire_g, ovaire_g_lbl, ovaire_d, ovaire_d_lbl,
            trompe_g, trompe_d, trompes_lbl,
            uterus, uterus_lbl,
            col, col_lbl,
            vagin, vagin_lbl,
            vulve, vulve_lbl,
        )
        schema.move_to(schema.get_center()).next_to(titre, DOWN, buff=0.6)

        with self.voiceover(
            text=(
                "De part et d'autre, les deux ovaires produisent l'ovule. "
                "Juste au-dessus de chacun, une trompe de Fallope, ou "
                "oviducte, capte l'ovule libéré : c'est là que la "
                "fécondation a lieu. Les deux trompes débouchent dans "
                "l'utérus, un organe musculaire creux destiné à accueillir "
                "l'embryon. En dessous, le col de l'utérus s'ouvre sur le "
                "vagin, le canal reliant l'utérus à l'extérieur, qui "
                "débouche lui-même sur la vulve, les organes génitaux "
                "externes."
            )
        ) as tracker:
            self.play(FadeIn(ovaire_g), FadeIn(ovaire_g_lbl), FadeIn(ovaire_d), FadeIn(ovaire_d_lbl))
            self.play(FadeIn(trompe_g), FadeIn(trompe_d), FadeIn(trompes_lbl))
            self.play(FadeIn(uterus), FadeIn(uterus_lbl))
            self.play(FadeIn(col), FadeIn(col_lbl))
            self.play(FadeIn(vagin), FadeIn(vagin_lbl))
            self.play(FadeIn(vulve), FadeIn(vulve_lbl))
            self.wait(tracker.get_remaining_duration())

        # --- Exemple traité : le trajet de l'ovule -----------------------------
        trajet_lbl = Text("Trajet d'un ovule", font_size=20, color=YELLOW, weight="BOLD")
        trajet_lbl.next_to(schema, DOWN, buff=0.35)

        point = Dot(color=YELLOW, radius=0.09)
        point.move_to(ovaire_d.get_center())

        chemin = VGroup(
            Line(ovaire_d.get_center(), trompe_d.get_start()),
            Line(trompe_d.get_start(), trompe_d.get_end()),
            Line(trompe_d.get_end(), uterus.get_center()),
        )

        with self.voiceover(
            text=(
                "Suivons le trajet d'un ovule : libéré par l'ovaire lors de "
                "l'ovulation, il est capté par la trompe de Fallope voisine, "
                "où la fécondation peut avoir lieu s'il rencontre un "
                "spermatozoïde, puis il descend vers l'utérus, où l'embryon "
                "pourra s'implanter et se développer."
            )
        ) as tracker:
            self.play(FadeIn(trajet_lbl), FadeIn(point))
            for segment in chemin:
                self.play(MoveAlongPath(point, segment), run_time=0.7)
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(schema), FadeOut(trajet_lbl), FadeOut(point))

        # --- À retenir : tableau des organes et de leur rôle -------------------
        entete_tab = Text("Tableau des organes", font_size=26, color=YELLOW, weight="BOLD")
        entete_tab.next_to(titre, DOWN, buff=0.5)

        tableau = _bullets(
            [
                "Ovaires : production des ovules et des hormones sexuelles",
                "Trompes de Fallope : captent l'ovule, lieu de la fécondation",
                "Utérus : accueille et nourrit l'embryon (paroi = endomètre)",
                "Vagin : canal reliant l'utérus à l'extérieur",
                "Vulve : organes génitaux externes",
            ],
            font_size=21,
            width=50,
        )
        tableau.next_to(entete_tab, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Résumons dans un tableau. Les ovaires produisent les ovules "
                "et les hormones sexuelles. Les trompes de Fallope captent "
                "l'ovule et sont le lieu de la fécondation. L'utérus "
                "accueille et nourrit l'embryon grâce à sa paroi, "
                "l'endomètre. Le vagin est le canal reliant l'utérus à "
                "l'extérieur. Enfin, la vulve regroupe les organes génitaux "
                "externes."
            )
        ) as tracker:
            self.play(FadeIn(entete_tab))
            self.play(FadeIn(tableau))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(entete_tab), FadeOut(tableau))

        # --- Piège à éviter ------------------------------------------------------
        piege = warning_box(
            Text(
                _wrap(
                    "Ne confonds pas la trompe de Fallope, lieu de la "
                    "FÉCONDATION, avec l'utérus, lieu de la NIDATION "
                    "(implantation) et du développement de l'embryon. Et "
                    "vagin ≠ vulve : le vagin est un canal interne, la "
                    "vulve désigne les organes externes.",
                    width=54,
                ),
                font_size=22,
            ),
            box_width=12.2,
        )
        piege.next_to(titre, DOWN, buff=0.55)

        with self.voiceover(
            text=(
                "Attention à ne pas confondre la trompe de Fallope, lieu de "
                "la fécondation, avec l'utérus, lieu de la nidation, "
                "c'est-à-dire de l'implantation, et du développement de "
                "l'embryon. Autre confusion fréquente : le vagin n'est pas "
                "la vulve. Le vagin est un canal interne, tandis que la "
                "vulve désigne les organes génitaux externes."
            )
        ) as tracker:
            self.play(FadeIn(piege))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(titre), FadeOut(piege))
