"""
scenes/Maths_Denombrement_02.py — Chapitre 6 « Dénombrement » (1ereC, Maths),
scène 02.

§ Partition d'un ensemble (3 conditions), exemple d'une classe de 45
élèves répartie par âge. Théorème du principe additif, avec justification.
Conséquence 1 (complémentaire), conséquence 2 (réunion de deux parties,
Card(A∪B)=Card(A)+Card(B)-Card(A∩B)) avec démonstration complète et
diagramme de Venn.
Source : 1ereC/Maths.pdf, chapitre 6, pages 67-68.
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
from shapes.boxes import definition_box, property_box, scene_title, theorem_box


def _wrap(text: str, width: int = 54) -> str:
    return "\n".join(textwrap.fill(line, width=width) for line in text.split("\n"))


def _venn(labelA="A", labelB="B") -> VGroup:
    cA = Circle(radius=1.1, color="#1E5FA8").shift(LEFT * 0.6)
    cB = Circle(radius=1.1, color="#DE7C1F").shift(RIGHT * 0.6)
    la = MathTex(labelA, font_size=28, color="#1E5FA8").move_to(cA.get_center() + LEFT * 0.8)
    lb = MathTex(labelB, font_size=28, color="#DE7C1F").move_to(cB.get_center() + RIGHT * 0.8)
    return VGroup(cA, cB, la, lb)


class PartitionPrincipeAdditif(NotionScene):
    def construct(self):
        titre = scene_title("Dénombrement — Partition et principe additif")
        titre.scale(0.5)
        titre.to_edge(UP)

        # --- Énoncé : définition de la partition --------------------------
        def_partition = definition_box(
            VGroup(
                Text("Partition d'un ensemble E", font_size=24, weight="BOLD"),
                Text(
                    _wrap(
                        "Des parties A₁, A₂, ..., Aₖ de E forment une partition de E si :",
                        width=52,
                    ),
                    font_size=22,
                ),
                MathTex(r"1)\ \ A_i \neq \emptyset \text{ pour tout } i", font_size=24),
                MathTex(r"2)\ \ A_i \cap A_j = \emptyset \text{ si } i \neq j \text{ (disjointes)}", font_size=24),
                MathTex(r"3)\ \ A_1 \cup A_2 \cup \cdots \cup A_k = E \text{ (réunion totale)}", font_size=24),
            ).arrange(DOWN, buff=0.22),
        )
        def_partition.next_to(titre, DOWN, buff=0.35)

        with self.voiceover(
            text=(
                "Commençons par une définition essentielle : la partition "
                "d'un ensemble. Des parties A-1, A-2, jusqu'à A-k de E "
                "forment une partition de E si trois conditions sont "
                "réunies. Premièrement, aucune de ces parties n'est vide. "
                "Deuxièmement, elles sont deux à deux disjointes : leur "
                "intersection est toujours vide. Et troisièmement, leur "
                "réunion reconstitue E tout entier. Autrement dit, on "
                "découpe E en morceaux qui ne se chevauchent jamais et "
                "qui, mis bout à bout, redonnent E."
            )
        ) as tracker:
            self.play(Write(titre))
            self.play(FadeIn(def_partition))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(def_partition))

        exemple_classe = MathTex(
            r"\text{Classe de 45 élèves : } A_{16} \ (16\text{ ans}),\ A_{17}\ (17\text{ ans}),\ A_{18}\ (18\text{ ans})",
            font_size=24,
        )
        chiffres_classe = MathTex(
            r"\mathrm{Card}(A_{16})=12,\ \ \mathrm{Card}(A_{17})=20,\ \ \mathrm{Card}(A_{18})=13",
            font_size=25,
        )
        total_classe = MathTex(r"12+20+13 = 45 = \mathrm{Card}(E)", font_size=27, color=YELLOW)
        bloc_classe = VGroup(exemple_classe, chiffres_classe, total_classe).arrange(DOWN, buff=0.35)
        bloc_classe.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Voici un exemple concret : une classe de 45 élèves, "
                "répartie selon l'âge, en trois groupes : les élèves de "
                "16 ans, ceux de 17 ans, et ceux de 18 ans. On compte 12 "
                "élèves de 16 ans, 20 de 17 ans, et 13 de 18 ans. Chaque "
                "élève appartient à un seul groupe d'âge : ces trois "
                "groupes forment donc une partition de la classe. Et "
                "naturellement, 12 plus 20 plus 13 fait bien 45, l'effectif "
                "total de la classe."
            )
        ) as tracker:
            self.play(Write(bloc_classe))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(bloc_classe))

        # --- Raisonnement : principe additif -------------------------------
        theo_additif = theorem_box(
            VGroup(
                Text("Principe additif", font_size=24, weight="BOLD"),
                MathTex(
                    r"\text{Si } A_1,\dots,A_k \text{ forment une partition de } E,",
                    font_size=24,
                ),
                MathTex(
                    r"\mathrm{Card}(E) = \mathrm{Card}(A_1) + \mathrm{Card}(A_2) + \cdots + \mathrm{Card}(A_k)",
                    font_size=26,
                ),
            ).arrange(DOWN, buff=0.25),
        )
        theo_additif.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Cet exemple illustre le principe additif : si des parties "
                "A-1 à A-k forment une partition de E, alors le cardinal "
                "de E est simplement la somme des cardinaux de chaque "
                "partie. C'est vrai parce que compter les éléments de E, "
                "puisqu'ils sont répartis sans chevauchement ni oubli dans "
                "les Ai, revient exactement à compter les éléments de "
                "chaque Ai puis à additionner les résultats."
            )
        ) as tracker:
            self.play(FadeIn(theo_additif))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(theo_additif))

        # --- Conséquence 1 : complémentaire ---------------------------------
        conseq1 = property_box(
            VGroup(
                Text("Conséquence 1 — Complémentaire", font_size=23, weight="BOLD"),
                MathTex(
                    r"\{A,\, \overline{A}\} \text{ est une partition de } E",
                    font_size=25,
                ),
                MathTex(
                    r"\mathrm{Card}(\overline{A}) = \mathrm{Card}(E) - \mathrm{Card}(A)",
                    font_size=27,
                    color=YELLOW,
                ),
            ).arrange(DOWN, buff=0.25),
        )
        conseq1.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Une première conséquence directe concerne le "
                "complémentaire. Une partie A et son complémentaire "
                "A-barre forment toujours une partition de E : chaque "
                "élément de E est soit dans A, soit dans son "
                "complémentaire, jamais les deux à la fois. Le principe "
                "additif donne alors immédiatement : le cardinal du "
                "complémentaire de A est égal au cardinal de E moins le "
                "cardinal de A."
            )
        ) as tracker:
            self.play(FadeIn(conseq1))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(conseq1))

        # --- Conséquence 2 : réunion de deux parties, avec démonstration --
        conseq2_enonce = MathTex(
            r"\mathrm{Card}(A \cup B) = \mathrm{Card}(A) + \mathrm{Card}(B) - \mathrm{Card}(A \cap B)",
            font_size=27,
            color=YELLOW,
        )
        conseq2_enonce.next_to(titre, DOWN, buff=0.4)
        venn = _venn()
        venn.next_to(conseq2_enonce, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "La deuxième conséquence, plus riche, concerne la réunion "
                "de deux parties A et B, pas nécessairement disjointes "
                "cette fois. On obtient : le cardinal de A union B est "
                "égal au cardinal de A, plus le cardinal de B, moins le "
                "cardinal de A inter B. Démontrons cette formule à l'aide "
                "d'un diagramme de Venn."
            )
        ) as tracker:
            self.play(Write(conseq2_enonce))
            self.play(Create(venn))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(conseq2_enonce), FadeOut(venn))

        demo1 = MathTex(
            r"A \setminus B,\ \ A \cap B,\ \ B \setminus A \ \text{ forment une partition de } A \cup B",
            font_size=23,
        )
        demo2 = MathTex(
            r"\mathrm{Card}(A \cup B) = \mathrm{Card}(A\setminus B) + \mathrm{Card}(A\cap B) + \mathrm{Card}(B\setminus A)",
            font_size=23,
        )
        demo3 = MathTex(
            r"\mathrm{Card}(A) = \mathrm{Card}(A\setminus B) + \mathrm{Card}(A\cap B) \ \Rightarrow\ "
            r"\mathrm{Card}(A\setminus B) = \mathrm{Card}(A) - \mathrm{Card}(A\cap B)",
            font_size=22,
        )
        demo4 = MathTex(
            r"\text{De même : } \mathrm{Card}(B\setminus A) = \mathrm{Card}(B) - \mathrm{Card}(A\cap B)",
            font_size=22,
        )
        demo5 = MathTex(
            r"\mathrm{Card}(A \cup B) = \big[\mathrm{Card}(A)-\mathrm{Card}(A\cap B)\big] + \mathrm{Card}(A\cap B)"
            r" + \big[\mathrm{Card}(B)-\mathrm{Card}(A\cap B)\big]",
            font_size=20,
        )
        demo6 = MathTex(
            r"\mathrm{Card}(A \cup B) = \mathrm{Card}(A) + \mathrm{Card}(B) - \mathrm{Card}(A\cap B)",
            font_size=25,
            color=YELLOW,
        )
        demo = VGroup(demo1, demo2, demo3, demo4, demo5, demo6).arrange(DOWN, buff=0.28)
        demo.next_to(titre, DOWN, buff=0.35)

        with self.voiceover(
            text=(
                "On découpe A union B en trois morceaux disjoints : "
                "A privé de B, l'intersection A inter B, et B privé de A. "
                "Ces trois morceaux forment une partition de A union B, "
                "donc par le principe additif, le cardinal de A union B "
                "est la somme de leurs trois cardinaux. Or A lui-même se "
                "partitionne en A privé de B et A inter B, ce qui donne "
                "le cardinal de A privé de B. De même pour B privé de A. "
                "En remplaçant ces deux expressions dans la somme "
                "précédente, le terme cardinal de A inter B apparaît deux "
                "fois en plus et une fois en moins : au final, il ne "
                "reste que le cardinal de A, plus le cardinal de B, moins "
                "le cardinal de A inter B. La formule est démontrée."
            )
        ) as tracker:
            self.play(Write(demo1))
            self.play(Write(demo2))
            self.play(Write(demo3))
            self.play(Write(demo4))
            self.play(Write(demo5))
            self.play(Write(demo6))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(demo), FadeOut(titre))
