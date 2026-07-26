"""
scenes/SVT_ProductionMatiere_08.py — Chapitre 11 (1ereD, SVT), scène 08.

§ 11.4.3 La transformation d'énergie (lumineuse → chimique) + piège
« confondre les deux équations » (photosynthèse vs respiration, en
MathTex côte à côte) + § 11.4.4 le devenir de la matière organique
produite (amidon stocké, croissance, respiration).
Source : 1ereD/SVT.pdf, pages 152-153.
"""

import textwrap

from manim import (
    DOWN,
    LEFT,
    RIGHT,
    UP,
    WHITE,
    YELLOW,
    Arrow,
    FadeIn,
    FadeOut,
    MathTex,
    Text,
    VGroup,
    Write,
)

from shapes.base_scene import NotionScene
from shapes.boxes import property_box, scene_title, warning_box


def _wrap(text: str, width: int = 56) -> str:
    return "\n".join(textwrap.fill(line, width=width) for line in text.split("\n"))


def _bullets(items, font_size=22, color=WHITE, width=52):
    lines = VGroup(
        *[Text(f"• {_wrap(it, width=width)}", font_size=font_size, color=color) for it in items]
    )
    lines.arrange(DOWN, aligned_edge=LEFT, buff=0.22)
    return lines


class TransformationEnergieEtDevenirMatiere(NotionScene):
    def construct(self):
        # --- Énoncé : la transformation d'énergie ----------------------------
        titre = scene_title("11.4.3-11.4.4 — Transformation d'énergie et devenir de la matière")
        titre.scale(0.42)
        titre.to_edge(UP)

        with self.voiceover(
            text=(
                "La réaction de l'assimilation chlorophyllienne ne peut "
                "pas se faire toute seule : elle consomme de l'énergie."
            )
        ) as tracker:
            self.play(Write(titre))
            self.wait(tracker.get_remaining_duration())

        # --- Animation du raisonnement : lumineuse -> chimique ---------------------
        lumiere_txt = Text("énergie lumineuse", font_size=26, color=YELLOW, weight="BOLD")
        fleche_energie = Arrow(LEFT, RIGHT, color=WHITE, buff=0.15).scale(1.1)
        chimique_txt = Text("énergie chimique\n(matière organique)", font_size=24, color="#3FA34D", weight="BOLD")
        conversion = VGroup(lumiere_txt, fleche_energie, chimique_txt).arrange(RIGHT, buff=0.35)
        conversion.next_to(titre, DOWN, buff=0.6)

        with self.voiceover(
            text=(
                "Cette énergie est fournie par la lumière, captée par la "
                "chlorophylle. L'assimilation chlorophyllienne réalise "
                "donc une conversion fondamentale : l'énergie lumineuse se "
                "transforme en énergie chimique, stockée dans la matière "
                "organique."
            )
        ) as tracker:
            self.play(FadeIn(lumiere_txt))
            self.play(Write(fleche_energie))
            self.play(FadeIn(chimique_txt))
            self.wait(tracker.get_remaining_duration())

        recuperation = Text(
            _wrap(
                "C'est cette énergie chimique que le végétal récupère en "
                "respirant, jour et nuit, et que tout consommateur "
                "récupère en mangeant le végétal. Quand Aya mange du riz "
                "ou de l'attiéké, elle consomme de l'énergie solaire "
                "stockée par les plantes.",
                width=56,
            ),
            font_size=22,
            color=WHITE,
        )
        recuperation.next_to(conversion, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "C'est cette énergie chimique que le végétal récupère en "
                "respirant, jour et nuit, et que tout consommateur, animal "
                "ou homme, récupère en mangeant le végétal. Quand Aya "
                "mange du riz ou de l'attiéké, elle consomme en réalité de "
                "l'énergie solaire que les plantes ont stockée sous forme "
                "chimique."
            )
        ) as tracker:
            self.play(FadeIn(recuperation))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(conversion), FadeOut(recuperation))

        # --- Piège à éviter : confondre les deux équations -------------------------
        eq_photo = MathTex(
            r"6\,CO_2 + 6\,H_2O \longrightarrow C_6H_{12}O_6 + 6\,O_2",
            font_size=26,
        )
        label_photo = Text("Photosynthèse (lumière, parties vertes)", font_size=16, weight="BOLD")
        bloc_photo = VGroup(label_photo, eq_photo).arrange(DOWN, buff=0.2)

        eq_respi = MathTex(
            r"C_6H_{12}O_6 + 6\,O_2 \longrightarrow 6\,CO_2 + 6\,H_2O",
            font_size=26,
        )
        label_respi = Text("Respiration (tout le temps, toutes les cellules)", font_size=16, weight="BOLD")
        bloc_respi = VGroup(label_respi, eq_respi).arrange(DOWN, buff=0.2)

        deux_equations = VGroup(bloc_photo, bloc_respi).arrange(DOWN, buff=0.4)
        note = Text(
            _wrap(
                "Les deux équations sont inverses l'une de l'autre, mais "
                "les mécanismes sont différents. La respiration a lieu "
                "jour et nuit, pas seulement la nuit.",
                width=50,
            ),
            font_size=17,
        )
        note.next_to(deux_equations, DOWN, buff=0.3)

        piege = warning_box(VGroup(deux_equations, note), box_width=11.5)
        piege.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Attention à ne jamais mélanger les deux équations du "
                "chapitre. L'assimilation chlorophyllienne, à la lumière, "
                "dans les parties vertes : six CO2 plus six H2O donnent "
                "C6H12O6 plus six O2 ; elle construit de la matière et "
                "rejette du O2. La respiration, en permanence, dans toutes "
                "les cellules vivantes : C6H12O6 plus six O2 donnent six "
                "CO2 plus six H2O ; elle détruit de la matière pour "
                "libérer de l'énergie, et consomme du O2. Les deux "
                "équations sont inverses l'une de l'autre, mais les "
                "mécanismes sont différents. Écrire que la respiration "
                "n'a lieu que la nuit est faux : elle a lieu jour et "
                "nuit."
            )
        ) as tracker:
            self.play(FadeIn(piege))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(piege))

        # --- À retenir : le devenir de la matière organique produite ---------------
        devenir = property_box(
            _bullets(
                [
                    "Une partie est transformée en amidon et stockée "
                    "(feuille le jour, puis graines comme le riz et le "
                    "maïs, tubercules comme l'igname et le manioc).",
                    "Une partie est utilisée sur place pour construire de "
                    "nouvelles cellules : cellulose des parois, "
                    "protéines, lipides des membranes (croissance).",
                    "Une partie est dégradée par la respiration pour "
                    "fournir l'énergie nécessaire à la vie de la plante.",
                ],
                font_size=20,
                width=54,
            ),
            box_width=11.8,
        )
        devenir.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Le glucose fabriqué dans les chloroplastes a trois "
                "destins principaux. Une partie est transformée en amidon "
                "et stockée, dans la feuille le jour, puis dans les "
                "organes de réserve, graines comme le riz et le maïs, "
                "tubercules comme l'igname et le manioc. Une partie est "
                "utilisée sur place pour construire de nouvelles cellules "
                ": cellulose des parois, protéines, lipides des "
                "membranes, c'est la croissance. Et une partie est "
                "dégradée par la respiration, pour fournir l'énergie "
                "nécessaire à la vie de la plante."
            )
        ) as tracker:
            self.play(FadeIn(devenir))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(titre), FadeOut(devenir))
