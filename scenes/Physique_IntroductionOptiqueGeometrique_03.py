"""
scenes/Physique_IntroductionOptiqueGeometrique_03.py — Chapitre 11
« Introduction à l'optique géométrique » (1ereC, Physique), scène 03.

§ 2. Milieux de propagation : transparent (air, eau claire, verre),
translucide (papier huilé, verre dépoli) et opaque (bois, carton, métal).
Un même corps peut changer de catégorie selon son épaisseur.
Source : 1ereC/Physique.pdf, pages 108-116 (chapitre 11, § 2).
"""

import textwrap

from manim import (
    DOWN,
    LEFT,
    ORIGIN,
    RIGHT,
    UP,
    GRAY,
    WHITE,
    YELLOW,
    Arrow,
    Dot,
    FadeIn,
    FadeOut,
    Rectangle,
    Text,
    VGroup,
    Write,
)

from shapes.base_scene import NotionScene
from shapes.boxes import definition_box, essentiel_box, example_box, scene_title, warning_box


def _wrap(text: str, width: int = 56) -> str:
    return "\n".join(textwrap.fill(line, width=width) for line in text.split("\n"))


def _bloc_milieu(largeur_rayons_sortants: int, opacity: float, label: str, color) -> VGroup:
    """Une source ponctuelle à gauche envoie un rayon vers un bloc
    rectangulaire ; le nombre de rayons qui en ressortent (0, quelques-uns
    diffus, ou plusieurs nets) traduit transparent / translucide / opaque.
    """
    source = Dot(LEFT * 2.6, color=YELLOW, radius=0.1)
    bloc = Rectangle(width=1.0, height=1.4, color=color, fill_color=color, fill_opacity=opacity)
    bloc.move_to(ORIGIN)
    rayon_entrant = Arrow(
        source.get_center(), bloc.get_left(), buff=0.0, stroke_width=2,
        color=YELLOW, max_tip_length_to_length_ratio=0.1,
    )
    sorties = VGroup()
    for i in range(largeur_rayons_sortants):
        depart = bloc.get_right() + UP * (0.3 - 0.3 * i)
        fleche = Arrow(
            depart, depart + RIGHT * 1.1, buff=0.0, stroke_width=2,
            color=YELLOW, max_tip_length_to_length_ratio=0.15,
        )
        sorties.add(fleche)
    label_txt = Text(label, font_size=17, color=WHITE)
    label_txt.next_to(bloc, DOWN, buff=0.5)
    return VGroup(source, rayon_entrant, bloc, sorties, label_txt)


class MilieuxDePropagation(NotionScene):
    def construct(self):
        titre = scene_title("Milieux de propagation")
        titre.scale(0.5)
        titre.to_edge(UP)

        # --- Énoncé ---------------------------------------------------------
        mise_en_situation = Text(
            _wrap(
                "L'air, l'eau, le bois, une vitre dépolie : la lumière "
                "les traverse-t-elle tous de la même façon ?",
                width=56,
            ),
            font_size=23,
        )
        mise_en_situation.next_to(titre, DOWN, buff=0.35)

        with self.voiceover(
            text=(
                "L'air, l'eau, le bois, une vitre dépolie : la lumière "
                "traverse-t-elle tous ces milieux de la même façon ? "
                "Non, et c'est ce que nous allons classer maintenant."
            )
        ) as tracker:
            self.play(Write(titre))
            self.play(FadeIn(mise_en_situation))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(mise_en_situation))

        # --- Raisonnement : les trois catégories ------------------------------
        definition_transparent = definition_box(
            VGroup(
                Text("MILIEU TRANSPARENT : laisse voir nettement les objets", font_size=19),
                Text("à travers lui.", font_size=19),
                Text("Exemples : air, eau claire, verre.", font_size=18),
            ).arrange(DOWN, aligned_edge=LEFT, buff=0.16),
            box_width=10.6,
        )
        definition_transparent.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Un milieu transparent laisse voir nettement les objets à "
                "travers lui. C'est le cas de l'air, de l'eau claire ou "
                "du verre."
            )
        ) as tracker:
            self.play(FadeIn(definition_transparent))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(definition_transparent))

        definition_translucide = definition_box(
            VGroup(
                Text("MILIEU TRANSLUCIDE : laisse passer la lumière, mais ne", font_size=19),
                Text("permet pas de voir nettement les objets à travers.", font_size=19),
                Text("Exemples : papier huilé, verre dépoli.", font_size=18),
            ).arrange(DOWN, aligned_edge=LEFT, buff=0.16),
            box_width=10.8,
        )
        definition_translucide.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Un milieu translucide laisse passer la lumière, mais ne "
                "permet pas de distinguer nettement les objets à travers "
                "lui : c'est le cas du papier huilé ou d'un verre dépoli."
            )
        ) as tracker:
            self.play(FadeIn(definition_translucide))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(definition_translucide))

        definition_opaque = definition_box(
            VGroup(
                Text("MILIEU OPAQUE : ne laisse pas passer la lumière.", font_size=19),
                Text("Exemples : bois, carton, métal.", font_size=18),
            ).arrange(DOWN, aligned_edge=LEFT, buff=0.16),
            box_width=9.6,
        )
        definition_opaque.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Enfin, un milieu opaque ne laisse pas passer la lumière "
                "du tout : c'est le cas du bois, du carton ou d'un métal."
            )
        ) as tracker:
            self.play(FadeIn(definition_opaque))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(definition_opaque))

        # --- Exemple traité : les trois blocs côte à côte ----------------------
        bloc_t = _bloc_milieu(3, 0.15, "Verre : transparent", WHITE)
        bloc_tl = _bloc_milieu(1, 0.55, "Verre dépoli : translucide", GRAY)
        bloc_o = _bloc_milieu(0, 1.0, "Métal : opaque", GRAY)

        groupe = VGroup(bloc_t, bloc_tl, bloc_o).arrange(RIGHT, buff=0.9)
        groupe.scale(0.62)
        groupe.next_to(titre, DOWN, buff=0.7)

        exemple = example_box(
            Text(
                "Le nombre de rayons qui ressortent nets diminue :\n"
                "transparent > translucide > opaque.",
                font_size=18,
            ),
            box_width=10.2,
        )
        exemple.next_to(groupe, DOWN, buff=0.35)

        with self.voiceover(
            text=(
                "Comparons trois blocs éclairés par la même source "
                "ponctuelle. Le verre transparent laisse ressortir "
                "plusieurs rayons nets. Le verre dépoli, translucide, ne "
                "laisse ressortir qu'un rayon affaibli et diffus. Le "
                "métal, opaque, ne laisse ressortir aucun rayon : toute la "
                "lumière est arrêtée."
            )
        ) as tracker:
            self.play(FadeIn(groupe))
            self.play(FadeIn(exemple))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(groupe), FadeOut(exemple))

        # --- À retenir --------------------------------------------------------
        retenir = essentiel_box(
            VGroup(
                Text("À retenir", font_size=24, weight="BOLD"),
                Text("Transparent : on voit nettement à travers.", font_size=20),
                Text("Translucide : la lumière passe mais l'image est floue.", font_size=20),
                Text("Opaque : la lumière ne passe pas du tout.", font_size=20),
            ).arrange(DOWN, aligned_edge=LEFT, buff=0.2),
            box_width=11.6,
        )
        retenir.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Retenons l'essentiel : un milieu transparent laisse voir "
                "nettement à travers lui, un milieu translucide laisse "
                "passer la lumière mais donne une image floue, et un "
                "milieu opaque ne laisse pas passer la lumière du tout."
            )
        ) as tracker:
            self.play(FadeIn(retenir))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(retenir))

        # --- Pièges à éviter --------------------------------------------------
        pieges = warning_box(
            VGroup(
                Text("• Un même corps peut changer de catégorie selon son", font_size=20),
                Text("   épaisseur : une fine feuille de papier est", font_size=20),
                Text("   translucide, un paquet épais de feuilles devient", font_size=20),
                Text("   opaque.", font_size=20),
                Text("• L'eau claire en fine couche est transparente ; très", font_size=20),
                Text("   trouble ou très épaisse, elle peut devenir translucide.", font_size=20),
            ).arrange(DOWN, aligned_edge=LEFT, buff=0.14),
            box_width=12.0,
        )
        pieges.next_to(titre, DOWN, buff=0.3)

        with self.voiceover(
            text=(
                "Attention : un même corps peut changer de catégorie selon "
                "son épaisseur. Une fine feuille de papier est translucide, "
                "mais un paquet épais de feuilles devient opaque. De même, "
                "l'eau claire en fine couche est transparente, mais très "
                "trouble ou très épaisse, elle peut devenir translucide."
            )
        ) as tracker:
            self.play(FadeIn(pieges))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(pieges), FadeOut(titre))
