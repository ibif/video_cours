"""
scenes/Maths_ExtensionNotionLimite_10.py — Chapitre 7 (1ereC, Maths), scène 10.

Exemple résolu complet d'étude de fonction : f(x) = (x²+x+1)/(x+1) — Df,
asymptote oblique par division euclidienne, asymptote verticale, position
relative, dérivée et tableau de variation, centre de symétrie, tracé. Puis
4 méthodes de synthèse et 2 pièges récapitulatifs, terminé par l'essentiel
à retenir du chapitre.
Source : 1ereC/Maths.pdf, chapitre 7, pages 80-90.
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
    DashedLine,
    Dot,
    FadeIn,
    FadeOut,
    MathTex,
    Text,
    VGroup,
    Write,
)

from shapes.base_scene import NotionScene
from shapes.boxes import essentiel_box, example_box, method_box, scene_title, warning_box


def _wrap(text: str, width: int = 58) -> str:
    return "\n".join(textwrap.fill(line, width=width) for line in text.split("\n"))


class EtudeFonctionComplete(NotionScene):
    def construct(self):
        titre = scene_title("Étude complète d'une fonction — synthèse")
        titre.scale(0.48)
        titre.to_edge(UP)

        # --- Énoncé -----------------------------------------------------------
        enonce_ex11 = Text(
            "Exemple 11 — étude complète de f(x) = (x²+x+1)/(x+1)",
            font_size=25,
            color=YELLOW,
            weight="BOLD",
        )
        enonce_ex11.next_to(titre, DOWN, buff=0.5)

        fonction_ex11 = MathTex(r"f(x) = \dfrac{x^2+x+1}{x+1}", font_size=32)
        fonction_ex11.next_to(enonce_ex11, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Pour clore ce chapitre, menons l'étude complète, étape par "
                "étape, de la fonction f de x égale x carré plus x plus un, "
                "sur x plus un, en réutilisant tous les outils rencontrés."
            )
        ) as tracker:
            self.play(Write(titre))
            self.play(FadeIn(enonce_ex11))
            self.play(Write(fonction_ex11))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(enonce_ex11), FadeOut(fonction_ex11))

        # --- Étape 1 : Df -------------------------------------------------
        etape1 = example_box(
            MathTex(r"D_f = \mathbb{R}\setminus\{-1\}", font_size=30),
            box_width=6.5,
        )
        etape1.next_to(titre, DOWN, buff=0.55)

        with self.voiceover(
            text=(
                "Étape un : le dénominateur x plus un s'annule en moins un, "
                "donc D indice f est ℝ privé de moins un."
            )
        ) as tracker:
            self.play(FadeIn(etape1))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(etape1))

        # --- Étape 2 : asymptotes -------------------------------------------
        etape2a = example_box(
            MathTex(
                r"""
                x^2+x+1 = (x+1)\cdot x + 1
                \quad \Longrightarrow \quad
                f(x) = x + \dfrac{1}{x+1}
                """,
                font_size=27,
            ),
            box_width=10.5,
        )
        etape2a.next_to(titre, DOWN, buff=0.55)

        with self.voiceover(
            text=(
                "Étape deux : la division euclidienne de x carré plus x "
                "plus un par x plus un donne un quotient x et un reste un. "
                "On écrit donc f de x égale x plus un sur x plus un."
            )
        ) as tracker:
            self.play(FadeIn(etape2a))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(etape2a))

        etape2b = example_box(
            MathTex(
                r"""
                \lim_{x\to\pm\infty} \dfrac{1}{x+1} = 0
                \ \Longrightarrow\ y=x \text{ asymptote oblique}
                \qquad\quad
                \lim_{x\to-1^{-}} f(x) = -\infty, \ \lim_{x\to-1^{+}} f(x) = +\infty
                """,
                font_size=20,
            ),
            box_width=11.7,
        )
        etape2b.next_to(titre, DOWN, buff=0.55)

        with self.voiceover(
            text=(
                "Comme un sur x plus un tend vers zéro en plus ou moins "
                "l'infini, la droite y égale x est asymptote oblique. Et "
                "comme le numérateur en moins un vaut un, non nul, la "
                "limite est infinie de part et d'autre : x égale moins un "
                "est asymptote verticale, avec moins l'infini à gauche et "
                "plus l'infini à droite."
            )
        ) as tracker:
            self.play(FadeIn(etape2b))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(etape2b))

        # --- Étape 3 : position relative -------------------------------------
        etape3 = example_box(
            MathTex(
                r"""
                d(x) = f(x)-x = \dfrac{1}{x+1}
                \ \Longrightarrow\
                \begin{cases}
                d(x)>0 \text{ si } x>-1 & (\mathcal{C}_f \text{ au-dessus de } \Delta) \\
                d(x)<0 \text{ si } x<-1 & (\mathcal{C}_f \text{ en dessous de } \Delta)
                \end{cases}
                """,
                font_size=22,
            ),
            box_width=11.0,
        )
        etape3.next_to(titre, DOWN, buff=0.55)

        with self.voiceover(
            text=(
                "Étape trois, la position relative : d de x égale f de x "
                "moins x vaut un sur x plus un. Cette quantité est positive "
                "quand x est supérieur à moins un, la courbe est alors "
                "au-dessus de l'asymptote ; elle est négative quand x est "
                "inférieur à moins un, la courbe est alors en dessous."
            )
        ) as tracker:
            self.play(FadeIn(etape3))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(etape3))

        # --- Étape 4 : dérivée et tableau de variation -------------------------
        etape4a = example_box(
            MathTex(
                r"""
                f'(x) = 1-\dfrac{1}{(x+1)^2} = \dfrac{(x+1)^2-1}{(x+1)^2}
                = \dfrac{x^2+2x}{(x+1)^2} = \dfrac{x(x+2)}{(x+1)^2}
                """,
                font_size=25,
            ),
            box_width=11.0,
        )
        etape4a.next_to(titre, DOWN, buff=0.55)

        with self.voiceover(
            text=(
                "Étape quatre : en dérivant x plus un sur x plus un, on "
                "obtient f prime de x égale un moins un sur x plus un au "
                "carré, qui se réécrit, après réduction au même "
                "dénominateur, x fois x plus deux, sur x plus un au carré."
            )
        ) as tracker:
            self.play(FadeIn(etape4a))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(etape4a))

        tableau_variation = example_box(
            MathTex(
                r"""
                \begin{array}{c|ccccccccc}
                x & -\infty & & -2 & & -1 & & 0 & & +\infty \\
                \hline
                f'(x) & & + & 0 & - & \|\| & - & 0 & + & \\
                \hline
                & & & -3 & & +\infty & & & & +\infty \\
                f(x) & -\infty & \nearrow & & \searrow & \|\| & \searrow & & \nearrow & \\
                & & & & & -\infty & & 1 & &
                \end{array}
                """,
                font_size=18,
            ),
            box_width=11.7,
        )
        tableau_variation.next_to(titre, DOWN, buff=0.55)

        with self.voiceover(
            text=(
                "Le numérateur x fois x plus deux s'annule en moins deux et "
                "en zéro, ce qui donne le tableau de variation suivant : f "
                "croît de moins l'infini jusqu'à un maximum local, moins "
                "trois, en x égale moins deux ; puis décroît jusqu'à moins "
                "l'infini en approchant moins un par la gauche. À droite de "
                "moins un, f repart de plus l'infini et décroît jusqu'à un "
                "minimum local, un, en x égale zéro ; puis croît à nouveau "
                "vers plus l'infini."
            )
        ) as tracker:
            self.play(FadeIn(tableau_variation))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(tableau_variation))

        # --- Étape 5 : centre de symétrie -------------------------------------
        etape5 = example_box(
            MathTex(
                r"""
                f(-2-x) = -2-f(x)
                \quad \text{(vérifié par exemple en } x=0\text{ : } f(-2)=-3=-2-f(0))
                \ \Longrightarrow\ \Omega(-1\,;-1) \text{ centre de symétrie}
                """,
                font_size=19,
            ),
            box_width=11.7,
        )
        etape5.next_to(titre, DOWN, buff=0.55)

        with self.voiceover(
            text=(
                "Étape cinq : on vérifie que f de moins deux moins x égale "
                "moins deux moins f de x — par exemple en zéro, f de moins "
                "deux vaut moins trois, et moins deux moins f de zéro vaut "
                "aussi moins trois. Cette relation traduit une symétrie par "
                "rapport au point Oméga de coordonnées moins un, moins un, "
                "qui est donc centre de symétrie de la courbe."
            )
        ) as tracker:
            self.play(FadeIn(etape5))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(etape5))

        # --- Étape 6/7 : tracé -------------------------------------------------
        axes = Axes(
            x_range=[-7, 5, 1],
            y_range=[-8, 8, 2],
            x_length=7.2,
            y_length=4.4,
            axis_config={"color": WHITE, "font_size": 14},
        )
        axes.next_to(titre, DOWN, buff=0.55)
        asymp_oblique = DashedLine(axes.c2p(-7, -7), axes.c2p(5, 5), color=YELLOW, stroke_width=2)
        asymp_v = DashedLine(axes.c2p(-1, -8), axes.c2p(-1, 8), color="#FF6666", stroke_width=2)
        branche_g = axes.plot(lambda x: x + 1 / (x + 1), x_range=[-7, -1.15], color="#1E90FF")
        branche_d = axes.plot(lambda x: x + 1 / (x + 1), x_range=[-0.82, 5], color="#1E90FF")
        point_max = Dot(axes.c2p(-2, -3), color=WHITE, radius=0.06)
        point_min = Dot(axes.c2p(0, 1), color=WHITE, radius=0.06)
        omega = Dot(axes.c2p(-1, -1), color="#FFA500", radius=0.06)
        label_omega = MathTex(r"\Omega", font_size=22, color="#FFA500").next_to(omega, LEFT, buff=0.1)
        figure = VGroup(
            axes, asymp_oblique, asymp_v, branche_g, branche_d,
            point_max, point_min, omega, label_omega,
        )
        figure.scale(0.9)

        with self.voiceover(
            text=(
                "En rassemblant toutes ces informations — asymptotes, "
                "variations, extremums locaux et centre de symétrie — on "
                "obtient le tracé complet de la courbe, avec sa branche "
                "gauche au-dessus de l'asymptote verticale, sa branche "
                "droite en dessous, et une symétrie parfaite autour du "
                "point Oméga."
            )
        ) as tracker:
            self.play(FadeIn(figure))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(figure))

        # --- À retenir : 4 méthodes de synthèse --------------------------------
        methode1 = method_box(
            Text(
                _wrap(
                    "1. Limite en x₀ de P(x)/Q(x) avec Q(x₀)=0 : regarder "
                    "P(x₀) — non nul → limite infinie (signe par tableau) ; "
                    "nul → factoriser par (x-x₀) et simplifier.",
                    width=54,
                ),
                font_size=21,
            ),
            box_width=10.8,
        )
        methode1.next_to(titre, DOWN, buff=0.55)

        with self.voiceover(
            text=(
                "Récapitulons avec quatre méthodes de synthèse. Première "
                "méthode : pour une limite en x zéro d'une fraction P sur "
                "Q, avec Q de x zéro nul, on regarde P de x zéro — s'il est "
                "non nul, la limite est infinie, avec un signe à "
                "déterminer par un tableau ; s'il est nul, on factorise par "
                "x moins x zéro et on simplifie."
            )
        ) as tracker:
            self.play(FadeIn(methode1))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(methode1))

        methode2 = method_box(
            Text(
                _wrap(
                    "2. Lever une indétermination avec radicaux : quantité "
                    "conjuguée pour ∞-∞, mise en facteur de x² sous le "
                    "radical, en surveillant le signe de x.",
                    width=54,
                ),
                font_size=21,
            ),
            box_width=10.8,
        )
        methode2.next_to(titre, DOWN, buff=0.55)

        with self.voiceover(
            text=(
                "Deuxième méthode : pour lever une indétermination avec des "
                "radicaux, on utilise la quantité conjuguée pour l'infini "
                "moins l'infini, et la mise en facteur de x carré sous le "
                "radical, en surveillant toujours le signe de x."
            )
        ) as tracker:
            self.play(FadeIn(methode2))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(methode2))

        methode3 = method_box(
            Text(
                _wrap(
                    "3. Prouver une asymptote oblique y = ax+b : division "
                    "euclidienne si fraction rationnelle, sinon calculer "
                    "a = lim f(x)/x puis b = lim [f(x)-ax], et vérifier "
                    "lim [f(x)-(ax+b)] = 0.",
                    width=54,
                ),
                font_size=20,
            ),
            box_width=10.8,
        )
        methode3.next_to(titre, DOWN, buff=0.55)

        with self.voiceover(
            text=(
                "Troisième méthode : pour prouver une asymptote oblique y "
                "égale a x plus b, on effectue une division euclidienne si "
                "c'est une fraction rationnelle, sinon on calcule a comme "
                "limite de f de x sur x, puis b comme limite de f de x "
                "moins a x, et on vérifie que la limite de f de x moins a x "
                "plus b vaut bien zéro."
            )
        ) as tracker:
            self.play(FadeIn(methode3))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(methode3))

        methode4 = method_box(
            Text(
                _wrap(
                    "4. Exploiter les symétries : une fonction paire ou "
                    "impaire, ou un centre/axe de symétrie détecté, permet "
                    "de n'étudier f que sur une moitié du domaine.",
                    width=54,
                ),
                font_size=21,
            ),
            box_width=10.8,
        )
        methode4.next_to(titre, DOWN, buff=0.55)

        with self.voiceover(
            text=(
                "Quatrième méthode : exploiter les symétries. Une fonction "
                "paire, impaire, ou possédant un centre ou un axe de "
                "symétrie, permet de restreindre l'étude à une moitié "
                "seulement du domaine, puis de compléter la courbe par "
                "symétrie."
            )
        ) as tracker:
            self.play(FadeIn(methode4))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(methode4))

        # --- Pièges à éviter -------------------------------------------------
        piege1 = warning_box(
            Text(
                _wrap(
                    "Piège 1 : ne jamais écrire √x² = x sans préciser le "
                    "signe de x. En toute rigueur, √x² = |x|, qui vaut x si "
                    "x ≥ 0, et -x si x < 0.",
                    width=56,
                ),
                font_size=22,
            ),
            box_width=11.0,
        )
        piege1.next_to(titre, DOWN, buff=0.55)

        with self.voiceover(
            text=(
                "Premier piège récapitulatif : ne jamais écrire racine de x "
                "carré égale x sans préciser le signe de x. En toute "
                "rigueur, racine de x carré vaut toujours valeur absolue de "
                "x, qui vaut x si x est positif ou nul, et moins x sinon."
            )
        ) as tracker:
            self.play(FadeIn(piege1))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(piege1))

        piege2 = warning_box(
            Text(
                _wrap(
                    "Piège 2 : une limite finie de f(x)/x seule ne suffit "
                    "pas à prouver une asymptote oblique — il faut aussi "
                    "que f(x) - ax ait une limite finie.",
                    width=56,
                ),
                font_size=22,
            ),
            box_width=11.0,
        )
        piege2.next_to(titre, DOWN, buff=0.55)

        with self.voiceover(
            text=(
                "Second piège récapitulatif : une limite finie de f de x "
                "sur x ne suffit jamais, à elle seule, à prouver une "
                "asymptote oblique. Il faut impérativement vérifier, en "
                "plus, que f de x moins a x admet elle aussi une limite "
                "finie — sinon, on n'a qu'une simple direction "
                "asymptotique."
            )
        ) as tracker:
            self.play(FadeIn(piege2))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(piege2))

        # --- L'essentiel à retenir du chapitre --------------------------------
        essentiel = essentiel_box(
            Text(
                _wrap(
                    "Limites à gauche/à droite ; limite = limites latérales "
                    "égales ; en ±∞ une fraction rationnelle suit le terme "
                    "de plus haut degré ; en x₀ où Q s'annule, factoriser "
                    "si P(x₀)=0 ; avec radicaux, conjuguée et |x| ; "
                    "asymptotes verticale/horizontale/oblique via les "
                    "limites ; direction asymptotique via lim f(x)/x ; "
                    "position relative via le signe de f(x)-(ax+b).",
                    width=58,
                ),
                font_size=21,
            )
        )
        essentiel.next_to(titre, DOWN, buff=0.6)

        with self.voiceover(
            text=(
                "L'essentiel à retenir de ce chapitre : les limites à "
                "gauche et à droite, et leur lien avec la limite globale ; "
                "en plus ou moins l'infini, une fonction rationnelle suit "
                "son terme de plus haut degré ; en un point où le "
                "dénominateur s'annule, on factorise si le numérateur "
                "s'annule aussi ; avec des radicaux, on combine quantité "
                "conjuguée et valeur absolue de x ; les asymptotes "
                "verticale, horizontale et oblique se lisent toutes dans "
                "des limites bien choisies ; la nature d'une branche "
                "infinie se lit dans la limite de f de x sur x ; et la "
                "position relative de la courbe se lit dans le signe de f "
                "de x moins a x plus b."
            )
        ) as tracker:
            self.play(FadeIn(essentiel))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(titre), FadeOut(essentiel))
