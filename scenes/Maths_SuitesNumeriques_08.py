"""
scenes/Maths_SuitesNumeriques_08.py — Chapitre 15 « Suites numériques »
(1ereC, Maths), scène 08.

Suites géométriques : définition, propriété caractéristique, moyenne
géométrique, théorème du terme général (avec démonstration par récurrence)
et sens de variation. Exemple résolu 8, comparaison visuelle croissance
arithmétique / géométrique.
Source : 1ereC/Maths.pdf, chapitre 15, pages 176-188.
"""

import textwrap

from manim import DOWN, LEFT, RIGHT, UP, WHITE, YELLOW, Axes, FadeIn, FadeOut, MathTex, Text, VGroup, Write

from shapes.base_scene import NotionScene
from shapes.boxes import (
    definition_box,
    essentiel_box,
    example_box,
    property_box,
    scene_title,
    theorem_box,
    warning_box,
)


def _wrap(text: str, width: int = 58) -> str:
    return "\n".join(textwrap.fill(line, width=width) for line in text.split("\n"))


class SuitesGeometriques(NotionScene):
    def construct(self):
        titre = scene_title("Suites géométriques — définition et terme général")
        titre.scale(0.44)
        titre.to_edge(UP)
        self.play(Write(titre))

        # --- Énoncé : définition ----------------------------------------------------
        definition = definition_box(
            VGroup(
                Text(
                    "(un) est géométrique de raison q (termes non nuls) s'il\n"
                    "existe un réel q tel que, pour tout n :",
                    font_size=22,
                ),
                MathTex(r"u_{n+1} = q\times u_n", font_size=32),
                Text(
                    "Propriété caractéristique : le quotient de deux termes\n"
                    "consécutifs est toujours constant, égal à q.",
                    font_size=21,
                ),
            ).arrange(DOWN, buff=0.25),
            box_width=10.8,
        )
        definition.next_to(titre, DOWN, buff=0.35)

        with self.voiceover(
            text=(
                "Une suite u indice n, à termes non nuls, est géométrique "
                "de raison q s'il existe un réel q tel que, pour tout "
                "entier n, u indice n plus un égale q fois u indice n. "
                "Autrement dit, on passe d'un terme au suivant en le "
                "multipliant toujours par la même quantité q. C'est la "
                "propriété caractéristique : un quotient constant entre "
                "deux termes consécutifs, égal à q. On pense par exemple "
                "aux intérêts composés, ou à une population qui évolue "
                "d'un même pourcentage chaque année."
            )
        ) as tracker:
            self.play(FadeIn(definition))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(definition))

        # --- Moyenne géométrique -----------------------------------------------------
        moyenne = property_box(
            VGroup(
                Text(
                    "Si a, b, c sont trois termes consécutifs positifs d'une\n"
                    "suite géométrique, b est la moyenne géométrique de a et c :",
                    font_size=21,
                ),
                MathTex(r"b^2 = ac", font_size=30),
            ).arrange(DOWN, buff=0.25),
            box_width=10.4,
        )
        moyenne.next_to(titre, DOWN, buff=0.35)

        with self.voiceover(
            text=(
                "Propriété de la moyenne géométrique : si a, b, c sont "
                "trois termes consécutifs et positifs d'une suite "
                "géométrique, alors b au carré égale a fois c. Cela vient "
                "du fait que b sur a et c sur b valent tous les deux q."
            )
        ) as tracker:
            self.play(FadeIn(moyenne))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(moyenne))

        # --- Théorème : terme général ------------------------------------------------
        theo_terme = theorem_box(
            VGroup(
                MathTex(r"u_n = u_0 \times q^n", font_size=32),
                MathTex(r"u_n = u_p \times q^{\,n-p}", font_size=32),
            ).arrange(DOWN, buff=0.25),
            box_width=8.5,
        )
        theo_terme.next_to(titre, DOWN, buff=0.35)

        with self.voiceover(
            text=(
                "Théorème du terme général : pour une suite géométrique de "
                "raison q, u indice n égale u zéro fois q puissance n. "
                "Plus généralement, à partir d'un terme quelconque u "
                "indice p : u indice n égale u indice p fois q puissance, "
                "n moins p."
            )
        ) as tracker:
            self.play(FadeIn(theo_terme))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(theo_terme))

        # --- Démonstration par récurrence -------------------------------------------
        demo_titre = Text(
            "Démonstration de un = u0 × qⁿ, par récurrence sur n :",
            font_size=21,
            color=YELLOW,
            weight="BOLD",
        )
        demo_titre.next_to(titre, DOWN, buff=0.35)
        demo_init = MathTex(
            r"\text{Initialisation : } u_0 = u_0\times q^0 = u_0\times 1 \ \text{ vraie.}",
            font_size=23,
        )
        demo_init.next_to(demo_titre, DOWN, buff=0.3)
        demo_heredite = VGroup(
            MathTex(
                r"\text{Hérédité : on suppose } u_n=u_0\, q^n \text{ pour un } n \text{ fixé.}",
                font_size=23,
            ),
            MathTex(
                r"u_{n+1} = q\times u_n = q\times(u_0\, q^n) = u_0\, q^{n+1}",
                font_size=25,
            ),
            Text(
                "La propriété est donc vraie au rang n+1.",
                font_size=21,
            ),
        ).arrange(DOWN, buff=0.2)
        demo_heredite.next_to(demo_init, DOWN, buff=0.3)
        demo_concl = Text(
            "Conclusion : vraie pour tout n (principe de récurrence).",
            font_size=20,
        )
        demo_concl.next_to(demo_heredite, DOWN, buff=0.3)

        with self.voiceover(
            text=(
                "Démontrons ce résultat par récurrence sur n. "
                "Initialisation : au rang zéro, u zéro égale u zéro fois q "
                "puissance zéro, qui vaut un, donc c'est vrai. Hérédité : "
                "on suppose la propriété vraie à un rang n fixé. Alors u "
                "indice n plus un égale q fois u indice n, donc, par "
                "hypothèse, q fois u zéro q puissance n, soit u zéro q "
                "puissance n plus un. La propriété est donc vraie au rang "
                "n plus un. D'après le principe de récurrence, elle est "
                "vraie pour tout entier n."
            )
        ) as tracker:
            self.play(FadeIn(demo_titre))
            self.play(FadeIn(demo_init))
            self.play(FadeIn(demo_heredite))
            self.play(FadeIn(demo_concl))
            self.wait(tracker.get_remaining_duration())

        self.play(
            FadeOut(demo_titre), FadeOut(demo_init), FadeOut(demo_heredite), FadeOut(demo_concl)
        )

        # --- Théorème : sens de variation ---------------------------------------------
        theo_variation = theorem_box(
            VGroup(
                Text("Cas u0 > 0 et q > 0 :", font_size=21, weight="BOLD"),
                MathTex(r"q>1 \Longrightarrow (u_n) \text{ croissante}", font_size=24),
                MathTex(r"0<q<1 \Longrightarrow (u_n) \text{ décroissante}", font_size=24),
                MathTex(r"q=1 \Longrightarrow (u_n) \text{ constante}", font_size=24),
                Text("Si q < 0, (un) change de signe : ni croissante ni décroissante.", font_size=20),
            ).arrange(DOWN, buff=0.2),
            box_width=10.8,
        )
        theo_variation.next_to(titre, DOWN, buff=0.35)

        with self.voiceover(
            text=(
                "Sens de variation, dans le cas où u zéro et q sont tous "
                "deux strictement positifs : si q est supérieur à un, la "
                "suite est croissante ; si q est compris strictement entre "
                "zéro et un, elle est décroissante ; si q vaut un, elle "
                "est constante. Si q est négatif, les termes changent de "
                "signe à chaque rang : la suite n'est ni croissante ni "
                "décroissante."
            )
        ) as tracker:
            self.play(FadeIn(theo_variation))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(theo_variation))

        # --- Exemple résolu 8 ----------------------------------------------------
        ex8_titre = Text(
            "Exemple 8 — suite géométrique (q > 0) avec u1 = 6 et u3 = 24 :",
            font_size=20,
            color=YELLOW,
            weight="BOLD",
        )
        ex8_titre.next_to(titre, DOWN, buff=0.35)
        ex8_calc = example_box(
            MathTex(
                r"""
                u_3=u_1 q^2 \Longrightarrow 24=6q^2 \Longrightarrow q^2=4
                \Longrightarrow q=2 \ (q>0)
                \qquad u_0=\dfrac{u_1}{q}=3
                """,
                font_size=21,
            ),
            box_width=11.6,
        )
        ex8_calc.next_to(ex8_titre, DOWN, buff=0.25)
        ex8_concl = MathTex(
            r"u_n = 3\times 2^n \qquad u_8 = 3\times 256 = 768",
            font_size=27,
        )
        ex8_concl.next_to(ex8_calc, DOWN, buff=0.25)

        with self.voiceover(
            text=(
                "Exemple : une suite géométrique de raison positive "
                "vérifie u un égale six et u trois égale vingt-quatre. "
                "Comme u trois égale u un fois q carré, on obtient q carré "
                "égale quatre, donc q égale deux, puisque q est positif. "
                "On en déduit u zéro égale u un sur q, soit trois. La "
                "formule du terme général est u indice n égale trois fois "
                "deux puissance n, et u huit égale trois fois deux cent "
                "cinquante-six, soit sept cent soixante-huit."
            )
        ) as tracker:
            self.play(FadeIn(ex8_titre))
            self.play(FadeIn(ex8_calc))
            self.play(FadeIn(ex8_concl))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(ex8_titre), FadeOut(ex8_calc), FadeOut(ex8_concl))

        # --- Comparaison visuelle arithmétique / géométrique --------------------
        axes = Axes(
            x_range=[0, 6, 1],
            y_range=[0, 40, 10],
            x_length=6.5,
            y_length=3.8,
            axis_config={"color": WHITE, "font_size": 16},
        )
        axes.move_to(DOWN * 0.3)
        arith_pts = [axes.c2p(n, 3 * n + 2) for n in range(6)]
        geo_pts = [axes.c2p(n, 2 * (1.6**n)) for n in range(6)]
        from manim import Dot, VMobject

        droite_arith = VMobject(color="#288073", stroke_width=3).set_points_as_corners(arith_pts)
        droite_geo = VMobject(color="#DE7C1F", stroke_width=3).set_points_as_corners(geo_pts)
        label_arith = Text("croissance arithmétique", font_size=18, color="#288073")
        label_arith.next_to(axes, DOWN, buff=0.2).shift(LEFT * 1.5)
        label_geo = Text("croissance géométrique", font_size=18, color="#DE7C1F")
        label_geo.next_to(label_arith, RIGHT, buff=0.4)
        figure = VGroup(axes, droite_arith, droite_geo, label_arith, label_geo)

        with self.voiceover(
            text=(
                "Comparons visuellement les deux types de croissance : la "
                "suite arithmétique, en vert, progresse régulièrement, "
                "toujours du même pas. La suite géométrique, en orange, "
                "avec une raison supérieure à un, s'envole beaucoup plus "
                "vite : elle finit toujours par dépasser largement la "
                "suite arithmétique."
            )
        ) as tracker:
            self.play(FadeIn(figure))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(figure))

        # --- À retenir -----------------------------------------------------------
        retenir = essentiel_box(
            Text(
                _wrap(
                    "Suite géométrique : un+1 = q × un (quotient constant, "
                    "termes non nuls). un = u0 × qⁿ = up × q^(n-p). Sens de "
                    "variation selon q, si u0 > 0.",
                    width=56,
                ),
                font_size=22,
            ),
            box_width=10.8,
        )
        retenir.next_to(titre, DOWN, buff=0.35)

        with self.voiceover(
            text=(
                "À retenir : une suite géométrique multiplie toujours par "
                "le même facteur q. Son terme général se calcule "
                "directement à partir de n'importe quel terme connu, et "
                "son sens de variation dépend de la position de q par "
                "rapport à zéro et à un."
            )
        ) as tracker:
            self.play(FadeIn(retenir))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(retenir))

        # --- Piège à éviter ----------------------------------------------------
        piege = warning_box(
            Text(
                _wrap(
                    "Piège : une suite géométrique est définie à termes "
                    "non nuls. Si q < 0, elle change de signe à chaque "
                    "rang : ni croissante, ni décroissante, même si |q| "
                    "compare q à 1.",
                    width=56,
                ),
                font_size=21,
            ),
            box_width=11.2,
        )
        piege.next_to(titre, DOWN, buff=0.35)

        with self.voiceover(
            text=(
                "Piège à éviter : une suite géométrique est toujours "
                "définie à termes non nuls. Et si la raison q est "
                "négative, les termes changent de signe à chaque rang : "
                "la suite n'est ni croissante ni décroissante, quelle que "
                "soit la valeur absolue de q."
            )
        ) as tracker:
            self.play(FadeIn(piege))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(piege), FadeOut(titre))
