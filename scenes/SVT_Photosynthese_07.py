"""
scenes/SVT_Photosynthese_07.py — Chapitre 10 (1ereC, SVT), scène 07.

§ 10.3.3-10.3.4 Formation de l'ATP (photophosphorylation, équation MathTex
ADP+Pi+énergie lumineuse -> ATP+H2O) et du NADPH,H+ (réduction du NADP+,
équation MathTex) + méthode point clé « ATP et NADPH,H+ = transports
d'énergie et de pouvoir réducteur » + bilan de la phase claire (tableau
entrées/sorties).
Source : 1ereC/SVT.pdf, page 109.
"""

import textwrap

from manim import DOWN, LEFT, RIGHT, UP, WHITE, YELLOW, FadeIn, FadeOut, MathTex, Text, VGroup, Write

from shapes.base_scene import NotionScene
from shapes.boxes import method_box, scene_title, warning_box


def _wrap(text: str, width: int = 56) -> str:
    return "\n".join(textwrap.fill(line, width=width) for line in text.split("\n"))


def _bullets(items, font_size=22, color=WHITE, width=52):
    lines = VGroup(
        *[Text(f"• {_wrap(it, width=width)}", font_size=font_size, color=color) for it in items]
    )
    lines.arrange(DOWN, aligned_edge=LEFT, buff=0.22)
    return lines


def _cell(text: str, x: float, y: float, font_size=17, color=WHITE, bold=False):
    t = Text(text, font_size=font_size, color=color, weight="BOLD" if bold else "NORMAL")
    t.move_to([x, y, 0])
    t.shift(RIGHT * (t.width / 2))
    return t


class FormationATPetNADPH(NotionScene):
    def construct(self):
        titre = scene_title("10.3.3-10.3.4 — Formation de l'ATP et du NADPH,H+")
        titre.scale(0.42)
        titre.to_edge(UP)

        # --- Énoncé : l'énergie des électrons excités sert à fabriquer -------
        intro = Text(
            _wrap(
                "L'énergie des électrons excités par la lumière est "
                "utilisée pour fabriquer deux composés riches en "
                "énergie : l'ATP et le NADPH,H+.",
                width=56,
            ),
            font_size=23,
            color=WHITE,
        )
        intro.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "L'énergie des électrons excités par la lumière, issus "
                "de la photolyse de l'eau, est utilisée pour fabriquer "
                "deux composés riches en énergie : l'ATP et le "
                "NADPH,H plus."
            )
        ) as tracker:
            self.play(Write(titre))
            self.play(FadeIn(intro))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(intro))

        # --- Animation du raisonnement : formation de l'ATP -------------------
        atp_texte = Text(
            _wrap(
                "L'ATP (adénosine triphosphate) est formé par "
                "photophosphorylation : l'addition d'un phosphate "
                "minéral (Pi) sur l'ADP grâce à l'énergie lumineuse.",
                width=54,
            ),
            font_size=21,
            color=WHITE,
        )
        atp_texte.next_to(titre, DOWN, buff=0.5)

        eq_atp = MathTex(
            r"ADP + P_i + \text{énergie lumineuse} \longrightarrow ATP + H_2O",
            font_size=28,
            color=YELLOW,
        )
        eq_atp.next_to(atp_texte, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "L'ATP, adénosine triphosphate, est formé par un "
                "mécanisme appelé photophosphorylation : c'est "
                "l'addition d'un phosphate minéral, noté Pi, sur l'ADP, "
                "grâce à l'énergie lumineuse. L'équation s'écrit : ADP "
                "plus phosphate inorganique plus énergie lumineuse "
                "donnent de l'ATP et de l'eau."
            )
        ) as tracker:
            self.play(FadeIn(atp_texte))
            self.play(Write(eq_atp))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(atp_texte), FadeOut(eq_atp))

        # --- Exemple traité : formation du NADPH,H+ ----------------------------
        nadph_texte = Text(
            _wrap(
                "Le NADP+ (nicotinamide adénine dinucléotide phosphate) "
                "capte les électrons et les protons issus de la "
                "photolyse ; il se réduit en NADPH,H+.",
                width=54,
            ),
            font_size=21,
            color=WHITE,
        )
        nadph_texte.next_to(titre, DOWN, buff=0.5)

        eq_nadph = MathTex(
            r"NADP^+ + 2\,e^- + 2\,H^+ \longrightarrow NADPH,H^+",
            font_size=28,
            color=YELLOW,
        )
        eq_nadph.next_to(nadph_texte, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Le second composé formé est le NADPH,H plus, un "
                "coenzyme réduit. Le NADP plus, nicotinamide adénine "
                "dinucléotide phosphate, capte les électrons et les "
                "protons issus de la photolyse de l'eau ; il se réduit "
                "ainsi : NADP plus, additionné de deux électrons et deux "
                "protons, donne du NADPH,H plus."
            )
        ) as tracker:
            self.play(FadeIn(nadph_texte))
            self.play(Write(eq_nadph))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(nadph_texte), FadeOut(eq_nadph))

        # --- Méthode : point clé ATP et NADPH,H+ = transports d'énergie ------
        methode = method_box(
            Text(
                _wrap(
                    "Point clé : l'ATP et le NADPH,H+ sont les "
                    "« transports d'énergie et de pouvoir réducteur » "
                    "qui serviront, dans la phase sombre, à transformer "
                    "le CO2 en glucose.",
                    width=54,
                ),
                font_size=21,
            ),
            box_width=12.0,
        )
        methode.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Retenez ce point clé : l'ATP et le NADPH,H plus sont "
                "les transports d'énergie et de pouvoir réducteur qui "
                "serviront, dans la phase sombre, à transformer le "
                "dioxyde de carbone en glucose. Sans eux, le cycle de "
                "Calvin ne pourrait tout simplement pas fonctionner."
            )
        ) as tracker:
            self.play(FadeIn(methode))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(methode))

        # --- À retenir : bilan de la phase claire (tableau entrées/sorties) --
        entete_tab = Text("Bilan de la phase claire", font_size=24, color=YELLOW, weight="BOLD")
        entete_tab.next_to(titre, DOWN, buff=0.4)

        x_entree, x_sortie = -4.5, 2.0
        row_y0 = entete_tab.get_bottom()[1] - 0.55
        row_h = 0.75

        header_row = VGroup(
            _cell("Entrées", x_entree, row_y0, font_size=18, color=YELLOW, bold=True),
            _cell("Sorties", x_sortie, row_y0, font_size=18, color=YELLOW, bold=True),
        )

        rows_data = [
            ("Eau H2O", "Dioxygène O2 (dégagé)"),
            ("Lumière (énergie)", "ATP (énergie chimique)"),
            ("NADP+, ADP, Pi", "NADPH,H+ (pouvoir réducteur)"),
        ]
        data_rows = VGroup()
        for i, (entree, sortie) in enumerate(rows_data):
            y = row_y0 - (i + 1) * row_h
            data_rows.add(
                VGroup(
                    _cell(entree, x_entree, y, font_size=16),
                    _cell(sortie, x_sortie, y, font_size=16),
                )
            )
        tableau = VGroup(header_row, data_rows)

        with self.voiceover(
            text=(
                "Résumons le bilan complet de la phase claire. En "
                "entrée : de l'eau, de la lumière, du NADP plus, de "
                "l'ADP et du phosphate inorganique. En sortie : du "
                "dioxygène dégagé, de l'ATP, énergie chimique "
                "utilisable, et du NADPH,H plus, pouvoir réducteur. En "
                "résumé, la phase claire convertit l'énergie lumineuse "
                "en énergie chimique et en pouvoir réducteur, tout en "
                "dégageant l'oxygène provenant de l'eau."
            )
        ) as tracker:
            self.play(FadeIn(entete_tab))
            self.play(FadeIn(header_row))
            for row in data_rows:
                self.play(FadeIn(row), run_time=0.4)
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(entete_tab), FadeOut(tableau))

        # --- Piège à éviter : ATP et NADPH,H+ ne sont pas stockés durablement --
        piege = warning_box(
            Text(
                _wrap(
                    "Piège à éviter : l'ATP et le NADPH,H+ formés dans "
                    "les thylakoïdes ne sont PAS stockés durablement ni "
                    "exportés hors du chloroplaste : ils sont consommés "
                    "presque aussitôt dans le stroma, par la phase "
                    "sombre, qui se déroule juste à côté.",
                    width=54,
                ),
                font_size=20,
            ),
            box_width=12.0,
        )
        piege.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Un dernier point de vigilance : l'ATP et le NADPH,H "
                "plus formés dans les thylakoïdes ne sont pas stockés "
                "durablement, ni exportés hors du chloroplaste. Ils sont "
                "consommés presque aussitôt dans le stroma voisin, par "
                "la phase sombre, que nous découvrirons dans les "
                "prochaines scènes."
            )
        ) as tracker:
            self.play(FadeIn(piege))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(titre), FadeOut(piege))
