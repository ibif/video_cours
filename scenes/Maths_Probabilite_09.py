"""
scenes/Maths_Probabilite_09.py — Chapitre 12 « Probabilité » (1ereC, Maths),
scène 09.

§ Espérance mathématique : définition E(X)=Σ p_i·x_i, interprétation
(valeur moyenne / gain moyen sur le long terme, « centre de gravité »
de la loi). Théorème de linéarité E(aX+b)=aE(X)+b avec démonstration
courte. Exemple : reprise de X (nombre de Face sur 2 pièces), E(X)=1.
Source : 1ereC/Maths.pdf, chapitre 12, page 151.
"""

import textwrap

from manim import DOWN, RIGHT, UP, WHITE, YELLOW, Dot, FadeIn, FadeOut, Line, MathTex, NumberLine, Text, VGroup, Write

from shapes.base_scene import NotionScene
from shapes.boxes import definition_box, example_box, scene_title, theorem_box


def _wrap(text: str, width: int = 54) -> str:
    return "\n".join(textwrap.fill(line, width=width) for line in text.split("\n"))


def _centre_de_gravite() -> VGroup:
    """Illustration : loi de X sur une droite graduée, E(X) = point d'équilibre."""
    ligne = NumberLine(x_range=[-0.5, 2.5, 1], length=6, color=WHITE, include_numbers=True, font_size=20)
    masses = VGroup(
        Dot(ligne.n2p(0), radius=0.14, color=YELLOW),
        Dot(ligne.n2p(1), radius=0.20, color=YELLOW),
        Dot(ligne.n2p(2), radius=0.14, color=YELLOW),
    )
    fleche_equilibre = Line(ligne.n2p(1) + DOWN * 0.55, ligne.n2p(1) + DOWN * 0.1, color="#DE7C1F", stroke_width=5)
    label_equilibre = MathTex(r"E(X)=1", font_size=22, color="#DE7C1F").next_to(fleche_equilibre, DOWN, buff=0.1)
    return VGroup(ligne, masses, fleche_equilibre, label_equilibre)


class EsperanceMathematique(NotionScene):
    def construct(self):
        titre = scene_title("Probabilité — Espérance mathématique")
        titre.scale(0.5)
        titre.to_edge(UP)

        # --- Énoncé : mise en situation --------------------------------------
        mise_en_situation = Text(
            _wrap(
                "Si l'on répète une expérience aléatoire un très grand "
                "nombre de fois, autour de quelle valeur X se "
                "stabilise-t-elle en moyenne ? C'est l'espérance "
                "mathématique.",
                width=56,
            ),
            font_size=23,
        )
        mise_en_situation.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Si l'on répète une expérience aléatoire un très grand "
                "nombre de fois, autour de quelle valeur la variable X "
                "se stabilise-t-elle, en moyenne ? La réponse à cette "
                "question s'appelle l'espérance mathématique."
            )
        ) as tracker:
            self.play(Write(titre))
            self.play(FadeIn(mise_en_situation))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(mise_en_situation))

        # --- Raisonnement : définition + interprétation --------------------------
        definition = definition_box(
            VGroup(
                Text("Espérance mathématique de X", font_size=23, weight="BOLD"),
                MathTex(r"E(X) = \sum_i p_i \, x_i = p_1 x_1 + p_2 x_2 + \dots + p_n x_n", font_size=26),
            ).arrange(DOWN, buff=0.25),
        )
        definition.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "L'espérance mathématique de X, notée E de X, est la "
                "somme des produits p-i fois x-i, pour chaque valeur "
                "prise par X, pondérée par sa probabilité."
            )
        ) as tracker:
            self.play(FadeIn(definition))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(definition))

        interpretation = definition_box(
            VGroup(
                Text("Interprétation", font_size=22, weight="BOLD"),
                Text(
                    _wrap(
                        "E(X) est la valeur MOYENNE prise par X sur un "
                        "très grand nombre de répétitions (« sur le long "
                        "terme »). C'est le CENTRE DE GRAVITÉ de la loi "
                        "de X.",
                        width=44,
                    ),
                    font_size=21,
                ),
            ).arrange(DOWN, buff=0.25),
        )
        interpretation.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Interprétons ce nombre. E de X représente la valeur "
                "moyenne que prend X sur un très grand nombre de "
                "répétitions de l'expérience — on parle de moyenne « sur "
                "le long terme ». On peut aussi l'imaginer comme le "
                "centre de gravité de la loi de X, si l'on place une "
                "masse p-i à chaque position x-i sur une droite graduée."
            )
        ) as tracker:
            self.play(FadeIn(interpretation))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(interpretation))

        # --- Théorème de linéarité ------------------------------------------------
        theoreme = theorem_box(
            VGroup(
                Text("Linéarité de l'espérance", font_size=22, weight="BOLD"),
                MathTex(r"E(aX+b) = a\,E(X) + b \qquad (a,b \in \mathbb{R})", font_size=26),
            ).arrange(DOWN, buff=0.25),
        )
        theoreme.next_to(titre, DOWN, buff=0.4)

        demo = VGroup(
            MathTex(r"E(aX+b) = \sum_i p_i\,(a x_i + b) = \sum_i \big(a\,p_i x_i + b\,p_i\big)", font_size=21),
            MathTex(r"= a \sum_i p_i x_i + b \sum_i p_i = a\,E(X) + b \times 1", font_size=21, color=YELLOW),
        ).arrange(DOWN, buff=0.25)
        demo.next_to(theoreme, DOWN, buff=0.35)

        with self.voiceover(
            text=(
                "Un théorème très utile : pour tous réels a et b, "
                "l'espérance de a-X plus b vaut a fois l'espérance de X, "
                "plus b. Démonstration courte : on développe a fois x-i "
                "plus b dans la somme, on sépare en deux sommes distinctes "
                "grâce à la distributivité, on sort les constantes a et "
                "b, et l'on reconnaît d'un côté E de X, et de l'autre la "
                "somme des p-i, qui vaut 1 par définition d'une loi de "
                "probabilité."
            )
        ) as tracker:
            self.play(FadeIn(theoreme))
            self.play(Write(demo))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(theoreme), FadeOut(demo))

        # --- Exemple : reprise de X (deux pièces) ---------------------------------
        enonce = Text(
            _wrap(
                "Reprenons X, le nombre de Face sur deux pièces : "
                "P(X=0)=1/4, P(X=1)=1/2, P(X=2)=1/4.",
                width=52,
            ),
            font_size=22,
        )
        enonce.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Reprenons l'exemple de la scène précédente : X, le "
                "nombre de Face obtenues sur deux pièces, avec P de X "
                "égale 0 égale 1 quart, P de X égale 1 égale 1 demi, et P "
                "de X égale 2 égale 1 quart."
            )
        ) as tracker:
            self.play(FadeIn(enonce))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(enonce))

        calcul = MathTex(
            r"E(X) = \tfrac{1}{4}\times 0 + \tfrac{1}{2}\times 1 + \tfrac{1}{4}\times 2 = 0 + \tfrac{1}{2} + \tfrac{1}{2} = 1",
            font_size=25,
        )
        calcul.next_to(titre, DOWN, buff=0.55)
        conclusion = MathTex(r"E(X) = 1", font_size=30, color=YELLOW)
        conclusion.next_to(calcul, DOWN, buff=0.4)

        centre_gravite = _centre_de_gravite()
        centre_gravite.next_to(conclusion, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "L'espérance de X vaut donc 1 quart fois 0, plus 1 demi "
                "fois 1, plus 1 quart fois 2, soit 0 plus 1 demi plus 1 "
                "demi, égale 1. En moyenne, sur un très grand nombre de "
                "lancers de deux pièces, on obtient donc 1 Face — ce qui "
                "est parfaitement cohérent avec l'intuition. "
                "Graphiquement, 1 est bien le point d'équilibre, le "
                "centre de gravité, de la loi de X."
            )
        ) as tracker:
            self.play(Write(calcul))
            self.play(FadeIn(conclusion))
            self.play(FadeIn(centre_gravite))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(calcul), FadeOut(conclusion), FadeOut(centre_gravite))

        # --- À retenir --------------------------------------------------------------
        recap = example_box(
            VGroup(
                Text("À retenir", font_size=22, weight="BOLD"),
                MathTex(r"E(X) \ : \ \text{valeur moyenne « sur le long terme », PAS une valeur réellement atteinte.}", font_size=20),
            ).arrange(DOWN, buff=0.22),
        )
        recap.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Retenons bien que E de X est une valeur moyenne sur le "
                "long terme, et pas forcément une valeur réellement "
                "atteinte par X : ici, X ne prend jamais la valeur 1,5 par "
                "exemple, alors que E de X pourrait très bien être 1,5 "
                "dans un autre exemple."
            )
        ) as tracker:
            self.play(FadeIn(recap))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(recap), FadeOut(titre))
