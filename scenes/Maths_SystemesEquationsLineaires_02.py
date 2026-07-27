"""
scenes/Maths_SystemesEquationsLineaires_02.py — Chapitre 13 « Systèmes
d'équations linéaires dans ℝ² et ℝ³ » (1ereC, Maths), scène 02.

§ Méthode de combinaison linéaire (quand aucun coefficient ne vaut ±1),
exemple résolu 2 (3x+4y=18, 5x-2y=4 → 𝒮={(2;3)}), définition du
déterminant D=ab'-a'b, à retenir, piège (erreur de signe à l'addition).
Source : 1ereC/Maths.pdf, chapitre 13, pages 154-164.
"""

import textwrap

from manim import DOWN, LEFT, UP, FadeIn, FadeOut, MathTex, Text, VGroup, Write, YELLOW

from shapes.base_scene import NotionScene
from shapes.boxes import definition_box, example_box, method_box, scene_title, warning_box


def _wrap(text: str, width: int = 56) -> str:
    return "\n".join(textwrap.fill(line, width=width) for line in text.split("\n"))


class CombinaisonLineaireDeterminant(NotionScene):
    def construct(self):
        titre = scene_title("Systèmes linéaires 2×2 — Combinaison, déterminant")
        titre.scale(0.5)
        titre.to_edge(UP)

        # --- Énoncé : limite de la substitution -------------------------------
        systeme_gene = MathTex(
            r"\begin{cases} 3x + 4y = 18 \\ 5x - 2y = 4 \end{cases}",
            font_size=30,
        )
        texte_limite = Text(
            _wrap(
                "Ici, aucun coefficient ne vaut 1 ou -1 : isoler une "
                "inconnue ferait apparaître des fractions dès la première "
                "étape. La substitution reste possible, mais devient "
                "lourde.",
                width=56,
            ),
            font_size=24,
        )
        bloc_limite = VGroup(systeme_gene, texte_limite).arrange(DOWN, buff=0.4)
        bloc_limite.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Reprenons un système un peu différent : trois x plus "
                "quatre y égale dix-huit, et cinq x moins deux y égale "
                "quatre. Cette fois, aucun coefficient ne vaut un ou moins "
                "un : isoler une inconnue ferait immédiatement apparaître "
                "des fractions. La substitution reste possible, mais "
                "devient lourde. Il existe une seconde méthode, souvent "
                "plus efficace dans ce cas : la combinaison linéaire."
            )
        ) as tracker:
            self.play(Write(titre))
            self.play(FadeIn(bloc_limite))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(bloc_limite))

        # --- Raisonnement : méthode combinaison linéaire -----------------------
        methode = VGroup(
            Text("1. Choisir l'inconnue à éliminer (x ou y).", font_size=24),
            Text("2. Multiplier une (ou les deux) équation(s) pour que", font_size=24),
            Text("    ses coefficients deviennent opposés.", font_size=24),
            Text("3. Additionner les deux équations : l'inconnue disparaît.", font_size=24),
            Text("4. Résoudre, puis revenir à une équation de départ.", font_size=24),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.24)
        methode_box = method_box(methode, box_width=12.0)
        methode_box.next_to(titre, DOWN, buff=0.35)

        with self.voiceover(
            text=(
                "Voici la méthode de combinaison linéaire. Première étape : "
                "choisir l'inconnue à éliminer, x ou y. Deuxième étape : "
                "multiplier une ou les deux équations par des nombres bien "
                "choisis, pour que les coefficients de cette inconnue "
                "deviennent opposés. Troisième étape : additionner membre à "
                "membre les deux équations obtenues : l'inconnue choisie "
                "disparaît. Quatrième étape : résoudre l'équation restante, "
                "puis revenir à l'une des équations de départ pour trouver "
                "la seconde inconnue."
            )
        ) as tracker:
            self.play(FadeIn(methode_box))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(methode_box))

        # --- Exemple traité 2 ------------------------------------------------------
        ex2_enonce = MathTex(
            r"\begin{cases} 3x + 4y = 18 \\ 5x - 2y = 4 \end{cases}",
            font_size=29,
        )
        ex2_mult = MathTex(
            r"(2\text{e éq.})\times 2 : \quad 10x - 4y = 8",
            font_size=27,
        )
        ex2_add = MathTex(
            r"3x+4y=18 \ \; + \ \; 10x-4y=8 \ \Longrightarrow\ 13x = 26",
            font_size=26,
        )
        ex2_x = MathTex(r"x = 2", font_size=28, color=YELLOW)
        ex2_y = MathTex(r"5\times 2 - 2y = 4 \;\Longrightarrow\; y = 3", font_size=28, color=YELLOW)
        ex2_concl = MathTex(r"\mathcal{S} = \{(2\,;\,3)\}", font_size=30, color=YELLOW)
        ex2 = VGroup(ex2_enonce, ex2_mult, ex2_add, ex2_x, ex2_y, ex2_concl).arrange(
            DOWN, buff=0.26
        )
        ex2_box = example_box(ex2, box_width=11.8)
        ex2_box.scale(0.82)
        ex2_box.next_to(titre, DOWN, buff=0.3)

        with self.voiceover(
            text=(
                "Reprenons notre système : trois x plus quatre y égale "
                "dix-huit, cinq x moins deux y égale quatre. Le coefficient "
                "de y y est déjà quatre et moins deux : en multipliant la "
                "seconde équation par deux, on obtient dix x moins quatre "
                "y égale huit, un coefficient exactement opposé à celui de "
                "la première équation. On additionne alors membre à membre "
                ": les termes en y s'annulent, et il reste treize x égale "
                "vingt-six, donc x égale deux. On revient à la seconde "
                "équation de départ : cinq fois deux moins deux y égale "
                "quatre, ce qui donne y égale trois. L'ensemble des "
                "solutions est S égale l'ensemble contenant le couple "
                "deux, trois."
            )
        ) as tracker:
            self.play(FadeIn(ex2_box))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(ex2_box))

        # --- À retenir : définition du déterminant ------------------------------
        def_determinant = definition_box(
            VGroup(
                Text("Déterminant du système", font_size=24, weight="BOLD"),
                MathTex(
                    r"D = \begin{vmatrix} a & b \\ a' & b' \end{vmatrix} = a b' - a' b"
                    r"\quad \text{pour } \begin{cases} ax+by=c \\ a'x+b'y=c' \end{cases}",
                    font_size=26,
                ),
                MathTex(
                    r"\text{Ici : } D = 3\times(-2) - 5\times 4 = -6-20 = -26",
                    font_size=25,
                    color=YELLOW,
                ),
            ).arrange(DOWN, buff=0.28),
        )
        def_determinant.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "La combinaison linéaire mélange en réalité toujours les "
                "mêmes coefficients : cela conduit à définir le "
                "déterminant du système, noté D, égal à a b prime moins a "
                "prime b, où a, b, a prime, b prime sont les coefficients "
                "des inconnues dans le système a x plus b y égale c, a "
                "prime x plus b prime y égale c prime. Sur notre exemple, D "
                "vaut trois fois moins deux, moins cinq fois quatre, soit "
                "moins vingt-six. Ce nombre D va nous permettre, dans la "
                "scène suivante, de résoudre directement tout système 2×2 "
                "sans repasser par toutes ces étapes."
            )
        ) as tracker:
            self.play(FadeIn(def_determinant))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(def_determinant))

        # --- Piège à éviter --------------------------------------------------------
        piege = warning_box(
            Text(
                "En additionnant les deux équations transformées, vérifier\n"
                "soigneusement le signe de chaque terme : une inconnue mal\n"
                "éliminée (signe oublié) fausse tout le reste du calcul.",
                font_size=23,
            ),
            box_width=12.0,
        )
        piege.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Piège fréquent avec cette méthode : au moment d'additionner "
                "les deux équations transformées, il faut vérifier "
                "soigneusement le signe de chaque terme. Une inconnue mal "
                "éliminée, à cause d'un signe oublié, fausse immédiatement "
                "tout le reste du calcul."
            )
        ) as tracker:
            self.play(FadeIn(piege))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(piege), FadeOut(titre))
