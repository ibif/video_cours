"""
scenes/Maths_StatistiqueUneVariable_07.py — Chapitre 17 « Statistique à une
variable » (1ereC, Maths), scène 07.

§ Quartiles et moyenne : définitions Q1 (25% des individus ≤ Q1) et Q3
(75% des individus ≤ Q3). Méthode série discrète (rang = premier entier
≥ N/4, resp. ≥ 3N/4) et série en classes (interpolation comme la médiane,
avec N/4 et 3N/4). Exemple (reprise de l'exemple 1 : Q1=10, Q3=14).
Définition moyenne x̄ = (Σn_i x_i)/N = Σf_i x_i (x_i = centre de classe si
série regroupée). Propriété de linéarité (y_i=ax_i+b ⟹ ȳ=ax̄+b). Exemple :
x̄=11,875 pour l'exemple 1.
Source : 1ereC/Maths.pdf, chapitre 17, pages 206-207.
"""

import textwrap

from manim import DOWN, UP, YELLOW, FadeIn, FadeOut, MathTex, Text, VGroup, Write

from shapes.base_scene import NotionScene
from shapes.boxes import definition_box, example_box, property_box, scene_title, warning_box

# --- Données reprises de la scène 02 (notes /20 de 40 élèves) --------------
NOTES = [8, 9, 10, 11, 12, 13, 14]
EFFECTIFS = [2, 1, 8, 3, 12, 3, 11]
ECC = [2, 3, 11, 14, 26, 29, 40]
N_TOTAL = 40


def _wrap(text: str, width: int = 54) -> str:
    return "\n".join(textwrap.fill(line, width=width) for line in text.split("\n"))


class QuartilesMoyenne(NotionScene):
    def construct(self):
        titre = scene_title("Statistique — Quartiles et moyenne")
        titre.scale(0.48)
        titre.to_edge(UP)

        # --- Énoncé : mise en situation --------------------------------------
        mise_en_situation = Text(
            _wrap(
                "La médiane partage la population en deux. Les "
                "QUARTILES affinent cette idée en la partageant en "
                "quatre, tandis que la MOYENNE en donne une synthèse "
                "d'un genre différent.",
                width=56,
            ),
            font_size=23,
        )
        mise_en_situation.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "La médiane partage la population en deux groupes "
                "égaux. Les quartiles affinent cette idée en la "
                "partageant cette fois en quatre, tandis que la "
                "moyenne, elle, en donne une synthèse d'un genre tout "
                "différent."
            )
        ) as tracker:
            self.play(Write(titre))
            self.play(FadeIn(mise_en_situation))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(mise_en_situation))

        # --- Raisonnement : quartiles -------------------------------------------
        def_quartiles = definition_box(
            VGroup(
                Text("Premier et troisième quartiles", font_size=22, weight="BOLD"),
                MathTex(r"Q_1 : \ \text{25\% des individus ont une modalité} \le Q_1", font_size=21),
                MathTex(r"Q_3 : \ \text{75\% des individus ont une modalité} \le Q_3", font_size=21),
            ).arrange(DOWN, buff=0.25),
        )
        def_quartiles.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Le premier quartile, Q1, est la valeur en dessous de "
                "laquelle se trouvent 25 pour cent des individus. Le "
                "troisième quartile, Q3, est la valeur en dessous de "
                "laquelle se trouvent 75 pour cent des individus. On "
                "pourrait de la même façon définir un deuxième "
                "quartile, qui n'est autre que la médiane."
            )
        ) as tracker:
            self.play(FadeIn(def_quartiles))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(def_quartiles))

        methode_quartiles = definition_box(
            VGroup(
                Text("Méthode de calcul", font_size=21, weight="BOLD"),
                Text(
                    _wrap(
                        "Série DISCRÈTE : Q1 = valeur au rang PREMIER "
                        "ENTIER ≥ N/4. Q3 = valeur au rang PREMIER "
                        "ENTIER ≥ 3N/4.",
                        width=46,
                    ),
                    font_size=19,
                ),
                Text(
                    _wrap(
                        "Série en CLASSES : même interpolation linéaire "
                        "que la médiane, en remplaçant N/2 par N/4 (pour "
                        "Q1) ou par 3N/4 (pour Q3).",
                        width=46,
                    ),
                    font_size=19,
                ),
            ).arrange(DOWN, buff=0.22),
        )
        methode_quartiles.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Pour une série discrète triée, Q1 est la valeur "
                "atteinte au rang égal au premier entier supérieur ou "
                "égal à N sur 4, et Q3 la valeur atteinte au rang égal "
                "au premier entier supérieur ou égal à 3N sur 4. Pour "
                "une série regroupée en classes, on utilise exactement "
                "la même interpolation linéaire que pour la médiane, en "
                "remplaçant simplement N sur 2 par N sur 4 pour Q1, ou "
                "par 3N sur 4 pour Q3."
            )
        ) as tracker:
            self.play(FadeIn(methode_quartiles))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(methode_quartiles))

        # --- Exemple traité : quartiles de la série des notes --------------------
        enonce_q = Text(
            _wrap(
                "Reprenons l'exemple des notes (N=40) : N/4=10 et "
                "3N/4=30, deux entiers exacts.",
                width=52,
            ),
            font_size=22,
        )
        enonce_q.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Reprenons l'exemple des notes, où N vaut 40. N sur 4 "
                "vaut 10, et 3N sur 4 vaut 30 : deux entiers exacts, ce "
                "qui simplifie le repérage des rangs."
            )
        ) as tracker:
            self.play(FadeIn(enonce_q))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(enonce_q))

        calcul_q1 = MathTex(
            r"\text{rang } 10 : \ \text{ECC}(9)=3 < 10 \le \text{ECC}(10)=11 \ \Rightarrow \ Q_1 = 10",
            font_size=22,
            color=YELLOW,
        )
        calcul_q3 = MathTex(
            r"\text{rang } 30 : \ \text{ECC}(13)=29 < 30 \le \text{ECC}(14)=40 \ \Rightarrow \ Q_3 = 14",
            font_size=22,
            color=YELLOW,
        )
        groupe_q = VGroup(calcul_q1, calcul_q3).arrange(DOWN, buff=0.3)
        groupe_q.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Au rang 10 : l'effectif cumulé croissant vaut 3 à la "
                "note 9, puis 11 à la note 10. Le rang 10 tombe donc "
                "dans le groupe de note 10 : Q1 vaut 10. Au rang 30 : "
                "l'effectif cumulé croissant vaut 29 à la note 13, puis "
                "40 à la note 14. Le rang 30 tombe dans le groupe de "
                "note 14 : Q3 vaut 14."
            )
        ) as tracker:
            self.play(Write(groupe_q))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(groupe_q))

        # --- Raisonnement : moyenne ----------------------------------------------
        def_moyenne = definition_box(
            VGroup(
                Text("Moyenne", font_size=23, weight="BOLD"),
                MathTex(r"\bar{x} = \dfrac{\sum_i n_i x_i}{N} = \sum_i f_i x_i", font_size=26),
                Text(
                    _wrap(
                        "Si la série est regroupée en classes, x_i "
                        "désigne le CENTRE de la classe.",
                        width=46,
                    ),
                    font_size=19,
                ),
            ).arrange(DOWN, buff=0.25),
        )
        def_moyenne.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "La moyenne, notée x barre, est la somme des effectifs "
                "n indice i multipliés chacun par leur modalité x "
                "indice i, le tout divisé par N ; ce qui équivaut aussi "
                "à la somme des fréquences f indice i multipliées "
                "chacune par x indice i. Si la série est regroupée en "
                "classes, x indice i désigne bien sûr le centre de "
                "chaque classe."
            )
        ) as tracker:
            self.play(FadeIn(def_moyenne))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(def_moyenne))

        prop_linearite = property_box(
            VGroup(
                Text("Propriété — Linéarité de la moyenne", font_size=20, weight="BOLD"),
                MathTex(r"y_i = a\,x_i + b \quad \Rightarrow \quad \bar{y} = a\,\bar{x} + b", font_size=25),
            ).arrange(DOWN, buff=0.25),
        )
        prop_linearite.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Une propriété très utile : si l'on transforme "
                "chaque modalité par une fonction affine, y indice i "
                "égale a fois x indice i plus b, alors la moyenne se "
                "transforme exactement de la même façon : y barre égale "
                "a fois x barre plus b."
            )
        ) as tracker:
            self.play(Write(prop_linearite))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(prop_linearite))

        # --- Exemple traité : moyenne de la série des notes -----------------------
        enonce_moy = Text(
            _wrap(
                "Calculons la moyenne exacte des notes de l'exemple 1.",
                width=48,
            ),
            font_size=22,
        )
        enonce_moy.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text="Calculons maintenant la moyenne exacte des notes de l'exemple 1."
        ) as tracker:
            self.play(FadeIn(enonce_moy))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(enonce_moy))

        calcul_moyenne = MathTex(
            r"\bar{x} = \dfrac{2(8)+1(9)+8(10)+3(11)+12(12)+3(13)+11(14)}{40} = \dfrac{475}{40} = 11{,}875",
            font_size=21,
            color=YELLOW,
        )
        calcul_moyenne.next_to(titre, DOWN, buff=0.6)

        with self.voiceover(
            text=(
                "On multiplie chaque note par son effectif, on "
                "additionne le tout, on obtient 475, puis on divise par "
                "N égale 40 : la moyenne vaut exactement 11,875 sur 20."
            )
        ) as tracker:
            self.play(Write(calcul_moyenne))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(calcul_moyenne))

        # --- À retenir --------------------------------------------------------
        recap = example_box(
            VGroup(
                Text("À retenir", font_size=22, weight="BOLD"),
                MathTex(
                    r"Q_1 = 10 \ , \quad \text{médiane} = 12 \ , \quad Q_3 = 14 \ , \quad \bar{x} = 11{,}875",
                    font_size=22,
                ),
            ).arrange(DOWN, buff=0.25),
        )
        recap.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Retenons, pour cet exemple, les quatre caractéristiques "
                "de position obtenues : Q1 égale 10, la médiane vaut "
                "12, Q3 égale 14, et la moyenne vaut 11,875."
            )
        ) as tracker:
            self.play(FadeIn(recap))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(recap))

        # --- Piège à éviter -----------------------------------------------------
        piege = warning_box(
            VGroup(
                Text("Piège — Q1/Q3 ne sont pas symétriques de la médiane", font_size=17, weight="BOLD"),
                Text(
                    _wrap(
                        "Rien n'oblige Q3 - médiane = médiane - Q1 : "
                        "dans l'exemple, 14-12=2 mais 12-10=2 (égalité "
                        "ici par coïncidence, pas une règle générale).",
                        width=46,
                    ),
                    font_size=18,
                ),
            ).arrange(DOWN, buff=0.2),
        )
        piege.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Piège à garder en tête : rien n'oblige les quartiles à "
                "être symétriques autour de la médiane. Dans notre "
                "exemple, Q3 moins la médiane égale 2, et la médiane "
                "moins Q1 égale aussi 2 — mais c'est une coïncidence de "
                "cet exemple précis, pas une règle générale valable "
                "pour toute série statistique."
            )
        ) as tracker:
            self.play(FadeIn(piege))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(piege), FadeOut(titre))
