"""
scenes/SVT_GametogeneseMammiferes_07.py — Chapitre 3 (1ereC, SVT), scène 07.

La structure du spermatozoïde : tête (noyau + acrosome), pièce
intermédiaire (mitochondries), flagelle (locomotion) — tableau
structure/fonction et schéma annoté.
Source : 1ereC/SVT.pdf, pages 29-30.
"""

import textwrap

from manim import (
    BLUE,
    DOWN,
    LEFT,
    ORANGE,
    RED,
    RIGHT,
    UP,
    WHITE,
    YELLOW,
    Arrow,
    Ellipse,
    FadeIn,
    FadeOut,
    Line,
    Text,
    VGroup,
    Write,
)

from shapes.base_scene import NotionScene
from shapes.boxes import definition_box, example_box, property_box, scene_title, warning_box


def _wrap(text: str, width: int = 56) -> str:
    return "\n".join(textwrap.fill(line, width=width) for line in text.split("\n"))


def _bullets(items, font_size=22, color=WHITE, width=52):
    lines = VGroup(
        *[Text(f"• {_wrap(it, width=width)}", font_size=font_size, color=color) for it in items]
    )
    lines.arrange(DOWN, aligned_edge=LEFT, buff=0.22)
    return lines


class StructureDuSpermatozoide(NotionScene):
    def construct(self):
        titre = scene_title("3.7 — La structure du spermatozoïde")
        titre.scale(0.68)
        titre.to_edge(UP)

        # --- Énoncé : trois parties, une cellule du voyage ----------------------
        definition = definition_box(
            Text(
                _wrap(
                    "Le spermatozoïde humain est une cellule filiforme "
                    "très allongée, longue d'environ 60 µm, adaptée à la "
                    "mobilité et à la pénétration de l'ovule. Il "
                    "comprend trois parties : la tête, la pièce "
                    "intermédiaire (col) et le flagelle (queue).",
                    width=54,
                ),
                font_size=23,
            ),
            box_width=12.2,
        )
        definition.next_to(titre, DOWN, buff=0.45)

        with self.voiceover(
            text=(
                "Le spermatozoïde humain est une cellule filiforme très "
                "allongée, longue d'environ soixante micromètres, adaptée "
                "à la mobilité et à la pénétration de l'ovule. Il comprend "
                "trois parties : la tête, la pièce intermédiaire, aussi "
                "appelée col, et le flagelle, la queue."
            )
        ) as tracker:
            self.play(Write(titre))
            self.play(FadeIn(definition))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(definition))

        # --- Animation du raisonnement : schéma annoté --------------------------
        entete_schema = Text("Schéma annoté", font_size=25, color=YELLOW, weight="BOLD")
        entete_schema.next_to(titre, DOWN, buff=0.4)

        noyau = Ellipse(width=0.55, height=0.75, color=BLUE, fill_color=BLUE, fill_opacity=0.85, stroke_width=2)
        acrosome = Ellipse(width=0.55, height=0.32, color=ORANGE, fill_color=ORANGE, fill_opacity=0.9, stroke_width=2)
        acrosome.move_to(noyau.get_top() + DOWN * 0.14)
        piece_intermediaire = Ellipse(width=0.3, height=0.4, color=RED, fill_color=RED, fill_opacity=0.85, stroke_width=2)
        piece_intermediaire.next_to(noyau, DOWN, buff=0.02)
        flagelle = Line(
            piece_intermediaire.get_bottom(),
            piece_intermediaire.get_bottom() + DOWN * 2.6,
            color=WHITE,
            stroke_width=3,
        )
        spermato_schema = VGroup(noyau, acrosome, piece_intermediaire, flagelle)
        spermato_schema.rotate(90 * 3.14159 / 180).move_to(RIGHT * 3.2)

        label_acrosome = Text("Acrosome (enzymes)", font_size=16, color=ORANGE)
        label_acrosome.move_to(LEFT * 3.3 + UP * 1.7)
        arrow_acr = Arrow(label_acrosome.get_right(), acrosome.get_center(), buff=0.1, color=WHITE)

        label_noyau = Text("Noyau haploïde (n)", font_size=16, color=BLUE)
        label_noyau.move_to(LEFT * 3.3 + UP * 0.6)
        arrow_noy = Arrow(label_noyau.get_right(), noyau.get_center(), buff=0.1, color=WHITE)

        label_pi = Text("Pièce intermédiaire\n(mitochondries)", font_size=16, color=RED)
        label_pi.move_to(LEFT * 3.3 + DOWN * 0.6)
        arrow_pi = Arrow(label_pi.get_right(), piece_intermediaire.get_center(), buff=0.1, color=WHITE)

        label_flag = Text("Flagelle (locomotion)", font_size=16, color=WHITE)
        label_flag.move_to(LEFT * 3.3 + DOWN * 1.9)
        arrow_flag = Arrow(label_flag.get_right(), flagelle.get_end() + LEFT * 0.5, buff=0.1, color=WHITE)

        schema_full = VGroup(
            spermato_schema,
            label_acrosome, arrow_acr,
            label_noyau, arrow_noy,
            label_pi, arrow_pi,
            label_flag, arrow_flag,
        )

        with self.voiceover(
            text=(
                "Observons le schéma. La tête, en haut, contient le "
                "noyau, haploïde, coiffé de l'acrosome, une vésicule "
                "riche en enzymes. Juste en dessous, la pièce "
                "intermédiaire est un manchon de mitochondries. Enfin, le "
                "flagelle, très long filament contractile, assure la "
                "locomotion de la cellule."
            )
        ) as tracker:
            self.play(FadeIn(entete_schema))
            self.play(FadeIn(spermato_schema))
            self.play(
                FadeIn(label_acrosome), FadeIn(arrow_acr),
                FadeIn(label_noyau), FadeIn(arrow_noy),
                FadeIn(label_pi), FadeIn(arrow_pi),
                FadeIn(label_flag), FadeIn(arrow_flag),
            )
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(entete_schema), FadeOut(schema_full))

        # --- Exemple traité : tableau structure / fonction ----------------------
        entete_tab = Text("Structure et fonction", font_size=25, color=YELLOW, weight="BOLD")
        entete_tab.next_to(titre, DOWN, buff=0.4)

        tableau = _bullets(
            [
                "Tête : noyau haploïde condensé (transporte le "
                "patrimoine génétique paternel) + acrosome (enzymes "
                "hyaluronidase et acrosine, digèrent les enveloppes de "
                "l'ovule).",
                "Pièce intermédiaire : manchon de mitochondries en "
                "spirale → production d'ATP pour les battements du "
                "flagelle.",
                "Flagelle : filament contractile (axonème 9+2 "
                "microtubules) → propulsion, vitesse de 2 à 3 mm/min.",
            ],
            font_size=20,
            width=50,
        )
        tableau.next_to(entete_tab, DOWN, buff=0.35)

        with self.voiceover(
            text=(
                "Détaillons structure et fonction. La tête associe le "
                "noyau haploïde condensé, qui transporte le patrimoine "
                "génétique paternel, et l'acrosome, dont les enzymes, "
                "hyaluronidase et acrosine, sont capables de digérer les "
                "enveloppes de l'ovule au moment de la fécondation. La "
                "pièce intermédiaire, manchon de mitochondries disposées "
                "en spirale autour de l'axe du flagelle, produit l'ATP, "
                "l'énergie indispensable aux battements du flagelle. Le "
                "flagelle lui-même, long filament contractile à structure "
                "interne en neuf plus deux microtubules, assure la "
                "locomotion : ses battements propulsent le spermatozoïde "
                "à une vitesse de deux à trois millimètres par minute."
            )
        ) as tracker:
            self.play(FadeIn(entete_tab))
            self.play(FadeIn(tableau))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(entete_tab), FadeOut(tableau))

        # --- À retenir : cellule du voyage ----------------------------------------
        retenir = property_box(
            _bullets(
                [
                    "Tête : information génétique (noyau) + outil de "
                    "pénétration (acrosome).",
                    "Pièce intermédiaire : moteur énergétique "
                    "(mitochondries → ATP).",
                    "Flagelle : appareil locomoteur (déplacement).",
                ],
                font_size=20,
                width=50,
            ),
            box_width=12.0,
        )
        retenir.next_to(titre, DOWN, buff=0.45)

        with self.voiceover(
            text=(
                "Retenons l'organisation fonctionnelle du spermatozoïde : "
                "la tête porte l'information génétique et l'outil de "
                "pénétration, la pièce intermédiaire est le moteur "
                "énergétique, et le flagelle est l'appareil locomoteur."
            )
        ) as tracker:
            self.play(FadeIn(retenir))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(retenir))

        # --- Piège à éviter -------------------------------------------------------
        piege = warning_box(
            Text(
                _wrap(
                    "Ne dis pas que le flagelle transporte l'information "
                    "génétique : c'est le NOYAU, dans la tête, qui la "
                    "porte. Le flagelle n'a qu'un rôle mécanique de "
                    "locomotion ; sans ses mitochondries (pièce "
                    "intermédiaire), il ne dispose d'aucune énergie pour "
                    "battre.",
                    width=54,
                ),
                font_size=21,
            ),
            box_width=12.2,
        )
        piege.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Piège fréquent : ne dis pas que le flagelle transporte "
                "l'information génétique. C'est le noyau, dans la tête, "
                "qui la porte. Le flagelle n'a qu'un rôle mécanique de "
                "locomotion ; sans les mitochondries de la pièce "
                "intermédiaire, il ne disposerait d'aucune énergie pour "
                "battre."
            )
        ) as tracker:
            self.play(FadeIn(piege))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(titre), FadeOut(piege))
