"""
scenes/Maths_Derivation_01.py — Chapitre 9 (1ereC, Maths), scène 01.

Taux d'accroissement : mise en situation (camion Daloa-Abidjan, vitesse
moyenne), définition du taux d'accroissement τ_a(h), interprétation
graphique comme coefficient directeur d'une sécante, exemple résolu avec
f(x) = x².
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
    Line,
    MathTex,
    Text,
    VGroup,
    Write,
)

from shapes.base_scene import NotionScene
from shapes.boxes import definition_box, essentiel_box, example_box, scene_title


def _wrap(text: str, width: int = 58) -> str:
    return "\n".join(textwrap.fill(line, width=width) for line in text.split("\n"))


class TauxAccroissement(NotionScene):
    def construct(self):
        titre = scene_title("Taux d'accroissement")
        titre.scale(0.55)
        titre.to_edge(UP)

        # --- Énoncé : mise en situation ------------------------------------
        situation = Text(
            _wrap(
                "Un camion parcourt les 400 km entre Daloa et Abidjan. "
                "Sa position dépend du temps : d(t). Quelle est sa vitesse "
                "moyenne entre deux instants donnés ?",
                width=56,
            ),
            font_size=26,
        )
        situation.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Imaginons un camion qui roule de Daloa vers Abidjan. Sa "
                "position sur la route, à l'instant t, est donnée par une "
                "fonction d de t. Une question naturelle se pose : quelle "
                "est la vitesse moyenne de ce camion entre deux instants "
                "donnés ? C'est exactement cette idée de variation moyenne "
                "que nous allons formaliser aujourd'hui."
            )
        ) as tracker:
            self.play(Write(titre))
            self.play(FadeIn(situation))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(situation))

        vitesse_moy = MathTex(
            r"v_{\text{moy}} = \dfrac{d(t_2) - d(t_1)}{t_2 - t_1}",
            font_size=34,
        )
        vitesse_moy.next_to(titre, DOWN, buff=0.6)

        with self.voiceover(
            text=(
                "La vitesse moyenne, c'est la distance parcourue divisée "
                "par le temps mis pour la parcourir : d de t deux, moins d "
                "de t un, le tout divisé par t deux moins t un. C'est "
                "exactement cette forme de quotient — variation de la "
                "fonction sur variation de la variable — que l'on retrouve "
                "partout en mathématiques, sous le nom de taux "
                "d'accroissement."
            )
        ) as tracker:
            self.play(Write(vitesse_moy))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(vitesse_moy))

        # --- Définition ------------------------------------------------------
        definition = definition_box(
            VGroup(
                Text(
                    _wrap(
                        "Soit f une fonction définie sur un intervalle I, "
                        "a ∈ I et h un réel non nul tel que a+h ∈ I. On "
                        "appelle taux d'accroissement de f entre a et a+h "
                        "le nombre :",
                        width=54,
                    ),
                    font_size=22,
                ),
                MathTex(
                    r"\tau_a(h) = \dfrac{f(a+h) - f(a)}{h}",
                    font_size=32,
                ),
            ).arrange(DOWN, buff=0.3),
            box_width=11.2,
        )
        definition.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Voici la définition générale. Soit f une fonction définie "
                "sur un intervalle I, a un réel de I, et h un réel non nul "
                "tel que a plus h reste dans I. On appelle taux "
                "d'accroissement de f entre a et a plus h le nombre tau "
                "indice a de h, égal à f de a plus h, moins f de a, le tout "
                "divisé par h."
            )
        ) as tracker:
            self.play(FadeIn(definition))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(definition))

        # --- Interprétation graphique : coefficient directeur de la sécante --
        axes = Axes(
            x_range=[-0.5, 3, 1],
            y_range=[-0.5, 6, 1],
            x_length=5.8,
            y_length=4.2,
            axis_config={"include_tip": True, "stroke_width": 2, "color": WHITE},
        )
        axes.next_to(titre, DOWN, buff=0.5).shift(LEFT * 2.4)

        courbe = axes.plot(lambda x: x**2, x_range=[-0.3, 2.6], color=YELLOW)
        a_val, h_val = 0.8, 1.3
        point_a = Dot(axes.c2p(a_val, a_val**2), color=WHITE, radius=0.07)
        point_ah = Dot(axes.c2p(a_val + h_val, (a_val + h_val) ** 2), color=WHITE, radius=0.07)
        secante = Line(
            axes.c2p(-0.2, (a_val - 0.9) ** 2 - 0.55),
            axes.c2p(2.5, 5.2),
            color="#DE7C1F",
        )
        label_a = MathTex("A", font_size=26).next_to(point_a, DOWN, buff=0.12)
        label_ah = MathTex("M", font_size=26).next_to(point_ah, RIGHT, buff=0.12)

        legende = VGroup(
            Text("τ_a(h) = coefficient directeur", font_size=22, color=YELLOW),
            Text("de la sécante (AM)", font_size=22, color=YELLOW),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.1)
        legende.next_to(axes, RIGHT, buff=0.5)

        figure = VGroup(axes, courbe, secante, point_a, point_ah, label_a, label_ah)

        with self.voiceover(
            text=(
                "Interprétons ce taux d'accroissement graphiquement. Sur la "
                "courbe de f, plaçons le point A d'abscisse a et le point M "
                "d'abscisse a plus h. Le taux d'accroissement tau indice a "
                "de h n'est rien d'autre que le coefficient directeur de la "
                "droite sécante qui passe par ces deux points A et M."
            )
        ) as tracker:
            self.play(Create(axes))
            self.play(Create(courbe))
            self.play(FadeIn(point_a), FadeIn(point_ah), Write(label_a), Write(label_ah))
            self.play(Create(secante), FadeIn(legende))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(figure), FadeOut(legende))

        # --- Exemple résolu : f(x) = x², taux entre 1 et 1+h ------------------
        exemple = example_box(
            VGroup(
                Text("f(x) = x², taux d'accroissement entre 1 et 1+h :", font_size=22),
                MathTex(
                    r"\tau_1(h) = \dfrac{f(1+h)-f(1)}{h}"
                    r" = \dfrac{(1+h)^2 - 1}{h} = \dfrac{2h+h^2}{h} = 2+h",
                    font_size=27,
                ),
                Text("Quand h se rapproche de 0, τ₁(h) se rapproche de 2.", font_size=22),
            ).arrange(DOWN, buff=0.3),
            box_width=11.4,
        )
        exemple.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Prenons un exemple concret : f de x égale x carré, et "
                "calculons le taux d'accroissement entre un et un plus h. "
                "On développe : un plus h au carré, moins un, le tout "
                "divisé par h, ce qui donne deux h plus h carré, divisé par "
                "h, soit finalement deux plus h, après simplification par "
                "h qui est non nul. On observe que lorsque h se rapproche "
                "de zéro, ce taux tau indice un de h se rapproche de deux."
            )
        ) as tracker:
            self.play(FadeIn(exemple))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(exemple))

        # --- À retenir ---------------------------------------------------------
        retenir = essentiel_box(
            Text(
                _wrap(
                    "Le taux d'accroissement τ_a(h) = [f(a+h)-f(a)]/h "
                    "mesure une variation moyenne de f. Graphiquement, "
                    "c'est le coefficient directeur d'une sécante. Il "
                    "dépend de h : quand h varie, la sécante pivote.",
                    width=58,
                ),
                font_size=23,
            )
        )
        retenir.next_to(titre, DOWN, buff=0.6)

        with self.voiceover(
            text=(
                "À retenir : le taux d'accroissement tau indice a de h "
                "mesure une variation moyenne de la fonction f entre a et a "
                "plus h. Graphiquement, c'est le coefficient directeur "
                "d'une sécante à la courbe. Il dépend de la valeur de h : "
                "quand h varie, la sécante pivote autour du point A. C'est "
                "cette observation, faire tendre h vers zéro, qui va nous "
                "mener tout naturellement au nombre dérivé dans la scène "
                "suivante."
            )
        ) as tracker:
            self.play(FadeIn(retenir))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(titre), FadeOut(retenir))
