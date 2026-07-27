"""
scenes/Maths_StatistiqueUneVariable_09.py — Chapitre 17 « Statistique à une
variable » (1ereC, Maths), scène 09.

§ Variance, écart-type et formule de Koenig : définition variance
V = (1/N)Σn_i(x_i - x̄)² et écart-type σ = √V, interprétation
(homogène/hétérogène). Théorème — formule de Koenig
V = (1/N)Σn_i x_i² - x̄², AVEC démonstration complète (développement du
carré). Propriété de transformation affine (V(aX+b) = a²V(X), σ = |a|σ_X).
Exemple résolu 4 complet : reprise des sacs de cacao (scène 03), tableau à
colonnes x_i / n_i / n_i x_i / n_i x_i², calcul x̄≈73,5 kg, V=29, σ≈5,39 kg,
interprétation.
Source : 1ereC/Maths.pdf, chapitre 17, pages 208-209.
"""

import textwrap

from manim import DOWN, UP, WHITE, YELLOW, FadeIn, FadeOut, MathTex, Table, Text, VGroup, Write

from shapes.base_scene import NotionScene
from shapes.boxes import definition_box, example_box, property_box, scene_title, theorem_box, warning_box

# --- Données reprises de la scène 03 (60 sacs de cacao pesés à Daloa) -----
CENTRES = [62.5, 67.5, 72.5, 77.5, 82.5]
EFFECTIFS = [4, 10, 24, 14, 8]
N_TOTAL = 60
MOYENNE = 73.5
N_X = ["250", "675", "1740", "1085", "660"]
N_X2 = ["15625", "45562,5", "126150", "84087,5", "54450"]


def _wrap(text: str, width: int = 54) -> str:
    return "\n".join(textwrap.fill(line, width=width) for line in text.split("\n"))


def _tableau_koenig() -> Table:
    valeurs = [
        [str(n) for n in EFFECTIFS],
        N_X,
        N_X2,
    ]
    table = Table(
        valeurs,
        row_labels=[
            MathTex(r"n_i", font_size=18),
            MathTex(r"n_i x_i", font_size=17),
            MathTex(r"n_i x_i^2", font_size=17),
        ],
        col_labels=[MathTex(str(x).replace(".", "{,}"), font_size=17) for x in CENTRES],
        top_left_entry=MathTex(r"x_i", font_size=18),
        element_to_mobject=MathTex,
        element_to_mobject_config={"font_size": 15},
        line_config={"color": WHITE, "stroke_width": 1},
        include_outer_lines=True,
        v_buff=0.2,
        h_buff=0.22,
    )
    table.get_entries().set_color(WHITE)
    table.get_row_labels().set_color(YELLOW)
    table.get_col_labels().set_color(YELLOW)
    if table.top_left_entry is not None:
        table.top_left_entry.set_color(YELLOW)
    for line in table.get_horizontal_lines():
        line.set_color(WHITE)
    for line in table.get_vertical_lines():
        line.set_color(WHITE)
    return table


class VarianceEcartTypeKoenig(NotionScene):
    def construct(self):
        titre = scene_title("Statistique — Variance, écart-type, formule de Koenig")
        titre.scale(0.40)
        titre.to_edge(UP)

        # --- Énoncé : mise en situation --------------------------------------
        mise_en_situation = Text(
            _wrap(
                "L'écart moyen mesure la dispersion, mais sa valeur "
                "absolue le rend difficile à manipuler algébriquement. "
                "La variance résout ce problème en élevant les écarts "
                "au carré.",
                width=56,
            ),
            font_size=23,
        )
        mise_en_situation.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "L'écart moyen mesure bien la dispersion, mais sa "
                "valeur absolue le rend difficile à manipuler "
                "algébriquement. La variance, l'indicateur de "
                "dispersion le plus utilisé en pratique, résout ce "
                "problème en élevant les écarts au carré plutôt qu'en "
                "prenant leur valeur absolue."
            )
        ) as tracker:
            self.play(Write(titre))
            self.play(FadeIn(mise_en_situation))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(mise_en_situation))

        # --- Raisonnement : définition variance/écart-type ------------------------
        def_variance = definition_box(
            VGroup(
                Text("Variance et écart-type", font_size=22, weight="BOLD"),
                MathTex(r"V = \dfrac{1}{N}\sum_i n_i (x_i - \bar{x})^2 \qquad \sigma = \sqrt{V}", font_size=25),
                Text(
                    _wrap(
                        "σ (écart-type) PETIT ⟹ série HOMOGÈNE "
                        "(resserrée autour de x̄). σ GRAND ⟹ série "
                        "HÉTÉROGÈNE (dispersée).",
                        width=46,
                    ),
                    font_size=19,
                ),
            ).arrange(DOWN, buff=0.22),
        )
        def_variance.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "La variance V est la moyenne des carrés des écarts à "
                "la moyenne, pondérés par les effectifs. L'écart-type "
                "sigma en est la racine carrée — ce retour à l'unité de "
                "départ, en kilogrammes ou en points par exemple, rend "
                "l'écart-type plus facile à interpréter que la "
                "variance. Un écart-type petit signale une série "
                "homogène, resserrée autour de la moyenne ; un "
                "écart-type grand signale une série hétérogène, "
                "dispersée."
            )
        ) as tracker:
            self.play(FadeIn(def_variance))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(def_variance))

        # --- Théorème de Koenig + démonstration ------------------------------------
        koenig = theorem_box(
            VGroup(
                Text("Théorème — Formule de Koenig", font_size=21, weight="BOLD"),
                MathTex(r"V = \dfrac{1}{N}\sum_i n_i x_i^2 \ - \ \bar{x}^2", font_size=26),
            ).arrange(DOWN, buff=0.25),
        )
        koenig.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "La formule de Koenig donne une seconde expression, "
                "bien plus pratique pour calculer : la variance vaut la "
                "moyenne des carrés des modalités, moins le carré de la "
                "moyenne."
            )
        ) as tracker:
            self.play(FadeIn(koenig))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(koenig))

        demo_etape1 = MathTex(
            r"N V = \sum_i n_i (x_i-\bar{x})^2 = \sum_i n_i \left(x_i^2 - 2 x_i \bar{x} + \bar{x}^2\right)",
            font_size=22,
        )
        demo_etape2 = MathTex(
            r"= \sum_i n_i x_i^2 \ - \ 2\bar{x}\sum_i n_i x_i \ + \ \bar{x}^2 \sum_i n_i",
            font_size=22,
        )
        demo_etape3 = MathTex(
            r"= \sum_i n_i x_i^2 \ - \ 2\bar{x}(N\bar{x}) \ + \ \bar{x}^2 N \quad (\text{car } \textstyle\sum_i n_i x_i = N\bar{x})",
            font_size=21,
        )
        demo_etape4 = MathTex(
            r"= \sum_i n_i x_i^2 \ - \ N\bar{x}^2 \quad \Rightarrow \quad V = \dfrac{1}{N}\sum_i n_i x_i^2 \ - \ \bar{x}^2 \ \blacksquare",
            font_size=22,
            color=YELLOW,
        )
        demonstration = VGroup(demo_etape1, demo_etape2, demo_etape3, demo_etape4).arrange(DOWN, buff=0.3)
        demonstration.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Démontrons-la. On développe le carré dans la "
                "définition : x indice i moins x barre au carré donne x "
                "indice i au carré, moins 2 x indice i x barre, plus x "
                "barre au carré. On distribue la somme sur les trois "
                "termes. Le second terme fait apparaître la somme des n "
                "indice i x indice i, qui vaut par définition N fois x "
                "barre. Le troisième terme fait apparaître la somme des "
                "n indice i, qui vaut N. Après simplification, il reste "
                "exactement la somme des n indice i x indice i au "
                "carré, moins N x barre au carré. En divisant par N, on "
                "retrouve bien la formule de Koenig."
            )
        ) as tracker:
            self.play(Write(demo_etape1))
            self.wait(1)
            self.play(Write(demo_etape2))
            self.wait(1)
            self.play(Write(demo_etape3))
            self.wait(1)
            self.play(Write(demo_etape4))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(demonstration))

        prop_affine = property_box(
            VGroup(
                Text("Propriété — Transformation affine", font_size=20, weight="BOLD"),
                MathTex(r"Y = aX + b \quad \Rightarrow \quad V(Y) = a^2\,V(X) \quad \sigma_Y = |a|\,\sigma_X", font_size=23),
            ).arrange(DOWN, buff=0.25),
        )
        prop_affine.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Autre propriété utile : si l'on transforme toutes les "
                "modalités par une fonction affine, a fois X plus b, la "
                "variance est multipliée par a au carré, et l'écart-type "
                "par la valeur absolue de a. Remarquez que le décalage "
                "b, lui, disparaît complètement : ajouter une constante "
                "ne change jamais la dispersion d'une série."
            )
        ) as tracker:
            self.play(Write(prop_affine))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(prop_affine))

        # --- Exemple résolu 4 : sacs de cacao ---------------------------------------
        enonce = Text(
            _wrap(
                "Exemple résolu 4 : calculons variance et écart-type "
                "des masses des 60 sacs de cacao (scène 03).",
                width=52,
            ),
            font_size=21,
        )
        enonce.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Exemple résolu numéro 4. Calculons la variance et "
                "l'écart-type des masses des 60 sacs de cacao pesés à "
                "Daloa, l'exemple de la scène 3."
            )
        ) as tracker:
            self.play(FadeIn(enonce))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(enonce))

        tableau = _tableau_koenig()
        tableau.scale(0.52)
        tableau.next_to(titre, DOWN, buff=0.35)

        with self.voiceover(
            text=(
                "On construit un tableau à colonnes : le centre x "
                "indice i, l'effectif n indice i, le produit n indice i "
                "fois x indice i, et enfin n indice i fois x indice i "
                "au carré. On additionnera les deux dernières lignes."
            )
        ) as tracker:
            self.play(FadeIn(tableau))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(tableau))

        calcul_moyenne = MathTex(
            r"\bar{x} = \dfrac{250+675+1740+1085+660}{60} = \dfrac{4410}{60} = 73{,}5\text{ kg}",
            font_size=22,
            color=YELLOW,
        )
        calcul_moyenne.next_to(titre, DOWN, buff=0.6)

        with self.voiceover(
            text=(
                "La somme des n indice i x indice i vaut 4410, divisée "
                "par 60, cela donne une moyenne de 73,5 kilogrammes."
            )
        ) as tracker:
            self.play(Write(calcul_moyenne))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(calcul_moyenne))

        calcul_variance = MathTex(
            r"V = \dfrac{325875}{60} - 73{,}5^2 = 5431{,}25 - 5402{,}25 = 29",
            font_size=23,
            color=YELLOW,
        )
        calcul_ecart_type = MathTex(
            r"\sigma = \sqrt{29} \approx 5{,}39\text{ kg}",
            font_size=25,
            color=YELLOW,
        )
        groupe_var = VGroup(calcul_variance, calcul_ecart_type).arrange(DOWN, buff=0.3)
        groupe_var.next_to(titre, DOWN, buff=0.55)

        with self.voiceover(
            text=(
                "La somme des n indice i x indice i au carré vaut "
                "325875. Divisée par 60, cela donne 5431,25. On "
                "soustrait le carré de la moyenne, 5402,25 : la "
                "variance vaut exactement 29 — un résultat positif, "
                "comme il se doit toujours. L'écart-type est sa racine "
                "carrée, environ 5,39 kilogrammes."
            )
        ) as tracker:
            self.play(Write(groupe_var))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(groupe_var))

        interpretation = Text(
            _wrap(
                "Interprétation : la masse d'un sac de cacao s'écarte "
                "en moyenne d'environ 5,39 kg autour de 73,5 kg — une "
                "dispersion modérée pour cette production.",
                width=50,
            ),
            font_size=20,
        )
        interpretation.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Interprétation : la masse d'un sac de cacao pris au "
                "hasard s'écarte en moyenne d'environ 5,39 kilogrammes "
                "autour des 73,5 kilogrammes de moyenne — une "
                "dispersion modérée pour cette production."
            )
        ) as tracker:
            self.play(FadeIn(interpretation))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(interpretation))

        # --- À retenir --------------------------------------------------------
        recap = example_box(
            VGroup(
                Text("À retenir", font_size=22, weight="BOLD"),
                MathTex(r"\text{Koenig} : V = \overline{x^2} - \bar{x}^2 \quad (\text{toujours plus rapide qu'appliquer la définition})", font_size=20),
            ).arrange(DOWN, buff=0.25),
        )
        recap.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Retenons l'essentiel : la formule de Koenig, variance "
                "égale la moyenne des carrés moins le carré de la "
                "moyenne, est presque toujours plus rapide à appliquer "
                "que la définition directe, car elle évite de calculer "
                "chaque écart individuellement."
            )
        ) as tracker:
            self.play(FadeIn(recap))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(recap))

        # --- Piège à éviter -----------------------------------------------------
        piege = warning_box(
            VGroup(
                Text("Piège — Toujours contrôler V ≥ 0", font_size=20, weight="BOLD"),
                Text(
                    _wrap(
                        "Une variance négative signale FORCÉMENT une "
                        "erreur de calcul (somme des n_i x_i² ou "
                        "x̄ mal calculés) : V est une moyenne de carrés, "
                        "donc toujours positive ou nulle.",
                        width=46,
                    ),
                    font_size=18,
                ),
            ).arrange(DOWN, buff=0.2),
        )
        piege.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Piège à ne jamais négliger : contrôlez systématiquement "
                "que V est positive ou nulle. Une variance négative "
                "signale forcément une erreur de calcul, sur la somme "
                "des n indice i x indice i au carré ou sur la moyenne, "
                "car la variance est par nature une moyenne de carrés, "
                "donc toujours positive ou nulle."
            )
        ) as tracker:
            self.play(FadeIn(piege))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(piege), FadeOut(titre))
