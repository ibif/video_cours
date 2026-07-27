"""
scenes/Physique_EnergiePotentielleElectrostatique_09.py — Chapitre « Énergie
potentielle électrostatique » (1ereC, Physique), scène 09.

Applications : condensateur plan (rappel : champ uniforme, équipotentielles,
potentiel décroissant linéairement) et accélération de particules
(principe du canon à électrons) : ½mv²=|q|U → v=√(2|q|U/m). Exemple résolu
complet : électron accéléré sous U=500 V dans un oscillographe →
Ec=500 eV=8×10⁻¹⁷ J, v≈1,33×10⁷ m/s (≈4% de la vitesse de la lumière).
Source : 1ereC/Physique.pdf, pages 66-75.
"""

import textwrap

from manim import (
    BLUE,
    DOWN,
    LEFT,
    RED,
    RIGHT,
    UP,
    WHITE,
    YELLOW,
    Arrow,
    Dot,
    FadeIn,
    FadeOut,
    MathTex,
    Rectangle,
    Text,
    VGroup,
    Write,
)

from shapes.base_scene import NotionScene
from shapes.boxes import essentiel_box, example_box, method_box, scene_title


def _wrap(text: str, width: int = 56) -> str:
    return "\n".join(textwrap.fill(line, width=width) for line in text.split("\n"))


def _canon_electrons(sep: float = 5.0, hauteur: float = 1.8):
    """Cathode (-) émettant un électron, accéléré vers l'anode (+) percée
    d'un trou par lequel il ressort."""
    cathode = Rectangle(width=0.16, height=hauteur, color=BLUE, fill_color=BLUE, fill_opacity=1.0)
    anode = Rectangle(width=0.16, height=hauteur, color=RED, fill_color=RED, fill_opacity=1.0)
    cathode.move_to(LEFT * sep / 2)
    anode.move_to(RIGHT * sep / 2)
    trou = Rectangle(width=0.2, height=0.22, color=WHITE, fill_color=WHITE, fill_opacity=1.0)
    trou.move_to(anode.get_center())
    label_cathode = Text("cathode (−)", font_size=16, color=BLUE).next_to(cathode, DOWN, buff=0.15)
    label_anode = Text("anode (+)", font_size=16, color=RED).next_to(anode, DOWN, buff=0.15)
    electron = Dot(cathode.get_center() + RIGHT * 0.2, color=YELLOW, radius=0.09)
    return VGroup(cathode, anode, trou, label_cathode, label_anode), electron


class ApplicationsCondensateurAccelerateur(NotionScene):
    def construct(self):
        titre = scene_title("Applications : condensateur et accélérateur")
        titre.scale(0.48)
        titre.to_edge(UP)

        # --- Énoncé : rappel condensateur plan --------------------------------------------
        rappel = method_box(
            VGroup(
                Text("Condensateur plan : rappel", font_size=23),
                Text("• Champ électrostatique uniforme entre les plaques.", font_size=20),
                Text("• Équipotentielles : plans parallèles aux plaques.", font_size=20),
                Text("• Le potentiel décroît linéairement le long du champ.", font_size=20),
            ).arrange(DOWN, buff=0.22, aligned_edge=LEFT),
            box_width=10.4,
        )
        rappel.next_to(titre, DOWN, buff=0.6)

        with self.voiceover(
            text=(
                "Récapitulons d'abord ce que nous savons du condensateur "
                "plan. Entre ses deux armatures règne un champ "
                "électrostatique uniforme. Les équipotentielles y sont des "
                "plans parallèles aux plaques, et le potentiel décroît "
                "linéairement le long des lignes de champ, de la plaque "
                "positive vers la plaque négative."
            )
        ) as tracker:
            self.play(FadeIn(rappel))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(rappel))

        # --- Raisonnement : principe de l'accélérateur électrostatique --------------------
        question = Text(
            _wrap(
                "Cette accélération d'une charge entre deux plaques a une "
                "application directe : le canon à électrons, ou "
                "accélérateur électrostatique.",
                width=52,
            ),
            font_size=23,
        )
        question.next_to(titre, DOWN, buff=0.7)

        with self.voiceover(
            text=(
                "Cette propriété d'accélération d'une charge entre deux "
                "plaques a une application directe et très concrète : le "
                "canon à électrons, aussi appelé accélérateur "
                "électrostatique, présent dans de nombreux appareils comme "
                "l'oscillographe."
            )
        ) as tracker:
            self.play(Write(question))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(question))

        schema, electron = _canon_electrons()
        schema.next_to(titre, DOWN, buff=0.6)
        electron.move_to(schema[0].get_center() + LEFT * 2.3)

        vitesse_finale = Arrow(
            schema[1].get_right() + RIGHT * 0.15,
            schema[1].get_right() + RIGHT * 1.1,
            color=YELLOW,
            buff=0,
            stroke_width=3,
        )
        label_v = MathTex("v", font_size=24, color=YELLOW).next_to(vitesse_finale, UP, buff=0.1)

        with self.voiceover(
            text=(
                "Une particule chargée, ici un électron, est libérée à "
                "proximité de la cathode, quasiment au repos. Sous "
                "l'effet de la tension U appliquée entre la cathode et "
                "l'anode, elle est fortement accélérée, et ressort par un "
                "petit trou percé dans l'anode avec une vitesse v."
            )
        ) as tracker:
            self.play(FadeIn(schema), FadeIn(electron))
            self.play(electron.animate.move_to(schema[1].get_center()), run_time=1.6)
            self.play(FadeOut(electron), FadeIn(vitesse_finale), Write(label_v))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(schema), FadeOut(vitesse_finale), FadeOut(label_v))

        theoreme = method_box(
            VGroup(
                Text("Théorème de l'énergie cinétique, vitesse initiale nulle :", font_size=21),
                MathTex(r"\dfrac{1}{2}mv^2 = |q|\,U \; \Rightarrow \; v = \sqrt{\dfrac{2|q|U}{m}}", font_size=28),
                Text("L'énergie cinétique gagnée, en eV, se lit directement :", font_size=20),
                Text("une charge élémentaire sous 1 kV gagne 1 keV.", font_size=20),
            ).arrange(DOWN, buff=0.25),
            box_width=10.8,
        )
        theoreme.next_to(titre, DOWN, buff=0.6)

        with self.voiceover(
            text=(
                "En appliquant le théorème de l'énergie cinétique, avec "
                "une vitesse initiale nulle à la cathode, un demi m v "
                "carré est égal à la valeur absolue de q, fois U, d'où la "
                "vitesse finale v, égale à la racine carrée de 2 fois la "
                "valeur absolue de q, fois U, le tout divisé par m. Autre "
                "avantage pratique de l'électronvolt : l'énergie cinétique "
                "gagnée se lit directement — une charge élémentaire "
                "accélérée sous 1 kilovolt gagne exactement 1 "
                "kiloélectronvolt."
            )
        ) as tracker:
            self.play(FadeIn(theoreme))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(theoreme))

        # --- Exemple résolu 5 : électron dans un oscillographe ----------------------------
        enonce = Text(
            _wrap(
                "Exemple : dans un oscillographe, un électron initialement "
                "au repos est accéléré sous U=500 V. Calculer son énergie "
                "cinétique puis sa vitesse finale.",
                width=54,
            ),
            font_size=21,
        )
        enonce.next_to(titre, DOWN, buff=0.7)

        with self.voiceover(
            text=(
                "Exemple complet. Dans un oscillographe, un électron, "
                "initialement au repos, est accéléré sous une tension de "
                "500 volts. Calculons son énergie cinétique à la sortie, "
                "puis sa vitesse finale. On donne la masse de l'électron : "
                "9 virgule 11 fois 10 puissance moins 31 kilogramme."
            )
        ) as tracker:
            self.play(Write(enonce))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(enonce))

        calcul1 = example_box(
            VGroup(
                MathTex(r"E_c = |q|\,U = e\times U = 500\ \text{eV}", font_size=27),
                MathTex(r"E_c = 500\times1{,}6\times10^{-19} = 8\times10^{-17}\ \text{J}", font_size=25),
            ).arrange(DOWN, buff=0.3),
            box_width=9.6,
        )
        calcul1.next_to(titre, DOWN, buff=0.6)

        with self.voiceover(
            text=(
                "L'énergie cinétique acquise vaut la valeur absolue de q "
                "fois U, soit, pour la charge élémentaire, exactement 500 "
                "électronvolts. En joules, cela donne 500 fois 1 virgule 6 "
                "fois 10 puissance moins 19, soit 8 fois 10 puissance moins "
                "17 joule."
            )
        ) as tracker:
            self.play(FadeIn(calcul1))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(calcul1))

        calcul2 = example_box(
            VGroup(
                MathTex(
                    r"v = \sqrt{\dfrac{2E_c}{m}} = \sqrt{\dfrac{2\times8\times10^{-17}}{9{,}11\times10^{-31}}}",
                    font_size=23,
                ),
                MathTex(r"v \approx 1{,}33\times10^{7}\ \text{m/s} \; (\approx 4\%\; \text{de } c)", font_size=27, color=YELLOW),
            ).arrange(DOWN, buff=0.32),
            box_width=10.8,
        )
        calcul2.next_to(titre, DOWN, buff=0.6)

        with self.voiceover(
            text=(
                "La vitesse finale vaut la racine carrée de 2 Ec sur m, "
                "soit environ 1 virgule 33 fois 10 puissance 7 mètres par "
                "seconde. C'est une vitesse considérable : environ 4 pour "
                "cent de la vitesse de la lumière, ce qui montre à quel "
                "point une tension de quelques centaines de volts suffit à "
                "accélérer fortement une particule aussi légère qu'un "
                "électron."
            )
        ) as tracker:
            self.play(FadeIn(calcul2))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(calcul2))

        # --- À retenir ------------------------------------------------------------------
        retenir = essentiel_box(
            Text(
                _wrap(
                    "Canon à électrons : ½mv²=|q|U (départ au repos), "
                    "v=√(2|q|U/m). L'électronvolt donne l'énergie "
                    "cinétique directement : charge élémentaire sous 1 kV "
                    "→ 1 keV.",
                    width=56,
                ),
                font_size=21,
            )
        )
        retenir.next_to(titre, DOWN, buff=0.6)

        with self.voiceover(
            text=(
                "À retenir : dans un accélérateur électrostatique, une "
                "particule partant du repos acquiert une énergie cinétique "
                "égale à la valeur absolue de sa charge fois la tension "
                "accélératrice, soit une vitesse finale égale à la racine "
                "carrée de 2 fois la valeur absolue de q fois U sur m. "
                "L'électronvolt donne directement cette énergie cinétique : "
                "une charge élémentaire accélérée sous 1 kilovolt gagne "
                "1 kiloélectronvolt."
            )
        ) as tracker:
            self.play(FadeIn(retenir))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(titre), FadeOut(retenir))
