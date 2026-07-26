"""
scenes/SVT_TectoniquePlaques_09.py — Chapitre 8 (1ereC, SVT), scène 09.

IV.B.1 Les frontières convergentes (1/2) — la subduction : définition,
fosse océanique, plan de Wadati-Benioff, fusion hydratée vers 100 km,
magmas andésitiques et volcanisme explosif, les 2 cas de figure
(océan-océan avec arc insulaire ; océan-continent avec cordillère, ex.
Andes) + compensation de l'expansion océanique. Source : 1ereC/SVT.pdf,
pages 90-91.
"""

import textwrap

from manim import (
    BLUE_E,
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
    Dot,
    FadeIn,
    FadeOut,
    Polygon,
    Rectangle,
    Text,
    VGroup,
    Write,
)

from shapes.base_scene import NotionScene
from shapes.boxes import definition_box, scene_title


def _wrap(text: str, width: int = 56) -> str:
    return "\n".join(textwrap.fill(line, width=width) for line in text.split("\n"))


def _bullets(items, font_size=24, color=WHITE, width=54):
    lines = VGroup(
        *[Text(f"• {_wrap(it, width=width)}", font_size=font_size, color=color) for it in items]
    )
    lines.arrange(DOWN, aligned_edge=LEFT, buff=0.22)
    return lines


class FrontieresConvergentesSubduction(NotionScene):
    def construct(self):
        titre = scene_title("IV.B La subduction (frontière convergente 1/2)")
        titre.scale(0.55)
        titre.to_edge(UP)
        self.play(Write(titre))

        # --- Énoncé : définition de la subduction -----------------------------
        d_subduction = definition_box(
            Text(
                _wrap(
                    "Subduction : enfoncement d'une plaque lithosphérique "
                    "océanique, froide et dense, sous une autre plaque, le "
                    "long d'un plan incliné, jusqu'au manteau. Elle se "
                    "marque en surface par une fosse océanique (jusqu'à "
                    "11 000 m de profondeur).",
                    width=54,
                ),
                font_size=22,
            ),
            box_width=12.0,
        )
        d_subduction.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "La subduction est l'enfoncement d'une plaque "
                "lithosphérique océanique, froide et dense, sous une autre "
                "plaque, le long d'un plan incliné, jusque dans le manteau. "
                "Elle se marque en surface par une fosse océanique, pouvant "
                "atteindre onze mille mètres de profondeur."
            )
        ) as tracker:
            self.play(FadeIn(d_subduction))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(d_subduction))

        # --- Animation du raisonnement : schéma fosse + plan de Wadati-Benioff
        continent = Polygon(
            [0.5, 0.6, 0], [4.5, 0.6, 0], [4.5, -1.8, 0], [0.5, -1.8, 0],
            fill_color=ORANGE, fill_opacity=0.7, stroke_color=WHITE, stroke_width=1,
        )
        ocean_plaque = Polygon(
            [-4.5, 0.15, 0], [0.2, 0.15, 0], [0.5, -0.4, 0], [-1.0, -3.2, 0], [-1.6, -3.2, 0], [-4.5, -0.35, 0],
            fill_color=BLUE_E, fill_opacity=0.8, stroke_color=WHITE, stroke_width=1,
        )
        fosse = Polygon(
            [-0.5, 0.15, 0], [0.5, 0.15, 0], [0.2, -0.5, 0], [-0.3, -0.5, 0],
            fill_color=RED, fill_opacity=0.7, stroke_color=WHITE, stroke_width=1,
        )

        # Foyers sismiques le long du plan de Wadati-Benioff
        wadati_pts = [[-0.1, -0.1, 0], [-0.4, -0.8, 0], [-0.8, -1.6, 0], [-1.1, -2.4, 0], [-1.4, -3.0, 0]]
        foyers = VGroup(*[Dot(point=p, radius=0.06, color=YELLOW) for p in wadati_pts])
        label_wadati = Text("plan de Wadati-Benioff", font_size=14, color=YELLOW)
        label_wadati.next_to(VGroup(*foyers), RIGHT, buff=0.2).shift(DOWN * 0.3)

        volcan = Polygon(
            [1.6, 0.6, 0], [2.1, 1.5, 0], [2.6, 0.6, 0],
            fill_color=RED, fill_opacity=0.8, stroke_color=WHITE, stroke_width=1,
        )
        label_volcan = Text("volcanisme andésitique", font_size=13, color=WHITE).next_to(volcan, UP, buff=0.1)

        fleche_plongee = Arrow(
            start=[-2.5, -0.6, 0], end=[-1.0, -2.4, 0], color=WHITE, buff=0, stroke_width=3
        )

        label_fosse = Text("fosse océanique", font_size=13, color=WHITE).next_to(fosse, DOWN, buff=0.5)
        label_ocean = Text("plaque océanique\n(froide, dense)", font_size=13, color=WHITE).move_to([-3.2, 0.6, 0])
        label_continent = Text("plaque continentale", font_size=13, color=WHITE).move_to([3.0, -1.4, 0])

        schema = VGroup(
            ocean_plaque, continent, fosse, foyers, label_wadati, volcan, label_volcan,
            fleche_plongee, label_fosse, label_ocean, label_continent,
        )
        schema.scale(0.85)
        schema.next_to(titre, DOWN, buff=0.55)

        with self.voiceover(
            text=(
                "Voici le schéma d'une zone de subduction. La plaque "
                "océanique, refroidie et dense, plonge sous l'autre plaque. "
                "Le plan de Wadati-Benioff est le plan incliné matérialisé "
                "par les foyers des séismes, dont la profondeur augmente "
                "régulièrement de la fosse vers l'intérieur des terres, "
                "jusqu'à environ sept cents kilomètres."
            )
        ) as tracker:
            self.play(FadeIn(ocean_plaque), FadeIn(continent))
            self.play(FadeIn(fosse), FadeIn(label_fosse), FadeIn(label_ocean), FadeIn(label_continent))
            self.play(Create(fleche_plongee))
            self.play(FadeIn(foyers), FadeIn(label_wadati))
            self.wait(tracker.get_remaining_duration())

        with self.voiceover(
            text=(
                "Vers cent kilomètres de profondeur, l'eau libérée par la "
                "plaque plongeante provoque la fusion hydratée du manteau "
                "situé au-dessus : les magmas produits sont andésitiques, "
                "riches en silice et visqueux, et alimentent un volcanisme "
                "explosif, des stratovolcans alignés parallèlement à la "
                "fosse."
            )
        ) as tracker:
            self.play(FadeIn(volcan), FadeIn(label_volcan))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(schema))

        # --- Exemple traité : les deux cas de figure ---------------------------
        entete_cas = Text("Deux cas de figure", font_size=26, color=YELLOW, weight="BOLD")
        entete_cas.next_to(titre, DOWN, buff=0.5)

        cas = _bullets(
            [
                "Océan-océan : fosse + arc insulaire volcanique (Japon, "
                "Mariannes, Aléoutiennes).",
                "Océan-continent : fosse + cordillère volcanique (Andes : "
                "plaque de Nazca plongeant sous la plaque sud-américaine).",
            ],
            font_size=22,
            width=52,
        )
        cas.next_to(entete_cas, DOWN, buff=0.35)

        with self.voiceover(
            text=(
                "Deux cas de figure sont possibles. Premier cas, "
                "océan-océan : une plaque océanique plonge sous une autre "
                "plaque océanique, ce qui forme une fosse et un arc "
                "insulaire volcanique, comme au Japon, aux Mariannes ou aux "
                "Aléoutiennes. Deuxième cas, océan-continent : une plaque "
                "océanique plonge sous une plaque continentale, ce qui "
                "forme une fosse et une cordillère volcanique, comme dans "
                "les Andes, où la plaque de Nazca plonge sous la plaque "
                "sud-américaine."
            )
        ) as tracker:
            self.play(FadeIn(entete_cas))
            self.play(FadeIn(cas))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(entete_cas), FadeOut(cas))

        # --- À retenir : compensation de l'expansion océanique -----------------
        compensation = Text(
            _wrap(
                "L'expansion océanique aux dorsales est ainsi compensée par "
                "la destruction de lithosphère dans les fosses : la surface "
                "totale du globe reste constante.",
                width=54,
            ),
            font_size=23,
            color=WHITE,
        )
        compensation.next_to(titre, DOWN, buff=0.6)

        with self.voiceover(
            text=(
                "Retenons ce principe essentiel : l'expansion océanique aux "
                "dorsales est compensée par la destruction de lithosphère "
                "dans les fosses de subduction. Ainsi, la surface totale du "
                "globe reste constante : ce qui se crée d'un côté disparaît "
                "de l'autre."
            )
        ) as tracker:
            self.play(FadeIn(compensation))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(compensation), FadeOut(titre))
