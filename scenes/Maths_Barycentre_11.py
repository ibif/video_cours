"""
scenes/Maths_Barycentre_11.py — Chapitre 4 « Barycentre » (1ereC, Maths),
scène 11.

§ Ligne de niveau MA/MB=k (cercle d'Apollonius) : construction (k=1 →
médiatrice, k≠1 → cercle de centre G=bar{(A,1),(B,-k²)}, diamètre [IJ]),
exemple résolu 9 (AB=6, MA=2MB, cercle de centre G rayon 4), mention du
centre d'inertie d'une plaque homogène.
Source : 1ereC/Maths.pdf, chapitre 4, pages 49-50.
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


def _dot_label(point, label, color=WHITE, label_dir=UP, font_size=26, dot_color=YELLOW):
    d = Dot(point, color=dot_color, radius=0.07)
    t = MathTex(label, font_size=font_size, color=color)
    t.next_to(d, label_dir, buff=0.12)
    return VGroup(d, t)


class CercleApollonius(NotionScene):
    def construct(self):
        titre = scene_title("Barycentre — Ligne de niveau MA/MB=k (cercle d'Apollonius)")
        titre.scale(0.4)
        titre.to_edge(UP)

        question = Text(
            _wrap(
                "Quel est l'ensemble des points M du plan tels que "
                "MA = k·MB, pour un réel k > 0 donné ?",
                width=52,
            ),
            font_size=25,
        )
        question.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Dernière ligne de niveau du chapitre : quel est "
                "l'ensemble des points M du plan tels que M-A soit égal à "
                "k fois M-B, pour un réel k strictement positif donné ?"
            )
        ) as tracker:
            self.play(Write(titre))
            self.play(FadeIn(question))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(question))

        # --- Raisonnement : construction ------------------------------------------
        cas_k1 = MathTex(r"k=1 \ :\ MA=MB \ \Rightarrow\ \text{médiatrice de } [AB]", font_size=25)
        cas_k1.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Premier cas, le plus simple : si k égale un, l'équation "
                "devient M-A égale M-B, c'est-à-dire que M est "
                "équidistant de A et de B. L'ensemble cherché est alors "
                "tout simplement la médiatrice du segment A-B."
            )
        ) as tracker:
            self.play(Write(cas_k1))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(cas_k1))

        transformation = MathTex(
            r"MA=k\,MB \ \Leftrightarrow\ MA^2-k^2MB^2=0"
            r"\quad (\text{ligne de niveau } a\,MA^2+b\,MB^2=0,\ a=1,\ b=-k^2)",
            font_size=20,
        )
        transformation.next_to(titre, DOWN, buff=0.4)

        construction = VGroup(
            MathTex(r"k\neq 1 \ \Rightarrow\ a+b=1-k^2\neq 0 \ \Rightarrow\ \text{cercle de centre } G", font_size=22),
            MathTex(r"G = \mathrm{bar}\{(A,1)\,;\,(B,-k^2)\}", font_size=25, color=YELLOW),
            Text("Diamètre [IJ], avec I et J sur la droite (AB) :", font_size=21),
            MathTex(r"I = \mathrm{bar}\{(A,1)\,;\,(B,k)\} \quad (\text{division intérieure : } \tfrac{IA}{IB}=k)", font_size=20),
            MathTex(r"J = \mathrm{bar}\{(A,1)\,;\,(B,-k)\} \quad (\text{division extérieure : } \tfrac{JA}{JB}=k)", font_size=20),
        ).arrange(DOWN, buff=0.28)
        construction.next_to(transformation, DOWN, buff=0.45)

        with self.voiceover(
            text=(
                "Si k est différent de un, on transforme l'équation : M-A "
                "égale k M-B équivaut à M-A au carré, moins k au carré "
                "M-B au carré, égale zéro. On reconnaît la ligne de "
                "niveau étudiée précédemment, avec a égale un et b égale "
                "moins k au carré. Comme a plus b égale un moins k au "
                "carré, non nul puisque k est différent de un, on obtient "
                "un cercle, appelé cercle d'Apollonius, de centre G égal "
                "au barycentre de A-un et B, moins k au carré. Ce cercle "
                "admet pour diamètre le segment I-J, où I et J sont deux "
                "points de la droite A-B : I est le barycentre de A-un et "
                "B-k, le point de division intérieure du segment dans le "
                "rapport k ; J est le barycentre de A-un et B, moins k, le "
                "point de division extérieure dans le même rapport."
            )
        ) as tracker:
            self.play(Write(transformation))
            self.play(FadeIn(construction))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(transformation), FadeOut(construction))

        # --- Exemple traité : exemple résolu 9 -------------------------------------
        enonce_ex9 = MathTex(r"AB=6, \quad \text{ensemble des } M \text{ tels que } MA=2MB \quad (k=2)", font_size=23)
        calcul_i = MathTex(r"I=\mathrm{bar}\{(A,1)\,;\,(B,2)\}: \ AI=\dfrac{2}{3}AB=4", font_size=21)
        calcul_j = MathTex(r"J=\mathrm{bar}\{(A,1)\,;\,(B,-2)\}: \ AJ=\dfrac{-2}{-1}AB=2\times 6=12", font_size=21)
        calcul_g = MathTex(r"G=\text{milieu de }[IJ]: \ AG=\dfrac{4+12}{2}=8, \quad \text{rayon}=\dfrac{12-4}{2}=4", font_size=21)
        resultat_ex9 = Text("Cercle de centre G (à 8 de A sur (AB)) et de rayon 4.", font_size=22, color=YELLOW)
        contenu_ex9 = VGroup(enonce_ex9, calcul_i, calcul_j, calcul_g, resultat_ex9).arrange(DOWN, buff=0.25)
        exemple9 = example_box(contenu_ex9)
        exemple9.next_to(titre, DOWN, buff=0.35)

        with self.voiceover(
            text=(
                "Exemple résolu : A-B égale six, cherchons l'ensemble des "
                "points M tels que M-A égale deux M-B, donc k égale deux. "
                "On place I, barycentre de A-un et B-deux : A-I égale "
                "deux tiers de A-B, soit quatre. On place J, barycentre "
                "de A-un et B, moins deux : A-J égale deux fois A-B, soit "
                "douze, donc J est au-delà de B. G, milieu de I-J, est "
                "alors à la distance huit de A sur la droite A-B, et le "
                "rayon du cercle, la moitié de I-J, vaut quatre. "
                "L'ensemble cherché est donc le cercle de centre G et de "
                "rayon quatre."
            )
        ) as tracker:
            self.play(FadeIn(exemple9))
            self.wait(tracker.get_remaining_duration())

        a_pt = LEFT * 4
        pas = 6 / 8  # 6 unités réelles → 8 unités "manim" d'axe utile (jusqu'à 12)
        b_pt = a_pt + RIGHT * (6 * pas)
        i_pt = a_pt + RIGHT * (4 * pas)
        j_pt = a_pt + RIGHT * (12 * pas)
        g_pt = a_pt + RIGHT * (8 * pas)
        rayon = 4 * pas

        axe = Line(a_pt + LEFT * 0.3, j_pt + RIGHT * 0.3, color=WHITE)
        pa = _dot_label(a_pt, "A", label_dir=UP)
        pb = _dot_label(b_pt, "B", label_dir=UP)
        pi = _dot_label(i_pt, "I", dot_color="#288073", label_dir=DOWN)
        pj = _dot_label(j_pt, "J", dot_color="#288073", label_dir=DOWN)
        pg = _dot_label(g_pt, "G", dot_color="#B42E41", label_dir=UP)
        cercle = Circle(radius=rayon, color="#B42E41").move_to(g_pt)
        figure = VGroup(axe, cercle, pa, pb, pi, pj, pg)
        figure.scale(0.75).next_to(exemple9, DOWN, buff=0.5)

        self.play(Create(figure))
        self.wait(1)
        self.play(FadeOut(exemple9), FadeOut(figure))

        # --- Mention : centre d'inertie -----------------------------------------
        mention = Text(
            _wrap(
                "Remarque interdisciplinaire : en Physique, le barycentre "
                "de points matériels pondérés par leur masse correspond "
                "exactement au centre d'inertie (ou centre de gravité) "
                "d'un système. Pour une plaque homogène (triangle, "
                "rectangle, disque…), les résultats du centre d'inertie "
                "utilisés en Physique — souvent admis dans ce cours — "
                "sont précisément ceux des isobarycentres étudiés ici.",
                width=54,
            ),
            font_size=22,
        )
        mention.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Une dernière remarque, interdisciplinaire : en Physique, "
                "le barycentre de points matériels, pondérés par leur "
                "masse, correspond exactement au centre d'inertie, ou "
                "centre de gravité, d'un système. Pour une plaque "
                "homogène, comme un triangle, un rectangle ou un disque, "
                "les résultats sur le centre d'inertie utilisés en cours "
                "de Physique, souvent admis sans démonstration, sont "
                "précisément ceux des isobarycentres que nous avons "
                "étudiés dans ce chapitre."
            )
        ) as tracker:
            self.play(FadeIn(mention))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(mention))

        # --- À retenir -----------------------------------------------------------
        retenir = VGroup(
            MathTex(r"k=1: \text{médiatrice de } [AB]", font_size=24),
            MathTex(r"k\neq 1: \text{cercle d'Apollonius, centre } G=\mathrm{bar}\{(A,1)\,;\,(B,-k^2)\}, \text{ diamètre } [IJ]", font_size=21),
        ).arrange(DOWN, buff=0.3)
        retenir_box = property_box(retenir)
        retenir_box.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "À retenir : pour k égal un, l'ensemble M-A égale k M-B "
                "est la médiatrice de A-B ; pour k différent de un, "
                "c'est le cercle d'Apollonius, de centre G, barycentre de "
                "A-un et B, moins k au carré, et de diamètre I-J."
            )
        ) as tracker:
            self.play(FadeIn(retenir_box))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(retenir_box))

        # --- Piège à éviter --------------------------------------------------------
        piege = warning_box(
            Text(
                _wrap(
                    "Ne cherchez jamais un « cercle d'Apollonius » pour "
                    "k=1 : ce cas particulier donne une droite (la "
                    "médiatrice), pas un cercle — le barycentre "
                    "bar{(A,1),(B,-k²)} n'existe même pas, car "
                    "1-k²=0.",
                    width=48,
                ),
                font_size=22,
            ),
        )
        piege.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Piège à éviter : ne cherchez jamais un cercle "
                "d'Apollonius pour k égal un. Ce cas particulier donne "
                "une droite, la médiatrice, et non un cercle : d'ailleurs "
                "le barycentre de A-un et B, moins k au carré, n'existe "
                "même pas dans ce cas, puisque un moins k au carré vaut "
                "zéro."
            )
        ) as tracker:
            self.play(FadeIn(piege))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(piege), FadeOut(titre))
