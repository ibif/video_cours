"""
scenes/SVT_TectoniquePlaques_03.py — Chapitre 8 (1ereC, SVT), scène 03.

II.B.2-3 Arguments paléontologiques (tableau des 4 fossiles) et
paléoclimatiques (tillites, charbon, évaporites, définition tillite) ;
tableau récapitulatif des 4 types d'arguments de Wegener ; §C portée et
limites de l'hypothèse. Source : 1ereC/SVT.pdf, pages 86-87.
"""

import textwrap

from manim import DOWN, LEFT, UP, WHITE, YELLOW, FadeIn, FadeOut, Table, Text, VGroup, Write

from shapes.base_scene import NotionScene
from shapes.boxes import definition_box, scene_title, warning_box


def _wrap(text: str, width: int = 56) -> str:
    return "\n".join(textwrap.fill(line, width=width) for line in text.split("\n"))


def _bullets(items, font_size=24, color=WHITE, width=54):
    lines = VGroup(
        *[Text(f"• {_wrap(it, width=width)}", font_size=font_size, color=color) for it in items]
    )
    lines.arrange(DOWN, aligned_edge=LEFT, buff=0.22)
    return lines


def _table(rows, col_labels, font_size=19, col_width=None):
    t = Table(
        rows,
        col_labels=[Text(c, font_size=font_size + 2, weight="BOLD") for c in col_labels],
        element_to_mobject=Text,
        element_to_mobject_config={"font_size": font_size},
        line_config={"color": WHITE, "stroke_width": 1},
        include_outer_lines=True,
    )
    t.get_entries().set_color(WHITE)
    t.get_col_labels().set_color(YELLOW)
    for line in t.get_horizontal_lines():
        line.set_color(WHITE)
    for line in t.get_vertical_lines():
        line.set_color(WHITE)
    return t


class ArgumentsPaleontologiquesEtClimatiques(NotionScene):
    def construct(self):
        titre = scene_title("II. La dérive des continents — les preuves")
        titre.scale(0.6)
        titre.to_edge(UP)
        self.play(Write(titre))

        # --- Énoncé : arguments paléontologiques ----------------------------
        entete = Text("Arguments paléontologiques", font_size=26, color=YELLOW, weight="BOLD")
        entete.next_to(titre, DOWN, buff=0.45)

        intro = Text(
            _wrap(
                "On retrouve les mêmes fossiles sur des continents "
                "aujourd'hui séparés par de vastes océans :",
                width=54,
            ),
            font_size=23,
            color=WHITE,
        )
        intro.next_to(entete, DOWN, buff=0.3)

        with self.voiceover(
            text=(
                "Deuxième famille d'arguments : les arguments "
                "paléontologiques. On retrouve les mêmes fossiles sur des "
                "continents aujourd'hui séparés par de vastes océans."
            )
        ) as tracker:
            self.play(FadeIn(entete))
            self.play(FadeIn(intro))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(intro))

        # --- Animation du raisonnement : tableau des 4 fossiles -------------
        fossiles_table = _table(
            [
                ["Mesosaurus", "Reptile d'eau douce (~280 Ma)", "Brésil, Afrique du Sud"],
                ["Glossopteris", "Fougère à graines (flore)", "Am. du Sud, Afrique, Inde,\nAntarctique, Australie"],
                ["Lystrosaurus", "Reptile terrestre", "Afrique, Inde, Antarctique"],
                ["Cynognathus", "Reptile terrestre", "Amérique du Sud, Afrique"],
            ],
            col_labels=["Fossile", "Nature", "Répartition"],
            font_size=18,
        )
        fossiles_table.set(width=12.5)
        fossiles_table.next_to(entete, DOWN, buff=0.35)

        with self.voiceover(
            text=(
                "Quatre fossiles emblématiques. Le Mesosaurus, un reptile "
                "d'eau douce vieux d'environ deux cent quatre-vingts "
                "millions d'années, se trouve au Brésil et en Afrique du "
                "Sud. Le Glossopteris, une fougère à graines, se retrouve en "
                "Amérique du Sud, en Afrique, en Inde, en Antarctique et en "
                "Australie. Le Lystrosaurus, un reptile terrestre, en "
                "Afrique, en Inde et en Antarctique. Et le Cynognathus, "
                "également un reptile terrestre, en Amérique du Sud et en "
                "Afrique."
            )
        ) as tracker:
            self.play(FadeIn(fossiles_table))
            self.wait(tracker.get_remaining_duration())

        with self.voiceover(
            text=(
                "Or le Mesosaurus, animal d'eau douce, ne pouvait "
                "absolument pas traverser l'océan Atlantique à la nage : "
                "les continents où l'on retrouve ses fossiles devaient donc "
                "être réunis à son époque."
            )
        ) as tracker:
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(entete), FadeOut(fossiles_table))

        # --- Arguments paléoclimatiques + définition tillite -----------------
        entete_clim = Text("Arguments paléoclimatiques", font_size=26, color=YELLOW, weight="BOLD")
        entete_clim.next_to(titre, DOWN, buff=0.45)

        clim = _bullets(
            [
                "Des tillites et des stries glaciaires, datées d'environ "
                "-300 Ma, existent en Afrique du Sud, en Amérique du Sud, "
                "en Inde et en Australie : ces régions aujourd'hui "
                "tropicales ont connu un climat glaciaire. En rapprochant "
                "les continents, les stries convergent vers un même "
                "centre glaciaire.",
                "Des gisements de charbon (climat chaud et humide) et des "
                "évaporites (climat chaud et sec) se trouvent aujourd'hui "
                "sous de hautes latitudes (Spitzberg) : ces terres ont "
                "donc changé de latitude.",
            ],
            font_size=21,
            width=52,
        )
        clim.next_to(entete_clim, DOWN, buff=0.35)

        with self.voiceover(
            text=(
                "Troisième famille d'arguments : les arguments "
                "paléoclimatiques. Des tillites et des stries gravées par "
                "les glaciers, datées d'environ moins trois cents millions "
                "d'années, existent en Afrique du Sud, en Amérique du Sud, "
                "en Inde et en Australie : ces régions, aujourd'hui "
                "tropicales, ont pourtant connu un climat glaciaire. Si l'on "
                "rapproche les continents, les stries convergent vers un "
                "même centre glaciaire. À l'inverse, des gisements de "
                "charbon, signe d'un climat chaud et humide, et des "
                "évaporites, signe d'un climat chaud et sec, se trouvent "
                "aujourd'hui sous de très hautes latitudes, comme au "
                "Spitzberg : ces terres ont donc changé de latitude depuis "
                "leur formation."
            )
        ) as tracker:
            self.play(FadeIn(entete_clim))
            self.play(FadeIn(clim))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(entete_clim), FadeOut(clim))

        def_tillite = definition_box(
            Text(
                _wrap(
                    "Tillite : roche détritique consolidée, formée par "
                    "l'accumulation de débris transportés puis déposés par "
                    "un glacier. Sa présence témoigne d'un climat glaciaire "
                    "ancien.",
                    width=54,
                ),
                font_size=23,
            ),
            box_width=12.0,
        )
        def_tillite.next_to(titre, DOWN, buff=0.55)

        with self.voiceover(
            text=(
                "Retenons la définition d'une tillite : c'est une roche "
                "détritique consolidée, formée par l'accumulation de "
                "débris transportés puis déposés par un glacier. Sa "
                "présence témoigne d'un climat glaciaire ancien."
            )
        ) as tracker:
            self.play(FadeIn(def_tillite))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(def_tillite))

        # --- Exemple traité : tableau récapitulatif des 4 arguments ---------
        entete_recap = Text("Tableau récapitulatif des arguments", font_size=25, color=YELLOW, weight="BOLD")
        entete_recap.next_to(titre, DOWN, buff=0.4)

        recap_table = _table(
            [
                ["Géométrique", "Emboîtement\nAfrique / Am. du Sud", "Les continents\nétaient réunis"],
                ["Géologique", "Continuité\nAppalaches-Calédonides", "Chaînes formées\nensemble, puis séparées"],
                ["Paléontologique", "Mesosaurus,\nGlossopteris", "Continents réunis à\nl'époque des fossiles"],
                ["Paléoclimatique", "Tillites tropicales,\ncharbon arctique", "Les continents ont\nchangé de position"],
            ],
            col_labels=["Type d'argument", "Exemple", "Conclusion"],
            font_size=17,
        )
        recap_table.set(width=12.5)
        recap_table.next_to(entete_recap, DOWN, buff=0.3)

        with self.voiceover(
            text=(
                "Résumons les quatre types d'arguments réunis par Wegener. "
                "L'argument géométrique, l'emboîtement de l'Afrique et de "
                "l'Amérique du Sud, montre que les continents étaient "
                "réunis. L'argument géologique, la continuité des "
                "Appalaches et des Calédonides, montre que ces chaînes se "
                "sont formées ensemble avant d'être séparées. L'argument "
                "paléontologique, le Mesosaurus et le Glossopteris, montre "
                "que les continents étaient réunis à l'époque de ces "
                "fossiles. Et l'argument paléoclimatique, les tillites "
                "tropicales et le charbon arctique, montre que les "
                "continents ont changé de position au fil du temps."
            )
        ) as tracker:
            self.play(FadeIn(entete_recap))
            self.play(FadeIn(recap_table))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(entete_recap), FadeOut(recap_table))

        # --- À retenir / piège : portée et limites de l'hypothèse ------------
        limites = warning_box(
            Text(
                _wrap(
                    "Portée et limites : Wegener n'a pas su proposer de "
                    "mécanisme capable de déplacer les continents (les "
                    "forces qu'il invoquait, marées, rotation terrestre, "
                    "sont des millions de fois trop faibles). Sa théorie "
                    "est rejetée par la majorité des géologues de son "
                    "époque. Elle sera confirmée dans les années 1960 par "
                    "la découverte de l'expansion océanique.",
                    width=54,
                ),
                font_size=21,
            ),
            box_width=12.2,
        )
        limites.next_to(titre, DOWN, buff=0.55)

        with self.voiceover(
            text=(
                "Mais Wegener n'a pas su proposer de mécanisme capable de "
                "déplacer des continents entiers : les forces qu'il "
                "invoquait, comme les marées ou la rotation terrestre, sont "
                "des millions de fois trop faibles. Sa théorie est donc "
                "rejetée par la majorité des géologues de son époque. Elle "
                "sera confirmée seulement dans les années mille neuf cent "
                "soixante, par la découverte de l'expansion océanique, "
                "fondement de la théorie de la tectonique des plaques, que "
                "nous allons étudier dans la partie suivante."
            )
        ) as tracker:
            self.play(FadeIn(limites))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(limites), FadeOut(titre))
