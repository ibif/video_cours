"""
scenes/Physique_ChampElectrostatique_02.py — Chapitre 6 « Champ
électrostatique » (1ereC, Physique), scène 02.

§ Quantification de la charge, conducteurs et isolants : définition de la
charge électrique (coulomb C), charge élémentaire e=1,6×10⁻¹⁹C, charge de
l'électron/du proton, quantification (q=n·e) et conservation de la charge
dans un système isolé, sous-multiples usuels (mC, µC, nC, pC), conducteurs
(métaux) et isolants/diélectriques (verre, ébonite, plastiques).
Source : 1ereC/Physique.pdf, pages 54-65 (chapitre 6, § 1).
"""

import textwrap

import numpy as np

from manim import (
    DOWN,
    LEFT,
    RIGHT,
    UP,
    WHITE,
    YELLOW,
    BLUE,
    GREY,
    Circle,
    Create,
    Dot,
    FadeIn,
    FadeOut,
    MathTex,
    Text,
    VGroup,
    Write,
)

from shapes.base_scene import NotionScene
from shapes.boxes import definition_box, essentiel_box, example_box, property_box, scene_title, warning_box


def _wrap(text: str, width: int = 56) -> str:
    return "\n".join(textwrap.fill(line, width=width) for line in text.split("\n"))


class QuantificationChargeConducteursIsolants(NotionScene):
    def construct(self):
        titre = scene_title("Quantification de la charge, conducteurs et isolants")
        titre.scale(0.42)
        titre.to_edge(UP)

        # --- Énoncé : peut-on diviser une charge indéfiniment ? -------------------
        mise_en_situation = Text(
            _wrap(
                "Peut-on diviser une charge électrique en morceaux "
                "aussi petits que l'on veut, ou existe-t-il une plus "
                "petite quantité de charge indivisible ?",
                width=52,
            ),
            font_size=24,
        )
        mise_en_situation.next_to(titre, DOWN, buff=0.5)

        electron = Dot(DOWN * 1.0, color=BLUE, radius=0.15)
        e_label = MathTex("-e", font_size=26, color=WHITE).next_to(electron, DOWN, buff=0.2)
        proton = Dot(DOWN * 1.0 + RIGHT * 2.5, color="#B42E41", radius=0.15)
        p_label = MathTex("+e", font_size=26, color=WHITE).next_to(proton, DOWN, buff=0.2)
        particules = VGroup(electron, e_label, proton, p_label)
        particules.next_to(mise_en_situation, DOWN, buff=0.6)

        with self.voiceover(
            text=(
                "Peut-on diviser une charge électrique en morceaux aussi "
                "petits que l'on veut, ou existe-t-il, au contraire, une "
                "plus petite quantité de charge indivisible ? La réponse "
                "vient des particules élémentaires : l'électron porte la "
                "charge négative la plus petite possible, notée moins e, "
                "et le proton porte exactement la charge opposée, plus e."
            )
        ) as tracker:
            self.play(Write(titre))
            self.play(FadeIn(mise_en_situation))
            self.play(Create(particules))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(mise_en_situation), FadeOut(particules))

        # --- Définition : charge électrique et charge élémentaire -----------------
        definition = definition_box(
            VGroup(
                Text("Charge électrique", font_size=23, weight="BOLD"),
                Text("Grandeur notée q, mesurée en coulombs (C).", font_size=20),
                MathTex(r"\text{Charge élémentaire : } e = 1{,}6 \times 10^{-19}\ \text{C}", font_size=24),
                Text("Charge de l'électron : -e.  Charge du proton : +e.", font_size=20),
            ).arrange(DOWN, buff=0.22),
            box_width=11.6,
        )
        definition.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "La charge électrique, notée q, se mesure en coulombs, "
                "symbole C. La plus petite charge que l'on puisse "
                "trouver isolément dans la nature est la charge "
                "élémentaire e, qui vaut un virgule six fois dix "
                "puissance moins dix-neuf coulomb. L'électron porte la "
                "charge moins e, le proton la charge plus e."
            )
        ) as tracker:
            self.play(FadeIn(definition))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(definition))

        # --- Propriété : quantification et conservation de la charge --------------
        propriete = property_box(
            VGroup(
                Text("Quantification de la charge", font_size=23, weight="BOLD"),
                MathTex(r"q = n\, e \qquad (n \in \mathbb{Z})", font_size=30),
                Text("Toute charge est un multiple entier (signé) de e.", font_size=20),
                Text("Conservation : dans un système isolé, la charge", font_size=20),
                Text("électrique totale se conserve.", font_size=20),
            ).arrange(DOWN, buff=0.22),
            box_width=11.4,
        )
        propriete.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Toute charge électrique q est un multiple entier, "
                "positif ou négatif, de la charge élémentaire e : q "
                "égale n fois e, avec n un entier relatif. C'est la "
                "quantification de la charge. Autre propriété "
                "fondamentale : dans un système isolé, la charge "
                "électrique totale se conserve, elle ne peut ni "
                "apparaître ni disparaître, seulement se répartir "
                "autrement entre les corps en présence."
            )
        ) as tracker:
            self.play(FadeIn(propriete))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(propriete))

        # --- Sous-multiples usuels du coulomb --------------------------------------
        table = VGroup(
            MathTex(r"1\ \text{mC} = 10^{-3}\ \text{C}", font_size=27),
            MathTex(r"1\ \mu\text{C} = 10^{-6}\ \text{C}", font_size=27),
            MathTex(r"1\ \text{nC} = 10^{-9}\ \text{C}", font_size=27),
            MathTex(r"1\ \text{pC} = 10^{-12}\ \text{C}", font_size=27),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.28)
        table_box = property_box(table, box_width=8.4)
        table_box.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Comme le coulomb est une grande unité, on utilise "
                "souvent ses sous-multiples : le millicoulomb, un "
                "millième de coulomb ; le microcoulomb, un millionième ; "
                "le nanocoulomb, un milliardième ; et le picocoulomb, un "
                "millième de milliardième de coulomb."
            )
        ) as tracker:
            self.play(FadeIn(table_box))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(table_box))

        # --- Conducteurs et isolants -------------------------------------------------
        positions_charges = [
            np.array([0.3, 0.3, 0]),
            np.array([-0.4, 0.1, 0]),
            np.array([0.1, -0.5, 0]),
            np.array([-0.3, -0.2, 0]),
        ]
        conducteur = Circle(radius=0.9, color=YELLOW, stroke_width=3).move_to(LEFT * 3.0)
        charges_libres = VGroup(*[Dot(conducteur.get_center() + 0.4 * pos, color=YELLOW, radius=0.06)
                                   for pos in positions_charges])
        conducteur_label = Text("conducteur (métal)", font_size=18).next_to(conducteur, DOWN, buff=0.3)
        conducteur_g = VGroup(conducteur, charges_libres, conducteur_label)

        isolant = Circle(radius=0.9, color=GREY, stroke_width=3).move_to(RIGHT * 3.0)
        charges_fixes = VGroup(*[Dot(isolant.get_center() + 0.4 * pos, color=GREY, radius=0.06)
                                   for pos in positions_charges])
        isolant_label = Text("isolant (verre, ébonite, plastique)", font_size=18).next_to(isolant, DOWN, buff=0.3)
        isolant_g = VGroup(isolant, charges_fixes, isolant_label)

        deux_materiaux = VGroup(conducteur_g, isolant_g)
        deux_materiaux.next_to(titre, DOWN, buff=0.6)

        with self.voiceover(
            text=(
                "Enfin, tous les matériaux ne laissent pas circuler les "
                "charges de la même façon. Dans un conducteur, comme les "
                "métaux, certaines charges sont libres de se déplacer "
                "dans tout le matériau. Dans un isolant, aussi appelé "
                "diélectrique, comme le verre, l'ébonite ou les "
                "plastiques, les charges restent fixées à l'endroit où "
                "elles ont été déposées."
            )
        ) as tracker:
            self.play(Create(conducteur), FadeIn(charges_libres), Write(conducteur_label))
            self.play(Create(isolant), FadeIn(charges_fixes), Write(isolant_label))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(deux_materiaux))

        # --- Exemple résolu : conversion de sous-multiples --------------------------
        exemple = example_box(
            VGroup(
                Text("Une charge q = 5 µC. Combien vaut-elle en coulombs ?", font_size=21),
                MathTex(r"q = 5\ \mu\text{C} = 5\times 10^{-6}\ \text{C}", font_size=27, color=YELLOW),
            ).arrange(DOWN, buff=0.28),
            box_width=10.4,
        )
        exemple.next_to(titre, DOWN, buff=0.45)

        with self.voiceover(
            text=(
                "Exemple : une charge q vaut cinq microcoulombs. En "
                "coulombs, cela s'écrit cinq fois dix puissance moins six "
                "coulomb."
            )
        ) as tracker:
            self.play(FadeIn(exemple))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(exemple))

        # --- À retenir -----------------------------------------------------------------
        retenir = essentiel_box(
            VGroup(
                Text("À retenir", font_size=24, weight="BOLD"),
                MathTex(r"e = 1{,}6\times 10^{-19}\ \text{C} \qquad q = n\, e", font_size=26),
                Text("Charge conservée dans un système isolé.", font_size=20),
                Text("Conducteur : charges libres. Isolant : charges fixes.", font_size=20),
            ).arrange(DOWN, buff=0.22),
            box_width=12.0,
        )
        retenir.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Retenons l'essentiel : la charge élémentaire vaut un "
                "virgule six fois dix puissance moins dix-neuf coulomb, "
                "et toute charge q est un multiple entier n fois e. La "
                "charge se conserve dans un système isolé. Enfin, un "
                "conducteur possède des charges libres de se déplacer, "
                "alors qu'un isolant garde ses charges fixées."
            )
        ) as tracker:
            self.play(FadeIn(retenir))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(retenir))

        # --- Piège à éviter -------------------------------------------------------------
        piege = warning_box(
            VGroup(
                Text("• Toujours convertir les sous-multiples (µC, nC, pC)", font_size=20),
                Text("   en coulombs AVANT tout calcul avec la loi de", font_size=20),
                Text("   Coulomb ou le champ électrostatique.", font_size=20),
                Text("• Une erreur de préfixe change le résultat d'un", font_size=20),
                Text("   facteur 10³, 10⁶, voire 10⁹ !", font_size=20),
            ).arrange(DOWN, aligned_edge=LEFT, buff=0.16),
            box_width=11.6,
        )
        piege.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Piège à éviter : il faut toujours convertir les "
                "sous-multiples, microcoulomb, nanocoulomb, picocoulomb, "
                "en coulombs avant tout calcul. Une erreur de préfixe "
                "change le résultat d'un facteur mille, un million, "
                "voire un milliard."
            )
        ) as tracker:
            self.play(FadeIn(piege))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(piege), FadeOut(titre))
