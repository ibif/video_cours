"""
scenes/Maths_StatistiqueUneVariable_02.py — Chapitre 17 « Statistique à une
variable » (1ereC, Maths), scène 02.

§ Effectifs, fréquences, effectifs/fréquences cumulés : définitions
effectif n_i, fréquence f_i=n_i/N (en %). Propriété Σn_i=N, Σf_i=1.
Définitions effectif cumulé croissant (ECC) / décroissant (ECD). Exemple
résolu 1 complet : notes sur 20 de 40 élèves (7 modalités : 8,9,10,11,12,
13,14 ; effectifs 2,1,8,3,12,3,11), tableau complet avec fréquences et
cumulés croissant/décroissant, diagramme en bâtons, interprétation
(« 26 élèves ont une note ≤ 12 »).
Source : 1ereC/Maths.pdf, chapitre 17, pages 201-202.
"""

import textwrap

from manim import DOWN, UP, WHITE, YELLOW, Axes, FadeIn, FadeOut, Line, MathTex, Table, Text, VGroup, Write

from shapes.base_scene import NotionScene
from shapes.boxes import definition_box, example_box, property_box, scene_title, warning_box

# --- Données de l'exemple résolu 1 (notes /20 de 40 élèves) -----------------
NOTES = [8, 9, 10, 11, 12, 13, 14]
EFFECTIFS = [2, 1, 8, 3, 12, 3, 11]
N_TOTAL = 40  # = sum(EFFECTIFS)
FREQUENCES_POURCENT = ["5", "2,5", "20", "7,5", "30", "7,5", "27,5"]
ECC = [2, 3, 11, 14, 26, 29, 40]
ECD = [40, 38, 37, 29, 26, 14, 11]


def _wrap(text: str, width: int = 54) -> str:
    return "\n".join(textwrap.fill(line, width=width) for line in text.split("\n"))


def _tableau_notes() -> Table:
    valeurs = [
        [str(n) for n in EFFECTIFS],
        [f + "\\%" for f in FREQUENCES_POURCENT],
        [str(e) for e in ECC],
        [str(e) for e in ECD],
    ]
    table = Table(
        valeurs,
        row_labels=[
            MathTex(r"n_i", font_size=20),
            MathTex(r"f_i", font_size=20),
            MathTex(r"\text{ECC}", font_size=18),
            MathTex(r"\text{ECD}", font_size=18),
        ],
        col_labels=[MathTex(str(x), font_size=20) for x in NOTES],
        top_left_entry=MathTex(r"x_i", font_size=20),
        element_to_mobject=MathTex,
        element_to_mobject_config={"font_size": 18},
        line_config={"color": WHITE, "stroke_width": 1},
        include_outer_lines=True,
        v_buff=0.2,
        h_buff=0.25,
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


def _diagramme_batons() -> VGroup:
    """Diagramme en bâtons des effectifs n_i pour les 7 notes."""
    axes = Axes(
        x_range=[7, 15, 1],
        y_range=[0, 14, 2],
        x_length=8,
        y_length=3.2,
        axis_config={"color": WHITE, "include_tip": False, "font_size": 16},
    )
    batons = VGroup()
    for x, n in zip(NOTES, EFFECTIFS):
        base = axes.c2p(x, 0)
        sommet = axes.c2p(x, n)
        barre = Line(base, sommet, color=YELLOW, stroke_width=8)
        label_x = MathTex(str(x), font_size=18).next_to(base, DOWN, buff=0.12)
        label_n = MathTex(str(n), font_size=16).next_to(sommet, UP, buff=0.08)
        batons.add(barre, label_x, label_n)
    return VGroup(axes, batons)


class EffectifsFrequencesCumules(NotionScene):
    def construct(self):
        titre = scene_title("Statistique — Effectifs, fréquences, cumuls")
        titre.scale(0.48)
        titre.to_edge(UP)

        # --- Énoncé : mise en situation --------------------------------------
        mise_en_situation = Text(
            _wrap(
                "Une fois les données recueillies, il faut les organiser "
                "dans un tableau : combien d'individus pour chaque "
                "modalité, et quelle proportion cela représente-t-il ?",
                width=56,
            ),
            font_size=24,
        )
        mise_en_situation.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Une fois les données recueillies, il faut les organiser "
                "dans un tableau statistique : combien d'individus pour "
                "chaque modalité, et quelle proportion cela "
                "représente-t-il dans la population totale ?"
            )
        ) as tracker:
            self.play(Write(titre))
            self.play(FadeIn(mise_en_situation))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(mise_en_situation))

        # --- Raisonnement : effectif, fréquence -------------------------------
        def_effectif = definition_box(
            VGroup(
                Text("Effectif et fréquence", font_size=23, weight="BOLD"),
                MathTex(r"n_i = \text{effectif de la modalité } x_i \ (\text{nombre d'individus concernés})", font_size=21),
                MathTex(r"f_i = \dfrac{n_i}{N} \quad (\text{souvent exprimée en \%})", font_size=23),
            ).arrange(DOWN, buff=0.25),
        )
        def_effectif.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "L'effectif n indice i d'une modalité x indice i est le "
                "nombre d'individus qui présentent cette modalité. La "
                "fréquence f indice i est le rapport de cet effectif à "
                "l'effectif total N, souvent exprimée en pourcentage."
            )
        ) as tracker:
            self.play(FadeIn(def_effectif))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(def_effectif))

        prop_sommes = property_box(
            VGroup(
                Text("Propriété — Sommes", font_size=22, weight="BOLD"),
                MathTex(r"\sum_i n_i = N \qquad \sum_i f_i = 1", font_size=26),
            ).arrange(DOWN, buff=0.25),
        )
        prop_sommes.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Deux propriétés indispensables à vérifier à chaque "
                "tableau : la somme de tous les effectifs redonne "
                "l'effectif total N, et la somme de toutes les "
                "fréquences vaut toujours 1, c'est-à-dire 100 pour cent."
            )
        ) as tracker:
            self.play(Write(prop_sommes))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(prop_sommes))

        def_cumules = definition_box(
            VGroup(
                Text("Effectifs cumulés croissant / décroissant", font_size=21, weight="BOLD"),
                Text(
                    _wrap(
                        "ECC(x_i) = nombre d'individus dont la modalité "
                        "est INFÉRIEURE OU ÉGALE à x_i.",
                        width=46,
                    ),
                    font_size=20,
                ),
                Text(
                    _wrap(
                        "ECD(x_i) = nombre d'individus dont la modalité "
                        "est SUPÉRIEURE OU ÉGALE à x_i.",
                        width=46,
                    ),
                    font_size=20,
                ),
            ).arrange(DOWN, buff=0.22),
        )
        def_cumules.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "L'effectif cumulé croissant d'une modalité x indice i "
                "est le nombre d'individus dont la modalité est "
                "inférieure ou égale à x indice i. Symétriquement, "
                "l'effectif cumulé décroissant compte les individus dont "
                "la modalité est supérieure ou égale à x indice i. On "
                "définit de la même façon les fréquences cumulées, en "
                "divisant simplement par N."
            )
        ) as tracker:
            self.play(FadeIn(def_cumules))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(def_cumules))

        # --- Exemple résolu 1 : notes sur 20 de 40 élèves --------------------
        enonce = Text(
            _wrap(
                "Exemple résolu 1 : on relève les notes sur 20, en "
                "mathématiques, de N=40 élèves d'une classe de 1ère C. "
                "Sept notes distinctes apparaissent : 8, 9, 10, 11, 12, "
                "13 et 14.",
                width=52,
            ),
            font_size=21,
        )
        enonce.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Exemple résolu numéro 1. On relève les notes sur 20, en "
                "mathématiques, de 40 élèves d'une classe de première C. "
                "Sept notes distinctes apparaissent : 8, 9, 10, 11, 12, "
                "13 et 14."
            )
        ) as tracker:
            self.play(FadeIn(enonce))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(enonce))

        tableau = _tableau_notes()
        tableau.scale(0.62)
        tableau.next_to(titre, DOWN, buff=0.35)

        with self.voiceover(
            text=(
                "Voici le tableau complet : en première ligne les "
                "effectifs, puis les fréquences en pourcentage, puis "
                "l'effectif cumulé croissant, et enfin l'effectif cumulé "
                "décroissant. On vérifie que la somme des effectifs vaut "
                "bien 40, et que la dernière colonne de l'effectif cumulé "
                "croissant atteint elle aussi 40."
            )
        ) as tracker:
            self.play(FadeIn(tableau))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(tableau))

        diagramme = _diagramme_batons()
        diagramme.scale(0.85)
        diagramme.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Ces effectifs se représentent naturellement par un "
                "diagramme en bâtons : en abscisse les notes, en "
                "ordonnée les effectifs, un bâton de hauteur "
                "proportionnelle pour chaque modalité."
            )
        ) as tracker:
            self.play(Write(diagramme))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(diagramme))

        interpretation = MathTex(
            r"\text{ECC}(12) = 26 \quad\Rightarrow\quad \text{26 élèves ont une note} \le 12",
            font_size=27,
            color=YELLOW,
        )
        interpretation.next_to(titre, DOWN, buff=0.6)

        with self.voiceover(
            text=(
                "Lisons l'effectif cumulé croissant à la modalité 12 : "
                "il vaut 26. Cela signifie que 26 élèves sur 40 ont "
                "obtenu une note inférieure ou égale à 12."
            )
        ) as tracker:
            self.play(Write(interpretation))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(interpretation))

        # --- À retenir ----------------------------------------------------------
        recap = example_box(
            VGroup(
                Text("À retenir", font_size=22, weight="BOLD"),
                MathTex(r"\text{ECC croît de } 0 \text{ à } N \ ; \quad \text{ECD décroît de } N \text{ à } n_{\text{dernier}}", font_size=21),
            ).arrange(DOWN, buff=0.25),
        )
        recap.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Retenons la logique des cumuls : l'effectif cumulé "
                "croissant part de 0 pour atteindre N à la dernière "
                "modalité, tandis que l'effectif cumulé décroissant part "
                "de N et se termine à l'effectif de la dernière "
                "modalité."
            )
        ) as tracker:
            self.play(FadeIn(recap))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(recap))

        # --- Piège à éviter -----------------------------------------------------
        piege = warning_box(
            VGroup(
                Text("Piège — Pourcentage ou fréquence décimale ?", font_size=19, weight="BOLD"),
                Text(
                    _wrap(
                        "f_i = n_i / N est un nombre DÉCIMAL (entre 0 et "
                        "1). On le multiplie par 100 seulement pour "
                        "L'AFFICHER en pourcentage — ne jamais mélanger "
                        "les deux formes dans un calcul.",
                        width=46,
                    ),
                    font_size=18,
                ),
            ).arrange(DOWN, buff=0.2),
        )
        piege.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Un piège classique dès cette première scène : la "
                "fréquence f indice i, définie comme n indice i divisé "
                "par N, est un nombre décimal compris entre 0 et 1. On "
                "la multiplie par 100 uniquement pour l'afficher sous "
                "forme de pourcentage. Ne mélangez jamais les deux "
                "formes dans un même calcul : ce piège reviendra "
                "notamment pour la moyenne et la variance."
            )
        ) as tracker:
            self.play(FadeIn(piege))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(piege), FadeOut(titre))
