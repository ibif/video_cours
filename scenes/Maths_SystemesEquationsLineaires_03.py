"""
scenes/Maths_SystemesEquationsLineaires_03.py — Chapitre 13 « Systèmes
d'équations linéaires dans ℝ² et ℝ³ » (1ereC, Maths), scène 03.

§ Théorème de Cramer 2×2 (avec démonstration), exemple résolu 3
(5x+3y=19, 2x-y=1 → (2;3)), discussion du nombre de solutions selon D,
Dx, Dy, interprétation géométrique (droites sécantes / strictement
parallèles / confondues).
Source : 1ereC/Maths.pdf, chapitre 13, pages 154-164.
"""

import textwrap

from manim import (
    DOWN,
    LEFT,
    RIGHT,
    UP,
    FadeOut,
    FadeIn,
    Create,
    Line,
    MathTex,
    Text,
    VGroup,
    Write,
    WHITE,
    YELLOW,
)

from shapes.base_scene import NotionScene
from shapes.boxes import definition_box, example_box, property_box, scene_title, theorem_box


def _wrap(text: str, width: int = 56) -> str:
    return "\n".join(textwrap.fill(line, width=width) for line in text.split("\n"))


class CramerDiscussion2x2(NotionScene):
    def construct(self):
        titre = scene_title("Systèmes linéaires 2×2 — Formules de Cramer")
        titre.scale(0.5)
        titre.to_edge(UP)
        self.play(Write(titre))

        # --- Énoncé : théorème de Cramer ---------------------------------------
        theoreme = theorem_box(
            VGroup(
                Text("Théorème de Cramer (2×2)", font_size=24, weight="BOLD"),
                MathTex(
                    r"\begin{cases} ax+by=c \\ a'x+b'y=c' \end{cases}, \quad "
                    r"D = ab'-a'b,\ D_x=cb'-c'b,\ D_y=ac'-a'c",
                    font_size=24,
                ),
                MathTex(
                    r"D \neq 0 \ \Longrightarrow\ \mathcal{S}=\left\{\left(\dfrac{D_x}{D}\,;\,\dfrac{D_y}{D}\right)\right\}",
                    font_size=27,
                    color=YELLOW,
                ),
            ).arrange(DOWN, buff=0.28),
            box_width=12.0,
        )
        theoreme.next_to(titre, DOWN, buff=0.35)

        with self.voiceover(
            text=(
                "Voici le théorème de Cramer. Pour le système a x plus b y "
                "égale c, a prime x plus b prime y égale c prime, on "
                "définit trois déterminants : D égale a b prime moins a "
                "prime b, D indice x égale c b prime moins c prime b, et D "
                "indice y égale a c prime moins a prime c. Si D est non "
                "nul, alors le système admet une unique solution, donnée "
                "directement par x égale D indice x sur D, et y égale D "
                "indice y sur D. Démontrons cette formule."
            )
        ) as tracker:
            self.play(FadeIn(theoreme))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(theoreme))

        # --- Raisonnement : démonstration ---------------------------------------
        demo1 = MathTex(
            r"(\text{éq. 1})\times b' :\ ab'x + bb'y = cb' \qquad "
            r"(\text{éq. 2})\times b :\ a'bx + bb'y = c'b",
            font_size=23,
        )
        demo2 = MathTex(
            r"\text{Soustraction : } (ab'-a'b)\,x = cb'-c'b \ \Longrightarrow\ D\,x = D_x",
            font_size=25,
        )
        demo3 = MathTex(
            r"\text{De même, en éliminant } x : \quad D\,y = D_y",
            font_size=25,
        )
        demo4 = MathTex(
            r"D\neq 0 \ \Longrightarrow\ x=\dfrac{D_x}{D}, \ y=\dfrac{D_y}{D}",
            font_size=27,
            color=YELLOW,
        )
        demo = VGroup(demo1, demo2, demo3, demo4).arrange(DOWN, buff=0.35)
        demo.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "On multiplie la première équation par b prime, et la "
                "seconde par b, pour obtenir le même coefficient en y. En "
                "soustrayant, le terme en y disparaît : il reste a b prime "
                "moins a prime b, fois x, égale c b prime moins c prime b, "
                "c'est-à-dire D fois x égale D indice x. En éliminant x de "
                "la même façon, on obtient D fois y égale D indice y. "
                "Comme D est non nul, on peut diviser des deux côtés : on "
                "retrouve exactement les formules de Cramer."
            )
        ) as tracker:
            self.play(Write(demo1))
            self.play(Write(demo2))
            self.play(Write(demo3))
            self.play(Write(demo4))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(demo))

        # --- Exemple traité 3 -------------------------------------------------------
        ex3_enonce = MathTex(r"\begin{cases} 5x+3y=19 \\ 2x-y=1 \end{cases}", font_size=29)
        ex3_D = MathTex(r"D = 5\times(-1)-2\times 3 = -5-6=-11", font_size=25)
        ex3_Dx = MathTex(r"D_x = 19\times(-1)-1\times 3 = -22 \ \Rightarrow\ x=\dfrac{-22}{-11}=2", font_size=25)
        ex3_Dy = MathTex(r"D_y = 5\times 1-2\times 19 = -33 \ \Rightarrow\ y=\dfrac{-33}{-11}=3", font_size=25)
        ex3_concl = MathTex(r"\mathcal{S} = \{(2\,;\,3)\}", font_size=28, color=YELLOW)
        ex3 = VGroup(ex3_enonce, ex3_D, ex3_Dx, ex3_Dy, ex3_concl).arrange(DOWN, buff=0.25)
        ex3_box = example_box(ex3, box_width=12.0)
        ex3_box.scale(0.82)
        ex3_box.next_to(titre, DOWN, buff=0.3)

        with self.voiceover(
            text=(
                "Appliquons directement les formules. Le système est : cinq "
                "x plus trois y égale dix-neuf, deux x moins y égale un. On "
                "calcule D égale cinq fois moins un, moins deux fois trois, "
                "soit moins onze, non nul. D indice x vaut dix-neuf fois "
                "moins un, moins un fois trois, soit moins vingt-deux, donc "
                "x égale moins vingt-deux sur moins onze, soit deux. D "
                "indice y vaut cinq fois un, moins deux fois dix-neuf, soit "
                "moins trente-trois, donc y égale trois. L'ensemble des "
                "solutions est S égale l'ensemble contenant le couple deux, "
                "trois."
            )
        ) as tracker:
            self.play(FadeIn(ex3_box))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(ex3_box))

        # --- À retenir : discussion + interprétation géométrique ------------------
        discussion = MathTex(
            r"""
            \begin{array}{|c|c|c|}
            \hline
            \text{Condition} & \text{Solutions} & \text{Droites } (d), (d') \\
            \hline
            D \neq 0 & \text{une seule} & \text{s\'ecantes en un point} \\
            \hline
            D=0,\ D_x \text{ ou } D_y \neq 0 & \text{aucune} & \text{strictement parall\`eles} \\
            \hline
            D=0,\ D_x=D_y=0 & \text{une infinit\'e} & \text{confondues} \\
            \hline
            \end{array}
            """,
            font_size=21,
        )
        discussion.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Ce couple D, D indice x, D indice y permet aussi de "
                "discuter du nombre de solutions sans même résoudre. Si D "
                "est non nul, il y a une seule solution : les deux droites "
                "représentées par les équations sont sécantes en un point. "
                "Si D est nul mais que D indice x ou D indice y est non "
                "nul, il n'y a aucune solution : les droites sont "
                "strictement parallèles, elles ne se rencontrent jamais. "
                "Si D, D indice x et D indice y sont tous les trois nuls, "
                "il y a une infinité de solutions : les deux équations "
                "représentent en réalité la même droite, les droites sont "
                "confondues."
            )
        ) as tracker:
            self.play(FadeIn(discussion))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(discussion))

        # --- Piège à éviter : illustration géométrique + mise en garde ------------
        d1 = Line(LEFT * 3, RIGHT * 3, color="#DE7C1F")
        d2 = Line(LEFT * 3 + DOWN * 0.9, RIGHT * 3 + UP * 0.9, color="#288073")
        secantes = VGroup(d1, d2, Text("sécantes", font_size=18).next_to(VGroup(d1, d2), DOWN, buff=0.15))

        d3 = Line(LEFT * 2.6 + UP * 0.5, RIGHT * 2.6 + UP * 1.3, color="#DE7C1F")
        d4 = Line(LEFT * 2.6 + DOWN * 0.6, RIGHT * 2.6 + UP * 0.2, color="#288073")
        paralleles = VGroup(d3, d4, Text("strictement parallèles", font_size=18).next_to(VGroup(d3, d4), DOWN, buff=0.15))

        d5 = Line(LEFT * 2.6, RIGHT * 2.6, color="#DE7C1F", stroke_width=6)
        d6 = Line(LEFT * 2.6, RIGHT * 2.6, color="#288073", stroke_width=2)
        confondues = VGroup(d5, d6, Text("confondues", font_size=18).next_to(VGroup(d5, d6), DOWN, buff=0.15))

        schemas = VGroup(secantes, paralleles, confondues).arrange(RIGHT, buff=1.0)
        schemas.next_to(titre, DOWN, buff=0.6)

        with self.voiceover(
            text=(
                "Piège fréquent : ne jamais conclure trop vite dès que D "
                "est nul. D nul signifie seulement que les droites ne sont "
                "pas sécantes : il faut ENSUITE examiner D indice x et D "
                "indice y pour savoir si elles sont strictement parallèles, "
                "sans aucun point commun, ou bien confondues, avec une "
                "infinité de points communs. Ce sont deux situations très "
                "différentes qu'un D nul, à lui seul, ne permet jamais de "
                "distinguer."
            )
        ) as tracker:
            self.play(Create(schemas))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(schemas), FadeOut(titre))
