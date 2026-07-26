"""
scenes/Maths_Probabilite_04.py — Chapitre 12 « Probabilité » (1ereC, Maths),
scène 04.

§ Définition d'une probabilité sur un univers fini (p_i ∈ [0;1], somme
des p_i = 1, P(A) = somme des p_i des issues de A) et 5 propriétés
fondamentales (P(Ω)=1, P(Ā)=1-P(A), incompatibles ⟹ additivité, formule
générale P(A∪B)=P(A)+P(B)-P(A∩B), A⊂B ⟹ P(A)≤P(B)) — avec démonstration
de P(Ā)=1-P(A) et de la formule de la réunion (diagramme de Venn).
Exemple résolu : jeu de 32 cartes, P(C∪R)=8/32+4/32-1/32=11/32.
Source : 1ereC/Maths.pdf, chapitre 12, pages 145-147.
"""

import textwrap

from manim import DOWN, LEFT, RIGHT, UP, YELLOW, Circle, FadeIn, FadeOut, MathTex, Text, VGroup, Write

from shapes.base_scene import NotionScene
from shapes.boxes import definition_box, example_box, scene_title, theorem_box


def _wrap(text: str, width: int = 54) -> str:
    return "\n".join(textwrap.fill(line, width=width) for line in text.split("\n"))


def _diagramme_venn() -> VGroup:
    cercle_A = Circle(radius=1.0, color=YELLOW).shift(LEFT * 0.55)
    cercle_B = Circle(radius=1.0, color="#288073").shift(RIGHT * 0.55)
    label_A = MathTex("A", font_size=26, color=YELLOW).move_to(cercle_A.get_center() + LEFT * 0.6)
    label_B = MathTex("B", font_size=26, color="#288073").move_to(cercle_B.get_center() + RIGHT * 0.6)
    return VGroup(cercle_A, cercle_B, label_A, label_B)


class DefinitionProbabiliteProprietes(NotionScene):
    def construct(self):
        titre = scene_title("Probabilité — Définition et propriétés")
        titre.scale(0.5)
        titre.to_edge(UP)

        # --- Énoncé : mise en situation --------------------------------------
        mise_en_situation = Text(
            _wrap(
                "À chaque issue de Ω, on associe un nombre entre 0 et 1 "
                "qui mesure sa « chance » de se produire : c'est une "
                "probabilité. Formalisons cette idée.",
                width=56,
            ),
            font_size=24,
        )
        mise_en_situation.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "À chaque issue de l'univers Ω, on associe un nombre "
                "compris entre 0 et 1, qui mesure sa chance de se "
                "produire : c'est une probabilité. Formalisons "
                "précisément cette idée."
            )
        ) as tracker:
            self.play(Write(titre))
            self.play(FadeIn(mise_en_situation))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(mise_en_situation))

        # --- Raisonnement : définition ----------------------------------------
        definition = definition_box(
            VGroup(
                Text("Probabilité sur un univers fini", font_size=23, weight="BOLD"),
                MathTex(r"\Omega = \{e_1\,;\,e_2\,;\,\dots\,;\,e_n\}", font_size=24),
                MathTex(r"\text{À chaque } e_i \text{ on associe } p_i \in [0\,;\,1] \text{ tel que } \textstyle\sum_i p_i = 1", font_size=23),
                MathTex(r"P(A) = \sum_{e_i \in A} p_i \quad \text{(somme des } p_i \text{ des issues de } A\text{)}", font_size=23),
            ).arrange(DOWN, buff=0.22),
        )
        definition.next_to(titre, DOWN, buff=0.35)

        with self.voiceover(
            text=(
                "Définir une probabilité sur un univers fini Ω, c'est "
                "associer à chaque issue e-i un nombre p-i compris entre 0 "
                "et 1, appelé sa probabilité, de sorte que la somme de "
                "tous ces nombres p-i vaille exactement 1. La probabilité "
                "d'un événement A, notée P de A, est alors simplement la "
                "somme des p-i des issues qui composent A."
            )
        ) as tracker:
            self.play(FadeIn(definition))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(definition))

        # --- Théorème : 5 propriétés fondamentales -------------------------------
        proprietes = theorem_box(
            VGroup(
                Text("5 propriétés fondamentales", font_size=22, weight="BOLD"),
                MathTex(r"1)\ P(\Omega) = 1 \qquad\qquad 2)\ P(\overline{A}) = 1 - P(A)", font_size=21),
                MathTex(r"3)\ A \cap B = \emptyset \ \Rightarrow\ P(A \cup B) = P(A) + P(B)", font_size=21),
                MathTex(r"4)\ P(A \cup B) = P(A) + P(B) - P(A \cap B) \quad \text{(cas général)}", font_size=21),
                MathTex(r"5)\ A \subset B \ \Rightarrow\ P(A) \le P(B)", font_size=21),
            ).arrange(DOWN, buff=0.22),
        )
        proprietes.next_to(titre, DOWN, buff=0.35)

        with self.voiceover(
            text=(
                "Cinq propriétés découlent directement de cette "
                "définition. Un : la probabilité de l'univers tout entier "
                "vaut 1. Deux : la probabilité du contraire de A vaut 1 "
                "moins la probabilité de A. Trois : si A et B sont "
                "incompatibles, la probabilité de leur réunion est la "
                "somme des probabilités. Quatre, cas général, sans "
                "incompatibilité : il faut retrancher la probabilité de "
                "l'intersection, pour ne pas la compter deux fois. Cinq : "
                "si A est inclus dans B, alors la probabilité de A est "
                "inférieure ou égale à celle de B."
            )
        ) as tracker:
            self.play(Write(proprietes))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(proprietes))

        # --- Démonstration 1 : P(Ā) = 1 - P(A) --------------------------------
        demo1_titre = Text("Démonstration — P(Ā) = 1 − P(A)", font_size=23, weight="BOLD")
        demo1 = VGroup(
            MathTex(r"A \cup \overline{A} = \Omega \quad \text{et} \quad A \cap \overline{A} = \emptyset", font_size=24),
            MathTex(r"\text{Propriété 3 (incompatibles)} \ \Rightarrow\ P(A) + P(\overline{A}) = P(\Omega) = 1", font_size=23),
            MathTex(r"\Rightarrow\ P(\overline{A}) = 1 - P(A)", font_size=25, color=YELLOW),
        ).arrange(DOWN, buff=0.28)
        bloc_demo1 = VGroup(demo1_titre, demo1).arrange(DOWN, buff=0.35)
        bloc_demo1.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Démontrons la propriété 2. On sait que A et son "
                "contraire sont incompatibles, et que leur réunion est Ω "
                "tout entier. La propriété 3, l'additivité pour des "
                "événements incompatibles, donne alors : P de A plus P du "
                "contraire de A égale P de Ω, c'est-à-dire 1. Il suffit de "
                "réarranger pour obtenir P du contraire de A égale 1 moins "
                "P de A."
            )
        ) as tracker:
            self.play(Write(demo1_titre))
            self.play(Write(demo1))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(bloc_demo1))

        # --- Démonstration 2 : formule de la réunion (diagramme de Venn) --------
        demo2_titre = Text("Démonstration — P(A∪B) = P(A)+P(B)−P(A∩B)", font_size=20, weight="BOLD")
        venn = _diagramme_venn()
        venn.scale(0.75)
        explication = Text(
            _wrap(
                "En additionnant P(A) et P(B), la zone A∩B (au centre) "
                "est comptée deux fois : il faut la retrancher une fois.",
                width=42,
            ),
            font_size=19,
        )
        bloc_droite = VGroup(venn, explication).arrange(DOWN, buff=0.3)
        bloc_demo2 = VGroup(demo2_titre, bloc_droite).arrange(DOWN, buff=0.35)
        bloc_demo2.next_to(titre, DOWN, buff=0.35)

        with self.voiceover(
            text=(
                "Démontrons maintenant la formule générale, à l'aide d'un "
                "diagramme de Venn. Quand on additionne P de A et P de B, "
                "la zone commune, A inter B, représentée au centre du "
                "diagramme, se retrouve comptée deux fois : une fois dans "
                "P de A, une fois dans P de B. Il faut donc la retrancher "
                "exactement une fois pour retrouver la vraie probabilité "
                "de la réunion."
            )
        ) as tracker:
            self.play(Write(demo2_titre))
            self.play(FadeIn(venn))
            self.play(FadeIn(explication))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(bloc_demo2))

        # --- Exemple traité : jeu de 32 cartes ------------------------------------
        enonce = Text(
            _wrap(
                "Exemple résolu : dans un jeu de 32 cartes, on tire une "
                "carte au hasard. C=« carte de Cœur » (8 cartes), "
                "R=« Roi » (4 cartes), 1 seule carte est à la fois "
                "Cœur ET Roi.",
                width=54,
            ),
            font_size=22,
        )
        enonce.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Passons à l'exemple résolu. Dans un jeu de 32 cartes, on "
                "tire une carte au hasard. On note C l'événement « la "
                "carte est un Cœur », qui compte 8 cartes, et R "
                "l'événement « la carte est un Roi », qui compte 4 cartes. "
                "Une seule carte, le Roi de Cœur, est à la fois Cœur et "
                "Roi."
            )
        ) as tracker:
            self.play(FadeIn(enonce))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(enonce))

        calcul = VGroup(
            MathTex(r"P(C) = \dfrac{8}{32} \qquad P(R) = \dfrac{4}{32} \qquad P(C \cap R) = \dfrac{1}{32}", font_size=24),
            MathTex(r"P(C \cup R) = \dfrac{8}{32} + \dfrac{4}{32} - \dfrac{1}{32} = \dfrac{11}{32}", font_size=27, color=YELLOW),
        ).arrange(DOWN, buff=0.4)
        calcul.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "On a donc P de C égale 8 trente-deuxièmes, P de R égale 4 "
                "trente-deuxièmes, et P de C inter R égale 1 "
                "trente-deuxième. En appliquant la formule générale : P de "
                "C union R égale 8 trente-deuxièmes plus 4 trente-deuxièmes "
                "moins 1 trente-deuxième, soit 11 trente-deuxièmes."
            )
        ) as tracker:
            self.play(Write(calcul[0]))
            self.play(Write(calcul[1]))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(calcul))

        # --- À retenir -----------------------------------------------------------
        recap = example_box(
            VGroup(
                Text("À retenir", font_size=22, weight="BOLD"),
                MathTex(r"\text{Incompatibles} \to \text{on ADDITIONNE simplement.}", font_size=22),
                MathTex(r"\text{Sinon} \to \text{on retranche } P(A \cap B) \text{ pour ne pas surcompter.}", font_size=22),
            ).arrange(DOWN, buff=0.22),
        )
        recap.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Retenons la règle pratique : si A et B sont "
                "incompatibles, on additionne simplement leurs "
                "probabilités. Sinon, il faut systématiquement retrancher "
                "la probabilité de leur intersection, pour ne pas la "
                "surcompter."
            )
        ) as tracker:
            self.play(FadeIn(recap))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(recap), FadeOut(titre))
