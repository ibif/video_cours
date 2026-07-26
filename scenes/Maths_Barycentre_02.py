"""
scenes/Maths_Barycentre_02.py — Chapitre 4 « Barycentre » (1ereC, Maths),
scène 02.

§ Propriété d'homogénéité du barycentre de deux points (avec démonstration
et exemple numérique), tableau récapitulatif de la position de G sur la
droite (AB) selon le signe de αβ, exemple résolu 1 (construction de G et
G').
Source : 1ereC/Maths.pdf, chapitre 4, page 42.
"""

import textwrap

from manim import (
    DOWN,
    LEFT,
    RIGHT,
    UP,
    WHITE,
    YELLOW,
    Create,
    Dot,
    FadeIn,
    FadeOut,
    Line,
    MathTex,
    Text,
    VGroup,
    Write,
)

from shapes.base_scene import NotionScene
from shapes.boxes import example_box, property_box, scene_title, warning_box


def _wrap(text: str, width: int = 54) -> str:
    return "\n".join(textwrap.fill(line, width=width) for line in text.split("\n"))


def _dot_label(point, label, color=WHITE, label_dir=UP, font_size=30, dot_color=YELLOW):
    d = Dot(point, color=dot_color)
    t = MathTex(label, font_size=font_size, color=color)
    t.next_to(d, label_dir, buff=0.15)
    return VGroup(d, t)


class HomogeneitePositionSurAB(NotionScene):
    def construct(self):
        titre = scene_title("Barycentre — Homogénéité et position sur (AB)")
        titre.scale(0.48)
        titre.to_edge(UP)

        # --- Énoncé -------------------------------------------------------------
        question = Text(
            _wrap(
                "Si on multiplie les deux coefficients α et β par le même "
                "réel non nul, le barycentre G change-t-il ? Et où se "
                "trouve G exactement sur la droite (AB) ?",
                width=54,
            ),
            font_size=25,
        )
        question.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Deux questions naturelles se posent. Première question : "
                "si on multiplie les deux coefficients alpha et bêta par un "
                "même réel non nul, le barycentre G change-t-il ? Seconde "
                "question : où se trouve exactement G sur la droite A-B, "
                "selon le signe des coefficients ?"
            )
        ) as tracker:
            self.play(Write(titre))
            self.play(FadeIn(question))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(question))

        # --- Raisonnement : homogénéité -----------------------------------------
        enonce_prop = MathTex(
            r"k \in \mathbb{R}^{*} \ \Rightarrow\ "
            r"\mathrm{bar}\{(A,\alpha)\,;\,(B,\beta)\} = \mathrm{bar}\{(A,k\alpha)\,;\,(B,k\beta)\}",
            font_size=25,
        )
        propriete = property_box(enonce_prop)
        propriete.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Réponse à la première question : c'est la propriété "
                "d'homogénéité. Pour tout réel k non nul, le barycentre de "
                "A-alpha et B-bêta est le même que celui de A, k-alpha, et "
                "B, k-bêta : multiplier tous les coefficients par un même "
                "nombre non nul ne change pas le barycentre."
            )
        ) as tracker:
            self.play(FadeIn(propriete))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(propriete))

        demo = MathTex(
            r"\overrightarrow{AG} = \dfrac{\beta}{\alpha+\beta}\,\overrightarrow{AB}"
            r" = \dfrac{k\beta}{k\alpha+k\beta}\,\overrightarrow{AB}",
            font_size=27,
        )
        demo.next_to(titre, DOWN, buff=0.6)

        exemple_num = MathTex(
            r"\mathrm{bar}\{(A,2222)\,;\,(B,3333)\} = \mathrm{bar}\{(A,2)\,;\,(B,3)\}"
            r"\quad (k = \tfrac{1}{1111})",
            font_size=25,
            color=YELLOW,
        )
        exemple_num.next_to(demo, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "La démonstration est immédiate : le vecteur A-G vaut bêta "
                "sur alpha plus bêta, fois le vecteur A-B ; en multipliant "
                "numérateur et dénominateur par k, on obtient exactement la "
                "même fraction, donc le même point G. Exemple : le "
                "barycentre de A pondéré par deux-mille deux-cent "
                "vingt-deux, et B pondéré par trois-mille trois-cent "
                "trente-trois, est le même que celui de A-deux et B-trois, "
                "car mille cent onze divise les deux coefficients."
            )
        ) as tracker:
            self.play(Write(demo))
            self.play(Write(exemple_num))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(demo), FadeOut(exemple_num))

        # --- Tableau récapitulatif de la position de G ---------------------------
        entete_tableau = Text("Position de G sur la droite (AB)", font_size=26, color=YELLOW, weight="BOLD")
        entete_tableau.next_to(titre, DOWN, buff=0.4)

        tableau = MathTex(
            r"""
            \begin{array}{|c|c|}
            \hline
            \alpha\beta > 0 & G \in [AB] \\
            \hline
            \alpha = 0 & G = B \\
            \hline
            \beta = 0 & G = A \\
            \hline
            \alpha\beta < 0 & G \notin [AB] \text{ (côté du plus grand } |\text{coefficient}|\text{)} \\
            \hline
            \end{array}
            """,
            font_size=25,
        )
        tableau.next_to(entete_tableau, DOWN, buff=0.4)
        groupe_tableau = VGroup(entete_tableau, tableau)

        with self.voiceover(
            text=(
                "Voici le tableau récapitulatif de la position de G sur la "
                "droite A-B. Si alpha fois bêta est strictement positif, "
                "c'est-à-dire si les deux coefficients ont le même signe, G "
                "est à l'intérieur du segment A-B. Si alpha est nul, G est "
                "confondu avec B ; si bêta est nul, G est confondu avec A. "
                "Enfin, si alpha fois bêta est strictement négatif, les "
                "coefficients sont de signes contraires, et G se trouve à "
                "l'extérieur du segment A-B, du côté du point dont le "
                "coefficient a la plus grande valeur absolue."
            )
        ) as tracker:
            self.play(FadeIn(entete_tableau))
            self.play(Write(tableau))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(groupe_tableau))

        # --- Exemple traité : exemple résolu 1 -----------------------------------
        a_pt = LEFT * 4.5
        b_pt = RIGHT * 0.5
        axe = Line(LEFT * 5.5, RIGHT * 3, color=WHITE)
        pa = _dot_label(a_pt, "A")
        pb = _dot_label(b_pt, "B")

        g_pt = a_pt + 0.6 * (b_pt - a_pt)  # AG = (3/5) AB
        pg = _dot_label(g_pt, "G", dot_color="#288073", label_dir=DOWN)

        gp_pt = a_pt + 1.5 * (b_pt - a_pt)  # AG' = (3/2) AB
        pgp = _dot_label(gp_pt, "G'", dot_color="#B42E41", label_dir=DOWN)

        figure = VGroup(axe, pa, pb, pg, pgp)
        figure.scale(0.85).move_to(DOWN * 1.5)

        calcul_g = MathTex(
            r"G = \mathrm{bar}\{(A,2)\,;\,(B,3)\}\ :\ "
            r"\overrightarrow{AG} = \dfrac{3}{5}\,\overrightarrow{AB} \ \Rightarrow\ G \in [AB]",
            font_size=24,
        )
        calcul_gp = MathTex(
            r"G' = \mathrm{bar}\{(A,-1)\,;\,(B,3)\}\ :\ "
            r"\overrightarrow{AG'} = \dfrac{3}{2}\,\overrightarrow{AB} \ \Rightarrow\ G' \notin [AB]",
            font_size=24,
        )
        exemple_content = VGroup(calcul_g, calcul_gp).arrange(DOWN, buff=0.3)
        exemple = example_box(exemple_content)
        exemple.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Application : plaçons G égal au barycentre de A-deux et "
                "B-trois. Les coefficients ont le même signe : G est dans "
                "le segment A-B, avec le vecteur A-G égal à trois "
                "cinquièmes du vecteur A-B, donc plus proche de B, qui a le "
                "plus grand coefficient. Plaçons maintenant G-prime, "
                "barycentre de A moins un et B-trois. Les coefficients "
                "sont de signes contraires : G-prime est à l'extérieur du "
                "segment, du côté de B, avec le vecteur A-G-prime égal à "
                "trois demis du vecteur A-B, donc au-delà de B."
            )
        ) as tracker:
            self.play(FadeIn(exemple))
            self.play(Create(figure))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(exemple), FadeOut(figure))

        # --- À retenir -----------------------------------------------------------
        retenir = property_box(
            VGroup(
                Text("Homogénéité : multiplier α et β par k≠0 ne change pas G.", font_size=22),
                Text("Signe de αβ : détermine si G est dans [AB] ou à l'extérieur.", font_size=22),
            ).arrange(DOWN, buff=0.25),
        )
        retenir.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "À retenir : le barycentre ne dépend que du rapport des "
                "coefficients, pas de leur valeur absolue, grâce à "
                "l'homogénéité ; et le signe du produit alpha bêta indique "
                "immédiatement si G se trouve dans le segment A-B ou à "
                "l'extérieur."
            )
        ) as tracker:
            self.play(FadeIn(retenir))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(retenir))

        # --- Piège à éviter --------------------------------------------------------
        piege = warning_box(
            Text(
                _wrap(
                    "« Plus grand coefficient » signifie plus grande valeur "
                    "absolue, pas plus grand au sens de l'ordre usuel : un "
                    "coefficient -5 est « plus grand en valeur absolue » "
                    "qu'un coefficient 3, même si -5 < 3.",
                    width=48,
                ),
                font_size=23,
            ),
        )
        piege.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Attention au piège classique : quand le tableau parle du "
                "« plus grand coefficient », il s'agit de la plus grande "
                "valeur absolue, et non de l'ordre usuel des nombres. Un "
                "coefficient de moins cinq est plus grand en valeur "
                "absolue qu'un coefficient de trois, même si moins cinq "
                "est inférieur à trois."
            )
        ) as tracker:
            self.play(FadeIn(piege))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(piege), FadeOut(titre))
