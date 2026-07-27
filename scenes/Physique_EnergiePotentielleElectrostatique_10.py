"""
scenes/Physique_EnergiePotentielleElectrostatique_10.py — Chapitre « Énergie
potentielle électrostatique » (1ereC, Physique), scène 10.

Synthèse du chapitre : tableau récapitulatif des grandeurs, méthodes
(calculer un travail dans un champ uniforme, exploiter E=U/d sans se
tromper, résoudre un problème d'accélération de particules) et pièges à
éviter (signe de la charge, U_AB vs U_BA, poids négligé sans justification,
conversions J↔eV).
Source : 1ereC/Physique.pdf, pages 66-75.
"""

import textwrap

from manim import DOWN, LEFT, RIGHT, UP, YELLOW, FadeIn, FadeOut, MathTex, Text, VGroup

from shapes.base_scene import NotionScene
from shapes.boxes import essentiel_box, method_box, scene_title, warning_box


def _wrap(text: str, width: int = 56) -> str:
    return "\n".join(textwrap.fill(line, width=width) for line in text.split("\n"))


class SyntheseTableauMethodesPieges(NotionScene):
    def construct(self):
        titre = scene_title("Synthèse : tableau, méthodes et pièges à éviter")
        titre.scale(0.46)
        titre.to_edge(UP)

        # --- Énoncé : objectif de la synthèse ------------------------------------------
        intro = Text(
            _wrap(
                "Terminons ce chapitre par un tableau récapitulatif des "
                "grandeurs, trois méthodes essentielles, puis les pièges "
                "les plus fréquents.",
                width=54,
            ),
            font_size=24,
        )
        intro.next_to(titre, DOWN, buff=0.7)

        with self.voiceover(
            text=(
                "Terminons ce chapitre sur l'énergie potentielle "
                "électrostatique par une synthèse complète : un tableau "
                "récapitulatif des grandeurs étudiées, trois méthodes "
                "essentielles à maîtriser, puis les pièges les plus "
                "fréquents à éviter."
            )
        ) as tracker:
            self.play(FadeIn(intro))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(intro))

        # --- Tableau récapitulatif des grandeurs ---------------------------------------
        tableau = VGroup(
            VGroup(Text("Potentiel", font_size=20), MathTex(r"V_M \; (\text{V})", font_size=24)).arrange(RIGHT, buff=0.3),
            VGroup(Text("Tension", font_size=20), MathTex(r"U_{AB}=V_A-V_B \; (\text{V})", font_size=24)).arrange(RIGHT, buff=0.3),
            VGroup(Text("Travail (champ uniforme)", font_size=20), MathTex(r"W=q\vec{E}\cdot\vec{AB}=qU_{AB} \; (\text{J})", font_size=22)).arrange(RIGHT, buff=0.3),
            VGroup(Text("Champ / tension (ligne de champ)", font_size=20), MathTex(r"E=U/d \; (\text{V/m})", font_size=24)).arrange(RIGHT, buff=0.3),
            VGroup(Text("Énergie potentielle", font_size=20), MathTex(r"E_p=qV \; (\text{J})", font_size=24)).arrange(RIGHT, buff=0.3),
            VGroup(Text("Énergie cinétique", font_size=20), MathTex(r"E_c=\tfrac{1}{2}mv^2 \; (\text{J})", font_size=24)).arrange(RIGHT, buff=0.3),
            VGroup(Text("Électronvolt", font_size=20), MathTex(r"1\ \text{eV}=1{,}6\times10^{-19}\ \text{J}", font_size=24)).arrange(RIGHT, buff=0.3),
        ).arrange(DOWN, buff=0.22, aligned_edge=LEFT)
        tableau.scale(0.85)
        tableau.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Voici les grandeurs à connaître par cœur : le potentiel V "
                "M en un point, en volts ; la tension U A B, égale à V A "
                "moins V B ; le travail de la force électrostatique dans "
                "un champ uniforme, q E fois AB, égal aussi à q U A B ; le "
                "champ E égal à U sur d le long d'une ligne de champ ; "
                "l'énergie potentielle électrostatique, q V ; l'énergie "
                "cinétique, un demi m v carré ; et enfin l'électronvolt, "
                "égal à 1 virgule 6 fois 10 puissance moins 19 joule."
            )
        ) as tracker:
            self.play(FadeIn(tableau))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(tableau))

        # --- Méthode 1 : calculer un travail dans un champ uniforme --------------------
        methode1 = method_box(
            VGroup(
                Text("Calculer un travail dans un champ uniforme :", font_size=21),
                MathTex(r"\text{Si } E,\, q,\, d \text{ connus : } W = qE\,d", font_size=25),
                MathTex(r"\text{Si } U_{AB} \text{ connue : } W = qU_{AB}", font_size=25),
                Text("Vérifier le signe (moteur/résistant) à la fin.", font_size=20),
            ).arrange(DOWN, buff=0.25),
            box_width=10.0,
        )
        methode1.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Première méthode : calculer un travail dans un champ "
                "uniforme. Deux formules équivalentes selon les données "
                "disponibles : q E d, si l'on connaît le champ, la charge "
                "et la distance parcourue le long du champ ; ou bien q U A "
                "B, si l'on connaît directement la tension. Dans tous les "
                "cas, on vérifie le signe obtenu à la fin, pour conclure "
                "sur le caractère moteur ou résistant du travail."
            )
        ) as tracker:
            self.play(FadeIn(methode1))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(methode1))

        # --- Méthode 2 : exploiter E=U/d --------------------------------------------------
        methode2 = method_box(
            VGroup(
                Text("Exploiter E=U/d sans se tromper :", font_size=21),
                Text("d est la distance le long d'une ligne de champ,", font_size=20),
                Text("PAS forcément la distance géométrique directe.", font_size=20),
                Text("Si le déplacement fait un angle avec E⃗, projeter", font_size=20),
                Text("d'abord le déplacement sur la direction du champ.", font_size=20),
            ).arrange(DOWN, buff=0.22),
            box_width=10.2,
        )
        methode2.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Deuxième méthode : exploiter la relation E égale U sur d "
                "sans se tromper. Le d de cette formule est la distance "
                "mesurée le long d'une ligne de champ, ce n'est pas "
                "forcément la distance géométrique directe entre deux "
                "points quelconques. Si le déplacement fait un angle avec "
                "le champ, il faut d'abord projeter ce déplacement sur la "
                "direction du champ avant d'appliquer la formule."
            )
        ) as tracker:
            self.play(FadeIn(methode2))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(methode2))

        # --- Méthode 3 : problèmes d'accélération de particules --------------------------
        methode3 = method_box(
            VGroup(
                Text("Problèmes d'accélération de particules :", font_size=21),
                Text("1. Identifier vitesse initiale (souvent nulle).", font_size=20),
                MathTex(r"2.\; \Delta E_c = |q|\,U \; \Rightarrow \; v = \sqrt{2|q|U/m}", font_size=25),
                Text("3. Convertir en eV si l'énoncé le demande.", font_size=20),
            ).arrange(DOWN, buff=0.25),
            box_width=10.2,
        )
        methode3.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Troisième méthode : résoudre un problème d'accélération "
                "de particules. On identifie d'abord la vitesse initiale, "
                "souvent nulle au départ de la cathode. On applique "
                "ensuite le théorème de l'énergie cinétique pour obtenir "
                "la vitesse finale, v égale racine carrée de 2 fois la "
                "valeur absolue de q fois U sur m. Enfin, on convertit si "
                "besoin l'énergie cinétique en électronvolts, si l'énoncé "
                "le demande."
            )
        ) as tracker:
            self.play(FadeIn(methode3))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(methode3))

        # --- Piège 1 : signe de la charge --------------------------------------------------
        piege1 = warning_box(
            Text(
                _wrap(
                    "Piège n°1 — Le signe de la charge inverse tout ! Une "
                    "charge négative se déplace spontanément vers les "
                    "potentiels CROISSANTS, contrairement à une charge "
                    "positive.",
                    width=54,
                ),
                font_size=22,
            ),
            box_width=11.0,
        )
        piege1.next_to(titre, DOWN, buff=0.6)

        with self.voiceover(
            text=(
                "Premier piège classique : le signe de la charge inverse "
                "tout le raisonnement. Une charge négative se déplace "
                "spontanément vers les potentiels croissants, exactement à "
                "l'inverse d'une charge positive, qui se déplace vers les "
                "potentiels décroissants."
            )
        ) as tracker:
            self.play(FadeIn(piege1))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(piege1))

        # --- Piège 2 : U_AB vs U_BA -------------------------------------------------------
        piege2 = warning_box(
            VGroup(
                Text("Piège n°2 — Ne pas confondre U_AB et U_BA :", font_size=22),
                MathTex(r"U_{BA} = -\,U_{AB}", font_size=27),
                Text(
                    "L'ordre des indices suit toujours le sens du déplacement.",
                    font_size=20,
                ),
            ).arrange(DOWN, buff=0.25),
            box_width=10.4,
        )
        piege2.next_to(titre, DOWN, buff=0.6)

        with self.voiceover(
            text=(
                "Deuxième piège : ne pas confondre U A B et U B A. U B A "
                "vaut moins U A B, jamais la même valeur. L'ordre des "
                "indices doit toujours suivre exactement le sens du "
                "déplacement considéré dans l'énoncé."
            )
        ) as tracker:
            self.play(FadeIn(piege2))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(piege2))

        # --- Piège 3 : poids négligé sans justification -----------------------------------
        piege3 = warning_box(
            Text(
                _wrap(
                    "Piège n°3 — Ne jamais négliger le poids par simple "
                    "habitude : il faut comparer numériquement |q|E (ou "
                    "|q|U/d) à mg pour justifier l'approximation.",
                    width=54,
                ),
                font_size=22,
            ),
            box_width=11.0,
        )
        piege3.next_to(titre, DOWN, buff=0.6)

        with self.voiceover(
            text=(
                "Troisième piège : ne jamais négliger le poids par simple "
                "habitude. Il faut comparer numériquement la force "
                "électrostatique, valeur absolue de q fois E, à la force "
                "de pesanteur m g, pour justifier réellement "
                "l'approximation avant de l'utiliser."
            )
        ) as tracker:
            self.play(FadeIn(piege3))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(piege3))

        # --- Piège 4 : conversions J↔eV -----------------------------------------------------
        piege4 = warning_box(
            Text(
                _wrap(
                    "Piège n°4 — Conversions J↔eV : diviser par "
                    "1,6×10⁻¹⁹ pour passer de joules à électronvolts, "
                    "multiplier pour l'inverse. Une erreur de sens change "
                    "le résultat de 19 ordres de grandeur !",
                    width=54,
                ),
                font_size=21,
            ),
            box_width=11.2,
        )
        piege4.next_to(titre, DOWN, buff=0.6)

        with self.voiceover(
            text=(
                "Quatrième et dernier piège : les conversions entre "
                "joules et électronvolts. On divise par 1 virgule 6 fois "
                "10 puissance moins 19 pour passer des joules aux "
                "électronvolts, et l'on multiplie pour l'opération "
                "inverse. Une erreur de sens dans cette conversion change "
                "le résultat de dix-neuf ordres de grandeur, une erreur "
                "évidemment fatale."
            )
        ) as tracker:
            self.play(FadeIn(piege4))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(piege4))

        # --- À retenir : synthèse finale --------------------------------------------------
        retenir = essentiel_box(
            Text(
                _wrap(
                    "Chapitre « Énergie potentielle électrostatique » : "
                    "Ep=qV, W_A→B(F⃗)=qU_AB=qE⃗·AB⃗, Em=½mv²+qV se conserve. "
                    "Toujours vérifier le signe de la charge et l'ordre "
                    "des indices de U.",
                    width=56,
                ),
                font_size=21,
            )
        )
        retenir.next_to(titre, DOWN, buff=0.6)

        with self.voiceover(
            text=(
                "Pour conclure ce chapitre : l'énergie potentielle "
                "électrostatique vaut q V, le travail de la force "
                "électrostatique dans un champ uniforme vaut q U A B, "
                "égal aussi à q E fois AB, et l'énergie mécanique, somme "
                "de l'énergie cinétique et de q V, se conserve. Retenez "
                "surtout ce réflexe : toujours vérifier le signe de la "
                "charge, et l'ordre des indices de la tension U, avant de "
                "conclure un calcul."
            )
        ) as tracker:
            self.play(FadeIn(retenir))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(titre), FadeOut(retenir))
