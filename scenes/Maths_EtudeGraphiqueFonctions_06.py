"""
scenes/Maths_EtudeGraphiqueFonctions_06.py — Chapitre 11 (1ereC, Maths), scène 06.

Étude complète d'une fonction homographique : forme générale, asymptotes
verticale et horizontale, dérivée, théorème de monotonie « sur chaque
intervalle séparément », centre de symétrie = intersection des asymptotes,
exemple résolu complet f(x) = (2x-1)/(x+1).
Source : 1ereC/Maths.pdf, chapitre 11, pages 130-141.
"""

import textwrap

from manim import DOWN, LEFT, RIGHT, UP, WHITE, YELLOW, Axes, DashedLine, Dot, FadeIn, FadeOut, MathTex, Text, VGroup, Write

from shapes.base_scene import NotionScene
from shapes.boxes import essentiel_box, example_box, scene_title, theorem_box, warning_box


def _wrap(text: str, width: int = 58) -> str:
    return "\n".join(textwrap.fill(line, width=width) for line in text.split("\n"))


class EtudeFonctionHomographique(NotionScene):
    def construct(self):
        titre = scene_title("Étude d'une fonction homographique")
        titre.scale(0.5)
        titre.to_edge(UP)

        # --- Énoncé ------------------------------------------------------------
        enonce = Text(
            "Appliquons le plan complet à f(x) = (ax+b)/(cx+d)",
            font_size=26,
            color=YELLOW,
            weight="BOLD",
        )
        enonce.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Deuxième famille de fonctions : les fonctions "
                "homographiques, de la forme f de x égale a x plus b, sur "
                "c x plus d, avec c non nul et a d moins b c non nul. "
                "Voyons comment le plan d'étude s'applique ici."
            )
        ) as tracker:
            self.play(Write(titre))
            self.play(FadeIn(enonce))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(enonce))

        # --- Cadre général : domaine, asymptotes, dérivée ------------------
        cadre_domaine = example_box(
            MathTex(
                r"D_f = \mathbb{R} \setminus \left\{-\dfrac{d}{c}\right\}"
                r"\qquad \text{asymptotes : } x=-\dfrac{d}{c} \ \text{ et } \ y=\dfrac{a}{c}",
                font_size=27,
            ),
            box_width=11.2,
        )
        cadre_domaine.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Le domaine de définition est ℝ privé de moins d sur c, "
                "valeur qui annule le dénominateur. La courbe admet "
                "toujours deux asymptotes : la verticale x égale moins d "
                "sur c, et l'horizontale y égale a sur c, obtenue en "
                "divisant numérateur et dénominateur par x à l'infini."
            )
        ) as tracker:
            self.play(FadeIn(cadre_domaine))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(cadre_domaine))

        cadre_derivee = example_box(
            MathTex(
                r"f'(x) = \dfrac{ad-bc}{(cx+d)^2}", font_size=32
            ),
            box_width=6.5,
        )
        cadre_derivee.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "La dérivée se calcule avec la formule du quotient : f "
                "prime de x égale a d moins b c, sur c x plus d au carré. "
                "Le dénominateur étant toujours strictement positif, le "
                "signe de f prime est constant, entièrement fixé par le "
                "signe du numérateur a d moins b c."
            )
        ) as tracker:
            self.play(FadeIn(cadre_derivee))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(cadre_derivee))

        # --- Théorème monotonie « sur chaque intervalle » -----------------
        theo_monotonie = theorem_box(
            Text(
                _wrap(
                    "f' garde un signe constant sur Df, donc f est monotone "
                    "SUR CHACUN des deux intervalles séparément — jamais "
                    "« sur ℝ\\{-d/c} tout entier » (f n'y est pas définie).",
                    width=58,
                ),
                font_size=22,
            ),
            box_width=11.2,
        )
        theo_monotonie.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Théorème de monotonie, à formuler avec précision : f "
                "prime gardant un signe constant sur Df, la fonction est "
                "monotone sur chacun des deux intervalles séparément — "
                "jamais « sur ℝ privé de moins d sur c tout entier », "
                "puisque f n'est justement pas définie en ce point."
            )
        ) as tracker:
            self.play(FadeIn(theo_monotonie))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(theo_monotonie))

        # --- Centre de symétrie ---------------------------------------------
        theo_centre = theorem_box(
            Text(
                "Le centre de symétrie de Cf est le point d'intersection "
                "des deux asymptotes.",
                font_size=23,
                weight="BOLD",
            ),
            box_width=10.0,
        )
        theo_centre.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Autre propriété remarquable : le centre de symétrie de la "
                "courbe d'une fonction homographique est exactement le "
                "point d'intersection de ses deux asymptotes."
            )
        ) as tracker:
            self.play(FadeIn(theo_centre))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(theo_centre))

        # --- Exemple résolu complet : f(x) = (2x-1)/(x+1) -----------------------
        enonce_ex = Text(
            "Exemple résolu — f(x) = (2x-1)/(x+1)",
            font_size=27,
            color=YELLOW,
            weight="BOLD",
        )
        enonce_ex.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Étudions complètement f de x égale deux x moins un, sur x "
                "plus un."
            )
        ) as tracker:
            self.play(FadeIn(enonce_ex))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(enonce_ex))

        etape_domaine = example_box(
            MathTex(
                r"D_f = \mathbb{R} \setminus \{-1\} \qquad "
                r"f'(x) = \dfrac{2\times1-(-1)\times1}{(x+1)^2} = \dfrac{3}{(x+1)^2} > 0",
                font_size=25,
            ),
            box_width=11.6,
        )
        etape_domaine.next_to(titre, DOWN, buff=0.55)

        with self.voiceover(
            text=(
                "Domaine : ℝ privé de moins un, valeur qui annule x plus "
                "un. Dérivée : deux fois un, moins moins un fois un, sur x "
                "plus un au carré, soit trois sur x plus un au carré, "
                "toujours strictement positif."
            )
        ) as tracker:
            self.play(FadeIn(etape_domaine))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(etape_domaine))

        etape_asymptotes = example_box(
            MathTex(
                r"\lim_{x\to-1} f(x) = \pm\infty \ \Longrightarrow \ x=-1"
                r"\qquad \lim_{x\to\pm\infty} f(x) = 2 \ \Longrightarrow \ y=2",
                font_size=26,
            ),
            box_width=11.4,
        )
        etape_asymptotes.next_to(titre, DOWN, buff=0.55)

        with self.voiceover(
            text=(
                "Les asymptotes : x égale moins un, verticale, puisque le "
                "dénominateur s'annule là. Et y égale deux, horizontale, "
                "puisque le rapport des coefficients dominants deux x sur "
                "x tend vers deux à l'infini."
            )
        ) as tracker:
            self.play(FadeIn(etape_asymptotes))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(etape_asymptotes))

        tableau_ex = MathTex(
            r"""
            \begin{array}{c|ccc}
            x & -\infty & -1 & +\infty \\
            \hline
            f'(x) & & \| & \\
            & + & \| & + \\
            \hline
            f(x) & 2 \nearrow +\infty & \| & -\infty \nearrow 2
            \end{array}
            """,
            font_size=23,
        )
        tableau_ex.next_to(titre, DOWN, buff=0.6)

        with self.voiceover(
            text=(
                "Le tableau de variation présente une double barre en "
                "moins un, la valeur exclue du domaine. f est strictement "
                "croissante de deux à plus l'infini sur le premier "
                "intervalle, puis strictement croissante de moins "
                "l'infini à deux sur le second — deux croissances "
                "distinctes, jamais une seule sur ℝ privé de moins un."
            )
        ) as tracker:
            self.play(FadeIn(tableau_ex))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(tableau_ex))

        etape_symetrie = example_box(
            MathTex(r"\Omega(-1\,;2) \text{ centre de symétrie de } C_f", font_size=28),
            box_width=8.0,
        )
        etape_symetrie.next_to(titre, DOWN, buff=0.55)

        with self.voiceover(
            text=(
                "Le point oméga de coordonnées moins un et deux, "
                "intersection des deux asymptotes, est centre de symétrie "
                "de la courbe."
            )
        ) as tracker:
            self.play(FadeIn(etape_symetrie))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(etape_symetrie))

        # --- Tracé de la courbe ------------------------------------------------
        axes = Axes(
            x_range=[-5, 4, 1], y_range=[-2, 6, 2], x_length=7.0, y_length=4.5,
            axis_config={"color": WHITE, "font_size": 16},
        )
        axes.move_to(titre.get_center() + DOWN * 3.5)

        def f(x):
            return (2 * x - 1) / (x + 1)

        courbe_gauche = axes.plot(f, x_range=[-4.6, -1.35], color="#1E90FF")
        courbe_droite = axes.plot(f, x_range=[-0.6, 3.7], color="#1E90FF")
        asym_v = DashedLine(axes.c2p(-1, -2), axes.c2p(-1, 6), color=YELLOW)
        asym_h = DashedLine(axes.c2p(-5, 2), axes.c2p(4, 2), color=YELLOW)
        pt_omega = Dot(axes.c2p(-1, 2), color="#B42E41")
        schema = VGroup(axes, courbe_gauche, courbe_droite, asym_v, asym_h, pt_omega)

        with self.voiceover(
            text=(
                "Voici la courbe : deux branches, chacune croissante, se "
                "rapprochant des deux asymptotes en pointillés, et "
                "parfaitement symétriques par rapport au point oméga, en "
                "rouge — la forme caractéristique de toute fonction "
                "homographique."
            )
        ) as tracker:
            self.play(FadeIn(schema))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(schema))

        # --- À retenir ---------------------------------------------------------
        retenir = essentiel_box(
            Text(
                _wrap(
                    "Homographique : deux asymptotes (x=-d/c, y=a/c), "
                    "monotone sur chaque intervalle séparément (jamais sur "
                    "ℝ privé d'un point tout entier), centre de symétrie = "
                    "intersection des asymptotes.",
                    width=58,
                ),
                font_size=22,
            ),
            box_width=11.2,
        )
        retenir.next_to(titre, DOWN, buff=0.6)

        with self.voiceover(
            text=(
                "À retenir : une fonction homographique possède toujours "
                "deux asymptotes, verticale et horizontale, est monotone "
                "sur chacun des deux intervalles séparément, et son centre "
                "de symétrie est exactement l'intersection de ces deux "
                "asymptotes."
            )
        ) as tracker:
            self.play(FadeIn(retenir))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(retenir))

        # --- Piège à éviter ------------------------------------------------
        piege = warning_box(
            Text(
                _wrap(
                    "Piège classique : ne JAMAIS écrire « f croissante sur "
                    "ℝ\\{-1} » — c'est faux, car f n'est pas définie en -1 "
                    "et les deux branches n'ont aucun lien de croissance "
                    "entre elles. Toujours écrire « sur chacun des deux "
                    "intervalles ».",
                    width=58,
                ),
                font_size=22,
            ),
            box_width=11.2,
        )
        piege.next_to(titre, DOWN, buff=0.6)

        with self.voiceover(
            text=(
                "Piège classique, très surveillé au bac : ne jamais écrire "
                "« f croissante sur ℝ privé de moins un » — c'est faux, car "
                "f n'est pas définie en moins un, et les deux branches "
                "n'ont aucun lien de croissance entre elles. La formulation "
                "correcte est toujours « sur chacun des deux intervalles »."
            )
        ) as tracker:
            self.play(FadeIn(piege))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(titre), FadeOut(piege))
