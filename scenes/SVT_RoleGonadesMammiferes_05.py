"""
scenes/SVT_RoleGonadesMammiferes_05.py — Chapitre 1 (1ereC, SVT), scène 05.

Structure et ultrastructure du testicule : albuginée, tubes séminifères,
tissu interstitiel, cellules germinales, cellules de Sertoli, cellules de
Leydig. Source : 1ereC/SVT.pdf, page 9.
"""

import textwrap

from manim import (
    DOWN,
    LEFT,
    RIGHT,
    UP,
    WHITE,
    YELLOW,
    Circle,
    Dot,
    Ellipse,
    FadeIn,
    FadeOut,
    MoveAlongPath,
    Rectangle,
    Text,
    VGroup,
    Write,
)

from shapes.base_scene import NotionScene
from shapes.boxes import definition_box, property_box, scene_title, warning_box


def _wrap(text: str, width: int = 56) -> str:
    return "\n".join(textwrap.fill(line, width=width) for line in text.split("\n"))


def _bullets(items, font_size=22, color=WHITE, width=50):
    lines = VGroup(
        *[Text(f"• {_wrap(it, width=width)}", font_size=font_size, color=color) for it in items]
    )
    lines.arrange(DOWN, aligned_edge=LEFT, buff=0.22)
    return lines


class StructureUltrastructureTesticule(NotionScene):
    def construct(self):
        titre = scene_title("1.5 — Structure du testicule")
        titre.scale(0.7)
        titre.to_edge(UP)

        # --- Énoncé : structure générale ---------------------------------------
        definition = definition_box(
            Text(
                _wrap(
                    "Le testicule est entouré d'une capsule, l'albuginée, "
                    "et formé de nombreux tubes séminifères pelotonnés, "
                    "séparés par du tissu interstitiel.",
                    width=54,
                ),
                font_size=25,
            ),
            box_width=11.8,
        )
        definition.next_to(titre, DOWN, buff=0.55)

        with self.voiceover(
            text=(
                "Le testicule est entouré d'une capsule protectrice, "
                "l'albuginée, et il est formé de nombreux tubes "
                "séminifères, très pelotonnés sur eux-mêmes, séparés les "
                "uns des autres par du tissu interstitiel."
            )
        ) as tracker:
            self.play(Write(titre))
            self.play(FadeIn(definition))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(definition))

        # --- Animation du raisonnement : coupe du testicule + zoom -----------
        albuginee = Ellipse(width=4.5, height=3.0, color=WHITE, stroke_width=3)
        albuginee.next_to(titre, DOWN, buff=0.7).shift(LEFT * 3.3)
        albuginee_lbl = Text("albuginée", font_size=14, color=WHITE).next_to(albuginee, UP, buff=0.1)

        tubes = VGroup(
            *[
                Circle(radius=0.35, color="#1E5FA8", stroke_width=2).move_to(
                    albuginee.get_center() + pos
                )
                for pos in [
                    LEFT * 1.1 + UP * 0.6, UP * 0.7, RIGHT * 1.0 + UP * 0.5,
                    LEFT * 1.2 + DOWN * 0.3, DOWN * 0.2, RIGHT * 1.1 + DOWN * 0.2,
                    LEFT * 0.7 + DOWN * 0.9, RIGHT * 0.6 + DOWN * 0.9,
                ]
            ]
        )
        tubes_lbl = Text("tubes séminifères", font_size=13, color="#1E5FA8").next_to(
            albuginee, DOWN, buff=0.15
        )

        interstitiel_dots = VGroup(
            *[
                Dot(color="#DE7C1F", radius=0.05).move_to(albuginee.get_center() + pos)
                for pos in [
                    LEFT * 0.2 + UP * 0.65, RIGHT * 0.4 + UP * 0.1,
                    LEFT * 0.5 + DOWN * 0.5, RIGHT * 0.15 + DOWN * 0.55,
                    UP * 0.0,
                ]
            ]
        )
        interstitiel_lbl = Text("tissu interstitiel\n(cellules de Leydig)", font_size=12, color="#DE7C1F")
        interstitiel_lbl.next_to(albuginee, LEFT, buff=0.15)

        schema_coupe = VGroup(albuginee, albuginee_lbl, tubes, tubes_lbl, interstitiel_dots, interstitiel_lbl)

        # Zoom : coupe d'un tube séminifère (couches concentriques)
        tube_zoom = Circle(radius=1.3, color="#1E5FA8", stroke_width=3)
        tube_zoom.next_to(titre, DOWN, buff=0.7).shift(RIGHT * 3.0)
        lumiere = Circle(radius=0.35, color="#F1F1F1", fill_opacity=0.9, stroke_width=1)
        lumiere.move_to(tube_zoom.get_center())
        lumiere_lbl = Text("lumière", font_size=12, color="#1B1B1B").move_to(lumiere.get_center())

        couche_sertoli = Circle(radius=1.15, color="#A42A5A", stroke_width=6)
        couche_sertoli.move_to(tube_zoom.get_center())
        sertoli_lbl = Text("cellules de Sertoli", font_size=13, color="#A42A5A").next_to(
            tube_zoom, UP, buff=0.15
        )

        couche_germinales = Circle(radius=0.75, color="#288073", stroke_width=6)
        couche_germinales.move_to(tube_zoom.get_center())
        germinales_lbl = Text(
            "cellules germinales\n(périphérie -> lumière)", font_size=12, color="#288073"
        )
        germinales_lbl.next_to(tube_zoom, DOWN, buff=0.15)

        schema_zoom = VGroup(
            tube_zoom, lumiere, lumiere_lbl,
            couche_sertoli, sertoli_lbl,
            couche_germinales, germinales_lbl,
        )

        with self.voiceover(
            text=(
                "Sur une coupe du testicule, on distingue, à l'intérieur de "
                "l'albuginée, de nombreux tubes séminifères, entourés par "
                "le tissu interstitiel qui contient les cellules de Leydig. "
                "Zoomons sur la paroi d'un seul tube : elle contient, de la "
                "périphérie vers la lumière centrale, les cellules "
                "germinales à différents stades de maturation, ainsi que "
                "les cellules de Sertoli, des cellules somatiques qui "
                "nourrissent et soutiennent ces cellules germinales."
            )
        ) as tracker:
            self.play(FadeIn(albuginee), FadeIn(albuginee_lbl))
            self.play(FadeIn(tubes), FadeIn(tubes_lbl))
            self.play(FadeIn(interstitiel_dots), FadeIn(interstitiel_lbl))
            self.play(FadeIn(tube_zoom))
            self.play(FadeIn(couche_sertoli), FadeIn(sertoli_lbl))
            self.play(FadeIn(couche_germinales), FadeIn(germinales_lbl))
            self.play(FadeIn(lumiere), FadeIn(lumiere_lbl))
            self.wait(tracker.get_remaining_duration())

        # --- Exemple traité : trajet d'une cellule germinale --------------------
        trajet_lbl = Text("De la périphérie à la lumière", font_size=18, color=YELLOW, weight="BOLD")
        trajet_lbl.next_to(VGroup(schema_coupe, schema_zoom), DOWN, buff=0.4)

        point = Dot(color=YELLOW, radius=0.09)
        point.move_to(couche_sertoli.point_at_angle(1.2))

        chemin_zigzag = VGroup(
            *[
                Circle(radius=r, color=YELLOW).move_to(tube_zoom.get_center())
                for r in [1.15, 0.75, 0.35]
            ]
        )

        with self.voiceover(
            text=(
                "Suivons une cellule germinale : née à la périphérie du "
                "tube, sous forme de spermatogonie, elle se rapproche "
                "progressivement de la lumière centrale en se transformant, "
                "toujours nourrie et soutenue par les cellules de Sertoli, "
                "jusqu'à devenir un spermatozoïde mature, libéré dans la "
                "lumière du tube."
            )
        ) as tracker:
            self.play(FadeIn(trajet_lbl), FadeIn(point))
            for cercle in chemin_zigzag:
                self.play(MoveAlongPath(point, cercle), run_time=0.8)
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(schema_coupe), FadeOut(schema_zoom), FadeOut(trajet_lbl), FadeOut(point))

        # --- À retenir : Sertoli vs Leydig --------------------------------------
        comparaison = property_box(
            Text(
                _wrap(
                    "Cellules de SERTOLI : DANS la paroi du tube "
                    "séminifère, rôle nourricier et de soutien des "
                    "cellules germinales. Cellules de LEYDIG : HORS du "
                    "tube, dans le tissu interstitiel, rôle ENDOCRINE, "
                    "sécrètent la testostérone.",
                    width=54,
                ),
                font_size=22,
            ),
            box_width=12.2,
        )
        comparaison.next_to(titre, DOWN, buff=0.55)

        with self.voiceover(
            text=(
                "Retenons la différence essentielle entre ces deux types de "
                "cellules. Les cellules de Sertoli sont situées dans la "
                "paroi du tube séminifère : leur rôle est nourricier, elles "
                "soutiennent les cellules germinales. Les cellules de "
                "Leydig, elles, sont situées en dehors du tube, dans le "
                "tissu interstitiel : leur rôle est endocrine, elles "
                "sécrètent la testostérone directement dans le sang."
            )
        ) as tracker:
            self.play(FadeIn(comparaison))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(comparaison))

        # --- Piège à éviter ------------------------------------------------------
        piege = warning_box(
            Text(
                _wrap(
                    "Ne confonds pas Sertoli et Leydig : Sertoli = DANS le "
                    "tube, nourricière (pas d'hormone sexuelle sécrétée) ; "
                    "Leydig = HORS du tube, endocrine (testostérone). Un "
                    "schéma qui place les cellules de Leydig À "
                    "L'INTÉRIEUR du tube séminifère est faux.",
                    width=56,
                ),
                font_size=21,
            ),
            box_width=12.4,
        )
        piege.next_to(titre, DOWN, buff=0.55)

        with self.voiceover(
            text=(
                "Attention à ne pas confondre Sertoli et Leydig : les "
                "cellules de Sertoli sont dans le tube, et jouent un rôle "
                "nourricier ; les cellules de Leydig sont hors du tube, et "
                "jouent un rôle endocrine. Un schéma qui placerait les "
                "cellules de Leydig à l'intérieur du tube séminifère serait "
                "donc faux."
            )
        ) as tracker:
            self.play(FadeIn(piege))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(titre), FadeOut(piege))
