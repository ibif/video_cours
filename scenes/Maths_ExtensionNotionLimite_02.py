"""
scenes/Maths_ExtensionNotionLimite_02.py — Chapitre 7 (1ereC, Maths), scène 02.

Lien entre limite et limites latérales : théorème d'équivalence (admis),
conséquence pratique, exemple résolu sur une fonction définie par morceaux
qui n'a pas de limite en 1.
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
    Axes,
    Dot,
    FadeIn,
    FadeOut,
    MathTex,
    Text,
    VGroup,
    Write,
)

from shapes.base_scene import NotionScene
from shapes.boxes import essentiel_box, example_box, scene_title, theorem_box, warning_box


def _wrap(text: str, width: int = 58) -> str:
    return "\n".join(textwrap.fill(line, width=width) for line in text.split("\n"))


class LienLimiteLimitesLaterales(NotionScene):
    def construct(self):
        titre = scene_title("Limite et limites latérales")
        titre.scale(0.5)
        titre.to_edge(UP)

        # --- Énoncé -----------------------------------------------------------
        enonce = Text(
            "Quel lien entre la limite en x₀ et les limites latérales ?",
            font_size=26,
            color=YELLOW,
            weight="BOLD",
        )
        enonce.next_to(titre, DOWN, buff=0.6)

        with self.voiceover(
            text=(
                "Nous venons de définir la limite à gauche et la limite à "
                "droite. Il reste une question essentielle : quel lien "
                "existe-t-il entre ces limites latérales et la limite "
                "« classique » de f en x zéro ?"
            )
        ) as tracker:
            self.play(Write(titre))
            self.play(FadeIn(enonce))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(enonce))

        # --- Animation du raisonnement : théorème d'équivalence ---------------
        theoreme = theorem_box(
            VGroup(
                Text(
                    _wrap(
                        "Soit f définie au voisinage de x₀, sauf peut-être en "
                        "x₀. f admet une limite L en x₀ si, et seulement si, "
                        "f admet une limite à gauche et une limite à droite "
                        "en x₀, et que ces deux limites sont égales à L :",
                        width=56,
                    ),
                    font_size=22,
                ),
                MathTex(
                    r"\lim_{x \to x_0} f(x) = L"
                    r"\ \Longleftrightarrow\ "
                    r"\lim_{x \to x_0^{-}} f(x) = \lim_{x \to x_0^{+}} f(x) = L",
                    font_size=26,
                ),
                Text("(résultat admis)", font_size=18, slant="ITALIC"),
            ).arrange(DOWN, buff=0.3),
            box_width=11.3,
        )
        theoreme.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Voici le théorème, admis, qui répond à cette question : f "
                "admet une limite L en x zéro si, et seulement si, f admet "
                "à la fois une limite à gauche et une limite à droite en x "
                "zéro, et que ces deux limites latérales sont égales, et "
                "valent toutes les deux L."
            )
        ) as tracker:
            self.play(FadeIn(theoreme))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(theoreme))

        consequence = theorem_box(
            Text(
                _wrap(
                    "Conséquence pratique : pour prouver qu'une fonction "
                    "n'a PAS de limite en x₀, il suffit de montrer que ses "
                    "limites à gauche et à droite existent mais diffèrent "
                    "— ou que l'une des deux n'existe pas.",
                    width=56,
                ),
                font_size=23,
            ),
            box_width=11.0,
        )
        consequence.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Conséquence pratique très utile : pour démontrer qu'une "
                "fonction n'a pas de limite en x zéro, il suffit de montrer "
                "que sa limite à gauche et sa limite à droite existent mais "
                "sont différentes — ou que l'une des deux n'existe même "
                "pas. C'est exactement l'outil qu'il nous fallait pour les "
                "fonctions définies par morceaux."
            )
        ) as tracker:
            self.play(FadeIn(consequence))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(consequence))

        # --- Exemple traité 2 : fonction par morceaux --------------------------
        enonce_ex2 = Text(
            "Exemple 2 — f a-t-elle une limite en x₀ = 1 ?",
            font_size=25,
            color=YELLOW,
            weight="BOLD",
        )
        enonce_ex2.next_to(titre, DOWN, buff=0.45)

        fonction_ex2 = MathTex(
            r"""
            f(x) =
            \left\{
            \begin{array}{ll}
            x^2+1 & \text{si } x \leq 1 \\
            {} 4-x & \text{si } x > 1
            \end{array}
            \right.
            """,
            font_size=30,
        )
        fonction_ex2.next_to(enonce_ex2, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Exemple : soit f définie par morceaux, égale à x carré "
                "plus un si x est inférieur ou égal à un, et égale à quatre "
                "moins x si x est strictement supérieur à un. La fonction "
                "f admet-elle une limite en x zéro égale à un ?"
            )
        ) as tracker:
            self.play(FadeIn(enonce_ex2))
            self.play(Write(fonction_ex2))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(enonce_ex2), FadeOut(fonction_ex2))

        calcul_ex2 = example_box(
            MathTex(
                r"""
                \begin{array}{l}
                \text{Pour } x \leq 1 : f(x) = x^2+1
                \ \Longrightarrow\
                \lim_{x \to 1^{-}} f(x) = 1^2+1 = 2 \\[0.25cm]
                \text{Pour } x > 1 : f(x) = 4-x
                \ \Longrightarrow\
                \lim_{x \to 1^{+}} f(x) = 4-1 = 3
                \end{array}
                """,
                font_size=27,
            ),
            box_width=11.4,
        )
        calcul_ex2.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Sur l'intervalle où x est inférieur ou égal à un, f de x "
                "vaut x carré plus un, donc la limite à gauche en un vaut "
                "un au carré plus un, c'est-à-dire deux. Sur l'intervalle "
                "où x est strictement supérieur à un, f de x vaut quatre "
                "moins x, donc la limite à droite en un vaut quatre moins "
                "un, c'est-à-dire trois."
            )
        ) as tracker:
            self.play(FadeIn(calcul_ex2))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(calcul_ex2))

        # Figure : saut de la courbe en x = 1
        axes = Axes(
            x_range=[-1, 3, 1],
            y_range=[-1, 4, 1],
            x_length=5.5,
            y_length=3.8,
            axis_config={"color": WHITE, "font_size": 18},
        )
        axes.next_to(titre, DOWN, buff=0.5)
        branche_gauche = axes.plot(lambda x: x**2 + 1, x_range=[-1, 1], color=YELLOW)
        branche_droite = axes.plot(lambda x: 4 - x, x_range=[1, 3], color=YELLOW)
        point_plein = Dot(axes.c2p(1, 2), color=YELLOW, radius=0.07)
        point_vide = Dot(axes.c2p(1, 3), color=YELLOW, radius=0.07, fill_opacity=0)
        point_vide.set_stroke(color=YELLOW, width=2)
        figure = VGroup(axes, branche_gauche, branche_droite, point_plein, point_vide)

        conclusion_ex2 = MathTex(
            r"\lim_{x \to 1^{-}} f(x) = 2 \ \neq\ 3 = \lim_{x \to 1^{+}} f(x)"
            r"\ \Longrightarrow\ f \text{ n'a pas de limite en } 1",
            font_size=24,
        )
        conclusion_ex2.next_to(figure, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "On observe sur la figure un véritable saut de la courbe en "
                "x égale un : la limite à gauche vaut deux, la limite à "
                "droite vaut trois. Comme deux est différent de trois, le "
                "théorème nous dit que f n'admet pas de limite en un."
            )
        ) as tracker:
            self.play(FadeIn(figure))
            self.play(Write(conclusion_ex2))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(figure), FadeOut(conclusion_ex2))

        # --- À retenir -----------------------------------------------------
        retenir = essentiel_box(
            Text(
                _wrap(
                    "Une fonction a une limite en x₀ si et seulement si ses "
                    "limites à gauche et à droite existent et sont égales. "
                    "Utile pour les fonctions définies par morceaux.",
                    width=58,
                ),
                font_size=24,
            )
        )
        retenir.next_to(titre, DOWN, buff=0.6)

        with self.voiceover(
            text=(
                "À retenir : une fonction admet une limite en x zéro si, et "
                "seulement si, ses limites à gauche et à droite existent et "
                "coïncident. C'est l'outil de référence pour étudier les "
                "fonctions définies par morceaux au raccord de deux "
                "expressions."
            )
        ) as tracker:
            self.play(FadeIn(retenir))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(retenir))

        # --- Piège à éviter --------------------------------------------------
        piege = warning_box(
            Text(
                _wrap(
                    "Piège : ne calculer qu'une seule des deux limites "
                    "latérales ne suffit jamais à conclure sur l'existence "
                    "d'une limite globale — il faut toujours les deux.",
                    width=58,
                ),
                font_size=24,
            )
        )
        piege.next_to(titre, DOWN, buff=0.6)

        with self.voiceover(
            text=(
                "Attention : se contenter de calculer une seule des deux "
                "limites latérales ne permet jamais de conclure sur "
                "l'existence d'une limite globale en x zéro. Il faut "
                "systématiquement examiner les deux côtés."
            )
        ) as tracker:
            self.play(FadeIn(piege))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(titre), FadeOut(piege))
