"""
scenes/Physique_AmplificateurOperationnel_03.py — Chapitre « L'amplificateur
opérationnel » (1ereC, Physique), scène 03.

§ 3. Le comparateur : montage et fonctionnement. Schéma sans liaison
sortie → E- (pas de réaction négative), Uref appliquée sur E-, Ue sur E+.
Propriété : Ue > Uref → Vs = +Vsat ; Ue < Uref → Vs = -Vsat.
Exemple résolu 1 : Uref = 3 V, Vsat = 14 V — Ue = 5 V → Vs = +14 V ;
Ue = 1 V → Vs = -14 V.
Source : 1ereC/Physique.pdf, pages 99-107 (§ 3).
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
    Polygon,
    Text,
    VGroup,
    Write,
)

from shapes.base_scene import NotionScene
from shapes.boxes import corrige_box, essentiel_box, example_box, property_box, scene_title, warning_box


def _wrap(text: str, width: int = 56) -> str:
    return "\n".join(textwrap.fill(line, width=width) for line in text.split("\n"))


def _ao_symbole(width=2.4, height=1.6):
    haut = UP * height / 2 + LEFT * width / 2
    bas = DOWN * height / 2 + LEFT * width / 2
    pointe = RIGHT * width / 2
    triangle = Polygon(haut, bas, pointe, color=WHITE, stroke_width=3)
    plus = Text("+", font_size=22, color=WHITE).move_to(haut + RIGHT * 0.35 + DOWN * 0.05)
    moins = Text("−", font_size=22, color=WHITE).move_to(bas + RIGHT * 0.35 + UP * 0.05)
    return VGroup(triangle, plus, moins), haut, bas, pointe


def _schema_comparateur():
    """Comparateur : Uref sur E- (broche du bas), Ue sur E+ (broche du
    haut), sortie S libre — AUCUNE liaison de réaction entre S et E-."""
    symbole, haut, bas, pointe = _ao_symbole()

    fil_e_plus = Line(haut + LEFT * 0.9, haut, stroke_width=3, color=WHITE)
    fil_e_moins = Line(bas + LEFT * 0.9, bas, stroke_width=3, color=WHITE)
    fil_s = Line(pointe, pointe + RIGHT * 0.9, stroke_width=3, color=WHITE)

    label_ue = Text("Ue", font_size=20, color=YELLOW).next_to(fil_e_plus, LEFT, buff=0.1)
    label_uref = Text("Uref", font_size=20, color=YELLOW).next_to(fil_e_moins, LEFT, buff=0.1)
    label_vs = Text("Vs", font_size=20, color=ORANGE).next_to(fil_s, RIGHT, buff=0.1)

    return VGroup(symbole, fil_e_plus, fil_e_moins, fil_s, label_ue, label_uref, label_vs)


class MontageComparateur(NotionScene):
    def construct(self):
        titre = scene_title("Le comparateur : montage et fonctionnement")
        titre.scale(0.42)
        titre.to_edge(UP)

        # --- Énoncé -------------------------------------------------------
        mise_en_situation = Text(
            _wrap(
                "Un thermostat qui déclenche un chauffage dès qu'une "
                "tension dépasse un seuil : c'est le rôle typique du "
                "montage comparateur, le plus simple des montages à AO. "
                "Comment fonctionne-t-il ?",
                width=58,
            ),
            font_size=22,
        )
        mise_en_situation.next_to(titre, DOWN, buff=0.35)

        with self.voiceover(
            text=(
                "Un thermostat qui déclenche un chauffage dès qu'une "
                "tension dépasse un seuil : c'est le rôle typique du "
                "montage comparateur, le plus simple des montages à "
                "amplificateur opérationnel. Comment fonctionne-t-il ?"
            )
        ) as tracker:
            self.play(Write(titre))
            self.play(FadeIn(mise_en_situation))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(mise_en_situation))

        # --- Raisonnement : schéma + propriété -------------------------------
        schema = _schema_comparateur()
        schema.scale(1.1)
        schema.next_to(titre, DOWN, buff=0.6).shift(LEFT * 2.6)

        propriete = property_box(
            VGroup(
                Text("Aucune liaison entre S et E− : pas de réaction", font_size=19),
                Text("négative → l'AO fonctionne toujours en saturé.", font_size=19),
                MathTex(r"U_e > U_{ref} \Rightarrow V_s = +V_{sat}", font_size=26),
                MathTex(r"U_e < U_{ref} \Rightarrow V_s = -V_{sat}", font_size=26),
            ).arrange(DOWN, aligned_edge=LEFT, buff=0.2),
            box_width=9.4,
        )
        propriete.next_to(schema, RIGHT, buff=0.5)

        with self.voiceover(
            text=(
                "Dans ce montage, la tension à comparer Ue est appliquée "
                "sur l'entrée E plus, et la tension de référence Uref sur "
                "l'entrée E moins. Aucun fil ne relie la sortie à E moins "
                ": il n'y a donc pas de réaction négative, et l'AO "
                "fonctionne toujours en régime saturé. Résultat : si Ue "
                "est supérieure à Uref, la sortie vaut plus Vsat ; si Ue "
                "est inférieure à Uref, la sortie vaut moins Vsat."
            )
        ) as tracker:
            self.play(FadeIn(schema))
            self.play(FadeIn(propriete))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(schema), FadeOut(propriete))

        # --- Exemple résolu 1 -------------------------------------------------
        enonce_ex = example_box(
            VGroup(
                Text("On règle Uref = 3 V et Vsat = 14 V.", font_size=20),
                Text("Que vaut Vs si Ue = 5 V ? Et si Ue = 1 V ?", font_size=20),
            ).arrange(DOWN, aligned_edge=LEFT, buff=0.2),
            box_width=9.6,
        )
        enonce_ex.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Exemple résolu. On règle Uref à 3 volts et Vsat à 14 "
                "volts. Que vaut Vs si Ue vaut 5 volts ? Et si Ue vaut 1 "
                "volt ?"
            )
        ) as tracker:
            self.play(FadeIn(enonce_ex))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(enonce_ex))

        corrige = corrige_box(
            VGroup(
                Text("Ue = 5 V > Uref = 3 V  →  Vs = +14 V", font_size=21, color=YELLOW),
                Text("Ue = 1 V < Uref = 3 V  →  Vs = −14 V", font_size=21, color=YELLOW),
            ).arrange(DOWN, aligned_edge=LEFT, buff=0.25),
            box_width=9.6,
        )
        corrige.next_to(titre, DOWN, buff=0.5)

        with self.voiceover(
            text=(
                "Corrigé. Pour Ue égale 5 volts, Ue est supérieure à Uref "
                "qui vaut 3 volts : la sortie bascule à plus 14 volts. "
                "Pour Ue égale 1 volt, Ue est inférieure à Uref : la "
                "sortie bascule à moins 14 volts."
            )
        ) as tracker:
            self.play(FadeIn(corrige))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(corrige))

        # --- À retenir --------------------------------------------------------
        retenir = essentiel_box(
            VGroup(
                Text("À retenir", font_size=24, weight="BOLD"),
                Text("Comparateur = pas de réaction négative → AO saturé.", font_size=20),
                MathTex(r"U_e > U_{ref} \Rightarrow V_s=+V_{sat} \ ; \ U_e < U_{ref} \Rightarrow V_s=-V_{sat}", font_size=23),
            ).arrange(DOWN, buff=0.22),
            box_width=12.0,
        )
        retenir.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Retenons l'essentiel. Un comparateur n'a pas de réaction "
                "négative, donc l'AO est toujours saturé. Si Ue dépasse "
                "Uref, la sortie vaut plus Vsat ; sinon, elle vaut moins "
                "Vsat."
            )
        ) as tracker:
            self.play(FadeIn(retenir))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(retenir))

        # --- Pièges à éviter --------------------------------------------------
        pieges = warning_box(
            VGroup(
                Text("• Ne pas chercher ε = 0 dans un comparateur : en", font_size=19),
                Text("   régime saturé, ε est toujours différent de zéro.", font_size=19),
                Text("• Bien identifier laquelle des deux tensions est sur", font_size=19),
                Text("   E+ et laquelle est sur E− avant de conclure sur", font_size=19),
                Text("   le signe de Vs.", font_size=19),
            ).arrange(DOWN, aligned_edge=LEFT, buff=0.15),
            box_width=12.0,
        )
        pieges.next_to(titre, DOWN, buff=0.4)

        with self.voiceover(
            text=(
                "Deux pièges à éviter. Ne cherchez jamais epsilon égale "
                "zéro dans un comparateur : en régime saturé, epsilon "
                "n'est jamais nul. Et identifiez bien, avant de conclure "
                "sur le signe de Vs, laquelle des deux tensions est "
                "appliquée sur E plus et laquelle est appliquée sur E "
                "moins."
            )
        ) as tracker:
            self.play(FadeIn(pieges))
            self.wait(tracker.get_remaining_duration())

        self.play(FadeOut(pieges), FadeOut(titre))
