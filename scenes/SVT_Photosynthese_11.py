"""
scenes/SVT_Photosynthese_11.py — Chapitre 10 (1ereC, SVT), scène 11.

§ 10.5.1 Mise en évidence expérimentale (1/2) : la méthode expérimentale
générale (lot expérimental vs lot témoin, une seule variable) + l'expérience
de la plante aquatique/élodée (protocole complet avec schéma du dispositif,
observations lot éclairé vs lot témoin à l'obscurité, conclusion).
Source : 1ereC/SVT.pdf, page 111.
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
    Circle,
    Dot,
    FadeIn,
    FadeOut,
    Line,
    Polygon,
    Rectangle,
    Text,
    VGroup,
    Write,
)

from shapes.base_scene import NotionScene
from shapes.boxes import definition_box, method_box, scene_title


def _wrap(text: str, width: int = 56) -> str:
    return "\n".join(textwrap.fill(line, width=width) for line in text.split("\n"))


def _bullets(items, font_size=22, color=WHITE, width=52):
    lines = VGroup(
        *[Text(f"• {_wrap(it, width=width)}", font_size=font_size, color=color) for it in items]
    )
    lines.arrange(DOWN, aligned_edge=LEFT, buff=0.22)
    return lines


def _dispositif_elodee(eclaire=True):
    """Dispositif : cuve d'eau, entonnoir renversé sur l'élodée, tube à
    essai rempli d'eau au sommet (bulles de gaz s'y accumulant si
    éclairé)."""
    cuve = Rectangle(width=2.6, height=2.4, stroke_color="#5AA9E6", stroke_width=2, fill_color="#1B3A5C", fill_opacity=0.35)

    entonnoir = Polygon(
        [-0.9, -0.6, 0], [0.9, -0.6, 0], [0.15, 0.5, 0], [-0.15, 0.5, 0],
        stroke_color="#AAAAAA", stroke_width=2, fill_color="#333333", fill_opacity=0.3,
    )
    entonnoir.move_to(cuve.get_center() + DOWN * 0.3)

    elodee = VGroup(
        *[
            Line(ORIGIN, [0.08 * (-1) ** i, 0.5 + 0.08 * i, 0], stroke_color="#2E9E4F", stroke_width=3)
            for i in range(6)
        ]
    )
    elodee.arrange(RIGHT, buff=0.05)
    elodee.move_to(entonnoir.get_bottom() + UP * 0.1)

    tube = Rectangle(width=0.4, height=1.0, stroke_color="#DDDDDD", stroke_width=1.5, fill_color="#1B3A5C", fill_opacity=0.25)
    tube.next_to(entonnoir, UP, buff=0.0).align_to(entonnoir, RIGHT).shift(LEFT * 0.55)

    if eclaire:
        bulles = VGroup(*[Dot(radius=0.045, color="#E8F0E8") for _ in range(5)])
        bulles.arrange(UP, buff=0.08)
        bulles.move_to(tube.get_center() + DOWN * 0.15)
        gaz = Rectangle(width=0.36, height=0.3, stroke_width=0, fill_color="#E8F0E8", fill_opacity=0.35)
        gaz.align_to(tube, UP).shift(DOWN * 0.02)
        contenu_tube = VGroup(gaz, bulles)
        lampe = VGroup(
            Circle(radius=0.22, stroke_color=YELLOW, fill_color=YELLOW, fill_opacity=0.7),
            *[Line(ORIGIN, [0.3 * (i - 1.5), -0.3, 0], stroke_color=YELLOW, stroke_width=1.5) for i in range(4)],
        )
        lampe[0].move_to([0, 2.4, 0])
        for i, rayon in enumerate(lampe[1:]):
            rayon.shift([0, 2.1, 0])
        legende = Text("dispositif éclairé", font_size=14, color=YELLOW, weight="BOLD")
    else:
        contenu_tube = VGroup()
        lampe = VGroup()
        legende = Text("dispositif témoin (obscurité)", font_size=14, color="#888888", weight="BOLD")

    legende.next_to(cuve, DOWN, buff=0.55)

    groupe = VGroup(cuve, entonnoir, elodee, tube, contenu_tube, lampe, legende)
    return groupe


class MethodeExperimentaleEtElodee(NotionScene):
    def construct(self):
        titre = scene_title("10.5.1 — Mise en évidence expérimentale (1/2)")
        titre.scale(0.55)
        titre.to_edge(UP)

        # --- Énoncé : la méthode expérimentale générale -----------------------
        methode_generale = method_box(
            Text(
                _wrap(
                    "Toute mise en évidence rigoureuse repose sur la "
                    "méthode expérimentale : on compare un lot "
                    "expérimental (où le facteur étudié est présent) à "
                    "un lot témoin (identique en tout point, sauf le "
                    "facteur étudié). Une seule variable doit différer "
                    "entre les deux lots.",
                    width=54,
                ),
                font_size=21,
            ),
            box_width=12.0,
        )
        methode_generale.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Comment prouver expérimentalement que la photosynthèse "
                "a bien lieu ? Toute mise en évidence rigoureuse repose "
                "sur la méthode expérimentale : on compare un lot "
                "expérimental, où le facteur étudié est présent, à un "
                "lot témoin, identique en tout point sauf le facteur "
                "étudié. Une seule variable doit différer entre les deux "
                "lots, sinon aucune conclusion n'est possible."
            )
        ) as tracker:
            self.play(Write(titre))
            self.play(FadeIn(methode_generale))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(methode_generale))

        # --- Animation du raisonnement : le protocole de l'élodée -------------
        protocole = _bullets(
            [
                "On place une élodée (plante aquatique) dans un "
                "entonnoir renversé, plongé dans une cuve à eau.",
                "On coiffe l'entonnoir d'un tube à essai rempli d'eau "
                "et renversé.",
                "Le dispositif est éclairé par une lampe ; un "
                "dispositif témoin identique est placé à l'obscurité.",
            ],
            font_size=20,
            width=50,
        )
        protocole.to_edge(LEFT, buff=0.4).shift(UP * 0.1)

        with self.voiceover(
            text=(
                "Voici le protocole de l'expérience de la plante "
                "aquatique. On place une élodée dans un entonnoir "
                "renversé, plongé dans une cuve à eau. On coiffe cet "
                "entonnoir d'un tube à essai rempli d'eau et renversé, "
                "pour recueillir le gaz éventuellement dégagé. Le "
                "dispositif est éclairé par une lampe ; un dispositif "
                "témoin, rigoureusement identique, est placé à "
                "l'obscurité."
            )
        ) as tracker:
            self.play(FadeIn(protocole))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(protocole))

        # --- Exemple traité : schéma des deux dispositifs et observations ----
        disp_eclaire = _dispositif_elodee(eclaire=True)
        disp_temoin = _dispositif_elodee(eclaire=False)
        deux_dispositifs = VGroup(disp_eclaire, disp_temoin).arrange(RIGHT, buff=1.4)
        deux_dispositifs.scale(0.85)
        deux_dispositifs.next_to(titre, DOWN, buff=0.55)

        with self.voiceover(
            text=(
                "Observons les résultats. Dans le lot éclairé, des "
                "bulles de gaz s'échappent de l'élodée et s'accumulent "
                "au sommet du tube ; le gaz recueilli ravive une braise "
                "presque éteinte : c'est du dioxygène. Dans le lot "
                "témoin, à l'obscurité, on n'observe strictement aucun "
                "dégagement gazeux."
            )
        ) as tracker:
            self.play(FadeIn(deux_dispositifs))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(deux_dispositifs))

        # --- À retenir : conclusion --------------------------------------------
        conclusion = definition_box(
            Text(
                _wrap(
                    "Conclusion : la plante verte éclairée dégage du "
                    "dioxygène ; ce dégagement nécessite la lumière "
                    "(absent chez le témoin à l'obscurité). C'est une "
                    "preuve directe de la photosynthèse.",
                    width=54,
                ),
                font_size=21,
            ),
            box_width=12.0,
        )
        conclusion.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Conclusion : la plante verte éclairée dégage du "
                "dioxygène ; ce dégagement nécessite la lumière, "
                "puisqu'il est absent chez le témoin maintenu à "
                "l'obscurité. C'est une preuve expérimentale directe de "
                "la photosynthèse."
            )
        ) as tracker:
            self.play(FadeIn(conclusion))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(conclusion))

        # --- Piège à éviter : le rôle indispensable du témoin -----------------
        piege = method_box(
            Text(
                _wrap(
                    "Piège à éviter : sans le dispositif témoin à "
                    "l'obscurité, on ne pourrait pas affirmer que c'est "
                    "bien la LUMIÈRE qui cause le dégagement de "
                    "dioxygène (et non, par exemple, un simple effet de "
                    "la température ou de l'agitation de l'eau). Le "
                    "témoin isole la variable étudiée.",
                    width=54,
                ),
                font_size=20,
            ),
            box_width=12.0,
        )
        piege.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Attention, un point souvent oublié : sans le "
                "dispositif témoin à l'obscurité, on ne pourrait pas "
                "affirmer que c'est bien la lumière qui cause le "
                "dégagement de dioxygène, et non, par exemple, un simple "
                "effet de la température ou de l'agitation de l'eau. "
                "C'est le témoin qui isole rigoureusement la variable "
                "étudiée."
            )
        ) as tracker:
            self.play(FadeIn(piege))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(titre), FadeOut(piege))
