"""
scenes/Maths_ComposeesTransformationsPlan_05.py — Chapitre 8 « Composées de
transformations du plan » (1ereC, Maths), scène 05.

§ Composée de deux translations : tv⃗∘tu⃗ = tu⃗+v⃗ (translation, commutative),
démonstration par la relation de Chasles, exemple traité.
Source : 1ereC/Maths.pdf, chapitre 8, page 97.
"""

import textwrap

from manim import (
    DOWN,
    LEFT,
    RIGHT,
    UP,
    WHITE,
    YELLOW,
    Arrow,
    Create,
    Dot,
    FadeIn,
    FadeOut,
    MathTex,
    Text,
    VGroup,
    Write,
)

from shapes.base_scene import NotionScene
from shapes.boxes import example_box, scene_title, theorem_box, warning_box


def _wrap(text: str, width: int = 56) -> str:
    return "\n".join(textwrap.fill(line, width=width) for line in text.split("\n"))


def _dot_label(point, label, color=WHITE, label_dir=UP, font_size=28, dot_color=YELLOW):
    d = Dot(point, color=dot_color, radius=0.08)
    t = MathTex(label, font_size=font_size, color=color)
    t.next_to(d, label_dir, buff=0.15)
    return VGroup(d, t)


class ComposeeDeuxTranslations(NotionScene):
    def construct(self):
        titre = scene_title("Composée de deux translations")
        titre.scale(0.5)
        titre.to_edge(UP)

        # --- Énoncé : théorème --------------------------------------------------
        theoreme = theorem_box(
            VGroup(
                Text("Composée de deux translations", font_size=25, weight="BOLD"),
                MathTex(r"t_{\vec v}\circ t_{\vec u} = t_{\vec u + \vec v}", font_size=32),
                Text(
                    _wrap("C'est une translation, de vecteur la somme des deux vecteurs. La composition est commutative."),
                    font_size=22,
                ),
            ).arrange(DOWN, buff=0.25)
        )
        theoreme.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Commençons par le cas le plus simple. La composée de deux "
                "translations, de vecteurs u et v, est encore une "
                "translation, de vecteur la somme u plus v. Autrement dit, "
                "t indice v, rond t indice u, est égale à t indice u plus "
                "v. Comme l'addition vectorielle est commutative, cette "
                "composition-là est commutative : l'ordre n'a pas "
                "d'importance."
            )
        ) as tracker:
            self.play(Write(titre))
            self.play(FadeIn(theoreme))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(theoreme))

        # --- Raisonnement : démonstration par Chasles ---------------------------
        etape1 = MathTex(r"M_1 = t_{\vec u}(M) \implies \overrightarrow{MM_1} = \vec u", font_size=27)
        etape2 = MathTex(r"M' = t_{\vec v}(M_1) \implies \overrightarrow{M_1M'} = \vec v", font_size=27)
        etape3 = MathTex(
            r"\overrightarrow{MM'} = \overrightarrow{MM_1} + \overrightarrow{M_1M'} = \vec u + \vec v"
            r"\quad (\text{relation de Chasles})",
            font_size=27,
            color=YELLOW,
        )
        etape4 = MathTex(r"\implies \ t_{\vec v}\circ t_{\vec u} = t_{\vec u+\vec v}", font_size=29)
        demo = VGroup(etape1, etape2, etape3, etape4).arrange(DOWN, buff=0.35)
        demo.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Démontrons ce résultat. Soit M un point quelconque. Son "
                "image par t indice u est M-un, avec le vecteur M M-un "
                "égal à u. L'image de M-un par t indice v est M prime, "
                "avec le vecteur M-un M prime égal à v. La relation de "
                "Chasles donne alors directement le vecteur M M prime "
                "égal au vecteur M M-un plus le vecteur M-un M prime, "
                "c'est-à-dire u plus v, un vecteur constant, indépendant "
                "de M. La transformation qui envoie tout point M sur M "
                "prime est donc bien la translation de vecteur u plus v."
            )
        ) as tracker:
            self.play(Write(etape1))
            self.play(Write(etape2))
            self.play(Write(etape3))
            self.play(Write(etape4))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(demo))

        # --- Exemple traité -------------------------------------------------
        enonce_ex = MathTex(
            r"\vec u(2\,;\,-1), \quad \vec v(-3\,;\,4), \quad A(1\,;\,1)",
            font_size=27,
        )
        calcul_ex = MathTex(
            r"\vec u+\vec v = (-1\,;\,3) \quad \implies \quad A' = A + (\vec u+\vec v) = (0\,;\,4)",
            font_size=27,
            color=YELLOW,
        )
        exemple = example_box(VGroup(enonce_ex, calcul_ex).arrange(DOWN, buff=0.3))
        exemple.next_to(titre, DOWN, buff=0.4)

        a_pt = LEFT * 2.5 + DOWN * 1.5
        somme = (-1, 3, 0)
        a1_pt = a_pt + RIGHT * somme[0] + UP * somme[1]
        fleche = Arrow(a_pt, a1_pt, color=YELLOW, buff=0.12)
        pt_a = _dot_label(a_pt, "A")
        pt_a1 = _dot_label(a1_pt, "A'")
        figure = VGroup(fleche, pt_a, pt_a1)
        figure.scale(0.75)
        figure.next_to(exemple, DOWN, buff=0.35)

        with self.voiceover(
            text=(
                "Traitons un exemple numérique. Soit u de coordonnées 2 et "
                "moins 1, v de coordonnées moins 3 et 4, et le point A de "
                "coordonnées 1 et 1. La somme u plus v vaut moins 1 et 3. "
                "L'image de A par t indice v rond t indice u s'obtient "
                "donc directement en ajoutant ce vecteur somme aux "
                "coordonnées de A, sans passer par le calcul intermédiaire "
                ": on trouve A prime de coordonnées 0 et 4."
            )
        ) as tracker:
            self.play(FadeIn(exemple))
            self.play(Create(figure))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(exemple), FadeOut(figure))

        # --- À retenir --------------------------------------------------------
        retenir = theorem_box(
            MathTex(r"t_{\vec v}\circ t_{\vec u} = t_{\vec u+\vec v} = t_{\vec u}\circ t_{\vec v}", font_size=30)
        )
        retenir.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "À retenir : composer deux translations revient simplement "
                "à additionner leurs vecteurs, et l'ordre des deux "
                "translations n'a aucune importance."
            )
        ) as tracker:
            self.play(FadeIn(retenir))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(retenir))

        # --- Piège à éviter -----------------------------------------------------
        piege = warning_box(
            Text(
                _wrap(
                    "Ce cas commutatif est une exception : dès la scène suivante, "
                    "l'ordre de composition redeviendra déterminant."
                ),
                font_size=23,
            )
        )
        piege.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Attention cependant : ce cas commutatif est une exception "
                "propre aux translations. Dès la prochaine composée que "
                "nous étudierons, l'ordre des transformations redeviendra "
                "déterminant."
            )
        ) as tracker:
            self.play(FadeIn(piege))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(piege), FadeOut(titre))
