"""
scenes/Maths_ComposeesTransformationsPlan_08.py — Chapitre 8 « Composées de
transformations du plan » (1ereC, Maths), scène 08.

§ Composée de deux symétries axiales d'axes sécants : sΔ'∘sΔ = r(O, 2θ)
(rotation d'angle double), démonstration, cas particulier axes
perpendiculaires (symétrie centrale), conséquence (décomposition d'une
rotation), exemple résolu 4 (Δ:y=x, Δ':axe des abscisses).
Source : 1ereC/Maths.pdf, chapitre 8, pages 99-100.
"""

import textwrap

import numpy as np

from manim import DOWN, LEFT, RIGHT, UP, WHITE, YELLOW, Create, Dot, FadeIn, FadeOut, Line, MathTex, Text, VGroup, Write

from shapes.base_scene import NotionScene
from shapes.boxes import example_box, scene_title, theorem_box, warning_box


def _wrap(text: str, width: int = 56) -> str:
    return "\n".join(textwrap.fill(line, width=width) for line in text.split("\n"))


def _dot_label(point, label, color=WHITE, label_dir=UP, font_size=28, dot_color=YELLOW):
    d = Dot(point, color=dot_color, radius=0.08)
    t = MathTex(label, font_size=font_size, color=color)
    t.next_to(d, label_dir, buff=0.15)
    return VGroup(d, t)


class ComposeeSymetriesAxialesAxesSecants(NotionScene):
    def construct(self):
        titre = scene_title("Symétries axiales — axes sécants")
        titre.scale(0.48)
        titre.to_edge(UP)

        # --- Énoncé : théorème fondamental --------------------------------------
        theoreme = theorem_box(
            VGroup(
                Text("Théorème fondamental (axes sécants en O)", font_size=23, weight="BOLD"),
                MathTex(r"s_{\Delta'}\circ s_{\Delta} = r_{(O,\,2\theta)} \quad \theta = (\widehat{\Delta,\Delta'})", font_size=29),
                Text(_wrap("Rotation de centre O, d'angle le double de l'angle orienté du premier axe vers le second."), font_size=21),
            ).arrange(DOWN, buff=0.25)
        )
        theoreme.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Passons maintenant au cas où les deux axes delta et delta "
                "prime sont sécants en un point O. La composée s indice "
                "delta prime, rond s indice delta, est alors une rotation "
                "de centre O, dont l'angle est le double de l'angle "
                "orienté qui va de delta vers delta prime."
            )
        ) as tracker:
            self.play(Write(titre))
            self.play(FadeIn(theoreme))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(theoreme))

        # --- Raisonnement : démonstration -----------------------------------
        etape1 = MathTex(r"O\in\Delta \text{ et } O\in\Delta' \implies OM=OM_1=OM' \quad (\text{isom\'etries})", font_size=23)
        etape2 = MathTex(
            r"\widehat{(\overrightarrow{OM},\overrightarrow{OM'})} = \widehat{(\overrightarrow{OM},\overrightarrow{OM_1})}"
            r"+\widehat{(\overrightarrow{OM_1},\overrightarrow{OM'})} \quad (\text{Chasles})",
            font_size=22,
        )
        etape3 = MathTex(
            r"\text{Propri\'et\'e des r\'eflexions : chaque sym\'etrie double l'angle vers son axe}",
            font_size=22,
        )
        etape4 = MathTex(
            r"\implies \widehat{(\overrightarrow{OM},\overrightarrow{OM'})} = 2\theta \quad (\text{ind\'ependant de } M)",
            font_size=24,
            color=YELLOW,
        )
        demo = VGroup(etape1, etape2, etape3, etape4).arrange(DOWN, buff=0.28)
        demo.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Démontrons ce résultat. D'abord, le point O appartenant "
                "aux deux axes est invariant par chaque symétrie, et "
                "chaque symétrie conserve les distances : on a donc OM "
                "égale OM-un égale OM prime, pour tout point M. La "
                "transformation composée fixe donc O et conserve les "
                "distances à O : c'est nécessairement une rotation de "
                "centre O. Pour trouver son angle, on utilise la relation "
                "de Chasles sur les angles orientés, combinée à la "
                "propriété des réflexions : chaque symétrie axiale double "
                "l'angle orienté entre un vecteur et son image, relativement "
                "à la direction de son axe. En développant soigneusement "
                "ce calcul, tous les termes qui dépendent de M "
                "s'éliminent, et il ne reste que deux fois thêta, l'angle "
                "orienté entre les deux axes : le résultat est bien "
                "indépendant du point M choisi."
            )
        ) as tracker:
            self.play(Write(etape1))
            self.play(Write(etape2))
            self.play(Write(etape3))
            self.play(Write(etape4))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(demo))

        # figure : deux droites sécantes
        o_pt = DOWN * 0.3
        delta = Line(o_pt + LEFT * 2.2, o_pt + RIGHT * 2.2, color="#1E5FA8")
        dir_dp = np.array([np.cos(1.15), np.sin(1.15), 0]) * 1.8
        delta_p = Line(o_pt - dir_dp, o_pt + dir_dp, color="#74458C")
        label_d = MathTex(r"\Delta", font_size=26).next_to(delta.get_end(), RIGHT, buff=0.1)
        label_dp = MathTex(r"\Delta'", font_size=26).next_to(delta_p.get_end(), UP, buff=0.1)
        pt_o = _dot_label(o_pt, "O", dot_color="#288073", label_dir=DOWN)
        figure = VGroup(delta, delta_p, label_d, label_dp, pt_o)
        figure.move_to(DOWN * 0.8)

        with self.voiceover(
            text=(
                "Voici les deux axes sécants en O : c'est autour de ce "
                "point que la rotation composée va tourner."
            )
        ) as tracker:
            self.play(Create(figure))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(figure))

        # --- Cas particulier : axes perpendiculaires ------------------------
        piege_perp = warning_box(
            VGroup(
                Text("Cas particulier : axes perpendiculaires", font_size=23, weight="BOLD"),
                MathTex(r"\theta = \dfrac{\pi}{2} \implies 2\theta = \pi \implies s_{\Delta'}\circ s_{\Delta} = s_O", font_size=27),
            ).arrange(DOWN, buff=0.25)
        )
        piege_perp.next_to(titre, DOWN, buff=0.45)

        with self.voiceover(
            text=(
                "Cas particulier à retenir : si les deux axes sont "
                "perpendiculaires, thêta vaut pi sur deux, donc l'angle de "
                "rotation, le double, vaut pi. Une rotation d'angle pi "
                "n'est autre qu'une symétrie centrale : la composée de "
                "deux symétries d'axes perpendiculaires en O est donc "
                "exactement la symétrie centrale de centre O."
            )
        ) as tracker:
            self.play(FadeIn(piege_perp))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(piege_perp))

        # --- Conséquence -----------------------------------------------------
        consequence = theorem_box(
            Text(
                _wrap(
                    "Conséquence : toute rotation de centre O et d'angle θ se "
                    "décompose en 2 symétries d'axes sécants en O, formant un "
                    "angle θ/2, l'un des deux axes pouvant être choisi "
                    "arbitrairement parmi les droites passant par O."
                ),
                font_size=21,
            )
        )
        consequence.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Conséquence essentielle pour les problèmes de "
                "construction : toute rotation de centre O et d'angle "
                "thêta se décompose en deux symétries d'axes sécants en O, "
                "formant entre eux un angle moitié, thêta sur deux, le "
                "premier axe étant choisi arbitrairement parmi les droites "
                "passant par O."
            )
        ) as tracker:
            self.play(FadeIn(consequence))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(consequence))

        # --- Exemple résolu 4 -------------------------------------------------
        enonce = MathTex(r"\Delta: y=x, \quad \Delta': y=0 \ (\text{axe des abscisses})", font_size=27)
        calc1 = MathTex(r"s_\Delta: x'=y,\ y'=x", font_size=25)
        calc2 = MathTex(r"s_{\Delta'}: x''=x'=y,\ y''=-y'=-x", font_size=25)
        calc3 = MathTex(r"f: (x,y)\mapsto(y,-x) \implies f = r_{(O,\,-\pi/2)}", font_size=27, color=YELLOW)
        verif = Text(_wrap("(Δ,Δ') = 0−π/4 = −π/4 ⟹ angle double = −π/2 : quart de tour indirect."), font_size=20)
        exemple = example_box(VGroup(enonce, calc1, calc2, calc3, verif).arrange(DOWN, buff=0.22))
        exemple.next_to(titre, DOWN, buff=0.35)

        with self.voiceover(
            text=(
                "Traitons un exemple analytique. Soit delta la première "
                "bissectrice, d'équation y égale x, et delta prime l'axe "
                "des abscisses. La symétrie par rapport à delta échange x "
                "et y. En appliquant ensuite la symétrie par rapport à "
                "delta prime, qui change le signe de y, on obtient x "
                "seconde égale y, y seconde égale moins x. On reconnaît "
                "exactement la formule de la rotation de centre O et "
                "d'angle moins pi sur deux : c'est un quart de tour "
                "indirect, c'est-à-dire dans le sens des aiguilles d'une "
                "montre. Et cela concorde avec le théorème : l'angle de "
                "delta vers delta prime vaut moins pi sur quatre, dont le "
                "double est bien moins pi sur deux."
            )
        ) as tracker:
            self.play(FadeIn(exemple))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(exemple))

        # --- À retenir + piège --------------------------------------------------
        retenir = theorem_box(MathTex(r"s_{\Delta'}\circ s_{\Delta} = r_{(O,\,2\theta)}", font_size=30))
        retenir.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "À retenir : deux symétries d'axes sécants en O se "
                "composent en une rotation de centre O, d'angle le double "
                "de celui séparant les deux axes."
            )
        ) as tracker:
            self.play(FadeIn(retenir))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(retenir))

        piege = warning_box(
            Text(
                _wrap(
                    "Piège : l'angle de la composée est le double de l'angle "
                    "ORIENTÉ du PREMIER axe vers le SECOND — pas l'angle géométrique "
                    "non orienté entre les deux droites."
                ),
                font_size=22,
            )
        )
        piege.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Piège très fréquent : l'angle de la rotation obtenue est "
                "le double de l'angle orienté du premier axe vers le "
                "second, dans cet ordre précis — surtout pas l'angle "
                "géométrique, non orienté, entre les deux droites."
            )
        ) as tracker:
            self.play(FadeIn(piege))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(piege), FadeOut(titre))
