"""
scenes/Maths_Derivation_08.py — Chapitre 9 (1ereC, Maths), scène 08.

Opérations sur les fonctions dérivables : tableau des opérations (somme,
produit par réel, produit, inverse, quotient, puissance uⁿ), démonstration
complète de la formule du produit et de la formule de l'inverse. Exemples
résolus 7, 8, 9, 10.
Source : 1ereC/Maths.pdf, chapitre 9, pages 105-117.
"""

import textwrap

from manim import DOWN, UP, FadeIn, FadeOut, MathTex, Text, VGroup, Write, YELLOW

from shapes.base_scene import NotionScene
from shapes.boxes import example_box, essentiel_box, scene_title, theorem_box


def _wrap(text: str, width: int = 58) -> str:
    return "\n".join(textwrap.fill(line, width=width) for line in text.split("\n"))


class OperationsFonctionsDerivables(NotionScene):
    def construct(self):
        titre = scene_title("Opérations sur les fonctions dérivables")
        titre.scale(0.48)
        titre.to_edge(UP)

        # --- Énoncé ------------------------------------------------------------
        enonce = Text(
            _wrap(
                "Calculer chaque dérivée à partir de la définition serait "
                "long. Existe-t-il des règles pour dériver une somme, un "
                "produit, un quotient de fonctions dérivables ?",
                width=56,
            ),
            font_size=23,
            color=YELLOW,
        )
        enonce.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Revenir systématiquement à la définition du nombre dérivé "
                "pour chaque calcul serait extrêmement long. Existe-t-il "
                "des règles générales pour dériver une somme, un produit ou "
                "un quotient de fonctions dérivables ? La réponse est oui, "
                "et c'est l'objet de cette scène."
            )
        ) as tracker:
            self.play(Write(titre))
            self.play(FadeIn(enonce))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(enonce))

        # --- Théorème : tableau des opérations --------------------------------------
        tableau = MathTex(
            r"""
            \begin{array}{|l|l|}
            \hline
            \text{Fonction} & \text{Dérivée} \\
            \hline
            u+v & u'+v' \\
            k\,u \ (k \in \mathbb{R}) & k\,u' \\
            u\,v & u'v + uv' \\
            \dfrac{1}{v} \ (v \neq 0) & -\dfrac{v'}{v^2} \\
            \dfrac{u}{v} \ (v \neq 0) & \dfrac{u'v - uv'}{v^2} \\
            u^n \ (n \geq 1) & n\,u'\,u^{n-1} \\
            \hline
            \end{array}
            """,
            font_size=27,
        )
        theoreme = theorem_box(
            VGroup(
                Text("Soit u et v dérivables sur un intervalle I :", font_size=22),
                tableau,
            ).arrange(DOWN, buff=0.3),
            box_width=8.6,
        )
        theoreme.next_to(titre, DOWN, buff=0.45)

        with self.voiceover(
            text=(
                "Voici le théorème, à connaître parfaitement, valable pour "
                "u et v deux fonctions dérivables sur un intervalle I. La "
                "dérivée d'une somme u plus v est u prime plus v prime. La "
                "dérivée de k fois u, pour k réel, est k fois u prime. La "
                "dérivée d'un produit u v est u prime v plus u v prime. La "
                "dérivée de l'inverse de v est moins v prime sur v carré. "
                "La dérivée d'un quotient u sur v est u prime v moins u v "
                "prime, le tout sur v carré. Et la dérivée de u puissance "
                "n est n fois u prime fois u puissance n moins un."
            )
        ) as tracker:
            self.play(FadeIn(theoreme))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(theoreme))

        # --- Démonstration du produit --------------------------------------------------
        demo_produit = theorem_box(
            VGroup(
                Text("Démonstration de (uv)' = u'v + uv' :", font_size=20),
                MathTex(
                    r"\dfrac{(uv)(a+h)-(uv)(a)}{h} ="
                    r" \dfrac{u(a+h)v(a+h) - u(a)v(a)}{h}",
                    font_size=21,
                ),
                Text("On ajoute et retranche u(a+h)v(a) :", font_size=19),
                MathTex(
                    r"= \dfrac{u(a+h)v(a+h) - u(a+h)v(a) + u(a+h)v(a) - u(a)v(a)}{h}",
                    font_size=20,
                ),
                MathTex(
                    r"= u(a+h)\dfrac{v(a+h)-v(a)}{h} + v(a)\dfrac{u(a+h)-u(a)}{h}",
                    font_size=21,
                ),
                MathTex(
                    r"\xrightarrow[h \to 0]{} u(a)v'(a) + v(a)u'(a)"
                    r"\quad (u \text{ continue en } a)",
                    font_size=22,
                ),
            ).arrange(DOWN, buff=0.2),
            box_width=11.8,
        )
        demo_produit.next_to(titre, DOWN, buff=0.3)

        with self.voiceover(
            text=(
                "Démontrons la formule du produit. On part du taux "
                "d'accroissement de u fois v en a. La technique clé "
                "consiste à ajouter et retrancher le même terme, u de a "
                "plus h, fois v de a, ce qui ne change rien à la valeur "
                "mais permet de regrouper astucieusement les termes. On "
                "obtient alors u de a plus h, fois le taux d'accroissement "
                "de v, plus v de a, fois le taux d'accroissement de u. "
                "Quand h tend vers zéro, u de a plus h tend vers u de a, "
                "car u est continue en a puisqu'elle est dérivable. On "
                "obtient bien u de a fois v prime de a, plus v de a fois u "
                "prime de a."
            )
        ) as tracker:
            self.play(FadeIn(demo_produit))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(demo_produit))

        # --- Démonstration de l'inverse -------------------------------------------------
        demo_inverse = theorem_box(
            VGroup(
                Text("Démonstration de (1/v)' = -v'/v² (v ≠ 0) :", font_size=20),
                MathTex(
                    r"\dfrac{1}{h}\left(\dfrac{1}{v(a+h)} - \dfrac{1}{v(a)}\right)"
                    r" = \dfrac{1}{h}\cdot\dfrac{v(a)-v(a+h)}{v(a+h)v(a)}",
                    font_size=22,
                ),
                MathTex(
                    r"= -\dfrac{v(a+h)-v(a)}{h}\cdot\dfrac{1}{v(a+h)v(a)}"
                    r"\ \xrightarrow[h \to 0]{}\ -v'(a)\cdot\dfrac{1}{v(a)^2}",
                    font_size=22,
                ),
            ).arrange(DOWN, buff=0.25),
            box_width=11.6,
        )
        demo_inverse.next_to(titre, DOWN, buff=0.45)

        with self.voiceover(
            text=(
                "Démontrons maintenant la formule de l'inverse. On met au "
                "même dénominateur un sur v de a plus h, moins un sur v de "
                "a, ce qui donne v de a moins v de a plus h, sur v de a "
                "plus h fois v de a. On reconnaît, au signe près, le taux "
                "d'accroissement de v. Quand h tend vers zéro, v de a plus "
                "h tend vers v de a par continuité, et on obtient moins v "
                "prime de a, divisé par v de a au carré."
            )
        ) as tracker:
            self.play(FadeIn(demo_inverse))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(demo_inverse))

        # --- Exemples résolus 7, 8, 9, 10 ------------------------------------------------
        exemple7 = example_box(
            VGroup(
                Text("Exemple 7 — f(x) = 3x⁴ - 5x² + 2x - 7 :", font_size=21),
                MathTex(r"f'(x) = 3 \times 4x^3 - 5 \times 2x + 2 = 12x^3 - 10x + 2", font_size=25),
            ).arrange(DOWN, buff=0.25),
            box_width=10.8,
        )
        exemple7.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Exemple sept : pour le polynôme f de x égale trois x "
                "puissance quatre, moins cinq x carré, plus deux x, moins "
                "sept, on dérive terme à terme : f prime de x égale douze x "
                "au cube, moins dix x, plus deux."
            )
        ) as tracker:
            self.play(FadeIn(exemple7))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(exemple7))

        exemple8 = example_box(
            VGroup(
                Text("Exemple 8 — f(x) = (2x+1)(x²-3), par la formule (uv)' :", font_size=20),
                MathTex(
                    r"u=2x+1,\ u'=2 \quad v=x^2-3,\ v'=2x",
                    font_size=23,
                ),
                MathTex(
                    r"f'(x) = 2(x^2-3) + (2x+1)(2x) = 6x^2+2x-6",
                    font_size=25,
                ),
                Text("Vérification en développant f(x) d'abord : même résultat.", font_size=18),
            ).arrange(DOWN, buff=0.22),
            box_width=11.6,
        )
        exemple8.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Exemple huit : soit f de x égale le produit de deux x plus "
                "un, par x carré moins trois. On pose u égale deux x plus "
                "un, de dérivée deux, et v égale x carré moins trois, de "
                "dérivée deux x. La formule du produit donne : f prime de x "
                "égale deux fois x carré moins trois, plus deux x plus un, "
                "fois deux x, ce qui se simplifie en six x carré plus deux "
                "x moins six. On peut vérifier ce résultat en développant "
                "d'abord f de x avant de dériver : on retrouve exactement "
                "la même expression, ce qui confirme le calcul."
            )
        ) as tracker:
            self.play(FadeIn(exemple8))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(exemple8))

        exemple9 = example_box(
            VGroup(
                Text("Exemple 9 — f(x) = (x+1)/(2x-3), quotient sur x ≠ 3/2 :", font_size=20),
                MathTex(
                    r"u=x+1,\ u'=1 \quad v=2x-3,\ v'=2",
                    font_size=23,
                ),
                MathTex(
                    r"f'(x) = \dfrac{1\times(2x-3) - (x+1)\times 2}{(2x-3)^2}"
                    r" = \dfrac{-5}{(2x-3)^2}",
                    font_size=25,
                ),
            ).arrange(DOWN, buff=0.25),
            box_width=11.4,
        )
        exemple9.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Exemple neuf : soit f de x égale le quotient x plus un, "
                "sur deux x moins trois, défini pour x différent de trois "
                "demis. On pose u égale x plus un, de dérivée un, et v "
                "égale deux x moins trois, de dérivée deux. La formule du "
                "quotient donne : f prime de x égale un fois deux x moins "
                "trois, moins x plus un fois deux, le tout sur deux x moins "
                "trois au carré, ce qui se simplifie en moins cinq, sur "
                "deux x moins trois au carré."
            )
        ) as tracker:
            self.play(FadeIn(exemple9))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(exemple9))

        exemple10 = example_box(
            VGroup(
                Text("Exemple 10 — f(x) = (x²+1)³, avec la formule (uⁿ)' :", font_size=21),
                MathTex(
                    r"u=x^2+1,\ u'=2x,\ n=3 \quad\Longrightarrow\quad "
                    r"f'(x) = 3\times 2x \times (x^2+1)^2 = 6x(x^2+1)^2",
                    font_size=24,
                ),
            ).arrange(DOWN, buff=0.25),
            box_width=11.6,
        )
        exemple10.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Exemple dix : soit f de x égale x carré plus un, le tout "
                "au cube. On pose u égale x carré plus un, de dérivée deux "
                "x, avec n égale trois. La formule de la puissance donne "
                "directement : f prime de x égale trois fois deux x, fois x "
                "carré plus un au carré, c'est-à-dire six x fois x carré "
                "plus un au carré."
            )
        ) as tracker:
            self.play(FadeIn(exemple10))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(exemple10))

        # --- À retenir ------------------------------------------------------------------
        retenir = essentiel_box(
            Text(
                _wrap(
                    "Les formules (u+v)', (ku)', (uv)', (1/v)', (u/v)', "
                    "(uⁿ)' permettent de dériver toute combinaison de "
                    "fonctions usuelles sans revenir à la définition. "
                    "Toujours identifier clairement u et v avant "
                    "d'appliquer une formule.",
                    width=58,
                ),
                font_size=21,
            )
        )
        retenir.next_to(titre, DOWN, buff=0.6)

        with self.voiceover(
            text=(
                "À retenir : les formules de dérivation d'une somme, d'un "
                "produit par une constante, d'un produit, d'un inverse, "
                "d'un quotient et d'une puissance permettent de dériver "
                "toute combinaison de fonctions usuelles, sans jamais "
                "revenir à la définition du nombre dérivé. Le bon réflexe "
                "est toujours d'identifier clairement u et v avant "
                "d'appliquer la bonne formule."
            )
        ) as tracker:
            self.play(FadeIn(retenir))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(titre), FadeOut(retenir))
