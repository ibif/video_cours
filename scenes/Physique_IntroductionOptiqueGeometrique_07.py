"""
scenes/Physique_IntroductionOptiqueGeometrique_07.py — Chapitre 11
« Introduction à l'optique géométrique » (1ereC, Physique), scène 07.

§ 4 (partie 3). Éclipses : alignement de trois astres. Éclipse de Soleil
(Lune entre Soleil et Terre, nouvelle Lune) et éclipse de Lune (Terre
entre Soleil et Lune, pleine Lune). Exemple résolu 2 : poteau à Abidjan,
ombre 3 m, élève 1,6 m d'ombre 0,8 m → hauteur du poteau = 6 m (triangles
semblables, rayons du Soleil considérés parallèles).
Source : 1ereC/Physique.pdf, pages 108-116 (chapitre 11, § 4).
"""

import textwrap

from manim import (
    DOWN,
    LEFT,
    RIGHT,
    UP,
    BLUE,
    BLUE_E,
    GRAY,
    ORANGE,
    WHITE,
    YELLOW,
    Circle,
    FadeIn,
    FadeOut,
    Line,
    MathTex,
    Text,
    VGroup,
    Write,
)

from shapes.base_scene import NotionScene
from shapes.boxes import definition_box, essentiel_box, example_box, scene_title, warning_box


def _wrap(text: str, width: int = 56) -> str:
    return "\n".join(textwrap.fill(line, width=width) for line in text.split("\n"))


def _eclipse_soleil() -> VGroup:
    """Soleil — Lune — Terre alignés : la Lune projette son cône d'ombre
    et de pénombre sur la Terre (éclipse de Soleil, à la nouvelle Lune)."""
    soleil = Circle(radius=0.5, color=YELLOW, fill_color=YELLOW, fill_opacity=1.0).move_to(LEFT * 4.6)
    label_soleil = Text("Soleil", font_size=15, color=YELLOW).next_to(soleil, DOWN, buff=0.15)

    lune = Circle(radius=0.12, color=GRAY, fill_color=GRAY, fill_opacity=1.0).move_to(LEFT * 0.6)
    label_lune = Text("Lune", font_size=14, color=WHITE).next_to(lune, UP, buff=0.15)

    terre = Circle(radius=0.35, color=BLUE, fill_color=BLUE_E, fill_opacity=1.0).move_to(RIGHT * 2.6)
    label_terre = Text("Terre", font_size=15, color=BLUE).next_to(terre, DOWN, buff=0.15)

    # Cône d'ombre (rayons tangents croisés) et de pénombre (non croisés)
    tangente_ombre_haut = Line(
        soleil.get_top(), lune.get_bottom() + DOWN * 0.02, color=ORANGE, stroke_width=1.5,
    )
    tangente_ombre_haut_prolongee = Line(
        lune.get_bottom(), terre.get_center() + DOWN * 0.15, color=ORANGE, stroke_width=1.5,
    )
    tangente_ombre_bas = Line(
        soleil.get_bottom(), lune.get_top() + UP * 0.02, color=ORANGE, stroke_width=1.5,
    )
    tangente_ombre_bas_prolongee = Line(
        lune.get_top(), terre.get_center() + UP * 0.15, color=ORANGE, stroke_width=1.5,
    )

    return VGroup(
        soleil, label_soleil, lune, label_lune, terre, label_terre,
        tangente_ombre_haut, tangente_ombre_haut_prolongee,
        tangente_ombre_bas, tangente_ombre_bas_prolongee,
    )


def _eclipse_lune() -> VGroup:
    """Soleil — Terre — Lune alignés : la Terre projette son cône d'ombre
    sur la Lune (éclipse de Lune, à la pleine Lune)."""
    soleil = Circle(radius=0.5, color=YELLOW, fill_color=YELLOW, fill_opacity=1.0).move_to(LEFT * 4.6)
    label_soleil = Text("Soleil", font_size=15, color=YELLOW).next_to(soleil, DOWN, buff=0.15)

    terre = Circle(radius=0.3, color=BLUE, fill_color=BLUE_E, fill_opacity=1.0).move_to(LEFT * 0.6)
    label_terre = Text("Terre", font_size=14, color=BLUE).next_to(terre, UP, buff=0.15)

    lune = Circle(radius=0.15, color=GRAY, fill_color=GRAY, fill_opacity=1.0).move_to(RIGHT * 2.6)
    label_lune = Text("Lune", font_size=15, color=WHITE).next_to(lune, DOWN, buff=0.15)

    tangente_haut = Line(soleil.get_top(), terre.get_top() + UP * 0.02, color=ORANGE, stroke_width=1.5)
    tangente_haut_prolongee = Line(
        terre.get_top(), terre.get_top() + (terre.get_top() - soleil.get_top()) * 3.2, color=ORANGE, stroke_width=1.5,
    )
    tangente_bas = Line(soleil.get_bottom(), terre.get_bottom() + DOWN * 0.02, color=ORANGE, stroke_width=1.5)
    tangente_bas_prolongee = Line(
        terre.get_bottom(), terre.get_bottom() + (terre.get_bottom() - soleil.get_bottom()) * 3.2, color=ORANGE, stroke_width=1.5,
    )

    return VGroup(
        soleil, label_soleil, terre, label_terre, lune, label_lune,
        tangente_haut, tangente_haut_prolongee, tangente_bas, tangente_bas_prolongee,
    )


class EclipsesDeSoleilEtDeLune(NotionScene):
    def construct(self):
        titre = scene_title("Éclipses de Soleil et de Lune")
        titre.scale(0.5)
        titre.to_edge(UP)

        # --- Énoncé -----------------------------------------------------------
        mise_en_situation = Text(
            _wrap(
                "Une éclipse : trois astres alignés. Mais comment "
                "distinguer une éclipse de Soleil d'une éclipse de Lune ?",
                width=56,
            ),
            font_size=23,
        )
        mise_en_situation.next_to(titre, DOWN, buff=0.35)

        with self.voiceover(
            text=(
                "Une éclipse se produit lorsque trois astres se "
                "retrouvent alignés. Mais comment distinguer une éclipse "
                "de Soleil d'une éclipse de Lune ?"
            )
        ) as tracker:
            self.play(Write(titre))
            self.play(FadeIn(mise_en_situation))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(mise_en_situation))

        # --- Raisonnement : éclipse de Soleil -----------------------------------
        schema_soleil = _eclipse_soleil()
        schema_soleil.scale(0.85)
        schema_soleil.next_to(titre, DOWN, buff=0.5)

        definition_eclipse_soleil = definition_box(
            VGroup(
                Text("ÉCLIPSE DE SOLEIL : la Lune se place entre le Soleil et", font_size=18),
                Text("la Terre. Elle projette sur la Terre une zone d'ombre", font_size=18),
                Text("totale, une zone de pénombre partielle, et parfois une", font_size=18),
                Text("zone annulaire. Se produit à la NOUVELLE LUNE.", font_size=18),
            ).arrange(DOWN, aligned_edge=LEFT, buff=0.14),
            box_width=11.6,
        )
        definition_eclipse_soleil.next_to(schema_soleil, DOWN, buff=0.3)

        with self.voiceover(
            text=(
                "Lors d'une éclipse de Soleil, la Lune se place entre le "
                "Soleil et la Terre. Elle projette sur la Terre une zone "
                "d'ombre totale, où l'éclipse est totale, une zone de "
                "pénombre où l'éclipse n'est que partielle, et parfois une "
                "zone dite annulaire. Ce phénomène ne peut se produire qu'à "
                "la nouvelle Lune."
            )
        ) as tracker:
            self.play(FadeIn(schema_soleil))
            self.play(FadeIn(definition_eclipse_soleil))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(schema_soleil), FadeOut(definition_eclipse_soleil))

        # --- Raisonnement : éclipse de Lune -------------------------------------
        schema_lune = _eclipse_lune()
        schema_lune.scale(0.85)
        schema_lune.next_to(titre, DOWN, buff=0.5)

        definition_eclipse_lune = definition_box(
            VGroup(
                Text("ÉCLIPSE DE LUNE : la Terre se place entre le Soleil et", font_size=18),
                Text("la Lune. Le cône d'ombre de la Terre recouvre la Lune,", font_size=18),
                Text("qui s'assombrit. Se produit à la PLEINE LUNE.", font_size=18),
            ).arrange(DOWN, aligned_edge=LEFT, buff=0.14),
            box_width=11.2,
        )
        definition_eclipse_lune.next_to(schema_lune, DOWN, buff=0.3)

        with self.voiceover(
            text=(
                "Lors d'une éclipse de Lune, c'est la Terre qui se place "
                "entre le Soleil et la Lune. Le cône d'ombre de la Terre "
                "recouvre alors la Lune, qui s'assombrit. Ce phénomène ne "
                "peut se produire qu'à la pleine Lune."
            )
        ) as tracker:
            self.play(FadeIn(schema_lune))
            self.play(FadeIn(definition_eclipse_lune))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(schema_lune), FadeOut(definition_eclipse_lune))

        # --- Exemple résolu 2 : poteau à Abidjan ---------------------------------
        enonce_poteau = example_box(
            VGroup(
                Text("Un poteau électrique à Abidjan projette une ombre de 3 m.", font_size=18),
                Text("Au même instant, un élève de 1,6 m projette une ombre", font_size=18),
                Text("de 0,8 m. Les rayons du Soleil, très lointain, sont", font_size=18),
                Text("considérés PARALLÈLES. Quelle est la hauteur du poteau ?", font_size=18),
            ).arrange(DOWN, aligned_edge=LEFT, buff=0.14),
            box_width=11.8,
        )
        enonce_poteau.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Exemple résolu : un poteau électrique à Abidjan projette "
                "une ombre de 3 mètres. Au même instant, un élève de 1,6 "
                "mètre projette une ombre de 0,8 mètre. Comme le Soleil "
                "est extrêmement lointain, ses rayons sont considérés "
                "parallèles. Quelle est la hauteur du poteau ?"
            )
        ) as tracker:
            self.play(FadeIn(enonce_poteau))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(enonce_poteau))

        resolution = example_box(
            VGroup(
                Text("Rayons parallèles → les deux triangles (poteau/ombre et", font_size=18),
                Text("élève/ombre) sont semblables : le rapport hauteur/ombre", font_size=18),
                Text("est constant.", font_size=18),
                MathTex(
                    r"\dfrac{h_{\text{poteau}}}{ombre_{\text{poteau}}} = \dfrac{h_{\text{élève}}}{ombre_{\text{élève}}}"
                    r"\ \Rightarrow\ h_{\text{poteau}} = \dfrac{1{,}6 \times 3}{0{,}8} = 6\ \text{m}",
                    font_size=24,
                ),
            ).arrange(DOWN, aligned_edge=LEFT, buff=0.2),
            box_width=11.8,
        )
        resolution.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Puisque les rayons du Soleil sont parallèles, le triangle "
                "formé par le poteau et son ombre est semblable à celui "
                "formé par l'élève et son ombre : le rapport entre la "
                "hauteur et la longueur de l'ombre est le même pour les "
                "deux. On calcule donc : hauteur du poteau égale un virgule "
                "six, multiplié par trois, le tout divisé par zéro virgule "
                "huit, ce qui donne six mètres."
            )
        ) as tracker:
            self.play(FadeIn(resolution))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(resolution))

        # --- À retenir --------------------------------------------------------
        retenir = essentiel_box(
            VGroup(
                Text("À retenir", font_size=24, weight="BOLD"),
                Text("Éclipse de Soleil : Lune entre Soleil et Terre (nouvelle Lune).", font_size=18),
                Text("Éclipse de Lune : Terre entre Soleil et Lune (pleine Lune).", font_size=18),
                Text("Rayons du Soleil quasi parallèles → méthode de Thalès.", font_size=18),
            ).arrange(DOWN, aligned_edge=LEFT, buff=0.2),
            box_width=12.0,
        )
        retenir.next_to(titre, DOWN, buff=0.35)

        with self.voiceover(
            text=(
                "Retenons l'essentiel. Une éclipse de Soleil se produit "
                "quand la Lune est entre le Soleil et la Terre, à la "
                "nouvelle Lune. Une éclipse de Lune se produit quand la "
                "Terre est entre le Soleil et la Lune, à la pleine Lune. "
                "Et comme les rayons du Soleil sont quasi parallèles, on "
                "peut utiliser le théorème de Thalès pour résoudre des "
                "problèmes d'ombre."
            )
        ) as tracker:
            self.play(FadeIn(retenir))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(retenir))

        # --- Pièges à éviter --------------------------------------------------
        pieges = warning_box(
            VGroup(
                Text("• Ne pas inverser les deux configurations : Soleil-Lune-", font_size=19),
                Text("   Terre pour l'éclipse de SOLEIL, Soleil-Terre-Lune pour", font_size=19),
                Text("   l'éclipse de LUNE.", font_size=19),
                Text("• Une éclipse ne se produit PAS à chaque nouvelle ou", font_size=19),
                Text("   pleine Lune : l'orbite de la Lune est inclinée, un", font_size=19),
                Text("   alignement parfait reste rare.", font_size=19),
            ).arrange(DOWN, aligned_edge=LEFT, buff=0.14),
            box_width=12.2,
        )
        pieges.next_to(titre, DOWN, buff=0.3)

        with self.voiceover(
            text=(
                "Attention à ne pas inverser les deux configurations : "
                "Soleil, Lune, Terre pour l'éclipse de Soleil ; Soleil, "
                "Terre, Lune pour l'éclipse de Lune. Et n'oubliez pas "
                "qu'une éclipse ne se produit pas à chaque nouvelle ou "
                "pleine Lune : l'orbite de la Lune étant inclinée, un "
                "alignement parfait reste un événement rare."
            )
        ) as tracker:
            self.play(FadeIn(pieges))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(pieges), FadeOut(titre))
