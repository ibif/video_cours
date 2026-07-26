"""
scenes/Maths_Barycentre_07.py — Chapitre 4 « Barycentre » (1ereC, Maths),
scène 07.

§ Théorème des barycentres partiels (associativité) avec démonstration,
point méthode, exemple résolu 6 (G=bar{(A,3),(B,-2),(C,1)} via le
barycentre partiel H=bar{(A,3),(B,-2)}, G milieu de [HC]).
Source : 1ereC/Maths.pdf, chapitre 4, page 45.
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
from shapes.boxes import example_box, method_box, scene_title, theorem_box, warning_box


def _wrap(text: str, width: int = 54) -> str:
    return "\n".join(textwrap.fill(line, width=width) for line in text.split("\n"))


def _dot_label(point, label, color=WHITE, label_dir=UP, font_size=28, dot_color=YELLOW):
    d = Dot(point, color=dot_color, radius=0.07)
    t = MathTex(label, font_size=font_size, color=color)
    t.next_to(d, label_dir, buff=0.12)
    return VGroup(d, t)


class BarycentresPartiels(NotionScene):
    def construct(self):
        titre = scene_title("Barycentre — Théorème des barycentres partiels")
        titre.scale(0.46)
        titre.to_edge(UP)

        # --- Énoncé ---------------------------------------------------------
        question = Text(
            _wrap(
                "Peut-on remplacer deux des trois points par leur "
                "barycentre, pour simplifier le calcul d'un barycentre à "
                "trois points ?",
                width=52,
            ),
            font_size=26,
        )
        question.next_to(titre, DOWN, buff=0.6)

        with self.voiceover(
            text=(
                "Une question pratique se pose : peut-on remplacer deux "
                "des trois points par leur barycentre, pour simplifier le "
                "calcul d'un barycentre à trois points ? La réponse est "
                "oui, c'est l'associativité du barycentre."
            )
        ) as tracker:
            self.play(Write(titre))
            self.play(FadeIn(question))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(question))

        # --- Raisonnement : théorème + démonstration -------------------------
        enonce = VGroup(
            MathTex(r"G = \mathrm{bar}\{(A,\alpha)\,;\,(B,\beta)\,;\,(C,\gamma)\}, \quad \alpha+\beta\neq 0", font_size=23),
            MathTex(r"H = \mathrm{bar}\{(A,\alpha)\,;\,(B,\beta)\} \ \Rightarrow\ G = \mathrm{bar}\{(H,\alpha+\beta)\,;\,(C,\gamma)\}", font_size=23),
        ).arrange(DOWN, buff=0.3)
        theoreme = theorem_box(enonce)
        theoreme.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Voici le théorème des barycentres partiels. Soit G le "
                "barycentre de A-alpha, B-bêta et C-gamma, avec alpha plus "
                "bêta non nul. Si H est le barycentre partiel de A-alpha "
                "et B-bêta, alors G est aussi le barycentre de H, affecté "
                "de la somme alpha plus bêta, et de C-gamma. On dit qu'on "
                "a remplacé A et B par leur barycentre partiel H, muni de "
                "la somme de leurs coefficients."
            )
        ) as tracker:
            self.play(FadeIn(theoreme))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(theoreme))

        demo = VGroup(
            MathTex(r"\overrightarrow{GA}=\overrightarrow{GH}+\overrightarrow{HA}, \quad \overrightarrow{GB}=\overrightarrow{GH}+\overrightarrow{HB}", font_size=23),
            MathTex(
                r"\alpha\,\overrightarrow{GA}+\beta\,\overrightarrow{GB}+\gamma\,\overrightarrow{GC} "
                r"= (\alpha+\beta)\,\overrightarrow{GH} + \underbrace{(\alpha\,\overrightarrow{HA}+\beta\,\overrightarrow{HB})}_{=\ \vec{0}\ (\text{déf. de }H)} + \gamma\,\overrightarrow{GC}",
                font_size=21,
            ),
            MathTex(r"(\alpha+\beta)\,\overrightarrow{GH}+\gamma\,\overrightarrow{GC} = \vec{0}", font_size=25, color=YELLOW),
            Text("Cette relation caractérise exactement G = bar{(H,α+β) ; (C,γ)} : c.q.f.d.", font_size=21),
        ).arrange(DOWN, buff=0.3)
        demo.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Démontrons ce résultat. Par définition de G, alpha G-A "
                "plus bêta G-B plus gamma G-C est nul. On fait apparaître "
                "H dans les deux premiers vecteurs par Chasles. Le terme "
                "alpha H-A plus bêta H-B s'annule, précisément parce que H "
                "est le barycentre de A-alpha et B-bêta. Il reste alpha "
                "plus bêta, fois G-H, plus gamma G-C, égale le vecteur "
                "nul. Cette relation est exactement celle qui caractérise "
                "G comme barycentre de H, affecté de alpha plus bêta, et "
                "de C-gamma : c'est ce qu'il fallait démontrer."
            )
        ) as tracker:
            self.play(Write(demo))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(demo))

        methode = method_box(
            VGroup(
                Text("Point méthode : associativité", font_size=23, weight="BOLD"),
                Text(
                    _wrap(
                        "1. Choisir deux des trois points dont la somme des "
                        "coefficients est non nulle. 2. Calculer leur "
                        "barycentre partiel H. 3. Le barycentre cherché G "
                        "devient le barycentre de seulement DEUX points : "
                        "H (affecté de la somme) et le troisième point.",
                        width=44,
                    ),
                    font_size=21,
                ),
            ).arrange(DOWN, buff=0.25),
        )
        methode.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Voici la méthode à retenir : on choisit deux des trois "
                "points dont la somme des coefficients est non nulle, on "
                "calcule leur barycentre partiel H, puis on ramène le "
                "problème initial, à trois points, à un problème à deux "
                "points seulement : H, affecté de la somme des "
                "coefficients, et le troisième point."
            )
        ) as tracker:
            self.play(FadeIn(methode))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(methode))

        # --- Exemple traité : exemple résolu 6 -----------------------------------
        donnees_ex6 = MathTex(r"G = \mathrm{bar}\{(A,3)\,;\,(B,-2)\,;\,(C,1)\}", font_size=26)
        etape_h = MathTex(r"H = \mathrm{bar}\{(A,3)\,;\,(B,-2)\} \quad (\text{coefficient partiel } 3-2=1)", font_size=23)
        etape_g = MathTex(r"G = \mathrm{bar}\{(H,1)\,;\,(C,1)\}", font_size=25)
        conclusion_ex6 = Text("Coefficients égaux (1 ; 1) : G est le milieu de [HC].", font_size=23, color=YELLOW)
        contenu_ex6 = VGroup(donnees_ex6, etape_h, etape_g, conclusion_ex6).arrange(DOWN, buff=0.3)
        exemple6 = example_box(contenu_ex6)
        exemple6.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Reprenons G égal au barycentre de A-trois, B-moins deux "
                "et C-un, déjà construit dans une scène précédente. "
                "Posons H égal au barycentre partiel de A-trois et "
                "B-moins deux, de coefficient total trois moins deux, "
                "c'est-à-dire un. Alors G est le barycentre de H-un et "
                "C-un : les deux coefficients sont égaux, donc G est tout "
                "simplement le milieu du segment H-C. L'associativité "
                "transforme ainsi un calcul à trois points en un simple "
                "milieu."
            )
        ) as tracker:
            self.play(FadeIn(exemple6))
            self.wait(tracker.get_remaining_duration())

        h_pt = LEFT * 2.5
        c_pt = RIGHT * 2.5
        g_pt = (h_pt + c_pt) / 2
        ph = _dot_label(h_pt, "H", dot_color="#A42A5A")
        pc = _dot_label(c_pt, "C")
        pg = _dot_label(g_pt, "G", dot_color="#288073", label_dir=DOWN)
        segment = Line(h_pt, c_pt, color=WHITE)
        figure = VGroup(segment, ph, pc, pg)
        figure.next_to(exemple6, DOWN, buff=0.5)

        self.play(Create(figure))
        self.wait(1)
        self.play(FadeOut(exemple6), FadeOut(figure))

        # --- À retenir -----------------------------------------------------------
        retenir = theorem_box(
            MathTex(
                r"G = \mathrm{bar}\{(A,\alpha)\,;\,(B,\beta)\,;\,(C,\gamma)\} = \mathrm{bar}\{(H,\alpha+\beta)\,;\,(C,\gamma)\}",
                font_size=24,
            ),
        )
        retenir.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "À retenir : l'associativité permet de remplacer deux "
                "points d'un barycentre par leur barycentre partiel, "
                "affecté de la somme de leurs coefficients, sans changer "
                "le résultat final."
            )
        ) as tracker:
            self.play(FadeIn(retenir))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(retenir))

        # --- Piège à éviter ------------------------------------------------------
        piege = warning_box(
            Text(
                _wrap(
                    "Le regroupement partiel n'est licite que si la somme "
                    "des coefficients regroupés est non nulle. Vérifiez "
                    "toujours α+β≠0 avant de remplacer A et B par H.",
                    width=48,
                ),
                font_size=23,
            ),
        )
        piege.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Piège classique : le regroupement partiel n'est licite "
                "que si la somme des coefficients regroupés est non "
                "nulle. Vérifiez toujours que alpha plus bêta est non nul "
                "avant de remplacer A et B par leur barycentre partiel H, "
                "sous peine d'introduire un point qui n'existe pas."
            )
        ) as tracker:
            self.play(FadeIn(piege))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(piege), FadeOut(titre))
