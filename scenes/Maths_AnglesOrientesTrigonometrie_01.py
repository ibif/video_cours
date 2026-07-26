"""
scenes/Maths_AnglesOrientesTrigonometrie_01.py — Chapitre « Angles orientés
et trigonométrie » (1ereC, Maths), scène 01.

§ Mise en situation (éolienne, canon arroseur, fromager), cercle
trigonométrique (sens direct/indirect), définition du radian, conversion
degrés/radians, longueur d'un arc, exemple résolu (roue de charrette).
Source : 1ereC/Maths.pdf, chapitre 2, pages 14-27.
"""

import textwrap

from manim import (
    DOWN,
    LEFT,
    ORIGIN,
    RIGHT,
    UP,
    WHITE,
    YELLOW,
    GREEN,
    GRAY_B,
    Arc,
    Circle,
    Dot,
    FadeIn,
    FadeOut,
    Line,
    MathTex,
    Text,
    VGroup,
    Write,
    config,
)

from shapes.base_scene import NotionScene
from shapes.boxes import definition_box, example_box, property_box, scene_title


def _wrap(text: str, width: int = 56) -> str:
    return "\n".join(textwrap.fill(line, width=width) for line in text.split("\n"))


def _fit(mobject, top_y):
    bas_visible = -config.frame_height / 2 + 0.25
    hauteur_dispo = top_y - bas_visible
    if mobject.height > hauteur_dispo:
        mobject.scale(hauteur_dispo / mobject.height, about_point=mobject.get_top())
    return mobject


def _cercle_axes(radius=1.5):
    """Cercle trigonométrique nu : axes, cercle, points O, I, J."""
    axe_x = Line(LEFT * radius * 1.2, RIGHT * radius * 1.2, color=GRAY_B, stroke_width=1)
    axe_y = Line(DOWN * radius * 1.2, UP * radius * 1.2, color=GRAY_B, stroke_width=1)
    cercle = Circle(radius=radius, color=WHITE, stroke_width=2)
    O = Dot(ORIGIN, color=WHITE, radius=0.04)
    I = Dot(RIGHT * radius, color=YELLOW, radius=0.05)
    J = Dot(UP * radius, color=YELLOW, radius=0.05)
    label_O = MathTex("O", font_size=24, color=WHITE).next_to(O, DOWN + LEFT, buff=0.08)
    label_I = MathTex("I", font_size=24, color=YELLOW).next_to(I, RIGHT, buff=0.08)
    label_J = MathTex("J", font_size=24, color=YELLOW).next_to(J, UP, buff=0.08)
    return VGroup(axe_x, axe_y, cercle, O, I, J, label_O, label_I, label_J)


class IntroductionCercleTrigonometriqueRadian(NotionScene):
    def construct(self):
        titre = scene_title("2. Angles orientés et trigonométrie")
        titre.scale(0.55)
        titre.to_edge(UP)

        # --- Énoncé : mise en situation -----------------------------------
        mise_en_situation = Text(
            _wrap(
                "Les pales d'une éolienne tournent autour d'un axe, le jet "
                "d'un canon arroseur balaie un secteur en pivotant, et la "
                "meule d'un fromager tourne pour affiner le fromage. Dans "
                "chaque cas, un objet tourne d'un certain angle, dans un "
                "sens précis. Comment mesurer précisément ces rotations, "
                "avec ou sans tenir compte du sens ?",
                width=56,
            ),
            font_size=24,
            color=WHITE,
        )
        mise_en_situation.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Les pales d'une éolienne tournent autour d'un axe, le jet "
                "d'un canon arroseur balaie un secteur en pivotant "
                "régulièrement, et la meule d'un fromager tourne pour "
                "affiner la pâte. Dans chaque cas, un objet tourne d'un "
                "certain angle, dans un sens précis. Comment mesurer "
                "précisément ces rotations, en tenant compte du sens de "
                "rotation ? C'est tout l'objet de ce chapitre sur les "
                "angles orientés et la trigonométrie."
            )
        ) as tracker:
            self.play(Write(titre))
            self.play(FadeIn(mise_en_situation))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(mise_en_situation))

        # --- Raisonnement : le cercle trigonométrique ----------------------
        def_cercle_fig = _cercle_axes(radius=1.3)
        arc_direct = Arc(radius=1.3, start_angle=0, angle=2.4, color=GREEN, stroke_width=5)
        fleche_direct = MathTex(r"\curvearrowleft", color=GREEN, font_size=34)
        fleche_direct.move_to(def_cercle_fig[2].point_at_angle(1.9))
        groupe_fig = VGroup(def_cercle_fig, arc_direct, fleche_direct)

        def_cercle = definition_box(
            VGroup(
                Text("Cercle trigonométrique", font_size=25, weight="BOLD"),
                Text(
                    _wrap(
                        "Cercle de rayon 1, de centre O, muni d'un sens de "
                        "parcours positif appelé sens direct (sens "
                        "trigonométrique, contraire des aiguilles d'une "
                        "montre). Le sens contraire est le sens indirect.",
                        width=42,
                    ),
                    font_size=21,
                ),
            ).arrange(DOWN, buff=0.25),
            box_width=6.6,
        )
        def_cercle.to_edge(LEFT, buff=0.5).shift(DOWN * 0.3)
        groupe_fig.next_to(def_cercle, RIGHT, buff=0.6)

        with self.voiceover(
            text=(
                "On munit le plan d'un cercle trigonométrique : un cercle "
                "de rayon un, de centre O, sur lequel on choisit un sens de "
                "parcours positif, appelé sens direct, ou sens "
                "trigonométrique : c'est le sens contraire des aiguilles "
                "d'une montre. Le sens contraire, celui des aiguilles d'une "
                "montre, est appelé sens indirect."
            )
        ) as tracker:
            self.play(FadeIn(def_cercle))
            self.play(FadeIn(groupe_fig[0]), Write(groupe_fig[1]), FadeIn(groupe_fig[2]))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(def_cercle), FadeOut(groupe_fig))

        # --- Le radian -------------------------------------------------------
        cercle_rad = _cercle_axes(radius=1.3)
        arc_rad = Arc(radius=1.3, start_angle=0, angle=1.0, color=YELLOW, stroke_width=5)
        rayon_ref = Line(ORIGIN, cercle_rad[2].point_at_angle(1.0), color=YELLOW, stroke_width=3)
        label_arc = MathTex(r"\ell = R", font_size=24, color=YELLOW)
        label_arc.move_to(cercle_rad[2].point_at_angle(0.5) * 1.28)
        fig_radian = VGroup(cercle_rad, arc_rad, rayon_ref, label_arc)

        def_radian = definition_box(
            VGroup(
                Text("Le radian (rad)", font_size=25, weight="BOLD"),
                Text(
                    _wrap(
                        "Un angle au centre mesure 1 radian lorsqu'il "
                        "intercepte, sur un cercle, un arc de longueur "
                        "égale au rayon de ce cercle.",
                        width=42,
                    ),
                    font_size=21,
                ),
            ).arrange(DOWN, buff=0.25),
            box_width=6.6,
        )
        def_radian.to_edge(LEFT, buff=0.5).shift(DOWN * 0.3)
        fig_radian.next_to(def_radian, RIGHT, buff=0.6)

        with self.voiceover(
            text=(
                "Pour mesurer un angle, on utilise souvent le degré, mais "
                "en trigonométrie on préfère une unité liée directement au "
                "cercle : le radian. Un angle au centre mesure un radian "
                "lorsqu'il intercepte, sur le cercle, un arc de longueur "
                "égale au rayon de ce cercle."
            )
        ) as tracker:
            self.play(FadeIn(def_radian))
            self.play(FadeIn(fig_radian))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(def_radian), FadeOut(fig_radian))

        # --- Correspondance pi rad = 180 degres + tableau -------------------
        correspondance = property_box(
            MathTex(r"\pi \text{ rad} = 180^{\circ}", font_size=32, color="#1A1A1A"),
            box_width=6,
        )
        correspondance.to_edge(UP, buff=1.3).shift(LEFT * 3.6)

        with self.voiceover(
            text=(
                "La correspondance fondamentale entre les deux unités est "
                "la suivante : pi radians valent cent quatre-vingts degrés. "
                "On en déduit un tableau de conversion pour les angles "
                "usuels."
            )
        ) as tracker:
            self.play(FadeIn(correspondance))
            self.wait(tracker.get_remaining_duration())

        degres = ["0°", "30°", "45°", "60°", "90°", "180°", "360°"]
        radians = [r"0", r"\dfrac{\pi}{6}", r"\dfrac{\pi}{4}", r"\dfrac{\pi}{3}", r"\dfrac{\pi}{2}", r"\pi", r"2\pi"]
        col_deg = VGroup(*[Text(d, font_size=22, color=WHITE) for d in degres]).arrange(RIGHT, buff=0.55)
        col_rad = VGroup(*[MathTex(r, font_size=24, color=YELLOW) for r in radians]).arrange(RIGHT, buff=0.55)
        for d_mob, r_mob in zip(col_deg, col_rad):
            r_mob.move_to([d_mob.get_center()[0], 0, 0])
        col_rad.next_to(col_deg, DOWN, buff=0.35)
        for d_mob, r_mob in zip(col_deg, col_rad):
            r_mob.move_to([d_mob.get_center()[0], r_mob.get_center()[1], 0])
        ligne_sep = Line(col_deg.get_left() + LEFT * 0.15, col_deg.get_right() + RIGHT * 0.15, color=GRAY_B, stroke_width=1)
        ligne_sep.next_to(col_deg, DOWN, buff=0.15)
        tableau = VGroup(col_deg, ligne_sep, col_rad)
        tableau.next_to(correspondance, DOWN, buff=0.5)
        tableau.scale(0.95)

        with self.voiceover(
            text=(
                "Zéro degré correspond à zéro radian ; trente degrés à pi "
                "sur six ; quarante-cinq degrés à pi sur quatre ; soixante "
                "degrés à pi sur trois ; quatre-vingt-dix degrés à pi sur "
                "deux ; cent quatre-vingts degrés à pi ; et trois cent "
                "soixante degrés, le tour complet, à deux pi."
            )
        ) as tracker:
            self.play(Write(tableau))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(correspondance), FadeOut(tableau))

        # --- Longueur d'un arc ------------------------------------------------
        longueur_arc = property_box(
            VGroup(
                Text("Longueur d'un arc de cercle", font_size=24, weight="BOLD"),
                MathTex(r"\ell = R\alpha", font_size=30),
                Text(
                    _wrap("R : rayon du cercle, en mètre ; α : angle au centre, en radian.", width=44),
                    font_size=20,
                ),
            ).arrange(DOWN, buff=0.25),
            box_width=8,
        )
        longueur_arc.next_to(titre, DOWN, buff=0.6)

        with self.voiceover(
            text=(
                "Cette définition du radian donne immédiatement une "
                "formule très utile : la longueur d'un arc de cercle "
                "intercepté par un angle au centre alpha, exprimé en "
                "radians, vaut ℓ égale R fois alpha, où R est le rayon du "
                "cercle."
            )
        ) as tracker:
            self.play(FadeIn(longueur_arc))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(longueur_arc))

        # --- Exemple résolu 1 : roue de charrette ----------------------------
        exemple = example_box(
            VGroup(
                Text(
                    _wrap(
                        "Une roue de charrette a un rayon R = 35 cm. Un "
                        "rayon de la roue tourne d'un angle α = 2π/5 rad. "
                        "Quelle est la longueur de l'arc parcouru par un "
                        "point du bord de la roue ?",
                        width=48,
                    ),
                    font_size=21,
                ),
                MathTex(
                    r"\ell = R\alpha = 35 \times \dfrac{2\pi}{5} = 14\pi \approx 43{,}98 \text{ cm}",
                    font_size=24,
                ),
            ).arrange(DOWN, buff=0.3),
            box_width=9.5,
        )
        exemple.next_to(titre, DOWN, buff=0.55)

        with self.voiceover(
            text=(
                "Exemple résolu. Une roue de charrette a un rayon R égal à "
                "trente-cinq centimètres. Un rayon de la roue tourne d'un "
                "angle alpha égal à deux pi cinquièmes de radian. Quelle "
                "est la longueur de l'arc parcouru par un point du bord de "
                "la roue ? On applique directement la formule : ℓ égale R "
                "alpha, soit trente-cinq fois deux pi sur cinq, c'est-à-dire "
                "quatorze pi, environ quarante-trois virgule quatre-vingt-"
                "dix-huit centimètres."
            )
        ) as tracker:
            self.play(FadeIn(exemple))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(exemple), FadeOut(titre))
