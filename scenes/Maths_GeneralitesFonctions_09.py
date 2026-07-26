"""
scenes/Maths_GeneralitesFonctions_09.py — Chapitre 3 (1ereC, Maths), scène 09.

Bijection et fonction réciproque (théorie) : injection, surjection,
bijection, existence et unicité de la fonction réciproque, condition
suffisante de bijection (stricte monotonie).
Source : 1ereC/Maths.pdf, chapitre 3, pages 28-40.
"""

import textwrap

from manim import DOWN, LEFT, RIGHT, UP, WHITE, YELLOW, FadeIn, FadeOut, MathTex, Text, VGroup, Write

from shapes.base_scene import NotionScene
from shapes.boxes import definition_box, essentiel_box, example_box, scene_title, theorem_box, warning_box


def _wrap(text: str, width: int = 60) -> str:
    return "\n".join(textwrap.fill(line, width=width) for line in text.split("\n"))


class BijectionFonctionReciproqueTheorie(NotionScene):
    def construct(self):
        titre = scene_title("Bijection et fonction réciproque")
        titre.scale(0.6)
        titre.to_edge(UP)
        self.play(Write(titre))

        # --- Énoncé : injection, surjection, bijection -----------------------
        def_injection = definition_box(
            MathTex(
                r"""
                \begin{array}{l}
                f \text{ injective sur } D_f : \ \forall a,b \in D_f,\ f(a)=f(b) \ \Longrightarrow \ a=b \\
                f \text{ surjective de } D_f \text{ sur } F : \ \forall y \in F,\ \exists x \in D_f,\ f(x)=y \\
                f \text{ bijective de } D_f \text{ sur } F : \ f \text{ injective et surjective sur } F
                \end{array}
                """,
                font_size=22,
            ),
            box_width=11.4,
        )
        def_injection.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "f est injective sur Df si deux réels distincts ont "
                "toujours des images distinctes : f de a égale f de b "
                "entraîne a égale b. f est surjective de Df sur F si tout "
                "élément y de F possède au moins un antécédent x dans Df. "
                "Et f est bijective de Df sur F si elle est à la fois "
                "injective et surjective : tout élément de F a alors "
                "exactement un antécédent."
            )
        ) as tracker:
            self.play(FadeIn(def_injection))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(def_injection))

        exemples = example_box(
            Text(
                _wrap(
                    "Exemples : f(x) = x² n'est pas injective sur ℝ "
                    "(f(−2)=f(2)=4), mais elle est bijective de [0;+∞[ "
                    "sur [0;+∞[. f(x) = 2x + 1 est bijective de ℝ sur ℝ.",
                    width=56,
                ),
                font_size=23,
            ),
            box_width=10.8,
        )
        exemples.next_to(titre, DOWN, buff=0.55)

        with self.voiceover(
            text=(
                "Exemples : la fonction x carré n'est pas injective sur ℝ "
                "tout entier, puisque moins deux et deux ont la même "
                "image, quatre. En revanche, elle est bijective de zéro, "
                "plus l'infini, sur zéro, plus l'infini. La fonction deux "
                "x plus un, elle, est bijective de ℝ sur ℝ."
            )
        ) as tracker:
            self.play(FadeIn(exemples))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(exemples))

        # --- Animation du raisonnement : fonction réciproque ------------------
        theo_reciproque = theorem_box(
            Text(
                _wrap(
                    "Si f est une bijection de Df sur F, alors il existe "
                    "une unique fonction, notée f⁻¹, définie sur F, telle "
                    "que : pour tout x de Df, f⁻¹(f(x)) = x, et pour tout "
                    "y de F, f(f⁻¹(y)) = y.",
                    width=56,
                ),
                font_size=23,
            ),
            box_width=10.8,
        )
        theo_reciproque.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Théorème central : si f est une bijection de Df sur F, "
                "alors il existe une unique fonction, appelée fonction "
                "réciproque et notée f exposant moins un, définie sur F, "
                "telle que f moins un de f de x redonne x, et f de f "
                "moins un de y redonne y."
            )
        ) as tracker:
            self.play(FadeIn(theo_reciproque))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(theo_reciproque))

        demo_reciproque = example_box(
            Text(
                _wrap(
                    "Démonstration (construction) : f bijective ⟹ tout "
                    "y de F a EXACTEMENT un antécédent x dans Df. On "
                    "définit alors f⁻¹(y) = cet unique x. Cette "
                    "construction associe à chaque y un unique antécédent, "
                    "ce qui définit une fonction — et une seule.",
                    width=58,
                ),
                font_size=22,
            ),
            box_width=11.2,
        )
        demo_reciproque.next_to(titre, DOWN, buff=0.55)

        with self.voiceover(
            text=(
                "Démonstration par construction : puisque f est "
                "bijective, tout y de F possède exactement un antécédent x "
                "dans Df — ni zéro, ni plusieurs. On définit alors f moins "
                "un de y comme étant cet unique antécédent x. Cette "
                "construction associe à chaque y une unique valeur, ce qui "
                "définit bien une fonction, et une seule : c'est "
                "l'existence et l'unicité de f moins un."
            )
        ) as tracker:
            self.play(FadeIn(demo_reciproque))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(demo_reciproque))

        # --- Exemple traité : condition suffisante de bijection --------------
        theo_monotonie = theorem_box(
            Text(
                _wrap(
                    "Condition suffisante de bijection : si f est "
                    "strictement monotone (strictement croissante ou "
                    "strictement décroissante) sur un intervalle I, alors "
                    "f réalise une bijection de I sur f(I).",
                    width=56,
                ),
                font_size=23,
            ),
            box_width=10.8,
        )
        theo_monotonie.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "En pratique, comment prouver qu'une fonction est "
                "bijective ? Théorème très utile : si f est strictement "
                "monotone sur un intervalle I — strictement croissante ou "
                "strictement décroissante — alors f réalise une bijection "
                "de I sur son image f de I. C'est le résultat le plus "
                "employé pour démontrer une bijection en pratique."
            )
        ) as tracker:
            self.play(FadeIn(theo_monotonie))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(theo_monotonie))

        # --- À retenir ---------------------------------------------------
        retenir = essentiel_box(
            Text(
                _wrap(
                    "Une bijection a une unique fonction réciproque f⁻¹. "
                    "En pratique, la stricte monotonie sur un intervalle "
                    "suffit à garantir la bijection.",
                    width=56,
                ),
                font_size=24,
            ),
            box_width=10.8,
        )
        retenir.next_to(titre, DOWN, buff=0.6)

        with self.voiceover(
            text=(
                "À retenir : une bijection possède une unique fonction "
                "réciproque, notée f moins un. En pratique, il suffit de "
                "montrer que f est strictement monotone sur un intervalle "
                "pour garantir qu'elle y est bijective."
            )
        ) as tracker:
            self.play(FadeIn(retenir))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(retenir))

        # --- Piège à éviter ----------------------------------------------
        piege = warning_box(
            Text(
                _wrap(
                    "Piège : f⁻¹ n'existe que si f est bijective. Ne "
                    "jamais confondre f⁻¹(x), la fonction réciproque, avec "
                    "1/f(x), l'inverse — ce sont deux notations qui se "
                    "ressemblent mais désignent des objets différents.",
                    width=56,
                ),
                font_size=22,
            ),
            box_width=11.0,
        )
        piege.next_to(titre, DOWN, buff=0.6)

        with self.voiceover(
            text=(
                "Attention, piège fréquent : f moins un n'existe que si f "
                "est bijective. Et il ne faut surtout jamais confondre f "
                "moins un de x, la fonction réciproque, avec un sur f de "
                "x, l'inverse — deux notations qui se ressemblent "
                "beaucoup, mais qui désignent des objets totalement "
                "différents."
            )
        ) as tracker:
            self.play(FadeIn(piege))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(titre), FadeOut(piege))
