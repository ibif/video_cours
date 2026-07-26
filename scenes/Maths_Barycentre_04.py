"""
scenes/Maths_Barycentre_04.py — Chapitre 4 « Barycentre » (1ereC, Maths),
scène 04.

§ Réduction de αMA⃗+βMB⃗ (avec démonstration), exemple résolu 2 (réduction
et ligne de niveau ‖2MA⃗+3MB⃗‖=10), coordonnées du barycentre de deux points
(avec démonstration), exemple résolu 3 (calcul de G(-3;6)), conservation
par projection.
Source : 1ereC/Maths.pdf, chapitre 4, pages 43-44.
"""

import textwrap

from manim import (
    DOWN,
    LEFT,
    RIGHT,
    UP,
    WHITE,
    YELLOW,
    Circle,
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


def _dot_label(point, label, color=WHITE, label_dir=UP, font_size=28, dot_color=YELLOW):
    d = Dot(point, color=dot_color, radius=0.07)
    t = MathTex(label, font_size=font_size, color=color)
    t.next_to(d, label_dir, buff=0.12)
    return VGroup(d, t)


class ReductionVectorielleEtCoordonnees(NotionScene):
    def construct(self):
        titre = scene_title("Barycentre — Réduction vectorielle et coordonnées")
        titre.scale(0.46)
        titre.to_edge(UP)

        # --- Énoncé ---------------------------------------------------------
        question = Text(
            _wrap(
                "Pour un point M quelconque du plan, peut-on simplifier "
                "l'écriture α MA⃗ + β MB⃗ ? Et comment calculer les "
                "coordonnées du barycentre G ?",
                width=52,
            ),
            font_size=25,
        )
        question.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Nouvelle question : pour un point M quelconque du plan, "
                "peut-on simplifier l'écriture alpha M-A plus bêta M-B ? Et "
                "comment calculer concrètement les coordonnées du "
                "barycentre G ?"
            )
        ) as tracker:
            self.play(Write(titre))
            self.play(FadeIn(question))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(question))

        # --- Raisonnement : réduction vectorielle ----------------------------
        enonce_reduction = VGroup(
            MathTex(
                r"\alpha+\beta \neq 0 \ \Rightarrow\ \alpha\,\overrightarrow{MA}+\beta\,\overrightarrow{MB} "
                r"= (\alpha+\beta)\,\overrightarrow{MG}, \quad G=\mathrm{bar}\{(A,\alpha)\,;\,(B,\beta)\}",
                font_size=23,
            ),
            MathTex(
                r"\alpha+\beta = 0 \ \Rightarrow\ \alpha\,\overrightarrow{MA}+\beta\,\overrightarrow{MB} "
                r"= \alpha\,\overrightarrow{BA} \quad (\text{vecteur constant})",
                font_size=23,
            ),
        ).arrange(DOWN, buff=0.3)
        reduction = property_box(enonce_reduction)
        reduction.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Voici la propriété de réduction. Si alpha plus bêta est "
                "non nul, alors pour tout point M, alpha M-A plus bêta M-B "
                "est égal à alpha plus bêta, fois le vecteur M-G, où G est "
                "le barycentre de A-alpha et B-bêta : la somme se réduit à "
                "un seul vecteur. Si au contraire alpha plus bêta est nul, "
                "la somme est un vecteur constant, indépendant de M, égal "
                "à alpha fois le vecteur B-A."
            )
        ) as tracker:
            self.play(FadeIn(reduction))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(reduction))

        demo = VGroup(
            MathTex(r"\overrightarrow{MA} = \overrightarrow{MG}+\overrightarrow{GA}, \quad \overrightarrow{MB} = \overrightarrow{MG}+\overrightarrow{GB}", font_size=25),
            MathTex(
                r"\alpha\,\overrightarrow{MA}+\beta\,\overrightarrow{MB} = (\alpha+\beta)\,\overrightarrow{MG} "
                r"+ \underbrace{\big(\alpha\,\overrightarrow{GA}+\beta\,\overrightarrow{GB}\big)}_{=\ \vec{0}\ (\text{déf. de } G)}",
                font_size=25,
            ),
            MathTex(r"\alpha\,\overrightarrow{MA}+\beta\,\overrightarrow{MB} = (\alpha+\beta)\,\overrightarrow{MG}", font_size=27, color=YELLOW),
        ).arrange(DOWN, buff=0.35)
        demo.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Démonstration : on fait apparaître G grâce à la relation "
                "de Chasles dans chacun des deux vecteurs M-A et M-B. En "
                "développant, on obtient alpha plus bêta, fois M-G, plus "
                "le terme alpha G-A plus bêta G-B, qui est nul par "
                "définition même de G. Il reste donc bien alpha M-A plus "
                "bêta M-B égale alpha plus bêta, fois M-G."
            )
        ) as tracker:
            self.play(Write(demo))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(demo))

        # --- Exemple traité : exemple résolu 2 -------------------------------
        reduction_ex2 = MathTex(
            r"2\,\overrightarrow{MA}+3\,\overrightarrow{MB} = 5\,\overrightarrow{MG}, \quad G=\mathrm{bar}\{(A,2)\,;\,(B,3)\}",
            font_size=27,
        )
        ligne_niveau_ex2 = MathTex(
            r"\lVert 2\,\overrightarrow{MA}+3\,\overrightarrow{MB} \rVert = 10"
            r"\ \Leftrightarrow\ \lVert 5\,\overrightarrow{MG}\rVert = 10 \ \Leftrightarrow\ MG = 2",
            font_size=25,
        )
        conclusion_ex2 = Text("Ensemble cherché : le cercle de centre G et de rayon 2.", font_size=24, color=YELLOW)
        contenu_ex2 = VGroup(reduction_ex2, ligne_niveau_ex2, conclusion_ex2).arrange(DOWN, buff=0.35)
        exemple2 = example_box(contenu_ex2)
        exemple2.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Exemple résolu : réduisons deux M-A plus trois M-B. Comme "
                "deux plus trois égale cinq, non nul, cette somme vaut cinq "
                "M-G, où G est le barycentre de A-deux et B-trois. "
                "Cherchons maintenant l'ensemble des points M tels que la "
                "norme de deux M-A plus trois M-B vaille dix. Cela revient "
                "à norme de cinq M-G égale dix, donc M-G égale deux : "
                "l'ensemble cherché est le cercle de centre G et de rayon "
                "deux."
            )
        ) as tracker:
            self.play(FadeIn(exemple2))
            self.wait(tracker.get_remaining_duration())

        g_pt = LEFT * 1
        cercle = Circle(radius=1.3, color="#288073").move_to(g_pt)
        pg = _dot_label(g_pt, "G", dot_color="#288073", label_dir=UP)
        figure2 = VGroup(cercle, pg)
        figure2.next_to(exemple2, DOWN, buff=0.5)

        self.play(Create(figure2))
        self.wait(1)
        self.play(FadeOut(exemple2), FadeOut(figure2))

        # --- Coordonnées du barycentre (2 points) ----------------------------
        enonce_coord = VGroup(
            Text("Coordonnées du barycentre de deux points pondérés :", font_size=22),
            MathTex(
                r"x_G = \dfrac{\alpha x_A + \beta x_B}{\alpha+\beta}, \qquad "
                r"y_G = \dfrac{\alpha y_A + \beta y_B}{\alpha+\beta}",
                font_size=27,
            ),
        ).arrange(DOWN, buff=0.3)
        coord_box = property_box(enonce_coord)
        coord_box.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Passons aux coordonnées. Dans un repère du plan, les "
                "coordonnées de G sont : x-G égale alpha x-A plus bêta "
                "x-B, le tout divisé par alpha plus bêta ; et de même pour "
                "y-G, avec les ordonnées y-A et y-B."
            )
        ) as tracker:
            self.play(FadeIn(coord_box))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(coord_box))

        demo_coord = MathTex(
            r"\overrightarrow{AG} = \dfrac{\beta}{\alpha+\beta}\,\overrightarrow{AB}"
            r"\ \Rightarrow\ x_G - x_A = \dfrac{\beta}{\alpha+\beta}(x_B-x_A)"
            r"\ \Rightarrow\ x_G = \dfrac{\alpha x_A+\beta x_B}{\alpha+\beta}",
            font_size=22,
        )
        demo_coord.next_to(titre, DOWN, buff=0.6)

        with self.voiceover(
            text=(
                "La démonstration découle directement de la formule A-G "
                "égale bêta sur alpha plus bêta, fois A-B, appliquée à "
                "l'abscisse : x-G moins x-A égale bêta sur alpha plus "
                "bêta, fois x-B moins x-A. En développant et en "
                "simplifiant, on retrouve exactement la formule annoncée. "
                "Le même raisonnement s'applique à l'ordonnée y-G."
            )
        ) as tracker:
            self.play(Write(demo_coord))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(demo_coord))

        # --- Exemple résolu 3 -----------------------------------------------
        donnees_ex3 = MathTex(r"A(2\,;\,1), \quad B(-1\,;\,4), \quad G = \mathrm{bar}\{(A,-2)\,;\,(B,5)\}", font_size=24)
        calcul_x = MathTex(r"x_G = \dfrac{(-2)\times 2 + 5\times(-1)}{-2+5} = \dfrac{-4-5}{3} = -3", font_size=24)
        calcul_y = MathTex(r"y_G = \dfrac{(-2)\times 1 + 5\times 4}{-2+5} = \dfrac{-2+20}{3} = 6", font_size=24)
        resultat_ex3 = MathTex(r"G(-3\,;\,6)", font_size=28, color=YELLOW)
        contenu_ex3 = VGroup(donnees_ex3, calcul_x, calcul_y, resultat_ex3).arrange(DOWN, buff=0.3)
        exemple3 = example_box(contenu_ex3)
        exemple3.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Exemple résolu : soit A de coordonnées deux et un, B de "
                "coordonnées moins un et quatre, et G égal au barycentre "
                "de A moins deux et B cinq. On calcule x-G : moins deux "
                "fois deux, plus cinq fois moins un, le tout divisé par "
                "moins deux plus cinq, soit moins neuf sur trois, égale "
                "moins trois. De même, y-G égale moins deux fois un, plus "
                "cinq fois quatre, divisé par trois, soit dix-huit sur "
                "trois, égale six. On obtient G de coordonnées moins trois "
                "et six."
            )
        ) as tracker:
            self.play(FadeIn(exemple3))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(exemple3))

        # --- Conservation par projection --------------------------------------
        mention_projection = Text(
            _wrap(
                "Le barycentre est conservé par projection : la projetée "
                "sur une droite (ou un axe) du barycentre de points "
                "pondérés est le barycentre des projetées de ces points, "
                "affectées des mêmes coefficients. C'est ce résultat qui "
                "justifie le calcul séparé de xG puis de yG.",
                width=52,
            ),
            font_size=23,
        )
        mention_projection.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Un dernier point important : le barycentre est conservé "
                "par projection. La projetée, sur une droite ou sur un "
                "axe, du barycentre de points pondérés, est le barycentre "
                "des projetées de ces points, avec les mêmes coefficients. "
                "C'est précisément ce résultat qui justifie de calculer "
                "x-G, puis y-G, séparément, axe par axe."
            )
        ) as tracker:
            self.play(FadeIn(mention_projection))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(mention_projection))

        # --- À retenir -----------------------------------------------------------
        retenir = property_box(
            VGroup(
                MathTex(r"\alpha\,\overrightarrow{MA}+\beta\,\overrightarrow{MB} = (\alpha+\beta)\,\overrightarrow{MG}", font_size=25),
                MathTex(r"x_G = \dfrac{\alpha x_A+\beta x_B}{\alpha+\beta}, \quad y_G = \dfrac{\alpha y_A+\beta y_B}{\alpha+\beta}", font_size=25),
            ).arrange(DOWN, buff=0.3),
        )
        retenir.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "À retenir : la réduction vectorielle transforme une "
                "somme de deux vecteurs en un seul vecteur M-G, et les "
                "coordonnées de G s'obtiennent par la moyenne pondérée des "
                "coordonnées de A et B."
            )
        ) as tracker:
            self.play(FadeIn(retenir))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(retenir))

        # --- Piège à éviter ------------------------------------------------------
        piege = warning_box(
            Text(
                _wrap(
                    "La formule de réduction (α+β) MG⃗ ne s'applique que "
                    "si α+β≠0 : vérifiez toujours cette condition avant de "
                    "l'utiliser, sinon utilisez le vecteur constant "
                    "α BA⃗.",
                    width=48,
                ),
                font_size=23,
            ),
        )
        piege.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Attention : la formule de réduction avec le point G ne "
                "s'applique que si alpha plus bêta est non nul. Vérifiez "
                "toujours cette condition avant de l'utiliser ; dans le "
                "cas contraire, c'est le vecteur constant alpha B-A qu'il "
                "faut utiliser."
            )
        ) as tracker:
            self.play(FadeIn(piege))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(piege), FadeOut(titre))
