"""
scenes/SVT_TectoniquePlaques_02.py — Chapitre 8 (1ereC, SVT), scène 02.

II. Les arguments de la dérive des continents (A. Wegener, 1912).
§A l'hypothèse de Wegener (Pangée/Panthalassa, Laurasie/Gondwana) ; §B.1
arguments géométriques et géologiques (complémentarité des rivages,
continuité Appalaches-Calédonides, continuité des provinces d'âge
Brésil/Côte d'Ivoire). Source : 1ereC/SVT.pdf, pages 85-86.
"""

import textwrap

from manim import (
    BLUE_E,
    DOWN,
    GREEN_D,
    LEFT,
    ORANGE,
    RIGHT,
    UP,
    WHITE,
    YELLOW,
    Circle,
    FadeIn,
    FadeOut,
    Polygon,
    Text,
    VGroup,
    Write,
)

from shapes.base_scene import NotionScene
from shapes.boxes import scene_title, warning_box


def _wrap(text: str, width: int = 56) -> str:
    return "\n".join(textwrap.fill(line, width=width) for line in text.split("\n"))


def _bullets(items, font_size=24, color=WHITE, width=54):
    lines = VGroup(
        *[Text(f"• {_wrap(it, width=width)}", font_size=font_size, color=color) for it in items]
    )
    lines.arrange(DOWN, aligned_edge=LEFT, buff=0.22)
    return lines


class DeriveDesContinentsWegener(NotionScene):
    def construct(self):
        titre = scene_title("II. La dérive des continents (Wegener, 1912)")
        titre.scale(0.62)
        titre.to_edge(UP)
        self.play(Write(titre))

        # --- Énoncé : Wegener et son hypothèse ------------------------------
        intro = Text(
            _wrap(
                "En 1912, le météorologue allemand Alfred Wegener émet "
                "l'hypothèse de la dérive des continents, exposée dans « La "
                "genèse des continents et des océans » (1915).",
                width=56,
            ),
            font_size=25,
            color=WHITE,
        )
        intro.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "En dix-neuf cent douze, le météorologue allemand Alfred "
                "Wegener émet l'hypothèse de la dérive des continents, "
                "qu'il expose dans son ouvrage « La genèse des continents "
                "et des océans », publié en dix-neuf cent quinze."
            )
        ) as tracker:
            self.play(FadeIn(intro))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(intro))

        # --- Schéma : Pangée -> fragmentation -> continents actuels ---------
        pangee = Circle(radius=1.5, fill_color=ORANGE, fill_opacity=0.7, stroke_color=WHITE, stroke_width=2)
        ocean_pangee = Circle(radius=2.3, fill_color=BLUE_E, fill_opacity=0.4, stroke_color=WHITE, stroke_width=1)
        ocean_pangee.move_to(pangee.get_center())
        label_pangee = Text("Pangée", font_size=22, color=WHITE, weight="BOLD")
        label_pangee.move_to(pangee.get_center())
        label_panthalassa = Text("Panthalassa", font_size=18, color=WHITE)
        label_panthalassa.move_to(ocean_pangee.get_bottom() + UP * 0.35)
        schema_pangee = VGroup(ocean_pangee, pangee, label_pangee, label_panthalassa)
        schema_pangee.next_to(titre, DOWN, buff=0.55)

        with self.voiceover(
            text=(
                "Il y a environ trois cents millions d'années, tous les "
                "continents actuels étaient réunis en un unique "
                "supercontinent, la Pangée, ce qui signifie « toute la "
                "Terre », entouré d'un océan unique, la Panthalassa."
            )
        ) as tracker:
            self.play(FadeIn(ocean_pangee), FadeIn(pangee))
            self.play(Write(label_pangee), FadeIn(label_panthalassa))
            self.wait(tracker.get_remaining_duration())

        laurasie = Polygon(
            [-0.9, 0.2, 0], [0.9, 0.5, 0], [1.1, 1.4, 0], [-1.1, 1.4, 0],
            fill_color=GREEN_D, fill_opacity=0.75, stroke_color=WHITE, stroke_width=1,
        )
        gondwana = Polygon(
            [-1.1, -0.1, 0], [1.1, -0.4, 0], [0.9, -1.4, 0], [-0.9, -1.4, 0],
            fill_color=ORANGE, fill_opacity=0.75, stroke_color=WHITE, stroke_width=1,
        )
        label_laurasie = Text("Laurasie (Nord)", font_size=18, color=WHITE)
        label_laurasie.move_to(laurasie.get_center())
        label_gondwana = Text("Gondwana (Sud)", font_size=18, color=WHITE)
        label_gondwana.move_to(gondwana.get_center())
        fragmentation = VGroup(laurasie, gondwana, label_laurasie, label_gondwana)
        fragmentation.move_to(schema_pangee.get_center())

        with self.voiceover(
            text=(
                "La Pangée s'est ensuite fragmentée en deux grands blocs : "
                "la Laurasie au nord, et le Gondwana au sud. Puis les blocs "
                "continentaux ont lentement dérivé, sur des centaines de "
                "millions d'années, jusqu'à leurs positions actuelles."
            )
        ) as tracker:
            self.play(FadeOut(label_pangee), FadeOut(pangee))
            self.play(FadeIn(laurasie), FadeIn(label_laurasie))
            self.play(FadeIn(gondwana), FadeIn(label_gondwana))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(schema_pangee), FadeOut(fragmentation))

        # --- Animation du raisonnement : arguments géométriques -----------
        entete_args = Text(
            "Les arguments géométriques et géologiques", font_size=26, color=YELLOW, weight="BOLD"
        )
        entete_args.next_to(titre, DOWN, buff=0.5)

        arg1 = _bullets(
            [
                "Complémentarité des rivages : les côtes de l'Amérique du "
                "Sud et de l'Afrique s'emboîtent comme les pièces d'un "
                "puzzle (mieux encore avec les bords des plateaux "
                "continentaux).",
                "Continuité des chaînes de montagnes : les Appalaches "
                "(Amérique du Nord) se prolongent par les chaînes "
                "calédoniennes d'Europe — mêmes âges, mêmes roches, mêmes "
                "structures.",
                "Continuité des provinces d'âge : les socles anciens du "
                "Brésil et de l'Afrique de l'Ouest, dont le socle ivoirien, "
                "se correspondent exactement lorsqu'on referme "
                "l'Atlantique.",
            ],
            font_size=21,
            width=54,
        )
        arg1.next_to(entete_args, DOWN, buff=0.35)

        with self.voiceover(
            text=(
                "Wegener s'appuie d'abord sur des arguments géométriques et "
                "géologiques. Premier argument : la complémentarité des "
                "rivages. Les côtes de l'Amérique du Sud et de l'Afrique "
                "s'emboîtent comme les pièces d'un puzzle ; la "
                "correspondance est encore meilleure si l'on compare les "
                "bords des plateaux continentaux plutôt que les côtes "
                "actuelles. Deuxième argument : la continuité des chaînes "
                "de montagnes. Les Appalaches, en Amérique du Nord, se "
                "prolongent par les chaînes calédoniennes d'Europe, en "
                "Écosse et en Scandinavie : mêmes âges, mêmes roches, mêmes "
                "structures de part et d'autre de l'Atlantique Nord. "
                "Troisième argument : la continuité des provinces d'âge. "
                "Les socles anciens du Brésil et de l'Afrique de l'Ouest, "
                "dont le socle ivoirien, présentent des provinces d'âge qui "
                "se correspondent exactement lorsqu'on referme "
                "l'Atlantique."
            )
        ) as tracker:
            self.play(FadeIn(entete_args))
            self.play(FadeIn(arg1))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(entete_args), FadeOut(arg1))

        # --- Exemple traité : le puzzle Afrique / Amérique du Sud -----------
        afrique = Polygon(
            [0.3, 1.2, 0], [1.3, 1.0, 0], [1.5, -0.2, 0], [0.9, -1.3, 0], [0.2, -1.0, 0], [0.0, 0.2, 0],
            fill_color=ORANGE, fill_opacity=0.8, stroke_color=WHITE, stroke_width=1,
        )
        amerique_sud = Polygon(
            [-0.2, 1.0, 0], [-0.9, 0.9, 0], [-1.4, -0.3, 0], [-0.7, -1.3, 0], [-0.1, -1.0, 0], [0.0, 0.2, 0],
            fill_color=GREEN_D, fill_opacity=0.8, stroke_color=WHITE, stroke_width=1,
        )
        label_afr = Text("Afrique", font_size=18, color=WHITE).move_to(afrique.get_center())
        label_ams = Text("Amérique\ndu Sud", font_size=16, color=WHITE).move_to(amerique_sud.get_center())
        puzzle = VGroup(amerique_sud, afrique, label_ams, label_afr)
        puzzle.next_to(titre, DOWN, buff=0.55)

        with self.voiceover(
            text=(
                "Regardons ce puzzle : les bords des deux continents "
                "s'ajustent presque parfaitement, comme si l'océan "
                "Atlantique n'était qu'une déchirure récente dans un seul "
                "et même bloc continental."
            )
        ) as tracker:
            self.play(FadeIn(amerique_sud), FadeIn(label_ams))
            self.play(FadeIn(afrique), FadeIn(label_afr))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(puzzle))

        # --- À retenir / piège : Wegener n'a pas prouvé le mécanisme -------
        piege = warning_box(
            Text(
                _wrap(
                    "Ces arguments géométriques et géologiques montrent que "
                    "les continents ont été réunis, mais ne prouvent pas à "
                    "eux seuls un mécanisme de déplacement. D'autres "
                    "arguments — paléontologiques et paléoclimatiques — "
                    "viennent renforcer l'hypothèse (scène suivante).",
                    width=54,
                ),
                font_size=22,
            ),
            box_width=12.0,
        )
        piege.next_to(titre, DOWN, buff=0.55)

        with self.voiceover(
            text=(
                "Retenons que ces arguments géométriques et géologiques "
                "montrent que les continents ont été réunis dans le passé, "
                "mais ils ne prouvent pas à eux seuls un mécanisme de "
                "déplacement. D'autres arguments, paléontologiques et "
                "paléoclimatiques, viendront renforcer l'hypothèse de "
                "Wegener, comme nous allons le voir dans la scène "
                "suivante."
            )
        ) as tracker:
            self.play(FadeIn(piege))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(piege), FadeOut(titre))
