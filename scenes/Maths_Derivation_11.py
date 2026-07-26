"""
scenes/Maths_Derivation_11.py — Chapitre 9 (1ereC, Maths), scène 11.

Extremums locaux : définition maximum/minimum local, condition nécessaire
f'(c)=0 avec démonstration (cas h>0 et h<0), réciproque fausse (x³ en 0),
condition suffisante (changement de signe). Exemple résolu 14.
Source : 1ereC/Maths.pdf, chapitre 9, pages 105-117.
"""

import textwrap

from manim import (
    DOWN,
    LEFT,
    RIGHT,
    UP,
    WHITE,
    YELLOW,
    Axes,
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
from shapes.boxes import definition_box, essentiel_box, example_box, scene_title, theorem_box, warning_box


def _wrap(text: str, width: int = 58) -> str:
    return "\n".join(textwrap.fill(line, width=width) for line in text.split("\n"))


class ExtremumsLocaux(NotionScene):
    def construct(self):
        titre = scene_title("Extremums locaux")
        titre.scale(0.6)
        titre.to_edge(UP)

        # --- Énoncé -----------------------------------------------------------------
        enonce = Text(
            _wrap(
                "Dans l'exemple précédent, la courbe présentait un point "
                "haut en x=-1 et un point bas en x=1. Comment définir et "
                "repérer ces points précisément ?",
                width=56,
            ),
            font_size=24,
            color=YELLOW,
        )
        enonce.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Dans l'exemple précédent, la courbe de f présentait un "
                "point haut local en x égale moins un, et un point bas "
                "local en x égale un. Comment définir précisément ces "
                "points, et comment les repérer à coup sûr grâce à la "
                "dérivée ?"
            )
        ) as tracker:
            self.play(Write(titre))
            self.play(FadeIn(enonce))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(enonce))

        # --- Définition maximum / minimum local ---------------------------------------
        definition = definition_box(
            VGroup(
                Text(
                    "f admet un maximum local en c s'il existe un\n"
                    "intervalle ouvert J contenant c tel que :",
                    font_size=21,
                ),
                MathTex(r"\forall x \in J,\ f(x) \leq f(c)", font_size=27),
                Text("(minimum local : inégalité inversée f(x) ≥ f(c))", font_size=19),
            ).arrange(DOWN, buff=0.25),
            box_width=10.4,
        )
        definition.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Définition : f admet un maximum local en c s'il existe un "
                "intervalle ouvert J contenant c, tel que pour tout x de J, "
                "f de x soit inférieur ou égal à f de c. Autrement dit, c "
                "est un sommet local, pas forcément le plus haut point de "
                "toute la courbe. On définit de la même façon un minimum "
                "local, avec l'inégalité inversée."
            )
        ) as tracker:
            self.play(FadeIn(definition))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(definition))

        # --- Théorème : condition nécessaire f'(c) = 0, avec démonstration ------------
        theoreme1 = theorem_box(
            VGroup(
                Text("Si f est dérivable en c et admet un extremum local en c :", font_size=21),
                MathTex(r"f'(c) = 0", font_size=32),
            ).arrange(DOWN, buff=0.3),
            box_width=9.4,
        )
        theoreme1.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Voici la condition nécessaire : si f est dérivable en c, "
                "et admet un extremum local en c, alors f prime de c est "
                "nécessairement nul."
            )
        ) as tracker:
            self.play(FadeIn(theoreme1))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(theoreme1))

        demo = theorem_box(
            VGroup(
                Text("Démonstration (cas maximum local) :", font_size=20),
                MathTex(
                    r"h>0 \text{ petit : } \dfrac{f(c+h)-f(c)}{h} \leq 0"
                    r"\ \Longrightarrow\ f'(c) = \lim_{h \to 0^+} \leq 0",
                    font_size=21,
                ),
                MathTex(
                    r"h<0 \text{ petit : } \dfrac{f(c+h)-f(c)}{h} \geq 0"
                    r"\ \Longrightarrow\ f'(c) = \lim_{h \to 0^-} \geq 0",
                    font_size=21,
                ),
                Text("f'(c) ≤ 0 et f'(c) ≥ 0 en même temps : donc f'(c) = 0.", font_size=19),
            ).arrange(DOWN, buff=0.22),
            box_width=11.6,
        )
        demo.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Démontrons ce résultat dans le cas d'un maximum local. "
                "Pour h positif et petit, f de c plus h est inférieur ou "
                "égal à f de c, donc le taux d'accroissement, quotient d'un "
                "numérateur négatif ou nul par h positif, est négatif ou "
                "nul : sa limite à droite, qui vaut f prime de c, est donc "
                "négative ou nulle. Pour h négatif et petit, c'est "
                "l'inverse : le numérateur reste négatif ou nul, mais h est "
                "négatif, donc le quotient est positif ou nul : sa limite à "
                "gauche, qui vaut aussi f prime de c puisque f est "
                "dérivable, est donc positive ou nulle. f prime de c est "
                "donc à la fois négatif ou nul, et positif ou nul : il ne "
                "peut être que nul."
            )
        ) as tracker:
            self.play(FadeIn(demo))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(demo))

        # --- Réciproque fausse : x³ en 0 -----------------------------------------------
        axes = Axes(
            x_range=[-1.5, 1.5, 1],
            y_range=[-1.5, 1.5, 1],
            x_length=4.4,
            y_length=3.2,
            axis_config={"include_tip": True, "stroke_width": 2, "color": WHITE},
        )
        axes.next_to(titre, DOWN, buff=0.5).shift(LEFT * 3.0)
        courbe = axes.plot(lambda x: x**3, x_range=[-1.15, 1.15], color=YELLOW)
        origine = Dot(axes.c2p(0, 0), color=WHITE, radius=0.06)
        figure = VGroup(axes, courbe, origine)

        reciproque = warning_box(
            VGroup(
                Text("Réciproque FAUSSE : f'(c)=0 n'implique pas extremum.", font_size=20),
                MathTex(
                    r"f(x)=x^3 : \ f'(x)=3x^2,\ f'(0)=0,"
                    r"\text{ mais } f \text{ est croissante sur } \mathbb{R}",
                    font_size=20,
                ),
                Text("(pas d'extremum en 0 : point d'inflexion)", font_size=18),
            ).arrange(DOWN, buff=0.2),
            box_width=6.9,
        )
        reciproque.next_to(axes, RIGHT, buff=0.5)

        with self.voiceover(
            text=(
                "Attention : la réciproque est fausse. Ce n'est pas parce "
                "que f prime de c est nul que f admet un extremum local en "
                "c. Contre-exemple classique : f de x égale x au cube. Sa "
                "dérivée, trois x carré, s'annule bien en zéro, mais f est "
                "strictement croissante sur l'ensemble des réels : il n'y a "
                "pas d'extremum en zéro, seulement un point d'inflexion, où "
                "la tangente traverse la courbe."
            )
        ) as tracker:
            self.play(Create(axes), Create(courbe), FadeIn(origine))
            self.play(FadeIn(reciproque))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(figure), FadeOut(reciproque))

        # --- Théorème : condition suffisante (changement de signe) --------------------
        theoreme2 = theorem_box(
            Text(
                _wrap(
                    "Condition suffisante : si f' s'annule en c en "
                    "CHANGEANT de signe, alors f admet un extremum local "
                    "en c (maximum si f' passe de + à -, minimum si f' "
                    "passe de - à +).",
                    width=52,
                ),
                font_size=22,
            ),
            box_width=10.6,
        )
        theoreme2.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Voici enfin la condition suffisante, la plus utile en "
                "pratique : si f prime s'annule en c en changeant "
                "réellement de signe, alors f admet bien un extremum local "
                "en c. Si f prime passe du positif au négatif, c'est un "
                "maximum local ; si f prime passe du négatif au positif, "
                "c'est un minimum local."
            )
        ) as tracker:
            self.play(FadeIn(theoreme2))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(theoreme2))

        # --- Exemple résolu 14 : f(x) = x²-6x+5 ---------------------------------------
        exemple = example_box(
            VGroup(
                Text("Exemple 14 — f(x) = x²-6x+5 :", font_size=22),
                MathTex(r"f'(x) = 2x-6 = 2(x-3)", font_size=27),
                MathTex(
                    r"""
                    \begin{array}{c|ccccc}
                    x & -\infty & & 3 & & +\infty \\
                    \hline
                    f'(x) & & - & 0 & + & \\
                    \end{array}
                    """,
                    font_size=22,
                ),
                Text("f' change de signe (- puis +) en x=3 : minimum local.", font_size=20),
                MathTex(r"f(3) = 9-18+5 = -4", font_size=25),
            ).arrange(DOWN, buff=0.22),
            box_width=10.8,
        )
        exemple.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Exemple : soit f de x égale x carré moins six x plus cinq. "
                "Sa dérivée vaut deux x moins six, qui se factorise en deux "
                "fois x moins trois, et s'annule en x égale trois. La "
                "dérivée est négative avant trois, positive après : elle "
                "change bien de signe, de moins à plus, donc f admet un "
                "minimum local en x égale trois. On calcule f de trois, qui "
                "vaut neuf moins dix-huit plus cinq, c'est-à-dire moins "
                "quatre."
            )
        ) as tracker:
            self.play(FadeIn(exemple))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(exemple))

        # --- À retenir ------------------------------------------------------------------
        retenir = essentiel_box(
            Text(
                _wrap(
                    "Extremum local en c dérivable ⟹ f'(c)=0 (nécessaire, "
                    "mais pas suffisant, voir x³). Pour CONCLURE à un "
                    "extremum, il faut un changement de signe de f' en c "
                    "(condition suffisante).",
                    width=58,
                ),
                font_size=22,
            )
        )
        retenir.next_to(titre, DOWN, buff=0.6)

        with self.voiceover(
            text=(
                "À retenir : un extremum local en c, où f est dérivable, "
                "entraîne toujours f prime de c égale zéro, mais cette "
                "condition seule ne suffit pas à conclure, comme le montre "
                "l'exemple de x au cube. Pour affirmer l'existence d'un "
                "extremum, il faut impérativement vérifier que f prime "
                "change effectivement de signe en c."
            )
        ) as tracker:
            self.play(FadeIn(retenir))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(titre), FadeOut(retenir))
