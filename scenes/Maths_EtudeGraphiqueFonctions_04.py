"""
scenes/Maths_EtudeGraphiqueFonctions_04.py — Chapitre 11 (1ereC, Maths), scène 04.

Dérivée et sens de variation, tableau de variation (exemple f(x)=x³-3x),
points remarquables (intersections axes, extremums, tangentes) et
théorèmes de centre / axe de symétrie.
Source : 1ereC/Maths.pdf, chapitre 11, pages 130-141.
"""

import textwrap

from manim import DOWN, LEFT, RIGHT, UP, WHITE, YELLOW, FadeIn, FadeOut, MathTex, Text, VGroup, Write

from shapes.base_scene import NotionScene
from shapes.boxes import essentiel_box, example_box, scene_title, theorem_box, warning_box


def _wrap(text: str, width: int = 58) -> str:
    return "\n".join(textwrap.fill(line, width=width) for line in text.split("\n"))


class DeriveeTableauVariationSymetries(NotionScene):
    def construct(self):
        titre = scene_title("Dérivée, tableau de variation, points remarquables")
        titre.scale(0.42)
        titre.to_edge(UP)

        # --- Énoncé ------------------------------------------------------------
        enonce = Text(
            "Étapes 5, 6 et 7 : dérivée, tableau, points remarquables",
            font_size=24,
            color=YELLOW,
            weight="BOLD",
        )
        enonce.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Les dernières étapes du plan d'étude reposent toutes sur "
                "la dérivée : son signe donne le sens de variation, qui se "
                "résume dans un tableau, avant de placer les points "
                "remarquables pour tracer la courbe."
            )
        ) as tracker:
            self.play(Write(titre))
            self.play(FadeIn(enonce))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(enonce))

        # --- Théorème lien dérivée / sens de variation --------------------------
        theo_signe = theorem_box(
            MathTex(
                r"""
                \begin{array}{lll}
                f'(x) > 0 \text{ sur } I & \Longrightarrow & f \text{ strictement croissante sur } I \\
                f'(x) < 0 \text{ sur } I & \Longrightarrow & f \text{ strictement décroissante sur } I \\
                f'(x) = 0 \text{ sur } I & \Longrightarrow & f \text{ constante sur } I
                \end{array}
                """,
                font_size=26,
            ),
            box_width=10.6,
        )
        theo_signe.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Théorème fondamental : si f prime de x est strictement "
                "positive sur un intervalle I, alors f est strictement "
                "croissante sur I. Si f prime est strictement négative, f "
                "est strictement décroissante. Et si f prime est "
                "identiquement nulle sur I, f est constante sur I."
            )
        ) as tracker:
            self.play(FadeIn(theo_signe))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(theo_signe))

        # --- Exemple : tableau de variation de f(x) = x³ - 3x -------------------
        enonce_ex1 = Text(
            "Exemple — tableau de variation de f(x) = x³ - 3x",
            font_size=25,
            color=YELLOW,
            weight="BOLD",
        )
        enonce_ex1.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Exemple : dressons le tableau de variation de f de x égale "
                "x au cube moins trois x, définie sur ℝ."
            )
        ) as tracker:
            self.play(FadeIn(enonce_ex1))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(enonce_ex1))

        derivee_ex1 = example_box(
            MathTex(
                r"""
                f'(x) = 3x^2-3 = 3(x-1)(x+1)
                \ \Longrightarrow \
                f'(x) > 0 \ \Longleftrightarrow \ x<-1 \text{ ou } x>1
                """,
                font_size=27,
            ),
            box_width=11.2,
        )
        derivee_ex1.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "La dérivée vaut trois x carré moins trois, qui se "
                "factorise en trois fois x moins un, fois x plus un. Cette "
                "dérivée est positive quand x est inférieur à moins un ou "
                "supérieur à un, et négative entre les deux."
            )
        ) as tracker:
            self.play(FadeIn(derivee_ex1))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(derivee_ex1))

        tableau_ex1 = MathTex(
            r"""
            \begin{array}{c|ccccccc}
            x & -\infty & & -1 & & 1 & & +\infty \\
            \hline
            f'(x) & & + & 0 & - & 0 & + & \\
            \hline
            f(x) & -\infty & \nearrow & 2 & \searrow & -2 & \nearrow & +\infty
            \end{array}
            """,
            font_size=24,
        )
        tableau_ex1.next_to(titre, DOWN, buff=0.6)

        with self.voiceover(
            text=(
                "Voici le tableau de variation : f est croissante de moins "
                "l'infini à moins un, où elle atteint un maximum local de "
                "deux. Elle décroît ensuite jusqu'en un, où elle atteint un "
                "minimum local de moins deux. Puis elle recroît jusqu'à "
                "plus l'infini."
            )
        ) as tracker:
            self.play(FadeIn(tableau_ex1))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(tableau_ex1))

        # --- Points remarquables et tangente -------------------------------
        points_remarquables = example_box(
            VGroup(
                Text(
                    "Points remarquables à placer sur la courbe :",
                    font_size=22,
                    weight="BOLD",
                ),
                Text(
                    "intersections avec (Ox) et (Oy), extremums locaux, "
                    "tangente en un point remarquable.",
                    font_size=21,
                ),
                MathTex(
                    r"\text{Tangente en } a : \ y = f'(a)(x-a) + f(a)",
                    font_size=27,
                ),
            ).arrange(DOWN, buff=0.28),
            box_width=10.8,
        )
        points_remarquables.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Avant de tracer, on place quelques points remarquables : "
                "les intersections avec l'axe des abscisses et l'axe des "
                "ordonnées, les extremums locaux déjà lus dans le tableau, "
                "et parfois la tangente en un point précis, d'équation y "
                "égale f prime de a, fois x moins a, plus f de a."
            )
        ) as tracker:
            self.play(FadeIn(points_remarquables))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(points_remarquables))

        # --- Théorèmes centre / axe de symétrie -----------------------------
        theo_centre = theorem_box(
            MathTex(
                r"""
                \begin{array}{c}
                \Omega(\alpha\,;\beta) \text{ centre de symétrie de } C_f \\
                \Longleftrightarrow \ f(\alpha+x)+f(\alpha-x) = 2\beta \ \ \forall x
                \end{array}
                """,
                font_size=27,
            ),
            box_width=9.8,
        )
        theo_centre.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Deux théorèmes utiles pour repérer une symétrie. Le point "
                "oméga de coordonnées alpha et bêta est centre de symétrie "
                "de la courbe si et seulement si f de alpha plus x, plus f "
                "de alpha moins x, est constamment égal à deux bêta, quel "
                "que soit x."
            )
        ) as tracker:
            self.play(FadeIn(theo_centre))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(theo_centre))

        theo_axe = theorem_box(
            MathTex(
                r"""
                \begin{array}{c}
                x=\alpha \text{ axe de symétrie de } C_f \\
                \Longleftrightarrow \ f(\alpha+x) = f(\alpha-x) \ \ \forall x
                \end{array}
                """,
                font_size=27,
            ),
            box_width=9.0,
        )
        theo_axe.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "De même, la droite d'équation x égale alpha est axe de "
                "symétrie de la courbe si et seulement si f de alpha plus "
                "x est constamment égal à f de alpha moins x, quel que soit "
                "x."
            )
        ) as tracker:
            self.play(FadeIn(theo_axe))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(theo_axe))

        # --- À retenir ---------------------------------------------------------
        retenir = essentiel_box(
            Text(
                _wrap(
                    "f' > 0 → croissante, f' < 0 → décroissante. Tableau de "
                    "variation = résumé du signe de f'. Pour un centre ou "
                    "un axe de symétrie, poser le test f(α+x)±f(α-x) et "
                    "vérifier qu'il est constant.",
                    width=58,
                ),
                font_size=22,
            ),
            box_width=11.2,
        )
        retenir.next_to(titre, DOWN, buff=0.6)

        with self.voiceover(
            text=(
                "À retenir : le signe de f prime pilote entièrement le "
                "sens de variation, résumé dans le tableau. Pour prouver un "
                "centre ou un axe de symétrie, on pose le test f de alpha "
                "plus x, additionné ou soustrait à f de alpha moins x, et "
                "on vérifie qu'il donne bien une constante."
            )
        ) as tracker:
            self.play(FadeIn(retenir))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(retenir))

        # --- Piège à éviter ------------------------------------------------
        piege = warning_box(
            Text(
                _wrap(
                    "Piège : un extremum local nécessite f'(a) = 0 ET un "
                    "changement de signe de f' de part et d'autre de a. "
                    "f'(a) = 0 seul ne suffit pas (ex : f(x) = x³ en 0, pas "
                    "d'extremum).",
                    width=58,
                ),
                font_size=22,
            ),
            box_width=11.0,
        )
        piege.next_to(titre, DOWN, buff=0.6)

        with self.voiceover(
            text=(
                "Piège classique : un extremum local exige que f prime de "
                "a soit nulle ET que f prime change de signe de part et "
                "d'autre de a. La seule condition f prime de a égale zéro "
                "ne suffit pas — pour f de x égale x au cube, la dérivée "
                "s'annule en zéro sans qu'il y ait d'extremum."
            )
        ) as tracker:
            self.play(FadeIn(piege))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(titre), FadeOut(piege))
