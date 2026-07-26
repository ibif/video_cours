"""
scenes/SVT_MouvementsPlaques_05.py — Chapitre 7 (1ereD, SVT), scène 05.

§ 7.2.3 L'âge des fonds océaniques et la vitesse d'expansion : propriété
de l'âge nul à l'axe, méthode de calcul d'une vitesse d'expansion,
exemple chiffré (100 km / 10 Ma -> 1 cm/an), attention aux conversions
d'unités. Source : 1ereD/SVT.pdf, page 94.
"""

import textwrap

from manim import (
    BLUE_D,
    BLUE_E,
    DOWN,
    LEFT,
    RED,
    RIGHT,
    UP,
    WHITE,
    YELLOW,
    Arrow,
    FadeIn,
    FadeOut,
    MathTex,
    Rectangle,
    Text,
    VGroup,
    Write,
)

from shapes.base_scene import NotionScene
from shapes.boxes import example_box, method_box, property_box, scene_title, warning_box


def _wrap(text: str, width: int = 56) -> str:
    return "\n".join(textwrap.fill(line, width=width) for line in text.split("\n"))


def _bullets(items, font_size=22, color=WHITE, width=52):
    lines = VGroup(
        *[Text(f"• {_wrap(it, width=width)}", font_size=font_size, color=color) for it in items]
    )
    lines.arrange(DOWN, aligned_edge=LEFT, buff=0.25)
    return lines


def _schema_ages():
    """Bandes d'âge du plancher océanique, croissant symétriquement depuis l'axe."""
    largeurs = [0.35, 0.5, 0.7, 0.9]
    couleurs = [RED, "#E8963C", "#D8C23C", BLUE_D]
    ages = ["0", "10 Ma", "50 Ma", "150 Ma"]

    demi_droit = VGroup()
    x = 0.0
    for larg, coul in zip(largeurs, couleurs):
        rect = Rectangle(width=larg, height=1.0, fill_color=coul, fill_opacity=0.85, stroke_color=WHITE, stroke_width=0.5)
        rect.move_to([x + larg / 2, 0, 0])
        demi_droit.add(rect)
        x += larg

    demi_gauche = demi_droit.copy()
    demi_gauche.rotate(3.14159265, axis=[0, 1, 0])  # miroir horizontal

    bandes = VGroup(demi_gauche, demi_droit)

    labels = VGroup()
    x = 0.0
    for larg, age in zip(largeurs, ages):
        centre = x + larg / 2
        lbl = Text(age, font_size=13, color=WHITE)
        lbl.move_to([centre, 0.75, 0])
        lbl2 = lbl.copy().move_to([-centre, 0.75, 0])
        labels.add(lbl, lbl2)
        x += larg

    return VGroup(bandes, labels)


class AgeFondsOceaniquesVitesse(NotionScene):
    def construct(self):
        titre = scene_title("7.2.3 — Âge des fonds et vitesse d'expansion")
        titre.scale(0.6)
        titre.to_edge(UP)

        # --- Énoncé : propriété de l'âge des fonds océaniques ------------------
        propriete_age = property_box(
            Text(
                _wrap(
                    "La datation des basaltes confirme le paléomagnétisme : "
                    "l'âge est nul à l'axe et croît symétriquement en "
                    "s'éloignant. Aucun fond océanique n'est plus ancien "
                    "qu'environ 200 Ma (la Terre a 4,6 Ga, certains "
                    "continents plus de 3 Ga) : la lithosphère océanique est "
                    "sans cesse renouvelée.",
                    width=54,
                ),
                font_size=21,
            ),
            box_width=11.8,
        )
        propriete_age.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Troisième preuve, la plus directe : l'âge des fonds "
                "océaniques. La datation des basaltes confirme ce que "
                "montrait le paléomagnétisme : l'âge de la roche est nul à "
                "l'axe de la dorsale, et croît symétriquement à mesure que "
                "l'on s'en éloigne. Fait remarquable : aucun fond océanique "
                "n'est plus ancien qu'environ deux cents millions "
                "d'années, alors que la Terre a quatre virgule six "
                "milliards d'années, et que certains continents dépassent "
                "trois milliards d'années. La lithosphère océanique est "
                "donc sans cesse renouvelée."
            )
        ) as tracker:
            self.play(Write(titre))
            self.play(FadeIn(propriete_age))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(propriete_age))

        schema = _schema_ages()
        schema.next_to(titre, DOWN, buff=0.7)
        label_axe = Text("axe (âge 0)", font_size=15, color=YELLOW)
        label_axe.next_to(schema, DOWN, buff=0.3)

        with self.voiceover(
            text=(
                "Voici l'idée en image : depuis l'axe de la dorsale, l'âge "
                "des roches augmente régulièrement et symétriquement vers "
                "les deux flancs, dix millions d'années, puis cinquante, "
                "puis cent cinquante millions d'années en s'éloignant "
                "encore. C'est exactement ce que prédit l'expansion "
                "océanique."
            )
        ) as tracker:
            self.play(FadeIn(schema), FadeIn(label_axe))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(schema), FadeOut(label_axe))

        # --- Animation du raisonnement : méthode de calcul ---------------------
        etapes = method_box(
            _bullets(
                [
                    "Étape 1 : repérer la distance d du basalte étudié à l'axe.",
                    "Étape 2 : noter l'âge t de ce basalte.",
                    "Étape 3 : appliquer v=d/t (convertir km en cm, Ma en années).",
                    "Étape 4 : multiplier par 2 pour la vitesse totale "
                    "d'écartement (les deux flancs s'écartent symétriquement).",
                ],
                font_size=20,
                width=52,
            ),
            box_width=12.0,
        )
        etapes.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Cet âge permet même de calculer une vitesse d'expansion "
                "océanique, en quatre étapes. Étape un : repérer la "
                "distance d du basalte étudié par rapport à l'axe de la "
                "dorsale. Étape deux : noter l'âge t de ce même basalte. "
                "Étape trois : appliquer la formule v égale d sur t, en "
                "convertissant bien les kilomètres en centimètres, et les "
                "millions d'années en années. Étape quatre : multiplier le "
                "résultat par deux, pour obtenir la vitesse totale "
                "d'écartement, puisque les deux flancs s'écartent "
                "symétriquement."
            )
        ) as tracker:
            self.play(FadeIn(etapes))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(etapes))

        # --- Exemple traité : calcul chiffré -----------------------------------
        enonce_exemple = Text(
            _wrap(
                "Un basalte prélevé à 100 km de l'axe de la dorsale "
                "médio-atlantique date de 10 Ma. Calculons la vitesse "
                "d'écartement entre l'Afrique et l'Amérique du Sud.",
                width=54,
            ),
            font_size=23,
            color=WHITE,
        )
        enonce_exemple.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Appliquons cette méthode. Un basalte prélevé à cent "
                "kilomètres de l'axe de la dorsale médio-atlantique date de "
                "dix millions d'années. Quelle est la vitesse d'écartement "
                "entre l'Afrique et l'Amérique du Sud ?"
            )
        ) as tracker:
            self.play(FadeIn(enonce_exemple))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(enonce_exemple))

        calcul1 = MathTex(r"d = 100\ \text{km} = 100 \times 10^{5}\ \text{cm} = 10^{7}\ \text{cm}", font_size=32, color=WHITE)
        calcul2 = MathTex(r"t = 10\ \text{Ma} = 10 \times 10^{6}\ \text{ans} = 10^{7}\ \text{ans}", font_size=32, color=WHITE)
        calcul3 = MathTex(r"v = \dfrac{d}{t} = \dfrac{10^{7}\ \text{cm}}{10^{7}\ \text{ans}} = 1\ \text{cm/an}", font_size=32, color=WHITE)
        calcul4 = MathTex(r"v_{\text{totale}} = 2 \times 1 = 2\ \text{cm/an}", font_size=34, color=YELLOW)
        calculs = VGroup(calcul1, calcul2, calcul3, calcul4).arrange(DOWN, buff=0.35, aligned_edge=LEFT)
        calculs.next_to(titre, DOWN, buff=0.6)

        with self.voiceover(
            text=(
                "Étape un : d égale cent kilomètres, soit cent fois dix "
                "puissance cinq centimètres, soit dix puissance sept "
                "centimètres. Étape deux : t égale dix millions d'années, "
                "soit dix fois dix puissance six ans, soit dix puissance "
                "sept ans. Étape trois : v égale d sur t, soit dix "
                "puissance sept centimètres sur dix puissance sept ans, "
                "soit un centimètre par an. Étape quatre : la vitesse "
                "totale d'écartement entre l'Afrique et l'Amérique du Sud "
                "vaut deux fois un, soit deux centimètres par an."
            )
        ) as tracker:
            self.play(Write(calcul1))
            self.play(Write(calcul2))
            self.play(Write(calcul3))
            self.play(Write(calcul4))
            self.wait(tracker.get_remaining_duration())

        exemple_recap = example_box(
            Text(
                _wrap(
                    "d=100 km=10^7 cm ; t=10 Ma=10^7 ans ; "
                    "v=d/t=1 cm/an ; vitesse totale d'écartement "
                    "Afrique / Amérique du Sud = 2×1 = 2 cm/an.",
                    width=52,
                ),
                font_size=20,
            ),
            box_width=11.5,
        )

        self.play(FadeOut(calculs))
        exemple_recap.next_to(titre, DOWN, buff=0.5)
        self.play(FadeIn(exemple_recap))
        self.wait(1.5)
        self.play(FadeOut(exemple_recap))

        # --- À retenir / piège : les conversions --------------------------------
        piege_conv = warning_box(
            Text(
                _wrap(
                    "1 km=10^5 cm et 1 Ma=10^6 ans, donc "
                    "1 km/Ma = 10^5 cm / 10^6 ans = 0,1 cm/an = 1 mm/an. "
                    "Toujours écrire la conversion avant le calcul, jamais "
                    "de tête.",
                    width=54,
                ),
                font_size=22,
            ),
            box_width=11.8,
        )
        piege_conv.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Piège numéro un de ce chapitre : les conversions "
                "d'unités. Rappelez-vous que un kilomètre égale dix "
                "puissance cinq centimètres, et qu'un million d'années "
                "égale dix puissance six ans. Donc un kilomètre par million "
                "d'années égale dix puissance cinq centimètres sur dix "
                "puissance six ans, soit zéro virgule un centimètre par "
                "an, soit un millimètre par an. Écrivez toujours la "
                "conversion complète avant de calculer, jamais de tête : "
                "c'est la source d'erreur numéro un de ce chapitre."
            )
        ) as tracker:
            self.play(FadeIn(piege_conv))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(titre), FadeOut(piege_conv))
