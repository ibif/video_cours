"""
scenes/Maths_LimitesContinuite_07.py — Chapitre 5 « Limites et continuité »
(1ereC, Maths), scène 07.

Méthode 3 : reconnaître un taux d'accroissement pour lever une F.I. 0/0.
Rappel de la définition (deviendra le nombre dérivé au chapitre suivant).
Exemples résolus 7 et 8, mention du changement de variable.
Source : 1ereC/Maths.pdf, chapitre 5, pages 52-65.
"""

from manim import DOWN, UP, FadeIn, FadeOut, MathTex, Text, VGroup, Write, YELLOW

from shapes.base_scene import NotionScene
from shapes.boxes import definition_box, essentiel_box, example_box, scene_title


class MethodeTauxAccroissement(NotionScene):
    def construct(self):
        titre = scene_title("Méthode 3 — reconnaître un taux d'accroissement")
        titre.scale(0.5)
        titre.to_edge(UP)
        self.play(Write(titre))

        # --- Énoncé : définition du taux d'accroissement -----------------------
        def_taux = definition_box(
            VGroup(
                MathTex(
                    r"\tau(x) = \dfrac{f(x)-f(x_0)}{x-x_0}, \quad x\neq x_0",
                    font_size=30,
                ),
                Text(
                    "s'appelle le taux d'accroissement de f entre x0 et x.",
                    font_size=22,
                ),
            ).arrange(DOWN, buff=0.3),
            box_width=9.5,
        )
        def_taux.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Rappel de définition : pour une fonction f et un point x "
                "zéro de son domaine, le quotient f de x moins f de x "
                "zéro, sur x moins x zéro, s'appelle le taux "
                "d'accroissement de f entre x zéro et x. Sa limite quand x "
                "tend vers x zéro deviendra, au chapitre suivant, le nombre "
                "dérivé de f en x zéro."
            )
        ) as tracker:
            self.play(FadeIn(def_taux))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(def_taux))

        methode_txt = Text(
            "Beaucoup de F.I. en 0/0 sont en réalité un taux d'accroissement déguisé.",
            font_size=24,
        )
        methode_txt.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Troisième méthode : de nombreuses formes indéterminées "
                "zéro sur zéro sont en réalité un taux d'accroissement "
                "déguisé — il suffit de savoir le reconnaître pour "
                "conclure directement."
            )
        ) as tracker:
            self.play(FadeIn(methode_txt))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(methode_txt))

        # --- Exemple 7 : (x³-1)/(x-1) en 1 ---------------------------------------
        ex7_titre = Text("Exemple 7 — lim (x³ - 1)/(x - 1) en x0 = 1 :", font_size=22, color=YELLOW, weight="BOLD")
        ex7_titre.next_to(titre, DOWN, buff=0.35)
        ex7_calc = MathTex(
            r"""
            \begin{array}{l}
            \text{Avec } f(x)=x^3 : \dfrac{x^3-1}{x-1} = \dfrac{f(x)-f(1)}{x-1} = \tau(x)\\
            x^3-1=(x-1)(x^2+x+1) \ \Longrightarrow\ \tau(x) = x^2+x+1 \quad (x\neq 1)\\
            \Longrightarrow\ \lim_{x\to 1} \dfrac{x^3-1}{x-1} = 1+1+1 = 3
            \end{array}
            """,
            font_size=23,
        )
        ex7_calc.next_to(ex7_titre, DOWN, buff=0.35)
        ex7_box = example_box(ex7_calc, box_width=10.5)
        ex7_box.next_to(ex7_titre, DOWN, buff=0.3)

        with self.voiceover(
            text=(
                "Exemple : x cube moins un, sur x moins un, en x égale un. "
                "En posant f de x égale x cube, on reconnaît exactement le "
                "taux d'accroissement de f entre un et x. En factorisant x "
                "cube moins un par x moins un, il reste x carré plus x plus "
                "un, dont la limite en un vaut trois."
            )
        ) as tracker:
            self.play(FadeIn(ex7_titre))
            self.play(FadeIn(ex7_box))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(ex7_titre), FadeOut(ex7_box))

        # --- Exemple 8 : (√(1+x)-1)/x en 0 ---------------------------------------
        ex8_titre = Text("Exemple 8 — lim (√(1+x) - 1)/x en x0 = 0 :", font_size=22, color=YELLOW, weight="BOLD")
        ex8_titre.next_to(titre, DOWN, buff=0.35)
        ex8_calc = MathTex(
            r"""
            \begin{array}{l}
            \text{Avec } f(x)=\sqrt{1+x} : \dfrac{\sqrt{1+x}-1}{x} = \dfrac{f(x)-f(0)}{x-0} = \tau(x)\\
            \text{(conjuguée) } \tau(x) = \dfrac{(1+x)-1}{x(\sqrt{1+x}+1)} = \dfrac{1}{\sqrt{1+x}+1} \quad (x\neq 0)\\
            \Longrightarrow\ \lim_{x\to 0} \dfrac{\sqrt{1+x}-1}{x} = \dfrac{1}{2}
            \end{array}
            """,
            font_size=22,
        )
        ex8_calc.next_to(ex8_titre, DOWN, buff=0.35)
        ex8_box = example_box(ex8_calc, box_width=11.0)
        ex8_box.next_to(ex8_titre, DOWN, buff=0.3)

        with self.voiceover(
            text=(
                "Deuxième exemple : racine de un plus x, moins un, sur x, "
                "en zéro. Avec f de x égale racine de un plus x, c'est le "
                "taux d'accroissement de f entre zéro et x. On combine avec "
                "la méthode de l'expression conjuguée : il reste un sur "
                "racine de un plus x, plus un, dont la limite en zéro vaut "
                "un demi."
            )
        ) as tracker:
            self.play(FadeIn(ex8_titre))
            self.play(FadeIn(ex8_box))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(ex8_titre), FadeOut(ex8_box))

        # --- Mention : changement de variable -----------------------------------
        cv_titre = Text("Cas d'un changement de variable — lim cos(2x) - 1 en 0 :", font_size=20, color=YELLOW, weight="BOLD")
        cv_titre.next_to(titre, DOWN, buff=0.35)
        cv_calc = MathTex(
            r"""
            \begin{array}{l}
            \text{Poser } h=2x : \dfrac{\cos(2x)-1}{2x} = \dfrac{\cos h - 1}{h} \ \underset{h\to 0}{\longrightarrow}\ 0\\
            \text{(taux d'accroissement de } \cos \text{ en } 0\text{)}
            \end{array}
            """,
            font_size=23,
        )
        cv_calc.next_to(cv_titre, DOWN, buff=0.35)

        with self.voiceover(
            text=(
                "Dernier point important : quand la variable n'est pas "
                "directement x, par exemple pour cosinus de deux x moins "
                "un, sur deux x, on effectue un changement de variable, ici "
                "h égale deux x, pour se ramener à un taux d'accroissement "
                "classique de la fonction cosinus en zéro."
            )
        ) as tracker:
            self.play(FadeIn(cv_titre))
            self.play(Write(cv_calc))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(cv_titre), FadeOut(cv_calc))

        # --- À retenir -----------------------------------------------------------
        retenir = essentiel_box(
            Text(
                "Une F.I. en 0/0 de la forme [f(x) - f(x0)] / (x - x0) est un taux "
                "d'accroissement : penser au changement de variable si besoin.",
                font_size=23,
            ),
            box_width=11.5,
        )
        retenir.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "À retenir : dès qu'une forme indéterminée zéro sur zéro a "
                "la forme f de x moins f de x zéro, sur x moins x zéro, "
                "c'est un taux d'accroissement — quitte à faire un "
                "changement de variable pour le faire apparaître."
            )
        ) as tracker:
            self.play(FadeIn(retenir))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(retenir), FadeOut(titre))
