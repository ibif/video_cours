"""
scenes/SVT_TectoniquePlaques_12.py — Chapitre 8 (1ereC, SVT), scène 12.

V. Les moteurs des mouvements des plaques : la convection mantellique
(chaleur interne, radioactivité, tapis roulant), la poussée des dorsales
(ridge push), la traction des plaques plongeantes (slab pull, force
dominante, 7-10 cm/an vs ~2 cm/an), les forces résistantes + point clé
méthode "la chaleur interne est le moteur ultime". Source : 1ereC/SVT.pdf,
page 92.
"""

import textwrap

from manim import (
    BLUE_D,
    DOWN,
    LEFT,
    ORANGE,
    RED,
    RIGHT,
    UP,
    WHITE,
    YELLOW,
    Arrow,
    Create,
    CurvedArrow,
    FadeIn,
    FadeOut,
    Polygon,
    Rectangle,
    Text,
    VGroup,
    Write,
)

from shapes.base_scene import NotionScene
from shapes.boxes import method_box, scene_title


def _wrap(text: str, width: int = 56) -> str:
    return "\n".join(textwrap.fill(line, width=width) for line in text.split("\n"))


def _bullets(items, font_size=24, color=WHITE, width=54):
    lines = VGroup(
        *[Text(f"• {_wrap(it, width=width)}", font_size=font_size, color=color) for it in items]
    )
    lines.arrange(DOWN, aligned_edge=LEFT, buff=0.22)
    return lines


class MoteursDesMouvementsDePlaques(NotionScene):
    def construct(self):
        titre = scene_title("V. Les moteurs des mouvements des plaques")
        titre.scale(0.58)
        titre.to_edge(UP)
        self.play(Write(titre))

        # --- Énoncé : la question -------------------------------------------
        question = Text(
            "Pourquoi les plaques bougent-elles ? Trois mécanismes complémentaires.",
            font_size=25,
            color=WHITE,
        )
        question.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Pourquoi les plaques bougent-elles ? Trois mécanismes "
                "complémentaires sont invoqués pour l'expliquer."
            )
        ) as tracker:
            self.play(FadeIn(question))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(question))

        # --- Animation du raisonnement : la convection mantellique ------------
        entete_conv = Text("1. La convection mantellique", font_size=25, color=YELLOW, weight="BOLD")
        entete_conv.next_to(titre, DOWN, buff=0.5)

        manteau = Rectangle(width=8.0, height=2.2, fill_color=RED, fill_opacity=0.3, stroke_color=WHITE, stroke_width=1)
        litho_conv = Rectangle(width=8.0, height=0.4, fill_color=ORANGE, fill_opacity=0.8, stroke_width=0)
        litho_conv.next_to(manteau, UP, buff=0)

        fleche_monte = CurvedArrow(start_point=[-1.0, -1.0, 0], end_point=[-1.0, 1.0, 0], color=RED, angle=1.2)
        fleche_descend = CurvedArrow(start_point=[1.0, 1.0, 0], end_point=[1.0, -1.0, 0], color=BLUE_D, angle=1.2)

        label_monte = Text("chaud, monte", font_size=14, color=RED).next_to(fleche_monte, LEFT, buff=0.15)
        label_descend = Text("froid, descend", font_size=14, color=BLUE_D).next_to(fleche_descend, RIGHT, buff=0.15)

        schema_conv = VGroup(manteau, litho_conv, fleche_monte, fleche_descend, label_monte, label_descend)
        schema_conv.next_to(entete_conv, DOWN, buff=0.35)

        with self.voiceover(
            text=(
                "Premier mécanisme : la convection mantellique. La chaleur "
                "interne de la Terre, produite par la désintégration "
                "radioactive de l'uranium, du thorium et du potassium, "
                "complétée par une chaleur fossile, engendre des mouvements "
                "de convection dans le manteau. La matière chaude monte, la "
                "matière froide descend. Ces courants entraînent la base "
                "des plaques par friction, comme un tapis roulant."
            )
        ) as tracker:
            self.play(FadeIn(entete_conv))
            self.play(FadeIn(manteau), FadeIn(litho_conv))
            self.play(Create(fleche_monte), FadeIn(label_monte))
            self.play(Create(fleche_descend), FadeIn(label_descend))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(entete_conv), FadeOut(schema_conv))

        # --- Exemple traité : ridge push et slab pull --------------------------
        entete_forces = Text("2. Poussée des dorsales et 3. traction des plaques", font_size=21, color=YELLOW, weight="BOLD")
        entete_forces.next_to(titre, DOWN, buff=0.5)

        forces = _bullets(
            [
                "Poussée des dorsales (ridge push) : la dorsale est "
                "surélevée ; la lithosphère qui s'y forme glisse "
                "gravitairement de part et d'autre de l'axe.",
                "Traction des plaques plongeantes (slab pull) : la "
                "lithosphère océanique, froide et dense, plonge dans le "
                "manteau et tire derrière elle le reste de la plaque. "
                "C'est la force DOMINANTE.",
                "Plaques bordées de subduction (pacifique, Nazca) : "
                "rapides, 7 à 10 cm/an. Plaques sans subduction "
                "(africaine) : lentes, ~2 cm/an.",
            ],
            font_size=20,
            width=54,
        )
        forces.next_to(entete_forces, DOWN, buff=0.3)

        with self.voiceover(
            text=(
                "Deuxième mécanisme : la poussée des dorsales, ou ridge "
                "push. La dorsale est surélevée ; la lithosphère qui s'y "
                "forme glisse gravitairement de part et d'autre de l'axe : "
                "la pesanteur pousse littéralement la plaque à s'écarter "
                "de la dorsale. Troisième mécanisme, le plus important : la "
                "traction des plaques plongeantes, ou slab pull. La "
                "lithosphère océanique, froide et dense, plonge dans le "
                "manteau et tire derrière elle le reste de la plaque. "
                "C'est la force dominante : les plaques bordées de zones "
                "de subduction, comme la pacifique ou la plaque de Nazca, "
                "sont les plus rapides, sept à dix centimètres par an, "
                "tandis que les plaques sans subduction, comme "
                "l'africaine, sont lentes, environ deux centimètres par "
                "an."
            )
        ) as tracker:
            self.play(FadeIn(entete_forces))
            self.play(FadeIn(forces))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(entete_forces), FadeOut(forces))

        # --- Schéma : ridge push + slab pull sur une coupe de plaque ----------
        litho_h = Rectangle(width=9.0, height=0.4, fill_color=ORANGE, fill_opacity=0.8, stroke_color=WHITE, stroke_width=1)
        litho_h.move_to([0, 0.3, 0])
        dorsale_h = Polygon([-0.4, 0.1, 0], [0.4, 0.1, 0], [0.2, 0.7, 0], [-0.2, 0.7, 0], fill_color=RED, fill_opacity=0.85, stroke_width=0.5, stroke_color=WHITE)
        dorsale_h.move_to([-3.0, 0.4, 0])
        plaque_plongeante = Polygon([3.5, 0.1, 0], [4.4, 0.1, 0], [4.4, -2.0, 0], [3.5, -1.5, 0], fill_color=ORANGE, fill_opacity=0.8, stroke_width=0.5, stroke_color=WHITE)

        fleche_ridge = Arrow(start=[-3.0, -0.3, 0], end=[-1.0, -0.3, 0], color=YELLOW, buff=0, stroke_width=4)
        label_ridge = Text("ridge push", font_size=14, color=YELLOW).next_to(fleche_ridge, DOWN, buff=0.1)

        fleche_slab = Arrow(start=[3.0, -0.3, 0], end=[4.0, -1.2, 0], color=RED, buff=0, stroke_width=4)
        label_slab = Text("slab pull", font_size=14, color=RED).next_to(fleche_slab, RIGHT, buff=0.1)

        schema_forces = VGroup(litho_h, dorsale_h, plaque_plongeante, fleche_ridge, label_ridge, fleche_slab, label_slab)
        schema_forces.next_to(titre, DOWN, buff=0.6)

        with self.voiceover(
            text=(
                "Sur ce schéma, on visualise les deux forces : la poussée "
                "gravitaire depuis la dorsale surélevée, à gauche, et la "
                "traction, bien plus puissante, exercée par la plaque qui "
                "plonge dans une zone de subduction, à droite. À cela "
                "s'ajoutent des forces résistantes : les frottements à la "
                "base de la lithosphère et la résistance du manteau à la "
                "plongée, qui freinent les mouvements."
            )
        ) as tracker:
            self.play(FadeIn(litho_h), FadeIn(dorsale_h), FadeIn(plaque_plongeante))
            self.play(Create(fleche_ridge), FadeIn(label_ridge))
            self.play(Create(fleche_slab), FadeIn(label_slab))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(schema_forces))

        # --- À retenir : point clé méthode --------------------------------------
        point_cle = method_box(
            Text(
                _wrap(
                    "Point clé : la chaleur interne de la Terre est le "
                    "moteur ultime ; la convection mantellique, la poussée "
                    "des dorsales et surtout la traction des plaques "
                    "plongeantes en sont les expressions mécaniques.",
                    width=54,
                ),
                font_size=22,
            ),
            box_width=12.0,
        )
        point_cle.next_to(titre, DOWN, buff=0.55)

        with self.voiceover(
            text=(
                "Retenons ce point clé : la chaleur interne de la Terre est "
                "le moteur ultime de tout le système. La convection "
                "mantellique, la poussée des dorsales, et surtout la "
                "traction des plaques plongeantes, n'en sont que les "
                "expressions mécaniques, à la surface du globe."
            )
        ) as tracker:
            self.play(FadeIn(point_cle))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(point_cle), FadeOut(titre))
