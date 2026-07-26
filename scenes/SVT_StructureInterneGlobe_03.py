"""
scenes/SVT_StructureInterneGlobe_03.py — Chapitre 7 (1ereC, SVT), scène 03.

§ I.2 Les indices indirects (2/2) : le champ magnétique terrestre (point de
Curie 578°C, effet dynamo, argument pour un noyau externe liquide en
fer-nickel) + la chaleur interne (sources chaudes, geysers, gradient
~3°C/100m) + les ondes sismiques, « la lumière qui éclaire l'intérieur de
la Terre ». Source : 1ereC/SVT.pdf, page 71.
"""

import textwrap

from manim import (
    DOWN,
    LEFT,
    ORANGE,
    RIGHT,
    UP,
    WHITE,
    YELLOW,
    Arrow,
    Circle,
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


def _bullets(items, font_size=23, color=WHITE, width=52):
    lines = VGroup(
        *[Text(f"• {_wrap(it, width=width)}", font_size=font_size, color=color) for it in items]
    )
    lines.arrange(DOWN, aligned_edge=LEFT, buff=0.22)
    return lines


class ChampMagnetiqueChaleurEtOndes(NotionScene):
    def construct(self):
        titre = scene_title("I.2 — Les indices indirects (2/2)")
        titre.scale(0.68)
        titre.to_edge(UP)

        # --- Énoncé : la Terre se comporte comme un aimant -------------------
        intro = Text(
            _wrap(
                "La Terre se comporte comme un aimant : une boussole "
                "s'oriente toujours vers le nord magnétique. D'où vient ce "
                "champ magnétique, alors que les roches de surface perdent "
                "leur aimantation dès quelques dizaines de km de profondeur ?",
                width=56,
            ),
            font_size=23,
            color=WHITE,
        )
        intro.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "La Terre se comporte comme un immense aimant : une boussole "
                "s'oriente toujours vers le nord magnétique. Mais d'où vient "
                "ce champ magnétique, alors que les roches de surface "
                "perdent leur aimantation dès quelques dizaines de "
                "kilomètres de profondeur ?"
            )
        ) as tracker:
            self.play(Write(titre))
            self.play(FadeIn(intro))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(intro))

        # --- Animation du raisonnement : point de Curie et effet dynamo ------
        definition_curie = definition_box(
            Text(
                _wrap(
                    "Un aimant permanent perd son aimantation au-dessus "
                    "d'une certaine température : le point de Curie (578°C "
                    "pour la magnétite), dépassé dès quelques dizaines de "
                    "km de profondeur. Le champ magnétique actuel ne peut "
                    "donc pas venir de roches aimantées en profondeur.",
                    width=54,
                ),
                font_size=21,
            ),
            box_width=11.9,
        )
        definition_curie.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Un aimant permanent perd son aimantation au-dessus d'une "
                "certaine température, appelée point de Curie, qui vaut "
                "cinq cent soixante-dix-huit degrés pour la magnétite. Cette "
                "température est dépassée dès quelques dizaines de "
                "kilomètres de profondeur. Le champ magnétique actuel ne "
                "peut donc pas venir de roches aimantées comme un vulgaire "
                "aimant de réfrigérateur."
            )
        ) as tracker:
            self.play(FadeIn(definition_curie))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(definition_curie))

        # Schéma effet dynamo : noyau avec mouvements et lignes de champ
        noyau = Circle(radius=0.9, color=ORANGE, fill_color=ORANGE, fill_opacity=0.6)
        fleche1 = Arrow(noyau.get_center() + LEFT * 0.3, noyau.get_center() + LEFT * 0.3 + UP * 0.6, color=YELLOW, buff=0)
        fleche2 = Arrow(noyau.get_center() + RIGHT * 0.3, noyau.get_center() + RIGHT * 0.3 + DOWN * 0.6, color=YELLOW, buff=0)
        label_noyau = Text("Fer liquide en\nmouvement (noyau externe)", font_size=15, color=WHITE)
        label_noyau.next_to(noyau, DOWN, buff=0.35)

        ligne_champ = Line(noyau.get_top() + UP * 0.2, noyau.get_top() + UP * 1.6, color="#4DABF7", stroke_width=3)
        ligne_champ2 = Line(noyau.get_bottom() + DOWN * 0.2, noyau.get_bottom() + DOWN * 1.6, color="#4DABF7", stroke_width=3)
        label_champ = Text("Champ magnétique\n(effet dynamo)", font_size=15, color="#4DABF7")
        label_champ.next_to(noyau, RIGHT, buff=1.4)

        schema = VGroup(noyau, fleche1, fleche2, label_noyau, ligne_champ, ligne_champ2, label_champ)
        schema.next_to(titre, DOWN, buff=0.5)

        arg_dynamo = property_box(
            Text(
                _wrap(
                    "Le champ magnétique s'explique par des mouvements d'un "
                    "matériau métallique liquide conducteur au sein du "
                    "globe : c'est l'effet « dynamo ». Argument fort en "
                    "faveur d'un noyau externe liquide en fer-nickel.",
                    width=54,
                ),
                font_size=21,
            ),
            box_width=11.9,
        )

        with self.voiceover(
            text=(
                "Le champ magnétique actuel s'explique par des mouvements "
                "d'un matériau métallique liquide et conducteur au sein du "
                "globe : c'est l'effet dynamo, comparable à celui d'une "
                "génératrice électrique. C'est un argument fort en faveur "
                "d'un noyau externe liquide, composé de fer et de nickel."
            )
        ) as tracker:
            self.play(FadeIn(schema))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(schema))

        arg_dynamo.next_to(titre, DOWN, buff=0.5)
        with self.voiceover(
            text="Résumons cet argument dans une propriété à retenir."
        ) as tracker:
            self.play(FadeIn(arg_dynamo))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(arg_dynamo))

        # --- Chaleur interne et ondes sismiques -------------------------------
        chaleur = definition_box(
            Text(
                _wrap(
                    "Les sources d'eau chaude, les geysers, les volcans et "
                    "l'augmentation de la température dans les mines et "
                    "forages (environ 3°C tous les 100 m) prouvent que "
                    "l'intérieur du globe est chaud.",
                    width=54,
                ),
                font_size=22,
            ),
            box_width=11.9,
        )
        chaleur.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Autre indice indirect : la chaleur interne. Les sources "
                "d'eau chaude, les geysers, les volcans et l'augmentation de "
                "la température dans les mines et les forages, environ "
                "trois degrés tous les cent mètres, prouvent que l'intérieur "
                "du globe est chaud."
            )
        ) as tracker:
            self.play(FadeIn(chaleur))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(chaleur))

        # --- Exemple traité : le forage de Kola et le gradient ---------------
        exemple = example_box(
            Text(
                _wrap(
                    "Au fond du forage de Kola (12 262 m), la température "
                    "atteint environ 180°C. Avec un gradient de 3°C/100 m, "
                    "vérifier cet ordre de grandeur.",
                    width=54,
                ),
                font_size=23,
            ),
            box_width=12.0,
        )
        exemple.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Exemple traité : au fond du forage de Kola, à douze mille "
                "deux cent soixante-deux mètres, la température atteint "
                "environ cent quatre-vingts degrés. Vérifions cet ordre de "
                "grandeur avec un gradient de trois degrés tous les cent "
                "mètres : douze mille deux cent soixante-deux mètres, soit "
                "environ cent vingt-trois fois cent mètres, multipliés par "
                "trois degrés, donnent environ trois cent soixante-neuf "
                "degrés. L'ordre de grandeur est cohérent avec une "
                "température de surface ajoutée, même si la valeur exacte "
                "dépend des roches traversées localement."
            )
        ) as tracker:
            self.play(FadeIn(exemple))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(exemple))

        # --- Les ondes sismiques : transition vers la partie II -------------
        ondes_intro = Text(
            _wrap(
                "C'est l'outil essentiel de la sismologie : comme les rayons "
                "X en médecine, les ondes émises lors des séismes "
                "traversent le globe. Leur propagation renseigne sur la "
                "nature des milieux traversés : c'est la « lumière » qui "
                "éclaire l'intérieur de la Terre.",
                width=56,
            ),
            font_size=23,
            color=WHITE,
        )
        ondes_intro.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Enfin, le dernier et le plus puissant des indices "
                "indirects : les ondes sismiques. Comme les rayons X en "
                "médecine, les ondes émises lors des séismes traversent le "
                "globe entier, et leur propagation renseigne sur la nature "
                "des milieux traversés. On peut les appeler la lumière qui "
                "éclaire l'intérieur de la Terre : ce sera l'objet de toute "
                "la partie suivante de ce chapitre."
            )
        ) as tracker:
            self.play(FadeIn(ondes_intro))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(ondes_intro))

        # --- À retenir ---------------------------------------------------------
        retenir = _bullets(
            [
                "Champ magnétique : point de Curie (578°C) dépassé en profondeur → effet dynamo → noyau externe liquide.",
                "Chaleur interne : gradient géothermique ~3°C/100 m près de la surface.",
                "Ondes sismiques : outil le plus puissant pour explorer tout l'intérieur du globe.",
            ],
            width=50,
        )
        entete_retenir = Text("À retenir", font_size=27, color=YELLOW, weight="BOLD")
        entete_retenir.next_to(titre, DOWN, buff=0.5)
        retenir.next_to(entete_retenir, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "À retenir : le champ magnétique s'explique par l'effet "
                "dynamo d'un noyau externe liquide, puisque le point de "
                "Curie est dépassé en profondeur. La chaleur interne suit un "
                "gradient géothermique d'environ trois degrés tous les cent "
                "mètres près de la surface. Et les ondes sismiques "
                "constituent l'outil le plus puissant pour explorer tout "
                "l'intérieur du globe."
            )
        ) as tracker:
            self.play(FadeIn(entete_retenir))
            self.play(FadeIn(retenir))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(entete_retenir), FadeOut(retenir))

        # --- Piège à éviter -----------------------------------------------------
        piege = warning_box(
            Text(
                _wrap(
                    "Ne pas croire que le noyau serait un gigantesque aimant "
                    "« aimanté » comme une roche : la température y est bien "
                    "trop élevée pour cela. Le champ magnétique vient d'un "
                    "mouvement de matière conductrice (effet dynamo), pas "
                    "d'une aimantation permanente.",
                    width=54,
                ),
                font_size=22,
            ),
            box_width=12.0,
        )
        piege.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Attention, piège à éviter : ne croyez pas que le noyau "
                "serait un gigantesque aimant permanent, comme une roche "
                "aimantée. La température y est bien trop élevée pour cela, "
                "largement au-dessus du point de Curie. Le champ magnétique "
                "vient d'un mouvement de matière conductrice, l'effet "
                "dynamo, et non d'une aimantation permanente."
            )
        ) as tracker:
            self.play(FadeIn(piege))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(titre), FadeOut(piege))
