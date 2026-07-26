"""
scenes/Maths_EtudeGraphiqueFonctions_03.py — Chapitre 11 (1ereC, Maths), scène 03.

Limites aux bornes et les trois types d'asymptotes (verticale, horizontale,
oblique) : rappel des formes indéterminées et méthodes de levée, théorème de
position relative courbe/asymptote oblique, méthode de la division
euclidienne pour trouver a et b.
Source : 1ereC/Maths.pdf, chapitre 11, pages 130-141.
"""

import textwrap

from manim import DOWN, LEFT, RIGHT, UP, WHITE, YELLOW, Axes, DashedLine, FadeIn, FadeOut, MathTex, Text, VGroup, Write

from shapes.base_scene import NotionScene
from shapes.boxes import definition_box, essentiel_box, example_box, method_box, scene_title, theorem_box, warning_box


def _wrap(text: str, width: int = 58) -> str:
    return "\n".join(textwrap.fill(line, width=width) for line in text.split("\n"))


class LimitesAsymptotes(NotionScene):
    def construct(self):
        titre = scene_title("Limites aux bornes et asymptotes")
        titre.scale(0.5)
        titre.to_edge(UP)

        # --- Énoncé ------------------------------------------------------------
        enonce = Text(
            "Étapes 3 et 4 : limites aux bornes, puis asymptotes",
            font_size=25,
            color=YELLOW,
            weight="BOLD",
        )
        enonce.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Une fois le domaine réduit, on calcule les limites de f à "
                "chacune de ses bornes. Ces limites révèlent ensuite "
                "l'existence d'asymptotes, qui guident directement le tracé "
                "de la courbe."
            )
        ) as tracker:
            self.play(Write(titre))
            self.play(FadeIn(enonce))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(enonce))

        # --- Rappel FI et méthodes ------------------------------------------
        rappel_fi = method_box(
            Text(
                _wrap(
                    "4 formes indéterminées à lever : ∞-∞, ∞/∞, 0/0, 0×∞. "
                    "Méthodes principales : factoriser par le terme de plus "
                    "haut degré (rationnelles), ou multiplier par la "
                    "quantité conjuguée (radicaux).",
                    width=58,
                ),
                font_size=22,
            ),
            box_width=11.2,
        )
        rappel_fi.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Rappel des quatre formes indéterminées classiques : infini "
                "moins infini, infini sur infini, zéro sur zéro, et zéro "
                "fois infini. Pour les lever, deux méthodes principales : "
                "factoriser par le terme de plus haut degré pour les "
                "fonctions rationnelles, ou multiplier par la quantité "
                "conjuguée en présence d'une racine carrée."
            )
        ) as tracker:
            self.play(FadeIn(rappel_fi))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(rappel_fi))

        # --- Définitions des 3 types d'asymptotes --------------------------
        def_asymptotes = definition_box(
            MathTex(
                r"""
                \begin{array}{ll}
                \text{Verticale } x=a & \lim\limits_{x\to a} f(x) = \pm\infty \\
                \text{Horizontale } y=\ell & \lim\limits_{x\to\infty} f(x) = \ell \\
                \text{Oblique } y=ax+b & \lim\limits_{x\to\infty} \big[f(x)-(ax+b)\big] = 0
                \end{array}
                """,
                font_size=27,
            ),
            box_width=10.8,
        )
        def_asymptotes.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Trois types d'asymptotes. Asymptote verticale d'équation x "
                "égale a, quand la limite de f en a est infinie. Asymptote "
                "horizontale d'équation y égale l, quand la limite de f à "
                "l'infini vaut ce réel l. Et asymptote oblique d'équation y "
                "égale a x plus b, quand la différence entre f de x et a x "
                "plus b tend vers zéro à l'infini."
            )
        ) as tracker:
            self.play(FadeIn(def_asymptotes))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(def_asymptotes))

        # --- Théorème position relative ------------------------------------
        theo_position = theorem_box(
            Text(
                _wrap(
                    "Position de Cf par rapport à l'asymptote oblique : "
                    "étudier le signe de f(x) - (ax+b) sur tout le domaine. "
                    "Positif → Cf au-dessus. Négatif → Cf en dessous. "
                    "Nul en x0 → Cf coupe l'asymptote en x0.",
                    width=58,
                ),
                font_size=22,
            ),
            box_width=11.2,
        )
        theo_position.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Théorème de position relative : pour savoir si la courbe "
                "est au-dessus ou en dessous de son asymptote oblique, on "
                "étudie le signe de f de x moins a x plus b sur tout le "
                "domaine. Là où ce signe est positif, la courbe est "
                "au-dessus de l'asymptote. Là où il est négatif, elle est "
                "en dessous. Et là où il s'annule, la courbe traverse "
                "l'asymptote."
            )
        ) as tracker:
            self.play(FadeIn(theo_position))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(theo_position))

        # --- Méthode : division euclidienne ---------------------------------
        methode_division = method_box(
            VGroup(
                Text(
                    "Pour trouver a et b d'une asymptote oblique : division "
                    "euclidienne du numérateur par le dénominateur",
                    font_size=21,
                    weight="BOLD",
                ),
                MathTex(
                    r"f(x) = \dfrac{N(x)}{D(x)} = (ax+b) + \dfrac{R(x)}{D(x)}"
                    r"\ \ \text{avec} \ \ \dfrac{R(x)}{D(x)} \xrightarrow[x\to\infty]{} 0",
                    font_size=26,
                ),
            ).arrange(DOWN, buff=0.3),
            box_width=11.4,
        )
        methode_division.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Méthode pratique pour trouver a et b : on effectue la "
                "division euclidienne du numérateur N de x par le "
                "dénominateur D de x. On obtient f de x égale a x plus b, "
                "plus un reste sur D de x, ce reste sur D de x tendant vers "
                "zéro à l'infini. La droite y égale a x plus b est alors "
                "l'asymptote oblique cherchée."
            )
        ) as tracker:
            self.play(FadeIn(methode_division))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(methode_division))

        # --- Exemple traité : illustration graphique ---------------------------
        enonce_ex = Text(
            "Exemple — les trois asymptotes sur une même figure",
            font_size=25,
            color=YELLOW,
            weight="BOLD",
        )
        enonce_ex.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Regardons une figure regroupant les trois types "
                "d'asymptotes sur une fonction rationnelle f de x égale x "
                "carré plus un, sur x, définie sur ℝ privé de zéro."
            )
        ) as tracker:
            self.play(FadeIn(enonce_ex))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(enonce_ex))

        axes = Axes(
            x_range=[-4, 4, 1], y_range=[-6, 6, 2], x_length=7.5, y_length=5.0,
            axis_config={"color": WHITE, "font_size": 16},
        )
        axes.move_to(titre.get_center() + DOWN * 3.4)

        def f(x):
            return x + 1 / x

        courbe_droite = axes.plot(f, x_range=[0.25, 3.8], color="#1E90FF")
        courbe_gauche = axes.plot(f, x_range=[-3.8, -0.25], color="#1E90FF")
        asym_verticale = DashedLine(axes.c2p(0, -6), axes.c2p(0, 6), color=YELLOW)
        asym_oblique = axes.plot(lambda x: x, x_range=[-4, 4], color="#B42E41")
        formule = MathTex(r"f(x) = x + \dfrac{1}{x}", font_size=28)
        formule.next_to(axes, UP, buff=0.15)

        schema = VGroup(axes, courbe_droite, courbe_gauche, asym_verticale, asym_oblique)

        with self.voiceover(
            text=(
                "Ici, la droite verticale x égale zéro, en jaune, est une "
                "asymptote verticale car un sur x explose en zéro. La "
                "droite rouge y égale x est une asymptote oblique, car un "
                "sur x tend vers zéro à l'infini : la courbe s'en "
                "rapproche de plus en plus, sans jamais la toucher. Cette "
                "fonction n'a en revanche aucune asymptote horizontale."
            )
        ) as tracker:
            self.play(FadeIn(formule))
            self.play(FadeIn(schema))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(schema), FadeOut(formule))

        # --- À retenir ---------------------------------------------------------
        retenir = essentiel_box(
            Text(
                _wrap(
                    "Verticale : limite infinie en une valeur finie. "
                    "Horizontale : limite finie à l'infini. Oblique : "
                    "f(x)-(ax+b) → 0 à l'infini, a et b s'obtiennent par "
                    "division euclidienne. Une fonction peut n'avoir aucune "
                    "asymptote horizontale.",
                    width=58,
                ),
                font_size=22,
            ),
            box_width=11.4,
        )
        retenir.next_to(titre, DOWN, buff=0.6)

        with self.voiceover(
            text=(
                "À retenir : asymptote verticale, limite infinie en une "
                "valeur finie. Asymptote horizontale, limite finie à "
                "l'infini. Asymptote oblique, la différence f de x moins a "
                "x plus b tend vers zéro à l'infini, a et b s'obtenant par "
                "division euclidienne. Et une fonction peut très bien "
                "n'avoir aucune asymptote horizontale, comme on vient de le "
                "voir."
            )
        ) as tracker:
            self.play(FadeIn(retenir))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(retenir))

        # --- Piège à éviter ------------------------------------------------
        piege = warning_box(
            Text(
                _wrap(
                    "Piège : horizontale et oblique sont exclusives en un "
                    "même infini (une fonction ne peut pas avoir les deux "
                    "en +∞). Toujours vérifier le signe du reste sur TOUT "
                    "le domaine, pas seulement au voisinage de l'infini.",
                    width=58,
                ),
                font_size=22,
            ),
            box_width=11.2,
        )
        piege.next_to(titre, DOWN, buff=0.6)

        with self.voiceover(
            text=(
                "Attention : en un même infini, une fonction ne peut pas "
                "avoir à la fois une asymptote horizontale et une "
                "asymptote oblique, ces deux comportements sont exclusifs "
                "l'un de l'autre. Et pour la position relative, il faut "
                "vérifier le signe du reste sur tout le domaine, pas "
                "seulement au voisinage de l'infini."
            )
        ) as tracker:
            self.play(FadeIn(piege))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(titre), FadeOut(piege))
