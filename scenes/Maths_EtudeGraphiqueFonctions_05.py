"""
scenes/Maths_EtudeGraphiqueFonctions_05.py — Chapitre 11 (1ereC, Maths), scène 05.

Étude complète d'une fonction polynôme du 3e degré : forme générale, dérivée
et discriminant, théorème du point d'inflexion toujours centre de symétrie,
exemple résolu complet f(x) = x³ - 3x + 2.
Source : 1ereC/Maths.pdf, chapitre 11, pages 130-141.
"""

import textwrap

from manim import DOWN, LEFT, RIGHT, UP, WHITE, YELLOW, Axes, Dot, FadeIn, FadeOut, MathTex, Text, VGroup, Write

from shapes.base_scene import NotionScene
from shapes.boxes import essentiel_box, example_box, scene_title, theorem_box, warning_box


def _wrap(text: str, width: int = 58) -> str:
    return "\n".join(textwrap.fill(line, width=width) for line in text.split("\n"))


class EtudePolynomeDegreTrois(NotionScene):
    def construct(self):
        titre = scene_title("Étude d'une fonction polynôme du 3e degré")
        titre.scale(0.48)
        titre.to_edge(UP)

        # --- Énoncé ------------------------------------------------------------
        enonce = Text(
            "Appliquons le plan complet à f(x) = ax³ + bx² + cx + d",
            font_size=25,
            color=YELLOW,
            weight="BOLD",
        )
        enonce.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Première famille de fonctions : les polynômes du troisième "
                "degré, de la forme f de x égale a x au cube plus b x carré "
                "plus c x plus d, avec a non nul. Voyons ce que donne le "
                "plan d'étude dans ce cas particulier."
            )
        ) as tracker:
            self.play(Write(titre))
            self.play(FadeIn(enonce))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(enonce))

        # --- Cadre général : domaine et dérivée ------------------------------
        cadre_general = example_box(
            MathTex(
                r"""
                D_f = \mathbb{R} \qquad
                f'(x) = 3ax^2+2bx+c \qquad
                \Delta' = 4b^2-12ac
                """,
                font_size=27,
            ),
            box_width=11.4,
        )
        cadre_general.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Un polynôme est toujours défini sur ℝ tout entier : "
                "l'étape du domaine est immédiate. Sa dérivée f prime de x "
                "vaut trois a x carré plus deux b x plus c, un trinôme du "
                "second degré, dont on étudie le signe grâce à son "
                "discriminant réduit delta prime égale quatre b carré "
                "moins douze a c."
            )
        ) as tracker:
            self.play(FadeIn(cadre_general))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(cadre_general))

        # --- Théorème point d'inflexion / centre de symétrie -----------------
        theo_inflexion = theorem_box(
            VGroup(
                Text(
                    "Le point d'inflexion d'abscisse x0 = -b/(3a) est "
                    "TOUJOURS centre de symétrie de la courbe.",
                    font_size=22,
                    weight="BOLD",
                ),
                MathTex(r"x_0 = -\dfrac{b}{3a}", font_size=30),
            ).arrange(DOWN, buff=0.3),
            box_width=10.6,
        )
        theo_inflexion.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Théorème important, spécifique aux polynômes du troisième "
                "degré : le point d'inflexion, d'abscisse x zéro égale "
                "moins b sur trois a, est toujours centre de symétrie de la "
                "courbe, quelle que soit la fonction cubique étudiée. C'est "
                "une propriété à retenir, elle simplifie beaucoup le tracé."
            )
        ) as tracker:
            self.play(FadeIn(theo_inflexion))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(theo_inflexion))

        # --- Exemple résolu complet : f(x) = x³ - 3x + 2 ------------------------
        enonce_ex = Text(
            "Exemple résolu — f(x) = x³ - 3x + 2",
            font_size=27,
            color=YELLOW,
            weight="BOLD",
        )
        enonce_ex.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Étudions complètement f de x égale x au cube moins trois x "
                "plus deux, en suivant les sept étapes."
            )
        ) as tracker:
            self.play(FadeIn(enonce_ex))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(enonce_ex))

        etape_domaine = example_box(
            MathTex(
                r"""
                D_f = \mathbb{R} \qquad
                f(-x) = -x^3+3x+2 \ \neq \ \pm f(x)
                \ \Longrightarrow \ f \text{ ni paire ni impaire}
                """,
                font_size=24,
            ),
            box_width=11.6,
        )
        etape_domaine.next_to(titre, DOWN, buff=0.55)

        with self.voiceover(
            text=(
                "Domaine : ℝ tout entier. Parité : f de moins x vaut moins "
                "x au cube plus trois x plus deux, qui n'est ni égal à f de "
                "x, ni à moins f de x, à cause du plus deux constant. f "
                "n'est donc ni paire ni impaire — on garde l'étude sur ℝ "
                "en entier."
            )
        ) as tracker:
            self.play(FadeIn(etape_domaine))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(etape_domaine))

        etape_limites = example_box(
            MathTex(
                r"\lim_{x\to-\infty} f(x) = -\infty \qquad \lim_{x\to+\infty} f(x) = +\infty",
                font_size=28,
            ),
            box_width=9.5,
        )
        etape_limites.next_to(titre, DOWN, buff=0.55)

        with self.voiceover(
            text=(
                "Limites aux bornes : en moins l'infini, f tend vers moins "
                "l'infini ; en plus l'infini, f tend vers plus l'infini, "
                "car le terme x au cube impose son comportement. Aucune "
                "asymptote pour un polynôme."
            )
        ) as tracker:
            self.play(FadeIn(etape_limites))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(etape_limites))

        etape_derivee = example_box(
            MathTex(
                r"""
                f'(x) = 3x^2-3 = 3(x-1)(x+1)
                \ \Longrightarrow \
                f'(x) \geq 0 \ \Longleftrightarrow \ x\leq-1 \text{ ou } x\geq1
                """,
                font_size=25,
            ),
            box_width=11.4,
        )
        etape_derivee.next_to(titre, DOWN, buff=0.55)

        with self.voiceover(
            text=(
                "Dérivée : f prime de x égale trois x carré moins trois, "
                "qui se factorise en trois fois x moins un, fois x plus "
                "un. Elle est positive ou nulle pour x inférieur ou égal à "
                "moins un, ou x supérieur ou égal à un."
            )
        ) as tracker:
            self.play(FadeIn(etape_derivee))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(etape_derivee))

        tableau_ex = MathTex(
            r"""
            \begin{array}{c|ccccccc}
            x & -\infty & & -1 & & 1 & & +\infty \\
            \hline
            f'(x) & & + & 0 & - & 0 & + & \\
            \hline
            f(x) & -\infty & \nearrow & 4 & \searrow & 0 & \nearrow & +\infty
            \end{array}
            """,
            font_size=24,
        )
        tableau_ex.next_to(titre, DOWN, buff=0.6)

        with self.voiceover(
            text=(
                "Tableau de variation : f croît de moins l'infini jusqu'à "
                "moins un, où elle vaut quatre, un maximum local. Elle "
                "décroît ensuite jusqu'à un, où elle vaut zéro, un minimum "
                "local. Puis elle recroît jusqu'à plus l'infini."
            )
        ) as tracker:
            self.play(FadeIn(tableau_ex))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(tableau_ex))

        etape_factorisation = example_box(
            MathTex(
                r"""
                f(1) = 0 \ \Longrightarrow \ (x-1) \text{ facteur} \qquad
                f(x) = (x-1)^2(x+2)
                """,
                font_size=27,
            ),
            box_width=10.5,
        )
        etape_factorisation.next_to(titre, DOWN, buff=0.55)

        with self.voiceover(
            text=(
                "Points remarquables : comme f de un vaut zéro d'après le "
                "tableau, x moins un est facteur de f de x. On factorise "
                "entièrement : f de x égale x moins un au carré, fois x "
                "plus deux — ce qui donne directement les intersections "
                "avec l'axe des abscisses en un et en moins deux."
            )
        ) as tracker:
            self.play(FadeIn(etape_factorisation))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(etape_factorisation))

        etape_symetrie = example_box(
            MathTex(
                r"x_0 = -\dfrac{b}{3a} = -\dfrac{0}{3} = 0 \ \Longrightarrow \ I(0\,;2) \text{ centre de symétrie}",
                font_size=27,
            ),
            box_width=10.5,
        )
        etape_symetrie.next_to(titre, DOWN, buff=0.55)

        with self.voiceover(
            text=(
                "Ici, b vaut zéro, donc x zéro égale moins b sur trois a "
                "égale zéro. D'après le théorème, le point I de "
                "coordonnées zéro et deux — puisque f de zéro vaut deux — "
                "est centre de symétrie de la courbe."
            )
        ) as tracker:
            self.play(FadeIn(etape_symetrie))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(etape_symetrie))

        # --- Tracé de la courbe ------------------------------------------------
        axes = Axes(
            x_range=[-3, 3, 1], y_range=[-2, 6, 2], x_length=6.5, y_length=4.5,
            axis_config={"color": WHITE, "font_size": 16},
        )
        axes.move_to(titre.get_center() + DOWN * 3.5)
        courbe = axes.plot(lambda x: x**3 - 3 * x + 2, x_range=[-2.3, 1.65], color="#DE7C1F")
        pt_min = Dot(axes.c2p(1, 0), color=WHITE)
        pt_max = Dot(axes.c2p(-1, 4), color=WHITE)
        pt_I = Dot(axes.c2p(0, 2), color=YELLOW)
        schema = VGroup(axes, courbe, pt_min, pt_max, pt_I)

        with self.voiceover(
            text=(
                "On peut maintenant tracer la courbe : elle monte jusqu'au "
                "maximum local en moins un, quatre, redescend jusqu'au "
                "minimum local en un, zéro qui est aussi un point double "
                "de la factorisation, puis remonte, le tout parfaitement "
                "symétrique par rapport au point I."
            )
        ) as tracker:
            self.play(FadeIn(schema))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(schema))

        # --- À retenir ---------------------------------------------------------
        retenir = essentiel_box(
            Text(
                _wrap(
                    "Polynôme du 3e degré : Df = ℝ, jamais d'asymptote. "
                    "Signe de f' donné par le trinôme dérivé (Δ'). Le point "
                    "d'inflexion x0 = -b/(3a) est TOUJOURS centre de "
                    "symétrie de la courbe.",
                    width=58,
                ),
                font_size=22,
            ),
            box_width=11.2,
        )
        retenir.next_to(titre, DOWN, buff=0.6)

        with self.voiceover(
            text=(
                "À retenir : un polynôme du troisième degré est défini sur "
                "ℝ, sans jamais avoir d'asymptote. Le signe de sa dérivée, "
                "un trinôme, se lit avec son discriminant. Et son point "
                "d'inflexion, d'abscisse moins b sur trois a, est toujours "
                "centre de symétrie de la courbe."
            )
        ) as tracker:
            self.play(FadeIn(retenir))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(retenir))

        # --- Piège à éviter ------------------------------------------------
        piege = warning_box(
            Text(
                _wrap(
                    "Piège : si Δ' ≤ 0, f' garde un signe constant (ou ne "
                    "s'annule qu'une fois) et f est strictement monotone "
                    "sur ℝ — pas d'extremum, pas de tableau en trois "
                    "parties. Vérifier Δ' avant de dresser le tableau.",
                    width=58,
                ),
                font_size=22,
            ),
            box_width=11.2,
        )
        piege.next_to(titre, DOWN, buff=0.6)

        with self.voiceover(
            text=(
                "Piège à éviter : si le discriminant réduit delta prime "
                "est négatif ou nul, la dérivée garde un signe constant, "
                "et f est strictement monotone sur ℝ tout entier — pas "
                "d'extremum, pas de tableau en trois parties. Il faut donc "
                "toujours vérifier le signe de delta prime avant de "
                "supposer que le tableau ressemblera à l'exemple traité ici."
            )
        ) as tracker:
            self.play(FadeIn(piege))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(titre), FadeOut(piege))
