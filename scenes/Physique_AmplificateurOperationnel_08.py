"""
scenes/Physique_AmplificateurOperationnel_08.py — Chapitre « L'amplificateur
opérationnel » (1ereC, Physique), scène 08.

§ 8. Conditions de linéarité : réaction négative ET |Us| < Vsat. Si le Us
calculé par les formules de gain dépasse Vsat en valeur absolue, l'AO est
en réalité saturé : Us réel = ±Vsat. Exemple résolu 4 : montage inverseur
R1 = 1 kΩ, R2 = 20 kΩ, Vsat = 12 V, Ue = 1 V → calcul « linéaire » donne
-20 V, or |-20| > 12 donc Us réel = -12 V. Tableau récapitulatif des 4
montages (suiveur, inverseur, non inverseur, comparateur) : gain et
propriété remarquable.
Source : 1ereC/Physique.pdf, pages 99-107 (§ 8).
"""

import textwrap

from manim import (
    DOWN,
    LEFT,
    ORANGE,
    RIGHT,
    UP,
    WHITE,
    YELLOW,
    FadeIn,
    FadeOut,
    Line,
    MathTex,
    Text,
    VGroup,
    Write,
)

from shapes.base_scene import NotionScene
from shapes.boxes import corrige_box, essentiel_box, example_box, property_box, scene_title, warning_box


def _wrap(text: str, width: int = 56) -> str:
    return "\n".join(textwrap.fill(line, width=width) for line in text.split("\n"))


def _tableau_recapitulatif():
    """Tableau récapitulatif des 4 montages, construit avec des Text/MathTex
    alignés en colonnes et des lignes de séparation (Line), sans étirer de
    SurroundingRectangle — uniquement des Line pour les séparateurs."""
    en_tetes = ["Montage", "Gain Av", "Propriété remarquable"]
    lignes = [
        ["Suiveur", "1", "Adaptation d'impédance (i+=0)"],
        ["Inverseur", "−R2/R1", "Masse virtuelle en E− (V−=0)"],
        ["Non inverseur", "1+R2/R1", "Toujours Av ≥ 1, pas d'inversion"],
        ["Comparateur", "—", "Pas de réaction négative → saturé"],
    ]

    col_x = [-4.2, -1.6, 2.2]
    lignes_txt = VGroup()

    ligne_entetes = VGroup(
        *[Text(t, font_size=19, color=YELLOW, weight="BOLD") for t in en_tetes]
    )
    for txt, x in zip(ligne_entetes, col_x):
        txt.move_to([x, 1.6, 0])
    lignes_txt.add(ligne_entetes)

    y = 1.05
    for row in lignes:
        for texte, x in zip(row, col_x):
            t = Text(texte, font_size=18)
            t.move_to([x, y, 0])
            lignes_txt.add(t)
        y -= 0.55

    separateur_haut = Line([-5.2, 1.3, 0], [4.2, 1.3, 0], stroke_width=2, color=WHITE)
    separateur_bas = Line([-5.2, y + 0.28, 0], [4.2, y + 0.28, 0], stroke_width=2, color=WHITE)

    return VGroup(lignes_txt, separateur_haut, separateur_bas)


class ConditionsLineariteRecapitulatif(NotionScene):
    def construct(self):
        titre = scene_title("Conditions de linéarité et récapitulatif")
        titre.scale(0.42)
        titre.to_edge(UP)

        # --- Énoncé -------------------------------------------------------
        mise_en_situation = Text(
            _wrap(
                "Les formules de gain établies pour le suiveur, l'inverseur "
                "et le non inverseur ne sont pas valables à tout coup : "
                "elles supposent une condition précise. Laquelle ?",
                width=58,
            ),
            font_size=22,
        )
        mise_en_situation.next_to(titre, DOWN, buff=0.35)

        with self.voiceover(
            text=(
                "Les formules de gain établies pour le suiveur, "
                "l'inverseur et le non inverseur ne sont pas valables à "
                "tout coup : elles supposent une condition précise. "
                "Laquelle ?"
            )
        ) as tracker:
            self.play(Write(titre))
            self.play(FadeIn(mise_en_situation))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(mise_en_situation))

        # --- Raisonnement : condition de linéarité -----------------------------
        condition = property_box(
            VGroup(
                Text("Condition de linéarité (pour utiliser ε = 0) :", font_size=20),
                Text("il faut une réaction négative ET |Us| < Vsat.", font_size=20, color=YELLOW),
                Text("Si le Us calculé dépasse Vsat en valeur absolue,", font_size=20),
                Text("l'AO est en réalité SATURÉ : Us réel = ±Vsat.", font_size=20),
            ).arrange(DOWN, aligned_edge=LEFT, buff=0.2),
            box_width=11.4,
        )
        condition.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "La condition de linéarité comporte deux exigences : il "
                "faut une réaction négative, ET la tension de sortie "
                "calculée doit rester inférieure à Vsat en valeur "
                "absolue. Si le Us obtenu par la formule de gain dépasse "
                "Vsat, cela signifie que l'AO est en réalité saturé, et "
                "la vraie sortie vaut alors plus ou moins Vsat, pas la "
                "valeur calculée."
            )
        ) as tracker:
            self.play(FadeIn(condition))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(condition))

        # --- Exemple résolu 4 ---------------------------------------------------
        enonce_ex = example_box(
            VGroup(
                Text("Montage inverseur : R1 = 1 kΩ, R2 = 20 kΩ,", font_size=20),
                Text("Vsat = 12 V, Ue = 1 V. Que vaut Us réellement ?", font_size=20),
            ).arrange(DOWN, aligned_edge=LEFT, buff=0.2),
            box_width=10.0,
        )
        enonce_ex.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Exemple résolu. On étudie un montage inverseur avec R1 "
                "égal 1 kilo-ohm, R2 égal 20 kilo-ohms, Vsat égal 12 "
                "volts, et Ue égal 1 volt. Que vaut réellement Us ?"
            )
        ) as tracker:
            self.play(FadeIn(enonce_ex))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(enonce_ex))

        corrige = corrige_box(
            VGroup(
                MathTex(r"U_s^{\text{calc}} = -\dfrac{R_2}{R_1} U_e = -\dfrac{20}{1}\times 1 = -20\ \text{V}", font_size=24),
                Text("Or |−20| = 20 V > Vsat = 12 V  →  l'AO est SATURÉ.", font_size=20),
                MathTex(r"U_s^{\text{réel}} = -V_{sat} = -12\ \text{V}", font_size=26, color=YELLOW),
            ).arrange(DOWN, buff=0.22),
            box_width=11.0,
        )
        corrige.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Corrigé. La formule du régime linéaire donnerait Us égal "
                "moins R2 sur R1 fois Ue, soit moins 20 fois 1, "
                "c'est-à-dire moins 20 volts. Mais 20 est supérieur à "
                "Vsat, qui vaut 12 volts : ce résultat est physiquement "
                "impossible, l'AO est en réalité saturé. La sortie réelle "
                "vaut donc moins Vsat, soit moins 12 volts."
            )
        ) as tracker:
            self.play(FadeIn(corrige))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(corrige))

        # --- Tableau récapitulatif ----------------------------------------------
        tableau_titre = Text("Tableau récapitulatif des 4 montages", font_size=22, weight="BOLD")
        tableau_titre.next_to(titre, DOWN, buff=0.4)
        tableau = _tableau_recapitulatif()
        tableau.scale(0.85)
        tableau.next_to(tableau_titre, DOWN, buff=0.35)

        with self.voiceover(
            text=(
                "Récapitulons les quatre montages étudiés. Le suiveur a "
                "un gain de 1 et sert à l'adaptation d'impédance. "
                "L'inverseur a un gain de moins R2 sur R1, avec une masse "
                "virtuelle en E moins. Le non inverseur a un gain de 1 "
                "plus R2 sur R1, toujours supérieur ou égal à 1, sans "
                "inversion. Le comparateur, lui, n'a pas de gain "
                "linéaire : sans réaction négative, il fonctionne "
                "toujours en saturation."
            )
        ) as tracker:
            self.play(FadeIn(tableau_titre))
            self.play(FadeIn(tableau))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(tableau_titre), FadeOut(tableau))

        # --- À retenir --------------------------------------------------------
        retenir = essentiel_box(
            VGroup(
                Text("À retenir", font_size=24, weight="BOLD"),
                Text("Linéarité = réaction négative ET |Us| < Vsat.", font_size=20),
                Text("Si |Us calculé| > Vsat  →  Us réel = ±Vsat (saturé).", font_size=20),
            ).arrange(DOWN, buff=0.2),
            box_width=11.6,
        )
        retenir.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Retenons l'essentiel. La linéarité exige une réaction "
                "négative et une tension de sortie inférieure à Vsat. Si "
                "le Us calculé dépasse Vsat, la sortie réelle vaut plus "
                "ou moins Vsat : l'AO est saturé."
            )
        ) as tracker:
            self.play(FadeIn(retenir))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(retenir))

        # --- Pièges à éviter --------------------------------------------------
        pieges = warning_box(
            VGroup(
                Text("• Piège majeur : oublier de vérifier la saturation", font_size=19),
                Text("   après TOUT calcul de Us par une formule de gain.", font_size=19),
                Text("   Un Us calculé irréaliste (> Vsat) doit alerter.", font_size=19),
                Text("• La formule Av = −R2/R1 (ou 1+R2/R1) ne donne QUE", font_size=19),
                Text("   le Us théorique en régime linéaire, pas le Us réel.", font_size=19),
            ).arrange(DOWN, aligned_edge=LEFT, buff=0.15),
            box_width=12.0,
        )
        pieges.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Le piège majeur de cette leçon : oublier de vérifier la "
                "saturation après tout calcul de Us par une formule de "
                "gain. Un Us calculé irréaliste, supérieur à Vsat, doit "
                "immédiatement vous alerter : la formule de gain ne donne "
                "que le Us théorique du régime linéaire, jamais "
                "automatiquement le Us réel."
            )
        ) as tracker:
            self.play(FadeIn(pieges))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(pieges), FadeOut(titre))
