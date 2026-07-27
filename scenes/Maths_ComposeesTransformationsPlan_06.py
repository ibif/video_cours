"""
scenes/Maths_ComposeesTransformationsPlan_06.py — Chapitre 8 « Composées de
transformations du plan » (1ereC, Maths), scène 06.

§ Composée de deux symétries centrales : sO'∘sO = t(2 OO'⃗) (translation),
démonstration (via les milieux), conséquences (réciproques, décomposition
d'une translation), exemple résolu 2.
Source : 1ereC/Maths.pdf, chapitre 8, pages 97-98.
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


class ComposeeDeuxSymetriesCentrales(NotionScene):
    def construct(self):
        titre = scene_title("Composée de deux symétries centrales")
        titre.scale(0.46)
        titre.to_edge(UP)

        # --- Énoncé : théorème fondamental --------------------------------------
        theoreme = theorem_box(
            VGroup(
                Text("Théorème fondamental", font_size=25, weight="BOLD"),
                MathTex(r"s_{O'}\circ s_O = t_{2\overrightarrow{OO'}}", font_size=32),
                Text(_wrap("La composée de deux symétries centrales est une translation."), font_size=22),
            ).arrange(DOWN, buff=0.25)
        )
        theoreme.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Voici le premier théorème fondamental du chapitre. La "
                "composée s indice O prime, rond s indice O, de deux "
                "symétries centrales de centres O puis O prime, est la "
                "translation de vecteur 2 fois le vecteur O O prime. Deux "
                "symétries centrales, appliquées l'une après l'autre, "
                "produisent donc toujours une translation."
            )
        ) as tracker:
            self.play(Write(titre))
            self.play(FadeIn(theoreme))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(theoreme))

        # --- Raisonnement : démonstration (théorème des milieux) ---------------
        etape1 = MathTex(r"M_1 = s_O(M) \implies O \text{ milieu de } [MM_1]", font_size=25)
        etape2 = MathTex(r"M' = s_{O'}(M_1) \implies O' \text{ milieu de } [M_1M']", font_size=25)
        etape3 = MathTex(
            r"\text{Th\'eor\`eme des milieux (triangle } MM_1M'\text{)} : \ \overrightarrow{MM'} = 2\,\overrightarrow{OO'}",
            font_size=24,
            color=YELLOW,
        )
        demo = VGroup(etape1, etape2, etape3).arrange(DOWN, buff=0.3)
        demo.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Démontrons ce résultat grâce au théorème des milieux. "
                "Comme M-un est l'image de M par s indice O, le point O "
                "est le milieu du segment M M-un. De même, O prime est le "
                "milieu du segment M-un M prime, puisque M prime est "
                "l'image de M-un par s indice O prime. Dans le triangle M, "
                "M-un, M prime, O et O prime sont donc les milieux de deux "
                "côtés : d'après le théorème des milieux, le troisième "
                "côté M M prime est parallèle au segment O O prime, et de "
                "longueur double. Vectoriellement, cela s'écrit : le "
                "vecteur M M prime est égal à deux fois le vecteur O O "
                "prime — un vecteur constant, indépendant de M."
            )
        ) as tracker:
            self.play(Write(etape1))
            self.play(Write(etape2))
            self.play(Write(etape3))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(demo))

        # figure
        o_pt = LEFT * 3 + DOWN * 0.3
        o1_pt = RIGHT * 1 + DOWN * 0.3
        m_pt = LEFT * 3.6 + UP * 1.6
        m1_pt = 2 * o_pt - m_pt
        m2_pt = 2 * o1_pt - m1_pt
        pt_o = _dot_label(o_pt, "O", dot_color="#288073", label_dir=DOWN)
        pt_o1 = _dot_label(o1_pt, "O'", dot_color="#288073", label_dir=DOWN)
        pt_m = _dot_label(m_pt, "M")
        pt_m1 = _dot_label(m1_pt, "M_1", font_size=24)
        pt_m2 = _dot_label(m2_pt, "M'")
        seg1 = Arrow(m_pt, m1_pt, color="#595959", stroke_width=2, buff=0.1, tip_length=0.15)
        seg2 = Arrow(m1_pt, m2_pt, color="#595959", stroke_width=2, buff=0.1, tip_length=0.15)
        vec_oo1 = Arrow(o_pt, o1_pt, color=YELLOW, buff=0.1)
        figure = VGroup(seg1, seg2, vec_oo1, pt_o, pt_o1, pt_m, pt_m1, pt_m2)
        figure.scale(0.8)
        figure.move_to(DOWN * 1.0)

        with self.voiceover(
            text=(
                "Sur la figure, on visualise bien le vecteur O O prime, "
                "qui relie les deux centres, et le vecteur M M prime, "
                "deux fois plus long et parallèle."
            )
        ) as tracker:
            self.play(Create(figure))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(figure))

        # --- Conséquences --------------------------------------------------------
        consequences = theorem_box(
            VGroup(
                Text("Conséquences", font_size=24, weight="BOLD"),
                MathTex(r"s_O\circ s_{O'} = t_{2\overrightarrow{O'O}} \quad (\text{translation oppos\'ee})", font_size=24),
                Text(_wrap("sO∘sO' et sO'∘sO sont réciproques l'une de l'autre."), font_size=21),
                Text(
                    _wrap("Toute translation est décomposable en 2 symétries centrales, l'un des deux centres pouvant être choisi arbitrairement."),
                    font_size=21,
                ),
            ).arrange(DOWN, buff=0.22)
        )
        consequences.next_to(titre, DOWN, buff=0.35)

        with self.voiceover(
            text=(
                "Ce théorème a plusieurs conséquences importantes. "
                "D'abord, en inversant l'ordre, s indice O rond s indice O "
                "prime donne la translation de vecteur opposé, 2 fois le "
                "vecteur O prime O : les deux composées sont réciproques "
                "l'une de l'autre. Ensuite, et c'est très utile pour les "
                "problèmes de construction : toute translation peut se "
                "décomposer en deux symétries centrales, en choisissant un "
                "premier centre totalement arbitraire, le second se "
                "déduisant alors du vecteur de translation voulu."
            )
        ) as tracker:
            self.play(FadeIn(consequences))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(consequences))

        # --- Exemple résolu 2 -------------------------------------------------
        enonce = MathTex(r"A(1\,;\,2), \quad B(4\,;\,1), \quad f = s_B\circ s_A", font_size=27)
        calcul1 = MathTex(r"2\,\overrightarrow{AB} = 2(3\,;\,-1) = (6\,;\,-2)", font_size=27)
        calcul2 = MathTex(r"f = t_{(6\,;\,-2)}", font_size=27, color=YELLOW)
        calcul3 = MathTex(r"M(0\,;\,0) \ \implies \ M' = f(M) = (6\,;\,-2)", font_size=27)
        exemple = example_box(VGroup(enonce, calcul1, calcul2, calcul3).arrange(DOWN, buff=0.25))
        exemple.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Exemple : soient A de coordonnées 1 et 2, B de "
                "coordonnées 4 et 1, et f égale s indice B rond s indice "
                "A. Le vecteur de translation est 2 fois le vecteur AB, "
                "c'est-à-dire 2 fois le vecteur de coordonnées 3 et moins "
                "1, soit 6 et moins 2. La composée f est donc la "
                "translation de vecteur 6, moins 2. Appliquons-la, par "
                "exemple, à l'origine M de coordonnées 0 et 0 : son image "
                "M prime a pour coordonnées 6 et moins 2."
            )
        ) as tracker:
            self.play(FadeIn(exemple))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(exemple))

        # --- À retenir + piège --------------------------------------------------
        retenir = theorem_box(MathTex(r"s_{O'}\circ s_O = t_{2\overrightarrow{OO'}}", font_size=30))
        retenir.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "À retenir : la composée de deux symétries centrales est "
                "la translation de vecteur deux fois le vecteur reliant le "
                "premier centre au second."
            )
        ) as tracker:
            self.play(FadeIn(retenir))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(retenir))

        piege = warning_box(
            Text(
                _wrap(
                    "Piège : le vecteur de translation est 2·OO⃗' et non OO⃗' — "
                    "et l'ordre O puis O' compte pour le sens du vecteur."
                ),
                font_size=23,
            )
        )
        piege.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Piège fréquent : le vecteur de translation vaut deux fois "
                "le vecteur O O prime, pas seulement le vecteur O O prime "
                "— et l'ordre dans lequel on lit les centres, O puis O "
                "prime, détermine le sens du vecteur obtenu."
            )
        ) as tracker:
            self.play(FadeIn(piege))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(piege), FadeOut(titre))
