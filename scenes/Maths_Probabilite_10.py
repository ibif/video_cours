"""
scenes/Maths_Probabilite_10.py — Chapitre 12 « Probabilité » (1ereC, Maths),
scène 10.

§ Variance, écart-type, formule de König-Huygens : définition
V(X)=Σp_i(x_i-m)² et σ(X)=√V(X), interprétation (dispersion autour de
la moyenne). Théorème de König-Huygens V(X)=E(X²)-[E(X)]² avec
démonstration. Théorème V(aX+b)=a²V(X), σ(aX+b)=|a|σ(X). Exemple
résolu complet, tableau de calcul (x_i, p_i, p_i·x_i, p_i·x_i²) :
reprise de X (2 pièces), E(X)=1, E(X²)=3/2, V(X)=1/2, σ(X)=√2/2≈0,71.
Source : 1ereC/Maths.pdf, chapitre 12, pages 151-152.
"""

import textwrap

from manim import DOWN, RIGHT, UP, YELLOW, FadeIn, FadeOut, MathTex, Text, VGroup, Write

from shapes.base_scene import NotionScene
from shapes.boxes import definition_box, example_box, scene_title, theorem_box


def _wrap(text: str, width: int = 54) -> str:
    return "\n".join(textwrap.fill(line, width=width) for line in text.split("\n"))


def _tableau_calcul() -> VGroup:
    """Tableau de calcul x_i / p_i / p_i·x_i / p_i·x_i² pour X (2 pièces)."""
    entetes = VGroup(
        MathTex(r"x_i", font_size=22),
        MathTex(r"p_i", font_size=22),
        MathTex(r"p_i x_i", font_size=22),
        MathTex(r"p_i x_i^2", font_size=22),
    ).arrange(RIGHT, buff=1.0)

    lignes_data = [
        (r"0", r"\tfrac{1}{4}", r"0", r"0"),
        (r"1", r"\tfrac{1}{2}", r"\tfrac{1}{2}", r"\tfrac{1}{2}"),
        (r"2", r"\tfrac{1}{4}", r"\tfrac{1}{2}", r"1"),
    ]
    lignes = VGroup()
    for x, p, px, px2 in lignes_data:
        ligne = VGroup(
            MathTex(x, font_size=20),
            MathTex(p, font_size=20),
            MathTex(px, font_size=20),
            MathTex(px2, font_size=20),
        ).arrange(RIGHT, buff=1.0)
        lignes.add(ligne)
    lignes.arrange(DOWN, buff=0.28)

    ligne_totaux = VGroup(
        MathTex(r"\Sigma", font_size=20),
        MathTex(r"1", font_size=20),
        MathTex(r"E(X)=1", font_size=20, color=YELLOW),
        MathTex(r"E(X^2)=\tfrac{3}{2}", font_size=20, color=YELLOW),
    ).arrange(RIGHT, buff=0.85)

    tableau = VGroup(entetes, lignes, ligne_totaux).arrange(DOWN, buff=0.35)
    return tableau


class VarianceEcartTypeKonigHuygens(NotionScene):
    def construct(self):
        titre = scene_title("Probabilité — Variance, écart-type")
        titre.scale(0.5)
        titre.to_edge(UP)

        # --- Énoncé : mise en situation --------------------------------------
        mise_en_situation = Text(
            _wrap(
                "L'espérance donne la valeur moyenne de X, mais pas sa "
                "DISPERSION : deux lois peuvent avoir la même moyenne et "
                "être très différentes. Il faut un second indicateur.",
                width=56,
            ),
            font_size=23,
        )
        mise_en_situation.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "L'espérance donne la valeur moyenne de X, mais pas sa "
                "dispersion autour de cette moyenne : deux lois "
                "différentes peuvent avoir exactement la même espérance, "
                "tout en étant très différentes, l'une resserrée autour "
                "de la moyenne, l'autre très étalée. Il faut donc un "
                "second indicateur."
            )
        ) as tracker:
            self.play(Write(titre))
            self.play(FadeIn(mise_en_situation))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(mise_en_situation))

        # --- Raisonnement : définitions variance et écart-type -----------------
        definition = definition_box(
            VGroup(
                Text("Variance et écart-type", font_size=23, weight="BOLD"),
                MathTex(r"V(X) = \sum_i p_i\,(x_i - m)^2, \quad m = E(X)", font_size=25),
                MathTex(r"\sigma(X) = \sqrt{V(X)}", font_size=27),
                Text(_wrap("V(X) et σ(X) mesurent la DISPERSION de X autour de sa moyenne m.", width=44), font_size=20),
            ).arrange(DOWN, buff=0.22),
        )
        definition.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "La variance de X, notée V de X, est la moyenne des "
                "carrés des écarts à la moyenne m égale E de X : la somme "
                "des p-i fois x-i moins m, le tout au carré. L'écart-type, "
                "noté sigma de X, en est simplement la racine carrée. Ces "
                "deux nombres mesurent la dispersion de X autour de sa "
                "moyenne."
            )
        ) as tracker:
            self.play(FadeIn(definition))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(definition))

        # --- Théorème König-Huygens + démonstration ------------------------------
        theoreme = theorem_box(
            VGroup(
                Text("Formule de König-Huygens", font_size=22, weight="BOLD"),
                MathTex(r"V(X) = E(X^2) - \big[E(X)\big]^2", font_size=27),
            ).arrange(DOWN, buff=0.25),
        )
        theoreme.next_to(titre, DOWN, buff=0.4)

        demo = VGroup(
            MathTex(r"V(X) = \sum_i p_i (x_i-m)^2 = \sum_i p_i\big(x_i^2 - 2m x_i + m^2\big)", font_size=19),
            MathTex(r"= \sum_i p_i x_i^2 - 2m \sum_i p_i x_i + m^2 \sum_i p_i", font_size=19),
            MathTex(r"= E(X^2) - 2m \cdot m + m^2 \times 1 = E(X^2) - m^2", font_size=19, color=YELLOW),
        ).arrange(DOWN, buff=0.2)
        demo.next_to(theoreme, DOWN, buff=0.35)

        with self.voiceover(
            text=(
                "En pratique, on utilise presque toujours la formule de "
                "König-Huygens, bien plus rapide à calculer : la variance "
                "de X vaut l'espérance de X au carré, moins le carré de "
                "l'espérance de X. Démonstration : on développe le carré "
                "x-i moins m, on sépare la somme en trois termes, et l'on "
                "reconnaît E de X au carré, puis E de X, puis la somme des "
                "p-i qui vaut 1 ; il ne reste plus que E de X au carré, "
                "moins m au carré."
            )
        ) as tracker:
            self.play(FadeIn(theoreme))
            self.play(Write(demo))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(theoreme), FadeOut(demo))

        # --- Théorème V(aX+b) -------------------------------------------------------
        theoreme2 = theorem_box(
            VGroup(
                Text("Effet d'une transformation affine", font_size=21, weight="BOLD"),
                MathTex(r"V(aX+b) = a^2\,V(X) \qquad \sigma(aX+b) = |a|\,\sigma(X)", font_size=24),
                Text(_wrap("Un décalage (+b) ne change PAS la dispersion ; une dilatation (×a) la multiplie par |a|.", width=44), font_size=19),
            ).arrange(DOWN, buff=0.22),
        )
        theoreme2.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Autre résultat utile : pour tous réels a et b, la "
                "variance de a-X plus b vaut a au carré fois la variance "
                "de X, et l'écart-type de a-X plus b vaut la valeur "
                "absolue de a fois l'écart-type de X. Intuitivement, un "
                "simple décalage, le plus b, ne change en rien la "
                "dispersion des valeurs ; seule une dilatation, le "
                "facteur a, modifie l'étalement de la loi."
            )
        ) as tracker:
            self.play(FadeIn(theoreme2))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(theoreme2))

        # --- Exemple résolu complet : tableau de calcul --------------------------
        enonce = Text(
            _wrap(
                "Exemple résolu complet : reprenons X, nombre de Face sur "
                "deux pièces. Construisons un tableau de calcul.",
                width=52,
            ),
            font_size=22,
        )
        enonce.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Exemple résolu complet. Reprenons X, le nombre de Face "
                "sur deux pièces, et construisons le tableau de calcul "
                "habituel : x-i, p-i, p-i fois x-i, et p-i fois x-i au "
                "carré."
            )
        ) as tracker:
            self.play(FadeIn(enonce))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(enonce))

        tableau = _tableau_calcul()
        tableau.scale(0.95)
        tableau.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "En sommant la colonne p-i fois x-i, on retrouve E de X "
                "égale 1. En sommant la colonne p-i fois x-i au carré, on "
                "obtient E de X au carré, égale 0 fois 1 quart, plus 1 "
                "fois 1 demi, plus 4 fois 1 quart, soit 1 demi plus 1, "
                "égale 3 demis."
            )
        ) as tracker:
            self.play(Write(tableau))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(tableau))

        calcul_final = VGroup(
            MathTex(r"V(X) = E(X^2) - [E(X)]^2 = \tfrac{3}{2} - 1^2 = \tfrac{1}{2}", font_size=25),
            MathTex(r"\sigma(X) = \sqrt{\tfrac{1}{2}} = \dfrac{\sqrt{2}}{2} \approx 0,71", font_size=27, color=YELLOW),
        ).arrange(DOWN, buff=0.4)
        calcul_final.next_to(titre, DOWN, buff=0.55)

        with self.voiceover(
            text=(
                "Par König-Huygens, la variance de X vaut donc 3 demis "
                "moins 1 au carré, soit 1 demi. L'écart-type de X vaut la "
                "racine carrée de 1 demi, c'est-à-dire racine de 2 sur 2, "
                "soit environ 0 virgule 71."
            )
        ) as tracker:
            self.play(Write(calcul_final[0]))
            self.play(Write(calcul_final[1]))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(calcul_final))

        # --- À retenir --------------------------------------------------------------
        recap = example_box(
            VGroup(
                Text("À retenir", font_size=22, weight="BOLD"),
                MathTex(r"\text{Toujours passer par König-Huygens : } V(X)=E(X^2)-[E(X)]^2.", font_size=21),
                MathTex(r"\sigma(X) \text{ s'exprime dans la MÊME unité que } X.", font_size=21),
            ).arrange(DOWN, buff=0.22),
        )
        recap.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Retenons deux points essentiels. D'abord, en pratique, "
                "on passe presque toujours par König-Huygens pour "
                "calculer la variance, bien plus rapide que la définition "
                "directe. Ensuite, l'écart-type sigma de X s'exprime dans "
                "la même unité que X, contrairement à la variance qui "
                "s'exprime dans le carré de cette unité."
            )
        ) as tracker:
            self.play(FadeIn(recap))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(recap), FadeOut(titre))
