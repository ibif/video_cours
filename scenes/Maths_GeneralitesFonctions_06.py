"""
scenes/Maths_GeneralitesFonctions_06.py — Chapitre 3 (1ereC, Maths), scène 06.

Extremums (maximum, minimum, local ou global), majorant, minorant, fonction
bornée.
Source : 1ereC/Maths.pdf, chapitre 3, pages 28-40.
"""

import textwrap

from manim import DOWN, LEFT, RIGHT, UP, WHITE, YELLOW, Axes, Dot, DashedLine, FadeIn, FadeOut, MathTex, Text, VGroup, Write

from shapes.base_scene import NotionScene
from shapes.boxes import definition_box, essentiel_box, example_box, scene_title, warning_box


def _wrap(text: str, width: int = 60) -> str:
    return "\n".join(textwrap.fill(line, width=width) for line in text.split("\n"))


class ExtremumsMajorantMinorant(NotionScene):
    def construct(self):
        titre = scene_title("Extremums, majorant, minorant")
        titre.scale(0.6)
        titre.to_edge(UP)
        self.play(Write(titre))

        # --- Énoncé : maximum / minimum / extremum ----------------------
        def_extremum = definition_box(
            MathTex(
                r"""
                \begin{array}{l}
                f \text{ admet un maximum en } x_0 \text{ sur } I : \ \forall x \in I,\ f(x) \leq f(x_0) \\
                f \text{ admet un minimum en } x_0 \text{ sur } I : \ \forall x \in I,\ f(x) \geq f(x_0) \\
                \text{extremum} = \text{maximum ou minimum, sur } D_f \text{ (global) ou sur } I \subset D_f \text{ (local)}
                \end{array}
                """,
                font_size=23,
            ),
            box_width=11.4,
        )
        def_extremum.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "f admet un maximum en x zéro sur I si f de x est "
                "inférieur ou égal à f de x zéro pour tout x de I. Elle "
                "admet un minimum en x zéro si l'inégalité est inversée. "
                "Un extremum est un maximum ou un minimum : on parle "
                "d'extremum global s'il l'est sur tout Df, et d'extremum "
                "local s'il ne l'est que sur un sous-intervalle I."
            )
        ) as tracker:
            self.play(FadeIn(def_extremum))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(def_extremum))

        # --- Majorant / minorant / bornée ---------------------------------
        def_majorant = definition_box(
            MathTex(
                r"""
                \begin{array}{l}
                M \text{ majore } f \text{ sur } D_f : \ \forall x \in D_f,\ f(x) \leq M \\
                m \text{ minore } f \text{ sur } D_f : \ \forall x \in D_f,\ f(x) \geq m \\
                f \text{ bornée} : f \text{ à la fois majorée et minorée}
                \end{array}
                """,
                font_size=25,
            ),
            box_width=9.7,
        )
        def_majorant.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Un réel M est un majorant de f sur Df si f de x est "
                "inférieur ou égal à M pour tout x de Df. Un réel m est un "
                "minorant si f de x est toujours supérieur ou égal à m. "
                "Une fonction est dite bornée lorsqu'elle est à la fois "
                "majorée et minorée."
            )
        ) as tracker:
            self.play(FadeIn(def_majorant))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(def_majorant))

        # --- Animation du raisonnement : remarques importantes ----------------
        remarques = example_box(
            Text(
                _wrap(
                    "Un majorant n'est pas unique : si M majore f, alors "
                    "tout M' ≥ M majore aussi f. Un majorant qui est "
                    "ATTEINT par f est un maximum. Contre-exemple : "
                    "f(x) = 1/(1+x²) est minorée par 0, mais cette borne "
                    "n'est jamais atteinte — 0 n'est donc pas un minimum.",
                    width=56,
                ),
                font_size=22,
            ),
            box_width=11.0,
        )
        remarques.next_to(titre, DOWN, buff=0.55)

        axes = Axes(
            x_range=[-4, 4, 1],
            y_range=[-0.3, 1.3, 1],
            x_length=6.5,
            y_length=2.3,
            axis_config={"color": WHITE, "font_size": 14},
        )
        axes.next_to(remarques, DOWN, buff=0.35)
        courbe = axes.plot(lambda x: 1 / (1 + x**2), x_range=[-3.8, 3.8], color=YELLOW)
        asymptote = DashedLine(axes.c2p(-4, 0), axes.c2p(4, 0), color=WHITE, stroke_width=1.5)
        schema = VGroup(axes, courbe, asymptote)

        with self.voiceover(
            text=(
                "Trois remarques importantes : un majorant n'est jamais "
                "unique — si M majore f, tout nombre plus grand que M "
                "majore aussi f. Ensuite, un majorant qui est effectivement "
                "atteint par la fonction est un maximum. Enfin, "
                "contre-exemple classique : la fonction un sur un plus x "
                "carré est minorée par zéro, mais cette valeur zéro n'est "
                "jamais atteinte — ce n'est donc pas un minimum, seulement "
                "un minorant."
            )
        ) as tracker:
            self.play(FadeIn(remarques))
            self.play(FadeIn(schema))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(remarques), FadeOut(schema))

        # --- Exemple traité 7 -------------------------------------------------
        enonce_ex7 = Text(
            "Exemple 7 — f(x) = 3 + 2x − x², forme canonique",
            font_size=24,
            color=YELLOW,
            weight="BOLD",
        )
        enonce_ex7.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Exemple 7 : étudions f de x égale trois plus deux x moins "
                "x carré, en mettant l'expression sous forme canonique."
            )
        ) as tracker:
            self.play(FadeIn(enonce_ex7))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(enonce_ex7))

        canonique = example_box(
            MathTex(
                r"""
                \begin{array}{l}
                f(x) = -(x^2-2x)+3 = -\big[(x-1)^2-1\big]+3 = 4-(x-1)^2 \\
                \forall x,\ (x-1)^2 \geq 0 \ \Longrightarrow \ f(x) \leq 4 \\
                f(1) = 4 \ \Longrightarrow \ f \text{ atteint } 4 \text{ en } x=1 : \text{maximum global}
                \end{array}
                """,
                font_size=24,
            ),
            box_width=11.0,
        )
        canonique.next_to(titre, DOWN, buff=0.55)

        axes2 = Axes(
            x_range=[-2, 4, 1],
            y_range=[-2, 5, 1],
            x_length=5.5,
            y_length=3.2,
            axis_config={"color": WHITE, "font_size": 14},
        )
        axes2.next_to(canonique, DOWN, buff=0.35)
        courbe2 = axes2.plot(lambda x: 3 + 2 * x - x**2, x_range=[-1.4, 3.4], color=YELLOW)
        sommet = Dot(axes2.c2p(1, 4), color=WHITE)
        schema2 = VGroup(axes2, courbe2, sommet)

        with self.voiceover(
            text=(
                "On factorise par moins un le terme en x carré, puis on "
                "reconnaît le début d'un carré parfait : f de x s'écrit "
                "quatre moins x moins un, le tout au carré. Comme un carré "
                "est toujours positif ou nul, f de x est toujours "
                "inférieur ou égal à quatre. Et comme f de un vaut "
                "exactement quatre, cette valeur est atteinte : quatre "
                "est donc bien un maximum global de f, atteint en x égale "
                "un."
            )
        ) as tracker:
            self.play(FadeIn(canonique))
            self.play(FadeIn(schema2))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(canonique), FadeOut(schema2))

        # --- À retenir ---------------------------------------------------
        retenir = essentiel_box(
            Text(
                _wrap(
                    "Passer par la forme canonique révèle directement le "
                    "majorant (ou minorant) d'une fonction du second "
                    "degré, et précise s'il est atteint (maximum/minimum) "
                    "ou non.",
                    width=56,
                ),
                font_size=23,
            ),
            box_width=10.8,
        )
        retenir.next_to(titre, DOWN, buff=0.6)

        with self.voiceover(
            text=(
                "À retenir : passer par la forme canonique révèle "
                "directement le majorant ou le minorant d'une fonction du "
                "second degré, et permet de savoir immédiatement si cette "
                "borne est atteinte — donc si c'est un véritable maximum "
                "ou minimum."
            )
        ) as tracker:
            self.play(FadeIn(retenir))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(retenir))

        # --- Piège à éviter ----------------------------------------------
        piege = warning_box(
            Text(
                _wrap(
                    "Piège : confondre « f est majorée par M » et « f "
                    "admet un maximum égal à M ». Ce n'est vrai que si M "
                    "est effectivement atteint par f en un point de Df.",
                    width=56,
                ),
                font_size=23,
            ),
            box_width=10.8,
        )
        piege.next_to(titre, DOWN, buff=0.6)

        with self.voiceover(
            text=(
                "Attention : ne pas confondre « f est majorée par M » et "
                "« f admet un maximum égal à M ». La seconde affirmation "
                "n'est vraie que si M est effectivement atteint par f, en "
                "au moins un point de son ensemble de définition."
            )
        ) as tracker:
            self.play(FadeIn(piege))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(titre), FadeOut(piege))
