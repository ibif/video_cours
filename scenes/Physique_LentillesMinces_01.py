"""
scenes/Physique_LentillesMinces_01.py — Chapitre 13 « Les lentilles minces »
(1ereC, Physique), scène 01 — DERNIER chapitre du programme de Physique.

§ Généralités : définition d'une lentille, définition d'une lentille mince,
les deux types (convergente / divergente) avec leurs caractéristiques
(bords minces/centre épais vs bords épais/centre mince, signe de f' et de
C), reconnaissance pratique, symboles normalisés (flèches).
Source : 1ereC/Physique.pdf, pages 130-140 (chapitre 13, § 1).
"""

import textwrap

from manim import (
    DOWN,
    LEFT,
    RIGHT,
    UP,
    WHITE,
    YELLOW,
    ArcBetweenPoints,
    Arrow,
    Create,
    Ellipse,
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


def _lens_symbol(convergente: bool = True, height: float = 2.2, color=WHITE) -> VGroup:
    """
    Symbole normalisé d'une lentille mince (voir CLAUDE.md) : un axe
    vertical terminé par des flèches. Convergente : flèches pointant vers
    l'EXTÉRIEUR (haut et bas). Divergente : flèches pointant vers
    l'INTÉRIEUR (repliées vers le centre).
    """
    half = height / 2
    if convergente:
        haut = Arrow(RIGHT * 0, UP * half, buff=0, stroke_width=4, color=color)
        bas = Arrow(RIGHT * 0, DOWN * half, buff=0, stroke_width=4, color=color)
        return VGroup(haut, bas)
    inner = half * 0.5
    axe = Line(UP * inner, DOWN * inner, color=color, stroke_width=4)
    haut = Arrow(UP * half, UP * inner, buff=0, stroke_width=4, color=color)
    bas = Arrow(DOWN * half, DOWN * inner, buff=0, stroke_width=4, color=color)
    return VGroup(axe, haut, bas)


def _coupe_convergente(color=WHITE) -> Ellipse:
    """Coupe schématique : bords minces, centre épais (silhouette biconvexe)."""
    return Ellipse(width=0.6, height=1.7, color=color, fill_color=color, fill_opacity=0.15, stroke_width=3)


def _coupe_divergente(color=WHITE) -> VGroup:
    """Coupe schématique : bords épais, centre mince (silhouette biconcave)."""
    edge = 0.32
    top_r, bot_r = UP * 0.85 + RIGHT * edge, DOWN * 0.85 + RIGHT * edge
    top_l, bot_l = UP * 0.85 + LEFT * edge, DOWN * 0.85 + LEFT * edge
    droite = ArcBetweenPoints(bot_r, top_r, angle=-1.3)
    gauche = ArcBetweenPoints(top_l, bot_l, angle=-1.3)
    cap_haut = Line(top_l, top_r)
    cap_bas = Line(bot_l, bot_r)
    shape = VGroup(gauche, cap_bas, droite, cap_haut)
    shape.set_stroke(color=color, width=3)
    return shape


class GeneralitesLentilles(NotionScene):
    def construct(self):
        titre = scene_title("Les lentilles minces : généralités")
        titre.scale(0.44)
        titre.to_edge(UP)

        # --- Énoncé : définitions ------------------------------------------------
        definitions = definition_box(
            VGroup(
                Text("Lentille", font_size=24, weight="BOLD"),
                Text(
                    "Milieu transparent limité par deux surfaces, dont l'une",
                    font_size=21,
                ),
                Text("au moins est sphérique.", font_size=21),
                Text("Lentille mince", font_size=24, weight="BOLD"),
                Text(
                    "Épaisseur négligeable devant les rayons de courbure des",
                    font_size=21,
                ),
                Text(
                    "faces : son centre optique, noté O, appartient à l'axe",
                    font_size=21,
                ),
                Text("optique principal de la lentille.", font_size=21),
            ).arrange(DOWN, buff=0.18, aligned_edge=LEFT),
            box_width=11.6,
        )
        definitions.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Une lentille est un milieu transparent limité par deux "
                "surfaces, dont l'une au moins est sphérique. Dans ce "
                "chapitre, on s'intéresse aux lentilles minces : leur "
                "épaisseur est négligeable devant les rayons de courbure de "
                "leurs faces. Une lentille mince possède un centre optique, "
                "noté O, situé sur son axe optique principal."
            )
        ) as tracker:
            self.play(Write(titre))
            self.play(FadeIn(definitions))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(definitions))

        # --- Raisonnement : les deux types ---------------------------------------
        coupe_conv = _coupe_convergente()
        symb_conv = _lens_symbol(True).scale(0.75).next_to(coupe_conv, DOWN, buff=0.35)
        label_conv = Text("CONVERGENTE", font_size=20, color=YELLOW, weight="BOLD").next_to(symb_conv, DOWN, buff=0.25)
        carac_conv = VGroup(
            Text("bords minces, centre épais", font_size=17),
            Text("f' > 0   et   C > 0", font_size=18, color=YELLOW),
        ).arrange(DOWN, buff=0.12).next_to(label_conv, DOWN, buff=0.2)
        bloc_conv = VGroup(coupe_conv, symb_conv, label_conv, carac_conv)

        coupe_div = _coupe_divergente()
        symb_div = _lens_symbol(False).scale(0.75).next_to(coupe_div, DOWN, buff=0.35)
        label_div = Text("DIVERGENTE", font_size=20, color=YELLOW, weight="BOLD").next_to(symb_div, DOWN, buff=0.25)
        carac_div = VGroup(
            Text("bords épais, centre mince", font_size=17),
            Text("f' < 0   et   C < 0", font_size=18, color=YELLOW),
        ).arrange(DOWN, buff=0.12).next_to(label_div, DOWN, buff=0.2)
        bloc_div = VGroup(coupe_div, symb_div, label_div, carac_div)

        deux_types = VGroup(bloc_conv, bloc_div).arrange(RIGHT, buff=1.8)
        deux_types.next_to(titre, DOWN, buff=0.6)

        with self.voiceover(
            text=(
                "On distingue deux types de lentilles minces. La lentille "
                "convergente a des bords minces et un centre épais : sa "
                "distance focale f prime est positive, et sa vergence C est "
                "positive. La lentille divergente, au contraire, a des "
                "bords épais et un centre mince : sa distance focale f "
                "prime est négative, et sa vergence C est négative. "
                "Chaque type possède son propre symbole normalisé : des "
                "flèches vers l'extérieur pour la convergente, vers "
                "l'intérieur pour la divergente."
            )
        ) as tracker:
            self.play(Create(coupe_conv), Create(coupe_div))
            self.play(Create(symb_conv), Create(symb_div))
            self.play(Write(label_conv), Write(label_div))
            self.play(FadeIn(carac_conv), FadeIn(carac_div))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(deux_types))

        # --- Exemple : reconnaissance pratique ------------------------------------
        exemple = example_box(
            VGroup(
                Text("Reconnaître une lentille sans instrument", font_size=22, weight="BOLD"),
                Text(
                    "En regardant un texte à travers elle : si les lettres",
                    font_size=20,
                ),
                Text(
                    "paraissent agrandies et nettes, c'est une lentille",
                    font_size=20,
                ),
                Text("CONVERGENTE.", font_size=20, color=YELLOW),
                Text(
                    "Si l'image reste petite et droite quelle que soit la",
                    font_size=20,
                ),
                Text("distance, c'est une lentille DIVERGENTE.", font_size=20, color=YELLOW),
            ).arrange(DOWN, buff=0.18, aligned_edge=LEFT),
            box_width=11.6,
        )
        exemple.next_to(titre, DOWN, buff=0.45)

        with self.voiceover(
            text=(
                "Comment reconnaître une lentille sans instrument de "
                "mesure ? En regardant un texte à travers elle : si les "
                "lettres paraissent agrandies et nettes, c'est une "
                "lentille convergente. Si l'image du texte reste petite et "
                "droite, quelle que soit la distance à laquelle on tient "
                "la lentille, c'est une lentille divergente."
            )
        ) as tracker:
            self.play(FadeIn(exemple))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(exemple))

        # --- À retenir --------------------------------------------------------------
        retenir = essentiel_box(
            VGroup(
                Text("À retenir", font_size=24, weight="BOLD"),
                Text("Lentille mince : épaisseur négligeable, centre optique O.", font_size=19),
                Text("Convergente : bords minces, centre épais, f' > 0, C > 0.", font_size=19),
                Text("Divergente : bords épais, centre mince, f' < 0, C < 0.", font_size=19),
            ).arrange(DOWN, buff=0.2, aligned_edge=LEFT),
            box_width=12.0,
        )
        retenir.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Retenons l'essentiel : une lentille mince a une épaisseur "
                "négligeable et un centre optique O. La lentille "
                "convergente a des bords minces, un centre épais, une "
                "distance focale et une vergence positives. La lentille "
                "divergente a des bords épais, un centre mince, une "
                "distance focale et une vergence négatives."
            )
        ) as tracker:
            self.play(FadeIn(retenir))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(retenir))

        # --- Piège à éviter -----------------------------------------------------------
        piege = warning_box(
            VGroup(
                Text("• La courbure exacte des faces (biconvexe, plan-", font_size=19),
                Text("   convexe, ménisque…) ne détermine PAS à elle", font_size=19),
                Text("   seule le type : seul le critère bords/centre", font_size=19),
                Text("   compte (minces/épais → convergente, l'inverse", font_size=19),
                Text("   → divergente).", font_size=19),
                Text("• Le symbole en flèches ne représente pas la forme", font_size=19),
                Text("   réelle : il indique seulement le comportement", font_size=19),
                Text("   optique (convergent ou divergent).", font_size=19),
            ).arrange(DOWN, aligned_edge=LEFT, buff=0.12),
            box_width=12.0,
        )
        piege.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Attention à un piège classique : la courbure exacte des "
                "faces ne détermine pas à elle seule le type de la "
                "lentille. Seul le critère bords minces, centre épais, "
                "pour la convergente, ou bords épais, centre mince, pour "
                "la divergente, compte vraiment. Et le symbole en flèches "
                "ne représente pas la forme réelle de la lentille : il "
                "indique seulement son comportement optique."
            )
        ) as tracker:
            self.play(FadeIn(piege))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(piege), FadeOut(titre))
