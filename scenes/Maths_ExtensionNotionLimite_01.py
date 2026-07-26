"""
scenes/Maths_ExtensionNotionLimite_01.py — Chapitre 7 (1ereC, Maths), scène 01.

Limite à gauche et limite à droite (rappel approfondi) : tableau de valeurs
de 1/x au voisinage de 0, définitions (versions finies et infinies), exemple
résolu sur (3x+1)/(x-2) en 2.
Source : 1ereC/Maths.pdf, chapitre 7, pages 80-90.
"""

import textwrap

from manim import (
    DOWN,
    LEFT,
    RIGHT,
    UP,
    WHITE,
    YELLOW,
    FadeIn,
    FadeOut,
    MathTex,
    Text,
    VGroup,
    Write,
)

from shapes.base_scene import NotionScene
from shapes.boxes import definition_box, essentiel_box, example_box, scene_title, warning_box


def _wrap(text: str, width: int = 58) -> str:
    return "\n".join(textwrap.fill(line, width=width) for line in text.split("\n"))


class LimiteGaucheDroite(NotionScene):
    def construct(self):
        titre = scene_title("Limite à gauche et limite à droite")
        titre.scale(0.5)
        titre.to_edge(UP)

        # --- Énoncé : tableau de valeurs de 1/x au voisinage de 0 ----------
        enonce = Text(
            "Que se passe-t-il pour 1/x quand x s'approche de 0 ?",
            font_size=26,
            color=YELLOW,
            weight="BOLD",
        )
        enonce.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Reprenons une question déjà rencontrée : que se passe-t-il "
                "pour un sur x quand x s'approche de zéro ? La réponse "
                "dépend en fait du côté par lequel on s'approche."
            )
        ) as tracker:
            self.play(Write(titre))
            self.play(FadeIn(enonce))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(enonce))

        tableau_gauche = MathTex(
            r"""
            \begin{array}{c|cccc}
            x & -0{,}1 & -0{,}01 & -0{,}001 & \cdots \\
            \hline
            \dfrac{1}{x} & -10 & -100 & -1000 & \cdots
            \end{array}
            """,
            font_size=26,
        )
        tableau_gauche.shift(LEFT * 3.2 + UP * 1.0)

        tableau_droite = MathTex(
            r"""
            \begin{array}{c|cccc}
            x & 0{,}1 & 0{,}01 & 0{,}001 & \cdots \\
            \hline
            \dfrac{1}{x} & 10 & 100 & 1000 & \cdots
            \end{array}
            """,
            font_size=26,
        )
        tableau_droite.shift(RIGHT * 3.2 + UP * 1.0)

        conclusion_tableaux = MathTex(
            r"""
            \lim_{x \to 0^{-}} \dfrac{1}{x} = -\infty
            \qquad\qquad
            \lim_{x \to 0^{+}} \dfrac{1}{x} = +\infty
            """,
            font_size=30,
        )
        conclusion_tableaux.next_to(titre, DOWN, buff=2.6)

        with self.voiceover(
            text=(
                "Quand x s'approche de zéro par valeurs négatives, un sur x "
                "devient un nombre négatif de plus en plus grand en valeur "
                "absolue : la limite est moins l'infini. Quand x s'approche "
                "de zéro par valeurs positives, un sur x devient un nombre "
                "positif de plus en plus grand : la limite est plus "
                "l'infini. Ces deux comportements différents portent le "
                "nom de limite à gauche et limite à droite."
            )
        ) as tracker:
            self.play(FadeIn(tableau_gauche), FadeIn(tableau_droite))
            self.play(Write(conclusion_tableaux))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(tableau_gauche), FadeOut(tableau_droite), FadeOut(conclusion_tableaux))

        # --- Animation du raisonnement : définitions --------------------------
        def_gauche = definition_box(
            VGroup(
                Text(
                    _wrap(
                        "Soit f définie au voisinage de x₀, sauf peut-être en "
                        "x₀. On dit que f admet L pour limite à gauche en x₀ "
                        "si f(x) se rapproche de L quand x tend vers x₀ en "
                        "restant strictement inférieur à x₀. On note :",
                        width=56,
                    ),
                    font_size=22,
                ),
                MathTex(
                    r"\lim_{x \to x_0^{-}} f(x) = L"
                    r"\qquad \text{ou} \qquad"
                    r"\lim_{x \to x_0^{-}} f(x) = \pm\infty",
                    font_size=26,
                ),
            ).arrange(DOWN, buff=0.3),
            box_width=11.0,
        )
        def_gauche.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Première définition : soit f une fonction définie au "
                "voisinage de x zéro, sauf peut-être en x zéro elle-même. "
                "On dit que f admet L pour limite à gauche en x zéro si f "
                "de x se rapproche de L quand x tend vers x zéro en restant "
                "strictement inférieur à x zéro. On note limite, x tend vers "
                "x zéro par valeurs inférieures, de f de x, égale L — cette "
                "limite pouvant aussi être infinie."
            )
        ) as tracker:
            self.play(FadeIn(def_gauche))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(def_gauche))

        def_droite = definition_box(
            VGroup(
                Text(
                    _wrap(
                        "De même, f admet L pour limite à droite en x₀ si "
                        "f(x) se rapproche de L quand x tend vers x₀ en "
                        "restant strictement supérieur à x₀. On note :",
                        width=56,
                    ),
                    font_size=22,
                ),
                MathTex(
                    r"\lim_{x \to x_0^{+}} f(x) = L"
                    r"\qquad \text{ou} \qquad"
                    r"\lim_{x \to x_0^{+}} f(x) = \pm\infty",
                    font_size=26,
                ),
            ).arrange(DOWN, buff=0.3),
            box_width=11.0,
        )
        def_droite.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "De la même façon, f admet L pour limite à droite en x zéro "
                "si f de x se rapproche de L quand x tend vers x zéro en "
                "restant strictement supérieur à x zéro. On note limite, x "
                "tend vers x zéro par valeurs supérieures, de f de x, égale "
                "L, avec là encore une version possible en plus l'infini ou "
                "moins l'infini."
            )
        ) as tracker:
            self.play(FadeIn(def_droite))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(def_droite))

        # --- Exemple traité 1 : (3x+1)/(x-2) en 2 -----------------------------
        enonce_ex1 = Text(
            "Exemple 1 — limites à gauche et à droite en 2 de f(x) = (3x+1)/(x-2)",
            font_size=23,
            color=YELLOW,
            weight="BOLD",
        )
        enonce_ex1.next_to(titre, DOWN, buff=0.45)

        fonction_ex1 = MathTex(r"f(x) = \dfrac{3x+1}{x-2}", font_size=32)
        fonction_ex1.next_to(enonce_ex1, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Exemple : étudions les limites à gauche et à droite en deux "
                "de f de x égale trois x plus un, sur x moins deux."
            )
        ) as tracker:
            self.play(FadeIn(enonce_ex1))
            self.play(Write(fonction_ex1))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(enonce_ex1), FadeOut(fonction_ex1))

        analyse_ex1 = example_box(
            MathTex(
                r"""
                \begin{array}{l}
                \text{Numérateur : } 3x+1 \to 7 \text{ quand } x \to 2 \\
                \text{Si } x \to 2^{-} : \ x-2 \to 0^{-} \\
                \text{Si } x \to 2^{+} : \ x-2 \to 0^{+}
                \end{array}
                """,
                font_size=27,
            ),
            box_width=9.5,
        )
        analyse_ex1.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Le numérateur, trois x plus un, tend vers sept quand x "
                "tend vers deux. Le dénominateur, x moins deux, tend vers "
                "zéro par valeurs négatives si x s'approche de deux par la "
                "gauche, et vers zéro par valeurs positives si x s'approche "
                "de deux par la droite."
            )
        ) as tracker:
            self.play(FadeIn(analyse_ex1))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(analyse_ex1))

        resultat_ex1 = example_box(
            MathTex(
                r"""
                \lim_{x \to 2^{-}} f(x) = \dfrac{7}{0^{-}} = -\infty
                \qquad\qquad
                \lim_{x \to 2^{+}} f(x) = \dfrac{7}{0^{+}} = +\infty
                """,
                font_size=28,
            ),
            box_width=11.3,
        )
        resultat_ex1.next_to(titre, DOWN, buff=0.6)

        with self.voiceover(
            text=(
                "On obtient donc : la limite de f en deux par valeurs "
                "inférieures vaut sept sur zéro moins, soit moins l'infini. "
                "Et la limite de f en deux par valeurs supérieures vaut "
                "sept sur zéro plus, soit plus l'infini. Les deux limites "
                "latérales sont différentes."
            )
        ) as tracker:
            self.play(FadeIn(resultat_ex1))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(resultat_ex1))

        # --- À retenir ---------------------------------------------------------
        retenir = essentiel_box(
            Text(
                _wrap(
                    "Limite à gauche : x → x₀ en restant < x₀. Limite à "
                    "droite : x → x₀ en restant > x₀. Chacune peut être "
                    "finie ou infinie, exactement comme une limite classique.",
                    width=58,
                ),
                font_size=24,
            )
        )
        retenir.next_to(titre, DOWN, buff=0.6)

        with self.voiceover(
            text=(
                "À retenir : la limite à gauche impose de rester en dessous "
                "de x zéro, la limite à droite impose de rester au-dessus. "
                "L'une comme l'autre peut parfaitement être infinie, comme "
                "n'importe quelle limite déjà étudiée."
            )
        ) as tracker:
            self.play(FadeIn(retenir))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(retenir))

        # --- Piège à éviter ------------------------------------------------
        piege = warning_box(
            Text(
                _wrap(
                    "Piège : x → x₀⁻ ne signifie pas « x négatif », mais "
                    "« x inférieur à x₀ », même si x₀ est négatif ou nul. "
                    "Toujours raisonner par rapport à x₀, pas par rapport à 0.",
                    width=58,
                ),
                font_size=24,
            )
        )
        piege.next_to(titre, DOWN, buff=0.6)

        with self.voiceover(
            text=(
                "Attention au piège classique : x tend vers x zéro par "
                "valeurs inférieures ne veut pas dire que x est négatif, "
                "mais bien que x reste inférieur à x zéro, même si x zéro "
                "lui-même est négatif ou nul. Il faut toujours raisonner "
                "par rapport à x zéro, pas par rapport à zéro."
            )
        ) as tracker:
            self.play(FadeIn(piege))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(titre), FadeOut(piege))
