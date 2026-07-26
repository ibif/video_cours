"""
scenes/SVT_MouvementsPlaques_04.py — Chapitre 7 (1ereD, SVT), scène 04.

§ 7.2.1-7.2.2 Les dorsales océaniques et le paléomagnétisme : définition de
la dorsale (rift axial, laves, séismes), définition du paléomagnétisme,
propriété de la symétrie des bandes magnétiques (expansion océanique).
Source : 1ereD/SVT.pdf, pages 93-94.
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
    FadeIn,
    FadeOut,
    Polygon,
    Rectangle,
    Text,
    VGroup,
    Write,
    GRAY_C,
    BLUE_D,
)

from shapes.base_scene import NotionScene
from shapes.boxes import definition_box, property_box, scene_title


def _wrap(text: str, width: int = 56) -> str:
    return "\n".join(textwrap.fill(line, width=width) for line in text.split("\n"))


def _schema_dorsale():
    """Coupe simplifiée d'une dorsale : plancher océanique + rift axial + laves."""
    ocean = Rectangle(width=9.0, height=1.4, fill_color=BLUE_E, fill_opacity=0.5, stroke_width=0)

    flanc_gauche = Polygon(
        [-4.5, -0.3, 0], [-0.5, -0.3, 0], [-0.15, 0.55, 0], [-4.5, 0.55, 0],
        fill_color=GRAY_C, fill_opacity=1, stroke_color=WHITE, stroke_width=1,
    )
    flanc_droit = Polygon(
        [4.5, -0.3, 0], [0.5, -0.3, 0], [0.15, 0.55, 0], [4.5, 0.55, 0],
        fill_color=GRAY_C, fill_opacity=1, stroke_color=WHITE, stroke_width=1,
    )
    rift = Polygon(
        [-0.5, -0.3, 0], [0.5, -0.3, 0], [0.15, 0.55, 0], [-0.15, 0.55, 0],
        fill_color=RED, fill_opacity=0.85, stroke_color=WHITE, stroke_width=1,
    )
    ocean.move_to(flanc_gauche.get_center() + UP * 1.3)
    ocean.stretch_to_fit_width(9.0)

    fleche_lave = Arrow(
        start=[0, -0.9, 0], end=[0, -0.05, 0], color=YELLOW, buff=0, stroke_width=5, max_tip_length_to_length_ratio=0.35
    )
    label_lave = Text("laves basaltiques", font_size=16, color=YELLOW)
    label_lave.next_to(fleche_lave, DOWN, buff=0.12)

    label_rift = Text("rift axial", font_size=16, color=WHITE)
    label_rift.next_to(rift, UP, buff=0.15)

    fleche_g = Arrow(start=[-0.6, 0.1, 0], end=[-2.2, 0.1, 0], color=WHITE, buff=0, stroke_width=3)
    fleche_d = Arrow(start=[0.6, 0.1, 0], end=[2.2, 0.1, 0], color=WHITE, buff=0, stroke_width=3)

    return VGroup(ocean, flanc_gauche, flanc_droit, rift, fleche_lave, label_lave, label_rift, fleche_g, fleche_d)


def _schema_paleomag():
    """Bandes d'aimantation alternées, symétriques par rapport à l'axe."""
    n_bandes = 6
    largeur = 0.7
    bandes = VGroup()
    for i in range(-n_bandes, n_bandes + 1):
        couleur = BLUE_D if i % 2 == 0 else RED
        bande = Rectangle(
            width=largeur, height=1.0, fill_color=couleur, fill_opacity=0.85, stroke_color=WHITE, stroke_width=0.5
        )
        bande.move_to([i * largeur, 0, 0])
        bandes.add(bande)

    axe = Rectangle(width=0.06, height=1.4, fill_color=YELLOW, fill_opacity=1, stroke_width=0)
    axe.move_to([0, 0, 0])

    label_normale = Text("aimantation normale", font_size=14, color=WHITE)
    legende_n = Rectangle(width=0.35, height=0.25, fill_color=BLUE_D, fill_opacity=0.85, stroke_width=0)
    legende_normale = VGroup(legende_n, label_normale).arrange(RIGHT, buff=0.15)

    label_inverse = Text("aimantation inverse", font_size=14, color=WHITE)
    legende_i = Rectangle(width=0.35, height=0.25, fill_color=RED, fill_opacity=0.85, stroke_width=0)
    legende_inverse = VGroup(legende_i, label_inverse).arrange(RIGHT, buff=0.15)

    legende = VGroup(legende_normale, legende_inverse).arrange(RIGHT, buff=0.7)
    legende.next_to(bandes, DOWN, buff=0.4)

    label_axe = Text("axe de la dorsale", font_size=14, color=YELLOW)
    label_axe.next_to(axe, UP, buff=0.1)

    return VGroup(bandes, axe, label_axe, legende)


class DorsalesEtPaleomagnetisme(NotionScene):
    def construct(self):
        titre = scene_title("7.2 — Dorsales et paléomagnétisme")
        titre.scale(0.68)
        titre.to_edge(UP)

        # --- Énoncé : définition de la dorsale --------------------------------
        definition_dorsale = definition_box(
            Text(
                _wrap(
                    "Une dorsale océanique est une chaîne de montagnes "
                    "sous-marines de plusieurs milliers de km, avec un rift "
                    "axial (dépression étroite à l'axe). Laves basaltiques "
                    "s'en échappent, séismes superficiels nombreux. Réseau "
                    "continu d'environ 60 000 km.",
                    width=54,
                ),
                font_size=22,
            ),
            box_width=11.8,
        )
        definition_dorsale.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Comment prouver que les plaques bougent réellement ? "
                "Première preuve : les dorsales océaniques. Une dorsale "
                "océanique est une chaîne de montagnes sous-marines, "
                "longue de plusieurs milliers de kilomètres, avec en son "
                "centre un rift axial, une dépression étroite. Des laves "
                "basaltiques s'en échappent, et de nombreux séismes "
                "superficiels s'y produisent. L'ensemble forme un réseau "
                "continu d'environ soixante mille kilomètres, qui fait le "
                "tour du globe."
            )
        ) as tracker:
            self.play(Write(titre))
            self.play(FadeIn(definition_dorsale))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(definition_dorsale))

        # --- Animation du raisonnement : schéma de la dorsale ------------------
        schema_dorsale = _schema_dorsale()
        schema_dorsale.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Voici une coupe simplifiée d'une dorsale : de part et "
                "d'autre du rift axial, où remontent les laves, les deux "
                "flancs de plancher océanique s'écartent lentement l'un de "
                "l'autre. La dorsale médio-atlantique, précisément, sépare "
                "les plaques africaine et sud-américaine ; en Islande, elle "
                "émerge même au-dessus du niveau de la mer, ce qui permet "
                "de l'observer directement à terre."
            )
        ) as tracker:
            self.play(FadeIn(schema_dorsale))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(schema_dorsale))

        # --- Exemple traité : le paléomagnétisme, un enregistreur -------------
        definition_paleomag = definition_box(
            Text(
                _wrap(
                    "Le champ magnétique terrestre s'est inversé de nombreuses "
                    "fois (le pôle Nord magnétique a parfois occupé la "
                    "position du pôle Sud). Quand une lave basaltique se "
                    "solidifie à une dorsale, ses minéraux magnétiques "
                    "(magnétite) s'orientent comme des boussoles et "
                    "conservent la direction du champ de l'époque : c'est le "
                    "paléomagnétisme.",
                    width=54,
                ),
                font_size=21,
            ),
            box_width=11.8,
        )
        definition_paleomag.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Deuxième preuve, plus subtile : le paléomagnétisme. Le "
                "champ magnétique terrestre s'est inversé de très "
                "nombreuses fois au cours de l'histoire de la Terre : le "
                "pôle Nord magnétique a parfois occupé la position du pôle "
                "Sud. Or, quand une lave basaltique se solidifie au niveau "
                "d'une dorsale, ses minéraux magnétiques, la magnétite, "
                "s'orientent comme de minuscules boussoles et conservent "
                "pour toujours la direction du champ magnétique de "
                "l'époque. On appelle cela le paléomagnétisme : la roche "
                "enregistre et garde en mémoire le champ magnétique du "
                "passé."
            )
        ) as tracker:
            self.play(FadeIn(definition_paleomag))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(definition_paleomag))

        schema_paleomag = _schema_paleomag()
        schema_paleomag.next_to(titre, DOWN, buff=0.7)

        propriete_bandes = property_box(
            Text(
                _wrap(
                    "De part et d'autre de l'axe d'une dorsale, le plancher "
                    "océanique présente des bandes alternativement à "
                    "aimantation normale et inverse, symétriques par rapport "
                    "à l'axe. Explication : la croûte océanique se forme à "
                    "l'axe, enregistre le champ du moment, puis s'écarte "
                    "lentement de part et d'autre (deux tapis roulants en "
                    "sens opposés) : c'est l'expansion océanique.",
                    width=54,
                ),
                font_size=21,
            ),
            box_width=11.8,
        )

        with self.voiceover(
            text=(
                "En étudiant le plancher océanique de part et d'autre de "
                "l'axe d'une dorsale, les géologues ont fait une découverte "
                "extraordinaire : des bandes alternativement à aimantation "
                "normale, en bleu ici, et inverse, en rouge, disposées de "
                "façon parfaitement symétrique par rapport à l'axe. "
                "L'explication est la suivante : la croûte océanique se "
                "forme continuellement à l'axe de la dorsale, enregistre le "
                "champ magnétique du moment, puis s'écarte lentement de "
                "part et d'autre, comme deux tapis roulants avançant en "
                "sens opposés. Ce phénomène porte un nom : l'expansion "
                "océanique."
            )
        ) as tracker:
            self.play(FadeIn(schema_paleomag))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(schema_paleomag))

        propriete_bandes.next_to(titre, DOWN, buff=0.5)
        self.play(FadeIn(propriete_bandes))
        self.wait(1.5)
        self.play(FadeOut(titre), FadeOut(propriete_bandes))
