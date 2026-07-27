"""
scenes/Physique_ChampElectrostatique_01.py — Chapitre 6 « Champ
électrostatique » (1ereC, Physique), scène 01.

§ Électrisation et les deux types de charges : expériences (bâton
d'ébonite frotté à la fourrure, pendule électrostatique attiré puis
repoussé), définition de l'électrisation (frottement, contact, influence),
expériences avec deux bâtons (ébonite-ébonite et verre-verre se
repoussent, verre-ébonite s'attirent) → deux types de charges (+ et -),
règle d'interaction (même signe repousse, signes contraires attirent).
Source : 1ereC/Physique.pdf, pages 54-65 (chapitre 6, § 1).
"""

import textwrap

from manim import (
    DOWN,
    LEFT,
    RIGHT,
    UP,
    WHITE,
    YELLOW,
    BLUE,
    RED,
    Circle,
    Create,
    Dot,
    FadeIn,
    FadeOut,
    Line,
    MathTex,
    Rectangle,
    Text,
    VGroup,
    Write,
)

from shapes.base_scene import NotionScene
from shapes.boxes import definition_box, essentiel_box, example_box, property_box, scene_title, warning_box


def _wrap(text: str, width: int = 56) -> str:
    return "\n".join(textwrap.fill(line, width=width) for line in text.split("\n"))


class ElectrisationDeuxTypesDeCharges(NotionScene):
    def construct(self):
        titre = scene_title("L'électrisation et les deux types de charges")
        titre.scale(0.46)
        titre.to_edge(UP)

        # --- Énoncé : bâton d'ébonite frotté, pendule électrostatique -------------
        baton = Rectangle(width=1.8, height=0.25, color="#3a2a1a", fill_color="#3a2a1a", fill_opacity=1)
        baton.rotate(0.15)
        baton.move_to(LEFT * 3.4 + UP * 0.8)
        fil = Line(baton.get_center() + DOWN * 2.0, baton.get_center() + DOWN * 0.6, color=WHITE, stroke_width=1.5)
        fil.shift(RIGHT * 2.2)
        boule = Dot(fil.get_end(), color=WHITE, radius=0.16)
        schema = VGroup(baton, fil, boule)
        schema.move_to(LEFT * 2.8)

        mise_en_situation = Text(
            _wrap(
                "Frottons un bâton d'ébonite avec de la fourrure, puis "
                "approchons-le d'une petite boule de sureau suspendue à un "
                "fil, initialement neutre. Que se passe-t-il ?",
                width=42,
            ),
            font_size=22,
        )
        mise_en_situation.next_to(schema, RIGHT, buff=0.6)

        with self.voiceover(
            text=(
                "Frottons un bâton d'ébonite avec de la fourrure, puis "
                "approchons-le d'une petite boule de sureau suspendue à un "
                "fil, initialement neutre. Que se passe-t-il ? "
                "L'électrisation, c'est cela : un corps qui acquiert des "
                "propriétés électriques qu'il n'avait pas auparavant."
            )
        ) as tracker:
            self.play(Write(titre))
            self.play(Create(schema))
            self.play(FadeIn(mise_en_situation))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(schema), FadeOut(mise_en_situation))

        # --- Raisonnement : la boule est d'abord attirée, puis repoussée ---------
        boule2 = Dot(LEFT * 2.5, color=WHITE, radius=0.16)
        baton2 = Rectangle(width=1.6, height=0.22, color="#3a2a1a", fill_color="#3a2a1a", fill_opacity=1)
        baton2.move_to(RIGHT * 2.0)
        fleche_attire = MathTex(r"\longrightarrow", font_size=30, color=YELLOW).next_to(boule2, RIGHT, buff=0.2)
        etape1 = VGroup(boule2, fleche_attire, baton2)
        etape1_label = Text("1) attirée, puis touche le bâton", font_size=20).next_to(etape1, DOWN, buff=0.3)

        boule3 = Dot(LEFT * 1.2, color=YELLOW, radius=0.16)
        baton3 = Rectangle(width=1.6, height=0.22, color="#3a2a1a", fill_color="#3a2a1a", fill_opacity=1)
        baton3.move_to(RIGHT * 2.0)
        fleche_repousse = MathTex(r"\longleftarrow", font_size=30, color=YELLOW).next_to(boule3, LEFT, buff=0.2)
        etape2 = VGroup(fleche_repousse, boule3, baton3)
        etape2_label = Text("2) repoussée après le contact", font_size=20).next_to(etape2, DOWN, buff=0.3)

        groupe = VGroup(
            VGroup(etape1, etape1_label).arrange(DOWN, buff=0.3),
            VGroup(etape2, etape2_label).arrange(DOWN, buff=0.3),
        ).arrange(DOWN, buff=0.6)
        groupe.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "On observe deux phases : d'abord, la boule neutre est "
                "attirée par le bâton chargé, jusqu'à le toucher. Puis, "
                "après ce contact, elle est repoussée. Ce contact a "
                "transféré une partie de la charge du bâton à la boule : "
                "on dit que la boule a été électrisée par contact. Le fait "
                "qu'elle soit ensuite repoussée montre qu'elle porte "
                "maintenant une charge de même nature que celle du bâton."
            )
        ) as tracker:
            self.play(Create(etape1), Write(etape1_label))
            self.play(Create(etape2), Write(etape2_label))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(groupe))

        # --- Définition : l'électrisation, trois modes ----------------------------
        definition = definition_box(
            VGroup(
                Text("Électrisation", font_size=24, weight="BOLD"),
                Text(
                    "Un corps s'électrise lorsqu'il acquiert une charge électrique.",
                    font_size=21,
                ),
                Text("Trois modes : par frottement, par contact, par influence", font_size=21),
                Text("(ce dernier se produit à distance, sans aucun contact).", font_size=21),
            ).arrange(DOWN, buff=0.22),
            box_width=11.8,
        )
        definition.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Un corps s'électrise lorsqu'il acquiert une charge "
                "électrique. On distingue trois modes d'électrisation : "
                "par frottement, comme le bâton d'ébonite sur la fourrure ; "
                "par contact, comme la boule qui touche le bâton chargé ; "
                "et par influence, où un corps chargé approché à distance, "
                "sans aucun contact, modifie la répartition des charges "
                "d'un autre corps."
            )
        ) as tracker:
            self.play(FadeIn(definition))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(definition))

        # --- Deux bâtons : deux types de charges -----------------------------------
        eb1 = Dot(LEFT * 3.2, color=BLUE, radius=0.18)
        eb2 = Dot(LEFT * 1.6, color=BLUE, radius=0.18)
        eb_label = MathTex("-", font_size=26, color=WHITE)
        eb_repel = MathTex(r"\leftrightarrow", font_size=28, color=YELLOW).move_to((eb1.get_center() + eb2.get_center()) / 2)
        ligne1 = VGroup(eb1, eb2, eb_repel)
        ligne1_txt = Text("ébonite-ébonite : se repoussent", font_size=19).next_to(ligne1, DOWN, buff=0.25)

        v1 = Dot(RIGHT * 0.4, color=RED, radius=0.18)
        v2 = Dot(RIGHT * 2.0, color=RED, radius=0.18)
        v_repel = MathTex(r"\leftrightarrow", font_size=28, color=YELLOW).move_to((v1.get_center() + v2.get_center()) / 2)
        ligne2 = VGroup(v1, v2, v_repel)
        ligne2_txt = Text("verre-verre : se repoussent", font_size=19).next_to(ligne2, DOWN, buff=0.25)

        eb3 = Dot(LEFT * 3.2 + DOWN * 2.2, color=BLUE, radius=0.18)
        v3 = Dot(LEFT * 1.6 + DOWN * 2.2, color=RED, radius=0.18)
        attire = MathTex(r"\rightarrow\!\leftarrow", font_size=26, color=YELLOW).move_to((eb3.get_center() + v3.get_center()) / 2)
        ligne3 = VGroup(eb3, v3, attire)
        ligne3_txt = Text("verre-ébonite : s'attirent", font_size=19).next_to(ligne3, DOWN, buff=0.25)

        experiences = VGroup(
            VGroup(ligne1, ligne1_txt).arrange(DOWN, buff=0.2),
            VGroup(ligne2, ligne2_txt).arrange(DOWN, buff=0.2),
        ).arrange(RIGHT, buff=1.2)
        experiences.next_to(titre, DOWN, buff=0.5)
        troisieme = VGroup(ligne3, ligne3_txt).arrange(DOWN, buff=0.2)
        troisieme.next_to(experiences, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Frottons maintenant deux bâtons identiques et approchons-les "
                "l'un de l'autre. Deux bâtons d'ébonite frottés se "
                "repoussent. Deux bâtons de verre frottés se repoussent "
                "également. Mais un bâton d'ébonite et un bâton de verre, "
                "tous deux frottés, s'attirent. Conclusion : il existe deux "
                "types de charges électriques, que l'on appelle charge "
                "positive et charge négative. L'ébonite frottée porte une "
                "charge négative, le verre frotté une charge positive."
            )
        ) as tracker:
            self.play(Create(ligne1), Write(ligne1_txt))
            self.play(Create(ligne2), Write(ligne2_txt))
            self.play(Create(ligne3), Write(ligne3_txt))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(experiences), FadeOut(troisieme))

        # --- Propriété : règle d'interaction ---------------------------------------
        regle = property_box(
            VGroup(
                Text("Règle d'interaction entre charges", font_size=23, weight="BOLD"),
                Text("Deux charges de même signe se repoussent.", font_size=21),
                Text("Deux charges de signes contraires s'attirent.", font_size=21),
            ).arrange(DOWN, buff=0.22),
            box_width=11.0,
        )
        regle.next_to(titre, DOWN, buff=0.45)

        with self.voiceover(
            text=(
                "Retenons la règle d'interaction : deux charges de même "
                "signe se repoussent, deux charges de signes contraires "
                "s'attirent."
            )
        ) as tracker:
            self.play(FadeIn(regle))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(regle))

        # --- Exemple résolu : ballons de baudruche ---------------------------------
        exemple = example_box(
            VGroup(
                Text(
                    "Deux ballons de baudruche frottés sur des cheveux secs",
                    font_size=21,
                ),
                Text(
                    "se chargent de la même façon, puis se repoussent",
                    font_size=21,
                ),
                Text("quand on les approche l'un de l'autre.", font_size=21),
                MathTex(r"\Rightarrow \ \text{même signe de charge}", font_size=25, color=YELLOW),
            ).arrange(DOWN, buff=0.22),
            box_width=11.4,
        )
        exemple.next_to(titre, DOWN, buff=0.45)

        with self.voiceover(
            text=(
                "Exemple : deux ballons de baudruche frottés sur des "
                "cheveux secs se chargent de la même façon, puis se "
                "repoussent lorsqu'on les approche l'un de l'autre. Cette "
                "répulsion prouve qu'ils portent des charges de même "
                "signe."
            )
        ) as tracker:
            self.play(FadeIn(exemple))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(exemple))

        # --- À retenir ---------------------------------------------------------------
        retenir = essentiel_box(
            VGroup(
                Text("À retenir", font_size=24, weight="BOLD"),
                Text("Un corps s'électrise par frottement, contact ou influence.", font_size=20),
                Text("Il existe deux types de charges : positive et négative.", font_size=20),
                Text("Même signe → répulsion. Signes contraires → attraction.", font_size=20),
            ).arrange(DOWN, buff=0.22),
            box_width=12.0,
        )
        retenir.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Retenons l'essentiel : un corps s'électrise par "
                "frottement, par contact ou par influence. Il existe deux "
                "types de charges, positive et négative. Deux charges de "
                "même signe se repoussent, deux charges de signes "
                "contraires s'attirent."
            )
        ) as tracker:
            self.play(FadeIn(retenir))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(retenir))

        # --- Piège à éviter -----------------------------------------------------------
        piege = warning_box(
            VGroup(
                Text("• Une ATTRACTION seule ne prouve pas des charges", font_size=20),
                Text("   de signes opposés : un corps chargé attire aussi", font_size=20),
                Text("   un corps NEUTRE par influence.", font_size=20),
                Text("• Seule une RÉPULSION prouve avec certitude que", font_size=20),
                Text("   les deux corps portent des charges de même signe.", font_size=20),
            ).arrange(DOWN, aligned_edge=LEFT, buff=0.16),
            box_width=12.0,
        )
        piege.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Attention à un piège classique : une attraction seule ne "
                "prouve pas que deux corps portent des charges de signes "
                "opposés, car un corps chargé attire aussi un corps "
                "parfaitement neutre, par influence. Seule une répulsion "
                "prouve avec certitude que les deux corps portent des "
                "charges de même signe."
            )
        ) as tracker:
            self.play(FadeIn(piege))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(piege), FadeOut(titre))
