"""
scenes/Maths_ExtensionNotionLimite_04.py — Chapitre 7 (1ereC, Maths), scène 04.

Limite en un point où le dénominateur s'annule : les deux cas possibles
(numérateur non nul en x₀ → limite infinie avec étude de signe ; numérateur
et dénominateur nuls en x₀ → factorisation par (x - x₀)), exemple résolu
sur (x²-x-2)/(x²-4) en 2.
Source : 1ereC/Maths.pdf, chapitre 7, pages 80-90.
"""

import textwrap

from manim import DOWN, UP, FadeIn, FadeOut, MathTex, Text, VGroup, Write, YELLOW

from shapes.base_scene import NotionScene
from shapes.boxes import essentiel_box, example_box, method_box, scene_title, warning_box


def _wrap(text: str, width: int = 58) -> str:
    return "\n".join(textwrap.fill(line, width=width) for line in text.split("\n"))


class LimitePointAnnulationDenominateur(NotionScene):
    def construct(self):
        titre = scene_title("Limite en un point où le dénominateur s'annule")
        titre.scale(0.48)
        titre.to_edge(UP)

        # --- Énoncé --------------------------------------------------------
        enonce = Text(
            "f(x) = P(x)/Q(x), avec Q(x₀) = 0 : que se passe-t-il en x₀ ?",
            font_size=24,
            color=YELLOW,
            weight="BOLD",
        )
        enonce.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Soit f de x le quotient de deux polynômes P et Q, avec Q "
                "de x zéro qui s'annule. Que peut-on dire de la limite de f "
                "en x zéro ? Il faut distinguer deux cas, selon que le "
                "numérateur s'annule lui aussi ou non."
            )
        ) as tracker:
            self.play(Write(titre))
            self.play(FadeIn(enonce))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(enonce))

        # --- Animation du raisonnement : cas 1 -------------------------------
        cas1 = method_box(
            VGroup(
                Text("Cas 1 : P(x₀) ≠ 0", font_size=23, weight="BOLD"),
                Text(
                    _wrap(
                        "Le numérateur tend vers une constante non nulle, le "
                        "dénominateur tend vers 0 : la limite est infinie. "
                        "On détermine le signe du dénominateur au voisinage "
                        "de x₀ (à gauche et à droite) avec un tableau de "
                        "signes pour conclure sur le signe de la limite.",
                        width=54,
                    ),
                    font_size=21,
                ),
            ).arrange(DOWN, buff=0.3),
            box_width=10.8,
        )
        cas1.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Premier cas : le numérateur P de x zéro est différent de "
                "zéro. Le numérateur tend alors vers une constante non "
                "nulle, tandis que le dénominateur tend vers zéro : la "
                "limite est donc infinie. Pour connaître son signe, on "
                "dresse un tableau de signes du dénominateur au voisinage "
                "de x zéro, à gauche et à droite, exactement comme pour un "
                "sur x en zéro."
            )
        ) as tracker:
            self.play(FadeIn(cas1))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(cas1))

        cas2 = method_box(
            VGroup(
                Text("Cas 2 : P(x₀) = 0 (forme 0/0)", font_size=23, weight="BOLD"),
                Text(
                    _wrap(
                        "x₀ est racine à la fois de P et de Q : on factorise "
                        "chacun par (x - x₀), on simplifie cette forme "
                        "indéterminée, puis on calcule la limite de "
                        "l'expression simplifiée en x₀.",
                        width=54,
                    ),
                    font_size=21,
                ),
                MathTex(
                    r"\dfrac{P(x)}{Q(x)} = \dfrac{(x-x_0)P_1(x)}{(x-x_0)Q_1(x)}"
                    r" = \dfrac{P_1(x)}{Q_1(x)}",
                    font_size=25,
                ),
            ).arrange(DOWN, buff=0.3),
            box_width=10.8,
        )
        cas2.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Deuxième cas : le numérateur s'annule lui aussi en x zéro, "
                "on obtient la forme indéterminée zéro sur zéro. Dans ce "
                "cas, x zéro est racine à la fois de P et de Q. On factorise "
                "chacun des deux polynômes par x moins x zéro, on simplifie "
                "cette forme commune qui donnait l'indétermination, puis on "
                "calcule la limite de l'expression simplifiée, qui, elle, "
                "ne pose plus de problème en x zéro."
            )
        ) as tracker:
            self.play(FadeIn(cas2))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(cas2))

        # --- Exemple traité 4 ------------------------------------------------
        enonce_ex4 = Text(
            "Exemple 4 — limite en 2 de f(x) = (x² - x - 2)/(x² - 4)",
            font_size=24,
            color=YELLOW,
            weight="BOLD",
        )
        enonce_ex4.next_to(titre, DOWN, buff=0.5)

        fonction_ex4 = MathTex(r"f(x) = \dfrac{x^2-x-2}{x^2-4}", font_size=32)
        fonction_ex4.next_to(enonce_ex4, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Exemple : calculons la limite en deux de f de x égale x "
                "carré moins x moins deux, sur x carré moins quatre."
            )
        ) as tracker:
            self.play(FadeIn(enonce_ex4))
            self.play(Write(fonction_ex4))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(enonce_ex4), FadeOut(fonction_ex4))

        constat_ex4 = example_box(
            MathTex(
                r"""
                \begin{array}{l}
                \text{Numérateur en } 2 : \ 2^2-2-2 = 0 \\
                \text{Dénominateur en } 2 : \ 2^2-4 = 0
                \end{array}
                \qquad \Longrightarrow \qquad \text{forme } \dfrac{0}{0}
                """,
                font_size=27,
            ),
            box_width=11.2,
        )
        constat_ex4.next_to(titre, DOWN, buff=0.55)

        with self.voiceover(
            text=(
                "On constate que le numérateur, comme le dénominateur, "
                "s'annulent tous les deux en deux : on est bien dans le "
                "deuxième cas, la forme indéterminée zéro sur zéro. Il faut "
                "donc factoriser par x moins deux."
            )
        ) as tracker:
            self.play(FadeIn(constat_ex4))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(constat_ex4))

        factorisation_ex4 = example_box(
            MathTex(
                r"""
                \begin{array}{l}
                x^2-x-2 = (x-2)(x+1) \\
                x^2-4 = (x-2)(x+2)
                \end{array}
                """,
                font_size=28,
            ),
            box_width=8.5,
        )
        factorisation_ex4.next_to(titre, DOWN, buff=0.55)

        with self.voiceover(
            text=(
                "On factorise : x carré moins x moins deux se factorise en "
                "x moins deux, fois x plus un. Et x carré moins quatre, "
                "identité remarquable, se factorise en x moins deux, fois x "
                "plus deux."
            )
        ) as tracker:
            self.play(FadeIn(factorisation_ex4))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(factorisation_ex4))

        resultat_ex4 = example_box(
            MathTex(
                r"""
                f(x) = \dfrac{(x-2)(x+1)}{(x-2)(x+2)} = \dfrac{x+1}{x+2}
                \quad \Longrightarrow \quad
                \lim_{x\to 2} f(x) = \dfrac{2+1}{2+2} = \dfrac{3}{4}
                """,
                font_size=27,
            ),
            box_width=11.4,
        )
        resultat_ex4.next_to(titre, DOWN, buff=0.55)

        with self.voiceover(
            text=(
                "En simplifiant par x moins deux, f de x devient x plus un "
                "sur x plus deux, expression qui ne pose plus aucun "
                "problème en deux. La limite de f en deux vaut donc trois "
                "sur quatre."
            )
        ) as tracker:
            self.play(FadeIn(resultat_ex4))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(resultat_ex4))

        # --- À retenir -----------------------------------------------------
        retenir = essentiel_box(
            Text(
                _wrap(
                    "Si Q(x₀)=0 : regarder d'abord P(x₀). Non nul → limite "
                    "infinie (signe par tableau). Nul → factoriser P et Q "
                    "par (x - x₀), simplifier, puis recalculer la limite.",
                    width=58,
                ),
                font_size=23,
            )
        )
        retenir.next_to(titre, DOWN, buff=0.6)

        with self.voiceover(
            text=(
                "À retenir : dès que le dénominateur s'annule en x zéro, on "
                "commence toujours par regarder la valeur du numérateur en "
                "x zéro. Si elle est non nulle, la limite est infinie, avec "
                "un signe à déterminer par un tableau. Si elle est nulle "
                "aussi, on factorise numérateur et dénominateur par x moins "
                "x zéro, on simplifie, et on recalcule la limite."
            )
        ) as tracker:
            self.play(FadeIn(retenir))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(retenir))

        # --- Piège à éviter --------------------------------------------------
        piege = warning_box(
            Text(
                _wrap(
                    "Piège : simplifier par (x - x₀) ne change f(x) que là "
                    "où x ≠ x₀. La fonction simplifiée sert seulement à "
                    "calculer la limite, pas à redéfinir f en x₀.",
                    width=58,
                ),
                font_size=23,
            )
        )
        piege.next_to(titre, DOWN, buff=0.6)

        with self.voiceover(
            text=(
                "Attention : simplifier par x moins x zéro n'est légitime "
                "que là où x est différent de x zéro. L'expression "
                "simplifiée sert uniquement à calculer la limite ; elle ne "
                "redéfinit pas la valeur de f en x zéro, qui reste souvent "
                "non définie."
            )
        ) as tracker:
            self.play(FadeIn(piege))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(titre), FadeOut(piege))
