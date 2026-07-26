"""
scenes/Maths_Barycentre_06.py — Chapitre 4 « Barycentre » (1ereC, Maths),
scène 06.

§ Homogénéité (3 points), isobarycentre (définition et cas particuliers :
milieu, centre de gravité, centre d'un parallélogramme), réduction de
αMA⃗+βMB⃗+γMC⃗, coordonnées du barycentre de trois points, exemple résolu 5
(calcul de G(7/3;4/3)).
Source : 1ereC/Maths.pdf, chapitre 4, pages 44-45.
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
    Polygon,
    Text,
    VGroup,
    Write,
)

from shapes.base_scene import NotionScene
from shapes.boxes import definition_box, example_box, property_box, scene_title


def _wrap(text: str, width: int = 54) -> str:
    return "\n".join(textwrap.fill(line, width=width) for line in text.split("\n"))


def _dot_label(point, label, color=WHITE, label_dir=UP, font_size=28, dot_color=YELLOW):
    d = Dot(point, color=dot_color, radius=0.07)
    t = MathTex(label, font_size=font_size, color=color)
    t.next_to(d, label_dir, buff=0.12)
    return VGroup(d, t)


class HomogeneiteIsobarycentreCoordonnees(NotionScene):
    def construct(self):
        titre = scene_title("Barycentre — Homogénéité, isobarycentre, coordonnées")
        titre.scale(0.44)
        titre.to_edge(UP)

        # --- Énoncé ---------------------------------------------------------
        question = Text(
            _wrap(
                "L'homogénéité vue pour deux points reste-t-elle vraie "
                "pour trois points ? Que devient le barycentre quand les "
                "trois coefficients sont égaux ?",
                width=52,
            ),
            font_size=25,
        )
        question.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "L'homogénéité vue pour deux points reste-t-elle vraie "
                "pour trois points ? Et que devient le barycentre lorsque "
                "les trois coefficients sont tous égaux ? Nous complétons "
                "aujourd'hui la boîte à outils du barycentre de trois "
                "points."
            )
        ) as tracker:
            self.play(Write(titre))
            self.play(FadeIn(question))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(question))

        # --- Homogénéité (3 points) -------------------------------------------
        homogeneite = property_box(
            MathTex(
                r"k\in\mathbb{R}^{*} \ \Rightarrow\ \mathrm{bar}\{(A,\alpha)\,;\,(B,\beta)\,;\,(C,\gamma)\}"
                r" = \mathrm{bar}\{(A,k\alpha)\,;\,(B,k\beta)\,;\,(C,k\gamma)\}",
                font_size=22,
            ),
        )
        homogeneite.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Oui : l'homogénéité s'étend sans changement à trois "
                "points. Multiplier les trois coefficients par un même "
                "réel non nul k ne change pas le barycentre G. La "
                "démonstration est identique à celle du cas à deux "
                "points."
            )
        ) as tracker:
            self.play(FadeIn(homogeneite))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(homogeneite))

        # --- Isobarycentre ------------------------------------------------------
        def_isobarycentre = definition_box(
            VGroup(
                Text("Isobarycentre", font_size=25, weight="BOLD"),
                Text(
                    _wrap("Barycentre de points affectés de coefficients tous égaux (et non nuls).", width=46),
                    font_size=22,
                ),
                MathTex(r"\text{2 points : milieu de } [AB]", font_size=23),
                MathTex(r"\text{3 points non alignés : centre de gravité du triangle } ABC", font_size=23),
                MathTex(r"\text{4 sommets d'un parallélogramme : son centre}", font_size=23),
            ).arrange(DOWN, buff=0.22),
        )
        def_isobarycentre.next_to(titre, DOWN, buff=0.35)

        with self.voiceover(
            text=(
                "On appelle isobarycentre le barycentre de points affectés "
                "de coefficients tous égaux, et non nuls. Pour deux "
                "points, c'est le milieu du segment. Pour trois points non "
                "alignés, c'est le centre de gravité du triangle. Et pour "
                "les quatre sommets d'un parallélogramme, c'est son "
                "centre. Grâce à l'homogénéité, peu importe la valeur "
                "commune des coefficients : seul compte le fait qu'ils "
                "soient égaux."
            )
        ) as tracker:
            self.play(FadeIn(def_isobarycentre))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(def_isobarycentre))

        # --- Réduction vectorielle (3 points) -----------------------------------
        reduction = property_box(
            MathTex(
                r"\alpha+\beta+\gamma \neq 0 \ \Rightarrow\ "
                r"\alpha\,\overrightarrow{MA}+\beta\,\overrightarrow{MB}+\gamma\,\overrightarrow{MC} = (\alpha+\beta+\gamma)\,\overrightarrow{MG}",
                font_size=23,
            ),
        )
        reduction.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "La réduction vectorielle se généralise elle aussi : pour "
                "tout point M, alpha M-A plus bêta M-B plus gamma M-C est "
                "égal à alpha plus bêta plus gamma, fois M-G. La "
                "démonstration est identique à celle du cas à deux points : "
                "on fait apparaître G par Chasles dans chaque vecteur, et "
                "le terme alpha G-A plus bêta G-B plus gamma G-C "
                "s'annule, par définition de G."
            )
        ) as tracker:
            self.play(FadeIn(reduction))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(reduction))

        # --- Coordonnées (3 points) ---------------------------------------------
        coord = property_box(
            VGroup(
                Text("Coordonnées du barycentre de trois points pondérés :", font_size=21),
                MathTex(
                    r"x_G = \dfrac{\alpha x_A+\beta x_B+\gamma x_C}{\alpha+\beta+\gamma}, \qquad "
                    r"y_G = \dfrac{\alpha y_A+\beta y_B+\gamma y_C}{\alpha+\beta+\gamma}",
                    font_size=25,
                ),
            ).arrange(DOWN, buff=0.3),
        )
        coord.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Les coordonnées de G s'obtiennent de la même façon, en "
                "ajoutant simplement le troisième point : x-G égale alpha "
                "x-A plus bêta x-B plus gamma x-C, divisé par alpha plus "
                "bêta plus gamma ; et de même pour y-G."
            )
        ) as tracker:
            self.play(FadeIn(coord))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(coord))

        # --- Exemple traité : exemple résolu 5 -----------------------------------
        donnees_ex5 = MathTex(r"A(0\,;\,1), \ B(4\,;\,-1), \ C(2\,;\,3), \ G=\mathrm{bar}\{(A,1)\,;\,(B,2)\,;\,(C,3)\}", font_size=21)
        calcul_x5 = MathTex(r"x_G = \dfrac{1\times 0+2\times 4+3\times 2}{1+2+3} = \dfrac{14}{6} = \dfrac{7}{3}", font_size=24)
        calcul_y5 = MathTex(r"y_G = \dfrac{1\times 1+2\times(-1)+3\times 3}{6} = \dfrac{8}{6} = \dfrac{4}{3}", font_size=24)
        resultat_ex5 = MathTex(r"G\left(\dfrac{7}{3}\,;\,\dfrac{4}{3}\right)", font_size=28, color=YELLOW)
        contenu_ex5 = VGroup(donnees_ex5, calcul_x5, calcul_y5, resultat_ex5).arrange(DOWN, buff=0.3)
        exemple5 = example_box(contenu_ex5)
        exemple5.next_to(titre, DOWN, buff=0.35)

        with self.voiceover(
            text=(
                "Exemple résolu : A de coordonnées zéro et un, B de "
                "coordonnées quatre et moins un, C de coordonnées deux et "
                "trois, et G égal au barycentre de A-un, B-deux, C-trois. "
                "On calcule x-G : un fois zéro, plus deux fois quatre, "
                "plus trois fois deux, divisé par un plus deux plus trois, "
                "soit quatorze sixièmes, c'est-à-dire sept tiers. De même, "
                "y-G égale un, moins deux, plus neuf, divisé par six, soit "
                "huit sixièmes, c'est-à-dire quatre tiers. On obtient G de "
                "coordonnées sept tiers et quatre tiers."
            )
        ) as tracker:
            self.play(FadeIn(exemple5))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(exemple5))

        # --- À retenir -----------------------------------------------------------
        retenir = definition_box(
            VGroup(
                Text("Isobarycentre = coefficients égaux (milieu, centre de gravité, centre de parallélogramme).", font_size=20),
                MathTex(r"x_G = \dfrac{\alpha x_A+\beta x_B+\gamma x_C}{\alpha+\beta+\gamma}", font_size=23),
            ).arrange(DOWN, buff=0.3),
        )
        retenir.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "À retenir : l'isobarycentre correspond à des coefficients "
                "égaux — milieu, centre de gravité, centre d'un "
                "parallélogramme — et les coordonnées du barycentre "
                "s'obtiennent toujours par une moyenne pondérée, "
                "coordonnée par coordonnée."
            )
        ) as tracker:
            self.play(FadeIn(retenir))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(retenir))

        # --- Piège à éviter (illustré, pas de warning_box supplémentaire ici) ---
        illustration = Polygon(LEFT * 2 + DOWN, RIGHT * 2 + DOWN, DOWN * 1 + UP * 1.6, color="#288073")
        centre_gravite = _dot_label(illustration.get_center_of_mass(), "G", dot_color="#288073", label_dir=DOWN)
        figure_finale = VGroup(illustration, centre_gravite)
        figure_finale.next_to(titre, DOWN, buff=0.6)

        with self.voiceover(
            text=(
                "Attention à ne pas confondre isobarycentre et milieu d'un "
                "côté : pour un triangle, l'isobarycentre — le centre de "
                "gravité — n'est pas le milieu d'un côté, mais un point "
                "intérieur situé aux deux tiers de chaque médiane, comme "
                "nous le démontrerons bientôt."
            )
        ) as tracker:
            self.play(Create(figure_finale))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(figure_finale), FadeOut(titre))
