"""
scenes/Maths_ComposeesTransformationsPlan_04.py — Chapitre 8 « Composées de
transformations du plan » (1ereC, Maths), scène 04.

§ Généralités sur la composée g∘f de deux transformations : définition
(ordre d'application), non-commutativité, propriétés (transformation,
réciproque, associativité, isométrie), démonstration de la réciproque,
exemple résolu (lecture de tu⃗∘sO), tableau des éléments caractéristiques.
Source : 1ereC/Maths.pdf, chapitre 8, pages 96-97.
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
    MathTex,
    Text,
    VGroup,
    Write,
)

from shapes.base_scene import NotionScene
from shapes.boxes import definition_box, scene_title, theorem_box, warning_box


def _wrap(text: str, width: int = 56) -> str:
    return "\n".join(textwrap.fill(line, width=width) for line in text.split("\n"))


def _dot_label(point, label, color=WHITE, label_dir=UP, font_size=28, dot_color=YELLOW):
    d = Dot(point, color=dot_color, radius=0.08)
    t = MathTex(label, font_size=font_size, color=color)
    t.next_to(d, label_dir, buff=0.15)
    return VGroup(d, t)


def _cell(text_str: str, font_size: int = 20, bold: bool = False):
    return Text(text_str, font_size=font_size, weight="BOLD" if bold else "NORMAL", color=WHITE)


class GeneralitesComposition(NotionScene):
    def construct(self):
        titre = scene_title("Composée de deux transformations")
        titre.scale(0.48)
        titre.to_edge(UP)

        # --- Énoncé : définition de g∘f ---------------------------------------
        def_composee = definition_box(
            VGroup(
                Text("Composée g∘f", font_size=25, weight="BOLD"),
                MathTex(r"(g\circ f)(M) = g\big(f(M)\big)", font_size=29),
                Text(
                    _wrap("On applique d'abord f, puis g au résultat : g∘f se lit « g rond f », f en premier."),
                    font_size=22,
                ),
                MathTex(r"\text{En g\'en\'eral : } g\circ f \neq f\circ g", font_size=25, color=YELLOW),
            ).arrange(DOWN, buff=0.25)
        )
        def_composee.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Nous savons composer des fonctions numériques ; faisons de "
                "même avec des transformations du plan. La composée g rond "
                "f, notée g∘f, associe à tout point M le point g de f de "
                "M. Le piège classique est l'ordre : on applique toujours "
                "f en premier, puis g au résultat obtenu — et retenez "
                "d'emblée que, en général, g∘f est différente de f∘g : la "
                "composition de transformations n'est pas commutative."
            )
        ) as tracker:
            self.play(Write(titre))
            self.play(FadeIn(def_composee))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(def_composee))

        # --- Raisonnement : propriétés + démonstration de la réciproque --------
        props = theorem_box(
            VGroup(
                Text("Propriétés générales", font_size=24, weight="BOLD"),
                MathTex(r"1)\ \ g\circ f \text{ est une transformation du plan}", font_size=24),
                MathTex(r"2)\ \ (g\circ f)^{-1} = f^{-1}\circ g^{-1}", font_size=24),
                MathTex(r"3)\ \ h\circ(g\circ f) = (h\circ g)\circ f \quad (\text{associativit\'e})", font_size=24),
                MathTex(r"4)\ \ \text{la compos\'ee de deux isom\'etries est une isom\'etrie}", font_size=24),
            ).arrange(DOWN, buff=0.22)
        )
        props.next_to(titre, DOWN, buff=0.35)

        with self.voiceover(
            text=(
                "Quatre propriétés à connaître. Un : la composée de deux "
                "transformations est encore une transformation, puisque la "
                "composée de deux bijections est une bijection. Deux : la "
                "réciproque de g∘f est f moins un rond g moins un — on "
                "inverse aussi l'ordre. Trois : la composition est "
                "associative, on peut donc écrire h∘g∘f sans ambiguïté. "
                "Quatre : composer deux isométries donne toujours une "
                "isométrie, ce qui, combiné à la règle de parité vue "
                "précédemment, permettra d'anticiper le type de résultat."
            )
        ) as tracker:
            self.play(FadeIn(props))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(props))

        demo_titre = Text("Démonstration de la propriété 2", font_size=24, weight="BOLD")
        demo1 = MathTex(
            r"(g\circ f)\circ(f^{-1}\circ g^{-1}) = g\circ\big(f\circ f^{-1}\big)\circ g^{-1}"
            r" = g\circ \mathrm{id} \circ g^{-1} = g\circ g^{-1} = \mathrm{id}",
            font_size=22,
        )
        demo2 = MathTex(
            r"(f^{-1}\circ g^{-1})\circ(g\circ f) = f^{-1}\circ\big(g^{-1}\circ g\big)\circ f"
            r" = f^{-1}\circ \mathrm{id} \circ f = f^{-1}\circ f = \mathrm{id}",
            font_size=22,
        )
        demo3 = Text(
            _wrap("f⁻¹∘g⁻¹ est donc bien l'application réciproque de g∘f."),
            font_size=22,
            color=YELLOW,
        )
        demo = VGroup(demo_titre, demo1, demo2, demo3).arrange(DOWN, buff=0.3)
        demo.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Démontrons la propriété 2, par associativité. D'une part, "
                "g∘f composé avec f moins un rond g moins un se simplifie "
                "en g rond f rond f moins un rond g moins un, où f rond f "
                "moins un vaut l'identité, ce qui donne finalement "
                "l'identité. D'autre part, dans l'autre sens, f moins un "
                "rond g moins un composé avec g∘f se simplifie de la même "
                "façon et redonne aussi l'identité. Les deux compositions "
                "valant l'identité, f moins un rond g moins un est bien "
                "la réciproque de g∘f."
            )
        ) as tracker:
            self.play(Write(demo_titre))
            self.play(FadeIn(demo1))
            self.play(FadeIn(demo2))
            self.play(FadeIn(demo3))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(demo))

        # --- Exemple traité : lecture d'une composée tu⃗∘sO --------------------
        exemple_titre = Text("Exemple résolu 1 — lire une composée", font_size=24, weight="BOLD")
        exemple_txt = MathTex(r"f = t_{\vec u}\circ s_O \quad : \quad \text{lecture de droite \`a gauche}", font_size=26)
        exemple = VGroup(exemple_titre, exemple_txt).arrange(DOWN, buff=0.3)
        exemple.next_to(titre, DOWN, buff=0.4)

        o_pt = LEFT * 2.5
        m_pt = LEFT * 0.5 + UP * 1.2
        m1_pt = 2 * o_pt - m_pt  # symétrique de M par rapport à O
        u_vec = RIGHT * 2.2 + DOWN * 0.3
        m2_pt = m1_pt + u_vec

        pt_o = _dot_label(o_pt, "O", dot_color="#288073", label_dir=DOWN)
        pt_m = _dot_label(m_pt, "M")
        pt_m1 = _dot_label(m1_pt, "M_1=s_O(M)", label_dir=DOWN, font_size=24)
        pt_m2 = _dot_label(m2_pt, "M'=f(M)", font_size=24)
        figure = VGroup(pt_o, pt_m, pt_m1, pt_m2)
        figure.scale(0.85)
        figure.move_to(DOWN * 1.2)

        with self.voiceover(
            text=(
                "Prenons f égale t indice u, rond s indice O. Pour lire "
                "cette composée, on part de la droite : on applique "
                "d'abord la symétrie centrale de centre O, qui envoie M "
                "sur M-un, puis on applique la translation de vecteur u à "
                "M-un pour obtenir M prime, l'image finale par f. C'est "
                "cet ordre de lecture, de droite à gauche, qu'il faut "
                "retenir pour toute composée."
            )
        ) as tracker:
            self.play(FadeIn(exemple))
            self.play(Create(figure))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(exemple), FadeOut(figure))

        # --- Tableau des éléments caractéristiques -----------------------------
        headers = [_cell("Transformation", bold=True), _cell("Élément(s) caractéristique(s)", bold=True)]
        rows = [
            ("Translation", "vecteur"),
            ("Symétrie centrale", "centre"),
            ("Symétrie axiale", "axe"),
            ("Rotation", "centre + angle"),
            ("Homothétie", "centre + rapport"),
        ]
        cells = list(headers)
        for a, b in rows:
            cells.append(_cell(a, font_size=20))
            cells.append(_cell(b, font_size=20))
        tableau = VGroup(*cells).arrange_in_grid(rows=6, cols=2, buff=(0.7, 0.2), col_alignments="lc")
        tableau.scale(0.8)
        tableau.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Pour identifier complètement une composée, il faut "
                "toujours préciser ses éléments caractéristiques : le "
                "vecteur pour une translation, le centre pour une symétrie "
                "centrale, l'axe pour une symétrie axiale, le centre et "
                "l'angle pour une rotation, le centre et le rapport pour "
                "une homothétie. C'est tout l'objet des théorèmes qui "
                "suivent : déterminer ces éléments pour chaque type de "
                "composée."
            )
        ) as tracker:
            self.play(FadeIn(tableau))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(tableau))

        # --- Piège à éviter -----------------------------------------------------
        piege = warning_box(
            VGroup(
                Text("Piège : l'ordre de composition", font_size=24, weight="BOLD"),
                MathTex(r"g\circ f \ \text{applique } f \text{ en premier, pas } g", font_size=26),
            ).arrange(DOWN, buff=0.25)
        )
        piege.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Le piège à éviter absolument dans tout ce chapitre : g∘f "
                "applique f en premier, jamais g. Une inversion de l'ordre "
                "change généralement le résultat, sauf dans les cas "
                "particuliers que nous rencontrerons, comme la composée de "
                "deux translations."
            )
        ) as tracker:
            self.play(FadeIn(piege))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(piege), FadeOut(titre))
