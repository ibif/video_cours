"""
scenes/Chimie_ClassificationQuantitativeRedox_03.py — Chapitre 11
« Classification quantitative des couples oxydant/réducteur » (1ereC,
Chimie), scène 03.

§ 3. La pile Daniell : interprétation. Demi-équation à l'anode (Zn → Zn²⁺
+ 2e⁻, oxydation, pôle négatif) et à la cathode (Cu²⁺ + 2e⁻ → Cu,
réduction, pôle positif), équation-bilan spontanée de la pile,
`definition_box` de la force électromotrice (f.é.m.), notation
conventionnelle de la pile (⊖Zn|Zn²⁺‖Cu²⁺|Cu⊕), rôle du pont salin
(migration des ions K⁺ et Cl⁻ pour assurer l'électroneutralité des deux
compartiments).
Source : 1ereC/Chimie.pdf, chapitre 11, pages 104-105.
"""

import textwrap

from manim import (
    BLUE,
    DOWN,
    LEFT,
    ORANGE,
    RIGHT,
    UP,
    WHITE,
    YELLOW,
    Arrow,
    FadeIn,
    FadeOut,
    MathTex,
    Text,
    VGroup,
    Write,
    config,
)

from shapes.base_scene import NotionScene
from shapes.boxes import definition_box, scene_title, warning_box


def _wrap(text: str, width: int = 56) -> str:
    return "\n".join(textwrap.fill(line, width=width) for line in text.split("\n"))


def _fit(mobject, top_y):
    bas_visible = -config.frame_height / 2 + 0.25
    hauteur_dispo = top_y - bas_visible
    if mobject.height > hauteur_dispo:
        mobject.scale(hauteur_dispo / mobject.height, about_point=mobject.get_top())
    return mobject


class PileDaniellInterpretation(NotionScene):
    def construct(self):
        titre = scene_title("11.3 La pile Daniell : interprétation")
        titre.scale(0.5)
        titre.to_edge(UP)

        # --- Énoncé -----------------------------------------------------------------
        intro = Text(
            _wrap(
                "Pourquoi la lame de zinc s'amincit-elle, pourquoi la "
                "lame de cuivre s'épaissit-elle ? Écrivons les réactions "
                "qui se produisent à chaque électrode.",
                width=56,
            ),
            font_size=24,
            color=WHITE,
        )
        intro.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Pourquoi la lame de zinc s'amincit-elle et pourquoi la "
                "lame de cuivre s'épaissit-elle ? Pour le comprendre, "
                "écrivons ce qui se produit réellement à chaque "
                "électrode de la pile Daniell."
            )
        ) as tracker:
            self.play(Write(titre))
            self.play(FadeIn(intro))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(intro))

        # --- Raisonnement : demi-équations aux électrodes ---------------------------
        entete_anode = Text("À l'anode (pôle ⊖, lame de Zn) : oxydation", font_size=21, color=WHITE, weight="BOLD")
        entete_anode.next_to(titre, DOWN, buff=0.4)
        eq_anode = MathTex(r"Zn \longrightarrow Zn^{2+} + 2\,e^{-}", font_size=30, color=WHITE)
        eq_anode.next_to(entete_anode, DOWN, buff=0.35)

        entete_cathode = Text("À la cathode (pôle ⊕, lame de Cu) : réduction", font_size=21, color=ORANGE, weight="BOLD")
        entete_cathode.next_to(eq_anode, DOWN, buff=0.55)
        eq_cathode = MathTex(r"Cu^{2+} + 2\,e^{-} \longrightarrow Cu", font_size=30, color=ORANGE)
        eq_cathode.next_to(entete_cathode, DOWN, buff=0.35)

        with self.voiceover(
            text=(
                "À l'anode, la lame de zinc, qui est le pôle négatif, le "
                "zinc métal cède deux électrons pour donner l'ion zinc "
                "deux plus, qui passe en solution : c'est une oxydation, "
                "et c'est elle qui explique que la lame s'amincit. À la "
                "cathode, la lame de cuivre, qui est le pôle positif, les "
                "ions cuivre deux plus de la solution captent deux "
                "électrons pour se déposer sous forme de cuivre métal : "
                "c'est une réduction, et c'est elle qui explique que la "
                "lame s'épaissit et que la solution bleue se décolore."
            )
        ) as tracker:
            self.play(FadeIn(entete_anode))
            self.play(Write(eq_anode))
            self.play(FadeIn(entete_cathode))
            self.play(Write(eq_cathode))
            self.wait(tracker.get_remaining_duration())

        self.play(
            FadeOut(entete_anode), FadeOut(eq_anode),
            FadeOut(entete_cathode), FadeOut(eq_cathode),
        )

        # --- Équation-bilan + définition f.é.m. --------------------------------------
        entete_bilan = Text("Équation-bilan spontanée de la pile", font_size=22, color=YELLOW, weight="BOLD")
        entete_bilan.next_to(titre, DOWN, buff=0.35)
        eq_bilan = MathTex(r"Zn + Cu^{2+} \longrightarrow Zn^{2+} + Cu", font_size=32, color=WHITE)
        eq_bilan.next_to(entete_bilan, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "En additionnant les deux demi-équations, on obtient "
                "l'équation-bilan spontanée de la pile : zinc plus ion "
                "cuivre deux plus donne ion zinc deux plus plus cuivre. "
                "C'est exactement la réaction que prévoyait la règle du "
                "gamma au début du chapitre : elle se déroule "
                "spontanément et fournit l'énergie électrique récupérée "
                "par le voltmètre."
            )
        ) as tracker:
            self.play(FadeIn(entete_bilan))
            self.play(Write(eq_bilan))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(entete_bilan), FadeOut(eq_bilan))

        def_fem = definition_box(
            Text(
                _wrap(
                    "La force électromotrice (f.é.m.) E d'une pile est la "
                    "tension à ses bornes mesurée à vide (intensité nulle), "
                    "pôle positif moins pôle négatif. Elle s'exprime en "
                    "volts (V).",
                    width=48,
                ),
                font_size=23,
            ),
        )
        def_fem.next_to(titre, DOWN, buff=0.45)

        with self.voiceover(
            text=(
                "Ce que mesure le voltmètre s'appelle la force "
                "électromotrice de la pile, notée E. Par définition, "
                "c'est la tension aux bornes de la pile mesurée à vide, "
                "c'est-à-dire à intensité nulle, calculée comme le "
                "potentiel du pôle positif moins le potentiel du pôle "
                "négatif. Elle s'exprime en volts."
            )
        ) as tracker:
            self.play(FadeIn(def_fem))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(def_fem))

        # --- Exemple traité : notation conventionnelle + pont salin -----------------
        entete_notation = Text("Notation conventionnelle de la pile", font_size=21, color=YELLOW, weight="BOLD")
        entete_notation.next_to(titre, DOWN, buff=0.35)
        notation = MathTex(
            r"\ominus\ Zn\,|\,Zn^{2+}\ \Vert\ Cu^{2+}\,|\,Cu\ \oplus",
            font_size=32,
            color=WHITE,
        )
        notation.next_to(entete_notation, DOWN, buff=0.4)
        aide_notation = Text(
            "( | sépare deux phases, ‖ symbolise le pont salin )",
            font_size=17,
            color=WHITE,
        )
        aide_notation.next_to(notation, DOWN, buff=0.3)

        with self.voiceover(
            text=(
                "On résume tout cela par une notation conventionnelle : "
                "pôle négatif, zinc, barre verticale, ion zinc deux plus, "
                "double barre verticale, ion cuivre deux plus, barre "
                "verticale, cuivre, pôle positif. Chaque barre verticale "
                "simple sépare deux phases différentes en contact, et la "
                "double barre symbolise le pont salin qui relie les deux "
                "demi-piles."
            )
        ) as tracker:
            self.play(FadeIn(entete_notation))
            self.play(Write(notation))
            self.play(FadeIn(aide_notation))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(entete_notation), FadeOut(notation), FadeOut(aide_notation))

        entete_pont = Text("Rôle du pont salin", font_size=21, color=YELLOW, weight="BOLD")
        entete_pont.next_to(titre, DOWN, buff=0.35)

        pont_k = MathTex(r"K^{+}", font_size=30, color=WHITE)
        pont_k.move_to([-1.6, 0.3, 0])
        pont_cl = MathTex(r"Cl^{-}", font_size=30, color=WHITE)
        pont_cl.move_to([1.6, 0.3, 0])
        fleche_k = Arrow(pont_k.get_center() + [0.5, 0, 0], [3.2, 0.3, 0], color=YELLOW, buff=0.3)
        fleche_cl = Arrow(pont_cl.get_center() + [-0.5, 0, 0], [-3.2, 0.3, 0], color=YELLOW, buff=0.3)
        label_zn = Text("compartiment Zn²⁺\n(charge + s'accumule)", font_size=15, color=WHITE, line_spacing=0.8)
        label_zn.move_to([-3.4, -0.6, 0])
        label_cu = Text("compartiment Cu²⁺\n(charge – s'accumule)", font_size=15, color=WHITE, line_spacing=0.8)
        label_cu.move_to([3.4, -0.6, 0])

        migration = VGroup(pont_k, pont_cl, fleche_k, fleche_cl, label_zn, label_cu)
        migration.next_to(entete_pont, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Le pont salin joue un rôle essentiel : sans lui, le "
                "compartiment du zinc s'enrichirait en charges positives, "
                "à cause des ions zinc deux plus produits, et le "
                "compartiment du cuivre s'enrichirait en charges "
                "négatives, la réaction s'arrêterait presque aussitôt. Le "
                "pont salin permet aux ions potassium de migrer vers le "
                "compartiment du cuivre, et aux ions chlorure de migrer "
                "vers le compartiment du zinc, assurant ainsi "
                "l'électroneutralité des deux solutions et fermant le "
                "circuit électrique."
            )
        ) as tracker:
            self.play(FadeIn(entete_pont))
            self.play(FadeIn(migration))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(entete_pont), FadeOut(migration))

        # --- Piège à éviter -----------------------------------------------------------
        piege = warning_box(
            Text(
                _wrap(
                    "Ne pas confondre anode/cathode avec pôle négatif/pôle "
                    "positif d'après leur seul nom : dans une pile qui "
                    "débite (fonctionnement spontané), l'anode est bien le "
                    "pôle négatif (oxydation) et la cathode le pôle "
                    "positif (réduction), mais cette association "
                    "s'inverse en électrolyse.",
                    width=48,
                ),
                font_size=20,
            ),
        )
        piege.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Attention à ce piège classique : dans une pile qui "
                "débite, donc en fonctionnement spontané, l'anode est le "
                "siège de l'oxydation et correspond au pôle négatif, "
                "tandis que la cathode est le siège de la réduction et "
                "correspond au pôle positif. Mais retenez bien que cette "
                "association s'inversera plus tard, lorsque nous "
                "étudierons l'électrolyse."
            )
        ) as tracker:
            self.play(FadeIn(piege))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(piege), FadeOut(titre))
