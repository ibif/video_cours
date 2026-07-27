"""
scenes/Physique_IntroductionOptiqueGeometrique_05.py — Chapitre 11
« Introduction à l'optique géométrique » (1ereC, Physique), scène 05.

§ 4 (partie 1). Ombre propre et ombre portée avec une source PONCTUELLE :
construction par rayons tangents à l'objet, contours nets.
Source : 1ereC/Physique.pdf, pages 108-116 (chapitre 11, § 4).
"""

import textwrap

from manim import (
    DOWN,
    LEFT,
    RIGHT,
    UP,
    BLUE,
    GRAY,
    WHITE,
    YELLOW,
    Circle,
    Dot,
    FadeIn,
    FadeOut,
    Line,
    Text,
    VGroup,
    Write,
)

from shapes.base_scene import NotionScene
from shapes.boxes import definition_box, essentiel_box, example_box, scene_title, warning_box


def _wrap(text: str, width: int = 56) -> str:
    return "\n".join(textwrap.fill(line, width=width) for line in text.split("\n"))


def _construction_ombre_ponctuelle() -> VGroup:
    """Source ponctuelle S, balle opaque, écran vertical à droite : les
    deux rayons tangents à la balle délimitent l'ombre propre (sur la
    balle) et l'ombre portée (sur l'écran)."""
    S = Dot(LEFT * 4.3, color=YELLOW, radius=0.09)
    label_S = Text("S", font_size=18, color=YELLOW).next_to(S, UP, buff=0.12)

    balle = Circle(radius=0.55, color=GRAY, fill_color=GRAY, fill_opacity=1.0)
    balle.move_to(LEFT * 1.2)

    ecran = Line(RIGHT * 2.6 + UP * 1.8, RIGHT * 2.6 + DOWN * 1.8, color=WHITE, stroke_width=4)
    label_ecran = Text("écran", font_size=16, color=WHITE).next_to(ecran, DOWN, buff=0.2)

    # Tangentes approximatives : haut et bas de la balle vers l'écran
    tangente_haut = Line(
        S.get_center(), balle.get_top() + UP * 0.02, color=YELLOW, stroke_width=2,
    )
    tangente_haut_prolongee = Line(
        balle.get_top(), balle.get_top() + (balle.get_top() - S.get_center()) * 2.3,
        color=YELLOW, stroke_width=2,
    )
    tangente_bas = Line(
        S.get_center(), balle.get_bottom() + DOWN * 0.02, color=YELLOW, stroke_width=2,
    )
    tangente_bas_prolongee = Line(
        balle.get_bottom(), balle.get_bottom() + (balle.get_bottom() - S.get_center()) * 2.3,
        color=YELLOW, stroke_width=2,
    )

    point_haut_ecran = tangente_haut_prolongee.get_end()
    point_bas_ecran = tangente_bas_prolongee.get_end()
    ombre_portee = Line(point_haut_ecran, point_bas_ecran, color=BLUE, stroke_width=6)
    label_ombre_portee = Text("ombre portée", font_size=15, color=BLUE)
    label_ombre_portee.next_to(ombre_portee, RIGHT, buff=0.15)

    ombre_propre = Line(
        balle.get_center() + RIGHT * 0.02 + UP * 0.5,
        balle.get_center() + RIGHT * 0.02 + DOWN * 0.5,
        color=BLUE, stroke_width=8,
    )
    label_ombre_propre = Text("ombre propre", font_size=14, color=BLUE)
    label_ombre_propre.next_to(balle, DOWN, buff=0.15)

    return VGroup(
        S, label_S, balle, ecran, label_ecran,
        tangente_haut, tangente_haut_prolongee, tangente_bas, tangente_bas_prolongee,
        ombre_portee, label_ombre_portee, ombre_propre, label_ombre_propre,
    )


class OmbrePropreOmbrePortee(NotionScene):
    def construct(self):
        titre = scene_title("Ombre propre et ombre portée")
        titre.scale(0.5)
        titre.to_edge(UP)

        # --- Énoncé -----------------------------------------------------------
        mise_en_situation = Text(
            _wrap(
                "Une balle éclairée par une petite lampe : une partie de "
                "la balle reste sombre, et une zone sombre apparaît aussi "
                "sur le mur derrière elle. Sont-ce les mêmes ombres ?",
                width=56,
            ),
            font_size=22,
        )
        mise_en_situation.next_to(titre, DOWN, buff=0.35)

        with self.voiceover(
            text=(
                "Une balle éclairée par une petite lampe : une partie de "
                "la balle reste sombre, et une zone sombre apparaît aussi "
                "sur le mur derrière elle. Sont-ce les mêmes ombres ?"
            )
        ) as tracker:
            self.play(Write(titre))
            self.play(FadeIn(mise_en_situation))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(mise_en_situation))

        # --- Raisonnement : définitions -----------------------------------------
        definitions = definition_box(
            VGroup(
                Text("OMBRE PROPRE : partie non éclairée de l'objet opaque", font_size=19),
                Text("lui-même, du côté opposé à la source.", font_size=19),
                Text("OMBRE PORTÉE : zone sombre projetée sur un écran ou", font_size=19),
                Text("une surface derrière l'objet, là où les rayons sont", font_size=19),
                Text("interceptés.", font_size=19),
            ).arrange(DOWN, aligned_edge=LEFT, buff=0.16),
            box_width=11.6,
        )
        definitions.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "L'ombre propre est la partie non éclairée de l'objet "
                "opaque lui-même, du côté opposé à la source. L'ombre "
                "portée, elle, est la zone sombre projetée sur un écran ou "
                "une surface derrière l'objet, là où les rayons lumineux "
                "sont interceptés."
            )
        ) as tracker:
            self.play(FadeIn(definitions))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(definitions))

        # --- Construction avec source ponctuelle S ------------------------------
        construction = _construction_ombre_ponctuelle()
        construction.scale(0.85)
        construction.next_to(titre, DOWN, buff=0.6)

        with self.voiceover(
            text=(
                "Avec une source ponctuelle S, on trace les deux rayons "
                "tangents à l'objet opaque. Ils délimitent exactement "
                "l'ombre propre sur la balle, et, prolongés jusqu'à "
                "l'écran, l'ombre portée sur celui-ci. Comme la source est "
                "un point unique, les contours de ces deux ombres sont "
                "parfaitement nets."
            )
        ) as tracker:
            self.play(FadeIn(construction))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(construction))

        # --- Exemple traité -------------------------------------------------------
        exemple = example_box(
            VGroup(
                Text("Un bâton vertical est éclairé par une lampe ponctuelle S.", font_size=19),
                Text("Les rayons tangents au bâton, prolongés jusqu'au sol,", font_size=19),
                Text("délimitent une ombre portée nette : un rectangle sombre", font_size=19),
                Text("dont la longueur dépend de la position de S.", font_size=19),
            ).arrange(DOWN, aligned_edge=LEFT, buff=0.16),
            box_width=11.6,
        )
        exemple.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Exemple : un bâton vertical est éclairé par une lampe "
                "ponctuelle S. Les rayons tangents au bâton, prolongés "
                "jusqu'au sol, délimitent une ombre portée nette, dont la "
                "longueur dépend directement de la position de la source."
            )
        ) as tracker:
            self.play(FadeIn(exemple))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(exemple))

        # --- À retenir --------------------------------------------------------
        retenir = essentiel_box(
            VGroup(
                Text("À retenir", font_size=24, weight="BOLD"),
                Text("Ombre propre : sur l'objet lui-même.", font_size=20),
                Text("Ombre portée : sur l'écran, derrière l'objet.", font_size=20),
                Text("Source ponctuelle → contours toujours nets.", font_size=20),
            ).arrange(DOWN, aligned_edge=LEFT, buff=0.2),
            box_width=11.2,
        )
        retenir.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Retenons l'essentiel. L'ombre propre se situe sur l'objet "
                "lui-même, l'ombre portée sur l'écran derrière l'objet. "
                "Et avec une source ponctuelle, les contours des deux "
                "ombres sont toujours nets."
            )
        ) as tracker:
            self.play(FadeIn(retenir))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(retenir))

        # --- Pièges à éviter --------------------------------------------------
        pieges = warning_box(
            VGroup(
                Text("• Ne pas confondre ombre propre (sur l'objet) et ombre", font_size=20),
                Text("   portée (sur l'écran) : ce sont deux zones distinctes.", font_size=20),
                Text("• Avec une source ponctuelle, il n'y a JAMAIS de", font_size=20),
                Text("   pénombre : les contours sont toujours nets.", font_size=20),
            ).arrange(DOWN, aligned_edge=LEFT, buff=0.16),
            box_width=11.8,
        )
        pieges.next_to(titre, DOWN, buff=0.35)

        with self.voiceover(
            text=(
                "Deux pièges à éviter. D'abord, ne pas confondre l'ombre "
                "propre, sur l'objet, et l'ombre portée, sur l'écran : ce "
                "sont deux zones bien distinctes. Ensuite, avec une source "
                "ponctuelle, il n'y a jamais de pénombre : les contours "
                "restent toujours nets. Nous verrons au contraire ce qui "
                "se passe avec une source étendue dans la scène suivante."
            )
        ) as tracker:
            self.play(FadeIn(pieges))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(pieges), FadeOut(titre))
