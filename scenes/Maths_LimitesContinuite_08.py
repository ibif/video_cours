"""
scenes/Maths_LimitesContinuite_08.py — Chapitre 5 « Limites et continuité »
(1ereC, Maths), scène 08.

Théorèmes de comparaison et des gendarmes (admis). Exemples résolus 9, 10
et 11, méthode « majorer avec sin/cos bornés ».
Source : 1ereC/Maths.pdf, chapitre 5, pages 52-65.
"""

from manim import DOWN, UP, FadeIn, FadeOut, MathTex, Text, VGroup, Write, YELLOW

from shapes.base_scene import NotionScene
from shapes.boxes import essentiel_box, example_box, method_box, scene_title, theorem_box


class TheoremesComparaisonEtGendarmes(NotionScene):
    def construct(self):
        titre = scene_title("Théorèmes de comparaison et des gendarmes")
        titre.scale(0.55)
        titre.to_edge(UP)
        self.play(Write(titre))

        # --- Énoncé : théorème de comparaison (admis) ---------------------------
        theo_comp = theorem_box(
            MathTex(
                r"""
                \begin{array}{l}
                \text{Si } f(x)\geq g(x) \text{ au voisinage de } +\infty \text{ et } \lim_{x\to+\infty} g(x)=+\infty,\\
                \text{alors } \lim_{x\to+\infty} f(x) = +\infty.\\[4pt]
                \text{(énoncé analogue avec } -\infty \text{ et } f(x)\leq g(x)\text{)}
                \end{array}
                """,
                font_size=25,
            ),
            box_width=11.0,
        )
        theo_comp.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Théorème de comparaison, admis : si f de x est toujours "
                "supérieure ou égale à g de x au voisinage de plus "
                "l'infini, et que g de x tend vers plus l'infini, alors f "
                "de x tend elle aussi vers plus l'infini. Il existe un "
                "énoncé analogue avec moins l'infini."
            )
        ) as tracker:
            self.play(FadeIn(theo_comp))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(theo_comp))

        # --- Exemple 9 : x + sin x en +∞ -----------------------------------------
        ex9_titre = Text("Exemple 9 — lim (x + sin x) en +∞ :", font_size=23, color=YELLOW, weight="BOLD")
        ex9_titre.next_to(titre, DOWN, buff=0.35)
        ex9_calc = MathTex(
            r"""
            x+\sin x \geq x-1 \quad\text{(car } \sin x\geq -1\text{)}, \qquad
            \lim_{x\to+\infty}(x-1)=+\infty
            """,
            font_size=24,
        )
        ex9_calc.next_to(ex9_titre, DOWN, buff=0.35)
        ex9_concl = MathTex(r"\Longrightarrow\ \lim_{x\to+\infty} (x+\sin x) = +\infty", font_size=27)
        ex9_concl.next_to(ex9_calc, DOWN, buff=0.3)

        with self.voiceover(
            text=(
                "Exemple : la limite de x plus sinus de x, en plus "
                "l'infini. Comme sinus de x est toujours supérieur ou égal "
                "à moins un, x plus sinus de x est toujours supérieur ou "
                "égal à x moins un, qui tend vers plus l'infini. Par "
                "comparaison, x plus sinus de x tend donc aussi vers plus "
                "l'infini."
            )
        ) as tracker:
            self.play(FadeIn(ex9_titre))
            self.play(Write(ex9_calc))
            self.play(FadeIn(ex9_concl))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(ex9_titre), FadeOut(ex9_calc), FadeOut(ex9_concl))

        # --- Théorème des gendarmes (admis) --------------------------------------
        theo_gendarmes = theorem_box(
            MathTex(
                r"""
                \begin{array}{l}
                \text{Si } g(x)\leq f(x)\leq h(x) \text{ au voisinage de } +\infty\\
                \text{et } \lim_{x\to+\infty} g(x) = \lim_{x\to+\infty} h(x) = \ell,\\
                \text{alors } \lim_{x\to+\infty} f(x) = \ell.
                \end{array}
                """,
                font_size=25,
            ),
            box_width=9.5,
        )
        theo_gendarmes.next_to(titre, DOWN, buff=0.35)

        with self.voiceover(
            text=(
                "Théorème des gendarmes, admis lui aussi : si f de x est "
                "encadrée entre g de x et h de x au voisinage de plus "
                "l'infini, et que g et h ont la même limite finie ℓ, alors "
                "f est « prise en étau » et tend elle aussi vers ℓ."
            )
        ) as tracker:
            self.play(FadeIn(theo_gendarmes))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(theo_gendarmes))

        methode_bornes = method_box(
            Text(
                "Méthode : pour encadrer, utiliser -1 ≤ sin(...) ≤ 1 et -1 ≤ cos(...) ≤ 1.",
                font_size=24,
            ),
            box_width=10.5,
        )
        methode_bornes.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Méthode pratique : pour construire un tel encadrement, on "
                "utilise presque toujours le fait que sinus et cosinus sont "
                "toujours compris entre moins un et un, quelle que soit "
                "leur variable."
            )
        ) as tracker:
            self.play(FadeIn(methode_bornes))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(methode_bornes))

        # --- Exemple 10 : (2+sin x)/x en +∞ ---------------------------------------
        ex10_titre = Text("Exemple 10 — lim (2 + sin x)/x en +∞ :", font_size=22, color=YELLOW, weight="BOLD")
        ex10_titre.next_to(titre, DOWN, buff=0.35)
        ex10_calc = MathTex(
            r"""
            \begin{array}{l}
            -1\leq \sin x \leq 1 \ \Longrightarrow\ \dfrac{1}{x} \leq \dfrac{2+\sin x}{x} \leq \dfrac{3}{x} \quad (x>0)\\
            \lim_{x\to+\infty}\dfrac{1}{x} = \lim_{x\to+\infty}\dfrac{3}{x} = 0
            \ \Longrightarrow\ \lim_{x\to+\infty} \dfrac{2+\sin x}{x} = 0
            \end{array}
            """,
            font_size=23,
        )
        ex10_calc.next_to(ex10_titre, DOWN, buff=0.35)
        ex10_box = example_box(ex10_calc, box_width=11.0)
        ex10_box.next_to(ex10_titre, DOWN, buff=0.3)

        with self.voiceover(
            text=(
                "Exemple : deux plus sinus de x, sur x, en plus l'infini. "
                "En encadrant sinus de x entre moins un et un, on obtient "
                "un sur x, inférieur ou égal à l'expression, elle-même "
                "inférieure ou égale à trois sur x. Les deux bornes tendent "
                "vers zéro, donc par le théorème des gendarmes, la limite "
                "cherchée vaut zéro."
            )
        ) as tracker:
            self.play(FadeIn(ex10_titre))
            self.play(FadeIn(ex10_box))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(ex10_titre), FadeOut(ex10_box))

        # --- Exemple 11 : x sin(1/x) en 0 -----------------------------------------
        ex11_titre = Text("Exemple 11 — lim x·sin(1/x) en x0 = 0 :", font_size=22, color=YELLOW, weight="BOLD")
        ex11_titre.next_to(titre, DOWN, buff=0.35)
        ex11_calc = MathTex(
            r"""
            \begin{array}{l}
            -1\leq \sin\!\left(\dfrac{1}{x}\right) \leq 1
            \ \Longrightarrow\ -|x|\leq x\sin\!\left(\dfrac{1}{x}\right)\leq |x| \quad (x\neq 0)\\
            \lim_{x\to 0} (-|x|) = \lim_{x\to 0} |x| = 0
            \ \Longrightarrow\ \lim_{x\to 0} x\sin\!\left(\dfrac{1}{x}\right) = 0
            \end{array}
            """,
            font_size=22,
        )
        ex11_calc.next_to(ex11_titre, DOWN, buff=0.35)
        ex11_box = example_box(ex11_calc, box_width=11.0)
        ex11_box.next_to(ex11_titre, DOWN, buff=0.3)

        with self.voiceover(
            text=(
                "Dernier exemple, classique : x fois sinus de un sur x, en "
                "zéro. Bien que sinus de un sur x n'ait pas de limite en "
                "zéro, il reste encadré entre moins un et un ; en "
                "multipliant par x, on obtient moins valeur absolue de x, "
                "inférieur ou égal à l'expression, elle-même inférieure ou "
                "égale à valeur absolue de x. Les deux bornes tendent vers "
                "zéro, donc la limite cherchée vaut zéro, par le théorème "
                "des gendarmes."
            )
        ) as tracker:
            self.play(FadeIn(ex11_titre))
            self.play(FadeIn(ex11_box))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(ex11_titre), FadeOut(ex11_box))

        # --- À retenir -----------------------------------------------------------
        retenir = essentiel_box(
            Text(
                "Une fonction bornée (comme sin ou cos) multipliée par une fonction "
                "qui tend vers 0 tend elle-même vers 0 : c'est l'idée clé des gendarmes.",
                font_size=22,
            ),
            box_width=11.5,
        )
        retenir.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "À retenir : une fonction bornée, comme sinus ou cosinus, "
                "multipliée par une fonction qui tend vers zéro, donne "
                "toujours une limite nulle. C'est l'idée essentielle "
                "derrière le théorème des gendarmes."
            )
        ) as tracker:
            self.play(FadeIn(retenir))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(retenir), FadeOut(titre))
