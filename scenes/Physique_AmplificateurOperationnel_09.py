"""
scenes/Physique_AmplificateurOperationnel_09.py — Chapitre « L'amplificateur
opérationnel » (1ereC, Physique), scène 09.

§ 9. Synthèse : applications (adaptation d'impédance, amplification de
signaux faibles, comparaison de seuil, traitement du signal). Méthode
pour résoudre un exercice sur un montage linéaire (5 étapes). Méthode
pour étudier un comparateur (4 étapes). Pièges à éviter récapitulés :
inverser R1/R2 dans le gain inverseur, utiliser ε = 0 dans un
comparateur, oublier de vérifier la saturation, astuce masse virtuelle,
astuce choix des résistances (entre 1 kΩ et 100 kΩ).
Source : 1ereC/Physique.pdf, pages 99-107 (§ 9, synthèse du chapitre).
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
    MathTex,
    Text,
    VGroup,
    Write,
)

from shapes.base_scene import NotionScene
from shapes.boxes import corrige_box, essentiel_box, example_box, method_box, scene_title, warning_box


def _wrap(text: str, width: int = 56) -> str:
    return "\n".join(textwrap.fill(line, width=width) for line in text.split("\n"))


class SyntheseApplicationsMethodesPieges(NotionScene):
    def construct(self):
        titre = scene_title("Synthèse : applications, méthodes, pièges")
        titre.scale(0.42)
        titre.to_edge(UP)

        # --- Énoncé : applications ---------------------------------------------
        applications = Text(
            _wrap(
                "Voltmètre électronique, table de mixage audio, thermostat, "
                "amplificateur de microphone : tous ces appareils "
                "exploitent l'un des montages à AO étudiés dans ce "
                "chapitre.",
                width=58,
            ),
            font_size=22,
        )
        applications.next_to(titre, DOWN, buff=0.35)

        with self.voiceover(
            text=(
                "Voltmètre électronique, table de mixage audio, "
                "thermostat, amplificateur de microphone : tous ces "
                "appareils exploitent l'un des montages à amplificateur "
                "opérationnel étudiés dans ce chapitre. Faisons la "
                "synthèse."
            )
        ) as tracker:
            self.play(Write(titre))
            self.play(FadeIn(applications))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(applications))

        applications_box = example_box(
            VGroup(
                Text("Adaptation d'impédance : suiveur (voltmètre électronique)", font_size=18),
                Text("Amplification de signaux faibles : inverseur / non inverseur", font_size=18),
                Text("Comparaison de seuil : comparateur (thermostat, éclairage)", font_size=18),
                Text("Traitement du signal : sommateur (mélangeur audio)", font_size=18),
            ).arrange(DOWN, aligned_edge=LEFT, buff=0.16),
            box_width=11.6,
        )
        applications_box.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Quatre grandes familles d'applications. L'adaptation "
                "d'impédance, avec le montage suiveur, comme dans un "
                "voltmètre électronique. L'amplification de signaux "
                "faibles, avec l'inverseur ou le non inverseur. La "
                "comparaison de seuil, avec le comparateur, dans un "
                "thermostat ou une commande d'éclairage. Et le traitement "
                "du signal, avec le sommateur, dans un mélangeur audio."
            )
        ) as tracker:
            self.play(FadeIn(applications_box))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(applications_box))

        # --- Raisonnement : méthode montage linéaire ----------------------------
        methode_lineaire = method_box(
            VGroup(
                Text("Méthode : résoudre un exercice sur un montage linéaire", font_size=19, weight="BOLD"),
                Text("1. Identifier le montage (suiveur, inverseur, non inv.).", font_size=18),
                Text("2. Vérifier la réaction négative (S relié à E−).", font_size=18),
                Text("3. Poser ε = 0 et i+ = i− = 0.", font_size=18),
                Text("4. Appliquer la formule de gain correspondante.", font_size=18),
                Text("5. Vérifier que |Us| < Vsat (sinon, AO saturé).", font_size=18),
            ).arrange(DOWN, aligned_edge=LEFT, buff=0.14),
            box_width=11.4,
        )
        methode_lineaire.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Pour résoudre un exercice sur un montage linéaire, cinq "
                "étapes. Un : identifier le montage, suiveur, inverseur "
                "ou non inverseur. Deux : vérifier la présence d'une "
                "réaction négative. Trois : poser epsilon égal zéro et i "
                "plus égal i moins égal zéro. Quatre : appliquer la "
                "formule de gain correspondante. Cinq : vérifier que Us "
                "reste inférieure à Vsat, sinon l'AO est saturé."
            )
        ) as tracker:
            self.play(FadeIn(methode_lineaire))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(methode_lineaire))

        # --- Raisonnement : méthode comparateur ---------------------------------
        methode_comparateur = method_box(
            VGroup(
                Text("Méthode : étudier un comparateur", font_size=19, weight="BOLD"),
                Text("1. Vérifier l'absence de réaction négative.", font_size=18),
                Text("2. Identifier Ue (sur E+) et Uref (sur E−).", font_size=18),
                Text("3. Comparer Ue et Uref à chaque instant.", font_size=18),
                Text("4. Conclure : Vs = +Vsat si Ue>Uref, −Vsat sinon.", font_size=18),
            ).arrange(DOWN, aligned_edge=LEFT, buff=0.16),
            box_width=11.0,
        )
        methode_comparateur.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Pour étudier un comparateur, quatre étapes. Un : "
                "vérifier l'absence de réaction négative. Deux : "
                "identifier quelle tension est sur E plus, et laquelle "
                "est sur E moins. Trois : comparer ces deux tensions à "
                "chaque instant. Quatre : conclure que Vs vaut plus Vsat "
                "si Ue est supérieure à Uref, et moins Vsat sinon."
            )
        ) as tracker:
            self.play(FadeIn(methode_comparateur))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(methode_comparateur))

        # --- Exemple traité : application des deux méthodes ---------------------
        enonce_ex = example_box(
            VGroup(
                Text("Montage inverseur, R1 = 1 kΩ. On veut Av = −8, avec", font_size=19),
                Text("Vsat = 15 V et Ue = 2 V. Quelle R2 choisir ? Est-ce", font_size=19),
                Text("valide (pas de saturation) ?", font_size=19),
            ).arrange(DOWN, aligned_edge=LEFT, buff=0.18),
            box_width=10.6,
        )
        enonce_ex.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Exemple traité, en appliquant la méthode. On étudie un "
                "montage inverseur avec R1 égal 1 kilo-ohm. On veut un "
                "gain Av de moins 8, avec Vsat égal 15 volts et Ue égal 2 "
                "volts. Quelle résistance R2 choisir, et ce choix est-il "
                "valide, c'est-à-dire sans saturation ?"
            )
        ) as tracker:
            self.play(FadeIn(enonce_ex))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(enonce_ex))

        corrige = corrige_box(
            VGroup(
                MathTex(r"A_v = -\dfrac{R_2}{R_1} = -8 \Rightarrow R_2 = 8 \times R_1 = 8\ \text{k}\Omega", font_size=23),
                MathTex(r"U_s = A_v \cdot U_e = -8 \times 2 = -16\ \text{V}", font_size=23),
                Text("|−16| = 16 V > Vsat = 15 V  →  AO saturé, invalide !", font_size=19, color=YELLOW),
                Text("Il faut réduire Ue ou revoir R2 pour rester linéaire.", font_size=18),
            ).arrange(DOWN, buff=0.2),
            box_width=11.4,
        )
        corrige.next_to(titre, DOWN, buff=0.45)

        with self.voiceover(
            text=(
                "Corrigé. Pour obtenir Av égal moins 8 avec R1 égal 1 "
                "kilo-ohm, il faut R2 égal 8 kilo-ohms, dans la fourchette "
                "usuelle entre 1 et 100 kilo-ohms. Mais avec Ue égal 2 "
                "volts, Us calculé vaut moins 16 volts, ce qui dépasse "
                "Vsat en valeur absolue : ce choix n'est pas valide, l'AO "
                "serait saturé. Étape 5 de la méthode : il faudrait "
                "réduire Ue, ou revoir R2, pour rester en régime "
                "linéaire."
            )
        ) as tracker:
            self.play(FadeIn(corrige))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(corrige))

        # --- À retenir --------------------------------------------------------
        retenir = essentiel_box(
            VGroup(
                Text("À retenir", font_size=24, weight="BOLD"),
                Text("4 montages : suiveur, inverseur, non inverseur,", font_size=20),
                Text("comparateur — chacun avec sa méthode dédiée.", font_size=20),
                Text("Toujours vérifier |Us| < Vsat avant de conclure.", font_size=20),
            ).arrange(DOWN, buff=0.2),
            box_width=11.8,
        )
        retenir.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Retenons l'essentiel du chapitre. Quatre montages à "
                "connaître : le suiveur, l'inverseur, le non inverseur, "
                "et le comparateur, chacun avec sa méthode dédiée. Et "
                "dans tous les cas, toujours vérifier que Us reste "
                "inférieure à Vsat en valeur absolue avant de conclure."
            )
        ) as tracker:
            self.play(FadeIn(retenir))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(retenir))

        # --- Pièges à éviter (récapitulatif du chapitre) ------------------------
        pieges = warning_box(
            VGroup(
                Text("• Inverser R1 et R2 : R2 est toujours le résistor de", font_size=18),
                Text("   réaction (relié à la sortie).", font_size=18),
                Text("• Utiliser ε = 0 dans un comparateur : faux, ε ≠ 0", font_size=18),
                Text("   en régime saturé.", font_size=18),
                Text("• Oublier de vérifier la saturation après un calcul", font_size=18),
                Text("   de Us par une formule de gain.", font_size=18),
                Text("• Astuce masse virtuelle : si E+ est à la masse,", font_size=18),
                Text("   alors V− = 0 (utile pour l'inverseur).", font_size=18),
                Text("• Astuce choix des résistances : rester entre 1 kΩ", font_size=18),
                Text("   et 100 kΩ pour un montage réaliste.", font_size=18),
            ).arrange(DOWN, aligned_edge=LEFT, buff=0.1),
            box_width=12.0,
        )
        pieges.next_to(titre, DOWN, buff=0.35)

        with self.voiceover(
            text=(
                "Récapitulons les pièges du chapitre. Premièrement, "
                "inverser R1 et R2 : R2 est toujours le résistor de "
                "réaction, relié à la sortie. Deuxièmement, utiliser "
                "epsilon égal zéro dans un comparateur : c'est faux, "
                "epsilon n'est jamais nul en régime saturé. "
                "Troisièmement, oublier de vérifier la saturation après "
                "un calcul de Us. Une astuce utile : si E plus est à la "
                "masse, alors V moins est nul, c'est la masse virtuelle "
                "de l'inverseur. Enfin, pour un montage réaliste, choisir "
                "des résistances comprises entre 1 kilo-ohm et 100 "
                "kilo-ohms."
            )
        ) as tracker:
            self.play(FadeIn(pieges))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(pieges), FadeOut(titre))
