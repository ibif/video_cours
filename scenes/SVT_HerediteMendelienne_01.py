"""
scenes/SVT_HerediteMendelienne_01.py — Chapitre 6 (1ereC, SVT), scène 01.

§ I.1 L'hérédité et les caractères héréditaires : définitions, exemples
courants, biographie de Grégoire Mendel (pois de senteur, 1865) et
objectifs pédagogiques du chapitre. Source : 1ereC/SVT.pdf, pages 57-58.
"""

import textwrap

from manim import (
    DOWN,
    LEFT,
    RIGHT,
    UP,
    WHITE,
    YELLOW,
    Circle,
    Create,
    FadeIn,
    FadeOut,
    Line,
    Rectangle,
    Text,
    VGroup,
    Write,
)

from shapes.base_scene import NotionScene
from shapes.boxes import definition_box, example_box, scene_title


def _wrap(text: str, width: int = 56) -> str:
    return "\n".join(textwrap.fill(line, width=width) for line in text.split("\n"))


def _bullets(items, font_size=23, color=WHITE, width=54):
    lines = VGroup(
        *[Text(f"• {_wrap(it, width=width)}", font_size=font_size, color=color) for it in items]
    )
    lines.arrange(DOWN, aligned_edge=LEFT, buff=0.22)
    return lines


class HeriteEtCaracteresHereditaires(NotionScene):
    def construct(self):
        titre = scene_title("6 — La transmission d'un caractère héréditaire")
        titre.scale(0.62)
        titre.to_edge(UP)

        # --- Énoncé : observation de la ressemblance parents-enfants -----------
        intro = Text(
            _wrap(
                "Les enfants ressemblent à leurs parents : couleur de peau, "
                "forme du nez, groupe sanguin se transmettent de génération "
                "en génération. Chez les plantes cultivées (maïs, riz, "
                "niébé), les graines d'une variété donnent toujours des "
                "plants de la même variété.",
                width=56,
            ),
            font_size=25,
            color=WHITE,
        )
        intro.next_to(titre, DOWN, buff=0.55)

        with self.voiceover(
            text=(
                "On observe couramment que les enfants ressemblent à leurs "
                "parents : la couleur de la peau, la forme du nez, le groupe "
                "sanguin se transmettent de génération en génération. De "
                "même, chez les plantes cultivées comme le maïs, le riz ou "
                "le niébé, les graines d'une variété donnent toujours des "
                "plants de la même variété. Ce chapitre étudie les lois qui "
                "gouvernent cette transmission."
            )
        ) as tracker:
            self.play(Write(titre))
            self.play(FadeIn(intro))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(intro))

        # --- Animation du raisonnement : les deux définitions de base ----------
        def_heredite = definition_box(
            Text(
                _wrap(
                    "L'hérédité est l'ensemble des phénomènes par lesquels "
                    "des caractères se transmettent des parents à leurs "
                    "descendants, de génération en génération.",
                    width=50,
                ),
                font_size=24,
            ),
            box_width=11.0,
        )
        def_heredite.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "L'hérédité est l'ensemble des phénomènes par lesquels des "
                "caractères se transmettent des parents à leurs "
                "descendants, de génération en génération. La science qui "
                "étudie l'hérédité et ses mécanismes s'appelle la "
                "génétique."
            )
        ) as tracker:
            self.play(FadeIn(def_heredite))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(def_heredite))

        def_caractere = definition_box(
            Text(
                _wrap(
                    "Un caractère héréditaire est un aspect observable d'un "
                    "individu qui se transmet de génération en génération. "
                    "Exemples : la couleur des graines du pois, le groupe "
                    "sanguin, la couleur du pelage d'un cobaye.",
                    width=50,
                ),
                font_size=23,
            ),
            box_width=11.0,
        )
        def_caractere.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Un caractère héréditaire est un aspect observable d'un "
                "individu qui se transmet de génération en génération : par "
                "exemple, la couleur des graines du pois, le groupe "
                "sanguin, ou la couleur du pelage d'un cobaye. C'est "
                "exactement ce type de caractère que nous allons apprendre "
                "à analyser tout au long de ce chapitre."
            )
        ) as tracker:
            self.play(FadeIn(def_caractere))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(def_caractere))

        # --- Exemple traité : la biographie de Grégoire Mendel -----------------
        entete_ex = Text("Le père de la génétique : Grégoire Mendel", font_size=25, color=YELLOW, weight="BOLD")
        entete_ex.next_to(titre, DOWN, buff=0.5)

        # Petit schéma symbolique : un monastère (rectangle + triangle-toit
        # remplacé par un simple carré) et une fleur de pois de senteur
        # (cercle + tige) dans son jardin.
        mur = Rectangle(width=1.6, height=1.1, color=WHITE, fill_color=WHITE, fill_opacity=0.15)
        toit = Line(mur.get_corner(UP + LEFT), mur.get_corner(UP + RIGHT) + UP * 0.7, color=WHITE)
        toit2 = Line(mur.get_corner(UP + LEFT), mur.get_top() + UP * 0.7, color=WHITE)
        toit3 = Line(mur.get_corner(UP + RIGHT), mur.get_top() + UP * 0.7, color=WHITE)
        monastere = VGroup(mur, toit2, toit3).shift(LEFT * 3)

        tige = Line(DOWN * 0.6, UP * 0.3, color=WHITE)
        petales = VGroup(*[Circle(radius=0.22, color=YELLOW, fill_color=YELLOW, fill_opacity=0.7) for _ in range(4)])
        petales.arrange(RIGHT, buff=-0.1)
        fleur = VGroup(tige, petales).arrange(UP, buff=0.05).shift(RIGHT * 3)

        schema = VGroup(monastere, fleur)
        schema.next_to(entete_ex, DOWN, buff=0.5)

        bio = _bullets(
            [
                "Grégoire Mendel (1822-1884), moine autrichien.",
                "Croise des pois de senteur dans le jardin de son "
                "monastère.",
                "Publie ses résultats en 1865 : les lois qui portent "
                "son nom.",
            ],
            font_size=22,
            width=50,
        )
        bio.next_to(schema, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "La génétique est née des travaux du moine autrichien "
                "Grégoire Mendel, qui vécut de mille huit cent vingt-deux à "
                "mille huit cent quatre-vingt-quatre. Dans le jardin de son "
                "monastère, il croisa méthodiquement des milliers de pois "
                "de senteur et compta soigneusement leurs descendants. Il "
                "publia ses résultats en mille huit cent soixante-cinq : "
                "ce sont les lois qui portent aujourd'hui son nom, et que "
                "nous allons étudier dans ce chapitre."
            )
        ) as tracker:
            self.play(FadeIn(entete_ex))
            self.play(Create(schema))
            self.play(FadeIn(bio))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(entete_ex), FadeOut(schema), FadeOut(bio))

        # --- À retenir : les objectifs du chapitre ------------------------------
        entete_obj = Text("Objectifs de ce chapitre", font_size=25, color=YELLOW, weight="BOLD")
        entete_obj.next_to(titre, DOWN, buff=0.5)

        objectifs = _bullets(
            [
                "Définir gène, allèle, locus, génotype, phénotype, "
                "homozygote, hétérozygote ; distinguer dominance et "
                "récessivité.",
                "Interpréter les croisements de Mendel sur le pois avec "
                "des échiquiers de croisement.",
                "Calculer les proportions théoriques des descendances "
                "(3/4-1/4 en F2 ; 1/2-1/2 en test-cross).",
                "Distinguer transmission autosomique et transmission "
                "liée au sexe (drépanocytose, groupes sanguins, "
                "daltonisme, hémophilie).",
                "Construire et lire un arbre généalogique simple.",
                "Expliquer le conseil génétique et la sélection "
                "agricole.",
            ],
            font_size=20,
            width=56,
        )
        objectifs.next_to(entete_obj, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Voici les objectifs de ce chapitre. À la fin, vous saurez "
                "définir les notions de gène, d'allèle, de locus, de "
                "génotype, de phénotype, d'homozygote et d'hétérozygote, et "
                "distinguer dominance et récessivité. Vous saurez "
                "interpréter les croisements de Mendel sur le pois grâce à "
                "des échiquiers de croisement, et calculer les proportions "
                "théoriques des descendances. Vous saurez distinguer une "
                "transmission autosomique d'une transmission liée au sexe, "
                "à travers des exemples comme la drépanocytose, les "
                "groupes sanguins, le daltonisme ou l'hémophilie. Enfin, "
                "vous saurez construire et lire un arbre généalogique "
                "simple, et expliquer les applications pratiques de la "
                "génétique : le conseil génétique et la sélection "
                "agricole."
            )
        ) as tracker:
            self.play(FadeIn(entete_obj))
            self.play(FadeIn(objectifs))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(titre), FadeOut(entete_obj), FadeOut(objectifs))
