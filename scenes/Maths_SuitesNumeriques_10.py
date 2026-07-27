"""
scenes/Maths_SuitesNumeriques_10.py — Chapitre 15 « Suites numériques »
(1ereC, Maths), scène 10.

Limite de qⁿ (théorème + démonstration du cas |q|<1, au programme) et
suites arithmético-géométriques : méthode du point fixe complète. Exemple
résolu 10.
Source : 1ereC/Maths.pdf, chapitre 15, pages 176-188.
"""

import textwrap

from manim import DOWN, UP, FadeIn, FadeOut, MathTex, Text, VGroup, Write, YELLOW

from shapes.base_scene import NotionScene
from shapes.boxes import definition_box, essentiel_box, example_box, method_box, scene_title, theorem_box, warning_box


def _wrap(text: str, width: int = 58) -> str:
    return "\n".join(textwrap.fill(line, width=width) for line in text.split("\n"))


class LimiteQnEtArithmeticoGeometrique(NotionScene):
    def construct(self):
        titre = scene_title("Limite de qⁿ — suites arithmético-géométriques")
        titre.scale(0.44)
        titre.to_edge(UP)
        self.play(Write(titre))

        # --- Énoncé : théorème limite de qⁿ -------------------------------------
        theo_qn = theorem_box(
            VGroup(
                Text("Limite de qⁿ quand n tend vers +∞ :", font_size=22, weight="BOLD"),
                MathTex(r"|q|<1 \Longrightarrow q^n \longrightarrow 0", font_size=25),
                MathTex(r"q=1 \Longrightarrow q^n \longrightarrow 1", font_size=25),
                MathTex(r"q>1 \Longrightarrow q^n \longrightarrow +\infty", font_size=25),
                MathTex(r"q\leq -1 \Longrightarrow q^n \text{ n'a pas de limite}", font_size=25),
            ).arrange(DOWN, buff=0.2),
            box_width=10.4,
        )
        theo_qn.next_to(titre, DOWN, buff=0.35)

        with self.voiceover(
            text=(
                "Théorème sur la limite de q puissance n, quand n tend "
                "vers plus l'infini : si la valeur absolue de q est "
                "strictement inférieure à un, alors q puissance n tend "
                "vers zéro. Si q vaut un, q puissance n vaut toujours un. "
                "Si q est strictement supérieur à un, q puissance n tend "
                "vers plus l'infini. Et si q est inférieur ou égal à moins "
                "un, q puissance n n'a pas de limite, car elle oscille en "
                "changeant de signe."
            )
        ) as tracker:
            self.play(FadeIn(theo_qn))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(theo_qn))

        # --- Démonstration du cas |q| < 1 (au programme) --------------------------
        demo_titre = Text(
            "Démonstration du cas 0 < q < 1 (au programme) :",
            font_size=22,
            color=YELLOW,
            weight="BOLD",
        )
        demo_titre.next_to(titre, DOWN, buff=0.35)
        demo = VGroup(
            MathTex(
                r"\text{On pose } q = \dfrac{1}{1+a} \text{ avec } a>0 \ (\text{car } 0<q<1).",
                font_size=23,
            ),
            MathTex(
                r"\text{L'inégalité de Bernoulli donne : } (1+a)^n \geq 1+na",
                font_size=23,
            ),
            MathTex(
                r"0 < q^n = \dfrac{1}{(1+a)^n} \leq \dfrac{1}{1+na}",
                font_size=25,
            ),
            Text(
                "Or 1/(1+na) tend vers 0 quand n tend vers +∞ (n au dénominateur) :",
                font_size=20,
            ),
            MathTex(
                r"\text{par comparaison (théorème des gendarmes), } q^n \longrightarrow 0.",
                font_size=23,
            ),
        ).arrange(DOWN, buff=0.2)
        demo.next_to(demo_titre, DOWN, buff=0.3)

        with self.voiceover(
            text=(
                "Démontrons le cas où q est strictement compris entre zéro "
                "et un, qui est au programme. On pose q égale un sur un "
                "plus a, avec a strictement positif. L'inégalité de "
                "Bernoulli donne : un plus a, puissance n, est supérieur "
                "ou égal à un plus n a. En passant à l'inverse, q "
                "puissance n est compris entre zéro et un sur un plus n "
                "a. Or cette dernière quantité tend vers zéro, puisque n a "
                "tend vers plus l'infini. Par le théorème des gendarmes, q "
                "puissance n tend donc vers zéro."
            )
        ) as tracker:
            self.play(FadeIn(demo_titre))
            self.play(FadeIn(demo))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(demo_titre), FadeOut(demo))

        # --- Énoncé : suite arithmético-géométrique --------------------------------
        definition = definition_box(
            VGroup(
                Text(
                    "(un) est arithmético-géométrique s'il existe deux réels\n"
                    "a et b tels que, pour tout n :",
                    font_size=22,
                ),
                MathTex(r"u_{n+1} = a\,u_n + b", font_size=32),
                Text(
                    "(arithmétique si a = 1, géométrique si b = 0)",
                    font_size=20,
                ),
            ).arrange(DOWN, buff=0.25),
            box_width=10.2,
        )
        definition.next_to(titre, DOWN, buff=0.35)

        with self.voiceover(
            text=(
                "Une suite u indice n est dite arithmético-géométrique "
                "s'il existe deux réels a et b tels que, pour tout n, u "
                "indice n plus un égale a fois u indice n, plus b. On "
                "retrouve une suite arithmétique si a vaut un, et une "
                "suite géométrique si b vaut zéro."
            )
        ) as tracker:
            self.play(FadeIn(definition))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(definition))

        # --- Méthode du point fixe --------------------------------------------------
        methode = method_box(
            VGroup(
                Text("Méthode du point fixe (pour a ≠ 1) :", font_size=22, weight="BOLD"),
                MathTex(r"1)\ \text{résoudre } \ell = a\ell+b \Longrightarrow \ell = \dfrac{b}{1-a}", font_size=24),
                MathTex(r"2)\ \text{poser } v_n = u_n-\ell \ : \ (v_n) \text{ est géométrique de raison } a", font_size=24),
                MathTex(r"3)\ v_n = (u_0-\ell)\,a^n \Longrightarrow u_n = (u_0-\ell)\,a^n+\ell", font_size=24),
            ).arrange(DOWN, buff=0.25),
            box_width=11.4,
        )
        methode.next_to(titre, DOWN, buff=0.35)

        with self.voiceover(
            text=(
                "Méthode du point fixe pour résoudre entièrement une suite "
                "arithmético-géométrique, avec a différent de un. Première "
                "étape : on résout l'équation ℓ égale a ℓ plus b, qui "
                "donne le point fixe ℓ égale b sur un moins a. Deuxième "
                "étape : on pose v indice n égale u indice n moins ℓ ; "
                "cette nouvelle suite est géométrique de raison a. "
                "Troisième étape : on en déduit v indice n, puis u indice "
                "n, en ajoutant de nouveau ℓ."
            )
        ) as tracker:
            self.play(FadeIn(methode))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(methode))

        # --- Exemple résolu 10 -----------------------------------------------------
        ex10_titre = Text(
            "Exemple 10 — u0 = 1, un+1 = 2un + 3 :",
            font_size=23,
            color=YELLOW,
            weight="BOLD",
        )
        ex10_titre.next_to(titre, DOWN, buff=0.35)
        ex10_calc = example_box(
            VGroup(
                MathTex(
                    r"\ell = 2\ell+3 \Longrightarrow -\ell=3 \Longrightarrow \ell=-3",
                    font_size=24,
                ),
                MathTex(
                    r"v_n=u_n+3 \ \Longrightarrow\ v_{n+1}=u_{n+1}+3=2u_n+6=2(u_n+3)=2v_n",
                    font_size=22,
                ),
                MathTex(
                    r"(v_n) \text{ géométrique de raison } 2, \ v_0=u_0+3=4 \Longrightarrow v_n=4\times 2^n=2^{n+2}",
                    font_size=22,
                ),
                MathTex(
                    r"u_n = v_n-3 = 2^{n+2}-3",
                    font_size=27,
                ),
            ).arrange(DOWN, buff=0.25),
            box_width=11.6,
        )
        ex10_calc.next_to(ex10_titre, DOWN, buff=0.25)

        with self.voiceover(
            text=(
                "Exemple : u zéro égale un, et u indice n plus un égale "
                "deux fois u indice n, plus trois. Le point fixe vérifie "
                "ℓ égale deux ℓ plus trois, donc ℓ égale moins trois. On "
                "pose v indice n égale u indice n plus trois : on vérifie "
                "que v indice n plus un égale deux fois v indice n, donc v "
                "indice n est géométrique de raison deux, avec v zéro "
                "égale quatre. On obtient v indice n égale quatre fois "
                "deux puissance n, soit deux puissance n plus deux. "
                "Finalement, u indice n égale deux puissance n plus deux, "
                "moins trois."
            )
        ) as tracker:
            self.play(FadeIn(ex10_titre))
            self.play(FadeIn(ex10_calc))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(ex10_titre), FadeOut(ex10_calc))

        # --- À retenir -----------------------------------------------------------
        retenir = essentiel_box(
            Text(
                _wrap(
                    "qⁿ tend vers 0 si |q| < 1. Suite arithmético-"
                    "géométrique un+1 = a un + b (a ≠ 1) : point fixe ℓ = "
                    "b/(1-a), vn = un - ℓ géométrique de raison a, un = "
                    "(u0 - ℓ)aⁿ + ℓ.",
                    width=58,
                ),
                font_size=21,
            ),
            box_width=11.4,
        )
        retenir.next_to(titre, DOWN, buff=0.35)

        with self.voiceover(
            text=(
                "À retenir : q puissance n tend vers zéro dès que la "
                "valeur absolue de q est strictement inférieure à un. Pour "
                "une suite arithmético-géométrique, la méthode du point "
                "fixe la ramène systématiquement à une suite géométrique "
                "auxiliaire, qu'on sait parfaitement étudier."
            )
        ) as tracker:
            self.play(FadeIn(retenir))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(retenir))

        # --- Piège à éviter ----------------------------------------------------
        piege = warning_box(
            Text(
                _wrap(
                    "Piège : une suite arithmético-géométrique (a ≠ 1 et b "
                    "≠ 0) n'est NI arithmétique, NI géométrique. Elle ne "
                    "vérifie pas directement le théorème du terme général "
                    "vu pour ces deux cas : il faut absolument passer par "
                    "la suite auxiliaire (vn).",
                    width=56,
                ),
                font_size=21,
            ),
            box_width=11.5,
        )
        piege.next_to(titre, DOWN, buff=0.35)

        with self.voiceover(
            text=(
                "Piège à éviter absolument : une suite arithmético-"
                "géométrique n'est ni arithmétique, ni géométrique, dès "
                "que a est différent de un et b différent de zéro. On ne "
                "peut donc jamais lui appliquer directement les formules "
                "du terme général vues précédemment : il faut "
                "systématiquement passer par la suite auxiliaire v indice "
                "n."
            )
        ) as tracker:
            self.play(FadeIn(piege))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(piege), FadeOut(titre))
