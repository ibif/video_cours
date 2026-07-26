"""
scenes/Maths_ExtensionNotionLimite_05.py — Chapitre 7 (1ereC, Maths), scène 05.

Limites de fonctions irrationnelles : méthode de la quantité conjuguée,
mise en facteur de x² sous un radical, piège fondamental √x² = |x|.
Exemples résolus : √(x²+3x) - x en +∞, et (2x+1)/√(x²+1) en -∞.
Source : 1ereC/Maths.pdf, chapitre 7, pages 80-90.
"""

import textwrap

from manim import DOWN, UP, FadeIn, FadeOut, MathTex, Text, VGroup, Write, YELLOW

from shapes.base_scene import NotionScene
from shapes.boxes import essentiel_box, example_box, method_box, scene_title, warning_box


def _wrap(text: str, width: int = 58) -> str:
    return "\n".join(textwrap.fill(line, width=width) for line in text.split("\n"))


class LimitesFonctionsIrrationnelles(NotionScene):
    def construct(self):
        titre = scene_title("Limites de fonctions irrationnelles")
        titre.scale(0.5)
        titre.to_edge(UP)

        # --- Énoncé ----------------------------------------------------------
        enonce = Text(
            "Comment lever une F.I. en présence d'une racine carrée ?",
            font_size=25,
            color=YELLOW,
            weight="BOLD",
        )
        enonce.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Quand une expression contient une racine carrée, les "
                "formes indéterminées classiques comme l'infini moins "
                "l'infini demandent des techniques spécifiques. Voyons les "
                "deux méthodes de référence."
            )
        ) as tracker:
            self.play(Write(titre))
            self.play(FadeIn(enonce))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(enonce))

        # --- Méthode 1 : quantité conjuguée -----------------------------------
        methode_conjuguee = method_box(
            VGroup(
                Text(
                    "Forme indéterminée ∞ - ∞ avec radicaux : multiplier "
                    "par la quantité conjuguée",
                    font_size=21,
                    weight="BOLD",
                ),
                MathTex(
                    r"\sqrt{u}-v = \dfrac{(\sqrt{u}-v)(\sqrt{u}+v)}{\sqrt{u}+v}"
                    r" = \dfrac{u-v^2}{\sqrt{u}+v}",
                    font_size=26,
                ),
                Text(
                    "On transforme ainsi une différence en un quotient, "
                    "souvent plus facile à étudier.",
                    font_size=20,
                ),
            ).arrange(DOWN, buff=0.3),
            box_width=11.2,
        )
        methode_conjuguee.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Première méthode : face à une forme indéterminée infini "
                "moins infini contenant une racine carrée, on multiplie "
                "l'expression par sa quantité conjuguée, en haut et en bas. "
                "Racine de u moins v, multiplié par racine de u plus v, "
                "donne u moins v carré, grâce à l'identité remarquable. On "
                "transforme ainsi une différence gênante en un quotient, "
                "en général bien plus facile à étudier."
            )
        ) as tracker:
            self.play(FadeIn(methode_conjuguee))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(methode_conjuguee))

        # --- Méthode 2 : mise en facteur de x² sous le radical -----------------
        methode_facteur = method_box(
            VGroup(
                Text(
                    "Sous un radical, mettre x² en facteur :",
                    font_size=21,
                    weight="BOLD",
                ),
                MathTex(
                    r"\sqrt{x^2+ax+b} = \sqrt{x^2\left(1+\dfrac{a}{x}+\dfrac{b}{x^2}\right)}"
                    r" = |x|\sqrt{1+\dfrac{a}{x}+\dfrac{b}{x^2}}",
                    font_size=25,
                ),
            ).arrange(DOWN, buff=0.3),
            box_width=11.2,
        )
        methode_facteur.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Deuxième méthode, souvent combinée à la première : sous un "
                "radical, on met x carré en facteur. Racine de x carré plus "
                "a x plus b devient racine de x carré, fois racine de un "
                "plus a sur x plus b sur x carré, soit valeur absolue de x, "
                "fois cette même racine, qui elle tend simplement vers un."
            )
        ) as tracker:
            self.play(FadeIn(methode_facteur))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(methode_facteur))

        # --- Piège fondamental --------------------------------------------
        piege_fondamental = warning_box(
            VGroup(
                Text(
                    "Piège fondamental : √x² = |x|, jamais simplement x !",
                    font_size=22,
                    weight="BOLD",
                ),
                MathTex(
                    r"\sqrt{x^2} = |x| ="
                    r"\begin{cases} x & \text{si } x \geq 0 \\ -x & \text{si } x < 0 \end{cases}",
                    font_size=25,
                ),
                Text(
                    "En -∞, x < 0 donc √x² = -x : il faut changer le signe !",
                    font_size=20,
                ),
            ).arrange(DOWN, buff=0.3),
            box_width=11.2,
        )
        piege_fondamental.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Un piège fondamental à ne jamais oublier : racine carrée "
                "de x carré vaut valeur absolue de x, et non pas simplement "
                "x. Cette valeur absolue vaut x si x est positif ou nul, et "
                "moins x si x est strictement négatif. Ainsi, en moins "
                "l'infini, x est négatif, donc racine de x carré vaut moins "
                "x : il faut absolument changer le signe, sous peine "
                "d'obtenir un résultat faux."
            )
        ) as tracker:
            self.play(FadeIn(piege_fondamental))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(piege_fondamental))

        # --- Exemple résolu 5 --------------------------------------------------
        enonce_ex5 = Text(
            "Exemple 5 — limite en +∞ de √(x²+3x) - x",
            font_size=25,
            color=YELLOW,
            weight="BOLD",
        )
        enonce_ex5.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Exemple : calculons la limite en plus l'infini de racine "
                "de x carré plus trois x, moins x. On reconnaît la forme "
                "infini moins infini."
            )
        ) as tracker:
            self.play(FadeIn(enonce_ex5))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(enonce_ex5))

        etape1_ex5 = example_box(
            MathTex(
                r"""
                \sqrt{x^2+3x}-x =
                \dfrac{(\sqrt{x^2+3x}-x)(\sqrt{x^2+3x}+x)}{\sqrt{x^2+3x}+x}
                = \dfrac{3x}{\sqrt{x^2+3x}+x}
                """,
                font_size=25,
            ),
            box_width=11.4,
        )
        etape1_ex5.next_to(titre, DOWN, buff=0.55)

        with self.voiceover(
            text=(
                "On multiplie par la quantité conjuguée : racine de x carré "
                "plus trois x, moins x, fois racine de x carré plus trois x, "
                "plus x, sur ce même dénominateur. Au numérateur, il ne "
                "reste que trois x, grâce à l'identité remarquable."
            )
        ) as tracker:
            self.play(FadeIn(etape1_ex5))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(etape1_ex5))

        etape2_ex5 = example_box(
            MathTex(
                r"""
                \dfrac{3x}{\sqrt{x^2+3x}+x}
                = \dfrac{3x}{|x|\sqrt{1+\frac{3}{x}}+x}
                = \dfrac{3x}{x\sqrt{1+\frac{3}{x}}+x}
                \quad (x>0 \text{ en } +\infty)
                """,
                font_size=24,
            ),
            box_width=11.6,
        )
        etape2_ex5.next_to(titre, DOWN, buff=0.55)

        with self.voiceover(
            text=(
                "On met x carré en facteur sous le radical : racine de x "
                "carré plus trois x devient valeur absolue de x, fois "
                "racine de un plus trois sur x. Comme on est en plus "
                "l'infini, x est positif, donc valeur absolue de x vaut "
                "simplement x."
            )
        ) as tracker:
            self.play(FadeIn(etape2_ex5))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(etape2_ex5))

        resultat_ex5 = example_box(
            MathTex(
                r"""
                = \dfrac{3x}{x\left(\sqrt{1+\frac{3}{x}}+1\right)}
                = \dfrac{3}{\sqrt{1+\frac{3}{x}}+1}
                \ \xrightarrow[x\to+\infty]{} \ \dfrac{3}{1+1} = \dfrac{3}{2}
                """,
                font_size=26,
            ),
            box_width=11.4,
        )
        resultat_ex5.next_to(titre, DOWN, buff=0.55)

        with self.voiceover(
            text=(
                "On factorise x au dénominateur puis on simplifie : il "
                "reste trois, sur racine de un plus trois sur x, plus un. "
                "Quand x tend vers plus l'infini, trois sur x tend vers "
                "zéro, donc la limite vaut trois sur un plus un, "
                "c'est-à-dire trois demis."
            )
        ) as tracker:
            self.play(FadeIn(resultat_ex5))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(resultat_ex5))

        # --- Exemple résolu 6 --------------------------------------------------
        enonce_ex6 = Text(
            "Exemple 6 — limite en -∞ de (2x+1)/√(x²+1)",
            font_size=25,
            color=YELLOW,
            weight="BOLD",
        )
        enonce_ex6.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Deuxième exemple : calculons la limite en moins l'infini "
                "de deux x plus un, sur racine de x carré plus un — un "
                "exemple où le piège du signe de x est décisif."
            )
        ) as tracker:
            self.play(FadeIn(enonce_ex6))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(enonce_ex6))

        etape1_ex6 = example_box(
            MathTex(
                r"""
                \sqrt{x^2+1} = |x|\sqrt{1+\dfrac{1}{x^2}}
                = -x\sqrt{1+\dfrac{1}{x^2}}
                \quad (x<0 \text{ en } -\infty)
                """,
                font_size=26,
            ),
            box_width=10.5,
        )
        etape1_ex6.next_to(titre, DOWN, buff=0.55)

        with self.voiceover(
            text=(
                "On met x carré en facteur sous le radical : racine de x "
                "carré plus un devient valeur absolue de x, fois racine de "
                "un plus un sur x carré. Mais cette fois, on est en moins "
                "l'infini, donc x est négatif, et valeur absolue de x vaut "
                "moins x. C'est ici que le piège du signe intervient."
            )
        ) as tracker:
            self.play(FadeIn(etape1_ex6))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(etape1_ex6))

        etape2_ex6 = example_box(
            MathTex(
                r"""
                \dfrac{2x+1}{\sqrt{x^2+1}}
                = \dfrac{x\left(2+\frac{1}{x}\right)}{-x\sqrt{1+\frac{1}{x^2}}}
                = \dfrac{2+\frac{1}{x}}{-\sqrt{1+\frac{1}{x^2}}}
                """,
                font_size=26,
            ),
            box_width=11.0,
        )
        etape2_ex6.next_to(titre, DOWN, buff=0.55)

        with self.voiceover(
            text=(
                "On met x en facteur au numérateur, moins x en facteur au "
                "dénominateur d'après l'étape précédente, puis on simplifie "
                "par x. Il reste deux plus un sur x, sur moins racine de un "
                "plus un sur x carré."
            )
        ) as tracker:
            self.play(FadeIn(etape2_ex6))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(etape2_ex6))

        resultat_ex6 = example_box(
            MathTex(
                r"""
                \lim_{x\to-\infty} \dfrac{2x+1}{\sqrt{x^2+1}}
                = \dfrac{2}{-\sqrt{1}} = -2
                """,
                font_size=28,
            ),
            box_width=9.0,
        )
        resultat_ex6.next_to(titre, DOWN, buff=0.55)

        with self.voiceover(
            text=(
                "Quand x tend vers moins l'infini, un sur x et un sur x "
                "carré tendent vers zéro, donc la limite vaut deux, sur "
                "moins racine de un, soit moins deux. Si on avait oublié le "
                "changement de signe, on aurait trouvé plus deux, un "
                "résultat faux."
            )
        ) as tracker:
            self.play(FadeIn(resultat_ex6))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(resultat_ex6))

        # --- À retenir -----------------------------------------------------
        retenir = essentiel_box(
            Text(
                _wrap(
                    "Avec des radicaux : quantité conjuguée pour ∞-∞, mise "
                    "en facteur de x² sous le radical pour ∞/∞. Toujours "
                    "vérifier le signe de x pour écrire √x² = |x|.",
                    width=58,
                ),
                font_size=23,
            )
        )
        retenir.next_to(titre, DOWN, buff=0.6)

        with self.voiceover(
            text=(
                "À retenir : face à des radicaux, on combine deux outils, "
                "la quantité conjuguée pour lever l'infini moins l'infini, "
                "et la mise en facteur de x carré sous le radical. Dans "
                "tous les cas, il faut vérifier le signe de x pour écrire "
                "correctement racine de x carré égale valeur absolue de x."
            )
        ) as tracker:
            self.play(FadeIn(retenir))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(retenir))

        # --- Piège à éviter --------------------------------------------------
        piege_final = warning_box(
            Text(
                _wrap(
                    "Piège récapitulatif : en +∞, √x² = x ; en -∞, √x² = -x. "
                    "Un oubli de signe ici inverse purement et simplement "
                    "le résultat final de la limite.",
                    width=58,
                ),
                font_size=23,
            )
        )
        piege_final.next_to(titre, DOWN, buff=0.6)

        with self.voiceover(
            text=(
                "Pour finir, gardons en tête ce piège récapitulatif : en "
                "plus l'infini, racine de x carré vaut x, mais en moins "
                "l'infini, elle vaut moins x. Un oubli de ce signe inverse "
                "purement et simplement le résultat final de la limite."
            )
        ) as tracker:
            self.play(FadeIn(piege_final))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(titre), FadeOut(piege_final))
