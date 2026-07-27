"""
scenes/Physique_Condensateur_04.py — Chapitre 9 « Le condensateur »
(1ereC, Physique), scène 04.

§ 3b. Définition de la capacité et le farad. Définition C=q/u (farad F).
Sous-multiples usuels (mF, µF, nF, pF).
Exemple résolu 2 : q=24 µC, u=6 V → C=4 µF.
Source : 1ereC/Physique.pdf, pages 88-98 (chapitre 9, § 3b).
"""

import textwrap

from manim import DOWN, LEFT, RIGHT, UP, YELLOW, FadeIn, FadeOut, MathTex, Text, VGroup, Write

from shapes.base_scene import NotionScene
from shapes.boxes import definition_box, essentiel_box, example_box, scene_title, warning_box


def _wrap(text: str, width: int = 56) -> str:
    return "\n".join(textwrap.fill(line, width=width) for line in text.split("\n"))


class CapaciteFarad(NotionScene):
    def construct(self):
        titre = scene_title("La capacité d'un condensateur et le farad")
        titre.scale(0.46)
        titre.to_edge(UP)

        # --- Énoncé -------------------------------------------------------
        mise_en_situation = Text(
            _wrap(
                "On a vu que u = q/C : la grandeur C mesure la capacité du "
                "condensateur à stocker de la charge pour une tension "
                "donnée. Comment la définit-on précisément, et dans quelle "
                "unité se mesure-t-elle ?",
                width=56,
            ),
            font_size=23,
        )
        mise_en_situation.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Nous avons déjà utilisé la relation u égale q sur C : la "
                "grandeur C mesure la capacité du condensateur à stocker de "
                "la charge pour une tension donnée. Comment la définit-on "
                "précisément, et dans quelle unité se mesure-t-elle ?"
            )
        ) as tracker:
            self.play(Write(titre))
            self.play(FadeIn(mise_en_situation))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(mise_en_situation))

        # --- Raisonnement : définition C = q/u --------------------------------
        definition_C = definition_box(
            VGroup(
                Text("La capacité d'un condensateur est le rapport, constant,", font_size=21),
                Text("de sa charge q à la tension u à ses bornes :", font_size=21),
                MathTex(r"C = \dfrac{q}{u}", font_size=34, color=YELLOW),
                Text("C s'exprime en FARADS, symbole F.", font_size=21),
            ).arrange(DOWN, buff=0.22),
            box_width=11.0,
        )
        definition_C.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "La capacité d'un condensateur est le rapport, constant "
                "pour un condensateur donné, de sa charge q à la tension u "
                "à ses bornes : C égale q sur u. Cette grandeur s'exprime "
                "en farads, de symbole F, en hommage au physicien Michael "
                "Faraday."
            )
        ) as tracker:
            self.play(FadeIn(definition_C))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(definition_C))

        # --- Raisonnement : le farad et ses sous-multiples ----------------------
        farad_def = definition_box(
            VGroup(
                Text("Un condensateur a une capacité de 1 farad s'il emmagasine", font_size=20),
                Text("une charge de 1 coulomb sous une tension de 1 volt.", font_size=20),
                Text("Le farad est une unité ÉNORME : en pratique, on utilise", font_size=20),
                Text("presque toujours ses sous-multiples.", font_size=20),
            ).arrange(DOWN, aligned_edge=LEFT, buff=0.18),
            box_width=11.4,
        )
        farad_def.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Un condensateur a une capacité de un farad s'il emmagasine "
                "une charge de un coulomb sous une tension de un volt. Le "
                "farad est en réalité une unité énorme pour les "
                "condensateurs courants : en pratique, on utilise presque "
                "toujours ses sous-multiples."
            )
        ) as tracker:
            self.play(FadeIn(farad_def))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(farad_def))

        tableau = VGroup(
            VGroup(Text("millifarad", font_size=19), MathTex("1\\ \\text{mF} = 10^{-3}\\ \\text{F}", font_size=22)).arrange(RIGHT, buff=0.4),
            VGroup(Text("microfarad", font_size=19), MathTex("1\\ \\mu\\text{F} = 10^{-6}\\ \\text{F}", font_size=22)).arrange(RIGHT, buff=0.4),
            VGroup(Text("nanofarad", font_size=19), MathTex("1\\ \\text{nF} = 10^{-9}\\ \\text{F}", font_size=22)).arrange(RIGHT, buff=0.4),
            VGroup(Text("picofarad", font_size=19), MathTex("1\\ \\text{pF} = 10^{-12}\\ \\text{F}", font_size=22)).arrange(RIGHT, buff=0.4),
        ).arrange(DOWN, buff=0.28, aligned_edge=LEFT)
        tableau_box = definition_box(tableau, box_width=9.5)
        tableau_box.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Voici les sous-multiples usuels du farad : le millifarad "
                "vaut dix puissance moins trois farad, le microfarad dix "
                "puissance moins six, le nanofarad dix puissance moins "
                "neuf, et le picofarad dix puissance moins douze. La "
                "plupart des condensateurs de nos circuits se situent entre "
                "le picofarad et quelques centaines de microfarads."
            )
        ) as tracker:
            self.play(FadeIn(tableau_box))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(tableau_box))

        # --- Exemple résolu 2 ------------------------------------------------------
        exemple = example_box(
            VGroup(
                Text("Un condensateur porte q = 24 µC sous une tension u = 6 V.", font_size=20),
                MathTex(r"C = \dfrac{q}{u} = \dfrac{24\ \mu\text{C}}{6\ \text{V}} = 4\ \mu\text{F}", font_size=28),
            ).arrange(DOWN, buff=0.25),
            box_width=11.0,
        )
        exemple.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Exemple résolu : un condensateur porte une charge de "
                "vingt-quatre microcoulombs sous une tension de six volts. "
                "Sa capacité vaut q sur u, soit vingt-quatre "
                "microcoulombs sur six volts, c'est-à-dire quatre "
                "microfarads."
            )
        ) as tracker:
            self.play(FadeIn(exemple))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(exemple))

        # --- À retenir -------------------------------------------------------------
        retenir = essentiel_box(
            VGroup(
                Text("À retenir", font_size=24, weight="BOLD"),
                MathTex(r"C = \dfrac{q}{u} \ \ (\text{farad, F})", font_size=30),
                Text("1 mF = 10⁻³ F, 1 µF = 10⁻⁶ F, 1 nF = 10⁻⁹ F, 1 pF = 10⁻¹² F.", font_size=20),
            ).arrange(DOWN, buff=0.22),
            box_width=11.6,
        )
        retenir.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Retenons l'essentiel : la capacité vaut C égale q sur u, "
                "en farads. Les sous-multiples à connaître sont le "
                "millifarad, le microfarad, le nanofarad et le picofarad, "
                "respectivement dix puissance moins trois, moins six, "
                "moins neuf et moins douze farad."
            )
        ) as tracker:
            self.play(FadeIn(retenir))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(retenir))

        # --- Pièges à éviter --------------------------------------------------------
        pieges = warning_box(
            VGroup(
                Text("• Ne pas confondre la CAPACITÉ C (en farads) avec la", font_size=20),
                Text("   CHARGE q (en coulombs) : deux lettres, deux grandeurs.", font_size=20),
                Text("• C est une caractéristique FIXE du condensateur : elle ne", font_size=20),
                Text("   dépend PAS de u, même si le rapport q/u la définit.", font_size=20),
            ).arrange(DOWN, aligned_edge=LEFT, buff=0.16),
            box_width=11.8,
        )
        pieges.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Deux pièges à éviter. Il ne faut pas confondre la "
                "capacité C, en farads, avec la charge q, en coulombs : ce "
                "sont deux grandeurs différentes. Et la capacité C est une "
                "caractéristique fixe du condensateur, liée à sa "
                "fabrication : elle ne dépend pas de la tension appliquée, "
                "même si c'est le rapport q sur u qui permet de la "
                "calculer."
            )
        ) as tracker:
            self.play(FadeIn(pieges))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(pieges), FadeOut(titre))
