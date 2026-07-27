"""
scenes/Physique_IntroductionOptiqueGeometrique_06.py — Chapitre 11
« Introduction à l'optique géométrique » (1ereC, Physique), scène 06.

§ 4 (partie 2). Ombre et pénombre avec une source ÉTENDUE : construction
géométrique (tangentes croisées / non croisées). Exemple : pylône
électrique à Abidjan, ombre nette au soleil (source lointaine, quasi
ponctuelle) et floue sous un lampadaire proche (source étendue proche).
Source : 1ereC/Physique.pdf, pages 108-116 (chapitre 11, § 4).
"""

import textwrap

from manim import (
    DOWN,
    LEFT,
    RIGHT,
    UP,
    BLUE,
    GRAY,
    ORANGE,
    WHITE,
    YELLOW,
    Dot,
    FadeIn,
    FadeOut,
    Line,
    Text,
    VGroup,
    Write,
)

from shapes.base_scene import NotionScene
from shapes.boxes import definition_box, essentiel_box, example_box, scene_title, warning_box


def _wrap(text: str, width: int = 56) -> str:
    return "\n".join(textwrap.fill(line, width=width) for line in text.split("\n"))


def _construction_penombre() -> VGroup:
    """Source étendue représentée par deux points A (haut) et B (bas),
    objet opaque vertical, écran à droite : la zone d'ombre (aucun point
    de la source visible) et les deux zones de pénombre (une partie de la
    source visible) sont matérialisées par des segments colorés sur
    l'écran."""
    A = Dot(LEFT * 4.4 + UP * 0.5, color=YELLOW, radius=0.08)
    B = Dot(LEFT * 4.4 + DOWN * 0.5, color=YELLOW, radius=0.08)
    label_source = Text("source étendue", font_size=15, color=YELLOW)
    label_source.next_to(VGroup(A, B), LEFT, buff=0.15).rotate(1.5708)

    objet = Line(LEFT * 1.2 + UP * 0.5, LEFT * 1.2 + DOWN * 0.5, color=GRAY, stroke_width=8)

    ecran_x = 3.0
    ecran = Line(RIGHT * ecran_x + UP * 2.2, RIGHT * ecran_x + DOWN * 2.2, color=WHITE, stroke_width=4)
    label_ecran = Text("écran", font_size=15, color=WHITE).next_to(ecran, DOWN, buff=0.2)

    def prolonge(depart, vers, x_cible):
        direction = vers - depart
        t = (x_cible - depart[0]) / direction[0]
        return depart + direction * t

    haut_objet = objet.get_start()
    bas_objet = objet.get_end()

    # Rayons tangents depuis A (haut de la source) via le bas de l'objet,
    # et depuis B (bas de la source) via le haut de l'objet : ce sont ces
    # rayons "croisés" qui délimitent la pénombre.
    tA_bas = Line(A.get_center(), prolonge(A.get_center(), bas_objet, ecran_x), color=YELLOW, stroke_width=1.5)
    tB_haut = Line(B.get_center(), prolonge(B.get_center(), haut_objet, ecran_x), color=YELLOW, stroke_width=1.5)
    # Rayons tangents "non croisés" : A avec le haut de l'objet, B avec le bas.
    tA_haut = Line(A.get_center(), prolonge(A.get_center(), haut_objet, ecran_x), color=YELLOW, stroke_width=1.5)
    tB_bas = Line(B.get_center(), prolonge(B.get_center(), bas_objet, ecran_x), color=YELLOW, stroke_width=1.5)

    y_tA_haut = tA_haut.get_end()[1]
    y_tB_bas = tB_bas.get_end()[1]
    y_tA_bas = tA_bas.get_end()[1]
    y_tB_haut = tB_haut.get_end()[1]

    zone_ombre = Line(
        [ecran_x, min(y_tA_bas, y_tB_haut), 0], [ecran_x, max(y_tA_bas, y_tB_haut), 0] if y_tA_bas > y_tB_haut else [ecran_x, y_tB_haut, 0],
        color=BLUE, stroke_width=8,
    )
    # Zone d'ombre totale = entre les deux rayons croisés (les plus resserrés)
    zone_ombre = Line([ecran_x, min(y_tA_bas, y_tB_haut), 0], [ecran_x, max(y_tA_bas, y_tB_haut), 0], color=BLUE, stroke_width=8)
    label_ombre = Text("ombre", font_size=14, color=BLUE).next_to(zone_ombre, RIGHT, buff=0.12)

    zone_penombre_haut = Line([ecran_x, y_tA_haut, 0], [ecran_x, y_tB_haut, 0], color=ORANGE, stroke_width=8)
    zone_penombre_bas = Line([ecran_x, y_tA_bas, 0], [ecran_x, y_tB_bas, 0], color=ORANGE, stroke_width=8)
    label_penombre = Text("pénombre", font_size=14, color=ORANGE).next_to(zone_penombre_haut, RIGHT, buff=0.12).shift(UP * 0.3)

    return VGroup(
        A, B, label_source, objet, ecran, label_ecran,
        tA_bas, tB_haut, tA_haut, tB_bas,
        zone_ombre, label_ombre, zone_penombre_haut, zone_penombre_bas, label_penombre,
    )


class OmbreEtPenombreSourceEtendue(NotionScene):
    def construct(self):
        titre = scene_title("Ombre et pénombre (source étendue)")
        titre.scale(0.45)
        titre.to_edge(UP)

        # --- Énoncé -----------------------------------------------------------
        mise_en_situation = Text(
            _wrap(
                "L'ombre d'un pylône est nette au soleil, mais floue sous "
                "un lampadaire. Pourquoi une source plus grande ou plus "
                "proche change-t-elle la nature de l'ombre ?",
                width=56,
            ),
            font_size=22,
        )
        mise_en_situation.next_to(titre, DOWN, buff=0.35)

        with self.voiceover(
            text=(
                "L'ombre d'un pylône électrique est nette en plein soleil, "
                "mais devient floue sous un lampadaire. Pourquoi une "
                "source plus grande, ou plus proche, change-t-elle la "
                "nature de l'ombre ?"
            )
        ) as tracker:
            self.play(Write(titre))
            self.play(FadeIn(mise_en_situation))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(mise_en_situation))

        # --- Raisonnement : définitions -----------------------------------------
        definitions = definition_box(
            VGroup(
                Text("OMBRE (zone d'ombre totale) : aucun point de la source", font_size=19),
                Text("n'est visible depuis cette zone.", font_size=19),
                Text("PÉNOMBRE : seule UNE PARTIE de la source est visible", font_size=19),
                Text("depuis cette zone (éclairement partiel, plus faible).", font_size=19),
            ).arrange(DOWN, aligned_edge=LEFT, buff=0.16),
            box_width=11.8,
        )
        definitions.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Avec une source étendue, on distingue deux zones. Dans la "
                "zone d'ombre, aucun point de la source n'est visible. "
                "Dans la zone de pénombre, seule une partie de la source "
                "est visible : cette zone reçoit donc un peu de lumière, "
                "moins que les zones pleinement éclairées."
            )
        ) as tracker:
            self.play(FadeIn(definitions))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(definitions))

        # --- Construction géométrique -------------------------------------------
        construction = _construction_penombre()
        construction.scale(0.85)
        construction.next_to(titre, DOWN, buff=0.55)

        with self.voiceover(
            text=(
                "Pour construire ces zones, on prend les deux points "
                "extrêmes de la source, A en haut et B en bas. Les rayons "
                "tangents CROISÉS, de A vers le bas de l'objet et de B "
                "vers le haut de l'objet, délimitent la zone d'ombre "
                "totale, au centre. Les rayons tangents NON CROISÉS "
                "délimitent, eux, les deux bandes de pénombre de part et "
                "d'autre."
            )
        ) as tracker:
            self.play(FadeIn(construction))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(construction))

        # --- Exemple traité : pylône à Abidjan -----------------------------------
        exemple = example_box(
            VGroup(
                Text("Un pylône électrique à Abidjan projette une ombre au sol.", font_size=19),
                Text("Au SOLEIL : la source est très lointaine, donc quasi", font_size=19),
                Text("ponctuelle relativement au pylône → ombre NETTE.", font_size=19),
                Text("Sous un LAMPADAIRE proche : la source est étendue et", font_size=19),
                Text("proche → large bande de pénombre → ombre FLOUE.", font_size=19),
            ).arrange(DOWN, aligned_edge=LEFT, buff=0.16),
            box_width=12.0,
        )
        exemple.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Exemple : un pylône électrique à Abidjan. En plein "
                "soleil, la source est extrêmement lointaine, donc quasi "
                "ponctuelle par rapport au pylône : l'ombre au sol est "
                "nette. Mais sous un lampadaire proche, la source est à la "
                "fois étendue et proche : une large bande de pénombre "
                "apparaît, et l'ombre devient floue sur ses bords."
            )
        ) as tracker:
            self.play(FadeIn(exemple))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(exemple))

        # --- À retenir --------------------------------------------------------
        retenir = essentiel_box(
            VGroup(
                Text("À retenir", font_size=24, weight="BOLD"),
                Text("Ombre : aucun point de la source visible.", font_size=20),
                Text("Pénombre : une partie seulement de la source visible.", font_size=20),
                Text("Source lointaine/petite → ombre nette (quasi ponctuelle).", font_size=20),
                Text("Source proche/grande → large pénombre, ombre floue.", font_size=20),
            ).arrange(DOWN, aligned_edge=LEFT, buff=0.2),
            box_width=12.2,
        )
        retenir.next_to(titre, DOWN, buff=0.35)

        with self.voiceover(
            text=(
                "Retenons l'essentiel. Dans l'ombre, aucun point de la "
                "source n'est visible ; dans la pénombre, une partie "
                "seulement l'est. Une source lointaine ou petite se "
                "comporte comme une source ponctuelle et donne une ombre "
                "nette. Une source proche ou grande donne une large "
                "pénombre et une ombre floue."
            )
        ) as tracker:
            self.play(FadeIn(retenir))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(retenir))

        # --- Pièges à éviter --------------------------------------------------
        pieges = warning_box(
            VGroup(
                Text("• Ne pas confondre pénombre (partiellement éclairée)", font_size=20),
                Text("   et ombre totale (complètement sombre).", font_size=20),
                Text("• Plus la source est proche ET grande, plus la bande", font_size=20),
                Text("   de pénombre est large — ce n'est pas systématique.", font_size=20),
            ).arrange(DOWN, aligned_edge=LEFT, buff=0.16),
            box_width=11.8,
        )
        pieges.next_to(titre, DOWN, buff=0.35)

        with self.voiceover(
            text=(
                "Attention à ne pas confondre la pénombre, partiellement "
                "éclairée, et l'ombre totale, complètement sombre. Et "
                "retenez que c'est la combinaison d'une source proche ET "
                "grande qui élargit la pénombre, pas l'un des deux "
                "facteurs seul."
            )
        ) as tracker:
            self.play(FadeIn(pieges))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(pieges), FadeOut(titre))
