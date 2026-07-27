"""
scenes/Maths_Denombrement_03.py — Chapitre 6 « Dénombrement » (1ereC, Maths),
scène 03.

§ Exemple résolu 1 : 25 élèves, basket et/ou foot — calcul complet par
disjonction et complémentaire. Définition du produit cartésien A×B,
remarques (p-uplets, l'ordre compte).
Source : 1ereC/Maths.pdf, chapitre 6, pages 68-69.
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
    MathTex,
    Text,
    VGroup,
    Write,
)

from shapes.base_scene import NotionScene
from shapes.boxes import definition_box, example_box, scene_title


def _wrap(text: str, width: int = 54) -> str:
    return "\n".join(textwrap.fill(line, width=width) for line in text.split("\n"))


class ExempleReunionProduitCartesien(NotionScene):
    def construct(self):
        titre = scene_title("Dénombrement — Exemple résolu et produit cartésien")
        titre.scale(0.5)
        titre.to_edge(UP)

        # --- Énoncé de l'exemple résolu 1 ------------------------------------
        enonce = Text(
            _wrap(
                "Exemple résolu 1 : dans une classe de 25 élèves, 15 "
                "pratiquent le basket, 12 pratiquent le foot, et 7 "
                "pratiquent les deux sports. Combien d'élèves ne "
                "pratiquent ni l'un ni l'autre ?",
                width=56,
            ),
            font_size=24,
        )
        enonce.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Mettons en pratique le principe additif et sa deuxième "
                "conséquence sur un exemple résolu. Dans une classe de "
                "25 élèves, 15 pratiquent le basket, 12 pratiquent le "
                "foot, et 7 pratiquent les deux sports à la fois. "
                "Combien d'élèves ne pratiquent ni l'un ni l'autre ?"
            )
        ) as tracker:
            self.play(Write(titre))
            self.play(FadeIn(enonce))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(enonce))

        # --- Raisonnement : réunion puis complémentaire ----------------------
        donnees = MathTex(
            r"\mathrm{Card}(E)=25,\ \ \mathrm{Card}(B)=15,\ \ \mathrm{Card}(F)=12,\ \ \mathrm{Card}(B\cap F)=7",
            font_size=23,
        )
        etape1 = MathTex(
            r"\mathrm{Card}(B\cup F) = \mathrm{Card}(B)+\mathrm{Card}(F)-\mathrm{Card}(B\cap F)",
            font_size=25,
        )
        etape2 = MathTex(r"\mathrm{Card}(B\cup F) = 15+12-7 = 20", font_size=27, color=YELLOW)
        etape3 = MathTex(
            r"\text{« ni l'un ni l'autre » } = \overline{B\cup F}",
            font_size=24,
        )
        etape4 = MathTex(
            r"\mathrm{Card}(\overline{B\cup F}) = \mathrm{Card}(E)-\mathrm{Card}(B\cup F) = 25-20 = 5",
            font_size=26,
            color=YELLOW,
        )
        bloc = VGroup(donnees, etape1, etape2, etape3, etape4).arrange(DOWN, buff=0.32)
        bloc.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Notons E l'ensemble des 25 élèves, B ceux qui font du "
                "basket et F ceux qui font du foot. On calcule d'abord le "
                "cardinal de B union F grâce à la formule de la réunion : "
                "15 plus 12 moins 7, ce qui donne 20 élèves pratiquant au "
                "moins un des deux sports. Les élèves qui ne pratiquent "
                "ni l'un ni l'autre forment exactement le complémentaire "
                "de B union F dans E. Par la propriété du complémentaire, "
                "leur nombre est 25 moins 20, soit 5 élèves."
            )
        ) as tracker:
            self.play(Write(donnees))
            self.play(Write(etape1))
            self.play(Write(etape2))
            self.play(Write(etape3))
            self.play(Write(etape4))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(bloc))

        # --- Exemple traité : conclusion en boîte -----------------------------
        conclusion = example_box(
            VGroup(
                Text("Conclusion", font_size=24, weight="BOLD"),
                MathTex(r"5 \text{ élèves ne pratiquent ni le basket, ni le foot.}", font_size=26),
            ).arrange(DOWN, buff=0.25),
        )
        conclusion.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Conclusion : 5 élèves de la classe ne pratiquent ni le "
                "basket ni le foot. On voit ici la puissance combinée du "
                "principe additif et du passage au complémentaire."
            )
        ) as tracker:
            self.play(FadeIn(conclusion))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(conclusion))

        # --- Produit cartésien --------------------------------------------------
        def_produit = definition_box(
            VGroup(
                Text("Produit cartésien A × B", font_size=24, weight="BOLD"),
                MathTex(
                    r"A \times B = \big\{\, (a,b) \ /\ a \in A \text{ et } b \in B \,\big\}",
                    font_size=27,
                ),
                Text(
                    _wrap("(a, b) est un couple : un « 2-uplet » ordonné d'éléments de A puis de B.", width=48),
                    font_size=22,
                ),
            ).arrange(DOWN, buff=0.25),
        )
        def_produit.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Changeons de notion : introduisons le produit cartésien "
                "de deux ensembles A et B, noté A fois B. C'est l'ensemble "
                "de tous les couples, a virgule b, où a est pris dans A et "
                "b dans B. Un tel couple est aussi appelé un 2-uplet "
                "ordonné d'éléments de A puis de B."
            )
        ) as tracker:
            self.play(FadeIn(def_produit))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(def_produit))

        exemple_produit = MathTex(
            r"A=\{1,2\},\ B=\{x,y\} \ \Rightarrow\ "
            r"A\times B = \big\{(1,x),(1,y),(2,x),(2,y)\big\}",
            font_size=25,
        )
        remarque_ordre = MathTex(
            r"(1,x) \neq (x,1) \quad : \text{ l'ordre des coordonnées compte !}",
            font_size=25,
            color=YELLOW,
        )
        bloc_produit = VGroup(exemple_produit, remarque_ordre).arrange(DOWN, buff=0.4)
        bloc_produit.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Prenons A égale 1, 2 et B égale x, y. Le produit "
                "cartésien A fois B contient quatre couples : "
                "un-x, un-y, deux-x, deux-y. Remarque essentielle : dans "
                "un couple, l'ordre des coordonnées compte. Le couple "
                "un-x est totalement différent du couple x-un : ce sont "
                "deux objets distincts, contrairement à un ensemble comme "
                "la paire un-x, où l'ordre n'a pas d'importance."
            )
        ) as tracker:
            self.play(Write(exemple_produit))
            self.play(Write(remarque_ordre))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(bloc_produit), FadeOut(titre))
