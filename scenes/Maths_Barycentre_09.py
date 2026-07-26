"""
scenes/Maths_Barycentre_09.py — Chapitre 4 « Barycentre » (1ereC, Maths),
scène 09.

§ Méthode pour démontrer un alignement (exemple résolu 7 : I, J, K alignés
via K=bar{(I,-3),(J,4)}) et méthode pour démontrer un concours de droites
(exemple résolu 8 : concours de (AJ), (BK), (CI) en G).
Source : 1ereC/Maths.pdf, chapitre 4, pages 47-48.
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
from shapes.boxes import example_box, method_box, scene_title, warning_box


def _wrap(text: str, width: int = 54) -> str:
    return "\n".join(textwrap.fill(line, width=width) for line in text.split("\n"))


def _dot_label(point, label, color=WHITE, label_dir=UP, font_size=26, dot_color=YELLOW):
    d = Dot(point, color=dot_color, radius=0.07)
    t = MathTex(label, font_size=font_size, color=color)
    t.next_to(d, label_dir, buff=0.12)
    return VGroup(d, t)


class AlignementEtConcours(NotionScene):
    def construct(self):
        titre = scene_title("Barycentre — Démontrer alignement et concours")
        titre.scale(0.46)
        titre.to_edge(UP)

        question = Text(
            _wrap(
                "Le barycentre est un outil puissant pour démontrer que "
                "des points sont alignés, ou que des droites sont "
                "concourantes.",
                width=52,
            ),
            font_size=25,
        )
        question.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Le barycentre est un outil très puissant en géométrie : "
                "il permet de démontrer facilement que des points sont "
                "alignés, ou que plusieurs droites sont concourantes. "
                "Voyons les deux méthodes."
            )
        ) as tracker:
            self.play(Write(titre))
            self.play(FadeIn(question))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(question))

        # --- Méthode : alignement -----------------------------------------------
        methode_alignement = method_box(
            VGroup(
                Text("Démontrer un alignement", font_size=23, weight="BOLD"),
                Text(
                    _wrap(
                        "Pour montrer que I, J, K sont alignés : écrire K "
                        "comme barycentre de I et J (coefficients x, y "
                        "avec x+y≠0). Un barycentre de deux points "
                        "appartient toujours à leur droite (théorème vu "
                        "précédemment) : donc K∈(IJ), donc I, J, K sont "
                        "alignés.",
                        width=46,
                    ),
                    font_size=20,
                ),
            ).arrange(DOWN, buff=0.25),
        )
        methode_alignement.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Pour démontrer que trois points I, J et K sont alignés, "
                "la méthode consiste à écrire K comme barycentre de I et "
                "de J, avec des coefficients x et y de somme non nulle. "
                "Or, nous avons démontré qu'un barycentre de deux points "
                "appartient toujours à la droite définie par ces deux "
                "points : K appartient donc à la droite I-J, ce qui "
                "prouve que les trois points sont alignés."
            )
        ) as tracker:
            self.play(FadeIn(methode_alignement))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(methode_alignement))

        # --- Exemple résolu 7 -----------------------------------------------------
        donnees7 = MathTex(
            r"I=\mathrm{bar}\{(A,2)\,;\,(B,1)\}, \ J=\mathrm{bar}\{(A,1)\,;\,(C,1)\}, \ K=\mathrm{bar}\{(B,-1)\,;\,(C,2)\}",
            font_size=20,
        )
        systeme7 = VGroup(
            Text("On cherche x, y tels que K = bar{(I,x) ; (J,y)}.", font_size=20),
            Text("En développant I et J sur A, B, C et en identifiant :", font_size=20),
            MathTex(r"2x+y=0, \quad x=-1t,\quad y=2t \ \Rightarrow\ x=-3,\ y=4 \ (t=3)", font_size=21),
        ).arrange(DOWN, buff=0.2)
        conclusion7 = MathTex(r"K = \mathrm{bar}\{(I,-3)\,;\,(J,4)\} \ \Rightarrow\ K \in (IJ) \ \Rightarrow\ I,J,K \text{ alignés}", font_size=21, color=YELLOW)
        contenu7 = VGroup(donnees7, systeme7, conclusion7).arrange(DOWN, buff=0.3)
        exemple7 = example_box(contenu7)
        exemple7.next_to(titre, DOWN, buff=0.35)

        with self.voiceover(
            text=(
                "Exemple résolu : soit I le barycentre de A-deux et B-un, "
                "J le barycentre de A-un et C-un, et K le barycentre de "
                "B-moins un et C-deux. Démontrons que I, J et K sont "
                "alignés. On cherche des réels x et y tels que K soit le "
                "barycentre de I-x et J-y. En développant I et J en "
                "fonction de A, B et C, puis en identifiant les "
                "coefficients de A, de B et de C, on obtient, par cette "
                "méthode d'élimination, x égale moins trois et y égale "
                "quatre. On vérifie que x plus y égale un, non nul. K est "
                "donc bien le barycentre de I-moins trois et J-quatre, "
                "donc K appartient à la droite I-J : les trois points I, "
                "J et K sont alignés."
            )
        ) as tracker:
            self.play(FadeIn(exemple7))
            self.wait(tracker.get_remaining_duration())

        a_pt = LEFT * 3.5 + UP * 1.3
        b_pt = LEFT * 3.5 + DOWN * 1.3
        c_pt = LEFT * 0.3 + DOWN * 0.2
        i_pt = a_pt + (1 / 3) * (b_pt - a_pt)
        j_pt = a_pt + 0.5 * (c_pt - a_pt)
        k_pt = i_pt + (4 / (-3 + 4)) * (j_pt - i_pt)

        pa = _dot_label(a_pt, "A")
        pb = _dot_label(b_pt, "B", label_dir=DOWN)
        pc = _dot_label(c_pt, "C", label_dir=RIGHT)
        pi = _dot_label(i_pt, "I", dot_color="#288073", label_dir=LEFT)
        pj = _dot_label(j_pt, "J", dot_color="#288073", label_dir=UP)
        pk = _dot_label(k_pt, "K", dot_color="#B42E41", label_dir=RIGHT)
        droite_ijk = Line(i_pt + (i_pt - k_pt) * 0.3, k_pt + (k_pt - i_pt) * 0.3, color="#288073")
        figure7 = VGroup(Line(a_pt, b_pt), Line(b_pt, c_pt), Line(c_pt, a_pt), droite_ijk, pa, pb, pc, pi, pj, pk)
        figure7.scale(0.75).next_to(exemple7, DOWN, buff=0.4)

        self.play(Create(figure7))
        self.wait(1)
        self.play(FadeOut(exemple7), FadeOut(figure7))

        # --- Méthode : concours ---------------------------------------------------
        methode_concours = method_box(
            VGroup(
                Text("Démontrer un concours de droites", font_size=23, weight="BOLD"),
                Text(
                    _wrap(
                        "Pour montrer que trois droites concourent : "
                        "trouver un barycentre G de trois points, tel que "
                        "chacune des trois droites contienne G après un "
                        "regroupement partiel différent des coefficients "
                        "(associativité). G appartient donc aux trois "
                        "droites à la fois.",
                        width=46,
                    ),
                    font_size=20,
                ),
            ).arrange(DOWN, buff=0.25),
        )
        methode_concours.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Pour démontrer que trois droites sont concourantes, la "
                "méthode consiste à trouver un même barycentre G de trois "
                "points, tel que chacune des trois droites contienne G, "
                "en regroupant les coefficients deux par deux, de trois "
                "façons différentes, grâce à l'associativité. G "
                "appartient alors simultanément aux trois droites."
            )
        ) as tracker:
            self.play(FadeIn(methode_concours))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(methode_concours))

        # --- Exemple résolu 8 -----------------------------------------------------
        donnees8 = MathTex(
            r"I=\mathrm{bar}\{(A,2)\,;\,(B,3)\}, \ J=\mathrm{bar}\{(B,3)\,;\,(C,1)\}, \ K=\mathrm{bar}\{(C,1)\,;\,(A,2)\}",
            font_size=20,
        )
        g_def8 = MathTex(r"G = \mathrm{bar}\{(A,2)\,;\,(B,3)\,;\,(C,1)\}", font_size=24)
        regroup8 = VGroup(
            MathTex(r"G=\mathrm{bar}\{(I,5)\,;\,(C,1)\} \Rightarrow G\in(CI)", font_size=20),
            MathTex(r"G=\mathrm{bar}\{(A,2)\,;\,(J,4)\} \Rightarrow G\in(AJ)", font_size=20),
            MathTex(r"G=\mathrm{bar}\{(B,3)\,;\,(K,3)\} \Rightarrow G\in(BK)", font_size=20),
        ).arrange(DOWN, buff=0.15)
        conclusion8 = Text("(AJ), (BK), (CI) sont concourantes en G.", font_size=22, color=YELLOW)
        contenu8 = VGroup(donnees8, g_def8, regroup8, conclusion8).arrange(DOWN, buff=0.28)
        exemple8 = example_box(contenu8)
        exemple8.next_to(titre, DOWN, buff=0.3)

        with self.voiceover(
            text=(
                "Exemple résolu : soit I le barycentre de A-deux et "
                "B-trois, J le barycentre de B-trois et C-un, et K le "
                "barycentre de C-un et A-deux. Démontrons que les droites "
                "A-J, B-K et C-I sont concourantes. Considérons G, le "
                "barycentre de A-deux, B-trois et C-un. En regroupant A "
                "et B, G est le barycentre de I-cinq et C-un, donc G "
                "appartient à la droite C-I. En regroupant B et C, G est "
                "le barycentre de A-deux et J-quatre, donc G appartient à "
                "la droite A-J. Enfin, en regroupant C et A, G est le "
                "barycentre de B-trois et K-trois, donc G appartient à la "
                "droite B-K. Le même point G appartenant aux trois "
                "droites, celles-ci sont concourantes en G."
            )
        ) as tracker:
            self.play(FadeIn(exemple8))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(exemple8))

        # --- À retenir -----------------------------------------------------------
        retenir = method_box(
            VGroup(
                Text("Alignement : exprimer un point comme barycentre des deux autres.", font_size=20),
                Text("Concours : regrouper un même barycentre à 3 points de 3 façons différentes.", font_size=20),
            ).arrange(DOWN, buff=0.2),
        )
        retenir.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "À retenir : pour un alignement, on exprime un point "
                "comme barycentre des deux autres ; pour un concours, on "
                "regroupe un même barycentre à trois points de trois "
                "façons différentes."
            )
        ) as tracker:
            self.play(FadeIn(retenir))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(retenir))

        # --- Piège à éviter ------------------------------------------------------
        piege = warning_box(
            Text(
                _wrap(
                    "Avant chaque regroupement partiel, vérifiez que la "
                    "somme des deux coefficients regroupés est non nulle "
                    "— sinon le point partiel (I, J ou K selon le cas) "
                    "n'existe pas, et tout le raisonnement s'effondre.",
                    width=48,
                ),
                font_size=22,
            ),
        )
        piege.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Piège à éviter : avant chaque regroupement partiel, "
                "vérifiez que la somme des deux coefficients regroupés "
                "est non nulle. Sinon, le point partiel n'existe pas, et "
                "tout le raisonnement d'alignement ou de concours "
                "s'effondre."
            )
        ) as tracker:
            self.play(FadeIn(piege))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(piege), FadeOut(titre))
