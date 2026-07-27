"""
scenes/Maths_StatistiqueUneVariable_08.py — Chapitre 17 « Statistique à une
variable » (1ereC, Maths), scène 08.

§ Étendue, écart interquartile, écart moyen : définition étendue
(max - min). Définition intervalle interquartile [Q1;Q3] et écart
interquartile Q3-Q1 (robuste, insensible aux valeurs extrêmes,
contrairement à l'étendue). Définition écart moyen
e_m = (1/N)Σn_i|x_i - x̄| (distance moyenne à la moyenne). Reprise de
l'exemple des notes (scène 02/07) pour les trois calculs.
Source : 1ereC/Maths.pdf, chapitre 17, pages 207-208.
"""

import textwrap

from manim import DOWN, UP, YELLOW, FadeIn, FadeOut, MathTex, Table, Text, VGroup, WHITE, Write

from shapes.base_scene import NotionScene
from shapes.boxes import definition_box, example_box, scene_title, warning_box

# --- Données reprises des scènes 02 et 07 (notes /20 de 40 élèves) --------
NOTES = [8, 9, 10, 11, 12, 13, 14]
EFFECTIFS = [2, 1, 8, 3, 12, 3, 11]
N_TOTAL = 40
MOYENNE = 11.875
ECARTS_ABSOLUS = ["3,875", "2,875", "1,875", "0,875", "0,125", "1,125", "2,125"]
CONTRIBUTIONS = ["7,75", "2,875", "15", "2,625", "1,5", "3,375", "23,375"]


def _wrap(text: str, width: int = 54) -> str:
    return "\n".join(textwrap.fill(line, width=width) for line in text.split("\n"))


def _tableau_ecart_moyen() -> Table:
    valeurs = [
        [str(n) for n in EFFECTIFS],
        ECARTS_ABSOLUS,
        CONTRIBUTIONS,
    ]
    table = Table(
        valeurs,
        row_labels=[
            MathTex(r"n_i", font_size=18),
            MathTex(r"|x_i - \bar{x}|", font_size=16),
            MathTex(r"n_i |x_i - \bar{x}|", font_size=16),
        ],
        col_labels=[MathTex(str(x), font_size=18) for x in NOTES],
        top_left_entry=MathTex(r"x_i", font_size=18),
        element_to_mobject=MathTex,
        element_to_mobject_config={"font_size": 16},
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


class EtenduEcartInterquartileEcartMoyen(NotionScene):
    def construct(self):
        titre = scene_title("Statistique — Étendue, écart interquartile, écart moyen")
        titre.scale(0.40)
        titre.to_edge(UP)

        # --- Énoncé : mise en situation --------------------------------------
        mise_en_situation = Text(
            _wrap(
                "Deux séries peuvent avoir la même moyenne mais être "
                "très différentes : l'une resserrée, l'autre très "
                "dispersée. Il faut donc, en plus de la position, "
                "mesurer la DISPERSION.",
                width=56,
            ),
            font_size=23,
        )
        mise_en_situation.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Nous entamons la quatrième et dernière partie du "
                "chapitre : les caractéristiques de dispersion. Deux "
                "séries peuvent en effet avoir exactement la même "
                "moyenne, mais être très différentes : l'une resserrée "
                "autour de cette moyenne, l'autre très étalée. Il faut "
                "donc, en plus de la position, mesurer la dispersion "
                "d'une série."
            )
        ) as tracker:
            self.play(Write(titre))
            self.play(FadeIn(mise_en_situation))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(mise_en_situation))

        # --- Raisonnement : étendue ----------------------------------------------
        def_etendue = definition_box(
            VGroup(
                Text("Étendue", font_size=22, weight="BOLD"),
                MathTex(r"\text{Étendue} = x_{\max} - x_{\min}", font_size=25),
            ).arrange(DOWN, buff=0.25),
        )
        def_etendue.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "La plus simple des caractéristiques de dispersion est "
                "l'étendue : la différence entre la plus grande et la "
                "plus petite modalité de la série."
            )
        ) as tracker:
            self.play(FadeIn(def_etendue))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(def_etendue))

        def_interquartile = definition_box(
            VGroup(
                Text("Intervalle et écart interquartile", font_size=21, weight="BOLD"),
                MathTex(r"\text{intervalle interquartile} = [Q_1\,;\,Q_3]", font_size=22),
                MathTex(r"\text{écart interquartile} = Q_3 - Q_1", font_size=23),
                Text(
                    _wrap(
                        "Contient les 50% CENTRAUX de la population : "
                        "ROBUSTE, insensible aux valeurs extrêmes "
                        "(contrairement à l'étendue).",
                        width=46,
                    ),
                    font_size=19,
                ),
            ).arrange(DOWN, buff=0.22),
        )
        def_interquartile.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "L'intervalle interquartile est l'intervalle entre Q1 "
                "et Q3, et l'écart interquartile est sa longueur, Q3 "
                "moins Q1. Cet intervalle contient toujours les 50 pour "
                "cent centraux de la population. Son grand avantage sur "
                "l'étendue : il est robuste, c'est-à-dire insensible aux "
                "valeurs extrêmes, puisqu'il ignore volontairement le "
                "quart le plus bas et le quart le plus haut de la "
                "série."
            )
        ) as tracker:
            self.play(FadeIn(def_interquartile))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(def_interquartile))

        def_ecart_moyen = definition_box(
            VGroup(
                Text("Écart moyen", font_size=22, weight="BOLD"),
                MathTex(r"e_m = \dfrac{1}{N}\sum_i n_i\,|x_i - \bar{x}|", font_size=25),
                Text(
                    _wrap(
                        "Distance MOYENNE de chaque individu à la "
                        "moyenne (valeur absolue, car les écarts "
                        "positifs et négatifs se compenseraient sinon).",
                        width=46,
                    ),
                    font_size=19,
                ),
            ).arrange(DOWN, buff=0.22),
        )
        def_ecart_moyen.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "L'écart moyen, noté e indice m, est la distance "
                "moyenne de chaque individu à la moyenne de la série : "
                "on prend la valeur absolue de chaque écart à la "
                "moyenne, pondérée par son effectif, et on divise le "
                "tout par N. La valeur absolue est indispensable, car "
                "sans elle, les écarts positifs et négatifs se "
                "compenseraient et la somme resterait toujours nulle."
            )
        ) as tracker:
            self.play(FadeIn(def_ecart_moyen))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(def_ecart_moyen))

        # --- Exemple traité : reprise de la série des notes -----------------------
        enonce = Text(
            _wrap(
                "Reprenons l'exemple des notes (N=40, moyenne=11,875, "
                "Q1=10, Q3=14) pour calculer les trois indicateurs.",
                width=52,
            ),
            font_size=21,
        )
        enonce.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Reprenons une dernière fois l'exemple des notes, où N "
                "vaut 40, la moyenne vaut 11,875, Q1 vaut 10 et Q3 vaut "
                "14, pour calculer nos trois indicateurs de dispersion."
            )
        ) as tracker:
            self.play(FadeIn(enonce))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(enonce))

        calcul_etendue_interq = MathTex(
            r"\text{Étendue} = 14 - 8 = 6 \qquad \text{écart interquartile} = 14 - 10 = 4",
            font_size=24,
            color=YELLOW,
        )
        calcul_etendue_interq.next_to(titre, DOWN, buff=0.55)

        with self.voiceover(
            text=(
                "La note maximale est 14, la minimale 8 : l'étendue "
                "vaut donc 6. Et comme Q3 vaut 14 et Q1 vaut 10, "
                "l'écart interquartile vaut 4 — nettement plus petit, "
                "car il ignore les 25 pour cent les plus bas et les 25 "
                "pour cent les plus hauts."
            )
        ) as tracker:
            self.play(Write(calcul_etendue_interq))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(calcul_etendue_interq))

        tableau = _tableau_ecart_moyen()
        tableau.scale(0.55)
        tableau.next_to(titre, DOWN, buff=0.35)

        with self.voiceover(
            text=(
                "Pour l'écart moyen, on construit un tableau à trois "
                "lignes : l'effectif, l'écart absolu à la moyenne "
                "11,875, puis le produit de l'effectif par cet écart "
                "absolu."
            )
        ) as tracker:
            self.play(FadeIn(tableau))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(tableau))

        calcul_em = MathTex(
            r"e_m = \dfrac{7{,}75+2{,}875+15+2{,}625+1{,}5+3{,}375+23{,}375}{40} = \dfrac{56{,}5}{40} \approx 1{,}41",
            font_size=21,
            color=YELLOW,
        )
        calcul_em.next_to(titre, DOWN, buff=0.6)

        with self.voiceover(
            text=(
                "En additionnant la dernière ligne du tableau, on "
                "obtient 56,5, que l'on divise par N égale 40 : l'écart "
                "moyen vaut environ 1,41. Autrement dit, une note "
                "s'écarte en moyenne d'un peu plus d'un point de la "
                "moyenne de la classe."
            )
        ) as tracker:
            self.play(Write(calcul_em))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(calcul_em))

        # --- À retenir --------------------------------------------------------
        recap = example_box(
            VGroup(
                Text("À retenir", font_size=22, weight="BOLD"),
                MathTex(
                    r"\text{Étendue}=6 \ , \quad \text{écart interquartile}=4 \ , \quad e_m \approx 1{,}41",
                    font_size=21,
                ),
            ).arrange(DOWN, buff=0.25),
        )
        recap.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Retenons ces trois résultats : une étendue de 6, un "
                "écart interquartile de 4, et un écart moyen d'environ "
                "1,41 point."
            )
        ) as tracker:
            self.play(FadeIn(recap))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(recap))

        # --- Piège à éviter -----------------------------------------------------
        piege = warning_box(
            VGroup(
                Text("Piège — L'étendue ne regarde QUE 2 valeurs", font_size=19, weight="BOLD"),
                Text(
                    _wrap(
                        "Une seule note extrême (ex : un 20 isolé) peut "
                        "faire exploser l'étendue sans que la série "
                        "soit globalement plus dispersée : l'écart "
                        "interquartile est alors bien plus fiable.",
                        width=46,
                    ),
                    font_size=18,
                ),
            ).arrange(DOWN, buff=0.2),
        )
        piege.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Piège à garder à l'esprit : l'étendue ne regarde que "
                "deux valeurs, le minimum et le maximum. Une seule note "
                "extrême, un 20 isolé par exemple, peut faire exploser "
                "l'étendue sans que la série soit globalement plus "
                "dispersée. Dans ce cas, l'écart interquartile, qui "
                "ignore les valeurs extrêmes, donne une image bien plus "
                "fiable de la dispersion réelle."
            )
        ) as tracker:
            self.play(FadeIn(piege))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(piege), FadeOut(titre))
