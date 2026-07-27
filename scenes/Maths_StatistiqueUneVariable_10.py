"""
scenes/Maths_StatistiqueUneVariable_10.py — Chapitre 17 « Statistique à une
variable » (1ereC, Maths), scène 10 (synthèse, dernière scène du chapitre
et DERNIÈRE scène du programme de 1ère C, 17/17).

§ Synthèse : tableau récapitulatif de toutes les caractéristiques (mode,
médiane, quartiles, moyenne, étendue, écart interquartile, écart moyen,
variance, écart-type) avec notation/rôle/formule. Méthode 1 (choisir les
classes : amplitude égale, 5 à 10 classes). Méthode 2 (calculer la
médiane en 4 étapes). Méthode 3 (calculer la variance rapidement avec
Koenig et un tableau à colonnes, contrôler V≥0). Méthode 4 (comparer deux
séries : moyennes puis écarts-types). Pièges : histogramme à amplitudes
inégales (aires, pas hauteurs) ; médiane (cumulés) vs moyenne (centres) ;
toujours trier une série discrète ; fréquences décimales (pas %) et
vérifier que leur somme vaut 1.
Source : 1ereC/Maths.pdf, chapitre 17, pages 209-210.
"""

import textwrap

from manim import DOWN, UP, FadeIn, FadeOut, MathTex, Text, VGroup, Write

from shapes.base_scene import NotionScene
from shapes.boxes import definition_box, essentiel_box, example_box, method_box, scene_title, warning_box


def _wrap(text: str, width: int = 54) -> str:
    return "\n".join(textwrap.fill(line, width=width) for line in text.split("\n"))


class SyntheseMethodesPieges(NotionScene):
    def construct(self):
        titre = scene_title("Statistique — Synthèse, méthodes et pièges")
        titre.scale(0.46)
        titre.to_edge(UP)

        # --- Énoncé : mise en situation --------------------------------------
        mise_en_situation = Text(
            _wrap(
                "Nous voici à la dernière scène du chapitre — et de "
                "toute l'année de 1ère C. Faisons le bilan de toutes "
                "les caractéristiques statistiques rencontrées.",
                width=56,
            ),
            font_size=23,
        )
        mise_en_situation.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Nous voici à la dernière scène de ce chapitre — et de "
                "toute l'année de première C. Faisons le bilan complet "
                "de toutes les caractéristiques statistiques "
                "rencontrées, avant de passer en revue les méthodes de "
                "résolution et les pièges classiques à éviter."
            )
        ) as tracker:
            self.play(Write(titre))
            self.play(FadeIn(mise_en_situation))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(mise_en_situation))

        # --- Raisonnement : tableau récapitulatif --------------------------------
        recap_position = definition_box(
            VGroup(
                Text("Caractéristiques de POSITION", font_size=21, weight="BOLD"),
                MathTex(r"\text{Mode / classe modale} : \text{modalité (ou centre) LA PLUS FRÉQUENTE}", font_size=18),
                MathTex(r"\text{Médiane } M : \text{partage en 2 effectifs ÉGAUX (discret ou interpolation)}", font_size=18),
                MathTex(r"Q_1,\,Q_3 : \text{partagent en QUARTILES (même principe, avec } N/4,\,3N/4)", font_size=18),
                MathTex(r"\text{Moyenne } \bar{x} = \dfrac{\sum n_i x_i}{N} = \sum f_i x_i", font_size=19),
            ).arrange(DOWN, buff=0.2),
        )
        recap_position.next_to(titre, DOWN, buff=0.35)

        with self.voiceover(
            text=(
                "Premier bloc : les caractéristiques de position. Le "
                "mode, ou la classe modale, est la modalité la plus "
                "fréquente. La médiane M partage la population en deux "
                "effectifs égaux, par lecture directe pour une série "
                "discrète, ou par interpolation linéaire pour une "
                "série en classes. Les quartiles Q1 et Q3 suivent le "
                "même principe, avec N sur 4 et 3N sur 4. Et la "
                "moyenne x barre est la somme des effectifs fois les "
                "modalités, divisée par N."
            )
        ) as tracker:
            self.play(FadeIn(recap_position))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(recap_position))

        recap_dispersion = definition_box(
            VGroup(
                Text("Caractéristiques de DISPERSION", font_size=21, weight="BOLD"),
                MathTex(r"\text{Étendue} = x_{\max}-x_{\min} \qquad \text{écart interquartile} = Q_3-Q_1", font_size=18),
                MathTex(r"\text{Écart moyen } e_m = \dfrac{1}{N}\sum n_i |x_i-\bar{x}|", font_size=19),
                MathTex(r"\text{Variance } V = \dfrac{1}{N}\sum n_i x_i^2 - \bar{x}^2 \ (\text{Koenig}) \qquad \sigma=\sqrt{V}", font_size=18),
            ).arrange(DOWN, buff=0.22),
        )
        recap_dispersion.next_to(titre, DOWN, buff=0.35)

        with self.voiceover(
            text=(
                "Second bloc : les caractéristiques de dispersion. "
                "L'étendue est la différence entre maximum et minimum, "
                "l'écart interquartile est Q3 moins Q1. L'écart moyen e "
                "indice m est la moyenne des écarts absolus à la "
                "moyenne. Et la variance V, calculée le plus souvent "
                "par la formule de Koenig, est la moyenne des carrés "
                "moins le carré de la moyenne ; son écart-type sigma en "
                "est la racine carrée."
            )
        ) as tracker:
            self.play(FadeIn(recap_dispersion))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(recap_dispersion))

        # --- Méthodes ------------------------------------------------------------
        methode1 = method_box(
            VGroup(
                Text("Méthode 1 — Choisir les classes", font_size=20, weight="BOLD"),
                Text(
                    _wrap("Amplitude ÉGALE si possible, et 5 à 10 classes environ.", width=44),
                    font_size=18,
                ),
            ).arrange(DOWN, buff=0.2),
        )
        methode1.next_to(titre, DOWN, buff=0.35)

        with self.voiceover(
            text=(
                "Méthode 1 : pour regrouper une série en classes, on "
                "choisit si possible une amplitude égale pour toutes "
                "les classes, et un nombre de classes raisonnable, "
                "typiquement entre 5 et 10."
            )
        ) as tracker:
            self.play(FadeIn(methode1))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(methode1))

        methode2 = method_box(
            VGroup(
                Text("Méthode 2 — Calculer une médiane (4 étapes)", font_size=18, weight="BOLD"),
                Text(
                    _wrap(
                        "1. Calculer N/2. 2. Repérer la classe médiane "
                        "via l'ECC. 3. Appliquer l'interpolation. "
                        "4. Vérifier que M tombe dans l'intervalle.",
                        width=44,
                    ),
                    font_size=17,
                ),
            ).arrange(DOWN, buff=0.2),
        )
        methode2.next_to(titre, DOWN, buff=0.35)

        with self.voiceover(
            text=(
                "Méthode 2, déjà vue en détail à la scène 6 : calculer "
                "N sur 2, repérer la classe médiane grâce à l'effectif "
                "cumulé croissant, appliquer la formule d'interpolation, "
                "puis vérifier que le résultat tombe bien dans "
                "l'intervalle de cette classe."
            )
        ) as tracker:
            self.play(FadeIn(methode2))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(methode2))

        methode3 = method_box(
            VGroup(
                Text("Méthode 3 — Calculer une variance rapidement", font_size=17, weight="BOLD"),
                Text(
                    _wrap(
                        "Tableau à colonnes x_i / n_i / n_i x_i / n_i "
                        "x_i². Appliquer Koenig. TOUJOURS contrôler "
                        "V ≥ 0 en fin de calcul.",
                        width=44,
                    ),
                    font_size=17,
                ),
            ).arrange(DOWN, buff=0.2),
        )
        methode3.next_to(titre, DOWN, buff=0.35)

        with self.voiceover(
            text=(
                "Méthode 3, déjà vue à la scène 9 : construire un "
                "tableau à colonnes x indice i, n indice i, n indice i "
                "x indice i, et n indice i x indice i au carré, puis "
                "appliquer directement la formule de Koenig. Et "
                "toujours contrôler, à la fin, que la variance obtenue "
                "est positive ou nulle."
            )
        ) as tracker:
            self.play(FadeIn(methode3))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(methode3))

        methode4 = method_box(
            VGroup(
                Text("Méthode 4 — Comparer deux séries", font_size=20, weight="BOLD"),
                Text(
                    _wrap(
                        "D'abord comparer les MOYENNES (position), "
                        "puis les ÉCARTS-TYPES (dispersion) : une "
                        "moyenne plus élevée n'implique rien sur la "
                        "dispersion.",
                        width=44,
                    ),
                    font_size=17,
                ),
            ).arrange(DOWN, buff=0.2),
        )
        methode4.next_to(titre, DOWN, buff=0.35)

        with self.voiceover(
            text=(
                "Méthode 4 : pour comparer deux séries statistiques, on "
                "compare d'abord leurs moyennes, qui renseignent sur la "
                "position, puis leurs écarts-types, qui renseignent sur "
                "la dispersion. Une moyenne plus élevée n'implique "
                "absolument rien sur la dispersion : les deux "
                "comparaisons sont indépendantes et complémentaires."
            )
        ) as tracker:
            self.play(FadeIn(methode4))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(methode4))

        # --- Exemple traité : bilan des deux exemples du chapitre -----------------
        enonce = Text(
            _wrap(
                "Bilan chiffré de nos deux exemples fil rouge : les "
                "notes des 40 élèves, et les 60 sacs de cacao de Daloa.",
                width=52,
            ),
            font_size=21,
        )
        enonce.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Terminons par un bilan chiffré de nos deux exemples "
                "fil rouge : les notes des 40 élèves, et les 60 sacs de "
                "cacao pesés à Daloa."
            )
        ) as tracker:
            self.play(FadeIn(enonce))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(enonce))

        bilan = example_box(
            VGroup(
                Text("Exemple 1 — Notes (N=40)", font_size=19, weight="BOLD"),
                MathTex(r"\text{mode}=12,\ M=12,\ Q_1=10,\ Q_3=14,\ \bar{x}=11{,}875,\ e_m\approx 1{,}41", font_size=17),
                Text("Exemple 2 — Sacs de cacao (N=60)", font_size=19, weight="BOLD"),
                MathTex(r"\text{mode}=72{,}5\text{ kg},\ M\approx 73{,}3\text{ kg},\ \bar{x}=73{,}5\text{ kg},\ V=29,\ \sigma\approx 5{,}39\text{ kg}", font_size=17),
            ).arrange(DOWN, buff=0.2),
        )
        bilan.next_to(titre, DOWN, buff=0.35)

        with self.voiceover(
            text=(
                "Pour les notes : mode égale 12, médiane égale 12, Q1 "
                "égale 10, Q3 égale 14, moyenne égale 11,875, et écart "
                "moyen environ 1,41. Pour les sacs de cacao : mode "
                "égale 72,5 kilogrammes, médiane environ 73,3 "
                "kilogrammes, moyenne 73,5 kilogrammes, variance 29, et "
                "écart-type environ 5,39 kilogrammes."
            )
        ) as tracker:
            self.play(Write(bilan))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(bilan))

        # --- À retenir : l'essentiel du chapitre ------------------------------------
        essentiel = essentiel_box(
            VGroup(
                Text("L'essentiel du chapitre", font_size=22, weight="BOLD"),
                Text(
                    _wrap(
                        "Position (mode, médiane, quartiles, moyenne) "
                        "et dispersion (étendue, écart interquartile, "
                        "écart moyen, variance, écart-type) sont "
                        "TOUJOURS complémentaires pour décrire une "
                        "série : jamais l'une sans l'autre.",
                        width=48,
                    ),
                    font_size=19,
                ),
            ).arrange(DOWN, buff=0.25),
        )
        essentiel.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "L'essentiel à retenir de ce chapitre, et de cette "
                "dernière scène : les caractéristiques de position et "
                "les caractéristiques de dispersion sont toujours "
                "complémentaires pour décrire une série statistique. "
                "Donner une moyenne sans un écart-type, ou une médiane "
                "sans un écart interquartile, c'est ne raconter que la "
                "moitié de l'histoire."
            )
        ) as tracker:
            self.play(FadeIn(essentiel))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(essentiel))

        # --- Pièges à éviter (bilan) -----------------------------------------------
        pieges1 = warning_box(
            VGroup(
                Text("Pièges à éviter — bilan (1/2)", font_size=20, weight="BOLD"),
                Text(
                    _wrap(
                        "1. Histogramme à amplitudes inégales : ce sont "
                        "les AIRES qui sont proportionnelles aux "
                        "effectifs, pas les hauteurs (hauteur = "
                        "densité).",
                        width=46,
                    ),
                    font_size=18,
                ),
                Text(
                    _wrap(
                        "2. Ne pas confondre MÉDIANE (se lit sur les "
                        "effectifs CUMULÉS) et MOYENNE (utilise les "
                        "CENTRES de classe).",
                        width=46,
                    ),
                    font_size=18,
                ),
            ).arrange(DOWN, buff=0.2),
        )
        pieges1.next_to(titre, DOWN, buff=0.35)

        with self.voiceover(
            text=(
                "Rappelons, pour terminer, les pièges les plus "
                "fréquents de ce chapitre. Premièrement : dans un "
                "histogramme à amplitudes inégales, ce sont les aires "
                "qui sont proportionnelles aux effectifs, jamais les "
                "hauteurs seules. Deuxièmement : ne confondez jamais la "
                "médiane, qui se lit sur les effectifs cumulés, et la "
                "moyenne, qui utilise les centres de classe — ce sont "
                "deux calculs radicalement différents."
            )
        ) as tracker:
            self.play(FadeIn(pieges1))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(pieges1))

        pieges2 = warning_box(
            VGroup(
                Text("Pièges à éviter — bilan (2/2)", font_size=20, weight="BOLD"),
                Text(
                    _wrap(
                        "3. TOUJOURS trier une série discrète avant de "
                        "chercher médiane ou quartiles.",
                        width=46,
                    ),
                    font_size=18,
                ),
                Text(
                    _wrap(
                        "4. Utiliser des fréquences DÉCIMALES (0,25) "
                        "et non des pourcentages (25) dans les "
                        "formules — et vérifier que Σf_i = 1.",
                        width=46,
                    ),
                    font_size=18,
                ),
            ).arrange(DOWN, buff=0.2),
        )
        pieges2.next_to(titre, DOWN, buff=0.35)

        with self.voiceover(
            text=(
                "Troisièmement : trier toujours une série discrète "
                "avant de chercher la médiane ou les quartiles — "
                "travailler sur des données non triées donne "
                "systématiquement un résultat faux. Et quatrièmement : "
                "dans toute formule, utilisez des fréquences décimales, "
                "comme 0,25, et non des pourcentages, comme 25 — et "
                "vérifiez toujours que la somme des fréquences vaut "
                "exactement 1. Sur ces quatre réflexes, le chapitre, et "
                "l'année de première C, s'achèvent ici."
            )
        ) as tracker:
            self.play(FadeIn(pieges2))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(pieges2), FadeOut(titre))
