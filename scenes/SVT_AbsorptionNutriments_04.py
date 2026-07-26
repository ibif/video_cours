"""
scenes/SVT_AbsorptionNutriments_04.py — Chapitre 13 (1ereD, SVT), scène 04.

§ 13.2.1 L'intestin grêle, une surface d'échange immense : les trois
niveaux d'amplification (plis circulaires ×3, villosités ×10,
microvillosités ×20) et le calcul complet de la surface d'absorption.
Source : 1ereD/SVT.pdf, pages 170-171.
"""

import textwrap

from manim import (
    DOWN,
    LEFT,
    RIGHT,
    UP,
    WHITE,
    YELLOW,
    GREEN,
    ORANGE,
    RED,
    FadeIn,
    FadeOut,
    Line,
    MathTex,
    Text,
    VGroup,
    Write,
)

from shapes.base_scene import NotionScene
from shapes.boxes import example_box, scene_title, warning_box


def _wrap(text: str, width: int = 56) -> str:
    return "\n".join(textwrap.fill(line, width=width) for line in text.split("\n"))


def _bullets(items, font_size=23, color=WHITE, width=52):
    lines = VGroup(
        *[Text(f"• {_wrap(it, width=width)}", font_size=font_size, color=color) for it in items]
    )
    lines.arrange(DOWN, aligned_edge=LEFT, buff=0.24)
    return lines


class SurfaceAbsorptionImmense(NotionScene):
    def construct(self):
        titre = scene_title("13.2 — Une surface d'échange immense")
        titre.scale(0.6)
        titre.to_edge(UP)

        # --- Énoncé : pourquoi l'intestin grêle absorbe-t-il si bien ? -------
        intro = Text(
            _wrap(
                "Pourquoi l'intestin grêle absorbe-t-il si efficacement ? "
                "Parce que sa structure réalise une prouesse : offrir une "
                "surface d'échange gigantesque dans un volume réduit.",
                width=56,
            ),
            font_size=25,
            color=WHITE,
        )
        intro.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Pourquoi l'intestin grêle absorbe-t-il si efficacement ? "
                "Parce que sa structure réalise une prouesse : offrir une "
                "surface d'échange gigantesque dans un volume réduit. Chez "
                "l'adulte, l'intestin grêle est un tube de six à sept "
                "mètres de long, replié sur lui-même dans l'abdomen : "
                "c'est le plus long organe du tube digestif. Mais la "
                "longueur ne suffit pas."
            )
        ) as tracker:
            self.play(Write(titre))
            self.play(FadeIn(intro))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(intro))

        # --- Animation du raisonnement : cascade des 3 amplifications --------
        entete = Text("Trois niveaux de replis multiplient la surface", font_size=23, color=YELLOW, weight="BOLD")
        entete.next_to(titre, DOWN, buff=0.5)

        # Niveau 1 : tube lisse -> plis circulaires (ligne ondulée)
        tube_lisse = Line(LEFT * 2, RIGHT * 2, color=WHITE, stroke_width=4)
        plis = VGroup(*[Line(UP * 0.18, DOWN * 0.18, color=ORANGE, stroke_width=3) for _ in range(9)])
        plis.arrange(RIGHT, buff=0.28)
        plis.move_to(tube_lisse.get_center())
        label1 = Text("plis circulaires  ×3", font_size=18, color=ORANGE)
        niveau1 = VGroup(tube_lisse, plis, label1).arrange(DOWN, buff=0.2)

        # Niveau 2 : villosités (doigts de gant)
        villosites = VGroup(
            *[Line(DOWN * 0.01, UP * 0.5, color=GREEN, stroke_width=5) for _ in range(9)]
        )
        villosites.arrange(RIGHT, buff=0.22)
        label2 = Text("villosités  ×10", font_size=18, color=GREEN)
        niveau2 = VGroup(villosites, label2).arrange(DOWN, buff=0.25)

        # Niveau 3 : microvillosités (petits traits fins sur chaque villosité)
        microv = VGroup(
            *[
                VGroup(*[Line(UP * 0.03, UP * 0.13, color=RED, stroke_width=1.5).shift(RIGHT * 0.05 * k) for k in range(5)])
                for _ in range(9)
            ]
        )
        for i, groupe in enumerate(microv):
            groupe.move_to(villosites[i].get_top() + UP * 0.12)
        label3 = Text("microvillosités  ×20", font_size=18, color=RED)

        niveau3 = VGroup(villosites.copy(), microv, label3).arrange(DOWN, buff=0.25)

        cascade = VGroup(niveau1, niveau2, niveau3).arrange(RIGHT, buff=1.0, aligned_edge=DOWN)
        cascade.scale(0.85)
        cascade.next_to(entete, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "La paroi interne présente trois niveaux de replis qui "
                "multiplient la surface d'échange avec le chyme. D'abord, "
                "les plis circulaires, ou valvules conniventes : des "
                "bourrelets visibles à l'œil nu, qui multiplient la "
                "surface par environ trois. Ensuite, les villosités "
                "intestinales : environ quatre à cinq millions de petites "
                "saillies en forme de doigt de gant, hautes d'environ un "
                "millimètre, qui multiplient la surface par environ dix. "
                "Enfin, les microvillosités : chaque cellule de la surface "
                "des villosités porte, sur sa face tournée vers la "
                "lumière, environ trois mille replis membranaires "
                "microscopiques formant la bordure en brosse, qui "
                "multiplient encore la surface par environ vingt."
            )
        ) as tracker:
            self.play(FadeIn(entete))
            self.play(FadeIn(niveau1))
            self.play(FadeIn(niveau2))
            self.play(FadeIn(niveau3))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(entete), FadeOut(cascade))

        # --- Exemple traité : calcul de la surface d'absorption ---------------
        exemple_titre = Text("Calcul de la surface d'absorption", font_size=24, color=YELLOW, weight="BOLD")
        exemple_titre.next_to(titre, DOWN, buff=0.5)

        etape1 = MathTex(
            r"S_0 = \pi \times d \times L = \pi \times 0{,}025 \times 6 \approx 0{,}47 \ \text{m}^2",
            font_size=27,
            color=WHITE,
        )
        etape2 = MathTex(
            r"S = S_0 \times 3 \times 10 \times 20 = 0{,}47 \times 600 \approx 283 \ \text{m}^2",
            font_size=27,
            color=YELLOW,
        )
        calculs = VGroup(etape1, etape2).arrange(DOWN, buff=0.45)

        exemple = example_box(
            VGroup(
                Text("Cylindre lisse : L = 6 m, d = 2,5 cm = 0,025 m", font_size=20, weight="BOLD"),
                calculs,
            ).arrange(DOWN, buff=0.35),
            box_width=11.7,
        )
        exemple.next_to(exemple_titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Faisons le calcul. On assimile l'intestin grêle à un "
                "cylindre lisse de longueur six mètres et de diamètre deux "
                "virgule cinq centimètres, soit zéro virgule zéro "
                "vingt-cinq mètre. La surface latérale d'un cylindre est "
                "le produit de la circonférence par la longueur : S zéro "
                "égale pi fois d fois L, soit pi fois zéro virgule zéro "
                "vingt-cinq fois six, ce qui donne environ zéro virgule "
                "quarante-sept mètre carré — moins qu'une porte de "
                "chambre. On applique ensuite les trois amplifications "
                "successives : S égale S zéro fois trois, fois dix, fois "
                "vingt, soit zéro virgule quarante-sept fois six cents, ce "
                "qui donne environ deux cent quatre-vingt-trois mètres "
                "carrés."
            )
        ) as tracker:
            self.play(FadeIn(exemple_titre))
            self.play(Write(etape1))
            self.play(Write(etape2))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(exemple_titre), FadeOut(exemple))

        # --- À retenir : comparaison au court de tennis -------------------------
        a_retenir = _bullets(
            [
                "Surface lisse ≈ 0,47 m² (moins qu'une porte de chambre).",
                "Surface réelle ≈ 283 m², grâce aux trois amplifications combinées.",
                "Soit environ la surface d'un court de tennis (261 m²).",
                "Cette surface, repliée dans l'abdomen, permet des échanges rapides et quasi complets.",
            ],
            font_size=21,
            width=54,
        )
        entete_retenir = Text("À retenir", font_size=26, color=YELLOW, weight="BOLD")
        entete_retenir.next_to(titre, DOWN, buff=0.55)
        a_retenir.next_to(entete_retenir, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "À retenir : grâce aux plis circulaires, aux villosités et "
                "aux microvillosités, la surface d'absorption de "
                "l'intestin grêle passe de moins de zéro virgule cinq "
                "mètre carré à près de trois cents mètres carrés, soit "
                "environ la surface d'un court de tennis. Cette immense "
                "surface, repliée dans l'abdomen, permet des échanges "
                "rapides et quasi complets entre le chyme et le milieu "
                "intérieur."
            )
        ) as tracker:
            self.play(FadeIn(entete_retenir))
            self.play(FadeIn(a_retenir))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(entete_retenir), FadeOut(a_retenir))

        # --- Piège à éviter : les unités et l'ordre du calcul --------------------
        piege = warning_box(
            Text(
                _wrap(
                    "Piège fréquent : oublier de convertir le diamètre en "
                    "mètres avant le calcul (2,5 cm = 0,025 m, pas 2,5 "
                    "m !), ou multiplier les trois facteurs d'amplification "
                    "sur une surface encore exprimée en cm². Toujours "
                    "calculer S0 en mètres carrés d'abord, puis multiplier "
                    "par 3 × 10 × 20 = 600.",
                    width=54,
                ),
                font_size=20,
            ),
            box_width=12.0,
        )
        piege.next_to(titre, DOWN, buff=0.55)

        with self.voiceover(
            text=(
                "Attention aux unités : un piège fréquent est d'oublier de "
                "convertir le diamètre en mètres avant le calcul — deux "
                "virgule cinq centimètres, ce n'est pas deux virgule cinq "
                "mètres, mais zéro virgule zéro vingt-cinq mètre. Un autre "
                "piège est de multiplier les trois facteurs d'amplification "
                "sur une surface encore exprimée en centimètres carrés. "
                "Toujours calculer S zéro en mètres carrés d'abord, puis "
                "multiplier par trois fois dix fois vingt, soit six cents."
            )
        ) as tracker:
            self.play(FadeIn(piege))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(titre), FadeOut(piege))
