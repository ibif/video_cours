"""
scenes/Maths_SuitesNumeriques_12.py — Chapitre 15 « Suites numériques »
(1ereC, Maths), scène 12.

Résolution de problèmes contextualisés (partie 1) : démarche en 3 étapes.
Exemple résolu 12 (épargne, modèle arithmétique, Moussa) et exemple résolu
13 (croissance de bactéries, modèle géométrique).
Source : 1ereC/Maths.pdf, chapitre 15, pages 176-188.
"""

import textwrap

from manim import DOWN, UP, FadeIn, FadeOut, MathTex, Text, VGroup, Write, YELLOW

from shapes.base_scene import NotionScene
from shapes.boxes import essentiel_box, example_box, method_box, scene_title, warning_box


def _wrap(text: str, width: int = 58) -> str:
    return "\n".join(textwrap.fill(line, width=width) for line in text.split("\n"))


class ProblemesContextualisesPartie1(NotionScene):
    def construct(self):
        titre = scene_title("Problèmes contextualisés — épargne et bactéries")
        titre.scale(0.46)
        titre.to_edge(UP)
        self.play(Write(titre))

        # --- Énoncé : démarche en 3 étapes ------------------------------------------
        methode = method_box(
            VGroup(
                Text("Démarche en 3 étapes pour un problème contextualisé :", font_size=22, weight="BOLD"),
                Text("1) Choisir l'indice n (souvent : nombre de mois, d'années...)", font_size=20),
                Text(
                    "2) Traduire l'évolution : ajout d'une quantité constante →\n"
                    "   suite arithmétique ; multiplication par un facteur constant →\n"
                    "   suite géométrique ; les deux à la fois → arithmético-géométrique.",
                    font_size=20,
                ),
                Text("3) Exploiter les formules du terme général et de la somme.", font_size=20),
            ).arrange(DOWN, buff=0.2),
            box_width=11.6,
        )
        methode.next_to(titre, DOWN, buff=0.35)

        with self.voiceover(
            text=(
                "Face à un problème contextualisé, on suit toujours la "
                "même démarche en trois étapes. D'abord, choisir "
                "clairement l'indice n, souvent un nombre de mois ou "
                "d'années. Ensuite, traduire l'énoncé : un ajout d'une "
                "quantité constante signale une suite arithmétique, une "
                "multiplication par un facteur constant signale une suite "
                "géométrique, et la présence des deux à la fois signale "
                "une suite arithmético-géométrique. Enfin, exploiter les "
                "formules du terme général et, si besoin, de la somme."
            )
        ) as tracker:
            self.play(FadeIn(methode))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(methode))

        # --- Exemple résolu 12 : épargne (arithmétique) ----------------------------
        ex12_titre = Text(
            "Exemple 12 — Épargne de Moussa (modèle arithmétique) :",
            font_size=22,
            color=YELLOW,
            weight="BOLD",
        )
        ex12_titre.next_to(titre, DOWN, buff=0.35)
        ex12_enonce = Text(
            "Moussa épargne 20 000 F, puis ajoute 5 000 F chaque mois.",
            font_size=21,
        )
        ex12_enonce.next_to(ex12_titre, DOWN, buff=0.25)
        ex12_calc = example_box(
            VGroup(
                MathTex(
                    r"u_0 = 20\,000, \quad r = 5\,000 \Longrightarrow u_n = 20\,000+5\,000\,n",
                    font_size=23,
                ),
                MathTex(
                    r"u_n>100\,000 \Longleftrightarrow 5\,000n>80\,000 \Longleftrightarrow n>16 \Longrightarrow n=17",
                    font_size=21,
                ),
                Text(
                    "Moussa dépasse 100 000 F au bout de 17 mois.",
                    font_size=21,
                    weight="BOLD",
                ),
            ).arrange(DOWN, buff=0.25),
            box_width=11.4,
        )
        ex12_calc.next_to(ex12_enonce, DOWN, buff=0.25)

        with self.voiceover(
            text=(
                "Exemple : Moussa commence avec vingt mille francs "
                "d'épargne, puis ajoute cinq mille francs chaque mois. "
                "L'ajout est constant : c'est une suite arithmétique, de "
                "premier terme vingt mille et de raison cinq mille. Son "
                "terme général est u indice n égale vingt mille plus cinq "
                "mille n. On cherche à partir de quel mois il dépasse cent "
                "mille francs : cinq mille n supérieur à quatre-vingt "
                "mille, soit n supérieur à seize, donc n égale dix-sept. "
                "Moussa dépasse cent mille francs au bout de dix-sept "
                "mois."
            )
        ) as tracker:
            self.play(FadeIn(ex12_titre))
            self.play(FadeIn(ex12_enonce))
            self.play(FadeIn(ex12_calc))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(ex12_titre), FadeOut(ex12_enonce), FadeOut(ex12_calc))

        # --- Exemple résolu 13 : bactéries (géométrique) ----------------------------
        ex13_titre = Text(
            "Exemple 13 — Croissance de bactéries (modèle géométrique) :",
            font_size=21,
            color=YELLOW,
            weight="BOLD",
        )
        ex13_titre.next_to(titre, DOWN, buff=0.35)
        ex13_enonce = Text(
            "Une culture démarre à 1 000 bactéries, doublant chaque heure.",
            font_size=21,
        )
        ex13_enonce.next_to(ex13_titre, DOWN, buff=0.25)
        ex13_calc = example_box(
            VGroup(
                MathTex(
                    r"b_0 = 1\,000, \quad q = 2 \Longrightarrow b_n = 1\,000\times 2^n",
                    font_size=23,
                ),
                MathTex(
                    r"b_{10} = 1\,000\times 1024 = 1\,024\,000",
                    font_size=23,
                ),
                MathTex(
                    r"b_n>500\,000 \Longleftrightarrow 2^n>500 \Longleftrightarrow n\geq 9 \ (2^9=512)",
                    font_size=21,
                ),
                Text(
                    "La culture dépasse 500 000 bactéries au bout de 9 heures.",
                    font_size=20,
                    weight="BOLD",
                ),
            ).arrange(DOWN, buff=0.22),
            box_width=11.6,
        )
        ex13_calc.next_to(ex13_enonce, DOWN, buff=0.25)

        with self.voiceover(
            text=(
                "Autre exemple : une culture de bactéries démarre à mille "
                "individus, et double chaque heure. La multiplication est "
                "constante : c'est une suite géométrique, de premier terme "
                "mille et de raison deux. Son terme général est b indice n "
                "égale mille fois deux puissance n. Au bout de dix heures, "
                "on trouve un million vingt-quatre mille bactéries. On "
                "cherche à partir de quelle heure la culture dépasse cinq "
                "cent mille bactéries : deux puissance n supérieur à cinq "
                "cents, soit n supérieur ou égal à neuf. La culture "
                "dépasse cinq cent mille bactéries au bout de neuf heures."
            )
        ) as tracker:
            self.play(FadeIn(ex13_titre))
            self.play(FadeIn(ex13_enonce))
            self.play(FadeIn(ex13_calc))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(ex13_titre), FadeOut(ex13_enonce), FadeOut(ex13_calc))

        # --- À retenir -----------------------------------------------------------
        retenir = essentiel_box(
            Text(
                _wrap(
                    "Ajout constant à chaque étape → suite arithmétique. "
                    "Multiplication par un facteur constant → suite "
                    "géométrique. Traduire l'énoncé en formule de "
                    "récurrence AVANT de calculer.",
                    width=58,
                ),
                font_size=22,
            ),
            box_width=11.3,
        )
        retenir.next_to(titre, DOWN, buff=0.35)

        with self.voiceover(
            text=(
                "À retenir : un ajout constant à chaque étape se modélise "
                "toujours par une suite arithmétique, une multiplication "
                "par un facteur constant toujours par une suite "
                "géométrique. Il faut systématiquement traduire l'énoncé "
                "en une relation de récurrence, avant de se lancer dans "
                "les calculs."
            )
        ) as tracker:
            self.play(FadeIn(retenir))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(retenir))

        # --- Piège à éviter ----------------------------------------------------
        piege = warning_box(
            Text(
                _wrap(
                    "Piège : bien identifier si l'indice n de l'énoncé "
                    "démarre à 0 ou à 1, et vérifier que le rang trouvé "
                    "correspond bien à la question posée (« au bout de "
                    "combien de mois » compte-t-il le mois 0 ?).",
                    width=56,
                ),
                font_size=21,
            ),
            box_width=11.3,
        )
        piege.next_to(titre, DOWN, buff=0.35)

        with self.voiceover(
            text=(
                "Piège à éviter : dans un problème contextualisé, il faut "
                "bien identifier si l'indice n démarre à zéro ou à un, et "
                "vérifier que le rang trouvé correspond exactement à la "
                "question posée — au bout de combien de mois, compte-t-on "
                "le mois zéro comme le premier mois écoulé, ou non ?"
            )
        ) as tracker:
            self.play(FadeIn(piege))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(piege), FadeOut(titre))
