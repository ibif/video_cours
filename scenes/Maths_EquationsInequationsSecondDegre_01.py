"""
scenes/Maths_EquationsInequationsSecondDegre_01.py — Chapitre 1 (1ereC,
Maths), scène 01.

Définition de l'équation du second degré et du trinôme, définition du
discriminant Δ, forme canonique du trinôme avec démonstration complète.
Source : 1ereC/Maths.pdf, chapitre 1, pages 4-13.
"""

from manim import DOWN, UP, FadeIn, FadeOut, MathTex, Text, VGroup, Write, YELLOW

from shapes.base_scene import NotionScene
from shapes.boxes import definition_box, scene_title, theorem_box


class DefinitionDiscriminantFormeCanonique(NotionScene):
    def construct(self):
        titre = scene_title("Équation du second degré — définitions")
        titre.scale(0.65)
        titre.to_edge(UP)

        # --- Énoncé : définition de l'équation du second degré -------------
        def_eq = VGroup(
            MathTex(r"ax^2 + bx + c = 0", font_size=36),
            MathTex(r"\text{avec } a, b, c \in \mathbb{R} \text{ et } a \neq 0", font_size=30),
        ).arrange(DOWN, buff=0.35)
        def_eq_box = definition_box(def_eq)
        def_eq_box.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Une équation du second degré, dans l'ensemble des nombres "
                "réels, est une équation qui peut s'écrire sous la forme "
                "a x carré plus b x plus c égale zéro, où a, b et c sont "
                "des nombres réels, et où a est différent de zéro. "
                "L'expression a x carré plus b x plus c s'appelle un "
                "trinôme du second degré."
            )
        ) as tracker:
            self.play(Write(titre))
            self.play(FadeIn(def_eq_box))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(def_eq_box))

        # --- Animation du raisonnement : le discriminant --------------------
        def_delta = VGroup(
            MathTex(r"\Delta = b^2 - 4ac", font_size=38),
            Text("Δ se lit « discriminant » du trinôme.", font_size=26),
        ).arrange(DOWN, buff=0.35)
        def_delta_box = definition_box(def_delta)
        def_delta_box.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "On appelle discriminant du trinôme le nombre réel delta, "
                "égal à b carré moins quatre a c. Ce nombre va nous "
                "permettre, dans les scènes suivantes, de savoir combien "
                "de solutions possède l'équation."
            )
        ) as tracker:
            self.play(FadeIn(def_delta_box))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(def_delta_box))

        # --- Exemple traité : forme canonique et sa démonstration -----------
        enonce_theoreme = MathTex(
            r"ax^2+bx+c = a\left[\left(x+\frac{b}{2a}\right)^2-\frac{\Delta}{4a^2}\right]",
            font_size=32,
        )

        demonstration = MathTex(
            r"""
            \begin{aligned}
            ax^2+bx+c &= a\left(x^2+\frac{b}{a}x\right)+c \\
            &= a\left[\left(x+\frac{b}{2a}\right)^2-\frac{b^2}{4a^2}\right]+c \\
            &= a\left(x+\frac{b}{2a}\right)^2-\frac{b^2}{4a}+c \\
            &= a\left(x+\frac{b}{2a}\right)^2-\frac{b^2-4ac}{4a} \\
            &= a\left[\left(x+\frac{b}{2a}\right)^2-\frac{\Delta}{4a^2}\right]
            \end{aligned}
            """,
            font_size=26,
        )

        contenu_theoreme = VGroup(enonce_theoreme, demonstration).arrange(DOWN, buff=0.4)
        theoreme_box = theorem_box(contenu_theoreme, box_width=11.8)
        theoreme_box.next_to(titre, DOWN, buff=0.4)
        theoreme_box.scale(0.85)
        theoreme_box.next_to(titre, DOWN, buff=0.35)

        with self.voiceover(
            text=(
                "Pour tout réel x, le trinôme a x carré plus b x plus c "
                "peut se réécrire sous une forme dite canonique : a fois, "
                "entre crochets, le carré de x plus b sur deux a, moins "
                "delta sur quatre a carré. Voyons la démonstration. On met "
                "d'abord a en facteur dans les deux premiers termes. On "
                "reconnaît ensuite le début du carré de x plus b sur deux "
                "a, ce qui nous fait apparaître un terme en trop qu'on "
                "soustrait aussitôt. On développe et on réduit c moins b "
                "carré sur quatre a au même dénominateur, ce qui fait "
                "apparaître exactement b carré moins quatre a c, c'est à "
                "dire delta, au numérateur. On peut enfin refactoriser a "
                "pour obtenir la forme canonique annoncée."
            )
        ) as tracker:
            self.play(Write(enonce_theoreme))
            self.wait(2)
            self.play(FadeIn(demonstration))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(theoreme_box))

        # --- À retenir -------------------------------------------------------
        retenir = Text(
            "À retenir : tout trinôme ax² + bx + c se ramène à sa forme\n"
            "canonique grâce au discriminant Δ = b² − 4ac.",
            font_size=28,
            color=YELLOW,
        )
        retenir.next_to(titre, DOWN, buff=0.8)

        with self.voiceover(
            text=(
                "À retenir : tout trinôme du second degré se ramène à sa "
                "forme canonique grâce au discriminant delta égal à b "
                "carré moins quatre a c. C'est cette forme canonique qui "
                "va nous servir, dès la prochaine scène, à résoudre "
                "l'équation a x carré plus b x plus c égale zéro."
            )
        ) as tracker:
            self.play(FadeIn(retenir))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(titre), FadeOut(retenir))
