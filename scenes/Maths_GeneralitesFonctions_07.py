"""
scenes/Maths_GeneralitesFonctions_07.py — Chapitre 3 (1ereC, Maths), scène 07.

Composition de fonctions : définition de g∘f, remarques (non-commutativité,
domaine), exemple traité, sens de variation d'une composée.
Source : 1ereC/Maths.pdf, chapitre 3, pages 28-40.
"""

import textwrap

from manim import DOWN, LEFT, RIGHT, UP, WHITE, YELLOW, Arrow, FadeIn, FadeOut, MathTex, Text, VGroup, Write

from shapes.base_scene import NotionScene
from shapes.boxes import definition_box, essentiel_box, example_box, scene_title, theorem_box, warning_box


def _wrap(text: str, width: int = 60) -> str:
    return "\n".join(textwrap.fill(line, width=width) for line in text.split("\n"))


class CompositionFonctions(NotionScene):
    def construct(self):
        titre = scene_title("Composition de fonctions")
        titre.scale(0.6)
        titre.to_edge(UP)
        self.play(Write(titre))

        # --- Énoncé : définition de la composée -----------------------------
        def_composee = definition_box(
            MathTex(
                r"(g \circ f)(x) = g\big(f(x)\big), \qquad D_{g \circ f} = "
                r"\{x \in D_f \ / \ f(x) \in D_g\}",
                font_size=27,
            ),
            box_width=10.4,
        )
        def_composee.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "La composée de g par f, notée g rond f, est la fonction "
                "qui à x associe g de f de x. Son ensemble de définition "
                "est formé des x de Df tels que f de x appartienne à Dg."
            )
        ) as tracker:
            self.play(FadeIn(def_composee))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(def_composee))

        # --- Schéma de composition ------------------------------------------
        boite_x = MathTex("x", font_size=32)
        fleche1 = Arrow(LEFT * 0.3, RIGHT * 1.0, color=WHITE, buff=0.1)
        label_f = MathTex("f", font_size=26, color=YELLOW).next_to(fleche1, UP, buff=0.05)
        boite_fx = MathTex("f(x)", font_size=32).next_to(fleche1, RIGHT, buff=0.3)
        fleche2 = Arrow(RIGHT * 0.1, RIGHT * 1.4, color=WHITE, buff=0.1)
        fleche2.next_to(boite_fx, RIGHT, buff=0.1)
        label_g = MathTex("g", font_size=26, color=YELLOW).next_to(fleche2, UP, buff=0.05)
        boite_gfx = MathTex("g(f(x))", font_size=32).next_to(fleche2, RIGHT, buff=0.3)

        schema = VGroup(boite_x, fleche1, label_f, boite_fx, fleche2, label_g, boite_gfx)
        schema.arrange(RIGHT, buff=0.15)
        schema.move_to(titre.get_center() + DOWN * 2.2)

        with self.voiceover(
            text=(
                "On peut représenter la composition par un schéma en deux "
                "étapes : x est d'abord transformé par f en f de x, puis f "
                "de x est transformé par g en g de f de x, résultat final "
                "de la composée g rond f."
            )
        ) as tracker:
            self.play(FadeIn(schema))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(schema))

        # --- Remarques ------------------------------------------------------
        remarques = example_box(
            Text(
                _wrap(
                    "En général, g∘f ≠ f∘g : la composition n'est PAS "
                    "commutative. Le domaine de g∘f n'est pas Df tout "
                    "entier : il faut en plus que f(x) tombe dans Dg.",
                    width=56,
                ),
                font_size=23,
            ),
            box_width=10.8,
        )
        remarques.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Deux remarques essentielles : en général, g rond f est "
                "différente de f rond g — la composition n'est pas "
                "commutative. Et le domaine de g rond f n'est pas "
                "simplement Df : il faut aussi que f de x tombe bien dans "
                "Dg, le domaine de g."
            )
        ) as tracker:
            self.play(FadeIn(remarques))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(remarques))

        # --- Exemple traité 8 -------------------------------------------------
        enonce_ex8 = Text(
            "Exemple 8 — f(x) = 2x + 1, g(x) = x²",
            font_size=25,
            color=YELLOW,
            weight="BOLD",
        )
        enonce_ex8.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Exemple 8 : soit f de x égale deux x plus un, et g de x "
                "égale x carré. Calculons g rond f et f rond g."
            )
        ) as tracker:
            self.play(FadeIn(enonce_ex8))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(enonce_ex8))

        calcul_ex8 = example_box(
            MathTex(
                r"""
                \begin{array}{l}
                (g \circ f)(x) = g(2x+1) = (2x+1)^2 = 4x^2+4x+1 \\
                (f \circ g)(x) = f(x^2) = 2x^2+1 \\
                (g\circ f)(1) = 9 \ \neq \ (f \circ g)(1) = 3
                \end{array}
                """,
                font_size=27,
            ),
            box_width=9.7,
        )
        calcul_ex8.next_to(titre, DOWN, buff=0.55)

        with self.voiceover(
            text=(
                "g rond f de x vaut g appliqué à deux x plus un, soit deux "
                "x plus un au carré, c'est-à-dire quatre x carré plus "
                "quatre x plus un. f rond g de x vaut f appliqué à x "
                "carré, soit deux x carré plus un. En x égale un, g rond f "
                "vaut neuf, alors que f rond g vaut trois : les deux "
                "composées sont bien différentes, ce qui confirme la "
                "non-commutativité."
            )
        ) as tracker:
            self.play(FadeIn(calcul_ex8))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(calcul_ex8))

        # --- Théorème : sens de variation d'une composée -----------------
        theo_variation = theorem_box(
            MathTex(
                r"""
                \begin{array}{lll}
                f \nearrow \text{ sur } I,\ g \nearrow \text{ sur } f(I) & \Longrightarrow & g\circ f \nearrow \\
                f \nearrow \text{ sur } I,\ g \searrow \text{ sur } f(I) & \Longrightarrow & g\circ f \searrow \\
                f \searrow \text{ sur } I,\ g \nearrow \text{ sur } f(I) & \Longrightarrow & g\circ f \searrow \\
                f \searrow \text{ sur } I,\ g \searrow \text{ sur } f(I) & \Longrightarrow & g\circ f \nearrow
                \end{array}
                """,
                font_size=25,
            ),
            box_width=9.0,
        )
        theo_variation.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Théorème sur le sens de variation d'une composée, quatre "
                "cas à retenir : si f et g varient dans le même sens — "
                "toutes deux croissantes ou toutes deux décroissantes — "
                "alors g rond f est croissante. Si f et g varient en sens "
                "contraires, alors g rond f est décroissante."
            )
        ) as tracker:
            self.play(FadeIn(theo_variation))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(theo_variation))

        demo_variation = example_box(
            Text(
                _wrap(
                    "Démonstration (cas f croissante, g décroissante) : "
                    "soit a < b dans I. f croissante ⟹ f(a) ≤ f(b). g "
                    "décroissante ⟹ g(f(a)) ≥ g(f(b)), c'est-à-dire "
                    "(g∘f)(a) ≥ (g∘f)(b) : g∘f est décroissante sur I.",
                    width=58,
                ),
                font_size=22,
            ),
            box_width=11.2,
        )
        demo_variation.next_to(titre, DOWN, buff=0.55)

        with self.voiceover(
            text=(
                "Démontrons le cas où f est croissante et g décroissante. "
                "Soit a strictement inférieur à b dans I. Comme f est "
                "croissante, f de a est inférieur ou égal à f de b. Comme "
                "g est décroissante, appliquer g inverse cette inégalité : "
                "g de f de a est supérieur ou égal à g de f de b. "
                "Autrement dit, g rond f de a est supérieur ou égal à g "
                "rond f de b : la composée est bien décroissante."
            )
        ) as tracker:
            self.play(FadeIn(demo_variation))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(demo_variation))

        # --- À retenir ---------------------------------------------------
        retenir = essentiel_box(
            Text(
                "Même sens (↗↗ ou ↘↘) → g∘f croissante. Sens contraires (↗↘ ou ↘↗) → g∘f décroissante.",
                font_size=24,
            ),
            box_width=11.2,
        )
        retenir.next_to(titre, DOWN, buff=0.6)

        with self.voiceover(
            text=(
                "À retenir : quand f et g varient dans le même sens, la "
                "composée g rond f est croissante. Quand elles varient en "
                "sens contraires, la composée est décroissante — c'est "
                "une règle de signe, comme pour la multiplication."
            )
        ) as tracker:
            self.play(FadeIn(retenir))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(retenir))

        # --- Piège à éviter ----------------------------------------------
        piege = warning_box(
            Text(
                _wrap(
                    "Piège : g∘f et f∘g sont deux fonctions différentes en "
                    "général — bien respecter l'ordre d'écriture et de "
                    "calcul, on applique f en premier dans g∘f.",
                    width=56,
                ),
                font_size=23,
            ),
            box_width=10.6,
        )
        piege.next_to(titre, DOWN, buff=0.6)

        with self.voiceover(
            text=(
                "Attention : g rond f et f rond g sont deux fonctions "
                "différentes en général. Il faut bien respecter l'ordre "
                "d'écriture — dans g rond f, c'est f qui est appliquée en "
                "premier, puis g."
            )
        ) as tracker:
            self.play(FadeIn(piege))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(titre), FadeOut(piege))
